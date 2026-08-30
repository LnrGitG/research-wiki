#!/usr/bin/env python3
"""Финал: 1-НОМ — старые файлы с ';' разделителем (hdr не разбился) → сниф均匀 разделителя и перезаливка.
Ожидаем 52 снимка × ~85 регионов."""
import csv, glob, re, sqlite3, pandas as pd
import io

con = sqlite3.connect('data/rosreestr_deals.db')
con.execute("DELETE FROM fns_1nom_okved_f_quarterly")
n = 0
snaps = set()
for f in sorted(glob.glob('raw/fns/1nom_????????.csv')):
    snap = re.search(r'1nom_(\d{8})\.csv', f).group(1)
    txt = open(f, encoding='utf-8', errors='replace').read()
    first = txt.splitlines()[0]
    delim = ';' if first.count(';') > first.count(',') else ','
    rows = list(csv.reader(io.StringIO(txt), delimiter=delim))
    if not rows:
        continue
    hdr = rows[0]
    if 'G53' not in hdr:
        continue
    g53 = hdr.index('G53')
    for r in rows[2:]:
        if len(r) <= g53:
            continue
        reg = r[1] if len(r) > 1 else ''
        if not reg or reg in ('Б', 'A') or len(reg) < 5:
            continue
        try:
            v = float((r[g53] or '0').replace(' ', '').replace(',', '.'))
            con.execute("INSERT OR REPLACE INTO fns_1nom_okved_f_quarterly VALUES (?,?,?,?)",
                        (reg, snap, 'G53_okved_F', v))
            n += 1; snaps.add(snap)
        except (ValueError, IndexError):
            pass
con.commit()
print('залито', n, 'снимков', len(snaps))
b = pd.read_sql("""SELECT snapshot_date, value FROM fns_1nom_okved_f_quarterly
                   WHERE region='Республика Башкортостан' ORDER BY snapshot_date""", con)
print('Башкортостан, начислено по ОКВЭД F (тыс. руб., нарастающим итогом):')
print(b.to_string(index=False))