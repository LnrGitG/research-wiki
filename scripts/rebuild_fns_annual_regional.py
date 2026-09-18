#!/usr/bin/env python3
"""
Пересборка staging.rosreestr_deals__fns_annual_regional на исправленном profitorg.

Таблица собирается из трёх источников ФНС: 1-НОМ (ОКВЭД F), profitorg (5-П,
выручка) и НДФЛ. Из них profitorg был испорчен кодировкой, поэтому выручка
приходила с битыми именами регионов. Остальные два чистые.

Запуск:  python3 rebuild_fns_annual_regional.py [--apply]
"""
import os
import sys
import re

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
APPLY = "--apply" in sys.argv

conn = psycopg.connect(DSN)
cur = conn.cursor()


def norm(name):
    """Нормализация написаний регионов."""
    r = re.sub(r"\s+", " ", (name or "").strip())
    m = {
        "Г.Санкт-Петербург": "г. Санкт-Петербург",
        "г.Санкт-Петербург": "г. Санкт-Петербург",
        "город Санкт-Петербург": "г. Санкт-Петербург",
        "Г.Севастополь": "г. Севастополь",
        "г.Севастополь": "г. Севастополь",
        "город Севастополь": "г. Севастополь",
        "Ямало-Hенецкий АО": "Ямало-Ненецкий АО",
        "Республика Марий-Эл": "Республика Марий Эл",
        "Республики Марий Эл": "Республика Марий Эл",
        "Архангельская область и Ненецкий автономный округ": "Архангельская область (с НАО)",
        "Архангельская область + Ненецкий АО": "Архангельская область (с НАО)",
        "Республика Татарстан)": "Республика Татарстан",
    }
    return m.get(r, r)


# 1-НОМ: выручка по ОКВЭД F, последний снапшот на отчётный год
cur.execute("""SELECT region, snapshot_date, value
               FROM staging."rosreestr_deals__fns_1nom_okved_f_quarterly"
               WHERE metric='G53_okved_F'""")
rows_1nom = cur.fetchall()

# profitorg: доходы от реализации по прибыльным, последний снапшот на год
cur.execute("""SELECT region, snapshot, value
               FROM staging."rosreestr_deals__fns_profitorg_key_quarterly"
               WHERE field LIKE 'Доходы от реализации по прибыльным%'""")
rows_prof = cur.fetchall()

# НДФЛ
cur.execute("""SELECT region, snapshot, value
               FROM staging."rosreestr_deals__fns_ndfl_regional"
               WHERE field='G1'""")
rows_ndfl = cur.fetchall()


def rep_year(snap):
    """Отчётный год: январский срез относится к предыдущему году."""
    s = str(snap)
    y, m = int(s[:4]), int(s[4:6]) if len(s) >= 6 else 1
    return y - (1 if m == 1 else 0)


out = []
seen = set()

# 1-НОМ (отбираем последний снапшот по региону и году)
tmp = {}
for region, snap, val in rows_1nom:
    k = (norm(region), rep_year(snap))
    if k not in tmp or str(snap) > str(tmp[k][0]):
        tmp[k] = (snap, val)
for (region, y), (_, val) in tmp.items():
    out.append(("1nom_okved_F", region, y, "G53_okved_F", float(val)))

# profitorg
tmp = {}
for region, snap, val in rows_prof:
    k = (norm(region), rep_year(snap))
    if k not in tmp or str(snap) > str(tmp[k][0]):
        tmp[k] = (snap, val)
for (region, y), (_, val) in tmp.items():
    out.append(("profitorg", region, y, "rev_profit", float(val)))

# НДФЛ
for region, snap, val in rows_ndfl:
    out.append(("ndfl", norm(region), rep_year(snap), "ndfl", float(val)))

print("строк к записи: %s" % format(len(out), ","))
from collections import Counter
c = Counter(r[0] for r in out)
for form, n in sorted(c.items()):
    regs = len({r[1] for r in out if r[0] == form})
    print("   %-14s строк=%-5s регионов=%s" % (form, format(n, ","), regs))

bad = [r for r in out if "\ufffd" in r[1]]
print("\nстрок с битым именем: %s" % len(bad))

if not APPLY:
    print("\nСУХОЙ ПРОГОН. Применить: python3 rebuild_fns_annual_regional.py --apply")
    conn.close()
    sys.exit(0)

cur.execute("DROP TABLE IF EXISTS staging.rosreestr_deals__fns_annual_regional_new")
cur.execute("""CREATE TABLE staging.rosreestr_deals__fns_annual_regional_new (
    form text, region text, year int, metric text, value numeric)""")
cur.executemany("""INSERT INTO staging.rosreestr_deals__fns_annual_regional_new
                   VALUES (%s,%s,%s,%s,%s)""", out)
conn.commit()
cur.execute("SELECT count(*) FROM staging.rosreestr_deals__fns_annual_regional_new")
print("\nзаписано: %s" % format(cur.fetchone()[0], ","))
cur.execute("DROP TABLE staging.rosreestr_deals__fns_annual_regional")
cur.execute("""ALTER TABLE staging.rosreestr_deals__fns_annual_regional_new
               RENAME TO rosreestr_deals__fns_annual_regional""")
conn.commit()
print("таблица заменена")

# обновляем region_id
cur.execute("""ALTER TABLE staging.rosreestr_deals__fns_annual_regional
               ADD COLUMN IF NOT EXISTS region_id int""")
cur.execute("SELECT region_id, name_ru FROM core.region")
reg = {re.sub(r"\s+", " ", n).strip().lower(): i for i, n in cur.fetchall()}
cur.execute("SELECT alias, region_id FROM meta.region_alias")
for a, i in cur.fetchall():
    reg.setdefault(re.sub(r"\s+", " ", a).strip().lower(), i)
cur.execute("SELECT DISTINCT region FROM staging.rosreestr_deals__fns_annual_regional")
for (nm,) in cur.fetchall():
    rid = reg.get(re.sub(r"\s+", " ", nm).strip().lower())
    if rid:
        cur.execute("""UPDATE staging.rosreestr_deals__fns_annual_regional
                       SET region_id=%s WHERE region=%s""", (rid, nm))
    else:
        print("   НЕ НАЙДЕН: %r" % nm)
conn.commit()
print("region_id проставлен")
conn.close()
