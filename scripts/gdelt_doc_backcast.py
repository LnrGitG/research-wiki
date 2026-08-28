#!/usr/bin/env python3
"""GDELT DOC 2.0 API backcast: daily tone + volume for Russia housing/mortgage keywords.

No BigQuery, no API key. Rate limit: >=5s between requests (we use 7s).
Output: research-wiki/data/processed/gdelt_doc_housing_rus_daily.csv
Columns: date, query, avg_tone, vol_index
"""
import csv
import json
import os
import subprocess
import time
from datetime import datetime, timezone

BASE = "https://api.gdeltproject.org/api/v2/doc/doc"
OUT = os.path.join(os.path.dirname(__file__), "../data/processed/gdelt_doc_housing_rus_daily.csv")

QUERIES = [
    'mortgage Russia',
    '"real estate" Russia',
    'housing Russia',
    'mortgage sourcecountry:RS',
]
# year chunks: 2017-01 .. present (GDELT V2 DOC coverage starts 2017-01-01)
START_YEAR = 2017

def fetch(url, retries=4):
    for a in range(retries):
        r = subprocess.run(
            ["curl", "-s", "--max-time", "90", url],
            capture_output=True, text=True, timeout=120,
        )
        body = r.stdout.strip()
        if body.startswith("{") and '"timeline"' in body:
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                pass
        time.sleep(10 * (a + 1))  # backoff: API is flaky, 5s/req limit
    return None

def get_series(query, mode, start, end):
    from urllib.parse import quote
    url = (f"{BASE}?query={quote(query)}&mode={mode}&format=json"
           f"&startdatetime={start}&enddatetime={end}")
    d = fetch(url)
    if not d:
        return {}
    tl = d.get("timeline", [])
    out = {}
    for series in tl:
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
            time.sleep(7)
            vol = get_series(query, "timelinevol", start, end)
            time.sleep(7)
            n = 0
            for day, t in tone.items():
                key = (day, query)
                rows.setdefault(key, {"date": day, "query": query, "avg_tone": t, "vol_index": vol.get(day, "")})
                n += 1
            print(f"[{query}] {year}: {n} days (vol days: {len(vol)})", flush=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "query", "avg_tone", "vol_index"])
        w.writeheader()
        for key in sorted(rows):
            w.writerow(rows[key])
    print(f"DONE -> {OUT} ({len(rows)} rows)", flush=True)

if __name__ == "__main__":
    main()