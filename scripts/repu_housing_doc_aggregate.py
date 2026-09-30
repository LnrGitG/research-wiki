#!/usr/bin/env python3
"""Финальная агрегация REPU-РФ v2 (метод Chen-Mo-Tang-Li) из дневного файла.

Вход: data/processed/repu_housing_doc_daily.csv (собран
scripts/repu_housing_doc_full.py; 2019-2026, 2800 дней; по году объём и тон
могут идти с разных таймингов API — берём пересечение месяцев).
Выход: data/processed/repu_housing_doc_monthly.csv — month, mean_volume,
mean_tone, repu_index (z по тон-среднему всех полных месяцев).

Контрольные события закрытия/анонса массовой льготной ипотеки (2024) —
проверка валидации по методу Chen (индекс должен расти при крупных
регуляторных событиях).
"""
import csv
import os
from collections import defaultdict
from statistics import mean, pstdev

INP = os.path.join(os.path.dirname(__file__), "../data/processed/repu_housing_doc_daily.csv")
OUT = os.path.join(os.path.dirname(__file__), "../data/processed/repu_housing_doc_monthly.csv")

CONTROL = {
    "2020-04": "запуск льготной ипотеки 6,5% (данных нет до 2019)",
    "2020-11": "продление на 2021 (недоступен тон)",
    "2022-03": "расширение семейной (недоступен тон)",
    "2023-01": "правки, анонс закрытия 01.07.2023",
    "2024-06": "анонс закрытия массовой",
    "2024-07": "закрытие массовой льготной",
}


def main():
    months = defaultdict(lambda: {"v": [], "t": []})
    with open(INP, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            m = row["date"][:6]
            try:
                months[m]["v"].append(float(row["volume"]))
            except (ValueError, TypeError):
                pass
            try:
                months[m]["t"].append(float(row["tone"]))
            except (ValueError, TypeError):
                pass

    both = sorted(m for m in months if months[m]["v"] and months[m]["t"])
    tm = {m: mean(months[m]["t"]) for m in both}
    mu, sd = mean(tm.values()), (pstdev(list(tm.values())) or 1.0)

    rows = []
    for m in sorted(months):
        v = mean(months[m]["v"]) if months[m]["v"] else None
        t = mean(months[m]["t"]) if months[m]["t"] else None
        rz = (t - mu) / sd if t is not None else None
        rows.append([m, round(v, 6) if v is not None else "",
                     round(t, 4) if t is not None else "",
                     round(rz, 3) if rz is not None else ""])
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["month", "mean_volume", "mean_tone", "repu_index"])
        w.writerows(rows)
    print(f"DONE -> {OUT} ({len(rows)} месяцев, {len(both)} с полным индексом)")

    print("\n== Контрольные события:")
    for ym, label in CONTROL.items():
        key = ym.replace("-", "")
        if key in tm:
            v = (tm[key] - mu) / sd
            flag = " <<<" if v > 0.5 else ""
            print(f"   {ym}: {v:+.2f}{flag} {label}")
        else:
            print(f"   {ym}: н/д {label}")

    print("\n== Топ-5 месяцев по repu_index:")
    tops = sorted(tm, key=lambda m: (tm[m] - mu) / sd, reverse=True)[:5]
    for m in tops:
        d = f"{m[:4]}-{m[4:]}"
        print(f"   {d}: {(tm[m]-mu)/sd:+.2f}")


if __name__ == "__main__":
    main()