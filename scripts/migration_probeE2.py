#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== пример дублирующегося ключа ===")
key = query("""SELECT metric_id, region_id, period_start, count(*) AS n
               FROM core.observation_v2
               GROUP BY 1,2,3 HAVING count(*) > 1
               ORDER BY n DESC LIMIT 1""")[0]
print("   ключ:", key)

rows = query("""SELECT obs_id, frequency_id, assessment_type, observation_status,
                       sub_dimension, source_id, release_id, value, value_str,
                       quality_flags, notes
                FROM core.observation_v2
                WHERE metric_id=%s AND region_id=%s AND period_start=%s
                ORDER BY obs_id""", (key[0], key[1], key[2]))
for r in rows[:12]:
    print("   ", r)

print("\n=== какие колонки различаются внутри дублирующихся ключей ===")
res = query("""
WITH dup AS (
    SELECT metric_id, region_id, period_start
    FROM core.observation_v2
    GROUP BY 1,2,3 HAVING count(*) > 1
)
SELECT
  count(DISTINCT o.frequency_id)        AS f_distinct,
  count(DISTINCT o.assessment_type)     AS a_distinct,
  count(DISTINCT o.observation_status)  AS s_distinct,
  count(DISTINCT o.sub_dimension)       AS d_distinct,
  count(DISTINCT o.source_id)           AS src_distinct,
  count(DISTINCT o.release_id)          AS rel_distinct,
  count(DISTINCT o.value)               AS v_distinct,
  count(*)                              AS rows_total,
  count(DISTINCT (o.metric_id,o.region_id,o.period_start)) AS keys_total
FROM core.observation_v2 o
JOIN dup d ON d.metric_id=o.metric_id AND d.region_id=o.region_id
          AND d.period_start=o.period_start""")[0]
labels = ["frequency_id","assessment_type","observation_status","sub_dimension",
          "source_id","release_id","value","строк","ключей"]
for lab, v in zip(labels, res):
    print(f"   различных {lab}: {v}")

print("\n=== сколько ключей станут уникальными при добавлении колонок ===")
for cols in [("frequency_id",),
             ("frequency_id","assessment_type"),
             ("frequency_id","assessment_type","sub_dimension"),
             ("frequency_id","assessment_type","sub_dimension","release_id")]:
    sel = ", ".join(cols)
    n = query(f"""SELECT count(*) FROM (
                    SELECT metric_id, region_id, period_start, {sel}
                    FROM core.observation_v2
                    GROUP BY 1,2,3,{",".join(str(i+4) for i in range(len(cols)))}
                    HAVING count(*) > 1) t""")[0][0]
    print(f"   + {sel}: остаётся дублей {n}")