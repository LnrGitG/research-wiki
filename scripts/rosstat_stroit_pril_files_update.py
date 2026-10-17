#!/usr/bin/env python3
"""Докачка и распаковка приложения к сборнику «Строительство в России».

Сырьё группы парка строительной техники — приложение к сборнику
(`Srtoit_<год>.rar` на портале Росстата). Используется таблица 2.11
(`R_10_2_4_pril.xlsx`), разбирает её `scripts/direct_stroit_pril.py`.

Сборник выходит раз в год, поэтому проверяются имена с текущим и следующим
годом: файла с будущим годом пока нет, и он появится сам после публикации.
Контроль целостности: HTTP 200, размер > 100 КБ и сигнатура RAR («Rar!»),
иначе файл удаляется (страница 404 у Росстата тоже весит больше 10 КБ).
Распаковка — `unrar x` в `yearbooks/Stroit_Pril_<год>/`, повторно не делается.

Запуск: python3 scripts/rosstat_stroit_pril_files_update.py [--check]
"""

import argparse
import datetime as dt
import os
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YB = os.path.join(REPO, 'raw', 'rosstat', 'yearbooks')
BASE = 'https://rosstat.gov.ru/storage/mediabank/'


def names(today):
    return ['Srtoit_%d.rar' % today.year, 'Srtoit_%d.rar' % (today.year + 1)]


def fetch(name, check_only=False):
    url = BASE + name
    if check_only:
        r = subprocess.run(['curl', '-k', '-s', '-o', '/dev/null', '-w', '%{http_code}',
                            '-L', '--max-time', '60', url], capture_output=True, text=True)
        return (r.stdout or '').strip()[-3:]
    dest = os.path.join(YB, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 100_000:
        return 'local'
    os.makedirs(YB, exist_ok=True)
    r = subprocess.run(['curl', '-k', '-s', '-L', '--max-time', '300',
                        '-w', '%{http_code}', '-o', dest, url],
                       capture_output=True, text=True)
    code = (r.stdout or '').strip()[-3:]
    ok = code == '200' and os.path.exists(dest) and os.path.getsize(dest) > 100_000
    if ok:
        with open(dest, 'rb') as fh:
            ok = fh.read(4) == b'Rar!'
    if not ok:
        if os.path.exists(dest):
            os.remove(dest)
        return None
    return 'скачан'


def extract(name):
    """Распаковка приложения в yearbooks/Stroit_Pril_<год>/ (один раз)."""
    year = name.split('_')[-1].split('.')[0]
    out = os.path.join(YB, 'Stroit_Pril_%s' % year)
    src = os.path.join(YB, name)
    if os.path.isdir(out) and any(f.endswith('.xlsx')
                                  for _, _, fs in os.walk(out) for f in fs):
        return '%s: уже распаковано' % name
    if not os.path.exists(src):
        return '%s: архива нет' % name
    os.makedirs(out, exist_ok=True)
    r = subprocess.run(['unrar', 'x', '-o+', '-idq', src, out + os.sep],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return '%s: unrar вернул %d (%s)' % (name, r.returncode, (r.stderr or '')[:80])
    found = [f for _, _, fs in os.walk(out) for f in fs if f.endswith('.xlsx')]
    return '%s: распаковано, xlsx %d' % (name, len(found))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    today = dt.date.today()
    print('дата запуска: %s' % today)

    if args.check:
        fresh = [n for n in names(today) if fetch(n, check_only=True) == '200']
        for n in names(today):
            print('  %s: HTTP %s' % (n, fetch(n, check_only=True)))
        print('\nдоступно на портале: %s' % (', '.join(fresh) or 'нет'))
        return 0

    got = []
    for name in names(today):
        st = fetch(name)
        if st:
            got.append(name)
            print('  %s: %s' % (name, st))
    # уже скачанные сборники прошлых лет тоже должны быть распакованы: имя файла
    # содержит год выпуска, поэтому проверяем и локальные архивы
    local = sorted(f for f in os.listdir(YB)
                   if f.startswith('Srtoit_') and f.endswith('.rar')) if os.path.isdir(YB) else []
    for name in local:
        if name not in got:
            got.append(name)
            print('  %s: локальный архив' % name)
    if not got:
        print('приложение к сборнику не найдено — имя изменилось?')
        return 1
    for name in got:
        print('     ' + extract(name))
    print('\nготово: %s' % ', '.join(got))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
