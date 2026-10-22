#!/usr/bin/env python3
"""Замер роста и состава ~/.hermes/state.db (Hermes Agent) в режиме read-only.

Печатает: размер файла/WAL, размер по объектам (dbstat), состав payload по полям
и ролям, суточную динамику вставок, оценку усиления записи (payload -> байты файла),
признак устаревшей (legacy) схемы FTS. Ничего не пишет в базу.

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/state_db_stats.py [path-to-state.db]
"""
from __future__ import annotations

import os
import sqlite3
import sys
from pathlib import Path

DEFAULT_DB = Path.home() / ".hermes" / "state.db"


def open_ro(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def sizes(conn: sqlite3.Connection, path: Path) -> None:
    page = conn.execute("PRAGMA page_size").fetchone()[0]
    pages = conn.execute("PRAGMA page_count").fetchone()[0]
    free = conn.execute("PRAGMA freelist_count").fetchone()[0]
    print(f"файл: {path}")
    print(f"  страниц {pages} x {page} Б; свободных {free} ({100.0 * free / max(pages, 1):.1f}%)")
    for suffix in ("-wal", "-shm"):
        p = Path(str(path) + suffix)
        if p.exists():
            print(f"  {suffix}: {p.stat().st_size / 1048576:.1f} MB")
    print("  PRAGMA:", {k: conn.execute(f"PRAGMA {k}").fetchone()[0]
                        for k in ("journal_mode", "auto_vacuum", "cache_size",
                                  "journal_size_limit", "wal_autocheckpoint", "mmap_size")})


def objects(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        "SELECT name, SUM(pgsize) FROM dbstat GROUP BY name ORDER BY 2 DESC").fetchall()
    total = sum(r[1] for r in rows) or 1
    print("\nобъекты (MB / доля):")
    for name, b in rows[:12]:
        print(f"  {name:36s} {b / 1048576:8.1f}  {100.0 * b / total:5.1f}%")


def payload(conn: sqlite3.Connection) -> None:
    cols = ("content", "tool_calls", "reasoning", "reasoning_content")
    total = 0
    print("\npayload по полям (MB):")
    for c in cols:
        v = conn.execute(f"SELECT COALESCE(SUM(LENGTH({c})),0) FROM messages").fetchone()[0]
        total += v
        print(f"  {c:18s} {v / 1048576:7.1f}")
    print("  по ролям:")
    for role, n, b in conn.execute(
            "SELECT role, COUNT(*), COALESCE(SUM(LENGTH(COALESCE(content,''))),0) "
            "FROM messages GROUP BY role ORDER BY 3 DESC"):
        print(f"    {role:12s} n={n:6d} {b / 1048576:7.1f}")
    rows = conn.execute(
        "SELECT date(timestamp,'unixepoch') d, COUNT(*), "
        "SUM(LENGTH(COALESCE(content,''))+LENGTH(COALESCE(tool_calls,''))"
        "+LENGTH(COALESCE(reasoning,''))) FROM messages GROUP BY d ORDER BY d").fetchall()
    if rows:
        span = len(rows)
        print(f"\nсуточная динамика: {span} активных дней, "
              f"payload {total / 1048576:.1f} MB, "
              f"среднее {total / span / 1048576:.2f} MB/день")
        for d, n, b in rows[-10:]:
            print(f"  {d} n={n:5d} {b / 1048576:6.2f} MB")


def fts_layout(conn: sqlite3.Connection) -> None:
    flag = conn.execute(
        "SELECT value FROM state_meta WHERE key='fts_optimize_available'").fetchone()
    ddl = dict(conn.execute(
        "SELECT name, sql FROM sqlite_master WHERE name IN "
        "('messages_fts','messages_fts_trigram')").fetchall())
    legacy = any("content=" not in (sql or "") for sql in ddl.values())
    print(f"\nFTS: legacy-раскладка={legacy}, fts_optimize_available={flag[0] if flag else None}"
          f" -> {'нужен hermes sessions optimize-storage' if flag or legacy else 'compact'}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DB
    if not path.exists():
        print(f"нет файла: {path}")
        return 1
    conn = open_ro(path)
    try:
        sizes(conn, path)
        objects(conn)
        payload(conn)
        fts_layout(conn)
    finally:
        conn.close()
    dbs = sorted(Path.home().glob(".hermes/**/state.db"))
    print("\nвсе state.db профилей (MB):")
    grand = 0
    for p in dbs:
        mb = p.stat().st_size / 1048576
        grand += mb
        print(f"  {mb:8.1f}  {p}")
    print(f"  итого {grand:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
