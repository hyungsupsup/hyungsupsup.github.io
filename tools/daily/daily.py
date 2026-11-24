"""매일 인사이트 생성기 + 기법 사전 자동 확장.

하루 1회:
  1. 기법 사전(techniques.json)에서 아직 카드가 없는 기법 1개 → notes/techniques/<slug>.md 카드 생성
  2. 어제 arXiv(cs.RO 등) 피지컬 AI 논문 중 1~2편 선정·요약
  3. "기법 × 문제" 조합 질문 1개
  → notes/daily/YYYY-MM-DD.md, 인덱스 갱신, (옵션) git push

사용 (저장소 루트):
  python tools/daily/daily.py run                  # 오늘 것 1회 생성
  python tools/daily/daily.py serve --at 07:30 --push   # 상주: 매일 07:30 실행 (시작 시 '생성 중' 페이지 먼저 push)
  (--cards N: 하루에 기법 카드 N장)
  python tools/daily/daily.py card "LoRA"          # 특정 기법 카드만 생성
  python tools/daily/daily.py saved [--push]       # alphaXiv 북마크 → 즐겨찾기 논문 (serve 중엔 2분마다 자동)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "paper-db"))
from paperdb import ROOT, http_get, llm_chat, load_env, parse_json, yaml_str  # noqa: E402

HERE = Path(__file__).resolve().parent
TECH_DIR = ROOT / "notes" / "techniques"
DAILY_DIR = ROOT / "notes" / "daily"


def daily_path(day) -> Path:
    """데일리는 연-월 폴더로 묶는다: notes/daily/2026-11/2026-11-17.md"""
    d = str(day)
    return DAILY_DIR / d[:7] / f"{d}.md"
CATALOG = json.loads((HERE / "techniques.json").read_text(encoding="utf-8"))


def slugify(name: str) -> str:
    s = re.sub(r"\(.*?\)", "", name).strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def log(msg: str) -> None:
    print(f"[{dt.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


# ---------------------------------------------------------------- 기법 카드
CARD_SYSTEM = """당신은 AI/로보틱스 기법 사전을 **누구나 단번에 이해할 수 있게** 풀어서 쓰는 해설자다.
독자: LLM 에이전트·diffusion·CV는 익숙하지만, 생소한 기법이나 로보틱스·강화학습·최적화 용어는 처음 볼 수 있다.
작성 원칙:
- 교과서식 정의나 현학적인 수식 나열을 피하고, **일상적인 비유 + '무엇이 들어가서 어떻게 바뀐 뒤 무엇이 나오는지'** 흐름으로 쉽게 풀어 쓴다.
- 전문용어·약어가 처음 나오면 반드시 괄호로 쉬운 설명을 붙인다. 예: KV cache(이전에 읽은 단어들의 핵심 정보를 다시 계산하지 않도록 저장해 두는 메모리).
- 복잡한 LaTeX 수식($...$)은 꼭 필요한 경우가 아니면 쓰지 말고 말로 풀어 설명한다.
- 한국어로 쓰되 기술 용어·모델명은 영어 원문 유지. 확신 없는 수치·연도·저자는 쓰지 말거나 '(확인 필요)'를 붙여라.
JSON 하나만 출력:
{"one_liner": "처음 보는 사람도 3초 만에 감을 잡을 수 있는 쉬운 한 줄 정의 (비유 포함 가능)",
 "year_paper": "대표 논문 제목 (연도)",
 "problem": "이 기법이 나오기 전에는 무엇이 왜 불편했고 어떤 한계가 있었나 (쉬운 말로 2~3문장)",
 "core_idea": "비유 1문장 + 실제로 작동하는 원리/단계를 순서대로 쉽게 풀어 설명 (3~4문장)",
 "why_it_works": "기존 방법 대신 이렇게 하면 왜 성능이나 속도가 좋아지는지 직관적 이유 (2~3문장)",
 "tradeoffs": ["실제로 쓸 때 감수해야 할 단점이나 한계 2~3개 (각 1문장, 쉽게)"],
 "predecessors": ["이 기법이 개선한 이전 기법 이름"],
 "successors": ["이 기법을 발전시킨 후속 기법 이름"],
 "robotics_use": ["피지컬 AI(로봇·VLA·월드모델)나 LLM/CV 실전에서 어떻게 쓰이는지 쉬운 예시 2~3개"],
 "idea_hooks": ["이 기법을 다른 문제나 기법과 엮어볼 수 있는 쉬운 아이디어 질문 2~3개"]}"""


def all_techniques() -> list[tuple[str, str]]:
    """(카테고리 이름, 기법) 목록, 카탈로그 순서대로."""
    return [(c["name"], t) for c in CATALOG.values() for items in c["groups"].values() for t in items]


def cat_id_of(category_name: str) -> str:
    return next((k for k, c in CATALOG.items() if c["name"] == category_name), "misc")


def link_if_known(name: str) -> str:
    norm = lambda x: slugify(x).replace("-", "")
    known = {norm(t): slugify(t) for _, t in all_techniques()}
    s = known.get(norm(name))
    return f"[[techniques/{s}|{name}]]" if s else name


def _norm(x: str) -> str:
    return slugify(x).replace("-", "")


ALIAS_MAP: dict[str, str] = {}


def known_technique(name: str) -> str | None:
    """카탈로그에 있으면 카탈로그상의 정식 이름을 반환 (대소문자·하이픈·괄호·별칭 차이 무시)."""
    target = ALIAS_MAP.get(_norm(name), name)
    return {_norm(t): t for _, t in all_techniques()}.get(_norm(target))


def known_technique_cat(name: str) -> tuple[str, str] | None:
    """카탈로그에 있으면 (카테고리 이름, 정식 이름) 반환."""
    target = ALIAS_MAP.get(_norm(name), name)
    return {_norm(t): (cat, t) for cat, t in all_techniques()}.get(_norm(target))


CLASSIFY_SYSTEM = """논문에서 추출된 AI/로봇/ML 기법·방법론 키워드를 기법 사전(techniques.json) 카테고리에 분류한다.

사전의 목적: 연구 아이디어를 구상할 때 **가져다 쓸 수 있는, 유명하고 검증된 모듈·모델·기법**을 모으는 것.
애매하면 무조건 skip. 하루 0개 추가도 정상이다.

규칙:
1. '기존 기법' 목록에 있는 것의 동의어·약어·변형 표기면 새로 만들지 말고 `skip: false`, `name`을 **기존 기법의 정확한 이름**으로 매핑한다. (예: VLA → 기존 이름)
2. 새로 추가하려면 아래를 **모두** 만족해야 한다:
   a. 구체적인 **이름이 붙은** 모듈·아키텍처·알고리즘·학습 기법·모델이다 (예: LoRA, FlashAttention, PPO, DPO, Flow Matching, Diffusion Policy, ACT, CLIP, SAM, DINOv2, ViT, Perceiver, MoE, Speculative Decoding, Chain-of-Thought).
   b. **검증되고 널리 쓰인다**: 출처 논문이 분명하고 많은 후속 연구가 그대로 가져다 쓰거나, 주요 라이브러리(PyTorch, HF Transformers/PEFT/Diffusers, LeRobot 등)에 구현이 있다.
   c. 모델 이름이라면 그 자체가 표준 백본·기준선으로 자리잡은 것만 (예: CLIP, SAM, Llama, OpenVLA, π0). 오늘 논문이 새로 제안한 모델·시스템은 제외.
3. 다음은 skip:
   - 현상·문제·성질·개념 용어 (예: Evaluation Noise, Catastrophic Forgetting, Hallucination, Reward Hacking, Distribution Shift)
   - 연구 분야·과제·패러다임 이름 (예: Continual Learning, Sim-to-Real, Robotics, Embodied AI, Multi-Agent Reasoning)
   - 평가 지표·벤치마크·실험 절차 (예: F1, Score@1, Benchmark Evaluation, Ablation)
   - 막연한 일반 용어 (예: Harness Optimization, Visual Encoder, Memory, Planner, Program Optimization)
   - 데이터 수집 관행 (예: Teleoperation Setup, Egocentric Recording)
   - 개별 논문의 고유 모델·데이터셋·시스템 이름 (예: GPT-6, LIBERO, SWE-CoWork)
4. 통과하면 canonical 영어 이름(`name`), 카테고리 id(`category`, 주어진 목록 중 하나), 세부 분류(`group`, 기존 세부 분류 중 맞는 것 우선, 없으면 새 이름 짧게)를 정한다.

JSON만 출력: {"items": [{"keyword": "입력 그대로", "skip": true, "reason": "짧게 (통과면 출처 논문/라이브러리 근거)", "name": "canonical 이름", "category": "카테고리 id", "group": "세부 분류"}]}"""


def save_catalog() -> None:
    (HERE / "techniques.json").write_text(
        "{\n" + ",\n".join(
            f'  {json.dumps(cid)}: {{\n    "name": {json.dumps(c["name"], ensure_ascii=False)},\n'
            f'    "emoji": {json.dumps(c["emoji"], ensure_ascii=False)},\n    "desc": {json.dumps(c["desc"], ensure_ascii=False)},\n'
            '    "groups": {\n' + ",\n".join(
                f"      {json.dumps(g, ensure_ascii=False)}: {json.dumps(ts, ensure_ascii=False)}" for g, ts in c["groups"].items()
            ) + "\n    }\n  }"
            for cid, c in CATALOG.items()
        ) + "\n}\n",
        encoding="utf-8",
    )


def add_new_techniques(keywords: list[str], max_new: int | None = None, notes: dict[str, dict] | None = None) -> list[str]:
    """논문에서 추출된 키워드 중:
    1) 카탈로그에 없는 키워드는 LLM으로 분류해 techniques.json에 추가(동의어는 기존 기법으로 매핑)하고,
    2) 논문 키워드에 해당하는 모든 기법 중 아직 마크다운 카드(.md)가 없는 것은 카드를 생성한다."""
    cand = []
    for k in keywords:
        k = k.strip()
        if k and not known_technique(k) and _norm(k) not in {_norm(c) for c in cand}:
            cand.append(k)

    alias_map: dict[str, str] = {}
    added: list[tuple[str, str]] = []
    if cand:
        cats = {cid: {"name": c["name"], "groups": list(c["groups"])} for cid, c in CATALOG.items()}
        existing = ", ".join(t for _, t in all_techniques())
        for i in range(0, len(cand), 8):
            batch = cand[i:i + 8]
            try:
                j = parse_json(llm_chat(
                    CLASSIFY_SYSTEM,
                    f"카테고리: {json.dumps(cats, ensure_ascii=False)}\n\n기존 기법: {existing}\n\n키워드: {json.dumps(batch, ensure_ascii=False)}",
                ))
            except Exception as e:
                log(f"새 기법 분류 실패: {e}")
                continue
            for it in j.get("items", []):
                kw = (it.get("keyword") or "").strip()
                name = (it.get("name") or "").strip()
                cid = it.get("category")
                if it.get("skip") or not name:
                    continue
                if kw:
                    alias_map[_norm(kw)] = name
                if known_technique(name):
                    alias_map[_norm(kw)] = known_technique(name)  # 기존 기법으로 정규화
                    continue
                if cid not in CATALOG:
                    continue
                group = (it.get("group") or "기타").strip()
                CATALOG[cid]["groups"].setdefault(group, []).append(name)
                added.append((CATALOG[cid]["name"], name))

    if added:
        save_catalog()
        log(f"기법 사전에 새 기법 {len(added)}개 추가: {', '.join(n for _, n in added)}")

    ALIAS_MAP.update(alias_map)
    # notes가 주어졌으면 키워드 표기를 카탈로그 정식 이름으로 정규화
    if notes and alias_map:
        for pk in notes.values():
            if "keywords" in pk:
                pk["keywords"] = [alias_map.get(_norm(k), k) for k in pk["keywords"]]

    # 오늘 논문에 등장한 키워드(기존 기법 + 신규 추가 기법 모두) 중 아직 .md 카드가 없는 것은 모두 생성
    to_make: list[tuple[str, str]] = []
    seen_norm: set[str] = set()
    for k in keywords:
        mapped = alias_map.get(_norm(k), k.strip())
        hit = known_technique_cat(mapped)
        if hit and _norm(hit[1]) not in seen_norm:
            seen_norm.add(_norm(hit[1]))
            if not (TECH_DIR / f"{slugify(hit[1])}.md").exists():
                to_make.append(hit)

    created = []
    for cat, name in to_make[:max_new]:
        try:
            make_card(name, cat)
            created.append(name)
        except Exception as e:
            log(f"카드 생성 실패 {name}: {e}")
    return created


def make_card(name: str, category: str) -> Path:
    path = TECH_DIR / f"{slugify(name)}.md"
    # LLM이 문자열 안에 따옴표를 그대로 넣어 JSON이 깨지는 경우가 있어 한 번 더 요청한다
    for attempt in range(3):
        try:
            hint = "" if attempt == 0 else "\n\n(주의: 반드시 유효한 JSON. 문자열 안의 큰따옴표는 \\\" 로 이스케이프하거나 작은따옴표를 쓸 것)"
            j = parse_json(llm_chat(CARD_SYSTEM, f"기법: {name}\n분류: {category}{hint}"))
            break
        except ValueError as e:  # json.JSONDecodeError 포함
            log(f"카드 JSON 파싱 실패 {name} ({attempt + 1}회차): {e}")
            if attempt == 2:
                raise
    bullets = lambda xs: "\n".join(f"- {x}" for x in xs) or "- (없음)"
    links = lambda xs: "\n".join(f"- {link_if_known(x)}" for x in xs) or "- (없음)"
    path.write_text(
        f"""---
title: {yaml_str(name)}
date: {dt.date.today()}
tags: [technique, {cat_id_of(category)}]
category: {yaml_str(category)}
status: draft
---

> {j.get('one_liner', '')}

**대표 논문**: {j.get('year_paper', '(확인 필요)')} · **분류**: {category}

## 해결한 문제
{j.get('problem', '')}

## 핵심 아이디어
{j.get('core_idea', '')}

## 왜 작동하나
{j.get('why_it_works', '')}

## 트레이드오프
{bullets(j.get('tradeoffs', []))}

## 계보
**이전**
{links(j.get('predecessors', []))}

**이후**
{links(j.get('successors', []))}

## 피지컬 AI에서의 쓰임
{bullets(j.get('robotics_use', []))}

## 💡 아이디어 훅
{bullets(j.get('idea_hooks', []))}

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
""",
        encoding="utf-8",
    )
    log(f"카드 생성: {path.relative_to(ROOT)}")
    return path


def next_technique() -> tuple[str, str] | None:
    for cat, t in all_techniques():
        if not (TECH_DIR / f"{slugify(t)}.md").exists():
            return cat, t
    return None


def card_summary(slug: str) -> str:
    p = TECH_DIR / f"{slug}.md"
    if not p.exists():
        return ""
    m = re.search(r"^> (.*)$", p.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else ""


def html_escape(x: str) -> str:
    return x.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def strip_math(x: str) -> str:
    return re.sub(r"\$[^$]*\$", "…", x)


COVERS = ["mh-c1", "mh-c2", "mh-c3", "mh-c4", "mh-c5", "mh-c6", "mh-c7", "mh-c8", "mh-c9"]


def write_tech_index() -> None:
    """기법 사전 목차(카테고리 카드) + 카테고리별 페이지(세부 분류별 기법 카드) 생성."""
    cat_dir = TECH_DIR / "category"
    cat_dir.mkdir(parents=True, exist_ok=True)
    today = dt.date.today()

    total = done_total = 0
    cards = []
    for i, (cid, c) in enumerate(CATALOG.items()):
        items = [t for g in c["groups"].values() for t in g]
        done = sum((TECH_DIR / f"{slugify(t)}.md").exists() for t in items)
        total += len(items)
        done_total += done
        preview = " · ".join(items[:5]) + (" …" if len(items) > 5 else "")
        cards.append(
            f'<a class="mh-card internal" href="/techniques/category/{cid}">'
            f'<div class="mh-cover {COVERS[i % len(COVERS)]}">{c["emoji"]}</div>'
            f'<div class="mh-body"><h3>{html_escape(c["name"])}</h3><p>{html_escape(c["desc"])}</p>'
            f'<p class="mh-preview">{html_escape(preview)}</p>'
            f'<div class="mh-meta">{len(c["groups"])}개 세부 분류 · {done}/{len(items)} 작성</div></div></a>'
        )

        # ---- 카테고리 페이지 ----
        sections = []
        for gname, techs in c["groups"].items():
            tcards = []
            for t in techs:
                slug = slugify(t)
                summ = strip_math(card_summary(slug))
                if summ:
                    tcards.append(
                        f'<a class="tc-card internal" href="/techniques/{slug}"><h4>{html_escape(t)}</h4>'
                        f'<p>{html_escape(summ)}</p><span class="tc-badge">초안</span></a>'
                    )
                else:
                    tcards.append(
                        f'<div class="tc-card tc-todo"><h4>{html_escape(t)}</h4>'
                        f'<p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div>'
                    )
            sections.append(
                f'<div class="mh-section"><span>{html_escape(gname)}</span></div>\n'
                f'<div class="tc-grid">{"".join(tcards)}</div>'
            )
        (cat_dir / f"{cid}.md").write_text(
            f"---\ntitle: {yaml_str(c['emoji'] + ' ' + c['name'])}\ndate: {today}\ntags: [technique-category]\n---\n\n"
            f'<p class="tc-lead">{html_escape(c["desc"])}</p>\n'
            + "\n".join(sections) + "\n\n[[techniques/index|← 기법 사전 전체]]\n",
            encoding="utf-8",
        )

    (cat_dir / "index.md").write_text(
        f"---\ntitle: 카테고리\ndate: {today}\ntags: [index]\n---\n\n"
        f'<div class="mh-grid">{"".join(cards)}</div>\n',
        encoding="utf-8",
    )
    (TECH_DIR / "index.md").write_text(
        f"---\ntitle: 기법 사전\ndate: {today}\ntags: [index]\n---\n\n"
        f'<p class="tc-lead">아이디어 구상용 AI 기법·모듈·모델 정리. 카드마다 '
        f"<b>해결한 문제 → 핵심 아이디어 → 트레이드오프 → 계보 → 피지컬 AI 쓰임 → 💡 아이디어 훅</b>. "
        f"매일 1개씩 자동으로 초안이 추가된다 ({done_total}/{total} 작성).</p>\n"
        f'<div class="mh-section"><span>카테고리</span></div>\n'
        f'<div class="mh-grid">{"".join(cards)}</div>\n',
        encoding="utf-8",
    )


# ---------------------------------------------------------------- arXiv
ARXIV_QUERY = ("(cat:cs.RO OR cat:cs.CV OR cat:cs.LG OR cat:cs.AI) AND "
               "(abs:robot OR abs:\"vision-language-action\" OR abs:\"world model\" OR abs:manipulation "
               "OR abs:\"embodied\" OR abs:\"imitation learning\" OR abs:\"diffusion policy\")")
NS = {"a": "http://www.w3.org/2005/Atom"}


def fetch_arxiv(n: int = 60) -> list[dict]:
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": ARXIV_QUERY, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": n})
    root = ET.fromstring(http_get(url))
    out = []
    for e in root.findall("a:entry", NS):
        out.append({
            "id": e.findtext("a:id", "", NS).rsplit("/", 1)[-1],
            "title": " ".join(e.findtext("a:title", "", NS).split()),
            "abstract": " ".join(e.findtext("a:summary", "", NS).split()),
            "published": e.findtext("a:published", "", NS)[:10],
        })
    return out


def fetch_hf_daily_papers(limit: int = 30) -> list[dict]:
    """Hugging Face Daily Papers에서 추천수 상위 AI/ML/CV/로봇 논문을 가져온다."""
    raw = http_get("https://huggingface.co/api/daily_papers")
    items = json.loads(raw)
    out = []
    for item in items:
        p = item.get("paper") or {}
        pid = p.get("id")
        title = " ".join((p.get("title") or "").split())
        abstract = " ".join((p.get("summary") or "").split())
        if not pid or not title:
            continue
        out.append({
            "id": pid,
            "title": title,
            "abstract": abstract,
            "published": (p.get("publishedAt") or "")[:10],
            "upvotes": item.get("upvotes") or p.get("upvotes") or 0,
        })
    out.sort(key=lambda x: x["upvotes"], reverse=True)
    return out[:limit]


ARXIV_ID = re.compile(r"\d{4}\.\d{4,5}(v\d+)?")


def alphaxiv_call(tool: str, args: dict) -> dict | None:
    """alphaXiv MCP(Streamable HTTP) 도구 호출 → 결과 텍스트를 JSON으로. 키가 없으면 None."""
    api_key = os.environ.get("ALPHAXIV_API_KEY", "").strip()
    if not api_key:
        log("ALPHAXIV_API_KEY 미설정 — alphaXiv 건너뜀")
        return None
    req = urllib.request.Request(
        "https://api.alphaxiv.org/mcp/v1",
        data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                         "params": {"name": tool, "arguments": args}}).encode("utf-8"),
        headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
                 "Authorization": f"Bearer {api_key}", "User-Agent": "Mozilla/5.0"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8")
    # Streamable HTTP는 SSE(data: {...}) 또는 일반 JSON으로 응답할 수 있음
    data_line = next((ln[5:].strip() for ln in body.splitlines() if ln.startswith("data:")), body)
    res = json.loads(data_line)
    if res.get("error"):
        raise RuntimeError(f"alphaXiv {tool}: {res['error']}")
    content = (res.get("result") or {}).get("content") or []
    text = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
    try:
        return json.loads(text)
    except Exception:
        raise RuntimeError(f"alphaXiv {tool}: JSON 아닌 응답 {text[:200]}")


def arxiv_lookup(ids: list[str]) -> dict[str, dict]:
    """arXiv ID 목록 → {버전 뗀 id: {id, title, abstract, published}}. 비-arXiv ID는 무시(섞이면 arXiv가 400)."""
    ids = [i for i in ids if ARXIV_ID.fullmatch(i)]
    found: dict[str, dict] = {}
    for k in range(0, len(ids), 50):
        chunk = ids[k:k + 50]
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(chunk), "max_results": len(chunk)})
        root = ET.fromstring(http_get(url))
        for e in root.findall("a:entry", NS):
            pid = re.sub(r"v\d+$", "", e.findtext("a:id", "", NS).rsplit("/", 1)[-1])
            found[pid] = {
                "id": pid,
                "title": " ".join(e.findtext("a:title", "", NS).split()),
                "abstract": " ".join(e.findtext("a:summary", "", NS).split()),
                "published": e.findtext("a:published", "", NS)[:10],
            }
    return found


def fetch_alphaxiv_papers(limit: int = 10) -> list[dict]:
    """alphaXiv hot feed 상위 논문을 인기 순서 그대로 가져온다."""
    items = alphaxiv_call("get_hot_feed", {"limit": limit * 2})  # 비-arXiv 슬러그를 거른 뒤에도 limit편이 남도록
    if not items:
        return []
    if isinstance(items, dict):
        items = items.get("papers") or items.get("results") or []
    ids = [re.sub(r"v\d+$", "", str(p.get("universal_paper_id") or p.get("id") or "")) for p in items]
    ids = [i for i in ids if ARXIV_ID.fullmatch(i)][:limit]
    found = arxiv_lookup(ids)
    # arXiv 응답 순서는 보장되지 않으므로 hot feed 순서(인기순)로 재정렬
    out = [dict(found[i], source="alphaXiv") for i in ids if i in found][:limit]
    for rank, p in enumerate(out, 1):
        p["rank"] = rank
    return out


def fetch_papers(n: int = 10) -> tuple[list[dict], list[dict]]:
    """(HF 추천수 상위 n편, alphaXiv hot feed 상위 n편). 둘 다 실패하면 HF 자리에 arXiv 최신 논문."""
    hf, ax = [], []
    try:
        hf = fetch_hf_daily_papers(limit=n)
        for p in hf:
            p["source"] = "HF"
    except Exception as e:
        log(f"HF Daily Papers 조회 실패: {e}")
    try:
        ax = fetch_alphaxiv_papers(limit=n)
    except Exception as e:
        log(f"alphaXiv 조회 실패: {e}")
    if not hf and not ax:
        log("외부 인기 논문 조회 실패, arXiv로 폴백")
        hf = [dict(p, source="arXiv") for p in fetch_arxiv()[:n]]
    return hf, ax


EXPLAIN_SYSTEM = """당신은 로보틱스·피지컬 AI **입문자**에게 오늘의 인기 논문을 풀어 설명한다.
독자: 로봇·강화학습·제어는 거의 모름. 대신 LLM 에이전트(도구 호출, ReAct 루프, RAG)와 diffusion·컴퓨터 비전은 잘 앎.
규칙:
- 주어진 논문 **전부**를 빠짐없이 설명한다. 고르거나 빼지 않는다. 목록 자체에 대한 메타 코멘트 금지.
- 본문(oneline/background/claim/connect/question)에는 괄호 용어 설명을 넣지 않는다. 대신 쉬운 말로 풀어 쓰고, 꼭 필요한 전문용어만 영어 그대로 쓴다.
- 본문에 나온 전문용어는 전부 glossary에 모아 입문자용으로 풀이한다. policy, DAgger, LIBERO, drift 같은 로봇·RL 기본 용어도 빠뜨리지 않는다. 풀이는 비유나 예시를 섞어 1문장. 예: {"term": "policy", "desc": "카메라 영상과 센서 값을 보고 '다음에 팔을 어떻게 움직일지'를 바로 출력하는 로봇 제어 모델"}.
- glossary는 최대 6개. 독자가 이미 아는 것(LLM·agent·tool call·ReAct·RAG·diffusion·CV 용어, training/model 같은 일반 단어)과 논문 고유 시스템명은 넣지 않는다. 로봇·RL·제어·벤치마크 용어 위주로 고른다.
- 본문의 각 칸에는 영어 전문용어를 최대 3개까지만 쓴다. 나머지는 한국어로 풀어 쓴다 (예: 'feedback channel' → '동작을 고쳐 주는 신호').
- 한 문장에는 아이디어 하나만. 수치는 가장 중요한 것 최대 3개, 'A → B' 형태로 무엇을 비교했는지 밝힌다.
- 논문마다 [초록]과 (있으면) [결론]이 주어진다. 결론에 나온 실제 결과·한계·향후 과제를 '주장'과 '생각해 볼 질문'에 적극 반영한다.
- 주어진 초록·결론에 없는 수치·사실을 지어내지 않는다.
- 한국어, 기술 용어는 영어 원문 유지. 수식 기호($) 쓰지 말 것.
JSON만 출력:
{"papers": [{"id": "주어진 id 그대로",
  "oneline": "한 줄: 비유나 질문 형태로, 처음 보는 사람도 바로 감 잡게 (1문장)",
  "background": "배경: 이 논문 전에는 보통 어떻게 했고 무엇이 불편/한계였나 (1~2문장)",
  "claim": "이 논문의 주장: 핵심 구조를 먼저 한 문장, 결과를 다음 문장 (2~3문장)",
  "connect": "내가 아는 것과의 연결: LLM 에이전트·diffusion·CV 중 가장 가까운 개념에 빗대기 (1문장)",
  "question": "생각해 볼 질문: 이 논문이 열어 둔 갈림길이나 후속 연구 아이디어. 논문을 안 읽은 사람도 이해할 수 있게 (1문장)",
  "glossary": [{"term": "본문에 나온 전문용어", "desc": "입문자용 쉬운 풀이 1문장"}],
  "keywords": ["이 논문을 이해하는 데 핵심인 기법·모듈·방법론 2~4개. 널리 쓰이는 영어 정식 이름으로(예: Flow Matching, LoRA, Diffusion Policy). 기법 목록에 같은 것이 있으면 그 표기를 그대로. 논문 고유 시스템명·너무 일반적인 단어 제외"]}]}"""


PICK_SYSTEM = """당신은 AI/피지컬 AI 연구자의 아침 브리핑을 쓴다. 독자: 로봇 입문자, LLM 에이전트·diffusion은 잘 앎.
오늘의 논문 한 줄 요약들을 보고 전체 흐름과 연구 아이디어 질문을 써라. 한국어, 기술 용어는 영어. JSON만 출력:
{"trend": "오늘 목록 전체에서 보이는 흐름 1~2문장",
 "question": "'기법 X × 문제 Y' 형태의 구체적 연구 아이디어 질문 1개 (오늘의 기법과 논문을 엮을 것)",
 "question_note": "그 질문이 왜 열려 있는지, 첫 실험은 무엇일지 2문장"}"""


# ---------------------------------------------------------------- 논문 해설 · 카드
_SEC_H2 = re.compile(r'<h2 class="ltx_title ltx_title_section"[^>]*>(.*?)</h2>', re.S)
_CONCL_NAMES = [r"conclusions?", r"concluding remarks", r"summary", r"discussion"]  # 앞쪽일수록 우선


def fetch_conclusion(pid: str, limit: int = 2500) -> str:
    """arXiv HTML 버전(arxiv.org/html/<id>)에서 결론 섹션 본문을 뽑는다. HTML이 없거나 못 찾으면 빈 문자열."""
    import html as _html
    try:
        req = urllib.request.Request(f"https://arxiv.org/html/{pid}", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            page = r.read().decode("utf-8", "replace")
    except Exception:
        return ""
    heads = [(m.start(), m.end(), re.sub(r"<[^>]+>", "", m.group(1))) for m in _SEC_H2.finditer(page)]
    pick = None
    for pat in _CONCL_NAMES:
        hits = [h for h in heads if re.search(rf"^\W*[\dA-Z.]*\s*{pat}\b", h[2].strip(), re.I)]
        if hits:
            pick = hits[-1]
            break
    if not pick:
        return ""
    nxt = [h[0] for h in heads if h[0] > pick[0]]
    end = min([page.find('<section class="ltx_bibliography"', pick[1]) % (len(page) + 1)] + nxt + [len(page)])
    body = page[pick[1]:end]
    body = re.sub(r'<math[^>]*alttext="([^"]*)"[^>]*>.*?</math>', r" \1 ", body, flags=re.S)  # 수식은 LaTeX 원문으로
    body = re.sub(r"<(script|style|figure|table)[^>]*>.*?</\1>", " ", body, flags=re.S)
    text = " ".join(_html.unescape(re.sub(r"<[^>]+>", " ", body)).split())
    return text[:limit]


def explain_papers(papers: list[dict]) -> dict[str, dict]:
    """논문 목록 → {id: 입문자용 해설(oneline/background/claim/connect/question/keywords)}. 5편씩 나눠 요청."""
    names = ", ".join(t for _, t in all_techniques())
    notes: dict[str, dict] = {}

    # 초록만으로는 너무 간추려져서 결론 섹션도 같이 준다 (arXiv HTML이 없으면 초록만)
    for p in papers:
        if "conclusion" not in p:
            p["conclusion"] = fetch_conclusion(p["id"])
    log(f"결론 섹션 확보: {sum(bool(p['conclusion']) for p in papers)}/{len(papers)}편")

    def ask(batch: list[dict]) -> None:
        listing = "\n\n".join(
            f"### {p['id']} | {p['title']}\n[초록] {p['abstract'][:1500]}"
            + (f"\n[결론] {p['conclusion']}" if p.get("conclusion") else "")
            for p in batch
        )
        jb = parse_json(llm_chat(EXPLAIN_SYSTEM, f"기법 목록: {names}\n\n논문:\n{listing}"))
        notes.update({str(pk.get("id")): pk for pk in jb.get("papers", [])})

    for i in range(0, len(papers), 5):
        batch = papers[i:i + 5]
        # 5편 묶음 → 실패하면 30초 쉬고 한 번 더 → 그래도 실패하면 1편씩 (응답이 짧아 타임아웃에 덜 걸림)
        for attempt in range(2):
            try:
                ask(batch)
                break
            except Exception as e:
                log(f"논문 해설 실패({i}~, {attempt + 1}회차): {e}")
                time.sleep(30)
        else:
            for p in batch:
                try:
                    ask([p])
                except Exception as e:
                    log(f"논문 해설 최종 실패 {p['id']}: {e}")
        missing = [p["id"] for p in batch if p["id"] not in notes]
        if missing:
            log(f"해설 누락 {len(missing)}편: {', '.join(missing)}")
    return notes


def tech_link(name: str, new_techs=()) -> str:
    canon = known_technique(name)
    if canon and (TECH_DIR / f"{slugify(canon)}.md").exists():
        new = " dp-new" if canon in new_techs else ""
        return f'<a class="internal dp-tech{new}" href="/techniques/{slugify(canon)}">{html_escape(name)}</a>'
    return f'<span class="dp-tech">{html_escape(name)}</span>'


def render_card(p: dict, pk: dict, badge: str = "", new_techs=(), saved: bool = False) -> str:
    """논문 카드 HTML. 데일리와 즐겨찾기 페이지가 같이 쓴다."""
    esc = lambda x: html_escape(strip_math(str(x or "")))

    def row(icon: str, label: str, text: str, cls: str = "") -> str:
        lab = f"<b>{label}</b>" if label else ""
        return f'<div class="dp-row {cls}"><span class="dp-ic">{icon}</span><div>{lab}{text}</div></div>'

    title = f'<a class="dp-title external" href="https://arxiv.org/abs/{p["id"]}">{html_escape(p["title"])}</a>'
    parts = [row("📄", "", title, "dp-trow")]
    if pk.get("oneline"):
        parts.append(row("💡", "", esc(pk["oneline"]), "dp-one"))
    for icon, label, k in [("🕰️", "배경", "background"), ("🎯", "이 논문의 주장", "claim"),
                           ("🔗", "내가 아는 것과의 연결", "connect"), ("❓", "생각해 볼 질문", "question")]:
        if pk.get(k):
            parts.append(row(icon, label, esc(pk[k])))
    gl = [g for g in pk.get("glossary") or [] if isinstance(g, dict) and g.get("term")]
    if gl:
        items = "".join(f'<li><b>{esc(g["term"])}</b>: {esc(g.get("desc", ""))}</li>' for g in gl)
        parts.append(row("📖", "용어 풀이", f'<ul class="dp-gloss">{items}</ul>'))
    if not pk:
        parts.append(row("📝", "초록", esc(p.get("abstract", "")[:400]) + "…"))
    techs = " ".join(tech_link(t, new_techs) for t in pk.get("keywords", []))
    if techs:
        parts.append(row("🏷️", "", f'<div class="dp-techs">{techs}</div>'))
    # alphaXiv에서 북마크하면 다음 동기화 때 즐겨찾기 논문으로 들어온다
    star = ('<span class="dp-star on">⭐ 담음</span>' if saved else
            f'<a class="dp-star external" href="https://www.alphaxiv.org/abs/{p["id"]}" title="alphaXiv에서 북마크하면 즐겨찾기 논문에 추가">☆ 담기</a>')
    return (
        f'<div class="dp-card"><div class="dp-top"><span class="dp-badge">{badge}</span>'
        f'<span class="dp-id">arXiv:{p["id"]}</span>{star}</div>' + "".join(parts) + "</div>"
    )


# ---------------------------------------------------------------- 즐겨찾기 (alphaXiv 북마크 동기화)
SAVED_DB = HERE / "saved.json"
SAVED_DIR = ROOT / "notes" / "knowledge" / "saved"
SAVED_SYNC_SEC = 120  # serve가 alphaXiv 북마크를 확인하는 주기


def load_saved() -> dict[str, dict]:
    return json.loads(SAVED_DB.read_text(encoding="utf-8")) if SAVED_DB.exists() else {}


def fetch_bookmarks() -> dict[str, list[str]] | None:
    """alphaXiv 라이브러리의 모든 폴더(내 논문 폴더 제외) → {arXiv id: [폴더 이름]}. 실패 시 None."""
    lib = alphaxiv_call("list_library", {"include_papers": True})
    if lib is None:
        return None
    out: dict[str, list[str]] = {}
    for f in lib.get("folders", []):
        if f.get("type") == "default-publications":
            continue
        if f.get("papers_truncated"):
            log(f"[!] alphaXiv 폴더 '{f.get('name')}' 논문 목록이 잘려서 일부만 동기화됨")
        for p in f.get("papers", []):
            pid = re.sub(r"v\d+$", "", str(p.get("id") or p.get("universal_paper_id") or ""))
            if ARXIV_ID.fullmatch(pid):
                out.setdefault(pid, []).append(f.get("name", ""))
    return out


def sync_saved() -> bool:
    """alphaXiv 북마크 ↔ saved.json 동기화 후 즐겨찾기 페이지 생성. 변경이 있었으면 True."""
    load_env()
    try:
        marks = fetch_bookmarks()
    except Exception as e:
        log(f"alphaXiv 북마크 조회 실패: {e}")
        return False
    if marks is None:
        return False
    db = load_saved()
    changed = False
    for pid in [k for k in db if k not in marks]:  # alphaXiv에서 북마크를 지우면 여기서도 뺀다
        log(f"즐겨찾기 해제: {db[pid]['title']}")
        del db[pid]
        changed = True
    for pid, folders in marks.items():
        if pid in db and db[pid].get("folders") != folders:
            db[pid]["folders"] = folders
            changed = True
    new_ids = [pid for pid in marks if pid not in db]
    if new_ids:
        meta = arxiv_lookup(new_ids)
        papers = [meta[i] for i in new_ids if i in meta]
        notes = explain_papers(papers)
        add_new_techniques([k for pk in notes.values() for k in pk.get("keywords", [])], notes=notes)
        today = str(dt.date.today())
        for p in papers:
            db[p["id"]] = dict(p, saved=today, folders=marks[p["id"]], note=notes.get(p["id"], {}))
            log(f"즐겨찾기 추가: {p['title']}")
        changed = True
    if changed:
        SAVED_DB.write_text(json.dumps(db, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        write_tech_index()
    write_saved_pages(db)
    return changed


def write_saved_pages(db: dict[str, dict] | None = None) -> None:
    """즐겨찾기 목차(연-월 카드) + 월별 페이지(논문 카드) 생성."""
    db = load_saved() if db is None else db
    SAVED_DIR.mkdir(parents=True, exist_ok=True)
    by_month: dict[str, list[dict]] = {}
    for p in db.values():
        by_month.setdefault(p["saved"][:7], []).append(p)
    for old in SAVED_DIR.glob("????-??.md"):
        if old.stem not in by_month:
            old.unlink()
    today = dt.date.today()
    for ym, items in by_month.items():
        items.sort(key=lambda x: (x["saved"], x["id"]), reverse=True)
        y, m = ym.split("-")
        cards = "".join(render_card(p, p.get("note", {}), f'⭐ {p["saved"][5:].replace("-", "/")}', saved=True) for p in items)
        (SAVED_DIR / f"{ym}.md").write_text(
            f"---\ntitle: {y}년 {int(m)}월 즐겨찾기\ndate: {today}\ntags: [saved]\n---\n\n"
            f'<p class="tc-lead">{y}년 {int(m)}월에 담은 논문 {len(items)}편. 최근에 담은 순.</p>\n'
            f'<div class="dp-src dp-sv"><div class="dp-saved-grid">{cards}</div></div>\n',
            encoding="utf-8",
        )
    months = sorted(by_month, reverse=True)
    if months:
        grid = "".join(
            f'<a class="mh-card internal" href="/knowledge/saved/{ym}"><div class="mh-cover {COVERS[k % len(COVERS)]}">⭐</div>'
            f'<div class="mh-body"><h3>{ym[:4]}년 {int(ym[5:])}월</h3>'
            f'<p>{html_escape(" · ".join(p["title"] for p in sorted(by_month[ym], key=lambda x: x["saved"], reverse=True)[:3]))}</p>'
            f'<div class="mh-meta">{len(by_month[ym])}편</div></div></a>'
            for k, ym in enumerate(months)
        )
        body = f'<div class="mh-grid">{grid}</div>'
    else:
        body = '<p class="dp-row">아직 담은 논문이 없습니다. 데일리 카드의 ☆ 담기 → alphaXiv에서 북마크하세요.</p>'
    (SAVED_DIR / "index.md").write_text(
        f"---\ntitle: 즐겨찾기 논문\ndate: {today}\ntags: [index]\n---\n\n"
        '<p class="tc-lead">데일리에서 <b>☆ 담기</b>를 누르고 alphaXiv에서 북마크한 논문. '
        f"담고 몇 분 안에 들어오고, 북마크를 지우면 여기서도 빠집니다. 총 {len(db)}편.</p>\n"
        '<div class="mh-section"><span>월별</span></div>\n' + body + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------- daily
GENERATING_MARK = "generating: true"


def is_generating(path: Path) -> bool:
    return path.exists() and GENERATING_MARK in path.read_text(encoding="utf-8")[:300]


def write_daily_index(day: dt.date) -> None:
    days = sorted((p.stem for p in DAILY_DIR.glob("????-??/????-??-??.md")), reverse=True)
    item = lambda d: f"- [[daily/{d[:7]}/{d}|{d}]]" + (" — ⏳ 생성 중" if is_generating(daily_path(d)) else "")
    months: dict[str, list[str]] = {}
    for d in days:
        months.setdefault(d[:7], []).append(d)
    body = "\n\n".join(f"## {ym[:4]}년 {int(ym[5:])}월\n" + "\n".join(item(d) for d in ds) for ym, ds in months.items())
    (DAILY_DIR / "index.md").write_text(
        "---\ntitle: 데일리 인사이트\ndate: " + str(day) + "\ntags: [index]\n---\n\n"
        "매일 아침 자동 생성: 오늘의 기법 카드 · 인기 논문 해설(HF · alphaXiv) · 아이디어 질문.\n\n"
        + body + "\n",
        encoding="utf-8",
    )


def write_placeholder(day: dt.date) -> None:
    """생성 시작을 알리는 임시 페이지. 생성이 끝나면 실제 데일리로 덮어쓴다."""
    daily_path(day).parent.mkdir(parents=True, exist_ok=True)
    daily_path(day).write_text(
        f"---\ntitle: {day} 데일리\ndate: {day}\ntags: [daily]\n{GENERATING_MARK}\n---\n\n"
        '<div class="dp-wait"><div class="dp-spin"></div><div><b>오늘의 데일리를 만드는 중입니다</b>'
        f"<p>{dt.datetime.now():%H:%M}에 시작했어요. 논문 20편 해설과 기법 카드 생성에 보통 10~20분 걸립니다. "
        "잠시 후 새로고침해 주세요.</p></div></div>\n",
        encoding="utf-8",
    )
    write_daily_index(day)


def run_daily(day: dt.date, push: bool, cards: int = 1) -> Path:
    load_env()
    TECH_DIR.mkdir(parents=True, exist_ok=True)
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    if push:  # 사이트에 '생성 중' 표시를 먼저 올린다
        write_placeholder(day)
        git_push(f"daily: {day} 생성 시작")

    nxt = next_technique()
    tech_md = "기법 사전의 모든 항목이 작성됨 — `techniques.json`에 새 기법을 추가하세요."
    tech_name = None
    for _ in range(cards - 1):  # 추가 카드 (데일리에는 첫 장만 소개)
        extra = next_technique()
        if extra:
            make_card(extra[1], extra[0])
    nxt = next_technique() if cards > 1 else nxt
    if nxt:
        cat, tech_name = nxt
        p = make_card(tech_name, cat)
        one = re.search(r"^> (.*)$", p.read_text(encoding="utf-8"), re.M)
        tech_md = f"**[[techniques/{slugify(tech_name)}|{tech_name}]]** ({cat})\n\n> {one.group(1) if one else ''}"
    write_tech_index()

    hf, ax = fetch_papers()
    log(f"인기 논문 조회: HF {len(hf)}편, alphaXiv {len(ax)}편")
    # 두 출처에 같은 논문이 있으면 LLM에는 한 번만 보낸다 (화면에는 양쪽 열에 모두 표시)
    uniq = list({p["id"]: p for p in hf + ax}.values())
    notes = explain_papers(uniq)
    # 논문 키워드 중 기법 사전에 없는 것은 자동 추가 + 아직 카드(.md)가 없는 기법은 모두 카드 생성
    new_techs = add_new_techniques([k for pk in notes.values() for k in pk.get("keywords", [])], notes=notes)
    write_tech_index()
    digest = "\n".join(f"- {p['title']}: {notes.get(p['id'], {}).get('oneline', '')}" for p in uniq)
    j = parse_json(llm_chat(PICK_SYSTEM, f"오늘의 기법: {tech_name}\n\n오늘의 논문:\n{digest}"))

    saved_ids = set(load_saved())

    def paper_card(p: dict) -> str:
        badge = f'▲ {p["upvotes"]}' if p["source"] == "HF" else (f'#{p["rank"]}' if p.get("rank") else "")
        return render_card(p, notes.get(p["id"], {}), badge, new_techs, saved=p["id"] in saved_ids)

    def column(cls: str, icon: str, name: str, sub: str, items: list[dict]) -> str:
        cards_html = "".join(paper_card(p) for p in items) or '<p class="dp-row">오늘은 가져오지 못함</p>'
        return (
            f'<div class="dp-src {cls}"><div class="dp-head"><span class="dp-logo">{icon}</span>'
            f'<span class="dp-name">{name}</span><span class="dp-subt">{sub}</span></div>'
            f'<div class="dp-list">{cards_html}</div></div>'
        )

    hf_label = "Hugging Face Daily Papers" if not hf or hf[0]["source"] == "HF" else "arXiv 최신 (폴백)"
    papers_section = (
        '<div class="dp-cols">'
        + column("dp-hf", "🤗", hf_label, "추천수 순 Top 10", hf)
        + column("dp-ax", "🔬", "alphaXiv Hot", "인기 순 Top 10", ax)
        + "</div>\n"
    ) if hf or ax else "(논문 조회 실패)"

    path = daily_path(day)
    path.write_text(
        f"""---
title: {day} 데일리
date: {day}
tags: [daily]
---

## 🧩 오늘의 기법
{tech_md}

## 📄 오늘의 논문
{papers_section}

## 📈 흐름
{j.get('trend', '')}

## 💡 오늘의 질문
**{j.get('question', '')}**

{j.get('question_note', '')}

> 좋은 질문이면 [[open-questions]]로 옮기기.
""",
        encoding="utf-8",
    )
    log(f"데일리 생성: {path.relative_to(ROOT)}")

    write_daily_index(day)
    if push:
        git_push(f"daily: {day}")
    return path


def git_push(msg: str) -> None:
    def sh(*cmd):
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            log(f"[!] {' '.join(cmd)}: {r.stderr.strip()[:300]}")
        return r.returncode == 0
    sh("git", "add", "notes/daily", "notes/techniques", "notes/knowledge/saved",
       "tools/daily/techniques.json", "tools/daily/saved.json")
    sh("git", "commit", "-q", "-m", msg)
    if sh("git", "push", "-q"):
        log("공개 저장소 push 완료")
    sh("powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ROOT / "sync-supnote.ps1"), msg)


def serve(at: str, push: bool, cards: int = 1) -> None:
    hh, mm = map(int, at.split(":"))
    log(f"상주 모드 시작 — 매일 {at} 실행 (Ctrl+C 종료)")
    load_env()
    last_sync = 0.0
    extra_day = None
    while True:
        now = dt.datetime.now()
        today = now.date()
        due = now.time() >= dt.time(hh, mm)
        path = daily_path(today)
        # .env의 DAILY_EXTRA_CMD: 같은 시각에 함께 돌릴 로컬 작업 (별도 프로세스, 하루 한 번)
        extra = os.environ.get("DAILY_EXTRA_CMD", "").strip()
        if due and extra and extra_day != today:
            extra_day = today
            log(f"추가 작업 시작: {extra}")
            subprocess.Popen(extra, cwd=ROOT, shell=True)
        if due and (not path.exists() or is_generating(path)):  # 생성 중 표시만 남은 채 실패했으면 재시도
            try:
                run_daily(today, push, cards)
            except Exception as e:  # 실패해도 프로세스는 유지, 10분 뒤 재시도
                log(f"[!] 실패: {e!r} — 10분 후 재시도")
                time.sleep(600)
                continue
        # 2분마다 alphaXiv 북마크 확인 (목록 조회만, 새 북마크가 있을 때만 LLM·push). 데일리 생성 중에는 건너뜀
        if time.time() - last_sync >= SAVED_SYNC_SEC and not is_generating(path):
            last_sync = time.time()
            try:
                if sync_saved() and push:
                    git_push(f"saved: 즐겨찾기 동기화 {now:%Y-%m-%d %H:%M}")
            except Exception as e:
                log(f"[!] 즐겨찾기 동기화 실패: {e!r}")
        time.sleep(60)


def backfill_daily_keywords() -> None:
    """기존 데일리 페이지들의 미연결 키워드(<span class="dp-tech">)를 추출해 기법 사전에 추가·카드 생성 후 링크로 치환."""
    load_env()
    TECH_DIR.mkdir(parents=True, exist_ok=True)
    md_files = sorted(DAILY_DIR.glob("????-??/????-??-??.md"), reverse=True)
    span_re = re.compile(r'<span class="dp-tech">(.*?)</span>')
    all_kws: list[str] = []
    for f in md_files:
        for m in span_re.finditer(f.read_text(encoding="utf-8")):
            all_kws.append(m.group(1))
    if not all_kws:
        log("미반영 키워드 없음")
        return
    new_techs = add_new_techniques(all_kws)
    write_tech_index()
    for f in md_files:
        txt = f.read_text(encoding="utf-8")
        new_txt = span_re.sub(lambda m: tech_link(m.group(1), new_techs), txt)
        if new_txt != txt:
            f.write_text(new_txt, encoding="utf-8")
            log(f"데일리 키워드 링크 갱신: {f.relative_to(ROOT)}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("--push", action="store_true"); r.add_argument("--cards", type=int, default=1)
    s = sub.add_parser("serve"); s.add_argument("--at", default="07:30"); s.add_argument("--push", action="store_true")
    s.add_argument("--cards", type=int, default=1, help="하루에 만들 기법 카드 수")
    c = sub.add_parser("card"); c.add_argument("name"); c.add_argument("--category", default="기타")
    sub.add_parser("index", help="기법 사전 목차·카테고리 페이지만 다시 생성")
    sub.add_parser("backfill", help="기존 데일리의 미연결 키워드를 기법 사전에 반영·카드 생성")
    sv = sub.add_parser("saved", help="alphaXiv 북마크 → 즐겨찾기 논문 동기화"); sv.add_argument("--push", action="store_true")
    a = ap.parse_args()
    if a.cmd == "saved":
        if sync_saved() and a.push:
            git_push("saved: 즐겨찾기 동기화")
    elif a.cmd == "run":
        run_daily(dt.date.today(), a.push, a.cards)
    elif a.cmd == "serve":
        serve(a.at, a.push, a.cards)
    elif a.cmd == "index":
        write_tech_index()
    elif a.cmd == "backfill":
        backfill_daily_keywords()
    else:
        load_env()
        TECH_DIR.mkdir(parents=True, exist_ok=True)
        make_card(a.name, a.category)
        write_tech_index()


if __name__ == "__main__":
    main()
