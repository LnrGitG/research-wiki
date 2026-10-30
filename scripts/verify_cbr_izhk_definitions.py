#!/usr/bin/env python3
"""Сверка определений и значений ипотечного блока ЦБ с первоисточником.

Зачем. Статус `official` у определения означает «смысл подтверждён», но
`verified_at` до сих пор пуст: подтверждения источником не было. Здесь
закрывается первый транш — ипотечные ряды, у которых первоисточник доступен
напрямую с VPS (`cbr.ru` отдаёт 200, в отличие от дом.рф и fedstat).

Три вещи, которые скрипт проверяет и которые легко перепутать:
  1. **Файл.** В каталоге `/vfs/statistics/BankSector/Mortgage/` лежат и ряды по
     всем кредитам физлицам (`02_04_New_loans_ind`, `02_05_Debt_ind`), и именно
     ипотечные (`02_11_New_loans_mortgage`, `02_14_Debt_mortgage`,
     `02_13_Rates_mortgage`). Сверка объёма ИЖК с файлом «все кредиты ФЛ» даёт
     расхождение в 6 раз — это не ошибка ряда, а чужой показатель.
  2. **Лист.** В `02_13_Rates_mortgage` первый лист — средневзвешенный *срок*
     (285,7 месяца), ставка лежит на листе «ставка в рублях». Поэтому лист
     задаётся явно, а не берётся `sheetnames[0]`.
  3. **Ревизия.** ЦБ пересматривает опубликованные значения: ядро отстаёт от
     текущей редакции файла на 0,02–0,09 %. Это не расхождение определения,
     поэтому два порога: 0,05 % — совпадение, 0,2 % — ревизия источника
     (тоже подтверждает смысл, но попадает в отчёт).

`--apply` ставит `verified_at` только кодам, прошедшим оба порога.
"""
import argparse
import io
import os
import re
import ssl
import sys
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402
import openpyxl  # noqa: E402

BASE = 'https://www.cbr.ru/vfs/statistics/BankSector/Mortgage/'
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

FILES = {
    'cbr_izhk_volume_m': ('02_11_New_loans_mortgage.xlsx', 'итого',
                          'выдано ИЖК, млн руб'),
    'cbr_izhk_debt_m': ('02_14_Debt_mortgage.xlsx', 'итого',
                        'задолженность по ИЖК, млн руб'),
    'cbr_izhk_rate_m': ('02_13_Rates_mortgage.xlsx', 'ставка в рублях',
                        'средневзвешенная ставка по ИЖК в рублях, % годовых'),
}
TOL = 0.0005       # 0,05 % — совпадение с точностью публикации
TOL_REV = 0.002    # 0,2 % — расхождение в пределах ревизии источника
MON = {'январ': 1, 'феврал': 2, 'март': 3, 'апрел': 4, 'ма': 5, 'июн': 6,
       'июл': 7, 'август': 8, 'сентябр': 9, 'октябр': 10, 'ноябр': 11, 'декабр': 12}


def to_num(v):
    """Число из ячейки: float, либо строка вида «1 234,5» / «0,00»."""
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.replace('\xa0', '').replace(' ', '').replace(',', '.').strip()
        try:
            return float(s)
        except ValueError:
            return None
    return None


def fetch(name):
    req = urllib.request.Request(BASE + name, headers={'User-Agent': 'Mozilla/5.0'})
    body = urllib.request.urlopen(req, context=CTX, timeout=90).read()
    return openpyxl.load_workbook(io.BytesIO(body), read_only=True, data_only=True)


def periods_of(header_row):
    out = []
    for cell in header_row[1:]:
        if cell is None:
            out.append(None)
            continue
        if hasattr(cell, 'year'):
            out.append((cell.year, cell.month))
            continue
        m = re.match(r'([А-Яа-я]+)\s+(\d{4})', str(cell).strip())
        out.append((int(m.group(2)), MON.get(m.group(1).lower()[:6])) if m else None)
    return out


def parse(ws, wanted):
    rows = list(ws.iter_rows(values_only=True))
    hdr = None
    for i, r in enumerate(rows[:6]):
        if r and any(hasattr(c, 'year') or (isinstance(c, str) and re.search(r'\d{4}', c))
                     for c in r[1:] if c is not None):
            hdr = i
            break
    if hdr is None:
        return {}
    periods = periods_of(rows[hdr])
    out = {}
    for r in rows[hdr + 1:]:
        if not r or not r[0]:
            continue
        name = str(r[0]).strip().upper()
        if not any(name.startswith(w) for w in wanted):
            continue
        key = 'RU' if name.startswith('РОССИЙСКАЯ') else 'RB'
        vals = {}
        for p, v in zip(periods, r[1:]):
            num = to_num(v)
            if p and p[1] and num is not None:
                vals[(p[0], p[1])] = num
        out[key] = vals
    return out


def canon(code):
    sql = """
    SELECT r.region_code, EXTRACT(year FROM o.period_start)::int,
           EXTRACT(month FROM o.period_start)::int, o.value
    FROM data.observation o
    JOIN catalog.metric m ON m.metric_id = o.metric_id
    JOIN catalog.region r ON r.region_id = o.region_id
    WHERE m.metric_code = %s
      AND o.observation_status NOT IN ('rejected', 'superseded')
      AND r.region_code IN ('ru', 'bashkortostan')
    """
    out = {}
    for rcode, y, m, v in db_tunnel.query(sql, (code,)):
        key = 'RU' if str(rcode).lower() == 'ru' else 'RB'
        out.setdefault(key, {})[(y, m)] = float(v)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    verdicts = {}
    for code, (fname, sheet, meaning) in FILES.items():
        wb = fetch(fname)
        if sheet not in wb.sheetnames:
            print(f'\n{code}: листа «{sheet}» нет в {fname} ({wb.sheetnames})')
            verdicts[code] = ('нет источника', 0, meaning)
            continue
        ws = wb[sheet]
        src = parse(ws, ('РОССИЙСКАЯ', 'РЕСПУБЛИКА БАШКОРТОСТАН'))
        can = canon(code)
        print(f'\n{code}: {fname} / «{sheet}», смысл — {meaning}')
        worst, checked, statuses = 0.0, 0, []
        for key, label in (('RU', 'РФ'), ('RB', 'Башкортостан')):
            s, c = src.get(key, {}), can.get(key, {})
            common = sorted(set(s) & set(c))[-3:]
            if not common:
                print(f'  {label}: общих периодов нет')
                continue
            for y, m in common:
                a, b = s[(y, m)], c[(y, m)]
                diff = abs(a - b) / max(abs(a), 1e-9)
                worst = max(worst, diff)
                checked += 1
                statuses.append(diff)
                flag = 'ok' if diff <= TOL else ('ревизия' if diff <= TOL_REV else 'РАСХОЖДЕНИЕ')
                print(f'  {label} {y}-{m:02d}: ЦБ {a:,.2f} | ядро {b:,.2f} | '
                      f'{diff*100:.4f}% {flag}')
        if checked and max(statuses) <= TOL_REV:
            verdict = 'ПОДТВЕРЖДЁН' if worst <= TOL else 'ПОДТВЕРЖДЁН (ревизия источника)'
        else:
            verdict = 'не подтверждён'
        verdicts[code] = (verdict, checked, meaning)

    print('\nитог:')
    for code, (verdict, n, meaning) in verdicts.items():
        print(f'  {code}: {verdict} ({n} сверок; {meaning})')

    if not args.apply:
        print('режим --check: verified_at не менялся')
        return 0

    ok_codes = [c for c, (v, n, _) in verdicts.items() if v.startswith('ПОДТВЕРЖДЁН')]
    if not ok_codes:
        print('нечего подтверждать')
        return 0
    conn = db_tunnel.connect()
    try:
        with conn.cursor() as cur:
            for code in ok_codes:
                cur.execute("""UPDATE catalog.metric_definition
                               SET verified_at = now(), updated_at = now()
                               WHERE metric_code = %s AND status = 'official'
                                 AND verified_at IS NULL""", (code,))
                print(f'  {code}: verified_at проставлен, строк {cur.rowcount}')
        conn.commit()
    finally:
        conn.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
