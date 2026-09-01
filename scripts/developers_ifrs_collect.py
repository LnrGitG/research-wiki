#!/usr/bin/env python3
"""Collect IFRS financial history for public developers from smart-lab.ru /q/<ticker>/f/{y,q}/.

Creates data/developers_ifrs.db, table dev_ifrs:
(ticker, company, freq Y/Q, period '2025'/'2025Q2', metric_en, value, source, loaded)

Annual: 2021-2025 (+LTM col). Quarterly: last 5 quarters incl. current.
Rerun after each reporting season; INSERT OR REPLACE keeps it idempotent.
"""
import sqlite3, re, sys, time, urllib.request

BASE = '/home/lnr/research-wiki'
DB = f'{BASE}/data/developers_ifrs.db'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0'
TICKERS = {'PIKK': 'ПИК', 'SMLT': 'Самолет', 'LSRG': 'ЛСР', 'ETLN': 'Эталон',
           'GLRX': 'GloraX', 'DOMRF': 'ДОМ.РФ'}
METRIC_MAP = {'Выручка': 'revenue', 'Операционная прибыль': 'op_profit',
              'EBITDA': 'ebitda', 'Чистая прибыль': 'net_profit',
              'Чистый долг': 'net_debt', 'Долг/EBITDA': 'netdebt_ebitda',
              'Капитал и резервы': 'equity', 'ROE': 'roe', 'ROA': 'roa',
              'Опер.денежный поток': 'ocf', 'CAPEX': 'capex', 'Активы': 'assets'}
METRIC_EN2RU = {v: k for k, v in METRIC_MAP.items()}

def fetch(url, retries=3):
    for a in range(retries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=25)
            return r.read().decode('utf-8', 'ignore')
        except Exception as e:
            print(f'  retry {a+1}: {str(e)[:60]}', flush=True)
            time.sleep(5 * (a + 1))
    return None

def clean(c):
    c = c.replace('\u2009', '').replace('\u00a0', '').replace(' ', '').replace('%', '')
    if c in ('', '?', '-', '—'):
        return None
    try:
        return float(c.replace(',', '.'))
    except ValueError:
        return None

def scrape_table(html_txt):
    """smart-lab financial page: <tr> header with periods, then <tr> metric rows."""
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.S)
    periods = None
    result = {}
    for row in rows:
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.S)
        cells = [re.sub(r'<[^>]+>', '', c).replace('&nbsp;', ' ').strip() for c in cells]
        cells = [c for c in cells if c != '']
        if not cells:
            continue
        if periods is None:
            cand = [c for c in cells if re.fullmatch(r'20[12]\d(?:Q[1-4])?', c)]
            if len(cand) >= 3:
                periods = cand
            continue
        c0 = re.sub(r'\s+', ' ', cells[0]).strip().rstrip(',')
        for ru, en in METRIC_MAP.items():
            if c0.startswith(ru):
                vals = [clean(c) for c in cells[1:]]
                pairs = list(zip(periods, vals))
                result[en] = {p: v for p, v in pairs if p and v is not None}
                break
    return result

def main():
    freq = 'Q' if '--quarterly' in sys.argv else 'Y'
    page = 'q' if freq == 'Q' else 'y'
    con = sqlite3.connect(DB)
    con.execute('''CREATE TABLE IF NOT EXISTS dev_ifrs (
        ticker TEXT, company TEXT, freq TEXT, period TEXT, metric TEXT,
        value REAL, source TEXT, loaded TEXT,
        PRIMARY KEY (ticker, freq, period, metric))''')
    total = 0
    for ticker, name in TICKERS.items():
        html = fetch(f'https://smart-lab.ru/q/{ticker}/f/{page}/')
        if html is None:
            print(f'{ticker}: fetch failed', flush=True)
            continue
        rows_out = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.S)
        periods = None
        data = {}
        for row in rows_out:
            cells = [re.sub(r'<[^>]+>', '', c).replace('&nbsp;', ' ').strip()
                     for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.S)]
            cells = [c for c in cells if c != '']
            if not cells:
                continue
            if periods is None:
                cand = [c for c in cells if re.fullmatch(r'20[12]\d(?:Q[1-4])?', c)]
                if len(cand) >= 3:
                    periods = cand
                continue
            c0 = re.sub(r'\s+', ' ', cells[0]).strip().rstrip(',')
            for ru, en in METRIC_MAP.items():
                if c0.startswith(ru):
                    vals = [clean(c) for c in cells[1:]]
                    data[en] = {p: v for p, v in zip(periods, vals) if p and v is not None}
                    break
        n = 0
        last_periods = []
        for metric_en, by_period in data.items():
            for period, val in by_period.items():
                con.execute('INSERT OR REPLACE INTO dev_ifrs VALUES (?,?,?,?,?,?,?,?)',
                            (ticker, name, freq, period, metric_en, val, 'smart-lab', '2026-09-01'))
                n += 1
            last_periods = sorted(by_period.keys())
        con.commit()
        print(f'{ticker} {freq}: {n} values, periods={last_periods}', flush=True)
        total += n
    con.close()
    print(f'TOTAL {total}')

if __name__ == '__main__':
    main()