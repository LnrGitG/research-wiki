#!/usr/bin/env python3
"""Одно ли хранилище под разными именами и кто читает наследие."""
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


print("=== Что за объекты core.observation_v2 и data.observation ===")
r = rows(
    "SELECT n.nspname, c.relname, c.relkind, c.oid, "
    "pg_get_userbyid(c.relowner) AS owner, "
    "pg_size_pretty(pg_total_relation_size(c.oid)) AS total, "
    "c.relispartition "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE (n.nspname='core' AND c.relname='observation_v2') "
    "   OR (n.nspname='data' AND c.relname='observation')"
)
if r:
    kinds = {"r": "таблица", "p": "партиционированная", "v": "ПРЕДСТАВЛЕНИЕ",
             "m": "матпредставление", "f": "foreign"}
    for x in r:
        print(f"  {x[0]}.{x[1]:<16} [{kinds.get(x[2], x[2])}] oid={x[3]} "
              f"владелец={x[4]} размер={x[5]} партиция={x[6]}")

print("\n=== Если представление — показываем его определение ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, pg_get_viewdef(c.oid, true) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relkind IN ('v','m') AND (c.relname LIKE '%observation%')"
)
if r is not None:
    if not r:
        print("  представлений с таким именем нет — значит это физическая таблица")
    for x in r:
        print(f"  {x[0]}:")
        for line in (x[1] or "").splitlines()[:12]:
            print(f"    {line}")

print("\n=== Родословная: наследие вложено в текущее? ===")
for tbl, col in (("core.observation_v2_old", "old"), ("v2.observation", "v2")):
    r = rows(f"SELECT count(*) FROM {tbl}")
    if r is None:
        continue
    total = r[0][0]
    r2 = rows(
        f"SELECT count(*) FROM {tbl} t WHERE NOT EXISTS "
        "(SELECT 1 FROM core.observation_v2 c WHERE c.metric_id = t.metric_id "
        "AND c.region_id = t.region_id AND c.period_start = t.period_start)"
    )
    if r2 is not None:
        extra = r2[0][0]
        verdict = "вложена ЦЕЛИКОМ" if extra == 0 else f"есть {extra} своих строк"
        print(f"  {tbl:<28} строк={total:>9} — {verdict}")

print("\n=== Кто читает наследие: запросы с ним в тексте ===")
r = rows(
    "SELECT calls, rows, "
    "left(regexp_replace(query, '\\s+', ' ', 'g'), 105) "
    "FROM pg_stat_statements "
    "WHERE query ILIKE '%observation_v2_legacy%' "
    "ORDER BY calls DESC LIMIT 10"
)
if r is not None:
    if not r:
        print("  в текстах запросов наследие не встречается")
    for x in r:
        print(f"  вызовов={x[0]:>8} строк={x[1]:>9}")
        print(f"      {x[2]}")

print("\n=== Кто читает data.observation / core.observation_v2 ===")
r = rows(
    "SELECT calls, rows, "
    "left(regexp_replace(query, '\\s+', ' ', 'g'), 100) "
    "FROM pg_stat_statements "
    "WHERE query ILIKE '%data.observation%' OR query ILIKE '%core.observation_v2%' "
    "ORDER BY calls DESC LIMIT 8"
)
if r is not None:
    for x in r:
        print(f"  вызовов={x[0]:>8} строк={x[1]:>9}")
        print(f"      {x[2]}")

print("\n=== Индексы core.observation_v2 (текущей) ===")
r = rows(
    "SELECT indexrelname, pg_size_pretty(pg_relation_size(indexrelid)), idx_scan "
    "FROM pg_stat_user_indexes WHERE relname = 'observation_v2' "
    "ORDER BY pg_relation_size(indexrelid) DESC"
)
if r is not None:
    if not r:
        print("  индексной статистики нет (таблица-партиция или иное)")
    for x in r:
        print(f"  {x[0]:<62} {x[1]:>9} прочтений={x[2]}")