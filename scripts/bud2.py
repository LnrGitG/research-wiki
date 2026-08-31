#!/usr/bin/env python3
"""Дополнение шага 1: 
(1) отдельная таблица разделов budget_razdel (99 строк из XLSX, не только с ВР);
(2) таблица budget_vr_important — флаги интересов: subsidy_ks(632), subsidy_noks(633),
    grants(321/323), budinvest(814/815), soc_neformal(811/812/813);
(3) CSV зеркало справочника в data/ для wiki."""
import openpyxl, sqlite3, csv

wb = openpyxl.load_workbook('raw/minfin/vr_kosgu_2024_2026.xlsx')
ws = wb['Лист1']
rows = list(ws.iter_rows(min_row=1, values_only=True))
recs, sections, order = [], {}, []
for r in rows[3:]:
    name, kod_r, kod_v = r[0], r[1], r[2]
    name = str(name).strip() if name else ''
    kod_r = str(kod_r).strip() if kod_r else ''
    kod_v = str(kod_v).strip() if kod_v else ''
    if not kod_r:
        continue
    if not kod_v:
        if kod_r not in sections:
            sections[kod_r] = name
            order.append(kod_r)
        continue
    recs.append((kod_r, name))

con = sqlite3.connect('data/rosreestr_deals.db')
con.executescript('''
DROP TABLE IF EXISTS budget_razdel;
CREATE TABLE budget_razdel (razdel TEXT PRIMARY KEY, name TEXT);
''')
con.executemany('INSERT INTO budget_razdel VALUES (?,?)', [(k, sections[k]) for k in order])

# флаги интересов
con.executescript('''
DROP TABLE IF EXISTS budget_vr_important;
CREATE TABLE budget_vr_important AS
SELECT razdel, razdel_name, vr, vr_name,
  CASE WHEN vr IN ('632','633') THEN 1 ELSE 0 END AS is_subsidy,
  CASE WHEN vr IN ('321','323') THEN 1 ELSE 0 END AS is_grant,
  CASE WHEN vr IN ('814','815') THEN 1 ELSE 0 END AS is_budinvest
FROM budget_vr_dict;
''')
con.commit()
print('razdel:', con.execute('SELECT COUNT(*) FROM budget_razdel').fetchone(),
      '| important:', con.execute("SELECT is_subsidy, COUNT(*) FROM budget_vr_important GROUP BY is_subsidy").fetchall())

# CSV зеркало
with open('data/budget_vr_dict.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['razdel', 'razdel_name', 'vr', 'vr_name'])
    for row in con.execute("SELECT razdel, razdel_name, vr, vr_name FROM budget_vr_dict ORDER BY razdel, vr"):
        w.writerow(row)
print('CSV written')