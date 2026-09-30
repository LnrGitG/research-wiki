#!/usr/bin/env python3
"""Ежедневный сентимент/тональность экономики России из GDELT DOC (без стройки).

Вход: data/processed/gdelt_doc_economy_rus_daily.csv (date, query, avg_tone, vol_index)
Выход: data/processed/gdelt_doc_economy_index_daily.csv
       (date YYYYMMDD, n_queries, tone_mean, vol_mean, tone_z, sentiment_index)

Агрегация: tone_mean — средний тон по доступным запросам дня;
vol_mean — средний объём новостного потока (нормированный к 0..1);
tone_z — z-скор по всему ряду; sentiment_index — пока = tone_z
(у жилищной версии та же схема, композит с vol оставлен на этап калибровки).
"""
import csv
import os
from collections import defaultdict
from statistics import mean, pstdev

INP = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_doc_economy_rus_daily.csv")
OUT = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_doc_economy_index_daily.csv")


def main():
    daily = defaultdict(lambda: {"tones": [], "vols": []})
    with open(INP, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                tone = float(row["avg_tone"])
            except (ValueError, KeyError):
                continue
            daily[row["date"]]["tones"].append(tone)
            try:
                vol = float(row["vol_index"])
                if vol > 0:
                    daily[row["date"]]["vols"].append(vol)
            except (ValueError, KeyError):
                pass

    dates = sorted(daily)
    if not dates:
        print("Вход пуст")
        return 1
    tone_mean = {d: mean(daily[d]["tones"]) for d in dates}
    vol_mean = {d: (mean(daily[d]["vols"]) if daily[d]["vols"] else None) for d in dates}

    ts = [tone_mean[d] for d in dates]
    mu = mean(ts)
    sd = pstdev(ts) or 1.0

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "n_queries", "tone_mean", "vol_mean", "tone_z", "sentiment_index"])
        for d in dates:
            tz = (tone_mean[d] - mu) / sd
            vm = vol_mean[d]
            w.writerow([d, len(daily[d]["tones"]), round(tone_mean[d], 4),
                        round(vm, 4) if vm is not None else "",
                        round(tz, 4), round(tz, 4)])
    print(f"DONE -> {OUT} ({len(dates)} дней, mu={mu:.3f}, sd={sd:.3f})")
    return 0


if __name__ == "__main__":
    exit(main())