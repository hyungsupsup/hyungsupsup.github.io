"""섭노트 daily 데이터 저장소 (PostgreSQL).

원본 데이터는 여기(DB)에 두고, notes/ 아래 md는 사이트 빌드용으로 DB에서 렌더링한다.
접속 정보는 .env 의 SUPNOTE_DB_* 를 쓴다 (HOST, PORT, NAME, USER, PASSWORD, SCHEMA).
"""
from __future__ import annotations

import json
import os
import re

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

_conn: psycopg.Connection | None = None


def schema() -> str:
    s = os.environ.get("SUPNOTE_DB_SCHEMA", "supnote")
    if not re.fullmatch(r"[a-z_][a-z0-9_]*", s):
        raise ValueError(f"잘못된 스키마 이름: {s}")
    return s


def conn() -> psycopg.Connection:
    global _conn
    if _conn is None or _conn.closed:
        e = os.environ
        missing = [k for k in ("SUPNOTE_DB_NAME", "SUPNOTE_DB_USER", "SUPNOTE_DB_PASSWORD") if not e.get(k)]
        if missing:
            raise RuntimeError(f".env에 {', '.join(missing)} 설정 필요")
        _conn = psycopg.connect(
            host=e.get("SUPNOTE_DB_HOST", "localhost"), port=int(e.get("SUPNOTE_DB_PORT", "5432")),
            dbname=e["SUPNOTE_DB_NAME"], user=e["SUPNOTE_DB_USER"], password=e["SUPNOTE_DB_PASSWORD"],
            autocommit=True, row_factory=dict_row,
        )
        _conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema()}")
        _conn.execute(f"SET search_path TO {schema()}")
        _create_tables(_conn)
    return _conn


def _create_tables(c: psycopg.Connection) -> None:
    c.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id          text PRIMARY KEY,
        name        text NOT NULL,
        emoji       text NOT NULL DEFAULT '',
        description text NOT NULL DEFAULT '',
        ord         int  NOT NULL DEFAULT 0
    );
    CREATE TABLE IF NOT EXISTS techniques (
        name        text PRIMARY KEY,
        category_id text NOT NULL REFERENCES categories(id),
        grp         text NOT NULL,
        seq         bigserial,                       -- 추가된 순서 (카테고리·세부 분류 안에서의 표시 순서)
        origin      text NOT NULL DEFAULT 'seed',    -- seed | paper (논문 키워드에서 자동 추가)
        added_at    timestamptz NOT NULL DEFAULT now()
    );
    CREATE TABLE IF NOT EXISTS technique_cards (
        slug        text PRIMARY KEY,
        name        text NOT NULL,
        category    text NOT NULL DEFAULT '',
        data        jsonb,                           -- LLM이 만든 원본 JSON (이관된 옛 카드는 NULL)
        markdown    text NOT NULL,                   -- 사이트용 렌더링 결과
        created_at  timestamptz NOT NULL DEFAULT now()
    );
    CREATE TABLE IF NOT EXISTS daily_runs (
        day          date PRIMARY KEY,
        status       text NOT NULL DEFAULT 'generating',   -- generating | done
        technique    text,
        trend        text,
        question     text,
        question_note text,
        markdown     text,
        started_at   timestamptz NOT NULL DEFAULT now(),
        finished_at  timestamptz
    );
    CREATE TABLE IF NOT EXISTS daily_papers (
        day        date NOT NULL REFERENCES daily_runs(day) ON DELETE CASCADE,
        source     text NOT NULL,                   -- HF | alphaXiv | arXiv
        paper_id   text NOT NULL,
        rank       int  NOT NULL,
        upvotes    int,
        title      text NOT NULL,
        abstract   text NOT NULL DEFAULT '',
        published  text NOT NULL DEFAULT '',
        note       jsonb NOT NULL DEFAULT '{}'::jsonb,  -- 입문자용 해설
        PRIMARY KEY (day, source, paper_id)
    );
    CREATE TABLE IF NOT EXISTS saved_papers (
        paper_id   text PRIMARY KEY,
        title      text NOT NULL,
        abstract   text NOT NULL DEFAULT '',
        published  text NOT NULL DEFAULT '',
        saved      date NOT NULL,                   -- 동기화가 처음 발견한 날 (월별 묶음 기준)
        folders    jsonb NOT NULL DEFAULT '[]'::jsonb,
        note       jsonb NOT NULL DEFAULT '{}'::jsonb
    );
    """)


# ---------------------------------------------------------------- 기법 사전
def load_catalog() -> dict:
    """{cat_id: {name, emoji, desc, groups: {세부분류: [기법...]}}} — 예전 techniques.json과 같은 모양."""
    c = conn()
    cat = {r["id"]: {"name": r["name"], "emoji": r["emoji"], "desc": r["description"], "groups": {}}
           for r in c.execute("SELECT * FROM categories ORDER BY ord, id")}
    for r in c.execute("SELECT name, category_id, grp FROM techniques ORDER BY seq"):
        if r["category_id"] in cat:
            cat[r["category_id"]]["groups"].setdefault(r["grp"], []).append(r["name"])
    return cat


def upsert_category(cid: str, name: str, emoji: str, desc: str, ord_: int) -> None:
    conn().execute(
        "INSERT INTO categories (id, name, emoji, description, ord) VALUES (%s,%s,%s,%s,%s) "
        "ON CONFLICT (id) DO UPDATE SET name=EXCLUDED.name, emoji=EXCLUDED.emoji, description=EXCLUDED.description, ord=EXCLUDED.ord",
        (cid, name, emoji, desc, ord_))


def add_technique(name: str, cid: str, grp: str, origin: str = "paper") -> bool:
    cur = conn().execute(
        "INSERT INTO techniques (name, category_id, grp, origin) VALUES (%s,%s,%s,%s) ON CONFLICT (name) DO NOTHING",
        (name, cid, grp, origin))
    return cur.rowcount == 1


def delete_technique(name: str) -> None:
    conn().execute("DELETE FROM techniques WHERE name=%s", (name,))


# ---------------------------------------------------------------- 기법 카드
def save_card(slug: str, name: str, category: str, data: dict | None, markdown: str) -> None:
    conn().execute(
        "INSERT INTO technique_cards (slug, name, category, data, markdown) VALUES (%s,%s,%s,%s,%s) "
        "ON CONFLICT (slug) DO UPDATE SET name=EXCLUDED.name, category=EXCLUDED.category, data=EXCLUDED.data, "
        "markdown=EXCLUDED.markdown",
        (slug, name, category, Jsonb(data) if data is not None else None, markdown))


def card_slugs() -> set[str]:
    return {r["slug"] for r in conn().execute("SELECT slug FROM technique_cards")}


def card_markdown(slug: str) -> str | None:
    r = conn().execute("SELECT markdown FROM technique_cards WHERE slug=%s", (slug,)).fetchone()
    return r["markdown"] if r else None


def all_cards() -> list[dict]:
    return list(conn().execute("SELECT slug, markdown FROM technique_cards"))


def delete_card(slug: str) -> None:
    conn().execute("DELETE FROM technique_cards WHERE slug=%s", (slug,))


# ---------------------------------------------------------------- 데일리
def start_daily(day) -> None:
    conn().execute(
        "INSERT INTO daily_runs (day, status) VALUES (%s, 'generating') "
        "ON CONFLICT (day) DO UPDATE SET status='generating', started_at=now(), finished_at=NULL",
        (day,))


def finish_daily(day, technique, trend, question, question_note, markdown, papers: list[dict], notes: dict) -> None:
    c = conn()
    with c.transaction():
        c.execute(
            "INSERT INTO daily_runs (day, status, technique, trend, question, question_note, markdown, finished_at) "
            "VALUES (%s,'done',%s,%s,%s,%s,%s,now()) ON CONFLICT (day) DO UPDATE SET status='done', "
            "technique=EXCLUDED.technique, trend=EXCLUDED.trend, question=EXCLUDED.question, "
            "question_note=EXCLUDED.question_note, markdown=EXCLUDED.markdown, finished_at=now()",
            (day, technique, trend, question, question_note, markdown))
        c.execute("DELETE FROM daily_papers WHERE day=%s", (day,))
        ranks: dict[str, int] = {}
        for p in papers:
            src = p.get("source", "HF")
            ranks[src] = ranks.get(src, 0) + 1
            up = p.get("upvotes")
            c.execute(
                "INSERT INTO daily_papers (day, source, paper_id, rank, upvotes, title, abstract, published, note) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
                (day, src, p["id"], p.get("rank") or ranks[src], up if isinstance(up, int) else None,
                 p["title"], p.get("abstract", ""), p.get("published", ""), Jsonb(notes.get(p["id"], {}))))


def daily_status(day) -> str | None:
    r = conn().execute("SELECT status FROM daily_runs WHERE day=%s", (day,)).fetchone()
    return r["status"] if r else None


def daily_days() -> list[dict]:
    return list(conn().execute("SELECT day, status, markdown FROM daily_runs ORDER BY day DESC"))


def import_daily_markdown(day, markdown: str) -> None:
    """예전 md 데일리를 그대로 보관 (논문 행 없이)."""
    conn().execute(
        "INSERT INTO daily_runs (day, status, markdown, finished_at) VALUES (%s,'done',%s,now()) "
        "ON CONFLICT (day) DO NOTHING", (day, markdown))


# ---------------------------------------------------------------- 즐겨찾기
def load_saved() -> dict[str, dict]:
    out = {}
    for r in conn().execute("SELECT * FROM saved_papers"):
        out[r["paper_id"]] = {"id": r["paper_id"], "title": r["title"], "abstract": r["abstract"],
                              "published": r["published"], "saved": str(r["saved"]),
                              "folders": r["folders"], "note": r["note"]}
    return out


def upsert_saved(p: dict) -> None:
    conn().execute(
        "INSERT INTO saved_papers (paper_id, title, abstract, published, saved, folders, note) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (paper_id) DO UPDATE SET title=EXCLUDED.title, "
        "abstract=EXCLUDED.abstract, published=EXCLUDED.published, folders=EXCLUDED.folders, note=EXCLUDED.note",
        (p["id"], p["title"], p.get("abstract", ""), p.get("published", ""), p["saved"],
         Jsonb(p.get("folders", [])), Jsonb(p.get("note", {}))))


def set_saved_folders(pid: str, folders: list[str]) -> None:
    conn().execute("UPDATE saved_papers SET folders=%s WHERE paper_id=%s", (Jsonb(folders), pid))


def delete_saved(pid: str) -> None:
    conn().execute("DELETE FROM saved_papers WHERE paper_id=%s", (pid,))


def counts() -> dict[str, int]:
    c = conn()
    return {t: c.execute(f"SELECT count(*) AS n FROM {t}").fetchone()["n"]
            for t in ("categories", "techniques", "technique_cards", "daily_runs", "daily_papers", "saved_papers")}
