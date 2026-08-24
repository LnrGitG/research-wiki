#!/usr/bin/env python3
"""
Экспорт данных observations → docs/data/observations_dashboard.json для GitHub Pages дашборда.
Запуск: python3 scripts/export_dashboard.py (после каждого обновления БД).
"""
import sqlite3, json, os

DB = '/home/lnr/research-wiki/data/rosstat_construction.db'
OUT = '/home/lnr/research-wiki/docs/data'
os.makedirs(OUT, exist_ok=True)

db = sqlite3.connect(DB)
cur = db.cursor()

# Дедупликация id=52 (стоимость строительства): лист содержит 3 блока
# (Всего/городское/сельское) с одинаковыми метками — берём max как «Всего».
def rf_series(indicator_id):
    rows = cur.execute("""
        SELECT period, value FROM observations 
        WHERE indicator_id=? AND region_name='Российская Федерация'
        ORDER BY CAST(period AS INTEGER), value
    """, (indicator_id,)).fetchall()
    by_year = {}
    for period, value in rows:
        y = int(period)
        if y not in by_year or value > by_year[y]:
            by_year[y] = value
    return sorted(by_year.items())

datasets = {}

datasets['housing_input_rf'] = {
    'name': 'Ввод жилых домов, РФ', 'unit': 'тыс. м²',
    'source': 'Росстат, vvod_jil_dom_RF_2025.xls',
    'data': rf_series(41)          # 1990–2021
}
datasets['cost_per_sqm_rf'] = {
    'name': 'Средняя фактическая стоимость строительства 1 м²', 'unit': 'руб.',
    'source': 'Росстат (max из 3 блоков листа)',
    'data': rf_series(52)          # 1999–2020
}
datasets['flats_rf'] = {
    'name': 'Построено квартир', 'unit': 'единиц',
    'source': 'Росстат',
    'data': rf_series(44)          # 2000–2021
}

rows = cur.execute("""
    SELECT period, value FROM observations 
    WHERE indicator_id=11 AND region_name='Российская Федерация'
""").fetchall()
datasets['unfinished_ratio_rf'] = {
    'name': 'Незавершёнка к годовому вводу', 'unit': '%',
    'source': 'Росстат',
    'data': sorted((int(p), v) for p, v in rows)   # 2000–2021
}

rows = cur.execute("""
    SELECT period, value FROM observations 
    WHERE indicator_id=50 AND region_name='Российская Федерация'
""").fetchall()
datasets['lowrise_share_rf'] = {
    'name': 'Доля малоэтажного жилья в вводе', 'unit': '%',
    'source': 'Росстат',
    'data': sorted((int(p), v) for p, v in rows)   # 2012–2021
}

rows = cur.execute("""
    SELECT region_name, period, value FROM observations 
    WHERE indicator_id=41 AND period IN ('2020','2021')
      AND region_name NOT LIKE '%округ%' AND region_name != 'Российская Федерация'
""").fetchall()
r20, r21 = {}, {}
for reg, per, v in rows:
    (r21 if per == '2021' else r20)[reg] = v
datasets['housing_input_regions'] = {
    'name': 'Ввод жилья по регионам', 'unit': 'тыс. м²',
    'data': {'2020': r20, '2021': r21}
}

with open(f'{OUT}/observations_dashboard.json', 'w', encoding='utf-8') as f:
    json.dump(datasets, f, ensure_ascii=False)

print('Экспортировано:', ', '.join(datasets.keys()))
db.close()
