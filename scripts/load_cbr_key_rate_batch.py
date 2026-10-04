#!/usr/bin/env python3
"""Догрузка дневного ряда ключевой ставки пакетами.

Построчная вставка через тоннель даёт около двух строк в секунду (каждая
вставка — отдельное соединение), на 3 271 точку это полчаса. Пакет по 400
строк в одном операторе ускоряет на порядок. Скрипт идемпотентен: уже
загруженные точки отсекаются ON CONFLICT.
"""
import json
import os
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

SRC = "/home/lnr/research-wiki-private/data/cbr_key_rate_daily.json"
CHUNK = 400

with open(SRC, encoding="utf-8") as f:
    daily = json.load(f)["daily"]

metric_id = query("SELECT metric_id FROM catalog.metric WHERE metric_code='cbr_key_rate'")[0][0]
rel = query("""SELECT release_id FROM catalog.release
               WHERE source_id=7 AND label LIKE 'Ключевая ставка (дневной ряд)%'
               ORDER BY release_id DESC LIMIT 1""")
release_id = rel[0][0]
region_id = query("SELECT region_id FROM catalog.region WHERE region_code='ru'")[0][0]
freq_id = query("SELECT frequency_id FROM catalog.frequency WHERE freq_code='D'")[0][0]

before = query("SELECT count(*) FROM data.observation WHERE metric_id=%s", (metric_id,))[0][0]
print(f"метрика={metric_id} релиз={release_id} регион={region_id} частота={freq_id}")
print(f"уже в базе: {before} из {len(daily)}")

rows = sorted(daily.items())
cols = "(metric_id, region_id, period_start, frequency_id, value, assessment_type," \
       " observation_status, source_id, release_id, sub_dimension, notes)"
conflict = ("ON CONFLICT (metric_id, region_id, period_start, frequency_id,"
            " assessment_type, sub_dimension, release_id) DO NOTHING")

total = 0
for i in range(0, len(rows), CHUNK):
    part = rows[i:i + CHUNK]
    values = ",".join(
        f"({metric_id},{region_id},'{iso}'::date,{freq_id},{val},'final',"
        f"'validated',7,{release_id},'','cbr.ru/hd_base/KeyRate')"
        for iso, val in part)
    sql = f"INSERT INTO data.observation {cols} VALUES {values} {conflict}"
    try:
        total += execute(sql)
    except Exception as e:
        print(f"   ошибка на блоке {i}: {str(e)[:160]}")
        break
    if (i // CHUNK) % 2 == 0:
        print(f"   обработано {min(i+CHUNK, len(rows))} из {len(rows)}")

after = query("SELECT count(*) FROM data.observation WHERE metric_id=%s", (metric_id,))[0][0]
print(f"\nдобавлено: {total}; всего в базе: {after}")

print("\n=== контроль ===")
r = query("""SELECT count(*), min(period_start), max(period_start)
             FROM data.observation WHERE metric_id=%s""", (metric_id,))[0]
print(f"   наблюдений {r[0]}, диапазон {r[1]} .. {r[2]}")
for x in query("""SELECT period_start, value FROM data.observation
                  WHERE metric_id=%s ORDER BY period_start DESC LIMIT 5""", (metric_id,)):
    print("     ", x)
print("   ступеней (смен значения):")
steps = query("""SELECT count(*) FROM (
                   SELECT value, lag(value) OVER (ORDER BY period_start) AS prev
                   FROM data.observation WHERE metric_id=%s) t
                 WHERE prev IS NULL OR value <> prev""", (metric_id,))[0][0]
print("     ", steps)