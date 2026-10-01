#!/usr/bin/env python3
"""H-001: композит Wordstat S2-S5 vs yoy ИФО СМР на лаге -1 месяц (перекат).

Методика (воспроизводит prior r=+0.644, n=18, окно comp 2025-01..2026-06):
  * композит недели = сумма share фраз групп S2_mat+S3_mach+S4_b2b+S4_procure+S5_permits
  * месячная агрегация = mean недельной суммы share по неделям месяца (метка — понедельник)
  * цель = yoy ИФО СМР (индекс, 100 = прошлый год), месячный ряд
  * лаг lead-k: comp_t vs smr_{t+k}   (lead-1 = композит опережает на 1 месяц)

Ряд ИФО СМР читается из PostgreSQL на ВМ (staging.rosstat_construction__construction_volume_monthly_rf)
через scripts/db_tunnel.py. Август 2026 (+2,7% г/г) задан константой: КЭП «январь-август»
на дату расчёта (01.10.2026) ещё не опубликован, значение взято из доклада osn-08-2026.
"""
import csv, sys, statistics, os
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as dbt

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(REPO, "data", "wordstat_weekly_construction.csv")
S25 = {"S2_mat", "S3_mach", "S4_b2b", "S4_procure", "S5_permits"}
SMR_AUG_2026 = 102.7   # доклад Росстата osn-08-2026; заменить на КЭП после релиза


def load_composite_monthly(path):
    byweek = defaultdict(lambda: defaultdict(float))
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            byweek[r["date"].strip()][r["group"].strip()] += float(r["share"])
    bm = defaultdict(list)
    for d, g in byweek.items():
        bm[d[:7]].append(sum(g.get(k, 0.0) for k in S25))
    return {k: statistics.fmean(v) for k, v in bm.items()}, max(byweek)


def load_smr():
    smr = {}
    for y, m, yoy in dbt.query(
            "SELECT report_year, report_month, yoy_pct "
            "FROM staging.rosstat_construction__construction_volume_monthly_rf "
            "WHERE report_month IS NOT NULL"):
        smr[f"{y:04d}-{m:02d}"] = float(yoy)
    smr["2026-08"] = SMR_AUG_2026
    return smr


def pearson(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = (sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys)) ** 0.5
    return num / den if den else float("nan")


def lead1_pairs(comp_m, smr, lo, hi):
    xs, ys = [], []
    for ym in sorted(comp_m):
        if not (lo <= ym <= hi):
            continue
        y, m = int(ym[:4]), int(ym[5:7]); m2, y2 = m + 1, y
        if m2 == 13:
            m2, y2 = 1, y + 1
        key = f"{y2:04d}-{m2:02d}"
        if key in smr:
            xs.append(comp_m[ym]); ys.append(smr[key])
    return xs, ys


def main():
    comp_m, last_week = load_composite_monthly(CSV)
    smr = load_smr()
    print(f"недель всего: {len(set(comp_m))} месяцев, последняя неделя {last_week}")

    print("\n-- профиль лагов (полное пересечение) --")
    months = sorted(set(comp_m) & set(smr))
    for k in (-2, -1, 0, 1, 2):
        xs, ys = [], []
        for i, t in enumerate(months):
            j = i + k
            if 0 <= j < len(months):
                xs.append(comp_m[t]); ys.append(smr[months[j]])
        if len(xs) >= 6:
            print(f"  lead k={k:+d}: r={pearson(xs, ys):+.4f}  n={len(xs)}")

    xs, ys = lead1_pairs(comp_m, smr, "2025-01", "2026-07")
    print(f"\nИТОГ lead-1: r={pearson(xs, ys):+.4f}  n={len(xs)}")
    for name, lo, hi in [("2025", "2025-01", "2025-12"),
                         ("2026H1", "2026-01", "2026-06"),
                         ("2026", "2026-01", "2026-07")]:
        a, b = lead1_pairs(comp_m, smr, lo, hi)
        if len(a) >= 4:
            print(f"  подпериод {name}: r={pearson(a, b):+.3f} n={len(a)}")


if __name__ == "__main__":
    main()