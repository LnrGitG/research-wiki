#!/usr/bin/env python3
"""Что из осадка миграции надо перенести в канон перед удалением.

Проверка идёт сравнением множеств (`EXCEPT`), а не антисоединением:
`data.observation` секционирована по `period_start` на 239 секций, и
антисоединение без ключа секционирования вырождается в прочёсывание всех
секций (замер: не завершалось за семь минут). `EXCEPT` обходится сортировкой
или хешированием и укладывается в минуты.

Ключ сверки — тот же, что в приёмке переезда (`migration_stepG_verify.py`):
metric_id, region_id, period_start, frequency_id, assessment_type,
sub_dimension, release_id. Для `v2.observation` строгий ключ неприменим: там
нет assessment_type, sub_dimension и release_id — это старая генерация со
своим флагом is_current, поэтому для неё ключ короче.

Читает только; ничего не пишет и не меняет.
"""
import sys
import time

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
import db_tunnel  # noqa: E402

K_FULL = ("metric_id, region_id, period_start, frequency_id, "
          "assessment_type, sub_dimension, release_id")
K_V2 = "metric_id, region_id, period_start, frequency_id"

TARGETS = [
    ("core.observation_v2_legacy", K_FULL),
    ("core.observation_v2_old", K_FULL),
    ("v2.observation", K_V2),
]


def main():
    with db_tunnel.connect() as c:
        with c.cursor() as cur:
            cur.execute("SET work_mem = '256MB'")
            cur.execute("SET statement_timeout = '3600s'")

            print("=== Недобор: чего нет в каноне по ключу приёмки ===")
            for table, key in TARGETS:
                sql = (f"SELECT count(*) FROM ("
                       f"  SELECT {key} FROM {table} "
                       f"  EXCEPT "
                       f"  SELECT {key} FROM data.observation) x")
                t0 = time.time()
                cur.execute(sql)
                n = cur.fetchone()[0]
                print(f"  {table:<32} недобор={n:>9}  ({time.time()-t0:.1f} с)")

            print("\n=== Ссылочная целостность недобора (упадёт ли вставка) ===")
            for table, key in TARGETS:
                sql = (f"SELECT count(*) FROM {table} o WHERE NOT EXISTS ("
                       f"  SELECT 1 FROM data.observation d WHERE "
                       + " AND ".join(
                           f"d.{col}=o.{col}" for col in key.split(", "))
                       + ")")
                # антисоединение здесь допустимо: недобор мал, но время
                # ограничим, чтобы не повторить семиминутный случай
                cur.execute("SET statement_timeout = '600s'")
                t0 = time.time()
                try:
                    cur.execute(sql)
                    n = cur.fetchone()[0]
                    print(f"  {table:<32} недобор={n:>9}  ({time.time()-t0:.1f} с)")
                except Exception as e:
                    print(f"  {table:<32} ERR {str(e).splitlines()[0][:90]}")
                finally:
                    cur.execute("SET statement_timeout = '3600s'")


if __name__ == "__main__":
    main()