#!/usr/bin/env python3
"""Обновление файлов промышленной статистики Росстата (Prom, ind_baza, ind_sub, sezon).

Заменяет ручной разбор страницы: имена файлов предсказуемы, поэтому скрипт вычисляет период
сам (предыдущий месяц от даты запуска, с откатом на месяц назад, если файла ещё нет), проверяет
наличие, скачивает новые в raw/rosstat/data/ и raw/prom и валидирует структуру через openpyxl.

`Prom_MM_YYYY.xlsx` (месячный бюллетень «Производство важнейших видов продукции») добавлен
16.10.2026: раньше его скачивали руками, из-за чего прямой загрузчик `direct_rosstat_prom.py`
мог месяцами не видеть нового выпуска. Лежит он в raw/prom рядом с индексами.

Запуск (в том числе из cron):
  python3 scripts/rosstat_prom_files_update.py            # обновить
  python3 scripts/rosstat_prom_files_update.py --check    # только проверить доступность
"""
import argparse
import datetime as dt
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIRS = [os.path.join(REPO, 'raw', 'rosstat', 'data'), os.path.join(REPO, 'raw', 'prom')]
BASE = 'https://rosstat.gov.ru/storage/mediabank/'
PATTERNS = ['Prom_{mm}_{yyyy}.xlsx',
            'ind_baza_2023_{mm}-{yyyy}.xlsx', 'ind_sub_2023_{mm}-{yyyy}.xlsx',
            'sezon_2023_{mm}-{yyyy}.xlsx']
# Росстат меняет написание имени бюллетеня от года к году: 2023–2024 —
# prom_MM-YYYY.xlsx, 2025 — Prom_MM-YYYY.xlsx, 2026 — prom_MM_YYYY.xlsx.
# Поэтому для Prom пробуются оба разделителя и оба регистра: иначе джоб решает,
# что выпуска «нет на портале», и группа копит разрыв молча.
REFERER = 'https://rosstat.gov.ru/enterprise_industrial'  # без него часть файлов отдаёт 404


def month_seq(today, back_max=4):
    """Последовательность (yyyy, mm) от предыдущего месяца назад."""
    seq = []
    y, m = today.year, today.month
    for _ in range(back_max):
        m -= 1
        if m == 0:
            m, y = 12, y - 1
        seq.append((y, m))
    return seq


def candidates(name):
    """Варианты написания имени файла (для Prom — оба разделителя и регистра)."""
    variants = [name]
    if name.startswith('Prom_'):
        for alt in (name.replace('_', '-', 1), name.lower(),
                    name.lower().replace('_', '-', 1)):
            if alt not in variants:
                variants.append(alt)
    return variants


def exists_local(name):
    for d in TARGET_DIRS:
        for alt in candidates(name):
            p = os.path.join(d, alt)
            if os.path.exists(p) and os.path.getsize(p) > 10_000:
                return p
    return None


def dest_for(name):
    """Каталог по типу файла.

    Промбюллетень читает только `direct_rosstat_prom.py` и только из `raw/prom`,
    а индексы — загрузчики из `raw/rosstat/data`. Раньше скачивание всегда шло в
    TARGET_DIRS[0]: файл Prom ложился в `raw/rosstat/data`, `exists_local()`
    находил его там и больше не копировал, а загрузчик промпродукции его не видел
    — группа копила разрыв при формально успешном джобе.
    """
    return TARGET_DIRS[1] if name.startswith('Prom_') else TARGET_DIRS[0]


def fetch(name, dest_dir, check_only=False):
    """Скачать файл, перебирая варианты написания; возвращает путь или None.

    Итоговый файл сохраняется под каноническим именем `name`, даже если на портале
    он лежал под другим вариантом: загрузчики ищут файл по умолчанию
    (Prom_MM_YYYY.xlsx), и переименование здесь избавляет их от знания вариантов.
    """
    for alt in candidates(name):
        url = BASE + alt
        if check_only:
            r = subprocess.run(['curl', '-k', '-s', '-o', '/dev/null', '-w', '%{http_code}',
                                '-L', '-e', REFERER, '--max-time', '60', url],
                               capture_output=True, text=True)
            if r.stdout.strip() == '200':
                return '200'
            continue
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, name)
        r = subprocess.run(['curl', '-k', '-s', '-L', '-e', REFERER, '--max-time', '180',
                            '-w', '%{http_code}', '-o', dest, url],
                           capture_output=True, text=True)
        if (r.stdout or '').strip()[-3:] == '200':
            break
    else:
        if not check_only and os.path.exists(os.path.join(dest_dir, name)):
            os.remove(os.path.join(dest_dir, name))
        return None
    code = (r.stdout or '').strip()[-3:]
    ok = code == '200' and os.path.exists(dest) and os.path.getsize(dest) > 10_000
    if ok:
        # xlsx — это zip-контейнер; 404-страница Росстата отдаёт HTML с HTTP 404,
        # но её тело >10 КБ, поэтому одной проверки размера недостаточно.
        try:
            with open(dest, 'rb') as fh:
                ok = fh.read(2) == b'PK'
        except OSError:
            ok = False
    if not ok:
        if os.path.exists(dest):
            os.remove(dest)
        return None
    return dest


def validate(path):
    try:
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True)
        sheets = wb.sheetnames[:4]
        wb.close()
        return f'листов {len(sheets)}: {", ".join(sheets)}'
    except Exception as e:
        return f'проверка не прошла: {type(e).__name__} {str(e)[:60]}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='только проверить доступность файлов')
    args = ap.parse_args()
    today = dt.date.today()
    print(f'дата запуска: {today}')

    found_period, results = None, []
    for (y, m) in month_seq(today):
        names = [p.format(mm=f'{m:02d}', yyyy=y) for p in PATTERNS]
        if args.check:
            codes = [(n, fetch(n, None, check_only=True)) for n in names]
            if all(c == '200' for _, c in codes):
                found_period = (y, m)
                for n, c in codes:
                    print(f'  {n}: HTTP {c}')
                break
            continue
        local = [(n, exists_local(n)) for n in names]
        if all(p for _, p in local):
            found_period = (y, m)
            print(f'период {m:02d}.{y}: все файлы уже есть локально')
            for n, p in local:
                print(f'  {n}: {p} ({os.path.getsize(p)} байт)')
            break
        # файла нет локально — пробуем скачать
        downloaded, failed = [], []
        for n in names:
            if exists_local(n):
                continue
            d = fetch(n, dest_for(n))
            (downloaded if d else failed).append(n)
        if failed and not downloaded:
            print(f'период {m:02d}.{y}: файлов нет на портале ({", ".join(failed)}) — смотрим предыдущий месяц')
            continue
        found_period = (y, m)
        print(f'период {m:02d}.{y}: скачано {len(downloaded)} файлов, недоступно {len(failed)}')
        for n in names:
            p = exists_local(n)
            if p:
                results.append((n, os.path.getsize(p), validate(p)))
        break

    if not found_period:
        print('свежих файлов промышленных индексов на портале нет')
        return 1
    if results:
        print('\nпроверка структуры:')
        for n, sz, info in results:
            print(f'  {n}: {sz} байт, {info}')
    print(f'\nитог: актуальный период — {found_period[1]:02d}.{found_period[0]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())