#!/usr/bin/env python3
"""Обновление ФНС 1-НОМ (open data 7707329152-1nom): докачка новых версий и переинжест.

Что делает:
1) читает страницу набора и список доступных версий (structure-ГГГГММДД.csv);
2) скачивает те версии, которых нет в raw/fns (файл данных + справочник полей);
3) запускает переинжест по кодам ОКВЭД (scripts/fix_fns_okved_codes.py) — идемпотентно.

Вызов по cron: месячная проверка (между публикациями версии может не быть — тогда скрипт
просто сообщает, что обновлять нечего). Календарь ФНС нерегулярный: в 2020-2022 годах
выходило по 8-11 версий в год, в 2025 — 4, в 2026 — 3 (примерно раз в квартал).
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'raw', 'fns')
STRUCT_DIR = os.path.join(RAW, 'structure')
PAGE = 'https://www.nalog.gov.ru/opendata/7707329152-1nom/'
DATA_TMPL = 'https://data.nalog.ru/opendata/7707329152-1nom/data-{v}-structure-{v}.csv'
STRUCT_TMPL = 'https://data.nalog.ru/opendata/7707329152-1nom/structure-{v}.csv'
UA = {'User-Agent': 'Mozilla/5.0 (hermes-research)'}


def fetch(url, timeout=60):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def available_versions():
    html = fetch(PAGE).decode('utf-8', 'replace')
    return sorted(set(re.findall(r'structure-(\d{8})\.csv', html)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-ingest', action='store_true', help='только скачать, без переинжеста')
    ap.add_argument('--limit', type=int, default=0, help='ограничить число новых версий')
    args = ap.parse_args()

    os.makedirs(STRUCT_DIR, exist_ok=True)
    vers = available_versions()
    have = {os.path.basename(f)[5:13] for f in os.listdir(RAW) if f.startswith('1nom_') and f.endswith('.csv')}
    new = [v for v in vers if v not in have]
    if args.limit:
        new = new[:args.limit]
    print(f'версий на портале: {len(vers)} (свежая {vers[-1]}), локально {len(have)}, новых {len(new)}')
    if not new:
        print('обновлять нечего')
        return 0

    for v in new:
        dpath = os.path.join(RAW, f'1nom_{v}.csv')
        spath = os.path.join(STRUCT_DIR, f'structure-{v}.csv')
        try:
            data = fetch(DATA_TMPL.format(v=v))
            open(dpath, 'wb').write(data)
            print(f'  данные {v}: {len(data)} байт')
        except Exception as e:
            print(f'  данные {v}: ОШИБКА {type(e).__name__} {str(e)[:60]}')
            continue
        try:
            st = fetch(STRUCT_TMPL.format(v=v))
            open(spath, 'wb').write(st)
            print(f'  справочник {v}: {len(st)} байт')
        except Exception as e:
            print(f'  справочник {v}: ОШИБКА {type(e).__name__} {str(e)[:60]} (винтаж будет пропущен)')

    if args.no_ingest:
        return 0

    script = os.path.join(ROOT, 'scripts', 'fix_fns_okved_codes.py')
    print('переинжест по кодам ОКВЭД...')
    res = subprocess.run([sys.executable, script], capture_output=True, text=True, timeout=3600)
    tail = [l for l in (res.stdout or '').splitlines() if l.strip()][-8:]
    for l in tail:
        print('   ', l)
    if res.returncode != 0:
        print('переинжест завершился с кодом', res.returncode, (res.stderr or '')[-300:])
    return res.returncode


if __name__ == '__main__':
    raise SystemExit(main())