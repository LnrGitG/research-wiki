#!/usr/bin/env python3
"""Parse CBR mortgage bulletin (Tag 211), escrow (Tag 167), VFS corporate/mortgage
files into data/cbr_lending.db (mortgage_monthly, escrow_monthly, corporate_monthly)."""
import os, re, glob, sqlite3, datetime
from openpyxl import load_workbook

ROOT = os.path.expanduser('~/research-wiki-private')
RAW = os.path.join(ROOT, 'raw', 'cbr')
DB = os.path.join(ROOT, 'data', 'cbr_lending.db')

MONTHS = {'январь':1,'февраль':2,'март':3,'апрель':4,'май':5,'июнь':6,'июль':7,
          'август':8,'сентябрь':9,'октябрь':10,'ноябрь':11,'декабрь':12}

def clean(v):
    if v is None: return None
    if isinstance(v, (int, float)):
        if isinstance(v, float) and (v != v or v in (float('inf'), float('-inf'))): return None
        return v
    s = str(v).replace('\xa0','').replace(' ','').replace(',','.')
    s = s.replace('−','-')
    if s in ('','-','–','…','x','X'): return None
    try: return float(s)
    except ValueError: return None

def norm_month(val):
    """Return (date, label) from month header cell, e.g. 'Июнь 2026'."""
    if val is None: return None, None
    s = str(val).strip().lower()
    m = re.match(r'([а-яё]+)\s+(\d{4})', s)
    if m and m.group(1) in MONTHS:
        return f'{int(m.group(2)):04d}-{MONTHS[m.group(1)]:02d}-01', str(val).strip()
    # try date objects
    if isinstance(val, datetime.datetime):
        return val.strftime('%Y-%m-%d'), val.strftime('%Y-%m')
    return None, None

def get_conn():
    conn = sqlite3.connect(DB)
    for tbl in ('mortgage_monthly','escrow_monthly','corporate_monthly'):
        conn.execute(f'''CREATE TABLE IF NOT EXISTS {tbl} (
            region_name TEXT, report_date TEXT, indicator TEXT,
            value REAL, unit TEXT,
            PRIMARY KEY (region_name, report_date, indicator))''')
    return conn

def parse_bulletin(path, conn):
    n = 0
    wb = load_workbook(path, data_only=True, read_only=True)
    sheets = sorted([s for s in wb.sheetnames if re.match(r'^[ТT]_(1[6-9]|2[0-9]|3[0-4])$', s)],
                    key=lambda s: int(re.sub(r'\D','',s)))
    indicators = {
        'Т_16': ('Количество ИЖК по регионам','ед.'),
        'Т_17': ('Количество ИЖК по ДДУ по регионам','ед.'),
        'Т_18': ('Количество ИЖК на цели ИЖС по регионам','ед.'),
        'T_19': ('Объём ИЖК по регионам','млн руб'),
        'T_20': ('Объём ИЖК по ДДУ по регионам','млн руб'),
        'T_21': ('Объём ИЖК на цели ИЖС по регионам','млн руб'),
        'T_22': ('Задолженность по ИЖК по регионам','млн руб'),
        'T_23': ('Задолженность по ИЖК по ДДУ по регионам','млн руб'),
        'T_24': ('Просроченная задолженность по ИЖК по регионам','млн руб'),
        'T_25': ('Просроченная задолженность по ИЖК по ДДУ','млн руб'),
        'T_26': ('Ставка по ИЖК по регионам','%'),
        'T_27': ('Ставка по ИЖК по ДДУ по регионам','%'),
        'T_28': ('Ставка по ИЖК без учёта ДДУ','%'),
        'T_29': ('Ставка по ИЖК на цели ИЖС','%'),
        'T_30': ('Доля ИЖК в общем объёме кредитов','%'),
        'T_31': ('Доля задолженности по ИЖК','%'),
        'T_32': ('Средний размер ИЖК','млн руб'),
        'T_33': ('Средний размер ИЖК по ДДУ','млн руб'),
        'Т_34': ('Средняя цена 1 кв.м по регионам','тыс руб/кв.м'),
    }
    for sh in sheets:
        key = sh.replace('Т','T') if sh.startswith('Т') else sh
        ind, unit = indicators.get(key, (f'Bulletin sheet {sh}', 'n/a'))
        ws = wb[sh]
        rows = list(ws.iter_rows(values_only=True))
        if len(rows) < 6: continue
        # header row: find row with month labels within first 6 rows
        hidx = None
        for i, r in enumerate(rows[:6]):
            cnt = sum(1 for v in r if norm_month(v)[0])
            if cnt >= 5: hidx = i; break
        if hidx is None: continue
        header_row = rows[hidx]
        month_cols = []
        for ci, v in enumerate(header_row):
            d, label = norm_month(v)
            if d: month_cols.append((ci, d))
        if not month_cols: continue
        for row in rows[hidx+1:]:
            region = row[0] if row else None
            if region is None: continue
            rname = str(region).strip()
            if not rname or rname.upper().startswith('ФЕДЕРАЛЬНЫЙ ОКРУГ'): continue
            if rname.startswith('Источник') or rname.startswith('Примеч'): continue
            for ci, d in month_cols:
                if ci >= len(row): continue
                val = clean(row[ci])
                if val is None: continue
                conn.execute('INSERT OR REPLACE INTO mortgage_monthly VALUES (?,?,?,?,?)',
                             (rname, d, ind, val, unit))
                n += 1
    wb.close()
    return n

def parse_escrow(path, conn):
    d = None
    m = re.search(r'(\d{2})(\d{2})(\d{4})', os.path.basename(path))
    if m: d = f'{m.group(3)}-{m.group(2)}-{m.group(1)}'
    n = 0
    wb = load_workbook(path, data_only=True, read_only=True)
    ws = wb[wb.sheetnames[0]]
    rows = list(ws.iter_rows(values_only=True))
    # find header row (contains '№ п/п' or 'Субъект')
    hidx = None
    for i, r in enumerate(rows[:10]):
        if r and any(v is not None and '№' in str(v) for v in r):
            hidx = i; break
    if hidx is None: return 0
    header = rows[hidx]
    # map columns by header text (layout varies across releases)
    colmap = []  # (col_idx, indicator, unit)
    for ci, v in enumerate(header):
        if v is None: continue
        t = str(v).lower().replace('\n',' ')
        if 'действующих кредит' in t and 'кол' in t: colmap.append((ci,'Количество действующих кредитных договоров','ед.'))
        elif 'сумма действующих' in t: colmap.append((ci,'Сумма действующих кредитных договоров','млн руб'))
        elif 'задолженность' in t: colmap.append((ci,'Задолженность по кредитам','млн руб'))
        elif 'счетов эскроу, имеющ' in t or ('счетов эскроу' in t and 'имеющ' in t): colmap.append((ci,'Количество счетов эскроу с остатком','ед.'))
        elif 'кол-во счетов эскроу' in t or 'кол-во счетов' in t: colmap.append((ci,'Количество счетов эскроу','ед.'))
        elif 'остатки средств' in t: colmap.append((ci,'Остатки средств на счетах эскроу','млн руб'))
        elif 'ставка' in t: colmap.append((ci,'Средневзвешенная ставка по кредитам','%'))
        elif 'раскрыт' in t and 'кол' in t: colmap.append((ci,'Количество раскрытых счетов эскроу','ед.'))
        elif 'перечислен' in t: colmap.append((ci,'Сумма средств с раскрытых счетов эскроу','млн руб'))
    for row in rows[hidx+1:]:
        if not row or len(row) < 3: continue
        # region: first non-numeric text cell
        rname = None
        for v in row:
            if v is None: continue
            s = str(v).strip()
            if s and not re.match(r'^[\d\s.,]+$', s):
                rname = s; break
        if rname is None: continue
        if rname.upper().startswith('ФЕДЕРАЛЬНЫЙ ОКРУГ'): continue
        if 'ФО' == rname.upper().strip()[-2:] and len(rname) <= 25 and re.match(r'^[А-ЯЁ][а-яё]+ ФО', rname): continue
        if rname.startswith('Источник') or rname.startswith('Примеч'): continue
        for ci, ind, unit in colmap:
            if ci >= len(row): continue
            val = clean(row[ci])
            if val is None: continue
            conn.execute('INSERT OR REPLACE INTO escrow_monthly VALUES (?,?,?,?,?)',
                         (rname, d, ind, val, unit))
            n += 1
    wb.close()
    return n

def parse_vfs(path, conn):
    """VFS cumulative: 3 sheets (рубли/валюта/итого), row 3 = month headers, row 4+ regions."""
    fname = os.path.basename(path)
    is_corp = fname.startswith('01_')
    kind = 'new_loans' if 'New_loans' in fname else 'debt'
    if is_corp:
        base = 'Корпоративные кредиты — ' + ('новые выдачи' if kind=='new_loans' else 'задолженность')
    else:
        base = 'Ипотека физлицам — ' + ('новые выдачи' if kind=='new_loans' else 'задолженность')
    sheet_labels = {'рубли':'рубли','валюта':'валюта','итого':'итого'}
    n = 0
    wb = load_workbook(path, data_only=True, read_only=True)
    for sh in wb.sheetnames:
        lab = sheet_labels.get(sh.lower().strip(), sh)
        ind = f'{base} ({lab})'
        ws = wb[sh]
        rows = list(ws.iter_rows(values_only=True))
        if len(rows) < 4: continue
        header = None; hidx = None
        for i, r in enumerate(rows[:6]):
            cnt = sum(1 for v in r if norm_month(v)[0])
            if cnt >= 5: header, hidx = r, i; break
        if header is None: continue
        month_cols = [(ci, norm_month(v)[0]) for ci, v in enumerate(header) if norm_month(v)[0]]
        for row in rows[(hidx or 0)+1:]:
            if not row: continue
            rname = row[0]
            if rname is None: continue
            rname = str(rname).strip()
            if not rname: continue
            if rname.startswith('Источник') or rname.startswith('Примеч'): continue
            for ci, d in month_cols:
                if ci >= len(row): continue
                val = clean(row[ci])
                if val is None: continue
                conn.execute('INSERT OR REPLACE INTO corporate_monthly VALUES (?,?,?,?,?)',
                             (rname, d, ind, val, 'млн руб'))
                n += 1
    wb.close()
    return n

def main():
    conn = get_conn()
    # bulletin: use latest
    bulls = sorted(glob.glob(os.path.join(RAW, 'bulletin', 'mortgage_lending_market_*.xlsx')))
    res = {}
    if bulls:
        latest = bulls[-1]
        print('Bulletin:', os.path.basename(latest))
        res['mortgage'] = parse_bulletin(latest, conn)
    escrows = sorted(glob.glob(os.path.join(RAW, 'escrow', '*.xlsx')))
    tot = 0
    for p in escrows:
        tot += parse_escrow(p, conn)
    res['escrow'] = tot
    vfs = [os.path.join(RAW, 'vfs', f) for f in
           ('01_04_D_New_loans_subj.xlsx','01_05_D_Debt_subj.xlsx',
            '02_04_New_loans_ind.xlsx','02_05_Debt_ind.xlsx')]
    tot = 0
    for p in vfs:
        if os.path.exists(p):
            tot += parse_vfs(p, conn)
    res['corporate'] = tot
    conn.commit()
    for tbl in ('mortgage_monthly','escrow_monthly','corporate_monthly'):
        cnt, last = conn.execute(
            f'SELECT COUNT(*), MAX(report_date) FROM {tbl}').fetchone()
        print(f'{tbl}: {cnt} rows, latest {last}')
    conn.close()
    print(res)

if __name__ == '__main__':
    main()