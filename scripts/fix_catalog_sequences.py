#!/usr/bin/env python3
"""Выравнивание последовательностей каталога после переезда.

При переезде строки вставлялись с явными ключами, и счётчики остались
далеко позади фактических максимумов. Симптом проявился на вставке релиза:
duplicate key value violates unique constraint "release_pkey" при первом же
INSERT без явного id. Дефект латентный: он не виден на чтении и всплывает
на первой же записи в справочник.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

TABLES = [
    ("catalog", "release", "release_id"),
    ("catalog", "metric", "metric_id"),
    ("catalog", "region", "region_id"),
    ("catalog", "source", "source_id"),
    ("catalog", "unit", "unit_id"),
    ("catalog", "frequency", "frequency_id"),
    ("catalog", "topic", "topic_id"),
]

print("=== до выравнивания ===")
for sch, tbl, col in TABLES:
    seq = query("""SELECT pg_get_serial_sequence(%s, %s)""", (f"{sch}.{tbl}", col))[0][0]
    if not seq:
        print(f"   {sch}.{tbl}.{col}: последовательности нет (ключ не serial)")
        continue
    mx = query(f"SELECT coalesce(max({col}), 0) FROM {sch}.{tbl}")[0][0]
    lv = query("SELECT last_value FROM " + seq.replace("public.", ""))[0][0]
    print(f"   {sch}.{tbl}: max={mx} счётчик={lv}")

print("\n=== выравнивание ===")
for sch, tbl, col in TABLES:
    seq = query("""SELECT pg_get_serial_sequence(%s, %s)""", (f"{sch}.{tbl}", col))[0][0]
    if not seq:
        continue
    try:
        execute(f"""SELECT setval('{seq}',
                       (SELECT coalesce(max({col}), 1) FROM {sch}.{tbl}), true)""")
        lv = query("SELECT last_value FROM " + seq.replace("public.", ""))[0][0]
        print(f"   OK {sch}.{tbl}: счётчик -> {lv}")
    except Exception as e:
        print(f"   ERR {sch}.{tbl}: {str(e)[:140]}")

print("\n=== после выравнивания ===")
for sch, tbl, col in TABLES:
    seq = query("""SELECT pg_get_serial_sequence(%s, %s)""", (f"{sch}.{tbl}", col))[0][0]
    if not seq:
        continue
    mx = query(f"SELECT max({col}) FROM {sch}.{tbl}")[0][0]
    lv = query("SELECT last_value FROM " + seq.replace("public.", ""))[0][0]
    mark = "OK" if lv >= mx else "ОТСТАЁТ"
    print(f"   {mark} {sch}.{tbl}: max={mx} счётчик={lv}")