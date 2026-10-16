#!/usr/bin/env python3
"""Пункт 3: убрать годовые итоги из-под месячных метрик стройматериалов.

Проблема. Семь метрик месячной частоты (`ptvg`, `ptb`, `pkk`, `pkf`, `ppp`,
`pkks`, `psllp`) содержат лишние наблюдения из релиза 29 «Rosstat
Proizvodstvo_god (annual file)»: годовые итоги приклеены к 1 января и
сталкиваются с январскими месячными значениями (напр. `pkks` 2020-01: годовые
5228,3 и 67 против месячного 375,3).

Правило. Для каждого периода с более чем одним наблюдением оставляется то, что
берёт месячный ряд: приоритет релизам, отличным от годового (release_id=29),
при равенстве — наименьшее значение. Остальные строки — отсев.

Запуск:  APPLY=1 python3 scripts/fix_materials_annual_rows.py
Без APPLY — только показать, что будет удалено (dry-run).
Точка возврата — дамп отсева в attic/.
"""
import gzip
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect, query  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATTIC = os.path.join(REPO, "attic")
DUMP = os.path.join(ATTIC, "materials_annual_rows_dropped.csv.gz")

CODES = ["ptvg", "ptb", "pkk", "pkf", "ppp", "pkks", "psllp"]
ANNUAL_RELEASE = 29

SELECT = """
SELECT o.observation_id, m.metric_code, o.period_start, o.value, o.release_id,
       o.sub_dimension
FROM data.observation o
JOIN catalog.metric m ON m.metric_id = o.metric_id
WHERE m.metric_code = %s
ORDER BY o.period_start, (o.release_id = %s), o.value
"""


def main():
    apply = os.environ.get("APPLY") == "1"
    drop_ids = []
    detail = []
    for code in CODES:
        rows = query(SELECT, (code, ANNUAL_RELEASE))
        by_period = {}
        for r in rows:
            by_period.setdefault(r[2], []).append(r)
        for period, grp in by_period.items():
            if len(grp) < 2:
                continue
            keep = grp[0]          # правило: уже отсортировано запросом
            for r in grp[1:]:
                drop_ids.append(r[0])
                detail.append((code, str(period), r[3], r[4], (r[5] or "")[-28:]))

    print(f"метрик: {len(CODES)}; периодов с дублями: "
          f"{len({(d[0], d[1]) for d in detail})}; строк к отсеву: {len(drop_ids)}")
    for d in detail:
        print("   %-6s %s value=%-14s rel=%-3s %s" % d)

    if not apply:
        print("\nDRY-RUN. Запустите с APPLY=1 для удаления.")
        return

    os.makedirs(ATTIC, exist_ok=True)
    with gzip.open(DUMP, "wt", encoding="utf-8") as f:
        f.write("metric_code,period_start,value,release_id,sub_dimension\n")
        for d in detail:
            f.write("%s,%s,%s,%s,%s\n" % (d[0], d[1], d[2], d[3], d[4].replace(",", " ")))
    print(f"\nдамп отсева: {DUMP} ({os.path.getsize(DUMP)} байт)")

    conn = connect()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM data.observation WHERE observation_id = ANY(%s)",
                    (drop_ids,))
        n = cur.rowcount
    conn.commit()
    print(f"удалено строк: {n}")
    print("контроль: осталось строк по коду ->", {
        c: query("SELECT count(*) FROM data.observation o JOIN catalog.metric m "
                 "ON m.metric_id=o.metric_id WHERE m.metric_code=%s", (c,))[0][0]
        for c in CODES})


if __name__ == "__main__":
    main()
