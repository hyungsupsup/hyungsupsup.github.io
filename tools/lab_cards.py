"""실험실 페이지(notes/lab/index.md)의 실험 카드 목록을 실험 노트들로부터 다시 만든다.

실험 노트 frontmatter: date(시작일), end(종료일, 선택), status, tags.
카드는 시작일 최신순. 마커 사이만 교체한다.
사용: python tools/lab_cards.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXP_DIR = ROOT / "notes" / "lab" / "experiments"
INDEX = ROOT / "notes" / "lab" / "index.md"
START, END = "<!-- lab-cards:start -->", "<!-- lab-cards:end -->"
STATUS_CLS = {"완료": "done", "진행": "doing", "진행 중": "doing", "실패": "fail", "보류": "hold", "계획": "plan"}


def front(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, m.group(2)


def goal(body: str) -> str:
    m = re.search(r"^##\s*목표[^\n]*\n+(.+?)(?:\n\n|\n##|$)", body, re.S | re.M)
    s = m.group(1) if m else body.strip().split("\n\n")[0]
    s = re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", s)
    s = re.sub(r"[*`#>-]", "", " ".join(s.split()))
    return s[:140] + ("…" if len(s) > 140 else "")


def card(path: Path) -> tuple[str, str]:
    meta, body = front(path.read_text(encoding="utf-8"))
    title = meta.get("title", path.stem)
    num, _, name = title.partition("·")
    if not name:
        num, name = path.stem[:3], title
    start, end = meta.get("date", ""), meta.get("end", "")
    status = meta.get("status", "진행")
    if not end and STATUS_CLS.get(status) in ("done", "fail"):
        end = start
    period = f"{start} ~ {end}" if end and end != start else (start if end else f"{start} ~ 진행 중")
    tags = [t.strip() for t in meta.get("tags", "").strip("[]").split(",") if t.strip() and t.strip() != "lab"]
    tag_html = "".join(f'<span class="lc-tag">#{html.escape(t)}</span>' for t in tags)
    href = f"/lab/experiments/{path.stem}"
    e = html.escape
    return start, (
        f'<a class="lc-card internal" href="{href}" data-no-popover="true">'
        f'<div class="lc-top"><span class="lc-num">{e(num.strip())}</span>'
        f'<span class="lc-status lc-{STATUS_CLS.get(status, "doing")}">{e(status)}</span></div>'
        f'<div class="lc-title">{e(name.strip())}</div>'
        f'<div class="lc-period">📅 {e(period)}</div>'
        f'<div class="lc-goal">{e(goal(body))}</div>'
        f'<div class="lc-tags">{tag_html}</div></a>'
    )


def main():
    cards = sorted((card(p) for p in EXP_DIR.glob("*.md")), key=lambda c: c[0], reverse=True)
    block = f'{START}\n<div class="lab-cards">\n' + "\n".join(c for _, c in cards) + f"\n</div>\n{END}"
    text = INDEX.read_text(encoding="utf-8")
    if START in text:
        text = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    else:
        raise SystemExit(f"{INDEX}에 {START} 마커가 없음")
    INDEX.write_text(text, encoding="utf-8", newline="\n")
    print(f"실험 카드 {len(cards)}개 갱신")


if __name__ == "__main__":
    main()
