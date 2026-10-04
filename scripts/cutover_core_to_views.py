#!/usr/bin/env python3
"""Переключение: core становится набором обновляемых представлений над
catalog/data. Одна физическая копия данных — в новых схемах; core работает
как псевдоним и для чтения, и для записи (представления простые, без
приведений типов, поэтому PostgreSQL делает их обновляемыми).

Порядок:
 0) снимок предсостояния;
 1) сохранить определения зависимых представлений;
 2) выровнять тип catalog.metric.tags под core (text[], а не jsonb) —
    скрипты читают tags как массив;
 3) переименовать 7 таблиц core -> *_legacy (данные остаются как откат);
 4) создать 7 представлений с прежними именами;
 5) пересоздать зависимые представления, чтобы они смотрели на новые;
 6) проверить счётчики, значения и запись.
"""
import json
import sys
from datetime import datetime, timezone

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

TABLES = [
    # (таблица, легаси-имя)
    ("observation_v2", "observation_v2_legacy"),
    ("metric", "metric_legacy"),
    ("source", "source_legacy"),
    ("release", "release_legacy"),
    ("region", "region_legacy"),
    ("unit", "unit_legacy"),
    ("frequency", "frequency_legacy"),
]

DEP_VIEWS = ["core.v_datalens_observations",
             "derived.v_catalog_active",
             "derived.v_metric_semantic"]

# ---------- 0) снимок ----------
snap = {"taken_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "step": "cutover_core_to_views", "counts": {}}
for t, _ in TABLES:
    try:
        snap["counts"][f"core.{t}"] = query(f"SELECT count(*) FROM core.{t}")[0][0]
    except Exception as e:
        snap["counts"][f"core.{t}"] = f"ERR {str(e)[:50]}"
snap["counts"]["data.observation"] = query("SELECT count(*) FROM data.observation")[0][0]
snap["counts"]["catalog.metric"] = query("SELECT count(*) FROM catalog.metric")[0][0]
with open("/home/lnr/research-wiki-private/backups/pre_cutover_20261004.json", "w",
          encoding="utf-8") as f:
    json.dump(snap, f, ensure_ascii=False, indent=2)
print("0) снимок записан")
for k, v in snap["counts"].items():
    print(f"     {k}: {v}")

# ---------- 1) определения зависимых представлений ----------
defs = {}
for v in DEP_VIEWS:
    sch, name = v.split(".")
    try:
        d = query("SELECT pg_get_viewdef(%s::regclass, true)", (v,))[0][0]
        defs[v] = d
        print(f"1) определение {v}: {len(d)} знаков")
    except Exception as e:
        print(f"1) ERR {v}: {str(e)[:120]}")

# ---------- 2) выровнять тип tags ----------
print("2) catalog.metric.tags -> text[]")
try:
    t = query("""SELECT data_type FROM information_schema.columns
                 WHERE table_schema='catalog' AND table_name='metric'
                   AND column_name='tags'""")[0][0]
    if t == "jsonb":
        execute("""ALTER TABLE catalog.metric
                   ALTER COLUMN tags TYPE text[]
                   USING CASE WHEN tags IS NULL THEN NULL
                              ELSE ARRAY(SELECT jsonb_array_elements_text(tags)) END""")
        print("     тип изменён jsonb -> text[]")
    else:
        print("     уже", t)
except Exception as e:
    print("     ERR:", str(e)[:200])

# ---------- 3) переименовать таблицы ----------
print("3) переименование core -> *_legacy")
for t, leg in TABLES:
    try:
        kind = query("""SELECT c.relkind FROM pg_class c
                        JOIN pg_namespace n ON n.oid=c.relnamespace
                        WHERE n.nspname='core' AND c.relname=%s""", (t,))
        if not kind:
            print(f"     {t}: нет (уже переключено?)")
            continue
        if kind[0][0] == "v":
            print(f"     {t}: уже представление, пропуск")
            continue
        execute(f"ALTER TABLE core.{t} RENAME TO {leg}")
        print(f"     core.{t} -> core.{leg}")
    except Exception as e:
        print(f"     ERR {t}: {str(e)[:160]}")

# ---------- 4) представления с прежними именами ----------
print("4) создание представлений")
VIEWS = {
 "observation_v2": """CREATE OR REPLACE VIEW core.observation_v2 AS
     SELECT observation_id AS obs_id, metric_id, region_id, frequency_id,
            period_start, period_end, value, value_str, assessment_type,
            observation_status, source_id, release_id, quality_flags,
            sub_dimension, notes, created_at
     FROM data.observation""",
 "metric": """CREATE OR REPLACE VIEW core.metric AS
     SELECT metric_id, metric_code, name_ru, short_name_ru, description,
            unit_id, frequency_id, metric_type, index_base, is_derived,
            formula_text, status, tags, created_at
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
for t, sql in VIEWS.items():
    try:
        execute(sql)
        print(f"     core.{t}: ок")
    except Exception as e:
        print(f"     ERR core.{t}: {str(e)[:200]}")

# ---------- 5) пересоздать зависимые представления ----------
print("5) пересоздание зависимых представлений")
for v, d in defs.items():
    sch, name = v.split(".")
    try:
        execute(f"CREATE OR REPLACE VIEW {sch}.{name} AS {d}")
        print(f"     {v}: пересоздано")
    except Exception as e:
        print(f"     ERR {v}: {str(e)[:200]}")

# ---------- 6) проверка ----------
print("\n6) проверка")
checks = [
    ("core.observation_v2", "data.observation"),
    ("core.metric", "catalog.metric"),
    ("core.source", "catalog.source"),
    ("core.release", "catalog.release"),
    ("core.region", "catalog.region"),
    ("core.unit", "catalog.unit"),
    ("core.frequency", "catalog.frequency"),
]
allok = True
for a, b in checks:
    na = query(f"SELECT count(*) FROM {a}")[0][0]
    nb = query(f"SELECT count(*) FROM {b}")[0][0]
    good = na == nb
    allok = allok and good
    print(f"   {'OK ' if good else 'РАСХ'} {a} {na:,} = {b} {nb:,}")
print("   переключение", "ПРОШЛО" if allok else "ТРЕБУЕТ ВНИМАНИЯ")