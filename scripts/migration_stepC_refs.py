#!/usr/bin/env python3
"""Этап C: перенос справочников core -> catalog (единицы, источники,
частоты, регионы, релизы). ID сохраняются. Порядок обязателен: метрики
ссылаются на справочники, наблюдения — на метрики и релизы.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

# 0) расширить справочники колонками, которые есть в источнике
EXTEND = [
    ("catalog.unit + description", "ALTER TABLE catalog.unit ADD COLUMN IF NOT EXISTS description text"),
    ("catalog.unit + created_at", "ALTER TABLE catalog.unit ADD COLUMN IF NOT EXISTS created_at timestamptz"),
    ("catalog.source + publisher", "ALTER TABLE catalog.source ADD COLUMN IF NOT EXISTS publisher text"),
    ("catalog.source + license", "ALTER TABLE catalog.source ADD COLUMN IF NOT EXISTS license text"),
    ("catalog.source + reliability", "ALTER TABLE catalog.source ADD COLUMN IF NOT EXISTS reliability text"),
    ("catalog.source + is_active", "ALTER TABLE catalog.source ADD COLUMN IF NOT EXISTS is_active boolean"),
    ("catalog.source + created_at", "ALTER TABLE catalog.source ADD COLUMN IF NOT EXISTS created_at timestamptz"),
    ("catalog.region + valid_from", "ALTER TABLE catalog.region ADD COLUMN IF NOT EXISTS valid_from date"),
    ("catalog.region + valid_to", "ALTER TABLE catalog.region ADD COLUMN IF NOT EXISTS valid_to date"),
    ("catalog.region + aggregate_of", "ALTER TABLE catalog.region ADD COLUMN IF NOT EXISTS aggregate_of int"),
    ("catalog.region + created_at", "ALTER TABLE catalog.region ADD COLUMN IF NOT EXISTS created_at timestamptz"),
    ("catalog.release + ingested_at", "ALTER TABLE catalog.release ADD COLUMN IF NOT EXISTS ingested_at timestamptz"),
    ("catalog.release + url", "ALTER TABLE catalog.release ADD COLUMN IF NOT EXISTS url text"),
    ("catalog.release + notes", "ALTER TABLE catalog.release ADD COLUMN IF NOT EXISTS notes text"),
]
for label, sql in EXTEND:
    try:
        execute(sql)
    except Exception as e:
        print("ERR ", label, str(e)[:120])
print("расширение справочников: ок")

# 1) проверка, что ID помещаются в int приёмника
print("\n=== диапазоны ID источника ===")
for label, sql in [
    ("metric_id", "SELECT max(metric_id) FROM core.metric"),
    ("region_id", "SELECT max(region_id) FROM core.region"),
    ("source_id", "SELECT max(source_id) FROM core.source"),
    ("release_id", "SELECT max(release_id) FROM core.release"),
    ("unit_id", "SELECT max(unit_id) FROM core.unit"),
    ("frequency_id", "SELECT max(frequency_id) FROM core.frequency"),
]:
    print(f"   {label}: {query(sql)[0][0]}")

# 2) перенос (ID явно)
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
               status, ingested_at, url, notes FROM core.release
        ON CONFLICT (release_id) DO NOTHING"""),
]
for label, sql in MOVES:
    try:
        n = execute(sql)
        print(f"OK   {label}: вставлено {n}")
    except Exception as e:
        print(f"ERR  {label}: {str(e)[:200]}")

# 3) контроль
print("\n=== контроль справочников ===")
for src, dst in [("core.unit", "catalog.unit"), ("core.source", "catalog.source"),
                 ("core.frequency", "catalog.frequency"),
                 ("core.region", "catalog.region"),
                 ("core.release", "catalog.release")]:
    a = query(f"SELECT count(*) FROM {src}")[0][0]
    b = query(f"SELECT count(*) FROM {dst}")[0][0]
    mark = "OK " if a == b else "РАСХ"
    print(f"   {mark} {src} {a} -> {dst} {b}")