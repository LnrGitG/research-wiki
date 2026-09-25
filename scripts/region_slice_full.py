#!/usr/bin/env python3
"""Первый полный региональный срез «регион × переменная» (блоки A/B/C/E/F).

Блоки для доклада начальника ГУ (без D и общефедеральных условий):
- A (инфляция):        emiss_31074_cpi_prevm_m (ИПЦ, % к пред. мес.)
- B (спрос/труд):      emiss_57824_wage_m (ЗП), emiss_43062_unemp_q (безработица МОТ)
- C (ДКУ/кредит):      zkf (кредиты физлицам), zyli_2 (кредиты юрлицам), vmd (ИЖК задолженность),
                       vmnl (новые ИЖК), vfs_ihc_rate_total_rub (ставка ИЖК)
- E (жильё/стройка):   rosstat_housing_total_m, rosstat_housing_pop_m (ИЖС)
- F (опорные):         snz (средняя ЗП Росстата)

Выход: data/region_slice_full_202610.csv (регион × метрика × месяц),
последние 6 месяцев доступных данных. Формат длинный.
"""
import csv
import os
import sys
from datetime import date

sys.path.insert(0, os.path.expanduser('~/research-wiki-private/scripts'))
import db_tunnel

OUT = os.path.expanduser('~/research-wiki-private/data/region_slice_full_202610.csv')
MONTHS_BACK = 6

METRICS = {
    'A_cpi': 'emiss_31074_cpi_prevm_m',
    'B_wage': 'emiss_57824_wage_m',
    'B_unemp': 'emiss_43062_unemp_q',
    'C_kf': 'zkf',
    'C_kyl': 'zyli',
    'C_mdebt': 'vmd',
    'C_mnew': 'vmnl',
    'C_irate': 'virtr',
    'E_housing': 'rosstat_housing_total_m',
    'E_izhs': 'rosstat_housing_pop_m',
    'F_snz': 'snz',
}


def main():
    db_tunnel.connect()
    n_months = 6 if True else 0
    rows = db_tunnel.query(f"""
        WITH last_periods AS (
            SELECT metric_id, MAX(period_start) AS max_p
            FROM core.observation_v2 WHERE region_id > 9 GROUP BY metric_id)
        SELECT m.metric_code, r.name_ru, o.frequency_id, o.period_start, o.value
        FROM core.observation_v2 o
        JOIN core.metric m ON m.metric_id = o.metric_id
        JOIN core.region r ON r.region_id = o.region_id
        JOIN last_periods lp ON lp.metric_id = m.metric_id
        WHERE o.region_id > 9 AND o.sub_dimension = ''
          AND m.metric_code = ANY(%(codes)s)
          AND o.period_start >= lp.max_p - interval '{MONTHS_BACK} months'
        ORDER BY m.metric_code, r.name_ru, o.period_start;""",
        {'codes': list(METRICS.values())})
    print('rows fetched:', len(rows))
    n = 0
    with open(OUT, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['block_metric', 'region', 'freq', 'period', 'value'])
        for mc, reg, fq, ps, v in rows:
            w.writerow([mc, reg, fq, ps, v])
            n += 1
    print('written', n, '->', OUT)
    # сводка
    from collections import Counter
    c = Counter(r[0] for r in rows)
    for k, v in sorted(c.items()):
        print(f'  {k}: {v}')


if __name__ == '__main__':
    main()