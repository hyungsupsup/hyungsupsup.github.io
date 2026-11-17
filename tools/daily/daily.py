"""매일 인사이트 생성기 + 기법 사전 자동 확장.

하루 1회:
  1. 기법 사전(techniques.json)에서 아직 카드가 없는 기법 1개 → notes/techniques/<slug>.md 카드 생성
  2. 어제 arXiv(cs.RO 등) 피지컬 AI 논문 중 1~2편 선정·요약
  3. "기법 × 문제" 조합 질문 1개
  → notes/daily/YYYY-MM-DD.md, 인덱스 갱신, (옵션) git push

사용 (저장소 루트):
  python tools/daily/daily.py run                  # 오늘 것 1회 생성
  python tools/daily/daily.py serve --at 07:30 --push   # 상주: 매일 07:30 실행
  (--cards N: 하루에 기법 카드 N장)
  python tools/daily/daily.py card "LoRA"          # 특정 기법 카드만 생성
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
CATALOG = json.loads((HERE / "techniques.json").read_text(encoding="utf-8"))


def slugify(name: str) -> str:
    s = re.sub(r"\(.*?\)", "", name).strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def log(msg: str) -> None:
    print(f"[{dt.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


# ---------------------------------------------------------------- 기법 카드
CARD_SYSTEM = """당신은 AI 연구자의 기법 사전을 작성한다. 독자는 diffusion/CV 석사 + LLM 엔지니어이며 피지컬 AI(로봇 학습, VLA, 월드모델) 연구 아이디어를 구상하려 한다.
한국어로 쓰되 기술 용어·모델명은 영어 원문 유지. 확신 없는 수치·연도·저자는 쓰지 말거나 '(확인 필요)'를 붙여라.
JSON 하나만 출력:
{"one_liner": "한 문장 정의",
 "year_paper": "대표 논문 제목 (연도)",
 "problem": "이전 방법의 어떤 병목을 해결했나 (2~3문장)",
 "core_idea": "핵심 아이디어 (3~5문장, 필요하면 LaTeX 수식 $...$ 포함)",
 "why_it_works": "직관적 설명 (2~3문장)",
 "tradeoffs": ["한계/비용 1", "..."],
 "predecessors": ["이 기법이 개선한 기법 이름", "..."],
 "successors": ["이 기법을 개선/변형한 기법 이름", "..."],
 "robotics_use": ["피지컬 AI/로봇에서 쓰이는 구체적 예 (모델명 포함)", "..."],
 "idea_hooks": ["아직 덜 탐구된 조합이나 연구 질문", "..."]}"""


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


def known_technique(name: str) -> str | None:
    """카탈로그에 있으면 카탈로그상의 정식 이름을 반환 (대소문자·하이픈·괄호 차이 무시)."""
    return {_norm(t): t for _, t in all_techniques()}.get(_norm(name))


CLASSIFY_SYSTEM = """AI 기법 사전에 넣을 후보 키워드를 **엄격하게** 심사한다. 애매하면 무조건 skip. 하루 0개 추가도 정상이다.

통과 조건 (전부 만족해야 함):
1. 구체적인 **기법·알고리즘·모듈·학습 방법** 이름이다 (예: LoRA, Flow Matching, Speculative Decoding, Chain-of-Thought, Diffusion Policy, PPO).
2. 여러 논문에서 같은 이름으로 재사용되는, 이미 자리잡은 용어다. 서베이·교과서·위키에 항목으로 나올 수준.
3. "이게 어떻게 작동하나"를 한 장짜리 카드(문제 → 핵심 아이디어 → 트레이드오프)로 설명할 수 있다.

skip 대상:
- 논문 고유 시스템·모델·데이터셋·벤치마크 이름 (예: "Diffusion Drafter", "GPT-6", "LIBERO")
- 분야·과제·문제 이름 (예: "Robotics", "Manipulation", "Sim-to-Real", "Embodied AI", "Autonomous Driving")
- 일반 부품·막연한 개념 (예: "Visual Encoder", "Memory", "Planner", "Benchmark", "Simulation", "Multi-Agent System")
- 데이터 수집 관행·실험 설정 (예: "Egocentric Recording", "Teleoperation Setup")
- 키워드 끝에 붙은 수식어만 다른 변형 (예: "Sparse-thinking Instruction Tuning" → skip)
- 아래 '기존 기법'과 같은 것이거나 약어/동의어인 경우 (예: VLA ↔ Vision-Language-Action Model) → skip

통과하면 canonical 영어 이름, 카테고리 id(주어진 목록 중 하나), 세부 분류(기존 세부 분류 중 맞는 것 우선, 없으면 새 이름 짧게)를 정한다.
JSON만 출력: {"items": [{"keyword": "입력 그대로", "skip": true, "reason": "짧게", "name": "canonical 이름", "category": "카테고리 id", "group": "세부 분류"}]}"""


def add_new_techniques(keywords: list[str], max_new: int = 5) -> list[str]:
    """카탈로그에 없는 키워드를 LLM으로 분류해 techniques.json에 추가하고 카드를 만든다.
    하루 max_new개까지만 카드를 바로 만들고, 나머지는 카탈로그에만 추가해 이후 '오늘의 기법'으로 순서대로 채운다."""
    cand = []
    for k in keywords:
        k = k.strip()
        if k and not known_technique(k) and _norm(k) not in {_norm(c) for c in cand}:
            cand.append(k)
    if not cand:
        return []
    cats = {cid: {"name": c["name"], "groups": list(c["groups"])} for cid, c in CATALOG.items()}
    try:
        existing = ", ".join(t for _, t in all_techniques())
        j = parse_json(llm_chat(CLASSIFY_SYSTEM, f"카테고리: {json.dumps(cats, ensure_ascii=False)}\n\n기존 기법: {existing}\n\n키워드: {json.dumps(cand, ensure_ascii=False)}"))
    except Exception as e:
        log(f"새 기법 분류 실패: {e}")
        return []
    added = []
    for it in j.get("items", []):
        name = (it.get("name") or "").strip()
        cid = it.get("category")
        if it.get("skip") or not name or cid not in CATALOG or known_technique(name):
            continue
        group = (it.get("group") or "기타").strip()
        CATALOG[cid]["groups"].setdefault(group, []).append(name)
        added.append((CATALOG[cid]["name"], name))
    if not added:
        return []
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
    log(f"기법 사전에 새 기법 {len(added)}개 추가: {', '.join(n for _, n in added)}")
    for cat, name in added[:max_new]:
        try:
            make_card(name, cat)
        except Exception as e:
            log(f"카드 생성 실패 {name}: {e}")
    return [n for _, n in added]


def make_card(name: str, category: str) -> Path:
    path = TECH_DIR / f"{slugify(name)}.md"
    j = parse_json(llm_chat(CARD_SYSTEM, f"기법: {name}\n분류: {category}"))
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


def fetch_alphaxiv_papers(limit: int = 10) -> list[dict]:
    """alphaXiv MCP(Streamable HTTP) hot feed 상위 논문을 인기 순서 그대로 가져온다. ALPHAXIV_API_KEY 필요."""
    api_key = os.environ.get("ALPHAXIV_API_KEY", "").strip()
    if not api_key:
        log("ALPHAXIV_API_KEY 미설정 — alphaXiv 수집 건너뜀")
        return []
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "get_hot_feed",
            "arguments": {"limit": limit * 2},  # 비-arXiv 슬러그를 거른 뒤에도 limit편이 남도록 여유 있게
        },
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.alphaxiv.org/mcp/v1",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "Mozilla/5.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
    # Streamable HTTP는 SSE(data: {...}) 또는 일반 JSON으로 응답할 수 있음
    data_line = next((ln[5:].strip() for ln in body.splitlines() if ln.startswith("data:")), body)
    res = json.loads(data_line)
    content = (res.get("result") or {}).get("content") or []
    text = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
    try:
        items = json.loads(text)
    except Exception:
        return []
    if isinstance(items, dict):
        items = items.get("papers") or items.get("results") or []
    ids = [str(p.get("universal_paper_id") or p.get("id") or p.get("arxiv_id") or "") for p in items]
    # alphaXiv 자체 논문 슬러그(예: 2611.weight-space-...)가 섞이면 arXiv API가 400을 반환하므로 걸러냄
    ids = [i for i in ids if re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", i)][:limit]
    if not ids:
        return []
    # get_hot_feed는 ID만 반환하므로 arXiv API로 제목/초록을 일괄 조회
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    root = ET.fromstring(http_get(url))
    found = {}
    for e in root.findall("a:entry", NS):
        pid = re.sub(r"v\d+$", "", e.findtext("a:id", "", NS).rsplit("/", 1)[-1])
        found[pid] = {
            "id": pid,
            "title": " ".join(e.findtext("a:title", "", NS).split()),
            "abstract": " ".join(e.findtext("a:summary", "", NS).split()),
            "published": e.findtext("a:published", "", NS)[:10],
            "source": "alphaXiv",
        }
    # arXiv 응답 순서는 보장되지 않으므로 hot feed 순서(인기순)로 재정렬
    out = [found[re.sub(r"v\d+$", "", i)] for i in ids if re.sub(r"v\d+$", "", i) in found]
    for rank, p in enumerate(out[:limit], 1):
        p["rank"] = rank
    return out[:limit]


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
- 전문용어는 처음 나올 때 괄호로 쉬운 설명을 붙인다. 예: task-specific policy(과제 하나만을 위해 따로 학습시킨 로봇 제어 모델).
- 초록에 없는 수치·사실을 지어내지 않는다.
- 한국어, 기술 용어는 영어 원문 유지. 수식 기호($) 쓰지 말 것.
JSON만 출력:
{"papers": [{"id": "주어진 id 그대로",
  "oneline": "한 줄: 비유나 질문 형태로, 처음 보는 사람도 바로 감 잡게 (1문장)",
  "background": "배경: 이 논문 전에는 보통 어떻게 했고 무엇이 불편/한계였나 (1~2문장)",
  "claim": "이 논문의 주장: 무엇을 했고 결과가 어땠나, 용어는 괄호 설명 (2문장)",
  "connect": "내가 아는 것과의 연결: LLM 에이전트·diffusion·CV 중 가장 가까운 개념에 빗대기 (1문장)",
  "question": "생각해 볼 질문: 이 논문이 열어 둔 갈림길이나 후속 연구 아이디어 (1문장)",
  "keywords": ["이 논문을 이해하는 데 핵심인 기법·모듈·방법론 2~4개. 널리 쓰이는 영어 정식 이름으로(예: Flow Matching, LoRA, Diffusion Policy). 기법 목록에 같은 것이 있으면 그 표기를 그대로. 논문 고유 시스템명·너무 일반적인 단어 제외"]}]}"""


PICK_SYSTEM = """당신은 AI/피지컬 AI 연구자의 아침 브리핑을 쓴다. 독자: 로봇 입문자, LLM 에이전트·diffusion은 잘 앎.
오늘의 논문 한 줄 요약들을 보고 전체 흐름과 연구 아이디어 질문을 써라. 한국어, 기술 용어는 영어. JSON만 출력:
{"trend": "오늘 목록 전체에서 보이는 흐름 1~2문장",
 "question": "'기법 X × 문제 Y' 형태의 구체적 연구 아이디어 질문 1개 (오늘의 기법과 논문을 엮을 것)",
 "question_note": "그 질문이 왜 열려 있는지, 첫 실험은 무엇일지 2문장"}"""


# ---------------------------------------------------------------- daily
def run_daily(day: dt.date, push: bool, cards: int = 1) -> Path:
    load_env()
    TECH_DIR.mkdir(parents=True, exist_ok=True)
    DAILY_DIR.mkdir(parents=True, exist_ok=True)

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
    names = ", ".join(t for _, t in all_techniques())
    notes: dict[str, dict] = {}
    for i in range(0, len(uniq), 5):  # 출력이 길어서 5편씩 나눠 요청
        batch = uniq[i:i + 5]
        listing = "\n".join(f"- {p['id']} | {p['title']} | {p['abstract'][:1200]}" for p in batch)
        try:
            jb = parse_json(llm_chat(EXPLAIN_SYSTEM, f"기법 목록: {names}\n\n논문:\n{listing}"))
            notes.update({str(pk.get("id")): pk for pk in jb.get("papers", [])})
        except Exception as e:
            log(f"논문 해설 실패({i}~): {e}")
    # 논문 키워드 중 기법 사전에 없는 것은 자동 추가 + 카드 생성
    new_techs = add_new_techniques([k for pk in notes.values() for k in pk.get("keywords", [])])
    write_tech_index()
    digest = "\n".join(f"- {p['title']}: {notes.get(p['id'], {}).get('oneline', '')}" for p in uniq)
    j = parse_json(llm_chat(PICK_SYSTEM, f"오늘의 기법: {tech_name}\n\n오늘의 논문:\n{digest}"))

    def tech_link(name: str) -> str:
        canon = known_technique(name)
        if canon and (TECH_DIR / f"{slugify(canon)}.md").exists():
            new = " dp-new" if canon in new_techs else ""
            return f'<a class="internal dp-tech{new}" href="/techniques/{slugify(canon)}">{html_escape(name)}</a>'
        return f'<span class="dp-tech">{html_escape(name)}</span>'

    esc = lambda x: html_escape(strip_math(str(x or "")))

    def paper_card(p: dict) -> str:
        pk = notes.get(p["id"], {})
        techs = " ".join(tech_link(t) for t in pk.get("keywords", []))
        badge = f'▲ {p["upvotes"]}' if p["source"] == "HF" else (f'#{p["rank"]}' if p.get("rank") else "")

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
        if not pk:
            parts.append(row("📝", "초록", esc(p["abstract"][:400]) + "…"))
        if techs:
            parts.append(row("🏷️", "", f'<div class="dp-techs">{techs}</div>'))
        return (
            f'<div class="dp-card"><div class="dp-top"><span class="dp-badge">{badge}</span>'
            f'<span class="dp-id">arXiv:{p["id"]}</span></div>' + "".join(parts) + "</div>"
        )

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

    path = DAILY_DIR / f"{day}.md"
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

    days = sorted((p.stem for p in DAILY_DIR.glob("????-??-??.md")), reverse=True)
    (DAILY_DIR / "index.md").write_text(
        "---\ntitle: 데일리 인사이트\ndate: " + str(day) + "\ntags: [index]\n---\n\n"
        "매일 아침 자동 생성: 오늘의 기법 카드 · 최신 arXiv 논문 · 아이디어 질문.\n\n"
        + "\n".join(f"- [[daily/{d}|{d}]]" for d in days) + "\n",
        encoding="utf-8",
    )
    if push:
        git_push(f"daily: {day}")
    return path


def git_push(msg: str) -> None:
    def sh(*cmd):
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            log(f"[!] {' '.join(cmd)}: {r.stderr.strip()[:300]}")
        return r.returncode == 0
    sh("git", "add", "notes/daily", "notes/techniques")
    sh("git", "commit", "-q", "-m", msg)
    if sh("git", "push", "-q"):
        log("공개 저장소 push 완료")
    sh("powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ROOT / "sync-supnote.ps1"), msg)


def serve(at: str, push: bool, cards: int = 1) -> None:
    hh, mm = map(int, at.split(":"))
    log(f"상주 모드 시작 — 매일 {at} 실행 (Ctrl+C 종료)")
    while True:
        now = dt.datetime.now()
        today = now.date()
        due = now.time() >= dt.time(hh, mm)
        if due and not (DAILY_DIR / f"{today}.md").exists():
            try:
                run_daily(today, push, cards)
            except Exception as e:  # 실패해도 프로세스는 유지, 10분 뒤 재시도
                log(f"[!] 실패: {e!r} — 10분 후 재시도")
                time.sleep(600)
                continue
        time.sleep(60)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("--push", action="store_true"); r.add_argument("--cards", type=int, default=1)
    s = sub.add_parser("serve"); s.add_argument("--at", default="07:30"); s.add_argument("--push", action="store_true")
    s.add_argument("--cards", type=int, default=1, help="하루에 만들 기법 카드 수")
    c = sub.add_parser("card"); c.add_argument("name"); c.add_argument("--category", default="기타")
    sub.add_parser("index", help="기법 사전 목차·카테고리 페이지만 다시 생성")
    a = ap.parse_args()
    if a.cmd == "run":
        run_daily(dt.date.today(), a.push, a.cards)
    elif a.cmd == "serve":
        serve(a.at, a.push, a.cards)
    elif a.cmd == "index":
        write_tech_index()
    else:
        load_env()
        TECH_DIR.mkdir(parents=True, exist_ok=True)
        make_card(a.name, a.category)
        write_tech_index()


if __name__ == "__main__":
    main()
