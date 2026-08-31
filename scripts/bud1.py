#!/usr/bin/env python3
"""Шаг 1: справочник бюджетной классификации в rosreestr_deals.db
Источник: таблица соответствия разделов/подразделов и видов расходов (Минфин, приказ 139н,
бюджеты субъектов 2024-2026). Разбор XLSX (Лист1) → таблица budget_vr_dict.
Дополнительно: свод по интересным ВР (субсидии 632/633/811/851, капвложения 814, ипотека-ЦСР не в этой таблице)."""
import openpyxl, sqlite3, re

SRC = 'raw/minfin/vr_kosgu_2024_2026.xlsx'
wb = openpyxl.load_workbook(SRC)
ws = wb['Лист1']

rows = list(ws.iter_rows(min_row=1, values_only=True))
recs = []          # (section, name, vr)
current_section, current_section_name = None, None
section_names = {}  # razdel kod -> name

for r in rows[3:]:
    name, kod_r, kod_v = r[0], r[1], r[2]
    name = str(name).strip() if name else ''
    kod_r = str(kod_r).strip() if kod_r else ''
    kod_v = str(kod_v).strip() if kod_v else ''
    if not kod_r:
        continue
    if not kod_v:  # строка = раздел/подраздел
        section_names[kod_r] = name
        current_section = kod_r
        continue
    recs.append((current_section, section_names.get(current_section, ''), kod_v, name))

print('строк-разделов:', len(section_names), '| пар раздел×ВР:', len(recs))

con = sqlite3.connect('data/rosreestr_deals.db')
con.executescript('''
DROP TABLE IF EXISTS budget_vr_dict;
CREATE TABLE budget_vr_dict (
    razdel TEXT, razdel_name TEXT, vr TEXT, vr_name TEXT,
    PRIMARY KEY (razdel, vr)
);
''')
con.executemany('INSERT OR IGNORE INTO budget_vr_dict VALUES (?,?,?,?)',
                [(s, sn, v, n) for (s, sn, v, n) in recs])
con.commit()
print('inserted:', con.execute("SELECT COUNT(*) FROM budget_vr_dict").fetchone()[0])

# Проверка: интересующие ВР
qs = '''
SELECT vr, COUNT(DISTINCT razdel) n_razdelov FROM budget_vr_dict WHERE vr IN
('632','633','811','812','813','814','831','851','321','323') GROUP BY vr ORDER BY vr
'''
for row in con.execute(qs):
    print(row)

# Смысл ключевых ВР (по справочнику 139н): 244 прочая закупка, 632/633 субсидии с/без казнач.сопровождения,
# 811 СО НКО, 812 взносы, 813 субсидии бюджетным/автономным учреждениям, 814 бюджетные инвестиции,
# 321 гранты, 851/853... — выведем для примера по разделу 11 (жилье)
print('--- Раздел 11 (жильё) выборка:')
for row in con.execute("SELECT razdel, vr, vr_name FROM budget_vr_dict WHERE razdel='1110' LIMIT 12"):
    print(row)
con.close()