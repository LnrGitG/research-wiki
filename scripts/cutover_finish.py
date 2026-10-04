#!/usr/bin/env python3
"""Завершение переключения: создать 6 представлений в core и пересоздать
зависимые представления, чтобы они смотрели на новые, а не на *_legacy."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

DEP_VIEWS = ["core.v_datalens_observations",
             "derived.v_catalog_active",
             "derived.v_metric_semantic"]

# 1) снять определения зависимых (сейчас они смотрят на legacy-таблицы)
defs = {}
for v in DEP_VIEWS:
    try:
        defs[v] = query("SELECT pg_get_viewdef(%s::regclass, true)", (v,))[0][0]
        print(f"сохранено определение {v}")
    except Exception as e:
        print(f"ERR {v}: {str(e)[:120]}")

# 2) создать представления
VIEWS = {
 "metric": """CREATE OR REPLACE VIEW core.metric AS
     SELECT metric_id, metric_code, name_ru, short_name_ru, description,
            unit_id, frequency_id, metric_type, index_base, is_derived,
            formula_text, status, tags, released_at AS created_at
     FROM catalog.metric""",
 "source": """CREATE OR REPLACE VIEW core.source AS
     SELECT source_id, source_code, name_ru, publisher, url, license,
            reliability, is_active, created_at
     FROM catalog.source""",
 "release": """CREATE OR REPLACE VIEW core.release AS
     SELECT release_id, source_id, label AS release_label, published_at,
            ingested_at, url, content_hash, status, notes
     FROM catalog.release""",
 "region": """CREATE OR REPLACE VIEW core.region AS
     SELECT region_id, region_code, name_ru, short_name, level, parent_id,
            is_active, valid_from, valid_to, oktmo, okato, iso_code,
            created_at, aggregation, aggregate_of
     FROM catalog.region""",
 "unit": """CREATE OR REPLACE VIEW core.unit AS
     SELECT unit_id, unit_code, name_ru, description, created_at
     FROM catalog.unit""",
 "frequency": """CREATE OR REPLACE VIEW core.frequency AS
     SELECT frequency_id, freq_code AS frequency_code, name_ru,
            period_type, months_per_period
     FROM catalog.frequency""",
}
print("\n--- создание представлений ---")
for t, sql in VIEWS.items():
    try:
        execute(sql)
        print(f"   core.{t}: ок")
    except Exception as e:
        print(f"   ERR core.{t}: {str(e)[:200]}")

# 3) пересоздать зависимые представления поверх новых
print("\n--- зависимые представления ---")
for v, d in defs.items():
    sch, name = v.split(".")
    try:
        execute(f"CREATE OR REPLACE VIEW {sch}.{name} AS {d}")
        print(f"   {v}: пересоздано")
    except Exception as e:
        print(f"   ERR {v}: {str(e)[:220]}")

# 4) проверка
print("\n--- проверка ---")
pairs = [("core.observation_v2", "data.observation"),
         ("core.metric", "catalog.metric"),
         ("core.source", "catalog.source"),
         ("core.release", "catalog.release"),
         ("core.region", "catalog.region"),
         ("core.unit", "catalog.unit"),
         ("core.frequency", "catalog.frequency")]
allok = True
for a, b in pairs:
    try:
        na = query(f"SELECT count(*) FROM {a}")[0][0]
        nb = query(f"SELECT count(*) FROM {b}")[0][0]
        good = na == nb
        allok = allok and good
        print(f"   {'OK ' if good else 'РАСХ'} {a} {na:,} = {b} {nb:,}")
    except Exception as e:
        allok = False
        print(f"   ERR {a}: {str(e)[:140]}")

print("\n--- зависимые представления читаются ---")
for v in DEP_VIEWS:
    try:
        n = query(f"SELECT count(*) FROM {v}")[0][0]
        print(f"   OK {v}: {n:,} строк")
    except Exception as e:
        allok = False
        print(f"   ERR {v}: {str(e)[:160]}")

print("\nпереключение", "ПРОШЛО" if allok else "ТРЕБУЕТ ВНИМАНИЯ")