#!/usr/bin/env python3
"""Wordstat construction-volume nowcasting collection: 21 phrases, 5 semantic groups.
Weekly 2018-01..now. Mirrors wordstat_core_collect.py pattern (MIDAS housing demand core).
Output: data/wordstat_weekly_construction.csv (date, phrase, group, count, share)
"""
import sys, os, csv, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import require_repo
os.chdir(require_repo())
from wordstat_api import dynamics


PHRASES = [
    # S1. Individual housing construction (household activity, leading IHS)
    ("строительство домов под ключ", "S1_ihb"),
    ("проектирование дома", "S1_ihb"),
    ("смета на строительство", "S1_ihb"),
    # S2. Materials demand (site-activity proxy)
    ("доставка бетона", "S2_mat"),
    ("бетон с доставкой цена", "S2_mat"),
    ("блоки бетонные купить", "S2_mat"),
    ("аренда бетононасоса", "S2_mat"),
    # S3. Machinery rental (B2B active construction sites)
    ("аренда спецтехники", "S3_mach"),
    ("экскаватор аренда", "S3_mach"),
    ("аренда крана", "S3_mach"),
    ("аренда гусеничного экскаватора", "S3_mach"),
    ("аренда экскаватора погрузчика", "S3_mach"),
    # S4. B2B contracting & procurement
    ("строительная компания", "S4_b2b"),
    ("строительная фирма", "S4_b2b"),
    ("строительный подрядчик", "S4_b2b"),
    ("подряд на строительство", "S4_procure"),
    ("тендер на строительство", "S4_procure"),
    # S5. Regulation
    ("разрешение на строительство", "S5_permits"),
    # D. broad denominators
    ("стройка", "D_broad"),
    ("строительство", "D_broad"),
]

GROUPS = dict(PHRASES)

# Конец диапазона считаем сами: у недельной гранулярности toDate обязан быть воскресеньем,
# иначе API отвечает HTTP 400. Захардкоженная дата здесь уже один раз стоила трёх недель данных.
import datetime as _dt

_today = _dt.date.today()
_last_sunday = _today - _dt.timedelta(days=(_today.weekday() + 1) % 7)
TO_DATE = _last_sunday.isoformat()
print(f'диапазон: 2018-01-01 .. {TO_DATE} (последнее воскресенье)', flush=True)

rows = []
for i, (ph, grp) in enumerate(PHRASES, 1):
    try:
        res = dynamics(ph, 'PERIOD_WEEKLY', '2018-01-01', TO_DATE)
        print(f"[{i}/{len(PHRASES)}] {ph!r}: {len(res)} pts", flush=True)
        for r in res:
            rows.append({"date": r["date"], "phrase": ph, "group": grp,
                         "count": int(r["count"]), "share": float(r["share"])})
    except Exception as e:
        print(f"[{i}] {ph!r}: FAILED {str(e)[:70]}", flush=True)
    time.sleep(2)

with open('data/wordstat_weekly_construction.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=["date", "phrase", "group", "count", "share"])
    w.writeheader()
    w.writerows(rows)
print("saved:", len(rows), "-> data/wordstat_weekly_construction.csv")