#!/usr/bin/env python3
"""Wordstat S6-B2B investment-specific phrases: for IKV (investment) nowcasting.
6 phrases × weekly 2018-01..now. Complements wordstat_construction_collect.py (S1-S5).
Output: data/wordstat_weekly_b2b_invest.csv (date, phrase, group, count, share)
Rate limit: 100 req/hour → 6 phrases fits easily.
"""
import sys, os, csv, time
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.chdir('/home/lnr/research-wiki')
from wordstat_api import dynamics
from pathlib import Path


PHRASES = [
    # S6a. Machinery purchase (capex signal — покупка, не аренда)
    ("экскаватор купить", "S6a_mach_buy"),
    ("купить бульдозер", "S6a_mach_buy"),
    ("купить бетононасос", "S6a_mach_buy"),
    # S6b. Tenders & procurement (гос/корп инвестиционный цикл)
    ("тендер строительство", "S6b_tender"),
    ("спецтехника купить", "S6a_mach_buy"),
    ("тендеры на строительство", "S6b_tender"),
]

rows = []
for i, (ph, grp) in enumerate(PHRASES, 1):
    try:
        res = dynamics(ph, 'PERIOD_WEEKLY', '2018-01-01', '2026-09-06')  # date_to must be Sunday
        print(f"[{i}/{len(PHRASES)}] {ph!r}: {len(res)} pts", flush=True)
        for r in res:
            rows.append({"date": r["date"], "phrase": ph, "group": grp,
                         "count": int(r["count"]), "share": float(r["share"])})
    except Exception as e:
        print(f"[{i}] {ph!r}: FAILED {str(e)[:70]}", flush=True)
    time.sleep(3)

with open('data/wordstat_weekly_b2b_invest.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=["date", "phrase", "group", "count", "share"])
    w.writeheader()
    w.writerows(rows)
print("saved:", len(rows), "-> data/wordstat_weekly_b2b_invest.csv")