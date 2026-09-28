#!/usr/bin/env python3
"""Региональный срез «регион × переменная» (блоки A/B/C/E/F) для доклада ГУ.

Блоки (без D и общефедеральных условий):
- A (инфляция):        emiss_31074_cpi_prevm_m (ИПЦ, % к пред. мес.)
- B (спрос/труд):      emiss_57824_wage_m (ЗП), emiss_43062_unemp_q (безработица МОТ)
- C (ДКУ/кредит):      zkf (кредиты физлицам), zyi (кредиты юрлицам), vhdt (жилищные
                       кредиты VFS, задолженность), vmd (ИЖК ЦБ, задолженность),
                       vhlvt (выдачи VFS), oipflrrivrsrf (объём ИЖК ЦБ Т_19),
                       vhrr / spsipflrrtmrsrf (ставки VFS / ЦБ Т_26)
- E (жильё/стройка):   rosstat_housing_total_m, rosstat_housing_pop_m (ИЖС)
- F (опорные):         snz (средняя ЗП Росстата)

Выход: data/region_slice_full_202610.csv (регион × метрика × месяц), формат длинный.

Глубина: MONTHS_BACK = 15 месяцев от последней доступной точки метрики.
Глубина выбрана под окно «год к году»: для потоковых и уровневых рядов
(ввод жилья, выдачи, задолженность, ЗП) сравнение идёт с одноимённым
3-месячным окном годом ранее — это снимает сезонность, из-за которой
сырое сравнение с предыдущим окном помечало половину стройки аномалиями.
Для коротких рядов (ЦБ ИЖК с 07.2025) год истории может не набраться —
отчёт помечает такие динамики как неочищенные от сезонности.
"""
import csv
import os
import sys
from datetime import date

sys.path.insert(0, os.path.expanduser('~/research-wiki-private/scripts'))
import db_tunnel

OUT = os.path.expanduser('~/research-wiki-private/data/region_slice_full_202610.csv')
MONTHS_BACK = 15

METRICS = {
    'A_cpi': 'emiss_31074_cpi_prevm_m',
    'B_wage': 'emiss_57824_wage_m',
    'B_unemp': 'emiss_43062_unemp_q',
    'C_kf': 'zkf',
    'C_kyl': 'zyi',
    # Жилищный блок: два определения рядом — длинный ряд VFS (сопоставления и исследования)
    # и свежий ряд ЦБ по ИЖК в каноническом коде vmd (актуализация; ряд zia — алиас,
    # перенесён в vmd 26.09.2026). Прежние vmd/vmnl/vmod/virtr несли ряды потребительского
    # кредита из-за коллизии меток в parse_cbr_lending.py — дефектные строки в карантине.
    'C_hdebt_long': 'vhdt',
    'C_mdebt_ihk': 'vmd',
    'C_hnew_long': 'vhlvt',
    'C_mnew_ihk': 'oipflrrivrsrf',
    'C_hrate_long': 'vhrr',
    'C_irate_ihk': 'spsipflrrtmrsrf',
    'E_housing': 'rosstat_housing_total_m',
    'E_izhs': 'rosstat_housing_pop_m',
    'F_snz': 'snz',
}


def main():
    db_tunnel.connect()
    rows = db_tunnel.query(f"""
        WITH last_periods AS (
            SELECT metric_id, MAX(period_start) AS max_p
            FROM core.observation_v2 WHERE region_id > 9 AND observation_status <> 'rejected' GROUP BY metric_id)
        SELECT m.metric_code, r.name_ru, o.frequency_id, o.period_start, o.value,
               coalesce(array_to_string(o.quality_flags, ';'), '') AS quality_flag
        FROM core.observation_v2 o
        JOIN core.metric m ON m.metric_id = o.metric_id
        JOIN core.region r ON r.region_id = o.region_id
        JOIN last_periods lp ON lp.metric_id = m.metric_id
        WHERE o.region_id > 9 AND o.sub_dimension = ''
          AND o.observation_status <> 'rejected'
          AND m.metric_code = ANY(%(codes)s)
          AND o.period_start >= lp.max_p - interval '{MONTHS_BACK} months'
        ORDER BY m.metric_code, r.name_ru, o.period_start;""",
        {'codes': list(METRICS.values())})
    print('rows fetched:', len(rows))
    n = 0
    with open(OUT, 'w', newline='') as f:
        w = csv.writer(f)
        # quality_flag несёт пометки определения ряда (например,
        # old_definition_15_72 у безработицы до 2017 года): точка, помеченная
        # здесь, публикуется только с этой пометкой.
        w.writerow(['block_metric', 'region', 'freq', 'period', 'value', 'quality_flag'])
        for mc, reg, fq, ps, v, qf in rows:
            w.writerow([mc, reg, fq, ps, v, qf])
            n += 1
    print('written', n, '->', OUT)
    # сводка
    from collections import Counter
    c = Counter(r[0] for r in rows)
    for k, v in sorted(c.items()):
        print(f'  {k}: {v}')


if __name__ == '__main__':
    main()