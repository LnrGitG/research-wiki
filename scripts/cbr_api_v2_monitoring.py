#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cbr_api_v2_monitoring.py — инжест блока мониторинга ЦБ (pub25/28/29/30) + ПБ (pub8-12) в PG v2.

Источник: SQLite data/rosstat_construction.db (cbr_monitoring_api, 312 612 строк,
сдвиг уже применён: период = date - 2, dt = месяц опроса; размерные группы включены)
и живой API для ПБ (pub8-12, кварталы, период из dt, сдвиг 0).

Метрики: metric_code = 'cbrmon_' + slug(dataset) + '_q' + N + '_' + adj + ['_' + slug(group)]
adjustment в sub_dimension. Оценка (assessment): RAW = 'final', SA = 'estimated'? 
Нет: SA = 'final' тоже (это опубликованная ЦБ величина), различие в sub_dimension='sa'/'raw'.

Run-версионность: release 'cbr_api_monitoring_v2_2026-09'.
"""
import os, sqlite3, re, sys, json, ssl, urllib.request, datetime

def connect():
    import psycopg2
    return psycopg2.connect(host=os.environ.get('PGHOST','127.0.0.1'),
        port=int(os.environ.get('PGPORT','5432')),
        user=os.environ.get('PGUSER','wiki'), dbname=os.environ.get('PGDATABASE','research_wiki'))

BASE = 'https://www.cbr.ru/dataservice'
SOURCE_CBR = 7
REGION_RF = 1

SLUG = {}
def slug(s):
    if s not in SLUG:
        t = re.sub(r'[^a-zа-я0-9]+', '-', s.lower()).strip('-')
        # транслит
        tr = str.maketrans('абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                            'abvgdeejzziklmnoprstufhccssyieuya')
        t = t.translate(tr)
        SLUG[s] = t[:24]
    return SLUG[s]

QIDX = {}
def qnum(question):
    if question not in QIDX:
        QIDX[question] = len(QIDX) + 1
    return QIDX[question]

def month_end(iso):
    y, m = int(iso[:4]), int(iso[5:7])
    return (datetime.date(y + (m == 12), (m % 12) + 1, 1) - datetime.timedelta(days=1)).isoformat()

QUARTER = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
def parse_quarter(dt):
    m = re.match(r'(I{1,3}|IV) квартал (\d{4})', dt)
    if not m:
        return None
    q, y = QUARTER[m.group(1)], int(m.group(2))
    start = datetime.date(y, (q - 1) * 3 + 1, 1)
    end = (datetime.date(y + (q == 4), (q % 4) * 3 + 1, 1) - datetime.timedelta(days=1))
    return start.isoformat(), end.isoformat()

def get_json(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return json.loads(urllib.request.urlopen(req, timeout=120, context=ctx).read().decode('utf-8', 'ignore'))

def ensure_metric(cur, code, name_ru, unit_id, freq_id, description=''):
    cur.execute("SELECT metric_id FROM core.metric WHERE metric_code=%s", (code,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("""INSERT INTO core.metric (metric_code, name_ru, unit_id, frequency_id,
                   metric_type, status, description)
                   VALUES (%s,%s,%s,%s,'primary','active',%s) RETURNING metric_id""",
                (code, name_ru, unit_id, freq_id, description))
    return cur.fetchone()[0]

UNIT_MAP = {'млрд руб.': 10, 'млн руб.': 11, '%': 12, '% годовых': 12, 'пунктов': 13,
            'месяцев': 33, 'руб.': 38, 'млн долларов США': None, 'единиц': 17, 'число опрошенных': 17}
UNIT_NEEDED_NEW = {'млн долларов США': 'mln_usd'}

def ensure_units(cur, needed):
    for name in needed:
        if name in UNIT_NEEDED_NEW:
            cur.execute("SELECT unit_id FROM core.unit WHERE unit_code=%s", (UNIT_NEEDED_NEW[name],))
            if not cur.fetchone():
                cur.execute("INSERT INTO core.unit (unit_code, name_ru) VALUES (%s,%s) RETURNING unit_id",
                            (UNIT_NEEDED_NEW[name], name))

def main():
    sqlite_path = '/home/ubuntu/sandbox_datasets/rosstat_construction.db'
    if not os.path.exists(sqlite_path):
        sqlite_path = '/home/lnr/research-wiki-private/data/rosstat_construction.db'
    sconn = sqlite3.connect(sqlite_path)
    scon = connect()
    cur = scon.cursor()

    # release
    cur.execute("SELECT release_id FROM core.release WHERE source_id=%s AND release_label='cbr_api_monitoring_v2_2026-09'", (SOURCE_CBR,))
    row = cur.fetchone()
    if row:
        rel = row[0]
        print('release exists', rel)
    else:
        cur.execute("""INSERT INTO core.release (source_id, release_label, published_at, ingested_at, status, notes)
                       VALUES (%s,'cbr_api_monitoring_v2_2026-09', now(), now(), 'loaded',
                       %s) RETURNING release_id""", (SOURCE_CBR,
                       'Мониторинг ЦБ pub25/28/29/30: 22 сектора + размерные группы, RAW+SA; период=date-2 (dt=месяц опроса). ПБ pub8-12: квартал из dt.'))
        rel = cur.fetchone()[0]
    print('release', rel)

    # 1. Мониторинг из SQLite
    scur = sconn.cursor()
    scur.execute("SELECT DISTINCT unit FROM cbr_monitoring_api")
    ensure_units(cur, [r[0] for r in scur.fetchall()])
    scon.commit()

    scur.execute("SELECT dataset, size_group, adjustment, question, unit, period, value FROM cbr_monitoring_api")
    n = 0
    batch = []
    metric_cache = {}
    for dataset, grp, adj, question, unit, period, value in scur.fetchall():
        if value is None:
            continue
        code_parts = ['cbrmon', slug(dataset), 'q%d' % qnum(question)]
        sub = adj
        if grp != 'Экономика всего':
            code_parts.append(slug(grp))
            sub = sub + '|' + slug(grp)
        code = '_'.join(code_parts)
        freq = 3 if re.match(r'^\d{4}Q[1-4]$', period) else 5
        if code not in metric_cache:
            name = f'{dataset}: {question[:80]} [{adj}]' + (f' [{grp}]' if grp != 'Экономика всего' else '')
            unit_id = UNIT_MAP.get(unit)
            if unit_id is None:
                ensure_units(cur, [unit])
                cur.execute("SELECT unit_id FROM core.unit WHERE unit_code=%s", (UNIT_NEEDED_NEW.get(unit, unit),))
                urow = cur.fetchone()
                unit_id = urow[0] if urow else 18
            metric_cache[code] = (ensure_metric(cur, code, name, unit_id, freq,
                                                f'ЦБ мониторинг, pub25/28/29/30, {dataset}'), freq)
        mid, mf = metric_cache[code]
        if mf == 3:
            pq = parse_period_q(period)
            if pq is None: continue
            ps, pe = pq
        else:
            ps, pe = period, month_end(period)
        batch.append((mid, REGION_RF, mf, ps, pe, float(value), SOURCE_CBR, rel, sub))
        n += 1
        if len(batch) >= 5000:
            insert_obs(cur, batch)
            scon.commit()
            batch = []
            print('progress', n)
    if batch:
        insert_obs(cur, batch)
    scon.commit()
    print(f'мониторинг: {n} строк')

    # 2. Платёжный баланс из API (pub8-12)
    pb = [(8,9,'Сальдо счёта текущих операций'), (8,10,'Сальдо счёта операций с капиталом'),
          (8,11,'Сальдо финансового счёта'), (8,12,'Чистые ошибки и пропуски'),
          (9,13,'ПБ: товары'), (9,14,'ПБ: услуги'), (9,15,'ПБ: первичные доходы'),
          (9,16,'ПБ: вторичные доходы'), (10,17,'ПБ: непроизв. нефинансовые активы'),
          (10,18,'ПБ: капитальные трансферты'), (11,19,'ПБ: прямые инвестиции'),
          (11,20,'ПБ: портфельные инвестиции'), (11,21,'ПБ: производные ФИ'),
          (11,22,'ПБ: прочие инвестиции'), (11,23,'ПБ: резервные активы'), (12,24,'ПБ: ЧОП')]
    npb = 0
    for pub, ds, name in pb:
        d = get_json(f'{BASE}/data?y1=1994&y2=2026&datasetId={ds}&publicationId={pub}')
        units = {u['id']: u['val'] for u in d.get('units', [])}
        hdr = {h['id']: h['elname'] for h in d.get('headerData', [])}
        mid = None
        rows = []
        for r in d.get('RawData', []):
            if r.get('obs_val') is None: continue
            uval = units.get(r['unit_id'], '')
            if mid is None:
                unit_id = UNIT_MAP.get(uval)
                if unit_id is None:
                    ensure_units(cur, [uval])
                    cur.execute("SELECT unit_id FROM core.unit WHERE unit_code=%s", (UNIT_NEEDED_NEW.get(uval, uval),))
                    urow = cur.fetchone()
                    unit_id = urow[0] if urow else 18
                code = f'pb_ds{ds}'
                mid = ensure_metric(cur, code, name, unit_id, 6,
                                    f'ЦБ РФ, платёжный баланс pub{pub} ds{ds}')
            pq = parse_quarter(r['dt'])
            if pq is None: continue
            ps, pe = pq
            rows.append((mid, REGION_RF, 6, ps, pe, float(r['obs_val']), SOURCE_CBR, rel, ''))
        if rows:
            insert_obs_q(cur, rows)
            npb += len(rows)
    scon.commit()
    print(f'ПБ: {npb} строк')
    print(f'ИТОГО: {n + npb}, release {rel}')
    scon.close()
    sconn.close()

def freq_id_check(period):
    return 3 if re.match(r'^(I{1,3}|IV) квартал', period) else 5

def parse_period_q(period):
    m = re.match(r'^(\d{4})Q(\d)', period)
    if not m: return None
    y, q = int(m.group(1)), int(m.group(2))
    return (f'{y}-{(q-1)*3+1:02d}-01', month_end_quarter(y, q))

def month_end_quarter(y, q):
    return (datetime.date(y + (q == 4), (q % 4) * 3 + 1, 1) - datetime.timedelta(days=1)).isoformat()

def insert_obs(cur, rows):
    cur.executemany("""INSERT INTO core.observation_v2
        (metric_id, region_id, frequency_id, period_start, period_end, value,
         assessment_type, observation_status, source_id, release_id, quality_flags, sub_dimension)
        VALUES (%s,%s,%s,%s,%s,%s,'final','raw',%s,%s,'{}',%s)
        ON CONFLICT (metric_id, region_id, frequency_id, period_start, source_id,
                     release_id, assessment_type, sub_dimension) DO NOTHING""",
        rows)

def insert_obs_q(cur, rows):
    insert_obs(cur, rows)

if __name__ == '__main__':
    main()
