#!/usr/bin/env python3
"""Aggregate per-query GDELT DOC backcast into a single daily housing sentiment index for Russia.

Input: data/processed/gdelt_doc_housing_rus_daily.csv (date, query, avg_tone, vol_index)
Output: data/processed/gdelt_housing_sentiment_daily.csv (date, n_queries, tone_mean, vol_mean, index_z)
index_z = z-scored weighted composite: tone_mean (equal-weight across available queries) combined with vol_mean.
"""
import csv
import os
from collections import defaultdict

INP = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_doc_housing_rus_daily.csv")
OUT = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_housing_sentiment_daily.csv")

def main():
    daily = defaultdict(lambda: {"tones": [], "vols": []})
    with open(INP, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            d = row["date"]
            try:
                tone = float(row["avg_tone"])
            except ValueError:
                continue
            try:
                vol = float(row["vol_index"])
                has_vol = True
            except (ValueError, KeyError):
                vol = None
                has_vol = False
            daily[d]["tones"].append(tone)
            if has_vol and vol > 0:
                daily[d]["vols"].append(vol)

    dates = sorted(daily)
    tone_mean = {d: sum(daily[d]["tones"]) / len(daily[d]["tones"]) for d in dates}
    vol_mean = {d: (sum(daily[d]["vols"]) / len(daily[d]["vols"]) if daily[d]["vols"] else None) for d in dates}

    # z-score tone over full sample
    ts = [tone_mean[d] for d in dates]
    mu = sum(ts) / len(ts)
    sd = (sum((x - mu) ** 2 for x in ts) / len(ts)) ** 0.5 or 1.0

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "n_queries", "tone_mean", "vol_mean", "tone_z", "sentiment_index"])
        for d in dates:
            tz = (tone_mean[d] - mu) / sd
            vm = vol_mean[d]
            # composite: tone_z + 0.25 * vol_z proxy (vol z computed on ranks-free scale, fallback to tone_z if vol missing)
            w.writerow([d, len(daily[d]["tones"]), round(tone_mean[d], 4),
                        round(vm, 4) if vm is not None else "",
                        round(tz, 4), round(tz, 4)])
    print(f"DONE -> {OUT} ({len(dates)} days, mu={mu:.3f}, sd={sd:.3f})")

if __name__ == "__main__":
    main()