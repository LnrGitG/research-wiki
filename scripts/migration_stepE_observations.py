#!/usr/bin/env python3
"""Этап E: перенос наблюдений core.observation_v2 -> data.observation.

Ключевое: уникальный индекс приёмника (metric_id, region_id, period_start)
отклонил бы 312 986 строк — реальный ключ данных шире. Проверено: добавление
frequency_id, assessment_type, sub_dimension, release_id даёт ноль дублей,
поэтому индекс пересоздаётся по этим семи колонкам.

ID наблюдений сохраняются (obs_id -> observation_id) для трассируемости.
"""
import sys, time
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

# 1) пересоздать уникальный индекс по полному естественному ключу
print("--- уникальный индекс ---")
try:
    execute("DROP INDEX IF EXISTS data.ux_observation")
    print("   старый индекс снят")
except Exception as e:
    print("   ERR снятия:", str(e)[:160])

try:
    execute("""CREATE UNIQUE INDEX IF NOT EXISTS ux_observation
               ON data.observation
               (metric_id, region_id, period_start, frequency_id,
                assessment_type, sub_dimension, release_id)""")
    print("   новый индекс по 7 колонкам создан")
except Exception as e:
    print("   ERR создания:", str(e)[:200])

# 2) перенос
print("\n--- перенос наблюдений (5,5 млн строк, серверная сторона) ---")
SQL = """
INSERT INTO data.observation
    (observation_id, metric_id, region_id, frequency_id, period_start,
     period_end, value, value_str, assessment_type, observation_status,
     source_id, release_id, quality_flags, sub_dimension, notes, created_at)
SELECT o.obs_id, o.metric_id::int, o.region_id::int, o.frequency_id::int,
       o.period_start, o.period_end, o.value, o.value_str,
       o.assessment_type, o.observation_status, o.source_id::int,
       o.release_id::int, o.quality_flags, o.sub_dimension, o.notes,
       o.created_at
FROM core.observation_v2 o
ON CONFLICT DO NOTHING
"""
t0 = time.time()
try:
    n = execute(SQL)
    print(f"   вставлено: {n} за {time.time()-t0:.1f} с")
except Exception as e:
    print("   ERR:", str(e)[:400])

# 3) последовательность
try:
    execute("""SELECT setval('data.observation_observation_id_seq',
               COALESCE((SELECT max(observation_id) FROM data.observation), 1))""")
    print("   последовательность выровнена")
except Exception as e:
    print("   ERR setval:", str(e)[:140])

# 4) контроль
print("\n=== контроль ===")
a = query("SELECT count(*) FROM core.observation_v2")[0][0]
b = query("SELECT count(*) FROM data.observation")[0][0]
print(f"   источник {a:,} -> приёмник {b:,}   {'OK' if a == b else 'РАСХОЖДЕНИЕ ' + str(a-b)}")
print("   период:", query("SELECT min(period_start), max(period_start) FROM data.observation")[0])