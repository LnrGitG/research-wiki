#!/usr/bin/env python3
"""trudvsem (Работа России) — еженедельный сбор статистики вакансий.

API: https://opendata.trudvsem.ru/api/v1/vacancies/region/<code>?limit=1
— открыт, без ключа. На регион-дату фиксируем только meta.total
(число вакансий) — лёгкий запрос limit=1. Данные складываем в
data/trudvsem_counts.csv (append, идемпотентно по регион+дата).

Запуск: cron еженедельно (среда). Регионы: коды ОКАТО-подобные
(6600000000000 = Свердловская). Список — из справочника API
opendata.trudvsem.ru/api/v1/regions или фиксированный словарь.
"""
import csv
import json
import os
import sys
import urllib.request
from datetime import date, timedelta

OUT = os.path.expanduser('~/research-wiki-private/data/trudvsem_counts.csv')
BASE = 'https://opendata.trudvsem.ru/api/v1'

# Ключевые макрорегионы ГУ ЦБ + РФ-крупные: (код, имя) — расширяемо
REGIONS = {
    '6600000000000': 'Свердловская область',
    '0200000000000': 'Республика Башкортостан',
    '4500000000000': 'город Москва',
    '5000000000000': 'Московская область',
    '7800000000000': 'город Санкт-Петербург',
    '2300000000000': 'Краснодарский край',
    '5400000000000': 'Новосибирская область',
    '6100000000000': 'Ростовская область',
    '6300000000000': 'Самарская область',
    '6400000000000': 'Саратовская область',
}


def fetch_total(code):
    url = f'{BASE}/vacancies/region/{code}?limit=1'
    req = urllib.request.Request(url, headers={'User-Agent': 'research-wiki/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode('utf-8'))
    return int(data['meta']['total'])


def main():
    today = date.today().isoformat()
    existing = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            existing = {(r['date'], r['region']) for r in csv.DictReader(f)}
    else:
        with open(OUT, 'w', newline='') as f:
            csv.DictWriter(f, ['date', 'region', 'region_code', 'vacancies']).writeheader()
    n = 0
    with open(OUT, 'a', newline='') as f:
        w = csv.DictWriter(f, ['date', 'region', 'region_code', 'vacancies'])
        for code, name in REGIONS.items():
            if (today, name) in existing:
                continue
            try:
                total = fetch_total(code)
                w.writerow({'date': today, 'region': name, 'region_code': code, 'vacancies': total})
                f.flush()
                n += 1
                print(f'{name}: {total}')
            except Exception as e:
                print(f'{name}: ERROR {e}', file=sys.stderr)
    print(f'appended {n} rows -> {OUT}')


if __name__ == '__main__':
    main()