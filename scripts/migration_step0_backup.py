#!/usr/bin/env python3
"""Шаг 0: точка возврата. Фиксирует предсостояние БД перед переездом.

Пишет снапшот схем/таблиц/счётчиков в файл. Данные старой схемы (core, v2,
dkp) не трогаются вовсе — откат = удаление catalog/data/derived-новых.
"""
import json
import sys
from datetime import datetime, timezone

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

OUT = "/home/lnr/research-wiki-private/backups/pre_migration_catalog_20261004.json"

snap = {"taken_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": "предсостояние перед переездом core -> catalog/data",
        "schemas": {}, "row_counts": {}}

rows = query("""SELECT nspname FROM pg_namespace
                WHERE nspname NOT LIKE 'pg_%' AND nspname <> 'information_schema'
                ORDER BY 1""")
snap["schemas"]["all"] = [r[0] for r in rows]

for sch in ("catalog", "data", "derived", "core", "v2", "dkp", "public"):
    rows = query("""SELECT table_name FROM information_schema.tables
                    WHERE table_schema=%s ORDER BY 1""", (sch,))
    snap["schemas"][sch] = [r[0] for r in rows]

for label, sql in [
    ("core.observation_v2", "SELECT count(*) FROM core.observation_v2"),
    ("core.metric", "SELECT count(*) FROM core.metric"),
    ("core.region", "SELECT count(*) FROM core.region"),
    ("core.source", "SELECT count(*) FROM core.source"),
    ("core.unit", "SELECT count(*) FROM core.unit"),
    ("core.frequency", "SELECT count(*) FROM core.frequency"),
    ("core.release", "SELECT count(*) FROM core.release"),
    ("catalog.metric", "SELECT count(*) FROM catalog.metric"),
    ("catalog.source", "SELECT count(*) FROM catalog.source"),
    ("catalog.unit", "SELECT count(*) FROM catalog.unit"),
    ("catalog.frequency", "SELECT count(*) FROM catalog.frequency"),
    ("catalog.release", "SELECT count(*) FROM catalog.release"),
    ("data.observation", "SELECT count(*) FROM data.observation"),
    ("dkp.meeting", "SELECT count(*) FROM dkp.meeting"),
    ("v2.metric", "SELECT count(*) FROM v2.metric"),
]:
    try:
        snap["row_counts"][label] = query(sql)[0][0]
    except Exception as e:
        snap["row_counts"][label] = f"ERR {str(e)[:60]}"

# распределение по годам — чтобы после переезда сверить построчно
snap["by_year"] = {str(r[0]): r[1] for r in query(
    "SELECT date_part('year', period_start)::int, count(*) "
    "FROM core.observation_v2 GROUP BY 1 ORDER BY 1")}

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(snap, f, ensure_ascii=False, indent=2)

print("точка возврата записана:", OUT)
print("схем:", len(snap["schemas"]["all"]))
for k, v in snap["row_counts"].items():
    print(f"  {k}: {v}")
print("лет в распределении:", len(snap["by_year"]),
      "| всего строк:", sum(snap["by_year"].values()))