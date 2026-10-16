#!/usr/bin/env python3
"""Прямой загрузчик МСФО/РСБУ девелоперов: smart-lab.ru → сырьё + канон.

Заменяет прежнюю дорогу «HTML → SQLite-лендинг data/developers_ifrs.db →
инжест рубежа 6» (метрики «МСФО девелоперов: <metric>», релиз `smart-lab`).
Загрузчик сам ходит за страницами `/q/<TICKER>/f/{y,q}/`, кладёт снимок
в raw/smartlab/ifrs/ (сырьё сохраняется для аудита) и пишет в канон.

Ключевые отличия от прежней дороги:

1. Частота. Рубеж 6 помечал все строки квартальной частотой (frequency_id 6),
   включая годовые ряды 2021–2025; здесь годовые идут частотой A,
   квартальные — Q.
2. Ключ итерации. Прежний путь писал в лендинг с `INSERT OR REPLACE`, а в канон
   попадал один раз; здесь перед вставкой снимаются строки пары
   «метрика — релиз» (в ux_observation входит sub_dimension, а NULL-ы Postgres
   считает различными — при пустом подразрезе уникальность не работает).
3. Сырьё. Прежний сборщик не оставлял исходного HTML/разбора — только строки
   лендинга; здесь снимок разбора сохраняется в raw/smartlab/ifrs/.

Запуск:
    python3 scripts/direct_smartlab.py                   # сбор + сухой прогон
    APPLY=1 python3 scripts/direct_smartlab.py           # запись
    APPLY=1 REPLACE=1 python3 scripts/direct_smartlab.py # со снятием прежних строк

Точка возврата: attic/smartlab_before_ifrs.csv.gz (в режиме REPLACE).
"""
import gzip
import io
import json
import os
import re
import sys
import time
import urllib.request

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(REPO, 'raw', 'smartlab', 'ifrs')
APPLY = os.environ.get('APPLY') == '1'
REPLACE = os.environ.get('REPLACE') == '1'
SOURCE = 'smartlab'
# Метка прежней дороги: релиз `smart-lab` уже держит строки группы, и переиспользование
# метки избавляет от переноса строк между релизами (release_id входит в уникальный ключ).
RELEASE = 'smart-lab'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0'

TICKERS = {'PIKK': 'ПИК', 'SMLT': 'Самолет', 'LSRG': 'ЛСР', 'ETLN': 'Эталон',
           'GLRX': 'GloraX', 'DOMRF': 'ДОМ.РФ'}
# русское название строки на странице → код метрики канона
METRIC_MAP = {'Выручка': 'revenue', 'Операционная прибыль': 'op_profit',
              'EBITDA': 'ebitda', 'Чистая прибыль': 'net_profit',
              'Чистый долг': 'net_debt', 'Долг/EBITDA': 'netdebt_ebitda',
              'Капитал и резервы': 'equity', 'ROE': 'roe', 'ROA': 'roa',
              'Опер.денежный поток': 'ocf', 'CAPEX': 'capex', 'Активы': 'assets'}
METRIC_NAMES = {en: 'МСФО девелоперов: %s' % en for en in METRIC_MAP.values()}

PERIOD_RE = re.compile(r'20[12]\d(?:Q[1-4])?')
QM = {'Q1': 1, 'Q2': 4, 'Q3': 7, 'Q4': 10}


def fetch(url, retries=3):
    last = None
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.read().decode('utf-8', 'ignore')
        except Exception as e:            # сеть/гео/лимит — пауза и повтор
            last = e
            print('  retry %d: %s' % (a + 1, str(e)[:60]), flush=True)
            time.sleep(5 * (a + 1))
    print('  сбой запроса: %s (%s)' % (url, last))
    return None


def num(c):
    c = (c.replace('\u2009', '').replace('\u00a0', '').replace(' ', '')
          .replace('%', '').strip())
    if c in ('', '?', '-', '—'):
        return None
    try:
        return float(c.replace(',', '.'))
    except ValueError:
        return None


def parse_page(html):
    """Страница /q/<TICKER>/f/{y,q}/: позиционная сетка таблицы.

    Разбор идёт по НОМЕРАМ СТОЛБЦОВ, а не по последовательности непустых ячеек.
    Таблица smart-lab широкая: у части строк значения идут через пустую ячейку
    (полугодовые отчётности), плюс есть столбцы-иконки и столбец LTM. Прежний
    разбор отбрасывал пустые ячейки и сдвигал значения на столбец влево, а LTM
    попадал в последний квартал окна (LSRG: 96.4 записывалось в 2025Q3 вместо
    2025Q2, 252.8 — в 2026Q2 вместо LTM). pandas раскрывает colspan/rowspan и
    сохраняет пустые позиции, поэтому столбцы периодов и значений совпадают.
    """
    tabs = pd.read_html(io.StringIO(html), header=None)
    if not tabs:
        return [], {}
    tab = max(tabs, key=lambda t: t.shape[0])
    periods, pcols, out = [], None, {}
    for _, row in tab.iterrows():
        cells = [' ' if (isinstance(c, float) and pd.isna(c)) else re.sub(r'\s+', ' ', str(c)).strip()
                 for c in row]
        if pcols is None:
            idx = [i for i, c in enumerate(cells) if PERIOD_RE.fullmatch(c)]
            if len(idx) >= 3:
                pcols = idx
                periods = [cells[i] for i in idx]
            continue
        label = cells[0].strip().rstrip(',')
        for ru, en in METRIC_MAP.items():
            if label.startswith(ru):
                vals = [num(cells[i]) if i < len(cells) else None for i in pcols]
                out[en] = {p: v for p, v in zip(periods, vals) if v is not None}
                break
    return periods, out


def ps_from_period(p):
    """'2025' → (2025, 0); '2025Q2' → (2025, 4)."""
    m = re.match(r'^(20[12]\d)(?:Q([1-4]))?$', str(p))
    if not m:
        return None
    y = int(m.group(1))
    return (y, QM['Q%s' % m.group(2)]) if m.group(2) else (y, 0)


def collect():
    """Обход страниц: (rows для канона, снимок разбора, счётчики)."""
    rows, snapshots = [], {}
    stats = {'ok': 0, 'failed': [], 'periods': {}}
    for ticker, company in TICKERS.items():
        for freq, page in (('Y', 'y'), ('Q', 'q')):
            html = fetch('https://smart-lab.ru/q/%s/f/%s/' % (ticker, page))
            if html is None:
                stats['failed'].append('%s/%s' % (ticker, freq))
                continue
            periods, data = parse_page(html)
            if not data:
                stats['failed'].append('%s/%s (пустой разбор)' % (ticker, freq))
                continue
            stats['ok'] += 1
            stats['periods']['%s/%s' % (ticker, freq)] = periods
            snapshots['%s_%s' % (ticker, freq)] = {
                'ticker': ticker, 'company': company, 'freq': freq,
                'periods': periods, 'html': html,
                'data': {en: {p: v for p, v in by_p.items()}
                         for en, by_p in data.items()},
            }
            for en, by_period in data.items():
                for p, v in by_period.items():
                    ps = ps_from_period(p)
                    if ps is None:
                        continue
                    rows.append(dict(
                        metric_name=METRIC_NAMES[en], value=v, ps=ps,
                        region=None, freq=('A' if freq == 'Y' else 'Q'),
                        source=SOURCE, release=RELEASE,
                        sub='company: %s | ticker: %s | freq: %s | metric: %s'
                            % (company, ticker, freq, en),
                        unit='unknown'))
    return rows, snapshots, stats


def ps_lo(ps):
    """(2025, 0) → 2025-01-01; (2025, 4) → 2025-04-01."""
    y, m = ps
    return '%04d-01-01' % y if m == 0 else '%04d-%02d-01' % (y, m)


def ps_hi(ps):
    """Верхняя граница периода наблюдения: год → 31.12, квартал → конец квартала."""
    y, m = ps
    return '%04d-12-31' % y if m == 0 else '%04d-%02d-30' % (y, m + 2)


def source_windows(stats):
    """Окно периодов источника по каждому тикеру и частоте: (компания, тикер, частота, min, max).

    Прежний разбор сдвигал значения на столбец, поэтому внутри окна часть строк
    заполнена там, где источник даёт пустую ячейку (двойник «96.4» у ЛСР: и
    2025Q2, и 2025Q3). Привести окно к источнику целиком можно только снятием
    всех строк компании-частоты в границах окна; периоды ВНЕ окна не трогаются —
    восстановить их из источника уже нельзя, а снос потерял бы историю.
    """
    out = []
    for key, periods in sorted(stats['periods'].items()):
        ticker, freq = key.split('/')
        ps = [ps_from_period(p) for p in periods]
        ps = [p for p in ps if p]
        if ps:
            out.append((TICKERS[ticker], ticker, freq,
                        ps_lo(min(ps)), ps_hi(max(ps))))
    return out


def main():
    rows, snapshots, stats = collect()
    print('== собрано: страниц %d | сбоев %d %s'
          % (stats['ok'], len(stats['failed']), stats['failed'] or ''))
    for k, v in sorted(stats['periods'].items()):
        print('   %-12s периоды %s … %s' % (k, v[0] if v else '—', v[-1] if v else '—'))
    print('== строк для канона: %d' % len(rows))
    if APPLY and snapshots:
        os.makedirs(RAW_DIR, exist_ok=True)
        stamp = time.strftime('%Y-%m-%d')
        for key, snap in snapshots.items():
            base = os.path.join(RAW_DIR, '%s_%s' % (key.lower(), stamp))
            with gzip.open(base + '.html.gz', 'wt', encoding='utf-8') as f:
                f.write(snap.pop('html') or '')
            with open(base + '.json', 'w', encoding='utf-8') as f:
                json.dump(snap, f, ensure_ascii=False, indent=2)
        print('   снимки сырья: %s (%d страниц, JSON + исходный HTML)'
              % (RAW_DIR, len(snapshots)))
    if not rows:
        raise SystemExit('нечего загружать — сеть или разметка страниц сломались')

    w = Writer(tag='direct_smartlab', simulate=not APPLY)
    names = sorted(METRIC_NAMES.values())
    if REPLACE:
        # только дамп (без снятия): источник отдаёт скользящее окно, и часть
        # прежних периодов в окно уже не попадает — сносить её нельзя
        dump = os.path.join(REPO, 'attic', 'smartlab_before_ifrs.csv.gz')
        n = w.dump_group(names, dump, delete=False)
        print('   точка возврата: %d строк → %s' % (n, dump))
        # годовым строкам прежней дороги выставлена квартальная частота — правим
        a = w.freq['A']
        w.cur.execute("""UPDATE data.observation o SET frequency_id=%s
            FROM catalog.metric m WHERE m.metric_id=o.metric_id
              AND m.name_ru = ANY(%s) AND o.sub_dimension LIKE '%%freq: Y%%'
              AND o.frequency_id <> %s""", (a, names, a))
        print('   годовым строкам выставлена частота A: %d' % w.cur.rowcount)
        w.conn.commit()
    if not APPLY:
        for c, tk, f, lo, hi in source_windows(stats):
            print('   окно %s/%s: %s … %s' % (tk, f, lo, hi))
        print('   СУХОЙ ПРОГОН (APPLY=1 — запись)')
        w.close()
        return
    # окно источника приводится к источнику: снимаются все строки компании-частоты
    # в границах окна, включая те, где прежний сдвиг заполнил пустую ячейку
    rel = w.ensure_release(SOURCE, RELEASE)
    wiped = 0
    for company, ticker, freq, lo, hi in source_windows(stats):
        w.cur.execute("""DELETE FROM data.observation o USING catalog.metric m
            WHERE m.metric_id = o.metric_id AND m.name_ru = ANY(%s)
              AND o.release_id = %s AND o.sub_dimension LIKE %s
              AND o.period_start BETWEEN %s AND %s""",
                      (names, rel, 'company: %s | ticker: %s | freq: %s | metric:%%'
                       % (company, ticker, freq), lo, hi))
        wiped += w.cur.rowcount
    w.conn.commit()
    print('   окно источника снято под перезапись: %d строк' % wiped)
    prep, ins, conf, newm = w.ingest(rows, group='smartlab_ifrs')
    print('   подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, newm))
    w.close()


if __name__ == '__main__':
    main()
