# -*- coding: utf-8 -*-
"""Построение 66 авторитетных ступеней из дневного ряда hd_base.

Ряд дневной: изменения = дни вступления ступеней в силу. Сохраняет
/tmp/keyrate_ladder.txt: effective_from;effective_to;value
"""
import datetime

series = []
with open("/tmp/keyrate_series.txt", encoding="utf-8") as f:
    for line in f:
        d, v = line.strip().split(";")
        dd = datetime.datetime.strptime(d, "%d.%m.%Y").date()
        series.append((dd, float(v.replace(",", "."))))
series.sort()

# Ступени: [effective_from, effective_to] по дням смены значения
changes = []  # (eff_date, prev_value, new_value)
for i in range(1, len(series)):
    if series[i][1] != series[i - 1][1]:
        changes.append((series[i][0], series[i - 1][1], series[i][1]))

ladder = []
start_date = series[0][0]
start_val = series[0][1]
for eff, prev_v, new_v in changes:
    ladder.append((start_date, (eff - datetime.timedelta(days=1)), start_val))
    start_date = eff
    start_val = new_v
ladder.append((start_date, None, start_val))

with open("/tmp/keyrate_ladder.txt", "w", encoding="utf-8") as f:
    for frm, to, val in ladder:
        f.write(f"{frm.isoformat()};{to.isoformat() if to else ''};{val}\n")

print("ступеней:", len(ladder))
print("первые 3:", ladder[:3])
print("последние 3:", ladder[-3:])