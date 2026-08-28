#!/usr/bin/env python3
"""Aggregate daily GDELT housing sentiment index to weekly (Sunday-ending, Wordstat-aligned).

Input: data/processed/gdelt_housing_sentiment_daily.csv (date YYYYMMDD, n_queries, tone_mean, vol_mean, tone_z, sentiment_index)
Output: data/processed/gdelt_housing_sentiment_weekly.csv
Columns: week_end (Sunday, YYYY-MM-DD), n_days, tone_mean, tone_z_mean, vol_mean
Rows with missing days are averaged over available days; weeks need >=3 days to be kept.
"""
import csv
import os
from collections import defaultdict
from datetime import datetime, timedelta

INP = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_housing_sentiment_daily.csv")
OUT = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_housing_sentiment_weekly.csv")

def week_end(d):
    """Sunday ending the week containing date d (Wordstat convention: week ends Sunday)."""
    # Python: Monday=0 .. Sunday=6; days until next Sunday
    offset = (6 - d.weekday()) % 7
    return d + timedelta(days=offset)

def main():
    weeks = defaultdict(lambda: {"tone": [], "tonez": [], "vol": []})
    with open(INP, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            d = datetime.strptime(row["date"], "%Y%m%d")
            we = week_end(d)
            weeks[we]["tone"].append(float(row["tone_mean"]))
            weeks[we]["tonez"].append(float(row["sentiment_index"]))
            if row["vol_mean"]:
                weeks[we]["vol"].append(float(row["vol_mean"]))

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["week_end", "n_days", "tone_mean", "tone_z_mean", "vol_mean"])
        n = 0
        for we in sorted(weeks):
            b = weeks[we]
            if len(b["tone"]) < 3:  # skip partial weeks at boundaries
                continue
            w.writerow([
                we.strftime("%Y-%m-%d"), len(b["tone"]),
                round(sum(b["tone"]) / len(b["tone"]), 4),
                round(sum(b["tonez"]) / len(b["tonez"]), 4),
                round(sum(b["vol"]) / len(b["vol"]), 4) if b["vol"] else "",
            ])
            n += 1
    print(f"DONE -> {OUT} ({n} weeks)")

if __name__ == "__main__":
    main()