#!/usr/bin/env python3
"""GDELT DOC 2.0 API: общеэкономическая тональность для России (без привязки к стройке).

Аналог scripts/gdelt_doc_backcast.py, но запросы — экономика в целом:
  economy Russia
  economy sourcecountry:RS
  "economic growth" Russia
Режимы: timelinetone (средний тон дня) + timelinevol (объём новостного потока).

Лимит API: 1 запрос / 5 с — держим паузу 10 с между запросами и бэкофф
15/30/45 с на rate-limit. Без ключа, без BigQuery.

Выход: data/processed/gdelt_doc_economy_rus_daily.csv
Колонки: date, query, avg_tone, vol_index. Период: 2017-01-01 → сегодня.
Повторный запуск перезаписывает файл целиком (полная перекачка).
"""
import csv
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from urllib.parse import quote

BASE = "https://api.gdeltproject.org/api/v2/doc/doc"
OUT = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_doc_economy_rus_daily.csv")

QUERIES = [
    'economy Russia',
    'economy sourcecountry:RS',
    '"economic growth" Russia',
]
START_YEAR = 2017


def fetch(url, retries=4):
    for a in range(retries):
        r = subprocess.run(["curl", "-s", "--max-time", "120", url],
                           capture_output=True, text=True, timeout=150)
        body = r.stdout.strip()
        if body.startswith("Please limit requests"):
            wait = 15 * (a + 1)
            print(f"  rate-limit, ждём {wait}s", flush=True)
            time.sleep(wait)
            continue
        if body.startswith("{") and '"timeline"' in body:
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                pass
        time.sleep(10 * (a + 1))
    return None


def get_series(query, mode, start, end):
    url = (f"{BASE}?query={quote(query)}&mode={mode}&format=json"
           f"&startdatetime={start}&enddatetime={end}")
    d = fetch(url)
    if not d:
        return {}
    out = {}
    for series in d.get("timeline", []):
        for p in series.get("data", []):
            out[p["date"][:8]] = p.get("value", 0.0)
    return out


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    rows = {}
    now = datetime.now(timezone.utc)
    for query in QUERIES:
        for year in range(START_YEAR, now.year + 1):
            start = f"{year}0101000000"
            end = f"{year}1231235959" if year < now.year else now.strftime("%Y%m%d%H%M%S")
            tone = get_series(query, "timelinetone", start, end)
            time.sleep(10)
            vol = get_series(query, "timelinevol", start, end)
            time.sleep(10)
            n = 0
            for day, t in tone.items():
                key = (day, query)
                rows.setdefault(key, {"date": day, "query": query,
                                      "avg_tone": t, "vol_index": vol.get(day, "")})
                n += 1
            print(f"[{query}] {year}: {n} дней (vol: {len(vol)})", flush=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "query", "avg_tone", "vol_index"])
        w.writeheader()
        for key in sorted(rows):
            w.writerow(rows[key])
    print(f"DONE -> {OUT} ({len(rows)} строк)", flush=True)


if __name__ == "__main__":
    main()