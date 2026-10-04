#!/usr/bin/env python3
"""Этап C-2: устранить препятствия переноса справочников.

Причины прошлых ошибок:
 1) в catalog.unit/source/frequency были предзаполнены строки-заглушки с
    кодами ('percent','rosstat','Q' и т.п.) и другими ID — они конфликтуют
    с реальными кодами. На заглушки ничего не ссылается (catalog.metric и
    data.observation пусты), поэтому их можно убрать;
 2) catalog.region.aggregate_of объявлен int, а в источнике это text;
 3) catalog.release.content_hash NOT NULL, а в исторических релизах бывает NULL.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

print("=== зависимости от справочников (должны быть нулевыми) ===")
print("   catalog.metric:", query("SELECT count(*) FROM catalog.metric")[0][0])
print("   data.observation:", query("SELECT count(*) FROM data.observation")[0][0])
print("   catalog.release:", query("SELECT count(*) FROM catalog.release")[0][0])

FIXES = [
    ("region.aggregate_of -> text",
     "ALTER TABLE catalog.region ALTER COLUMN aggregate_of TYPE text USING aggregate_of::text"),
    ("release.content_hash -> nullable",
     "ALTER TABLE catalog.release ALTER COLUMN content_hash DROP NOT NULL"),
    ("release.status -> default",
     "ALTER TABLE catalog.release ALTER COLUMN status SET DEFAULT 'registered'"),
]
for label, sql in FIXES:
    try:
        execute(sql)
        print("OK  ", label)
    except Exception as e:
        print("ERR ", label, str(e)[:140])

print("\n=== убрать заглушки справочников ===")
for tbl, n in (("catalog.unit", 4), ("catalog.source", 5), ("catalog.frequency", 5)):
    try:
        before = query(f"SELECT count(*) FROM {tbl}")[0][0]
        execute(f"DELETE FROM {tbl}")
        after = query(f"SELECT count(*) FROM {tbl}")[0][0]
        print(f"   {tbl}: {before} -> {after}")
    except Exception as e:
        print(f"   ERR {tbl}: {str(e)[:140]}")

print("\n=== повторный перенос справочников ===")
MOVES = [
    ("catalog.unit", """INSERT INTO catalog.unit
        (unit_id, unit_code, name_ru, description, created_at)
        SELECT unit_id, unit_code, name_ru, description, created_at FROM core.unit
        ON CONFLICT (unit_id) DO NOTHING"""),
    ("catalog.source", """INSERT INTO catalog.source
        (source_id, source_code, name_ru, url, publisher, license, reliability,
         is_active, created_at)
        SELECT source_id, source_code, name_ru, url, publisher, license,
               reliability, is_active, created_at FROM core.source
        ON CONFLICT (source_id) DO NOTHING"""),
    ("catalog.frequency", """INSERT INTO catalog.frequency
        (frequency_id, freq_code, name_ru, period_type, months_per_period)
        SELECT frequency_id, frequency_code, name_ru, period_type, months_per_period
        FROM core.frequency
        ON CONFLICT (frequency_id) DO NOTHING"""),
    ("catalog.region", """INSERT INTO catalog.region
        (region_id, region_code, name_ru, short_name, level, parent_id, is_active,
         oktmo, okato, iso_code, aggregation, valid_from, valid_to, aggregate_of,
         created_at)
        SELECT region_id, region_code, name_ru, short_name, level, parent_id,
               is_active, oktmo, okato, iso_code, aggregation, valid_from,
               valid_to, aggregate_of, created_at FROM core.region
        ON CONFLICT (region_id) DO NOTHING"""),
    ("catalog.release", """INSERT INTO catalog.release
        (release_id, source_id, label, published_at, content_hash, status,
         ingested_at, url, notes)
        SELECT release_id, source_id, release_label, published_at, content_hash,
               coalesce(status,'registered'), ingested_at, url, notes
        FROM core.release
        ON CONFLICT (release_id) DO NOTHING"""),
]
for label, sql in MOVES:
    try:
        n = execute(sql)
        print(f"OK   {label}: вставлено {n}")
    except Exception as e:
        print(f"ERR  {label}: {str(e)[:200]}")

print("\n=== контроль ===")
for src, dst in [("core.unit", "catalog.unit"), ("core.source", "catalog.source"),
                 ("core.frequency", "catalog.frequency"),
                 ("core.region", "catalog.region"),
                 ("core.release", "catalog.release")]:
    a = query(f"SELECT count(*) FROM {src}")[0][0]
    b = query(f"SELECT count(*) FROM {dst}")[0][0]
    print(f"   {'OK ' if a == b else 'РАСХ'} {src} {a} -> {dst} {b}")