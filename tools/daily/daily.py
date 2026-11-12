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
import re
import subprocess
import sys
import time
import urllib.parse
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
    return [(cat, t) for cat, items in CATALOG.items() for t in items]


def link_if_known(name: str) -> str:
    norm = lambda x: slugify(x).replace("-", "")
    known = {norm(t): slugify(t) for _, t in all_techniques()}
    s = known.get(norm(name))
    return f"[[techniques/{s}|{name}]]" if s else name


def make_card(name: str, category: str) -> Path:
    path = TECH_DIR / f"{slugify(name)}.md"
    j = parse_json(llm_chat(CARD_SYSTEM, f"기법: {name}\n분류: {category}"))
    bullets = lambda xs: "\n".join(f"- {x}" for x in xs) or "- (없음)"
    links = lambda xs: "\n".join(f"- {link_if_known(x)}" for x in xs) or "- (없음)"
    path.write_text(
        f"""---
title: {yaml_str(name)}
date: {dt.date.today()}
tags: [technique, {slugify(category) or 'misc'}]
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


def write_tech_index() -> None:
    lines = ["---", "title: 기법 사전", f"date: {dt.date.today()}", "tags: [index]", "---", "",
             "아이디어 구상용 AI 기법·모듈·모델 정리. 카드마다 **해결한 문제 → 핵심 아이디어 → 트레이드오프 → 계보 → 피지컬 AI 쓰임 → 💡 아이디어 훅**.",
             "매일 1개씩 자동으로 초안이 추가된다 (✅ 작성됨 · ⬜ 예정).", ""]
    for cat, items in CATALOG.items():
        lines.append(f"## {cat}")
        for t in items:
            s = slugify(t)
            lines.append(f"- ✅ [[techniques/{s}|{t}]]" if (TECH_DIR / f"{s}.md").exists() else f"- ⬜ {t}")
        lines.append("")
    (TECH_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


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


PICK_SYSTEM = """당신은 피지컬 AI 연구자의 아침 브리핑을 쓴다. 독자: diffusion/CV 석사 + LLM 에이전트 엔지니어.
주어진 최신 arXiv 논문 목록에서 아이디어 구상에 가장 자극이 되는 논문 2편을 고르고, 기법 목록과 연결하라.
한국어, 기술 용어는 영어. JSON만 출력:
{"papers": [{"id": "arXiv id", "why": "왜 흥미로운가 1문장", "summary": "핵심 3문장", "techniques": ["기법 목록 중 관련된 이름"]}],
 "trend": "오늘 목록 전체에서 보이는 흐름 1~2문장",
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

    papers = fetch_arxiv()
    log(f"arXiv {len(papers)}편 조회")
    listing = "\n".join(f"- {p['id']} | {p['title']} | {p['abstract'][:500]}" for p in papers)
    names = ", ".join(t for _, t in all_techniques())
    j = parse_json(llm_chat(PICK_SYSTEM, f"오늘의 기법: {tech_name}\n기법 목록: {names}\n\n논문:\n{listing}"))
    by_id = {p["id"]: p for p in papers}

    paper_md = []
    for pk in j.get("papers", [])[:2]:
        p = by_id.get(pk.get("id"), {})
        title = p.get("title", pk.get("id"))
        techs = ", ".join(link_if_known(t) for t in pk.get("techniques", []))
        paper_md.append(f"### [{title}](https://arxiv.org/abs/{pk.get('id')})\n"
                        f"*{pk.get('why', '')}*\n\n{pk.get('summary', '')}\n\n관련 기법: {techs or '-'}\n")

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
{chr(10).join(paper_md) or '(선정 실패)'}

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
    a = ap.parse_args()
    if a.cmd == "run":
        run_daily(dt.date.today(), a.push, a.cards)
    elif a.cmd == "serve":
        serve(a.at, a.push, a.cards)
    else:
        load_env()
        TECH_DIR.mkdir(parents=True, exist_ok=True)
        make_card(a.name, a.category)
        write_tech_index()


if __name__ == "__main__":
    main()
