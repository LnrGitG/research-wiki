#!/usr/bin/env python3
"""MVP step 1: collect Wordstat weekly series for housing demand semantic core.
3 intent groups (investment/rental/panic) + broad denominators for RII.
One API call per phrase covers 2018->now (verified client wordstat_api.py).
Output: data/wordstat_weekly_core.csv (long format: date,phrase,group,count,share)
"""
import sys, time, csv
sys.path.insert(0, '/home/lnr/research-wiki/scripts')
import os
os.chdir('/home/lnr/research-wiki')
from wordstat_api import dynamics

PHRASES = [
    # group A: investment / primary market demand
    ("купить квартиру в новостройке", "A_invest"),
    ("новостройки от застройщика",    "A_invest"),
    ("льготная ипотека",              "A_invest"),
    ("семейная ипотека",              "A_invest"),
    ("дду",                           "A_invest"),
    # group B: consumer rental demand
    ("снять квартиру",                "B_rent"),
    ("аренда квартир",                "B_rent"),
    ("снять квартиру на длительный срок", "B_rent"),
    ("аренда без посредников",        "B_rent"),
    # group C: panic / protective demand
    ("куда вложить деньги",           "C_panic"),
    ("вложение в недвижимость",       "C_panic"),
    ("продать квартиру и купить",     "C_panic"),
    # broad denominators for RII
    ("недвижимость",                  "D_broad"),
    ("ипотека",                       "D_broad"),
    ("купить квартиру",               "D_broad"),
    ("вторичное жильё",               "D_broad"),
]

rows = []
for i, (ph, grp) in enumerate(PHRASES, 1):
    try:
        res = dynamics(ph, 'PERIOD_WEEKLY', '2018-01-01', '2026-08-30')
        print(f"[{i}/{len(PHRASES)}] {ph!r}: {len(res)} pts {res[0]['date']}->{res[-1]['date']}", flush=True)
        for r in res:
            rows.append({"date": r["date"], "phrase": ph, "group": grp,
                         "count": r["count"], "share": r["share"]})
    except Exception as e:
        print(f"[{i}/{len(PHRASES)}] {ph!r}: FAILED {e}", flush=True)
    time.sleep(2)

with open('data/wordstat_weekly_core.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=["date","phrase","group","count","share"])
    w.writeheader()
    w.writerows(rows)
print(f"DONE: {len(rows)} rows -> data/wordstat_weekly_core.csv")
