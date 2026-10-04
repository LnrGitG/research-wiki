#!/usr/bin/env python3
"""Уточняющие вопросы: реестры метрик, наличие внешнего ключа, жив ли артефакт миграции."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import db_tunnel  # noqa: E402


def rows(sql, params=None):
    try:
        return db_tunnel.query(sql, params)
    except Exception as exc:  # noqa: BLE001
        print(f"  не прошло: {type(exc).__name__}: {str(exc).splitlines()[0]}")
        return None


print("=== Три реестра метрик: что это физически ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, c.relkind, "
    "pg_size_pretty(pg_total_relation_size(c.oid)), c.reltuples::bigint, "
    "pg_get_userbyid(c.relowner) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relname = 'metric' AND n.nspname IN ('core','v2','catalog') "
    "ORDER BY n.nspname"
)
if r:
    kinds = {"r": "таблица", "v": "ПРЕДСТАВЛЕНИЕ", "p": "партиц.", "m": "матпредст."}
    for x in r:
        print(f"  {x[0]:<20} [{kinds.get(x[1], x[1]):<13}] {x[2]:>9} ~строк={x[3]:>7} владелец={x[4]}")

print("\n=== Внешние ключи: есть ли защита наблюдений ===")
r = rows(
    "SELECT conrelid::regclass::text AS tbl, conname, "
    "pg_get_constraintdef(oid), convalidated "
    "FROM pg_constraint WHERE contype = 'f' "
    "AND (conrelid::regclass::text LIKE '%observation%' "
    "  OR confrelid::regclass::text LIKE '%observation%') "
    "ORDER BY 1"
)
if r is not None:
    if not r:
        print("  ВНЕШНИХ КЛЮЧЕЙ НЕТ — ни одного, во всей базе ни на наблюдениях")
    for x in r:
        print(f"  {x[0]:<40} {x[1]:<34} проверен={x[3]}")

print("\n=== Все внешние ключи в базе (сколько их вообще) ===")
r = rows(
    "SELECT count(*), count(*) FILTER (WHERE NOT convalidated) "
    "FROM pg_constraint WHERE contype = 'f'"
)
if r:
    print(f"  всего внешних ключей: {r[0][0]}, из них непроверенных: {r[0][1]}")

print("\n=== CHECK-ограничения ===")
r = rows(
    "SELECT n.nspname, count(*) FROM pg_constraint k "
    "JOIN pg_class c ON c.oid = k.conrelid "
    "JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE k.contype = 'c' AND n.nspname NOT LIKE 'pg\\_%' "
    "GROUP BY n.nspname ORDER BY 2 DESC"
)
if r is not None:
    if not r:
        print("  CHECK-ограничений нет")
    for x in r:
        print(f"  {x[0]:<16} {x[1]}")

print("\n=== Артефакт миграции: читается ли он СЕЙЧАС ===")
r = rows(
    "SELECT pid, state, extract(epoch from (now() - query_start))::int AS сек, "
    "left(regexp_replace(query, '\\s+',' ','g'), 80) "
    "FROM pg_stat_activity WHERE datname = current_database() AND pid <> pg_backend_pid()"
)
if r is not None:
    if not r:
        print("  других соединений нет — артефакт не читается никем прямо сейчас")
    for x in r:
        print(f"  pid={x[0]} {x[1]} {x[2]}с: {x[3]}")

print("\n=== Сброс статистики: с какого момента считаются прочтения ===")
r = rows("SELECT stats_reset FROM pg_stat_database WHERE datname = current_database()")
if r:
    print(f"  статистика базы: {r[0][0]}")

print("\n=== Живут ли имена v3 (следы миграции) ===")
r = rows(
    "SELECT n.nspname, c.relname FROM pg_class c "
    "JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relname LIKE '%v3%' OR c.relname LIKE '%\\_v2\\_legacy%' "
    "ORDER BY 1, 2 LIMIT 15"
)
if r is not None:
    if not r:
        print("  объектов с v3 в имени нет")
    for x in r:
        print(f"  {x[0]}.{x[1]}")

print("\n=== Схема ops: что там (она наша, может принять политику) ===")
r = rows(
    "SELECT c.relkind, c.relname, pg_size_pretty(pg_total_relation_size(c.oid)) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE n.nspname = 'ops' ORDER BY 1, 2"
)
if r is not None:
    if not r:
        print("  ops пуста")
    for x in r:
        print(f"  [{x[0]}] {x[1]:<40} {x[2]}")

print("\n=== meta.catalog_policy: существует ли уже ===")
r = rows(
    "SELECT c.relkind, pg_size_pretty(pg_total_relation_size(c.oid)), c.reltuples::bigint "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE n.nspname='meta' ORDER BY c.relname"
)
if r is not None:
    for x in r:
        print(f"  meta: [{x[0]}] {x[1]:>9} ~строк={x[2]}")