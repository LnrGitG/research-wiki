#!/usr/bin/env python3
"""Загрузчик инфляционных ожиданий населения (inFOM) с сайта Банка России.

Рациональный путь: не 125 месячных файлов, а ОДИН — последний по времени, у
которого есть лист «Данные за все годы» (163 опроса, декабрь 2009 — сентябрь
2026). История в нём уже ревизована источником: это текущий винтаж, а не
первая публикация, поэтому провенанс фиксируется меткой файла.

Источник: https://www.cbr.ru/statistics/ddkp/inflationary_expectations/
Формат: xlsx, лист «Данные за все годы»; шапка — строка с датами опросов,
ряды — блоки «медианные значения» с подписями «наблюдаемая инфляция (в %)»,
«ожидаемая инфляция (в %)» (годовая и пятилетняя, всего и по группам
сбережений).

Разбор идёт по ПОДПИСЯМ блоков, а не по номерам строк: номера смещаются
между выпусками.

Запись — в канон (catalog/data через обновляемые представления core.*),
релиз на файл, снятие окна по паре «метрика — релиз» перед вставкой.

Запуск:
  python3 scripts/cbr_infom_canon.py --fetch      # скачать последний файл
  python3 scripts/cbr_infom_canon.py --parse      # разобрать сохранённое сырьё
  python3 scripts/cbr_infom_canon.py --load       # записать в канон
  python3 scripts/cbr_infom_canon.py --all        # всё подряд (по умолчанию)
  python3 scripts/cbr_infom_canon.py --verify     # сверка канона со снимком
"""
import argparse
import datetime as dt
import json
import os
import re
import ssl
import sys
import unicodedata
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = 'https://www.cbr.ru/statistics/ddkp/inflationary_expectations/'
RAW_DIR = os.path.join(REPO, 'raw/cbr/infom')
SNAP = os.path.join(RAW_DIR, 'parse_snapshot.json')
SOURCE_ID = 7          # catalog.source: cbr, «Банк России»
FREQ_M = 5             # catalog.frequency: M, месячная
UNIT_PCT = 12          # catalog.unit: pct, %
REGION_RU = 1

# (код метрики, подпись ряда, блок, подразрез)
SERIES = [
    ('infom_observed_median_m', 'наблюдаемая инфляция (в %)', 'год', 'median',
     'Инфляция, наблюдаемая населением, медиана, %'),
    ('infom_expected_1y_median_m', 'ожидаемая инфляция (в %)', 'год', 'median',
     'Инфляционные ожидания населения на год вперёд, медиана, %'),
    ('infom_observed_savers_m', 'наблюдаемая инфляция среди тех, кто имеет сбережения (в %)', 'год', 'savers',
     'Наблюдаемая инфляция, имеющие сбережения, медиана, %'),
    ('infom_observed_nonsavers_m', 'наблюдаемая инфляция среди тех, кто не имеет сбережений (в %)', 'год', 'nonsavers',
     'Наблюдаемая инфляция, не имеющие сбережений, медиана, %'),
    ('infom_expected_1y_savers_m', 'ожидаемая инфляция среди тех, кто имеет сбережения (в %)', 'год', 'savers',
     'Ожидания на год, имеющие сбережения, медиана, %'),
    ('infom_expected_1y_nonsavers_m', 'ожидаемая инфляция среди тех, кто не имеет сбережений (в %)', 'год', 'nonsavers',
     'Ожидания на год, не имеющие сбережений, медиана, %'),
    ('infom_expected_5y_median_m', 'ожидаемая инфляция (в %)', '5лет', 'median',
     'Инфляционные ожидания населения на 5 лет, медиана, %'),
    ('infom_expected_5y_savers_m', 'ожидаемая инфляция среди тех, кто имеет сбережения (в %)', '5лет', 'savers',
     'Ожидания на 5 лет, имеющие сбережения, медиана, %'),
    ('infom_expected_5y_nonsavers_m', 'ожидаемая инфляция среди тех, кто не имеет сбережений (в %)', '5лет', 'nonsavers',
     'Ожидания на 5 лет, не имеющие сбережений, медиана, %'),
]


def norm(s):
    s = unicodedata.normalize('NFKC', str(s)).lower().replace('ё', 'е')
    return re.sub(r'\s+', ' ', s).strip()


# ---------------------------------------------------------------- сбор сырья
def latest_link(html):
    """Последний по месяцу файл: stat_Infl_exp_YY-MM.xlsx или Infl_exp_YY-MM.xlsx."""
    pat = re.compile(r'/Collection/Collection/File/\d+/(?:stat_)?[Ii]nfl_exp_(\d{2})-(\d{2})\.xlsx')
    best = None
    for m in pat.finditer(html):
        y, mo = int(m.group(1)), int(m.group(2))
        if not (1 <= mo <= 12) or y > 40:
            continue
        if best is None or (y, mo) > best[0]:
            best = ((y, mo), m.group(0))
    if best is None:
        raise RuntimeError('на странице не найдено ни одного файла Infl_exp_YY-MM.xlsx')
    return best[0], 'https://www.cbr.ru' + best[1]


def fetch():
    os.makedirs(RAW_DIR, exist_ok=True)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(PAGE, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
                html = r.read().decode('utf-8', 'replace')
            break
        except Exception as e:                                  # noqa: BLE001
            if attempt == 3:
                raise
            print('  повтор страницы (%s)' % e)
    (ym, url) = latest_link(html)
    name = url.rsplit('/', 1)[-1]
    dst = os.path.join(RAW_DIR, name)
    if os.path.exists(dst) and os.path.getsize(dst) > 10000:
        print('уже скачан: %s (%d байт)' % (name, os.path.getsize(dst)))
        return dst, ym, url
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
                blob = r.read()
            break
        except Exception as e:                                  # noqa: BLE001
            if attempt == 3:
                raise
            print('  повтор файла (%s)' % e)
    if blob[:2] != b'PK':
        raise RuntimeError('скачанный файл не xlsx (нет сигнатуры PK)')
    with open(dst, 'wb') as f:
        f.write(blob)
    print('скачано: %s (%d байт), выпуск 20%02d-%02d' % (name, len(blob), ym[0], ym[1]))
    return dst, ym, url


# ------------------------------------------------------------------- разбор
def parse(path):
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    if 'Данные за все годы' not in wb.sheetnames:
        raise RuntimeError('в файле нет листа «Данные за все годы» — сменился формат')
    ws = wb['Данные за все годы']
    rows = list(ws.iter_rows(max_row=1400, max_col=200, values_only=True))

    hdr_i = None
    for i, r in enumerate(rows[:8]):
        if sum(1 for c in r[1:] if isinstance(c, dt.datetime)) >= 50:
            hdr_i = i
            break
    if hdr_i is None:
        raise RuntimeError('не найдена строка шапки с датами опросов')
    dates = {j: c.date() for j, c in enumerate(rows[hdr_i]) if isinstance(c, dt.datetime)}

    out, block = [], ''
    pending = {}                     # (нормированная подпись, блок) -> код
    for code, label, blk, sub, _nm in SERIES:
        pending[(norm(label), blk)] = (code, sub)

    for r in rows[hdr_i + 1:]:
        lab = norm(r[0]) if r[0] else ''
        if not lab:
            continue
        if 'медианн' in lab and 'значени' in lab:
            block = '5лет' if 'пятилетн' in lab else ('год' if 'годов' in lab else block)
            continue
        key = (lab, block)
        if key not in pending:
            continue
        code, sub = pending[key]
        for j, d in dates.items():
            v = r[j] if j < len(r) else None
            if isinstance(v, (int, float)):
                out.append({'metric': code, 'sub': sub, 'period': d.isoformat(),
                            'value': float(v)})
        pending.pop(key)

    missing = [c for c, *_ in SERIES if c not in {o['metric'] for o in out}]
    if missing:
        raise RuntimeError('не найдены ряды: %s — формат файла изменился' % ', '.join(missing))

    periods = sorted({o['period'] for o in out})
    return {'source_file': os.path.basename(path), 'periods': len(periods),
            'first': periods[0], 'last': periods[-1], 'rows': out}


# ------------------------------------------------------------------- запись
def ensure_metric(cur, code, name, desc):
    cur.execute("select metric_id from core.metric where metric_code=%s", (code,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""insert into core.metric (metric_code, name_ru, description, frequency_id,
                     unit_id, metric_type, is_derived, status)
                   values (%s, %s, %s, %s, %s, 'primary', false, 'active')
                   returning metric_id""", (code, name[:200], desc, FREQ_M, UNIT_PCT))
    return cur.fetchone()[0]


def ensure_release(cur, label, published):
    cur.execute("select release_id from core.release where release_label=%s", (label,))
    r = cur.fetchone()
    if r:
        cur.execute("update core.release set published_at=%s where release_id=%s", (published, r[0]))
        return r[0]
    cur.execute("""insert into core.release (source_id, release_label, published_at, status)
                   values (%s, %s, %s, 'registered') returning release_id""",
                (SOURCE_ID, label, published))
    return cur.fetchone()[0]


def month_end(ym):
    y, m = 2000 + ym[0], ym[1]
    nxt = dt.date(y + (m == 12), 1 if m == 12 else m + 1, 1)
    return nxt - dt.timedelta(days=1)


def load(conn, snap, ym):
    cur = conn.cursor()
    label = 'cbr_infom_expectations_20%02d-%02d' % ym
    rel = ensure_release(cur, label, month_end(ym))
    ids = {}
    for code, _l, _b, sub, name in SERIES:
        ids[code] = ensure_metric(cur, code, name,
                                  'inFOM (опрос населения для Банка России), медиана; '
                                  'cbr.ru/statistics/ddkp/inflationary_expectations, '
                                  'лист «Данные за все годы», файл %s' % snap['source_file'])
    cur.execute("""delete from core.observation_v2
                   where release_id=%s and metric_id = any(%s)""",
                (rel, list(ids.values())))
    cleaned = cur.rowcount
    n = 0
    for o in snap['rows']:
        cur.execute("""insert into core.observation_v2
                         (metric_id, region_id, frequency_id, period_start, period_end, value,
                          assessment_type, observation_status, source_id, release_id, sub_dimension)
                       values (%s, %s, %s, %s, %s, %s, 'final', 'raw', %s, %s, %s)""",
                    (ids[o['metric']], REGION_RU, FREQ_M, o['period'], o['period'],
                     o['value'], SOURCE_ID, rel, o['sub']))
        n += 1
    cur.execute("update core.release set status='loaded' where release_id=%s", (rel,))
    conn.commit()
    print('релиз %s: снято %d строк, вставлено %d' % (label, cleaned, n))
    return label


def verify(conn, snap):
    cur = conn.cursor()
    cur.execute("""select m.metric_code, o.period_start::text, o.value
                   from data.observation o
                   join catalog.metric m on m.metric_id = o.metric_id
                   where m.metric_code like 'infom%%'""")
    canon = {(c, p): float(v) for c, p, v in cur.fetchall()}
    src = {(o['metric'], o['period']): o['value'] for o in snap['rows']}
    miss = [k for k in src if k not in canon]
    bad = [(k, src[k], canon[k]) for k in src if k in canon and abs(src[k] - canon[k]) > 1e-9]
    extra = [k for k in canon if k not in src]
    print('сверка: источник %d, канон %d, расхождений %d, пропущено %d, лишних %d'
          % (len(src), len(canon), len(bad), len(miss), len(extra)))
    for k, a, b in bad[:5]:
        print('  расхождение %s: источник %s, канон %s' % (k, a, b))
    for k in miss[:5]:
        print('  пропуск %s' % (k,))
    return not miss and not bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fetch', action='store_true')
    ap.add_argument('--parse', action='store_true')
    ap.add_argument('--load', action='store_true')
    ap.add_argument('--verify', action='store_true')
    ap.add_argument('--all', action='store_true')
    a = ap.parse_args()
    if not any((a.fetch, a.parse, a.load, a.verify, a.all)):
        a.all = True

    path = SNAP
    ym = None
    if a.fetch or a.all:
        path, ym, url = fetch()
    if a.parse or a.all:
        if not os.path.exists(path):
            raise SystemExit('нет сырья: сначала --fetch')
        snap = parse(path)
        with open(SNAP, 'w') as f:
            json.dump(snap, f, ensure_ascii=False, indent=1)
        print('разобрано: %d точек, %d периодов, %s .. %s -> %s'
              % (len(snap['rows']), snap['periods'], snap['first'], snap['last'],
                 os.path.basename(SNAP)))
    else:
        with open(SNAP) as f:
            snap = json.load(f)

    if ym is None:
        m = re.search(r'(\d{2})-(\d{2})', snap['source_file'])
        ym = (int(m.group(1)), int(m.group(2))) if m else (26, 9)

    import db_tunnel
    conn = db_tunnel.connect()
    if a.load or a.all:
        load(conn, snap, ym)
    if a.verify or a.all:
        ok = verify(conn, snap)
        conn.close()
        sys.exit(0 if ok else 1)
    conn.close()


if __name__ == '__main__':
    main()
