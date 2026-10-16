#!/usr/bin/env python3
"""Экспорт годовых рядов Росстата в docs/data/observations_dashboard.json
для GitHub Pages (docs/dashboard.html).

Источник — канон PostgreSQL (`data.observation` + `catalog.metric`), не SQLite:
прежняя таблица `observations` в `data/rosstat_construction.db` исчезла при
замене схемы файла 05.10.2026, из-за чего дашборд застыл на снимке 19.09.

Ряды (metric_code → датасеты витрины):
  y477110016        → housing_input_rf      (ввод жилья, РФ, тыс. м²)
  sfssokmpzpvvezzb  → cost_per_sqm_rf       (факт. стоимость 1 м², руб.)
  kpk               → flats_rf              (построено квартир, единиц)
  opnzdgvzbizd      → unfinished_ratio_rf   (незавершёнка к годовому вводу, %)
  dvmzoovz          → lowrise_share_rf      (доля малоэтажного ввода, %)
  y477110016        → housing_input_regions (по регионам за 2020 и 2021)

ВАЖНО про годы: в прежнем JSON год был сдвинут на единицу (значение за 2020
стояло под меткой 2019 и т.п.). Канон хранит корректную привязку, поэтому
пересобранный файл — исправление подписи лет, а не расхождение данных.

Запуск: python3 scripts/export_dashboard.py
"""
import json
import os
import sys
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from db_tunnel import query
except Exception as exc:  # noqa: BLE001
    print('db_tunnel недоступен: %s' % exc)
    raise SystemExit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / 'docs' / 'data'
os.makedirs(OUT, exist_ok=True)

RF = 'Российская Федерация%'


def _num(v):
    return float(v) if isinstance(v, Decimal) else v


def annual_rf(code):
    """Годовой ряд по РФ: [[год, значение], ...]."""
    rows = query(
        """
        SELECT EXTRACT(year FROM o.period_start)::int AS y, o.value
        FROM data.observation o
        JOIN catalog.metric m ON m.metric_id = o.metric_id
        LEFT JOIN catalog.region r ON r.region_id = o.region_id
        WHERE m.metric_code = %s AND r.name_ru ILIKE %s
        ORDER BY 1
        """,
        (code, RF),
    )
    by_year = {}
    for y, v in rows:
        by_year[y] = _num(v)
    return sorted(by_year.items())


def regions_for_year(code, year):
    """Разрез по регионам за год (без агрегатов уровня округа/РФ)."""
    rows = query(
        """
        SELECT r.name_ru, o.value
        FROM data.observation o
        JOIN catalog.metric m ON m.metric_id = o.metric_id
        JOIN catalog.region r ON r.region_id = o.region_id
        WHERE m.metric_code = %s
          AND EXTRACT(year FROM o.period_start)::int = %s
          AND r.name_ru NOT ILIKE %s
          AND r.name_ru NOT ILIKE %s
        ORDER BY r.name_ru
        """,
        (code, year, RF, '%округ%'),
    )
    return {name: _num(v) for name, v in rows}


datasets = {}

datasets['housing_input_rf'] = {
    'name': 'Ввод жилых домов, РФ',
    'unit': 'тыс. м²',
    'source': 'Росстат/ЕМИСС y477110016 (канон)',
    'data': annual_rf('y477110016'),
}
datasets['cost_per_sqm_rf'] = {
    'name': 'Средняя фактическая стоимость строительства 1 м²',
    'unit': 'руб.',
    'source': 'Росстат sfssokmpzpvvezzb (канон)',
    'data': annual_rf('sfssokmpzpvvezzb'),
}
datasets['flats_rf'] = {
    'name': 'Построено квартир',
    'unit': 'единиц',
    'source': 'Росстат kpk (канон)',
    'data': annual_rf('kpk'),
}
datasets['unfinished_ratio_rf'] = {
    'name': 'Незавершёнка к годовому вводу',
    'unit': '%',
    'source': 'Росстат opnzdgvzbizd (канон)',
    'data': annual_rf('opnzdgvzbizd'),
}
datasets['lowrise_share_rf'] = {
    'name': 'Доля малоэтажного жилья в вводе',
    'unit': '%',
    'source': 'Росстат dvmzoovz (канон)',
    'data': annual_rf('dvmzoovz'),
}
datasets['housing_input_regions'] = {
    'name': 'Ввод жилья по регионам',
    'unit': 'тыс. м²',
    'source': 'Росстат/ЕМИСС y477110016 (канон)',
    'data': {'2020': regions_for_year('y477110016', 2020),
             '2021': regions_for_year('y477110016', 2021)},
}

out_path = OUT / 'observations_dashboard.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(datasets, f, ensure_ascii=False)

print('Экспортировано:', ', '.join(datasets))
for k, v in datasets.items():
    d = v['data']
    if isinstance(d, list) and d:
        print('  %s: %d точек (%s → %s)' % (k, len(d), d[0][0], d[-1][0]))
    elif isinstance(d, dict):
        print('  %s: годы %s' % (k, ','.join(d)))
