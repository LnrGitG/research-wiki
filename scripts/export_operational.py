import sqlite3, json, os

db = sqlite3.connect('/home/lnr/research-wiki/data/rosstat_construction.db')
cur = db.cursor()
OUT = '/home/lnr/research-wiki/docs/data'
os.makedirs(OUT, exist_ok=True)

D = {}

# ---------- 1. Ввод жилья (operational monthly) ----------
rows = cur.execute("""
    SELECT report_year, report_month, indicator, value, yoy_pct
    FROM housing_input_operational_monthly
    WHERE region_name='Российская Федерация'
    ORDER BY report_year, report_month
""").fetchall()
series = {}
for y, m, ind, v, yoy in rows:
    key = f"{y}-{m:02d}"
    series.setdefault(key, {})[ind] = {'value': round(v, 1), 'yoy': round(yoy, 1) if yoy else None}
D['housing_input'] = {
    'name': 'Ввод жилья (оперативно)', 'unit': 'тыс. м²',
    'source': 'Росстат, jil_dom-oper (помесячно)',
    'monthly': series
}

# ---------- 2. СМР ----------
rows = cur.execute("""
    SELECT report_year, report_month, value_bln_rub, yoy_pct
    FROM construction_volume_monthly_rf WHERE report_month IS NOT NULL
    ORDER BY report_year, report_month
""").fetchall()
D['construction_works'] = {
    'name': 'СМР', 'unit': 'млрд руб.',
    'source': 'Росстат, соц-эк положение',
    'monthly': {f"{y}-{m:02d}": {'value': v, 'yoy': yy} for y, m, v, yy in rows}
}
# квартал/полугодие отдельно
rows = cur.execute("""
    SELECT period_label, report_year, value_bln_rub, yoy_pct
    FROM construction_volume_monthly_rf WHERE report_month IS NULL
""").fetchall()
D['construction_works_agg'] = [
    {'label': lb, 'year': y, 'value': v, 'yoy': yy} for lb, y, v, yy in rows
]

# ---------- 3. Договоры подряда ----------
rows = cur.execute("""
    SELECT report_year, report_month, contracts_bln_rub, backlog_months
    FROM construction_contracts_monthly_rf ORDER BY report_year, report_month
""").fetchall()
D['contracts'] = {
    'name': 'Договоры строительного подряда', 'unit': 'млрд руб.',
    'source': 'Росстат',
    'monthly': {f"{y}-{m:02d}": {'value': v, 'backlog': b} for y, m, v, b in rows}
}

# ---------- 4. Мониторинг ЦБ (12 вопросов × 2 корректировки) ----------
QMAP = {}
rows = cur.execute("SELECT DISTINCT question FROM cbr_monitoring_construction").fetchall()
for i, (q,) in enumerate(rows):
    if '(ожид.)' in q:
        QMAP[q] = 'ibk_expected'
    elif '(факт.)' in q:
        QMAP[q] = 'ibk_actual'
    elif q.startswith('Индикатор'):
        QMAP[q] = 'ibk'
    elif 'объем производства' in q and 'ближайшие' not in q:
        QMAP[q] = 'production'
    elif 'спрос на' in q and 'ближайшие' not in q:
        QMAP[q] = 'demand'
    elif 'цены на готовую' in q:
        QMAP[q] = 'prices'
    elif 'Ценовые ожидания' in q:
        QMAP[q] = 'price_expectations'
    elif 'издержки' in q:
        QMAP[q] = 'costs'
    elif 'условия кредитования' in q:
        QMAP[q] = 'credit_conditions'

rows = cur.execute("""
    SELECT date, question, adjustment, value FROM cbr_monitoring_construction
""").fetchall()
mon = {}
for d, q, adj, v in rows:
    key = QMAP.get(q)
    if not key:
        continue
    adj_key = 'raw' if adj == 'Исходные данные' else 'sa'
    mon.setdefault(f'{key}|{adj_key}', {})[d[:7]] = round(v, 2)
D['cbr_monitoring'] = mon

# question map for legend
LEGEND = {
    'ibk': 'ИБК сводный',
    'ibk_actual': 'ИБК фактический',
    'ibk_expected': 'ИБК ожидания',
    'production': 'Производство (факт)',
    'demand': 'Спрос (факт)',
    'prices': 'Цены на продукцию',
    'price_expectations': 'Ценовые ожидания 3м',
    'costs': 'Издержки',
    'credit_conditions': 'Условия кредитования'
}
# средний ожидаемый темп прироста цен — отдельный вопрос в %; найдём его точное имя
row = cur.execute("""
    SELECT DISTINCT question FROM cbr_monitoring_construction 
    WHERE question LIKE '%Средний ожидаемый%'
""").fetchone()
if row:
    LEGEND['price_inflation_exp'] = 'Ожидаемый прирост цен, %'
rows = cur.execute("SELECT date, value FROM cbr_monitoring_construction WHERE adjustment='Исходные данные' AND question LIKE '%Средний ожидаемый%'").fetchall()
mon['price_inflation_exp|raw'] = {d[:7]: round(v, 2) for d, v in rows if v is not None}
D['monitoring_legend'] = LEGEND

# ---------- 5. Эскроу (РФ агрегаты по месяцам) ----------
rows = cur.execute("""
    SELECT report_date, indicator, SUM(value)
    FROM cbr_escrow_monthly
    WHERE indicator IN ('escrow_balance','escrow_accounts_count','escrow_credit_debt')
      AND region_name NOT LIKE '%ОКРУГ%'
    GROUP BY report_date, indicator ORDER BY report_date
""").fetchall()
esc = {}
for d, ind, v in rows:
    esc.setdefault(d[:7], {})[ind] = round(v, 1)
D['escrow'] = {
    'name': 'Эскроу-счета', 'unit': 'млн руб / шт',
    'source': 'ЦБ РФ',
    'monthly': esc
}

# ---------- 6. Зарплата ----------
rows = cur.execute("""
    SELECT year, month, wage_rub FROM average_wage_monthly_regional
    WHERE region_name LIKE '%Российская%' ORDER BY year, month
""").fetchall()
D['wage'] = {
    'name': 'Номинальная зарплата (все отрасли)', 'unit': 'руб/мес',
    'source': 'Росстат',
    'monthly': {f"{y}-{m:02d}": round(w, 0) for y, m, w in rows}
}

with open(f'{OUT}/operational_dashboard.json', 'w', encoding='utf-8') as f:
    json.dump(D, f, ensure_ascii=False)

import os as o
print(f"Экспортировано {o.path.getsize(f'{OUT}/operational_dashboard.json')//1024} КБ")
for k, v in D.items():
    if isinstance(v, dict) and 'monthly' in v:
        months = sorted(v['monthly'].keys())
        print(f"  {k}: {len(months)} мес ({months[0]} → {months[-1]})")
db.close()
