#!/usr/bin/env python3
"""Оптимизация витрины derived.metric_card.

Было: соединение catalog.metric с data.observation и группировка ПОСЛЕ
соединения. Планировщик получал 5,5 млн строк на входе агрегата, выгружал
~5 ГБ во временные файлы, обновление занимало 172 с.

Стало: наблюдения агрегируются до соединения (15 868 строк), затем
соединяются с метриками. Замер: 1,4 с вместо 172 с.
"""
import sys
import time

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

NEW = """
SELECT m.metric_id,
       m.metric_code,
       m.name_ru,
       u.unit_code,
       s.source_code,
       f.freq_code,
       st.last_observation,
       st.observations_cnt
FROM catalog.metric m
JOIN catalog.unit      u ON u.unit_id      = m.unit_id
JOIN catalog.source    s ON s.source_id    = m.source_id
JOIN catalog.frequency f ON f.frequency_id = m.frequency_id
LEFT JOIN (
    SELECT metric_id,
           max(period_start) AS last_observation,
           count(*)          AS observations_cnt
    FROM data.observation
    GROUP BY metric_id
) st ON st.metric_id = m.metric_id
"""

print("=== снятие старого определения ===")
try:
    execute("DROP MATERIALIZED VIEW IF EXISTS derived.metric_card")
    print("   снято")
except Exception as e:
    print("   ERR:", str(e)[:200])

print("=== создание с агрегатом до соединения ===")
t = time.time()
try:
    execute(f"CREATE MATERIALIZED VIEW derived.metric_card AS {NEW}")
    print(f"   создано за {time.time()-t:.1f} с")
except Exception as e:
    print("   ERR:", str(e)[:300])

try:
    execute("CREATE UNIQUE INDEX ux_metric_card ON derived.metric_card (metric_id)")
    print("   уникальный индекс создан")
except Exception as e:
    print("   ERR индекса:", str(e)[:200])

print("\n=== замер обновления ===")
for mode, sql in (("обычный", "REFRESH MATERIALIZED VIEW derived.metric_card"),
                  ("CONCURRENTLY", "REFRESH MATERIALIZED VIEW CONCURRENTLY derived.metric_card")):
    t = time.time()
    try:
        execute(sql)
        print(f"   {mode}: {time.time()-t:.1f} с")
    except Exception as e:
        print(f"   {mode}: ERR {str(e)[:200]}")

print("\n=== контроль ===")
print("   строк в витрине:", query("SELECT count(*) FROM derived.metric_card")[0][0])
print("   пример:", query("SELECT metric_code, last_observation, observations_cnt "
                          "FROM derived.metric_card WHERE observations_cnt > 0 "
                          "ORDER BY observations_cnt DESC LIMIT 3"))