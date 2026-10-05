#!/usr/bin/env python3
"""Разбор недобора `core.observation_v2_old`: что это за 209 103 строки.

Двухступенчатый план (первая версия падала по таймауту):
1. Собрать недобор по КЛЮЧЕВЫМ полям через EXCEPT — быстро (сортировка, не
   антисоединение против секций).
2. Присоединить полные строки к временной таблице ключей с условием по
   period_start — секционное отсечение (partition pruning) делает это дёшево.

Вопрос, который решается до удаления: это законные наблюдения, которые надо
перенести в канон, или устаревшие строки, снятые более поздней правкой
(след такой правки — дамп `obs_v2_before_h5fix.dump` в бакете)?
Признак «вытесненной» строки: почти-двойник в каноне по сокращённому ключу
(метрика, регион, начало периода, частота), отличающийся типом оценки,
подразмерностью или релизом. Читает только; временные таблицы — в своей сессии.
"""
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
import db_tunnel  # noqa: E402

K_FULL = ["metric_id", "region_id", "period_start", "frequency_id",
          "assessment_type", "sub_dimension", "release_id"]


def main():
    with db_tunnel.connect() as c:
        with c.cursor() as cur:
            cur.execute("SET work_mem = '256MB'")
            cur.execute("SET statement_timeout = '3000s'")

            print("=== Шаг 1: ключи недобора через EXCEPT ===")
            sel = ", ".join("o." + x for x in K_FULL)
            cur.execute(f"""
                CREATE TEMP TABLE gap_keys AS
                SELECT {sel} FROM core.observation_v2_old o
                EXCEPT
                SELECT {sel.replace("o.", "d.")} FROM data.observation d
            """)
            cur.execute("SELECT count(*) FROM gap_keys")
            n = cur.fetchone()[0]
            print(f"  строк недобора по ключу: {n:,}")

            print("\n=== Шаг 2: полные строки к ключам (через period_start) ===")
            cond = " AND ".join(
                f"g.{x} IS NOT DISTINCT FROM o.{x}"
                for x in K_FULL)
            cur.execute(f"""
                CREATE TEMP TABLE gap AS
                SELECT o.* FROM core.observation_v2_old o
                JOIN gap_keys g ON o.period_start = g.period_start
                    AND {cond}
            """)
            cur.execute("SELECT count(*) FROM gap")
            print(f"  строк в разборе: {cur.fetchone()[0]:,}")

            print("\n=== Внешние ключи канона (упадёт ли вставка) ===")
            cur.execute("""
                SELECT
                  count(*) FILTER (WHERE NOT EXISTS (SELECT 1
                        FROM catalog.metric m WHERE m.metric_id = g.metric_id)),
                  count(*) FILTER (WHERE NOT EXISTS (SELECT 1
                        FROM catalog.region r WHERE r.region_id = g.region_id)),
                  count(*) FILTER (WHERE g.release_id IS NOT NULL
                        AND NOT EXISTS (SELECT 1
                        FROM catalog.release l WHERE l.release_id = g.release_id))
                FROM gap g
            """)
            a, b, cc = cur.fetchone()
            print(f"  без метрики={a}, без региона={b}, без релиза={cc}")

            print("\n=== Почти-двойник в каноне (сокращённый ключ) ===")
            cur.execute("""
                SELECT count(*) FROM gap g
                WHERE EXISTS (SELECT 1 FROM data.observation d
                              WHERE d.metric_id = g.metric_id
                                AND d.region_id = g.region_id
                                AND d.period_start = g.period_start
                                AND d.frequency_id IS NOT DISTINCT
                                    FROM g.frequency_id)
            """)
            near = cur.fetchone()[0]
            print(f"  почти-двойник есть: {near:,} из {n:,} "
                  f"({100.0*near/n:.1f} %)")
            print(f"  вовсе без пары:     {n - near:,}")

            print("\n=== Распределение недобора по годам ===")
            cur.execute("""
                SELECT date_part('year', period_start)::int, count(*)
                FROM gap GROUP BY 1 ORDER BY 1
            """)
            for y, k in cur.fetchall():
                print(f"  {y}: {k:,}")

            print("\n=== Топ-10 метрик в недоборе ===")
            cur.execute("""
                SELECT g.metric_id, coalesce(m.metric_code, '?'), count(*) AS n
                FROM gap g LEFT JOIN catalog.metric m
                     ON m.metric_id = g.metric_id
                GROUP BY 1, 2 ORDER BY n DESC LIMIT 10
            """)
            for mid, code, k in cur.fetchall():
                print(f"  {mid:>7} {code:<40} {k:,}")

            print("\n=== Чем различаются с почти-двойниками (все поля) ===")
            cur.execute("""
                SELECT bool_or(g.assessment_type IS DISTINCT
                           FROM d.assessment_type) AS тип_оценки,
                       bool_or(g.sub_dimension IS DISTINCT
                           FROM d.sub_dimension) AS подразмерность,
                       bool_or(g.release_id IS DISTINCT
                           FROM d.release_id) AS релиз,
                       bool_or(g.value IS DISTINCT FROM d.value) AS значение,
                       bool_or(g.run_id IS DISTINCT FROM d.run_id) AS прогон
                FROM gap g
                JOIN data.observation d ON
                     d.metric_id = g.metric_id
                 AND d.region_id = g.region_id
                 AND d.period_start = g.period_start
                 AND d.frequency_id IS NOT DISTINCT FROM g.frequency_id
                LIMIT 1
            """)
            f = cur.fetchone()
            print(f"  различия: тип оценки={f[0]}, подразмерность={f[1]}, "
                  f"релиз={f[2]}, значение={f[3]}, прогон={f[4]}")


if __name__ == "__main__":
    main()