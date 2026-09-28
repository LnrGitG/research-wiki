#!/usr/bin/env python3

import json, csv, os, sys, time, subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / 'raw' / 'gdp'
RAW_DIR.mkdir(parents=True, exist_ok=True)

def curl_fetch(url, retries=3, backoff=2):
    for attempt in range(1, retries+1):
        try:
            result = subprocess.run(['curl', '-fsSL', url], capture_output=True, text=True, timeout=20)
            if result.returncode == 0:
                return result.stdout
            else:
                raise RuntimeError(f"curl error {result.returncode}: {result.stderr.strip()}")
        except Exception as e:
            if attempt == retries:
                print(f"Failed after {retries} attempts: {e}", file=sys.stderr)
                raise
            time.sleep(backoff)
    return None

def fetch_imf():
    url = 'https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH'
    data = curl_fetch(url)
    if not data:
        return
    raw_path = RAW_DIR / 'imf_raw.json'
    raw_path.write_text(data, encoding='utf-8')
    obj = json.loads(data)
    # DataMapper отдаёт матрицу «показатель -> страна -> год -> значение».
    # Забираем ряд по России и сохраняем отдельным файлом.
    rus = obj.get('values', {}).get('NGDP_RPCH', {}).get('RUS', {})
    if not rus:
        print('IMF: RUS series not found in response', file=sys.stderr)
        return
    norm_path = RAW_DIR / 'imf.json'
    norm_path.write_text(json.dumps({'indicator': 'NGDP_RPCH', 'country': 'RUS',
                                     'values': rus}, ensure_ascii=False, indent=2),
                         encoding='utf-8')
    csv_path = RAW_DIR / 'imf.csv'
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['year', 'value'])
        for year in sorted(rus, key=int):
            writer.writerow([year, rus[year]])
    print(f"IMF data saved: {norm_path} (raw: {raw_path}) and {csv_path}")


def fetch_wb():
    url = 'https://api.worldbank.org/v2/country/RUS/indicator/NY.GDP.MKTP.KD.ZG?format=json&per_page=64&date=1990:2031'
    data = curl_fetch(url)
    if not data:
        return
    path_json = RAW_DIR / 'wb.json'
    path_json.write_text(data, encoding='utf-8')
    obj = json.loads(data)
    if not (isinstance(obj, list) and len(obj) >= 2):
        print('WB: unexpected response shape', file=sys.stderr)
        return
    records = [r for r in obj[1] if r.get('value') is not None]
    csv_path = RAW_DIR / 'wb.csv'
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['year', 'value'])
        for rec in sorted(records, key=lambda r: r['date']):
            writer.writerow([rec['date'], rec['value']])
    print(f"World Bank data saved: {path_json} and {csv_path} ({len(records)} obs)")

def main():
    fetch_imf()
    fetch_wb()

if __name__ == '__main__':
    main()
