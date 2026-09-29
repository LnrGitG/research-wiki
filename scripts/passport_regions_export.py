#!/usr/bin/env python3
"""Паспорт региона: экспорт JSON для GitHub Pages дашборда (29.09.2026).

Данные: region_slice_full_202610.csv (data/), перегенерируемый
scripts/region_slice_full.py после каждого обновления БД.
Мета: названия блоков, человеко-читаемые имена метрик, частоты, единицы.
Выход: docs/data/passport_regions.json (~14 метрик × 85 регионов × 13 мес).
"""
import csv
import json
import os
from collections import defaultdict
from datetime import date

SRC = os.path.join(os.path.dirname(__file__), '..', 'data', 'region_slice_full_202610.csv')
OUT = os.path.join(os.path.dirname(__file__), '..', 'docs', 'data', 'passport_regions.json')

META = {
    'emiss_31074_cpi_prevm_m': {'block': 'A', 'name': 'ИПЦ, % к пред. месяцу', 'unit': '%', 'freq': 'мес', 'dir': 1},
    'emiss_43062_unemp_q': {'block': 'B', 'name': 'Безработица МОТ 15+', 'unit': '%', 'freq': 'кв', 'dir': 1},
    'emiss_57824_wage_m': {'block': 'B', 'name': 'Номинальная ЗП', 'unit': 'руб.', 'freq': 'мес', 'dir': 0},
    'snz': {'block': 'F', 'name': 'Средняя начисленная ЗП', 'unit': 'руб.', 'freq': 'мес', 'dir': 0},
    'zkf': {'block': 'C', 'name': 'Кредиты физлицам, задолженность', 'unit': 'млн руб.', 'freq': 'мес', 'dir': 0},
    'zyi': {'block': 'C', 'name': 'Кредиты юрлицам, задолженность', 'unit': 'млн руб.', 'freq': 'мес', 'dir': 0},
    'vhdt': {'block': 'C', 'name': 'Жилищные кредиты, задолженность (VFS)', 'unit': 'млн руб.', 'freq': 'мес', 'dir': 0},
    'vmd': {'block': 'C', 'name': 'ИЖК, задолженность (канон.)', 'unit': 'млн руб.', 'freq': 'мес', 'dir': 0},
    'vhlvt': {'block': 'C', 'name': 'Выдачи жилищных кредитов', 'unit': 'млн руб.', 'freq': 'мес', 'dir': 0},
    'oipflrrivrsrf': {'block': 'C', 'name': 'Объём ИЖК (Т_19)', 'unit': 'млн руб.', 'freq': 'мес', 'dir': 0},
    'vhrr': {'block': 'C', 'name': 'Средняя ставка ИЖК', 'unit': '% год', 'freq': 'мес', 'dir': 1},
    'spsipflrrtmrsrf': {'block': 'C', 'name': 'Просрочка по ИЖК', 'unit': 'млн руб.', 'freq': 'мес', 'dir': 1},
    'rosstat_housing_total_m': {'block': 'E', 'name': 'Ввод жилья, всего', 'unit': 'тыс. м²', 'freq': 'мес', 'dir': 0},
    'rosstat_housing_pop_m': {'block': 'E', 'name': 'Ввод жилья населением (ИЖС)', 'unit': 'тыс. м²', 'freq': 'мес', 'dir': 0},
}
BLOCKS = {'A': 'Цены', 'B': 'Рынок труда', 'C': 'Кредитование и ДКУ',
          'E': 'Жильё и стройка', 'F': 'Доходы населения'}


def main():
    data = defaultdict(lambda: defaultdict(list))  # metric -> region -> [(period, value)]
    regions, codes = set(), set()
    with open(SRC, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            code, region, freq, period, val = (row['block_metric'], row['region'],
                                                row['freq'], row['period'], row['value'])
            if code not in META:
                continue
            try:
                v = float(val)
            except (ValueError, TypeError):
                continue
            data[code][region].append([period, round(v, 4)])
            regions.add(region)
            codes.add(code)
    for code in data:
        for reg in data[code]:
            data[code][reg].sort(key=lambda x: x[0])
    payload = {
        '_meta': {
            'title': 'Паспорт региона',
            'description': 'Основные показатели по блокам макро по субъектам РФ; '
                           'срез из БД v2 (region_slice), обновляется автоматически.',
            'generated': date.today().isoformat(),
            'blocks': BLOCKS,
            'metrics': META,
        },
        'regions': sorted(regions),
        'metrics': sorted(codes),
        'data': {code: dict(regions_data) for code, regions_data in data.items()},
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, separators=(',', ':'))
    print(f'passport_regions.json: метрик {len(codes)}, регионов {len(regions)}, '
          f'размер {os.path.getsize(OUT)//1024} КБ')


if __name__ == '__main__':
    main()