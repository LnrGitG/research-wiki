#!/usr/bin/env python3
"""Парк техники: РФ-ряд из PDF не удалять, а помечать надгробным статусом.

Разбор 17.10.2026. По метрике `pste` (парк строительных машин, шт.) в каноне
лежат два среза по Российской Федерации:

  * приложение к сборнику (`Stroit_Pril_*/R_10_2_4_pril.xlsx`, таблица 2.11) —
    четыре вида машин (excavators, bulldozers, cranes_mobile, loaders),
    значения точные (2023: экскаваторы 14 502);
  * PDF/docx сборника (`Stroit_2022.pdf Table 2.26`,
    `Stroit_2024/R-2-4 Table 2.26`) — семь видов машин (автокраны, бульдозеры,
    грейдеры, краны башенные, краны на гусеничном ходу, скреперы, экскаваторы),
    значения округлены до сотен (14 500 против 14 502).

Это НЕ один ряд под двумя именами: у срезов разный состав видов машин
(2021: бульдозеры 7 000 против 6 991 — совпадает с точностью округления, а
краны 6 600 «автокраны» против 4 339 «cranes_mobile» — это разные определения).
Поэтому данные не удаляются и не переливаются: 28 строк РФ переводятся в
`observation_status='superseded'`, чтобы читатель по умолчанию брал приложение,
а срез PDF оставался доступен для сверки и для тех видов машин, которых в
приложении нет (грейдеры, скреперы, башенные краны).

Запуск: python3 scripts/supersede_pdf_dupes.py [APPLY=1]
"""

import csv
import gzip
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP = os.path.join(REPO, 'attic', 'pste_pdf_dupes_before.csv.gz')

SELECT = """
    SELECT o.observation_id, m.metric_code, r.release_label, o.period_start::text,
           o.region_id, o.sub_dimension, o.value::text, o.observation_status
    FROM data.observation o
    JOIN core.metric m USING(metric_id)
    JOIN core.release r USING(release_id)
    WHERE m.metric_code = 'pste' AND r.release_label LIKE '%%Table 2.26'
    ORDER BY o.period_start, o.sub_dimension"""


def main():
    rows = tunnel.query(SELECT)
    print('строк РФ-среза из PDF: %d' % len(rows))
    by_status = {}
    for r in rows:
        by_status[r[7]] = by_status.get(r[7], 0) + 1
    print('текущие статусы:', by_status)
    # контроль: сверка совпадающих по определению видов с приложением
    ctrl = tunnel.query("""
        SELECT o.period_start, o.sub_dimension, o.value
        FROM data.observation o JOIN core.metric m USING(metric_id)
        JOIN core.release r USING(release_id)
        WHERE m.metric_code = 'pste' AND r.release_label LIKE '%%R_10_2_4_pril%%'
          AND o.region_id = 1 AND o.period_start IN ('2021-01-01', '2023-01-01')
        ORDER BY 1, 2""")
    print('контроль из приложения (2021/2023, РФ):')
    for r in ctrl:
        print('   %s %-34s %s' % (r[0], r[1], r[2]))
    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для отметки superseded)')
        return 0
    with gzip.open(DUMP, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['observation_id', 'metric_code', 'release_label', 'period',
                    'region_id', 'sub_dimension', 'value', 'observation_status'])
        for r in rows:
            w.writerow([str(x) if x is not None else '' for x in r])
    print('дамп: %s (%d строк)' % (DUMP, len(rows)))
    tunnel.execute("""
        UPDATE data.observation o SET observation_status = 'superseded'
        FROM core.metric m, core.release r
        WHERE o.metric_id = m.metric_id AND o.release_id = r.release_id
          AND m.metric_code = 'pste' AND r.release_label LIKE '%%Table 2.26'
          AND o.observation_status <> 'superseded'""")
    after = tunnel.query("""
        SELECT o.observation_status, count(*) FROM data.observation o
        JOIN core.metric m USING(metric_id) JOIN core.release r USING(release_id)
        WHERE m.metric_code = 'pste' AND r.release_label LIKE '%%Table 2.26'
        GROUP BY 1""")
    print('после отметки:', after)
    live = tunnel.query("""
        SELECT count(*) FROM data.observation o
        JOIN core.metric m USING(metric_id) JOIN core.release r USING(release_id)
        WHERE m.metric_code = 'pste' AND r.release_label LIKE '%%R_10_2_4_pril%%'""")[0][0]
    print('строк приложения (активный срез) осталось: %d' % live)
    print('ИТОГ: данные не удалены, читатель по умолчанию берёт приложение')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
