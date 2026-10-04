#!/usr/bin/env python3
"""Проверка записи через представления: 35 скриптов пишут в core.*, значит
представления должны пропускать INSERT/UPDATE/DELETE в catalog/data.
Тест вставляет пробную строку, проверяет, что она легла в data.observation,
и удаляет её."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

MARK = "cutover-write-test-20261004"

print("=== 1. запись через core.observation_v2 ===")
try:
    n = execute("""INSERT INTO core.observation_v2
                   (obs_id, metric_id, region_id, frequency_id, period_start,
                    period_end, value, assessment_type, observation_status,
                    source_id, release_id, sub_dimension, notes)
                   VALUES (999999999, 1, 1, 5, DATE '2026-09-01', DATE '2026-09-30',
                           123.45, 'final', 'test', 7, 1, %s, %s)""", (MARK, MARK))
    print("   INSERT через представление:", "ок" if n is not None else "?")
except Exception as e:
    print("   ERR INSERT:", str(e)[:250])

print("   видно в core.observation_v2:",
      query("SELECT count(*) FROM core.observation_v2 WHERE notes=%s", (MARK,))[0][0])
print("   видно в data.observation:",
      query("SELECT count(*) FROM data.observation WHERE notes=%s", (MARK,))[0][0])

print("\n=== 2. UPDATE через представление ===")
try:
    execute("UPDATE core.observation_v2 SET value=999.99 WHERE notes=%s", (MARK,))
    v = query("SELECT value FROM data.observation WHERE notes=%s", (MARK,))
    print("   значение в физической таблице:", v[0][0] if v else "нет")
except Exception as e:
    print("   ERR UPDATE:", str(e)[:250])

print("\n=== 3. DELETE через представление ===")
try:
    execute("DELETE FROM core.observation_v2 WHERE notes=%s", (MARK,))
    print("   остаток в data.observation:",
          query("SELECT count(*) FROM data.observation WHERE notes=%s", (MARK,))[0][0])
except Exception as e:
    print("   ERR DELETE:", str(e)[:250])

print("\n=== 4. запись в справочник через core.metric ===")
try:
    execute("""INSERT INTO core.metric
               (metric_id, metric_code, name_ru, unit_id, source_id,
                frequency_id, status, tags)
               VALUES (999999, 'cutover_test_metric', 'Тест переключения', 1, 1,
                       5, 'active', ARRAY['test'])""")
    print("   INSERT core.metric: ок")
    print("   видно в catalog.metric:",
          query("SELECT count(*) FROM catalog.metric WHERE metric_code='cutover_test_metric'")[0][0])
    execute("DELETE FROM core.metric WHERE metric_code='cutover_test_metric'")
    print("   после удаления в catalog.metric:",
          query("SELECT count(*) FROM catalog.metric WHERE metric_code='cutover_test_metric'")[0][0])
except Exception as e:
    print("   ERR:", str(e)[:250])

print("\n=== 5. контрольные счётчики не поехали ===")
for t in ("core.observation_v2", "core.metric"):
    print(f"   {t}: {query(f'SELECT count(*) FROM {t}')[0][0]:,}")