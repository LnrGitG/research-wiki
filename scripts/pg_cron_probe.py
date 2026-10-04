#!/usr/bin/env python3
"""Разведка планировщика внутри базы: что уже стоит в pg_cron и что нам позволено.

Только чтение плюс пробные проверки прав (без записи). Запуск:
    ~/.hermes/hermes-agent/venv/bin/python3 scripts/pg_cron_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import db_tunnel  # noqa: E402


def rows(sql: str, params=None):
    try:
        return db_tunnel.query(sql, params)
    except Exception as exc:  # noqa: BLE001
        print(f"  не прошло: {type(exc).__name__}: {str(exc).splitlines()[0]}")
        return None


def main() -> int:
    print("=== Что уже стоит в pg_cron ===")
    r = rows(
        "SELECT jobid, schedule, command, nodename, database, username, active "
        "FROM cron.job ORDER BY jobid"
    )
    if r is not None:
        print(f"  всего джобов: {len(r)}")
        for x in r:
            print(f"  #{x[0]} [{x[1]}] active={x[6]} db={x[4]} user={x[5]}")
            print(f"      {x[2][:110]}")

    print("\n=== История прогонов (последние 10) ===")
    r = rows(
        "SELECT jobid, status, return_message, start_time, "
        "extract(epoch from (end_time - start_time))::int "
        "FROM cron.job_run_details ORDER BY start_time DESC LIMIT 10"
    )
    if r is not None:
        if not r:
            print("  пусто — ни один джоб ещё не запускался")
        for x in r:
            print(f"  #{x[0]} {x[1]} {x[4]}с {x[3]}")
            print(f"      {(x[2] or '')[:100]}")

    print("\n=== Права роли wiki на объекты cron ===")
    r = rows(
        "SELECT c.relname, "
        "has_table_privilege(current_user, c.oid, 'SELECT') AS sel, "
        "has_table_privilege(current_user, c.oid, 'INSERT') AS ins, "
        "has_table_privilege(current_user, c.oid, 'UPDATE') AS upd, "
        "has_table_privilege(current_user, c.oid, 'DELETE') AS del "
        "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
        "WHERE n.nspname = 'cron' AND c.relkind = 'r' ORDER BY c.relname"
    )
    if r is not None:
        for x in r:
            print(f"  {x[0]:<22} select={x[1]} insert={x[2]} update={x[3]} delete={x[4]}")

    print("\n=== Схема cron в пути поиска? ===")
    r = rows("SELECT current_setting('search_path')")
    if r is not None:
        print(f"  search_path: {r[0]}")

    print("\n=== Права wiki на чужие схемы (кто владелец postgres) ===")
    for sch in ("core", "meta", "derived", "marts", "pipeline"):
        r = rows(
            "SELECT has_schema_privilege(current_user, %s, 'USAGE') AS u, "
            "has_schema_privilege(current_user, %s, 'CREATE') AS c",
            (sch, sch),
        )
        if r is not None:
            print(f"  {sch:<10} usage={r[0][0]} create={r[0][1]}")

    print("\n=== Индексы kb: что уже есть ===")
    r = rows(
        "SELECT schemaname||'.'||tablename, indexname, "
        "pg_size_pretty(pg_relation_size(indexname::regclass)) "
        "FROM pg_indexes WHERE schemaname = 'kb' "
        "ORDER BY pg_relation_size(indexname::regclass) DESC LIMIT 8"
    )
    if r is not None:
        for x in r:
            print(f"  {x[1]:<44} {x[2]:>9}")

    print("\n=== Материализованные представления ===")
    r = rows(
        "SELECT n.nspname||'.'||c.relname, c.relispopulated "
        "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
        "WHERE c.relkind = 'm' ORDER BY 1"
    )
    if r is not None:
        if not r:
            print("  ни одного")
        for x in r:
            print(f"  {x[0]} populated={x[1]}")

    print("\n=== Триггеры в пользовательских схемах ===")
    r = rows(
        "SELECT n.nspname||'.'||c.relname||' → '||t.tgname "
        "FROM pg_trigger t JOIN pg_class c ON c.oid = t.tgrelid "
        "JOIN pg_namespace n ON n.oid = c.relnamespace "
        "WHERE NOT t.tgisinternal AND n.nspname NOT LIKE 'pg\\_%' "
        "ORDER BY 1 LIMIT 15"
    )
    if r is not None:
        if not r:
            print("  ни одного")
        for x in r:
            print(f"  {x[0]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())