"""paper-db: 학회 논문 수집 → 필터 → LLM 요약 → 인용 관계 → 노트 생성.

사용법 (저장소 루트에서):
    python tools/paper-db/paperdb.py collect   --venue cvpr --year 2025
    python tools/paper-db/paperdb.py abstracts --venue cvpr --year 2025
    python tools/paper-db/paperdb.py summarize --venue cvpr --year 2025 [--limit N]
    python tools/paper-db/paperdb.py link      --venue cvpr --year 2025
    python tools/paper-db/paperdb.py export    --venue cvpr --year 2025
    python tools/paper-db/paperdb.py all       --venue cvpr --year 2025

LLM 설정은 저장소 루트 .env: LLM_BASE_URL, LLM_API_KEY, DEFAULT_LLM_MODEL (OpenAI 호환 API)
표준 라이브러리만 사용한다.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = Path(__file__).resolve().parent / "data"
NOTES = ROOT / "notes" / "knowledge"
UA = "paper-db/0.1 (personal research notes)"

# ---------------------------------------------------------------------------
# 필터 기준
# ---------------------------------------------------------------------------
# 1차: 제목 키워드 (넓게 잡고, 2차에서 LLM이 초록 보고 걸러낸다)
TITLE_KEYWORDS = re.compile(
    r"robot|manipulat|grasp|embodi|vision[- ]language[- ]action|\bVLAs?\b|world model|"
    r"\bpolic(y|ies)\b|navigat|humanoid|dexter|sim[- ]?to[- ]?real|sim2real|affordance|"
    r"teleoperat|imitation|reinforcement|locomot|bimanual|action model|action chunk|"
    r"action generation|action prediction|autonomous driving|driving world|physical|"
    r"interactive video|video world|agent",
    re.I,
)

TOPICS = [
    "VLA",
    "World Model",
    "Imitation Learning",
    "Reinforcement Learning",
    "Manipulation",
    "Navigation",
    "Humanoid & Locomotion",
    "Autonomous Driving",
    "Embodied Perception",
    "Simulation & Sim2Real",
    "Dataset & Benchmark",
    "Other",
]

SYSTEM_PROMPT = f"""You are a research assistant who triages computer vision / ML papers for a researcher studying Physical AI
(robot learning, Vision-Language-Action models, world models, embodied agents, sim-to-real).
Read the paper title and abstract and return ONLY a JSON object (no markdown fences) with these keys:
- "relevant": true if the paper's main contribution is meaningfully useful for Physical AI research
  (robot policies, VLA, world models/video prediction for agents or driving, embodied perception for action,
  simulation/sim2real, robot datasets/benchmarks). false for pure 2D/3D vision, generic generation, etc.
- "topics": 1-3 items chosen from {TOPICS}
- "tldr": one-sentence summary in Korean
- "problem": the problem being solved, in Korean (1-2 sentences)
- "key_idea": the core idea that differs from prior work, in Korean (1-2 sentences)
- "method": how it works, in Korean (2-3 sentences)
- "results": main results or claims, in Korean (1-2 sentences, keep numbers exactly as in the abstract)
Use only information in the abstract. Keep technical terms (model names, method names) in English."""


# ---------------------------------------------------------------------------
# 공통 유틸
# ---------------------------------------------------------------------------
def load_env() -> None:
    env = ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def http_get(url: str, retries: int = 3) -> str:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError) as e:
            if i == retries - 1:
                raise
            time.sleep(2 * (i + 1))
    raise RuntimeError("unreachable")


def http_post_json(url: str, payload: dict, headers: dict | None = None, timeout: int = 180) -> dict:
    data = json.dumps(payload).encode("utf-8")
    h = {"Content-Type": "application/json", "User-Agent": UA, **(headers or {})}
    req = urllib.request.Request(url, data=data, headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def db_path(venue: str, year: int) -> Path:
    return DATA / f"{venue}{year}.jsonl"


def load_db(venue: str, year: int) -> list[dict]:
    p = db_path(venue, year)
    if not p.exists():
        sys.exit(f"[!] {p} 가 없습니다. 먼저 collect를 실행하세요.")
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def save_db(venue: str, year: int, papers: list[dict]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    tmp = db_path(venue, year).with_suffix(".tmp")
    tmp.write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in papers) + "\n", encoding="utf-8")
    tmp.replace(db_path(venue, year))


def clean(text: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = re.sub(r"(\w)- (\w)", r"\1\2", text)  # PDF 줄바꿈 하이픈 제거 ("im- age" → "image")
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------------------
# 1. collect — CVF Open Access 목록
# ---------------------------------------------------------------------------
CVF_BASE = "https://openaccess.thecvf.com"


def collect_cvf(venue: str, year: int) -> list[dict]:
    tag = f"{venue.upper()}{year}"
    page = http_get(f"{CVF_BASE}/{tag}?day=all")
    blocks = page.split('<dt class="ptitle">')[1:]
    papers = []
    for b in blocks:
        m = re.search(r'<a href="([^"]+_paper\.html)">(.*?)</a>', b, re.S)
        if not m:
            continue
        href, title = m.group(1), clean(m.group(2))
        slug = re.sub(rf"_{venue.upper()}_{year}_paper\.html$", "", href.rsplit("/", 1)[-1])
        authors = re.findall(r'name="query_author" value="([^"]+)"', b)
        arxiv = re.search(r'arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})', b)
        papers.append(
            {
                "id": f"{venue}{year}-{slug}",
                "slug": slug,
                "venue": venue.upper(),
                "year": year,
                "title": title,
                "authors": authors,
                "url": CVF_BASE + href,
                "arxiv": arxiv.group(1) if arxiv else None,
            }
        )
    return papers


def cmd_collect(a) -> None:
    if a.venue not in ("cvpr", "iccv", "eccv", "wacv"):
        sys.exit("[!] 현재는 CVF 학회(cvpr/iccv/eccv/wacv)만 지원합니다.")
    papers = collect_cvf(a.venue, a.year)
    old = {p["id"]: p for p in load_db(a.venue, a.year)} if db_path(a.venue, a.year).exists() else {}
    merged = [{**p, **{k: v for k, v in old.get(p["id"], {}).items() if k not in p}} for p in papers]
    for p in merged:
        p["candidate"] = bool(TITLE_KEYWORDS.search(p["title"]))
    save_db(a.venue, a.year, merged)
    n_c = sum(p["candidate"] for p in merged)
    print(f"[collect] {a.venue.upper()} {a.year}: 전체 {len(merged)}편, 제목 키워드 후보 {n_c}편")


# ---------------------------------------------------------------------------
# 2. abstracts — 후보 논문의 초록 수집
# ---------------------------------------------------------------------------
def fetch_abstract(p: dict) -> str | None:
    try:
        page = http_get(p["url"])
    except Exception as e:  # noqa: BLE001
        print(f"  [!] {p['slug']}: {e}")
        return None
    m = re.search(r'<div id="abstract">(.*?)</div>', page, re.S)
    return clean(m.group(1)) if m else None


def cmd_abstracts(a) -> None:
    papers = load_db(a.venue, a.year)
    todo = [p for p in papers if p.get("candidate") and not p.get("abstract")]
    print(f"[abstracts] 초록 수집 대상 {len(todo)}편")
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, (p, abs_) in enumerate(zip(todo, ex.map(fetch_abstract, todo)), 1):
            if abs_:
                p["abstract"] = abs_
            if i % 50 == 0:
                print(f"  {i}/{len(todo)}")
                save_db(a.venue, a.year, papers)
    save_db(a.venue, a.year, papers)
    print(f"[abstracts] 완료: {sum(1 for p in papers if p.get('abstract'))}편 보유")


# ---------------------------------------------------------------------------
# 3. summarize — LLM으로 관련성 판정 + 요약
# ---------------------------------------------------------------------------
def llm_chat(system: str, user: str) -> str:
    base = os.environ.get("LLM_BASE_URL", "").rstrip("/")
    key = os.environ.get("LLM_API_KEY", "")
    model = os.environ.get("DEFAULT_LLM_MODEL", "")
    if not (base and model):
        sys.exit("[!] .env에 LLM_BASE_URL, DEFAULT_LLM_MODEL (필요시 LLM_API_KEY)을 설정하세요.")
    res = http_post_json(
        f"{base}/chat/completions",
        {
            "model": model,
            "temperature": 0.2,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        },
        headers={"Authorization": f"Bearer {key}"} if key else None,
    )
    return res["choices"][0]["message"]["content"]


def parse_json(text: str) -> dict:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)  # reasoning 모델 대응
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError("JSON not found")
    return json.loads(m.group(0))


def summarize_one(p: dict) -> dict | None:
    user = f"Title: {p['title']}\n\nAbstract: {p['abstract']}"
    for attempt in range(3):
        try:
            out = parse_json(llm_chat(SYSTEM_PROMPT, user))
            out["topics"] = [t for t in out.get("topics", []) if t in TOPICS] or ["Other"]
            out["relevant"] = bool(out.get("relevant"))
            return out
        except Exception as e:  # noqa: BLE001
            if attempt == 2:
                print(f"  [!] {p['slug']}: {e}")
            time.sleep(2 * (attempt + 1))
    return None


def cmd_summarize(a) -> None:
    load_env()
    papers = load_db(a.venue, a.year)
    todo = [p for p in papers if p.get("abstract") and "summary" not in p]
    if a.limit:
        todo = todo[: a.limit]
    print(f"[summarize] LLM 요약 대상 {len(todo)}편 (model={os.environ.get('DEFAULT_LLM_MODEL')})")
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for i, (p, s) in enumerate(zip(todo, ex.map(summarize_one, todo)), 1):
            if s:
                p["summary"] = s
            if i % 20 == 0:
                print(f"  {i}/{len(todo)}")
                save_db(a.venue, a.year, papers)
    save_db(a.venue, a.year, papers)
    rel = [p for p in papers if p.get("summary", {}).get("relevant")]
    print(f"[summarize] 완료: 관련 논문 {len(rel)}편 / 요약 {sum('summary' in p for p in papers)}편")


# ---------------------------------------------------------------------------
# 4. link — Semantic Scholar로 인용 관계·인용수
# ---------------------------------------------------------------------------
S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"


def cmd_link(a) -> None:
    load_env()
    papers = load_db(a.venue, a.year)
    rel = [p for p in papers if p.get("summary", {}).get("relevant") and p.get("arxiv")]
    print(f"[link] Semantic Scholar 조회 {len(rel)}편 (arXiv ID 있는 관련 논문)")
    headers = {"x-api-key": os.environ["S2_API_KEY"]} if os.environ.get("S2_API_KEY") else None
    for i in range(0, len(rel), 100):
        chunk = rel[i : i + 100]
        for attempt in range(5):
            try:
                res = http_post_json(
                    S2_BATCH + "?fields=citationCount,references.externalIds,references.title",
                    {"ids": [f"ARXIV:{p['arxiv']}" for p in chunk]},
                    headers=headers,
                )
                break
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < 4:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise
        for p, r in zip(chunk, res):
            if not r:
                continue
            p["citation_count"] = r.get("citationCount")
            p["references"] = [
                {"arxiv": (ref.get("externalIds") or {}).get("ArXiv"), "title": ref.get("title")}
                for ref in (r.get("references") or [])
                if ref
            ]
        time.sleep(1.5)
    save_db(a.venue, a.year, papers)
    print(f"[link] 완료: {sum('references' in p for p in papers)}편 참고문헌 확보")


# ---------------------------------------------------------------------------
# 5. export — Quartz 노트 생성
# ---------------------------------------------------------------------------
def load_map_papers() -> dict[str, str]:
    """notes/knowledge/map.md 표에서 {arxiv_id: 논문명} 추출 (대표 논문과 연결용)."""
    out = {}
    mp = NOTES / "map.md"
    if not mp.exists():
        return out
    for line in mp.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(.+?)\s*\|\s*\d{4}\s*\|\s*\[(\d{4}\.\d{4,5})\]", line)
        if m:
            out[m.group(2)] = re.sub(r"[*💡]", "", m.group(1)).strip()
    return out


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def topic_tag(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def cmd_export(a) -> None:
    papers = load_db(a.venue, a.year)
    rel = [p for p in papers if p.get("summary", {}).get("relevant")]
    if not rel:
        sys.exit("[!] 관련 논문이 없습니다. summarize를 먼저 실행하세요.")
    venue_slug = f"{a.venue}-{a.year}"
    out_dir = NOTES / "venues" / venue_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.md"):
        old.unlink()

    map_papers = load_map_papers()
    by_arxiv = {p["arxiv"]: p for p in rel if p.get("arxiv")}
    cited_by: dict[str, list[dict]] = defaultdict(list)
    for p in rel:
        for ref in p.get("references", []):
            if ref.get("arxiv") in by_arxiv:
                cited_by[by_arxiv[ref["arxiv"]]["id"]].append(p)

    for p in rel:
        s = p["summary"]
        link = lambda q: f"[[knowledge/venues/{venue_slug}/{q['slug']}|{q['title']}]]"  # noqa: E731
        refs_in_db = [by_arxiv[r["arxiv"]] for r in p.get("references", []) if r.get("arxiv") in by_arxiv]
        refs_classic = sorted({map_papers[r["arxiv"]] for r in p.get("references", []) if r.get("arxiv") in map_papers})
        tags = [f"{a.venue}{a.year}"] + [topic_tag(t) for t in s["topics"]]
        lines = [
            "---",
            f"title: {yaml_str(p['title'])}",
            f"tags: [{', '.join(tags)}]",
            f"venue: {p['venue']} {p['year']}",
            f"arxiv: {yaml_str(p['arxiv'] or '')}",
            f"citations: {p.get('citation_count') if p.get('citation_count') is not None else ''}",
            "auto: true",
            "---",
            "",
            f"> **TL;DR** {s.get('tldr', '')}",
            "",
            f"**{p['venue']} {p['year']}** · {', '.join(p['authors'][:6])}{' 외' if len(p['authors']) > 6 else ''}",
            f"[CVF]({p['url']})" + (f" · [arXiv](https://arxiv.org/abs/{p['arxiv']})" if p.get("arxiv") else "")
            + (f" · 인용 {p['citation_count']}회" if p.get("citation_count") is not None else ""),
            "",
            f"**주제:** {' · '.join(s['topics'])}",
            "",
            "## 문제", s.get("problem", ""), "",
            "## 핵심 아이디어", s.get("key_idea", ""), "",
            "## 방법", s.get("method", ""), "",
            "## 결과", s.get("results", ""), "",
        ]
        if refs_classic or refs_in_db or cited_by.get(p["id"]):
            lines.append("## 연결")
            if refs_classic:
                lines.append("- **기반 대표 논문:** " + ", ".join(refs_classic) + " — [[knowledge/map|분야 지도]]")
            for q in refs_in_db:
                lines.append(f"- 인용함 → {link(q)}")
            for q in cited_by.get(p["id"], []):
                lines.append(f"- 인용됨 ← {link(q)}")
            lines.append("")
        lines += ["## 초록 (원문)", p["abstract"], "", "> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.", "", "## 내 메모", ""]
        (out_dir / f"{p['slug']}.md").write_text("\n".join(lines), encoding="utf-8")

    # 학회·연도 인덱스 페이지
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for p in rel:
        by_topic[p["summary"]["topics"][0]].append(p)
    n_cand = sum(1 for p in papers if p.get("candidate"))
    idx = [
        "---",
        f"title: {p['venue'] if rel else a.venue.upper()} {a.year} — Physical AI 논문",
        f"tags: [venue, {a.venue}{a.year}]",
        "---",
        "",
        f"전체 {len(papers)}편 → 제목 키워드 후보 {n_cand}편 → LLM 판정 관련 논문 **{len(rel)}편**",
        "",
        "| 주제 | 편수 |",
        "|---|---|",
    ]
    for t in TOPICS:
        if by_topic.get(t):
            idx.append(f"| [[#{t}]] | {len(by_topic[t])} |")
    for t in TOPICS:
        ps = sorted(by_topic.get(t, []), key=lambda q: -(q.get("citation_count") or 0))
        if not ps:
            continue
        idx += ["", f"## {t}", "", "| 논문 | 한 줄 요약 | 인용 |", "|---|---|---|"]
        for q in ps:
            tl = q["summary"].get("tldr", "").replace("|", "\\|")
            title = q["title"].replace("|", "\\|")
            idx.append(f"| [[knowledge/venues/{venue_slug}/{q['slug']}\\|{title}]] | {tl} | {q.get('citation_count') or ''} |")
    (NOTES / "venues" / f"{venue_slug}.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    # 학회 목록 인덱스
    venues_idx = NOTES / "venues" / "index.md"
    pages = sorted(f.stem for f in (NOTES / "venues").glob("*-*.md"))
    venues_idx.write_text(
        "---\ntitle: 학회별 논문\ntags: [venue]\n---\n\n"
        "탑티어 학회의 Physical AI 관련 논문을 연도별로 모아 자동 요약한 페이지입니다.\n\n"
        + "\n".join(f"- [[knowledge/venues/{s}|{s.split('-')[0].upper()} {s.split('-')[1]}]]" for s in pages)
        + "\n",
        encoding="utf-8",
    )
    print(f"[export] {len(rel)}편 → notes/knowledge/venues/{venue_slug}/")


def cmd_all(a) -> None:
    for f in (cmd_collect, cmd_abstracts, cmd_summarize, cmd_link, cmd_export):
        f(a)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["collect", "abstracts", "summarize", "link", "export", "all"])
    ap.add_argument("--venue", default="cvpr")
    ap.add_argument("--year", type=int, default=2025)
    ap.add_argument("--limit", type=int, default=0, help="summarize 최대 편수 (테스트용)")
    ap.add_argument("--workers", type=int, default=4, help="LLM 동시 요청 수")
    a = ap.parse_args()
    a.venue = a.venue.lower()
    {"collect": cmd_collect, "abstracts": cmd_abstracts, "summarize": cmd_summarize,
     "link": cmd_link, "export": cmd_export, "all": cmd_all}[a.command](a)


if __name__ == "__main__":
    main()
