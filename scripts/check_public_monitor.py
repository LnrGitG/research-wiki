#!/usr/bin/env python3
"""Проверка контракта публичной витрины: страница читает ровно то, что есть в JSON.

Смысл: браузер на VPS недоступен, поэтому вместо скриншота проверяем
(1) наличие всех полей, которые использует JS, и (2) воспроизводим расчёт KPI
и рядов той же логикой, что в docs/public-monitor.html.
Запуск: python3 scripts/check_public_monitor.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(ROOT, "docs", "public-monitor.json")

KPI = ["orvdssmpg", "vzszopmrvzs", "cbr_izhk_rate_m", "cbr_izhk_volume_m",
       "cbr_izhk_debt_m", "rkop_3"]


def year_ago(pts, period):
    target = f"{int(period[:4]) - 1}{period[4:]}"
    found = None
    for p in pts:
        if p[0] <= target:
            found = p
        else:
            break
    return found


def main() -> int:
    with open(JSON_PATH, encoding="utf-8") as f:
        D = json.load(f)

    errors = []
    for key in ("generated_at", "source", "metrics", "regions", "series"):
        if key not in D:
            errors.append(f"нет ключа {key}")
    if errors:
        print("ОШИБКИ:", *errors, sep="\n  ")
        return 1

    codes = [m["code"] for m in D["metrics"]]
    for m in D["metrics"]:
        for field in ("code", "title", "unit", "freq", "note", "regions", "last_rf"):
            if field not in m:
                errors.append(f"{m['code']}: нет поля {field}")
    for code in codes:
        s = D["series"].get(code)
        if not s:
            errors.append(f"{code}: нет ряда")
            continue
        if "by_region" not in s or "rf" not in s:
            errors.append(f"{code}: нет by_region/rf")

    region_codes = {r["code"] for r in D["regions"]}
    if len(region_codes) < 80:
        errors.append(f"регионов мало: {len(region_codes)}")

    print(f"срез {D['generated_at']}; метрик {len(codes)}; регионов {len(region_codes)}")

    # Воспроизводим поведение страницы для региона по умолчанию
    default = next((r["code"] for r in D["regions"] if "Башкортостан" in r["name"]), None)
    print(f"регион по умолчанию: {default}")
    for code in KPI:
        s = D["series"][code]
        reg = s["by_region"].get(default, [])
        pts = reg if reg else s["rf"]
        if not pts:
            errors.append(f"{code}: пустой ряд для {default} и для РФ")
            continue
        last = pts[-1]
        prev = year_ago(pts, last[0])
        delta = None
        if prev and prev[1]:
            delta = last[1] - prev[1] if code in ("orvdssmpg", "cbr_izhk_rate_m") else (last[1] / prev[1] - 1) * 100
        print(f"  {code:<20} последняя {last[0]} = {last[1]:>14,.2f} "
              f"({'регион' if reg else 'РФ'})" + (f", Δ {delta:+.2f}" if delta is not None else ""))

    # Ряды в диапазоне ползунка: не меньше 2 точек, иначе график пустой
    thin = [c for c in codes if len(D["series"][c]["rf"]) < 2]
    if thin:
        errors.append(f"ряды из одной точки: {thin}")

    if errors:
        print("\nОШИБКИ:", *errors, sep="\n  ")
        return 1
    print("\nКонтракт в порядке: все поля на месте, KPI и ряды считаются.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
