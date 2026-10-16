#!/usr/bin/env python3
"""Докачка файлов Росстата по вводу в действие зданий (vv-zd, vv-mosh).

Имена файлов на портале предсказуемы, поэтому период вычисляется от даты
запуска: `vv-zd-sub_MM-YYYY.xlsx` — по субъектам РФ, за каждый месяц года
(файл кумулятивный внутри года: в сентябрьском выпуске лежат январь..сентябрь);
`vv-zd-oper_Qkv-YYYY.xlsx` — по типам зданий в РФ, накопленным итогом с начала
года, выходит по кварталам. Дополнительно проверяются файлы ввода мощностей
(`vv-mosh-oper`, `vv-mosh-sub`) — они нужны следующей группе прямых загрузчиков.

Проверка целостности как у промышленного апдейтера: HTTP 200, размер > 10 КБ и
сигнатура zip («PK»), иначе файл удаляется — страница 404 у Росстата тоже
весит больше 10 КБ.

Запуск: python3 scripts/rosstat_vv_zd_files_update.py [--check]
"""
import argparse
import datetime as dt
import os
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(REPO, 'raw', 'rosstat', 'data')
BASE = 'https://rosstat.gov.ru/storage/mediabank/'


def month_names(today, back=4):
    out = []
    y, m = today.year, today.month
    for _ in range(back):
        out.append('vv-zd-sub_%02d-%d.xlsx' % (m, y))
        m -= 1
        if m == 0:
            m, y = 12, y - 1
    return out


def quarter_names(today, back=3):
    """Квартальные файлы: ввод зданий по типам и ввод мощностей (РФ и субъекты).

    `vv-mosh-oper` — ввод производственных мощностей по видам, накопленным
    итогом с начала года (разбирает `direct_mosh.py`); `vv-mosh-sub` — тот же
    показатель по субъектам, он пока только скачивается: разбор регионального
    разреза ждёт решения владельца.
    """
    q = (today.month - 1) // 3 + 1
    out = []
    y = today.year
    for _ in range(back):
        out.append('vv-zd-oper_%dkv-%d.xlsx' % (q, y))
        out.append('vv-mosh-oper_%dkv-%d.xlsx' % (q, y))
        out.append('vv-mosh-sub_%dkv-%d.xlsx' % (q, y))
        q -= 1
        if q == 0:
            q, y = 4, y - 1
    return out


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
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True)
        names = wb.sheetnames
        wb.close()
        return 'листов %d (%s .. %s)' % (len(names), names[0], names[-1])
    except Exception as e:  # noqa: BLE001
        return 'проверка не прошла: %s %s' % (type(e).__name__, str(e)[:60])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    today = dt.date.today()
    print('дата запуска: %s' % today)

    fresh, seen = [], []
    for name in month_names(today) + quarter_names(today):
        code = fetch(name, check_only=True) if args.check else fetch(name)
        if args.check:
            print('  %s: HTTP %s' % (name, code))
            if code == '200':
                fresh.append(name)
            continue
        if code:
            path = os.path.join(DEST, name)
            seen.append(name)
            if code == 'скачан':
                print('  %s: скачан, %s' % (name, sheets(path)))
            else:
                print('  %s: уже есть локально' % name)

    if args.check:
        print('\nдоступно на портале: %s' % (', '.join(fresh) or 'нет'))
        return 0
    if not seen:
        print('ни одного файла по вводу зданий получить не удалось')
        return 1
    subs = sorted(n for n in seen if n.startswith('vv-zd-sub'))
    print('\nготово; свежайший по субъектам: %s' % (subs[-1] if subs else 'нет'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
