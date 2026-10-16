#!/usr/bin/env python3
"""Уборка метрик-заглушек, созданных дефектом обрезки имени.

Дефект. `harmonize_6_rosstat_extra.py` искал метрику по ПОЛНОМУ имени, а
хранил — обрезанное до 200 знаков. Названия длиннее 200 знаков не находились,
и каждый прогон создавал новую метрику (`..._2`, `..._3`) с тем же единственным
наблюдением. Исправлено в самом гармонайзере; этот скрипт убирает уже
накопленное.

Признак заглушки: `length(name_ru)=200` и есть более старая метрика с тем же
199-знаковым префиксом. Удаляются только метрики с `metric_id >= MIN_ID`
(порог прогона-виновника) — история не трогается.

Точка возврата: дамп наблюдений в attic/.
Запуск: APPLY=1 python3 scripts/clean_truncated_metric_stubs.py
"""
import gzip
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect, query  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP = os.path.join(REPO, "attic", "truncated_metric_stubs.csv.gz")
MIN_ID = 74000          # id метрик, созданных прогоном 16.10.2026

FIND = """
SELECT m.metric_id, m.metric_code, m.name_ru
FROM catalog.metric m
WHERE m.metric_id >= %s AND length(m.name_ru) = 200
  AND EXISTS (SELECT 1 FROM catalog.metric o
              WHERE o.metric_id < %s AND left(o.name_ru, 199) = left(m.name_ru, 199))
ORDER BY m.metric_id
"""


def main():
    apply = os.environ.get("APPLY") == "1"
    stubs = query(FIND, (MIN_ID, MIN_ID))
    print("метрик-заглушек к удалению: %d" % len(stubs))
    for r in stubs[:5]:
        print("   id=%s %s" % (r[0], r[2][:70]))

    obs = query("""SELECT metric_id, region_id, period_start, frequency_id, value,
                          source_id, release_id, sub_dimension
                   FROM data.observation WHERE metric_id = ANY(%s)""",
                ([r[0] for r in stubs],)) if stubs else []
    print("наблюдений у них: %d" % len(obs))

    if not apply:
        print("\nDRY-RUN. Запустите с APPLY=1.")
        return

    os.makedirs(os.path.dirname(DUMP), exist_ok=True)
    with gzip.open(DUMP, "wt", encoding="utf-8") as f:
        f.write("metric_id,metric_code,name_ru,region_id,period_start,value\n")
        by_id = {r[0]: r for r in stubs}
        for o in obs:
            f.write("%s,%s,%s,%s,%s,%s\n" % (o[0], by_id[o[0]][1],
                                             by_id[o[0]][2].replace(",", " "),
                                             o[1], o[2], o[4]))
    print("дамп: %s" % DUMP)

    ids = [r[0] for r in stubs]
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM data.observation WHERE metric_id = ANY(%s)", (ids,))
        n_obs = cur.rowcount
        cur.execute("DELETE FROM catalog.metric WHERE metric_id = ANY(%s)", (ids,))
        n_m = cur.rowcount
    conn.commit()
    print("удалено: наблюдений %d, метрик %d" % (n_obs, n_m))
    print("метрик в каталоге:", query("SELECT count(*) FROM catalog.metric")[0][0])


if __name__ == "__main__":
    main()
