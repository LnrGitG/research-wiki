#!/usr/bin/env python3
"""Точечные вопросы к базе: существующий триггер, статистика запросов, партиции."""
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


print("=== Что делает существующий триггер trg_observation_change ===")
r = rows(
    "SELECT p.proname, pg_get_functiondef(p.oid) "
    "FROM pg_trigger t JOIN pg_proc p ON p.oid = t.tgfoid "
    "WHERE t.tgname = 'trg_observation_change'"
)
if r:
    for x in r:
        print(f"  функция: {x[0]}")
        for line in (x[1] or "").splitlines()[:22]:
            print(f"    {line}")

print("\n=== Партиционирование: есть ли partitioned-таблицы ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, c.relkind, "
    "pg_get_partkeydef(c.oid) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relkind = 'p' ORDER BY 1"
)
if r is not None:
    if not r:
        print("  ни одной партиционированной таблицы")
    for x in r:
        print(f"  {x[0]}  ключ: {x[2]}")

print("\n=== Число секций-наследников у крупных таблиц ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, count(i.inhrelid) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "LEFT JOIN pg_inherits i ON i.inhparent = c.oid "
    "WHERE c.relkind IN ('p','r') AND n.nspname NOT LIKE 'pg\\_%' "
    "GROUP BY 1 HAVING count(i.inhrelid) > 0 ORDER BY 2 DESC LIMIT 10"
)
if r is not None:
    if not r:
        print("  наследования нет — всё плоскими таблицами")
    for x in r:
        print(f"  {x[0]:<44} секций: {x[1]}")

print("\n=== pg_stat_statements: годится ли для разбора наследия ===")
r = rows("SELECT count(*) FROM pg_stat_statements")
if r:
    print(f"  записей: {r[0][0]}")
r = rows(
    "SELECT calls, round(total_exec_time)::bigint, "
    "round(mean_exec_time::numeric, 1), rows, "
    "left(regexp_replace(query, '\\s+', ' ', 'g'), 88) "
    "FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 10"
)
if r:
    print("  топ-10 по суммарному времени:")
    for x in r:
        print(f"    вызовов={x[0]:>7} всего={x[1]:>8}мс среднее={x[2]:>8}мс строк={x[3]}")
        print(f"      {x[4]}")

print("\n=== Наследственные объекты: кто ещё читает/пишет ===")
r = rows(
    "SELECT schemaname||'.'||relname, seq_scan, idx_scan, n_tup_ins, n_tup_upd "
    "FROM pg_stat_user_tables WHERE relname LIKE '%legacy%' OR relname LIKE '%old%' "
    "ORDER BY seq_scan DESC LIMIT 8"
)
if r is not None:
    for x in r:
        print(f"  {x[0]:<42} seq={x[1]:>6} idx={x[2]:>6} ins={x[3]:>8} upd={x[4]:>6}")

print("\n=== Есть ли внутрибазовые события: слушатели LISTEN ===")
r = rows(
    "SELECT pid, usename, application_name, state, left(query,60) "
    "FROM pg_stat_activity WHERE state IS NOT NULL ORDER BY state LIMIT 10"
)
if r is not None:
    print(f"  живых соединений: {len(r)}")
    for x in r:
        print(f"  pid={x[0]} {x[1]} {x[3]} | {x[4]}")

print("\n=== Размеры схем (кто занимает 11 ГБ) ===")
r = rows(
    "SELECT schemaname, pg_size_pretty(sum(pg_total_relation_size(relid))) "
    "FROM pg_stat_user_tables GROUP BY schemaname "
    "ORDER BY sum(pg_total_relation_size(relid)) DESC LIMIT 12"
)
if r:
    for x in r:
        print(f"  {x[0]:<20} {x[1]:>10}")