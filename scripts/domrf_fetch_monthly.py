#!/usr/bin/env python3
"""ДОМ.РФ priceindex/living — скачивание и запись сырья (CSV).

Шаг «скачать», без записи в БД: результат кладётся в
raw/domrf/price_index/domrf_priceindex_all_regions.csv, откуда его забирает
прямой загрузчик scripts/direct_domrf.py («сырьё → канон»). Прежняя версия
этого скрипта писала ещё и SQLite-лендинг domrf_price_index — звено снято
16.10.2026 вместе с остальными лендингами: после переезда канона в
PostgreSQL лендинг лишь удваивал точки отказа.

API: POST /api/v2/priceindex/living/mainchart/ — ряды по регионам
(index_value, index_diff_month, index_count_deal) с 2021-01.
"""
import csv
import json
import os
import shutil
import ssl
import time
import urllib.request

HOST = "https://" + "xn--d1aqf" + ".xn--p1ai"  # дом.рф (punycode)
BASE = HOST + "/api/v2/priceindex/living/"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

CSV_PATH = ("/home/lnr/research-wiki-private/raw/domrf/price_index/"
            "domrf_priceindex_all_regions.csv")


def req(url, body=None, retries=3):
    data = json.dumps(body).encode() if body is not None else None
    hdr = {"Content-Type": "application/json"} if data else {}
    last = None
    for i in range(retries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, data=data, headers=hdr),
                                       timeout=60, context=CTX)
            return json.load(r)
        except Exception as e:                       # сеть/гео/лимит — пауза и повтор
            last = e
            print("retry", i, e)
            time.sleep(3)
    raise RuntimeError("request failed: %s (%s)" % (url, last))


def csv_max_month():
    """Последний месяц в уже выгруженном CSV — чтобы не ходить в API зря."""
    if not os.path.exists(CSV_PATH):
        return ""
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        months = [(row.get('month') or '')[:10] for row in csv.DictReader(f)]
    return max(months) if months else ""


def main():
    full = req(BASE + "changesfull/")
    json.dump(full, open("/tmp/changesfull.json", "w"))
    dates = full["data"]["filter"]["dates"]
    items = full["data"].get("items", [])
    max_date = max(dates)                     # "2026-08-01"
    print("api max date:", max_date, "| n_items:", len(items))

    have = csv_max_month()
    print("csv max:", have or "(нет файла)")
    if have and max_date <= have:
        print("NO UPDATES")
        return

    y, m, _ = max_date.split("-")
    regions = [{"region": it["region"], "estateClass": "Все классы",
                "rooms": "Комнат", "id": i} for i, it in enumerate(items)]
    body = {"regions": regions, "date_from": "2021.01.01",
            "date_to": "%s.%s.01" % (y, m), "haveRF": True, "type": "def"}
    chart = req(BASE + "mainchart/", body)
    json.dump(chart, open("/tmp/mainchart.json", "w"))

    rows = {}
    for key, series in chart["data"]["regions"].items():
        for it in series.get("items", []):
            mon = (it.get("month_dt") or "")[:10]
            if not mon:
                continue
            rows[(it["region"], mon)] = (it.get("index_value"),
                                         it.get("index_diff_month"),
                                         it.get("index_count_deal"))
    print("fetched rows:", len(rows))
    if not rows:
        raise SystemExit("API отдал пустой ответ — CSV не перезаписываем")

    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    if os.path.exists(CSV_PATH):
        shutil.copy(CSV_PATH, CSV_PATH + ".bak")
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["region", "month", "index_value", "mom_pct", "n_deals"])
        for (r, mo), (val, mom, nd) in sorted(rows.items()):
            w.writerow([r, mo, val, mom, nd])
    print("csv written:", CSV_PATH, os.path.getsize(CSV_PATH))
    print("max month в CSV:", max(rows)[1] if rows else "-")


if __name__ == "__main__":
    main()
