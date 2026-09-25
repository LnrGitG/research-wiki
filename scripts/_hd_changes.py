# -*- coding: utf-8 -*-
"""Извлечение фактических дат вступления ступеней из дневного ряда hd_base.

Ряд дневной: изменения ряда = дни вступления в силу. Сопоставляем с
лестницей dkp.rate_level и цепочкой решений dkp.decision.
"""
import datetime
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")

# Дневной ряд: дата;значение
series = []
with open("/tmp/keyrate_series.txt", encoding="utf-8") as f:
    for line in f:
        d, v = line.strip().split(";")
        dd = datetime.datetime.strptime(d, "%d.%m.%Y").date()
        series.append((dd, float(v.replace(",", "."))))
series.sort()

print("== Фактические дни вступления (изменение ряда):")
changes = []
for i in range(1, len(series)):
    if series[i][1] != series[i - 1][1]:
        changes.append((series[i][0], series[i - 1][1], series[i][1]))
        print(f"  {series[i][0]}: {series[i-1][1]} → {series[i][1]}")

print("\n== Лестница dkp.rate_level за тот же период:")
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query
for frm, to, val, lid, did in query("""
        SELECT effective_from, effective_to, value, level_id, decision_id
        FROM dkp.rate_level WHERE rate_code='key_rate'
        AND effective_from >= '2025-12-01' ORDER BY effective_from"""):
    print(f"  level {lid} (decision {did}): {val} с {frm} по {to}")

print("\n== Записанные решения за тот же период:")
for mid, md, prev, new, delta, action in query("""
        SELECT m.meeting_id, m.meeting_date::text, d.rate_prev, d.rate_new, d.delta_bp, d.action
        FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
        WHERE m.meeting_date >= '2025-12-01' ORDER BY m.meeting_date"""):
    print(f"  {md} (mid {mid}): prev={prev} new={new} {action}")