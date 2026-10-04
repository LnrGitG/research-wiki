#!/usr/bin/env python3
"""Из чего состоят 11 ГБ: живые данные, наследие, пустые но занятые таблицы."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import db_tunnel  # noqa: E402

GB = 1024 ** 3


def rows(sql, params=None):
    try:
        return db_tunnel.query(sql, params)
    except Exception as exc:  # noqa: BLE001
        print(f"  не прошло: {type(exc).__name__}: {str(exc).splitlines()[0]}")
        return None


print("=== Размер базы и что доступно для оценки распухания ===")
r = rows(
    "SELECT pg_size_pretty(pg_database_size(current_database())) AS db, "
    "current_setting('data_directory', true) AS datadir"
)
if r:
    print(f"  база: {r[0][0]}")
    print(f"  каталог данных: {r[0][1]}")

print("\n=== Таблицы, занявшие место при НУЛЕ живых строк ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname AS tbl, "
    "pg_total_relation_size(c.oid) AS bytes, "
    "coalesce(s.n_live_tup, -1) AS live, "
    "pg_size_pretty(pg_total_relation_size(c.oid)) AS pretty "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE c.relkind IN ('r','m','p') AND n.nspname NOT LIKE 'pg\\_%' "
    "AND coalesce(s.n_live_tup, 0) = 0 "
    "ORDER BY bytes DESC LIMIT 25"
)
total_empty = 0
if r is not None:
    for x in r:
        total_empty += x[1]
        print(f"  {x[0]:<50} {x[3]:>10} живых={x[2]}")
    print(f"  ИТОГО под пустыми объектами: {total_empty/GB:.2f} ГБ")

print("\n=== Полный список по размеру: топ-25 с числом строк ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname AS tbl, "
    "pg_size_pretty(pg_total_relation_size(c.oid)) AS pretty, "
    "pg_total_relation_size(c.oid) AS bytes, "
    "coalesce(s.n_live_tup,0) AS live, coalesce(s.n_dead_tup,0) AS dead "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE c.relkind IN ('r','m','p') AND n.nspname NOT LIKE 'pg\\_%' "
    "ORDER BY bytes DESC LIMIT 25"
)
if r:
    for x in r:
        print(f"  {x[0]:<44} {x[1]:>10} живых={x[3]:>9} мёртвых={x[4]:>8}")

print("\n=== Итог по схемам: сколько занято и сколько из этого пустое ===")
r = rows(
    "SELECT n.nspname, "
    "sum(pg_total_relation_size(c.oid)) AS bytes, "
    "sum(CASE WHEN coalesce(s.n_live_tup,0) = 0 "
    "    THEN pg_total_relation_size(c.oid) ELSE 0 END) AS empty_bytes, "
    "count(*) AS objs "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE c.relkind IN ('r','m','p') AND n.nspname NOT LIKE 'pg\\_%' "
    "GROUP BY n.nspname ORDER BY bytes DESC"
)
if r:
    print(f"  {'схема':<14} {'занято':>10} {'из них пусто':>14} {'объектов':>9}")
    tot = 0
    tot_empty = 0
    for x in r:
        tot += x[1]
        tot_empty += x[2]
        print(f"  {x[0]:<14} {x[1]/GB:>9.2f} ГБ {x[2]/GB:>12.2f} ГБ {x[3]:>9}")
    print(f"  {'ИТОГО':<14} {tot/GB:>9.2f} ГБ {tot_empty/GB:>12.2f} ГБ")

print("\n=== Наследие: сколько занимает и живо ли ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, "
    "pg_size_pretty(pg_total_relation_size(c.oid)), "
    "coalesce(s.n_live_tup,0), coalesce(s.n_tup_ins,0), coalesce(s.n_tup_upd,0), "
    "coalesce(s.idx_scan,0) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE (c.relname LIKE '%legacy%' OR c.relname LIKE '%\\_old' "
    "   OR c.relname LIKE '%\\_v2' OR c.relname LIKE '%stage%') "
    "AND c.relkind IN ('r','m','p') ORDER BY pg_total_relation_size(c.oid) DESC LIMIT 20"
)
if r:
    print(f"  {'объект':<44} {'размер':>10} {'живых':>9} {'вставок':>9} {'обновл':>8} {'чтений(инд)':>11}")
    for x in r:
        print(f"  {x[0]:<44} {x[1]:>10} {x[2]:>9} {x[3]:>9} {x[4]:>8} {x[5]:>11}")

print("\n=== Содержимое схемы marts (нам закрыта, но каталог читаем) ===")
r = rows(
    "SELECT c.relkind, n.nspname||'.'||c.relname, "
    "pg_size_pretty(pg_total_relation_size(c.oid)), "
    "coalesce(s.n_live_tup,0), pg_get_userbyid(c.relowner) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE n.nspname = 'marts' ORDER BY pg_total_relation_size(c.oid) DESC LIMIT 20"
)
if r is not None:
    if not r:
        print("  схема marts пуста — ни одного объекта")
    for x in r:
        kind = {"r": "таблица", "m": "матпредставление", "v": "представление",
                "p": "партиц.", "S": "последовательность", "i": "индекс"}.get(x[0], x[0])
        print(f"  [{kind}] {x[1]:<40} {x[2]:>10} строк={x[3]:>8} владелец={x[4]}")

print("\n=== Партиции data.observation: размеры по годам ===")
r = rows(
    "SELECT c.relname, pg_size_pretty(pg_total_relation_size(c.oid)), "
    "coalesce(s.n_live_tup,0), coalesce(s.n_dead_tup,0) "
    "FROM pg_inherits i JOIN pg_class c ON c.oid = i.inhrelid "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE i.inhparent = 'data.observation'::regclass "
    "ORDER BY pg_total_relation_size(c.oid) DESC LIMIT 12"
)
if r is not None:
    for x in r:
        print(f"  {x[0]:<34} {x[1]:>10} живых={x[2]:>8} мёртвых={x[3]:>7}")

print("\n=== Индексы: сколько места съедают ===")
r = rows(
    "SELECT n.nspname, sum(pg_relation_size(c.oid)) AS idx_bytes "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relkind = 'i' AND n.nspname NOT LIKE 'pg\\_%' "
    "GROUP BY n.nspname ORDER BY idx_bytes DESC LIMIT 10"
)
if r:
    for x in r:
        print(f"  {x[0]:<16} индексы: {x[1]/GB:.2f} ГБ")