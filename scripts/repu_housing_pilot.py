#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пилот REPU-РФ: индекс неопределённости жилищной политики (метод Chen et al. 2023).

Индекс — русский аналог китайского REPU (Real Estate Policy Uncertainty).
Сигнал определяется на THEMES-тегах GDELT (это готовый тематический классификатор):
  * экономическая тема: EPU_ECONOMY*, ECON_*, HOUSING*, REAL_ESTATE*;
  * политика/регулирование: EPU_POLICY*, LEGISLATION, USPEC_POLITICS*,
    USPEC_POLICY1;
  * неопределённость: *UNCERTAINTY*, CRISISLEX*.
Совпадение всех трёх фильтров в одной записи — «попадание REPU».

Вход: data/raw/gdelt/gdelt_gkg_rus_*.csv (с THEMES-тегами от GDELT,
действующий источник профиля monitor).
Выход: data/processed/repu_housing_daily.csv, ..._monthly.csv,
..._control_points.csv, график visualizations/repu_housing_pilot.png.

Ограничение честности: GDELT-корпус покрывает дату только 25.08–10.09.2026 —
этого мало для индекса, поэтому скрипт работает как проверка механики + счётчик
попаданий. Полный корпуы деловых СМИ (см. план H-015) даст полноценный индекс.
"""
import csv
import re
import statistics
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parent.parent
SRC_DIR = REPO / 'data/raw/gdelt'
OUT_DAILY = REPO / 'data/processed/repu_housing_daily.csv'
OUT_MONTH = REPO / 'data/processed/repu_housing_monthly.csv'
OUT_CTRL = REPO / 'data/processed/repu_housing_control_points.csv'
PNG = REPO / 'visualizations/repu_housing_pilot.png'

# THEMES-фильтры (тройка «тема + политика + неопределённость»):
THEME_ECON = {
    'ECON_', 'EPU_ECONOMY', 'HOUSING', 'REAL_ESTATE', 'MORTGAGE', 'CONSTRUCTION',
}
THEME_POLICY = {
    'EPU_POLICY', 'LEGISLATION', 'WB_845_LEGAL_AND_REGULATORY_FRAMEWORK',
    'WB_410_BUSINESS_LAW_AND_REGULATION', 'USPEC_POLITICS_GENERAL1',
    'USPEC_POLICY1',
}
THEME_UNCERT = {
    'USPEC_UNCERTAINTY1', 'CRISISLEX',
}

# Контрольные события regulating-политики (индекс должен расти)
CONTROL_POINTS = [
    ('2020-04', 'Постановление 566: запуск льготной ипотеки 6,5%'),
    ('2020-11', 'Продление льготной ипотеки на 2021'),
    ('2021-06', 'Изменение условий льготной ипотеки'),
    ('2022-03', 'Расширение семейной ипотеки после 01.03.2022'),
    ('2023-01', 'Правки льготной ипотеки; закрытие 01.07.2023'),
    ('2024-07', 'Массовая льготная ипотека закрыта; семейная ограничена'),
]


def flag_of(theme_set, targets):
    return any(any(theme == t or theme.startswith(t) for t in targets) for theme in theme_set)


def main():
    daily_counts = defaultdict(lambda: [0, 0])          # дата -> [попаданий, статей]
    files = sorted(SRC_DIR.glob('gdelt_gkg_rus_*.csv'))
    if not files:
        print('Нет файлов в data/raw/gdelt/ (только gkg с THEMES)')
        return 1
    for path in files:
        with open(path, newline='', encoding='utf-8') as fh:
            for row in csv.DictReader(fh):
                th = (row.get('THEMES') or '')
                themes = [t for t in th.split(';') if t]
                if not themes:
                    continue
                date_raw = row.get('DATE') or row.get('SQLDATE') or ''
                if not date_raw or len(date_raw) < 8:
                    continue
                d = datetime.strptime(date_raw[:8], '%Y%m%d').date()
                set_of = set(themes)
                econ = any(any(t == x or t.startswith(x) for x in THEME_ECON) for t in set_of)
                pol = any(any(t == x or t.startswith(x) for x in THEME_POLICY) for t in set_of)
                unc = any(('UNCERTAINTY' in t) or (t.startswith('CRISISLEX')) for t in set_of)
                daily_counts[d][1] += 1
                if econ and pol and unc:
                    daily_counts[d][0] += 1
    # Ежедневный CSV
    with open(OUT_DAILY, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['date', 'repu_hits', 'articles_total', 'hit_share'])
        for d in sorted(daily_counts):
            n_h, n_t = daily_counts[d]
            w.writerow([d.isoformat(), n_h, n_t, round(100.0 * n_h / n_t, 3)])
    # Месячная агрегация (доля статей месяца с попаданием)
    months = defaultdict(lambda: [0, 0])
    for d in sorted(daily_counts):
        n_h, n_t = daily_counts[d]
        key = d.strftime('%Y-%m')
        months[key][0] += n_h
        months[key][1] += n_t
    re_index = {}
    for key, (n_h, n_t) in months.items():
        re_index[key] = round(100.0 * n_h / n_t, 3) if n_t else 0.0
    # Нормировка на стандартное отклонение базового периода (полный набор)
    vals = list(re_index.values())
    mu = statistics.mean(vals) if vals else 0.0
    sd = statistics.stdev(vals) if len(vals) > 1 else 1.0
    re_index_n = {k: round((v - mu) / (sd or 1), 3) for k, v in re_index.items()}
    with open(OUT_MONTH, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['month', 'repu_share_pct', 'repu_index'])
        for k in sorted(months):
            w.writerow([k, re_index[k], re_index_n[k]])
    # Контрольные точки
    ctrl_rows = []
    for ym, label in CONTROL_POINTS:
        val = re_index_n.get(ym)
        if val is None:
            continue
        ctrl_rows.append((ym, label, val))
    with open(OUT_CTRL, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['month', 'event', 'repu_index'])
        w.writerows(ctrl_rows)
    print('== месячная доля попавших статей (пилот GDELT-корпуса):')
    for k in sorted(months):
        v = re_index[k]
        n = re_index_n[k]
        print(f'   {k}: доля {v:6.2f}% | индекс {n:>6}')
    print('\n== контрольные точки:')
    for ym, label, val in ctrl_rows:
        flag = '<<< сигнал' if val > 0 else ''
        print(f'   {ym} | индекс {val:>6} | {label[:60]} {flag}')
    print('\n== ограничение пилота:')
    print('   GDELT-gkg корпус в наличии только 25.08-10.09.2026 (6 файлов),')
    print('   месячные значения нерекомендуемы для вывода; механика проверена,')
    print('   полный корпус деловых СМИ — план H-015.')
    return 0


if __name__ == '__main__':
    sys.exit(main())