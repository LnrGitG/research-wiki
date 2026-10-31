#!/usr/bin/env python3
"""Докачка квартального файла Росстата по инвестициям в основной капитал.

Сырьё группы ИКВ по регионам — `Inv_reg_kv_2020-2026.xlsx` (лист «млн. рублей»
и лист «к соотв.периоду»), его разбирает `scripts/direct_ikv_reg.py`. Имя файла
содержит диапазон лет, который Росстат раз в год сдвигает, поэтому проверяются
варианты «Inv_reg_kv_2020-<текущий год>.xlsx» и «Inv_reg_kv_2020-<год+1>.xlsx»:
файла ровно с будущим годом в имени на портале ещё нет, а после продления
диапазона он появится сам.

Проверка целостности как у остальных апдейтеров: HTTP 200, размер > 10 КБ и
сигнатура zip («PK»), иначе файл удаляется — страница 404 у Росстата тоже весит
больше 10 КБ.

Запуск: python3 scripts/rosstat_inv_files_update.py [--check]
"""

try:
    from xlsx_engine import add_engine_arg, engine_from_argv, open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import add_engine_arg, engine_from_argv, open_workbook  # noqa: E402
ENGINE = engine_from_argv()  # --xlsx-engine openpyxl|fastexcel, резерв — XLSX_ENGINE

try:
    from xlsx_engine import open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import open_workbook  # noqa: E402

import argparse
import datetime as dt
import os
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(REPO, 'raw', 'rosstat', 'data')
BASE = 'https://rosstat.gov.ru/storage/mediabank/'


def names(today):
    """Варианты имени файла: диапазон лет в имени сдвигается раз в год."""
    return ['Inv_reg_kv_2020-%d.xlsx' % today.year,
            'Inv_reg_kv_2020-%d.xlsx' % (today.year + 1)]


def fetch(name, check_only=False):
    url = BASE + name
    if check_only:
        r = subprocess.run(['curl', '-k', '-s', '-o', '/dev/null', '-w', '%{http_code}',
                            '-L', '--max-time', '60', url], capture_output=True, text=True)
        return (r.stdout or '').strip()[-3:]
    os.makedirs(DEST, exist_ok=True)
    dest = os.path.join(DEST, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 10_000:
        return 'local'
    r = subprocess.run(['curl', '-k', '-s', '-L', '--max-time', '180',
                        '-w', '%{http_code}', '-o', dest, url],
                       capture_output=True, text=True)
    code = (r.stdout or '').strip()[-3:]
    ok = code == '200' and os.path.exists(dest) and os.path.getsize(dest) > 10_000
    if ok:
        with open(dest, 'rb') as fh:
            ok = fh.read(2) == b'PK'
    if not ok:
        if os.path.exists(dest):
            os.remove(dest)
        return None
    return 'скачан'


def sheets(path):
    try:
        wb = open_workbook(path, engine=ENGINE)
        out = 'листов %d (%s)' % (len(wb.sheetnames), ', '.join(wb.sheetnames))
        wb.close()
        return out
    except Exception as e:  # noqa: BLE001
        return 'проверка не прошла: %s %s' % (type(e).__name__, str(e)[:60])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    today = dt.date.today()
    print('дата запуска: %s' % today)

    fresh, seen = [], []
    for name in names(today):
        code = fetch(name, check_only=True) if args.check else fetch(name)
        if args.check:
            print('  %s: HTTP %s' % (name, code))
            if code == '200':
                fresh.append(name)
            continue
        if code:
            seen.append(name)
            print('  %s: %s' % (name, sheets(os.path.join(DEST, name))
                                if code == 'скачан' else 'уже есть локально'))

    if args.check:
        print('\nдоступно на портале: %s' % (', '.join(fresh) or 'нет'))
        return 0
    if not seen:
        print('файл по ИКВ получить не удалось — имя изменилось?')
        return 1
    print('\nготово; свежайший: %s' % sorted(seen)[-1])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
