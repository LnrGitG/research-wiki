#!/usr/bin/env python3
"""Add FNS opendata + Wordstat inflation/housing attention series to docs/data-summary.json."""
import json, csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'docs', 'data-summary.json')
with open(OUT, encoding='utf-8') as f:
    d = json.load(f)

# --- FNS: key annual series (RF-level, bln RUB) ---
rows = list(csv.DictReader(open(os.path.join(BASE, 'data', 'fns_rf_annual_long.csv'), encoding='utf-8')))
KEEP = [
    ('5-П', 'rev_profit', 'Прибыль организаций (5-П)'),
    ('5-П', 'exp_sales_profit', 'Расходы, всего (5-П)'),
    ('1-НДС', 'nds_accrued_total', 'НДС начисленный'),
    ('5-НДФЛ', 'ndfl_withheld', 'НДФЛ удержанный'),
    ('5-ТН', 'tnpayers', 'Налогоплательщики (тыс.)'),
    ('5-УСН', 'usn_income', 'УСН доходы'),
    ('5-УСН', 'usn_expense', 'УСН расходы'),
]
fns = {}
for form, met, name in KEEP:
    series = sorted((int(r['year']), float(r['rf_value_bln_rub']))
                    for r in rows if r['form'] == form and r['metric'] == met and r['partial'] == '0' and r['rf_value_bln_rub'].strip())
    if series:
        fns[f'fns_{met}'] = {'name': name, 'unit': 'млрд руб.' if 'налогоплат' not in name else 'тыс.',
                             'source': f'ФНС опендата, форма {form}',
                             'data': series}
d.update(fns)

# --- Wordstat inflation attention (macro-regions) ---
with open(os.path.join(BASE, 'data', 'wordstat_infl_attention_macro_monthly.csv'), encoding='utf-8') as f:
    r = csv.reader(f)
    header = next(r)
    macro = [{header[i]: float(row[i]) for i in range(1, len(header))} | {'date': row[0]} for row in r]
d['wordstat_infl_attention_macro'] = {
    'name': 'Внимание к инфляции по макрорегионам', 'unit': 'запросов на 100 тыс.',
    'source': 'Яндекс Wordstat (инфляция/рост цен/подорожание), 2018-01..2026-08',
    'data': macro}

# --- Wordstat subject-level (92 columns -> provide RF-median and top/bottom subjects via full matrix) ---
with open(os.path.join(BASE, 'data', 'wordstat_infl_attention_subjects_monthly.csv'), encoding='utf-8') as f:
    r = csv.reader(f)
    header = next(r)
    subj = [{header[i]: float(row[i]) for i in range(1, len(header))} | {'date': row[0]} for row in r]
# store compactly: population-weighted top-8 largest regions + RU average
key_regions = ['Москва и область', 'Санкт-Петербург и Ленинградская область',
               'Свердловская область', 'Челябинская область', 'Новосибирская область',
               'Республика Татарстан', 'Краснодарский край', 'Ростовская область']
d['wordstat_infl_attention_subjects'] = {
    'name': 'Внимание к инфляции, крупные регионы', 'unit': 'запросов на 100 тыс.',
    'source': 'Яндекс Wordstat (субъекты РФ, фраза «инфляция»), 2018-01..2026-08',
    'data': subj, 'regions': key_regions}

# --- Wordstat housing attention (macro) ---
with open(os.path.join(BASE, 'data', 'wordstat_housing_att_macro_monthly.csv'), encoding='utf-8') as f:
    r = csv.reader(f)
    header = next(r)
    hatt = [{header[i]: float(row[i]) for i in range(1, len(header))} | {'date': row[0]} for row in r]
d['wordstat_housing_attention'] = {
    'name': 'Внимание к ценам на жильё по макрорегионам', 'unit': 'запросов на 100 тыс.',
    'source': 'Яндекс Wordstat («цены на квартиры», «стоит ли покупать квартиру»)',
    'data': hatt}

d['_updated'] = '2026-09-01'
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False)
print('added:', list(fns.keys()), '+ 3 wordstat; total keys:', len(d))
