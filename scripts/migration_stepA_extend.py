#!/usr/bin/env python3
"""Этап A: расширение схемы-приёмника. Ничего не удаляет.

- data.observation: добавляет колонки, которые есть в источнике и которых нет
  в приёмнике (value_str, frequency_id, source_id, quality_flags,
  sub_dimension, notes, created_at);
- catalog.metric: добавляет short_name_ru, description, metric_type,
  index_base, is_derived, formula_text, status;
- catalog.region: новая таблица-справочник регионов;
- ослабляет CHECK на metric_code, чтобы прошли коды с дефисом.
Идемпотентно: повторный запуск ничего не ломает.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

STEPS = [
    ("data.observation + value_str",
     "ALTER TABLE data.observation ADD COLUMN IF NOT EXISTS value_str text"),
    ("data.observation + frequency_id",
     "ALTER TABLE data.observation ADD COLUMN IF NOT EXISTS frequency_id int"),
    ("data.observation + source_id",
     "ALTER TABLE data.observation ADD COLUMN IF NOT EXISTS source_id int"),
    ("data.observation + quality_flags",
     "ALTER TABLE data.observation ADD COLUMN IF NOT EXISTS quality_flags text[]"),
    ("data.observation + sub_dimension",
     "ALTER TABLE data.observation ADD COLUMN IF NOT EXISTS sub_dimension text"),
    ("data.observation + notes",
     "ALTER TABLE data.observation ADD COLUMN IF NOT EXISTS notes text"),
    ("data.observation + created_at",
     "ALTER TABLE data.observation ADD COLUMN IF NOT EXISTS created_at timestamptz"),
    ("catalog.metric + short_name_ru",
     "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS short_name_ru text"),
    ("catalog.metric + description",
     "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS description text"),
    ("catalog.metric + metric_type",
     "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS metric_type text"),
    ("catalog.metric + index_base",
     "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS index_base text"),
    ("catalog.metric + is_derived",
     "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS is_derived boolean"),
    ("catalog.metric + formula_text",
     "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS formula_text text"),
    ("catalog.metric + status",
     "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS status text"),
    ("catalog.region (новая)",
     """CREATE TABLE IF NOT EXISTS catalog.region (
            region_id   serial PRIMARY KEY,
            region_code text UNIQUE NOT NULL,
            name_ru     text NOT NULL,
            short_name  text,
            level       text,
            parent_id   int,
            is_active   boolean,
            oktmo       text,
            okato       text,
            iso_code    text,
            aggregation text
        )"""),
]

for label, sql in STEPS:
    try:
        execute(sql)
        print("OK  ", label)
    except Exception as e:
        print("ERR ", label, "->", str(e)[:150])

# --- ослабить CHECK на metric_code: разрешить дефис ---
print("\n--- CHECK на catalog.metric.metric_code ---")
rows = query("""SELECT con.conname, pg_get_constraintdef(con.oid)
                FROM pg_constraint con
                JOIN pg_class c ON c.oid = con.conrelid
                JOIN pg_namespace n ON n.oid = c.relnamespace
                WHERE n.nspname='catalog' AND c.relname='metric'
                  AND con.contype='c'""")
for name, ddl in rows:
    print(f"   {name}: {ddl}")
    if "metric_code" in ddl:
        try:
            execute(f'ALTER TABLE catalog.metric DROP CONSTRAINT "{name}"')
            print("   снято:", name)
        except Exception as e:
            print("   ERR снятия:", str(e)[:120])

try:
    execute("""ALTER TABLE catalog.metric
               ADD CONSTRAINT catalog_metric_code_chk
               CHECK (metric_code ~ '^[a-z0-9_-]+$')""")
    print("   новое правило: строчные латинские, цифры, подчёркивание и дефис")
except Exception as e:
    print("   ERR нового правила:", str(e)[:150])

# --- внешний ключ на регион ---
try:
    execute("""ALTER TABLE data.observation
               ADD CONSTRAINT observation_region_fk
               FOREIGN KEY (region_id) REFERENCES catalog.region(region_id)""")
    print("OK   FK data.observation.region_id -> catalog.region")
except Exception as e:
    print("FK   (пропущено):", str(e)[:150])

print("\n--- итоговые колонки ---")
for t, s in (("observation", "data"), ("metric", "catalog"), ("region", "catalog")):
    cs = [r[0] for r in query(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_schema=%s AND table_name=%s ORDER BY ordinal_position", (s, t))]
    print(f"   {s}.{t}: {len(cs)} колонок")