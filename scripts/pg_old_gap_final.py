#!/usr/bin/env python3
"""Финальный блок разбора недобора `core.observation_v2_old`.

Отвечает на два вопроса перед удалением:
1. Чем почти-двойники (204 078 строк, совпадающих по сокращённому ключу)
   отличаются от канона — релизом, значением или подразмерностью?
2. Что за метрика 483 (5 025 строк, отсутствует во всех реестрах)?

Читает только.
"""
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
import db_tunnel  # noqa: E402


def main():
    with db_tunnel.connect() as c:
        with c.cursor() as cur:
            cur.execute("SET work_mem = '256MB'")
            cur.execute("SET statement_timeout = '1800s'")

            print("=== Чем различаются почти-двойники с каноном ===")
            cur.execute("""
                SELECT bool_or(o.assessment_type IS DISTINCT
                               FROM d.assessment_type),
                       bool_or(o.sub_dimension IS DISTINCT
                               FROM d.sub_dimension),
                       bool_or(o.release_id IS DISTINCT
                               FROM d.release_id),
                       bool_or(o.value IS DISTINCT FROM d.value)
                FROM core.observation_v2_old o
                JOIN data.observation d
                  ON d.metric_id = o.metric_id
                 AND d.region_id = o.region_id
                 AND d.period_start = o.period_start
                WHERE NOT EXISTS (
                      SELECT 1 FROM data.observation dx
                      WHERE dx.metric_id = o.metric_id
                        AND dx.region_id = o.region_id
                        AND dx.period_start = o.period_start
                        AND dx.frequency_id IS NOT DISTINCT
                            FROM o.frequency_id
                        AND dx.assessment_type IS NOT DISTINCT
                            FROM o.assessment_type
                        AND dx.sub_dimension IS NOT DISTINCT
                            FROM o.sub_dimension
                        AND dx.release_id IS NOT DISTINCT
                            FROM o.release_id)
                  AND o.metric_id <> 483
            """)
            f = cur.fetchone()
            print(f"  различия: тип оценки={f[0]}, подразмерность={f[1]}, "
                  f"релиз={f[2]}, значение={f[3]}")

            print("\n=== Релизы почти-двойников: старые против канона ===")
            cur.execute("""
                SELECT o.release_id, count(DISTINCT (o.metric_id, o.region_id,
                              o.period_start)) AS grp
                FROM core.observation_v2_old o
                WHERE o.metric_id <> 483
                  AND NOT EXISTS (SELECT 1 FROM data.observation dx
                       WHERE dx.metric_id=o.metric_id
                         AND dx.region_id=o.region_id
                         AND dx.period_start=o.period_start
                         AND dx.frequency_id IS NOT DISTINCT
                             FROM o.frequency_id
                         AND dx.assessment_type IS NOT DISTINCT
                             FROM o.assessment_type
                         AND dx.sub_dimension IS NOT DISTINCT
                             FROM o.sub_dimension
                         AND dx.release_id IS NOT DISTINCT
                             FROM o.release_id)
                GROUP BY 1 ORDER BY 2 DESC LIMIT 10
            """)
            for rid, n in cur.fetchall():
                print(f"  release_id={rid}: {n:,} групп")

            print("\n=== Метрика 483: строки в осадке ===")
            cur.execute("""
                SELECT min(period_start), max(period_start), count(*)
                FROM core.observation_v2_old WHERE metric_id = 483
            """)
            a, b, n = cur.fetchone()
            print(f"  период {a} .. {b}, строк {n:,}")
            cur.execute("""
                SELECT region_id, count(*) FROM core.observation_v2_old
                WHERE metric_id = 483 GROUP BY 1 ORDER BY 2 DESC LIMIT 5
            """)
            for rid, k in cur.fetchall():
                print(f"  регион {rid}: {k:,}")
            cur.execute("""
                SELECT obs_id, region_id, period_start, frequency_id,
                       assessment_type, sub_dimension, release_id, value
                FROM core.observation_v2_old WHERE metric_id = 483 LIMIT 3
            """)
            for row in cur.fetchall():
                print("  пример:", row)


if __name__ == "__main__":
    main()