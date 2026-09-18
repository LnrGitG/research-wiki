#!/usr/bin/env python3
"""
Удаление legacy-таблицы core.observation.

Обоснование (проверено 18.09.2026): из 551 022 строк legacy НОЛЬ строк
не имеют двойника в core.observation_v2 по (регион, период, значение).
Все данные сохранены в целевой таблице — часть под другими metric_id,
поскольку при гармонизации метрики были переназначены.

Две метрики (itzdrrm, vdpzdcn) существуют только в legacy, но их значения
полностью присутствуют в витрине под кодами itzdr и vdpzdcn_2
(совпадение 5025/5025 и 2062/2062). После удаления таблицы они станут
пустыми и их нужно убрать.

Запуск:  python3 drop_legacy_observation.py            # сухой прогон
         APPLY=1 python3 drop_legacy_observation.py     # применить
"""
import os
import sys

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
APPLY = os.environ.get("APPLY") == "1"

conn = psycopg.connect(DSN)
cur = conn.cursor()


def n(sql, args=None):
    cur.execute(sql, args or ())
    return cur.fetchone()[0]


print("=== 1. Состояние до ===")
print("  core.observation    : %s строк" % format(n('SELECT count(*) FROM core.observation'), ','))
print("  core.observation_v2 : %s строк" % format(n('SELECT count(*) FROM core.observation_v2'), ','))
print("  витрина             : %s строк" % format(
    n('SELECT count(*) FROM core.v_datalens_observations'), ','))
print("  метрик              : %s" % n('SELECT count(*) FROM core.metric'))

print("\n=== 2. Проверка безопасности (ноль = безопасно) ===")
orphan = n("""
SELECT count(*) FROM core.observation o
WHERE NOT EXISTS (SELECT 1 FROM core.observation_v2 v
  WHERE v.region_id = o.region_id AND v.period_start = o.period_start
    AND v.value IS NOT DISTINCT FROM o.value)""")
print("  строк legacy без двойника в v2 : %s" % format(orphan, ','))
if orphan:
    print("  ОСТАНОВ: есть уникальные данные — удалять нельзя")
    conn.close()
    sys.exit(1)

# метрики, которые держатся ТОЛЬКО на legacy
cur.execute("""
SELECT m.metric_id, m.metric_code, m.name_ru, m.tags,
       (SELECT count(*) FROM core.observation o WHERE o.metric_id = m.metric_id) AS legacy_rows,
       (SELECT count(*) FROM core.observation_v2 v WHERE v.metric_id = m.metric_id) AS v2_rows
FROM core.metric m
WHERE EXISTS (SELECT 1 FROM core.observation o WHERE o.metric_id = m.metric_id)
  AND NOT EXISTS (SELECT 1 FROM core.observation_v2 v WHERE v.metric_id = m.metric_id)
""")
lonely = cur.fetchall()
print("  метрик только в legacy         : %d" % len(lonely))
for mid, code, nm, tg, lr, vr in lonely:
    print("     id=%-5s %-12s %-46s legacy=%-6s v2=%s" % (mid, code, str(nm)[:46], lr, vr))

print("\n=== 3. План ===")
print("  1) удалить %d метрик, оставшихся без данных" % len(lonely))
print("  2) DROP TABLE core.observation")
print("  3) проверить витрину и перегенерировать дамп схемы")

if not APPLY:
    print("\nСУХОЙ ПРОГОН. Применить: APPLY=1 python3 drop_legacy_observation.py")
    conn.close()
    sys.exit(0)

print("\n=== 4. Выполняю ===")
# Порядок важен. От core.observation зависят:
#   - observation_metric_id_fkey (на core.metric) — не даёт удалить метрики
#   - note_obs_id_fkey (из core.note) — не даёт удалить таблицу
# Таблица core.note часть схемы (аннотации к наблюдениям), поэтому снимаем
# только внешний ключ, а не удаляем её через CASCADE.
cur.execute("""ALTER TABLE core.note
               DROP CONSTRAINT IF EXISTS note_obs_id_fkey""")
conn.commit()
print("  снят внешний ключ core.note.note_obs_id_fkey")

cur.execute("DROP TABLE core.observation")
conn.commit()
print("  DROP TABLE core.observation — выполнено")

for mid, code, nm, tg, lr, vr in lonely:
    cur.execute("DELETE FROM core.metric WHERE metric_id=%s", (mid,))
    print("  удалена метрика %s (id=%s)" % (code, mid))
conn.commit()

print("\n=== 5. После ===")
print("  core.observation_v2 : %s строк" % format(n('SELECT count(*) FROM core.observation_v2'), ','))
print("  витрина             : %s строк" % format(
    n('SELECT count(*) FROM core.v_datalens_observations'), ','))
print("  метрик              : %s" % n('SELECT count(*) FROM core.metric'))
print("  дублей по ключу     : %s" % n("""SELECT coalesce(sum(c-1),0) FROM (
    SELECT count(*) c FROM core.observation_v2
    GROUP BY metric_id, region_id, frequency_id, period_start, source_id,
             release_id, assessment_type, sub_dimension HAVING count(*) > 1) x"""))
print("  метрик без данных   : %s" % n("""SELECT count(*) FROM core.metric m
    WHERE NOT EXISTS (SELECT 1 FROM core.observation_v2 v WHERE v.metric_id = m.metric_id)"""))
conn.close()
