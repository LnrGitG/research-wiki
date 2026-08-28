#!/usr/bin/env python3
"""Add GDELT housing sentiment series to docs/data-summary.json for the mobile dashboard.

Sources (research-wiki/data/processed/):
- gdelt_housing_sentiment_weekly.csv  (week_end, n_days, tone_mean, tone_z_mean, vol_mean)
- gdelt_housing_sentiment_daily.csv   (date YYYYMMDD, n_queries, tone_mean, vol_mean, tone_z, sentiment_index)

Adds keys:
- gdelt_sentiment_weekly: [{week:'YYYY-MM-DD', tone_z, tone, vol}]
- gdelt_sentiment_monthly: [{month:'YYYY-MM', tone_z, tone, vol}] (mean of weeks)
"""
import csv
import json
import os
from collections import defaultdict

WEEKLY = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_housing_sentiment_weekly.csv")
DAILY = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_housing_sentiment_daily.csv")
OUT = os.path.join(os.path.dirname(__file__), "../docs/data-summary.json")


def main():
    weekly = []
    with open(WEEKLY, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            weekly.append({
                "week": r["week_end"],
                "tone": round(float(r["tone_mean"]), 3),
                "tone_z": round(float(r["tone_z_mean"]), 3),
                "vol": round(float(r["vol_mean"]), 4) if r["vol_mean"] else None,
            })

    # monthly aggregation from weekly (mean over weeks whose week_end falls in month)
    acc = defaultdict(lambda: {"z": [], "tone": [], "vol": []})
    for w in weekly:
        m = w["week"][:7]
        acc[m]["z"].append(w["tone_z"])
        acc[m]["tone"].append(w["tone"])
        if w["vol"] is not None:
            acc[m]["vol"].append(w["vol"])
    monthly = []
    for m in sorted(acc):
        a = acc[m]
        monthly.append({
            "month": m,
            "tone": round(sum(a["tone"]) / len(a["tone"]), 3),
            "tone_z": round(sum(a["z"]) / len(a["z"]), 3),
            "vol": round(sum(a["vol"]) / len(a["vol"]), 4) if a["vol"] else None,
        })

    with open(OUT, encoding="utf-8") as f:
        doc = json.load(f)
    doc["gdelt_sentiment_weekly"] = weekly
    doc["gdelt_sentiment_monthly"] = monthly
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, separators=(",", ":"))
    print(f"OK: {len(weekly)} weeks, {len(monthly)} months -> {OUT} ({os.path.getsize(OUT)/1024:.0f} KB)")


if __name__ == "__main__":
    main()