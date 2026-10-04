#!/usr/bin/env python3
"""Сколько база набирает за месяц и что даёт каждое поколение таблиц."""
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


print("=== Свежие партиции: что набирается сейчас ===")
r = rows(
    "SELECT c.relname, pg_size_pretty(pg_total_relation_size(c.oid)), "
    "coalesce(s.n_live_tup,0) "
    "FROM pg_inherits i JOIN pg_class c ON c.oid = i.inhrelid "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE i.inhparent = 'data.observation'::regclass "
    "ORDER BY c.relname DESC LIMIT 10"
)
if r:
    for x in r:
        print(f"  {x[0]:<30} {x[1]:>9} строк~{x[2]:>8}")

print("\n=== Разброс периодов в живом хранилище ===")
r = rows(
    "SELECT min(period_start), max(period_start), count(*) "
    "FROM data.observation"
)
if r:
    print(f"  от {r[0][0]} до {r[0][1]}, всего строк {r[0][2]}")

print("\n=== Сколько строк приходится на последние годы ===")
r = rows(
    "SELECT extract(year from period_start)::int AS yr, count(*), "
    "pg_size_pretty(sum(pg_column_size(period_start))) AS грубо "
    "FROM data.observation WHERE period_start >= '2024-01-01' "
    "GROUP BY 1 ORDER BY 1"
)
if r:
    for x in r:
        print(f"  {x[0]}: {x[1]:>9} строк")

print("\n=== Таблица-наследие: что известно о её создании ===")
r = rows(
    "SELECT stats_reset FROM pg_stat_database WHERE datname = current_database()"
)
if r:
    print(f"  статистика базы сброшена: {r[0][0]}")

print("\n=== Совокупный вес поколений наблюдений ===")
gens = [
    ("data.observation (живое хранилище)", 2520),
    ("core.observation_v2_legacy (артефакт миграции)", 3431),
    ("core.observation_v2_old (990k строк)", 442),
    ("v2.observation (428k строк)", 138),
]
s = 0
for name, mb in gens:
    s += mb
    print(f"  {name:<46} {mb:>5} МБ")
print(f"  ИТОГО: {s} МБ = {s/1024:.2f} ГБ из ~11 ГБ базы")

print("\n=== Итог по возможному освобождению ===")
r = rows(
    "SELECT pg_size_pretty(pg_total_relation_size('core.observation_v2_legacy')), "
    "pg_size_pretty(pg_indexes_size('core.observation_v2_legacy'))"
)
if r:
    print(f"  наследие целиком: {r[0][0]}, из них индексы: {r[0][1]}")
r = rows(
    "SELECT pg_size_pretty(sum(pg_total_relation_size(c.oid))) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE n.nspname IN ('staging','v2_stage') AND c.relkind = 'r'"
)
if r:
    print(f"  схемы staging+v2_stage целиком: {r[0][0]}")