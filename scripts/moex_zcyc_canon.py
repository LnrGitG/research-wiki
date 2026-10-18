#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Кривая бескупонной доходности ОФЗ Мосбиржи: ISS API → канон напрямую.

Источник: ISS Московской Биржи, эндпоинт
`/iss/engines/stock/zcyc.json?date=YYYY-MM-DD` — отдаёт на дату ОДНУ строку
(последний пересчёт дня, время ~18:54) с тремя блоками:
  * yearyields — доходность нулевого купона по 11 фиксированным срокам
    (0.25, 0.5, 0.75, 1, 2, 3, 5, 7, 10, 15, 20 лет), % годовых;
  * params — параметры модели Нельсона — Сигеля — Свенссона
    (B1, B2, B3 в %, T1 в годах, G1..G9 безразмерные);
  * securities — эталонные выпуски ОФЗ, по которым строится кривая
    (цена закрытия в % от номинала, доходность, дюрация).

Почему так, а не через `/iss/history/engines/stock/zcyc.json`: исторический
эндпоинт отдаёт ВНУТРИДНЕВНЫЕ точки (≈20 100 строк на день) и игнорирует
`start`, то есть за 12 лет это сотни миллионов строк. Эндпоинт с `date`
даёт ровно одну точку в день при 7 КБ ответа — в 2000 раз меньше трафика
на ту же информацию.

Метрики канона (частота D, регион РФ, sub_dimension — разрез):
  moex__zcyc__yield        %,   sub = '0.25y' ... '20y'
  moex__zcyc__nss_b        %,   sub = 'b1','b2','b3'
  moex__zcyc__nss_tau      лет, sub = 't1'
  moex__zcyc__nss_g        коэф., sub = 'g1' ... 'g9'
  moex__zcyc__bench__yield %,   sub = <secid>  (эталонные выпуски)
  moex__zcyc__bench__price %,   sub = <secid>  (цена, % от номинала)

Идемпотентен: повторный прогон за тот же период не добавляет строк
(ON CONFLICT DO NOTHING по ux_observation + предснятие пары «метрика — релиз»).
Сырьё сохраняется помесячно в gzip-JSONL (data/moex_raw/) — по нему же
делается приёмка `--accept`.

Примеры:
  python3 scripts/moex_zcyc_canon.py --from 2014-01-01 --to 2026-10-18
  python3 scripts/moex_zcyc_canon.py --from 2026-10-01 --accept
  python3 scripts/moex_zcyc_canon.py --probe-start      # поиск первой даты
"""
import argparse
import datetime as dt
import gzip
import io
import json
import os
import ssl
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE = 'https://iss.moex.com/iss/engines/stock/zcyc.json'
UA = {'User-Agent': 'Mozilla/5.0 (research-wiki; +https://github.com/LnrGitG)'}
RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'moex_raw')
STATE = '/tmp/moex_zcyc_state.json'

TENORS = [0.25, 0.5, 0.75, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0]
UNIT_PCT, UNIT_YEARS, UNIT_RATIO = 12, 47, 37
FREQ_D = 4
RELEASE_LABEL = 'moex-zcyc-direct'

METRICS = {
    'moex__zcyc__yield': ('Доходность бескупонной кривой ОФЗ по срокам (модель Нельсона — Сигеля — Свенссона, Мосбиржа)',
                          UNIT_PCT),
    'moex__zcyc__nss_b': ('Параметры уровня кривой бескупонной доходности ОФЗ B1–B3 (NSS, Мосбиржа)', UNIT_PCT),
    'moex__zcyc__nss_tau': ('Параметр T1 кривой бескупонной доходности ОФЗ (NSS, Мосбиржа)', UNIT_YEARS),
    'moex__zcyc__nss_g': ('Параметры формы кривой бескупонной доходности ОФЗ G1–G9 (NSS, Мосбиржа)', UNIT_RATIO),
    'moex__zcyc__bench__yield': ('Доходность эталонных выпусков ОФЗ, используемых для построения кривой (Мосбиржа)',
                                 UNIT_PCT),
    'moex__zcyc__bench__price': ('Цена закрытия эталонных выпусков ОФЗ, % от номинала (Мосбиржа)', UNIT_PCT),
}

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def fetch(day, attempts=4):
    """JSON одного дня; None, если кривая в этот день не публиковалась."""
    url = '%s?date=%s&iss.meta=off' % (BASE, day)
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
                return json.loads(r.read().decode('utf-8', 'ignore'))
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError('ISS не ответил по %s: %s' % (day, last))


def parse(day, payload):
    """→ ([(metric_code, sub_dimension, value, unit_id)], meta) или (None, meta)."""
    yy = (payload.get('yearyields') or {}).get('data') or []
    pr = (payload.get('params') or {}).get('data') or []
    se = (payload.get('securities') or {}).get('data') or []
    if not yy:
        return None, {'date': day, 'tenors': 0, 'params': 0, 'bonds': 0, 'tradetime': None}
    col_p = (payload['params']['columns'] if 'columns' in payload['params'] else None) or []
    idx = {c.lower(): i for i, c in enumerate(col_p)}
    p = pr[0]
    rows = []
    for t, v in ((float(r[2]), r[3]) for r in yy):
        if v is None:
            continue
        rows.append(('moex__zcyc__yield', _tenor_label(t), float(v), UNIT_PCT))
    for k, code in (('b1', 'b1'), ('b2', 'b2'), ('b3', 'b3')):
        if idx.get(k) is not None and p[idx[k]] is not None:
            rows.append(('moex__zcyc__nss_b', code, float(p[idx[k]]), UNIT_PCT))
    if idx.get('t1') is not None and p[idx['t1']] is not None:
        rows.append(('moex__zcyc__nss_tau', 't1', float(p[idx['t1']]), UNIT_YEARS))
    for n in range(1, 10):
        k = 'g%d' % n
        if idx.get(k) is not None and p[idx[k]] is not None:
            rows.append(('moex__zcyc__nss_g', k, float(p[idx[k]]), UNIT_RATIO))
    cols = {c: i for i, c in enumerate((payload['securities'] or {}).get('columns') or [])}
    for r in se:
        sec = r[cols['secid']]
        for field, code in (('clcyield', 'moex__zcyc__bench__yield'), ('clcprice', 'moex__zcyc__bench__price')):
            i = cols.get(field)
            if i is not None and r[i] is not None:
                rows.append((code, sec, float(r[i]), UNIT_PCT))
    tradetime = p[idx['tradetime']] if idx.get('tradetime') is not None else None
    return rows, {'date': day, 'tenors': len(yy), 'params': 1, 'bonds': len(se), 'tradetime': tradetime}


def _tenor_label(t):
    return '%gy' % t


def raw_path(day):
    return os.path.join(RAW_DIR, 'zcyc_%s.jsonl.gz' % day[:7])


def save_raw(day, rows, meta):
    os.makedirs(RAW_DIR, exist_ok=True)
    path = raw_path(day)
    with gzip.open(path, 'at', encoding='utf-8') as f:
        f.write(json.dumps({'meta': meta, 'rows': rows}, ensure_ascii=False) + '\n')


def load_raw(month):
    path = os.path.join(RAW_DIR, 'zcyc_%s.jsonl.gz' % month)
    if not os.path.exists(path):
        return []
    out = []
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def weekdays(start, end):
    d = start
    while d <= end:
        if d.weekday() < 5:
            yield d
        d += dt.timedelta(days=1)


def collect(start, end, sleep=0.12, limit=None):
    rows, missing, done = [], [], 0
    for d in weekdays(start, end):
        day = d.isoformat()
        payload = fetch(day)
        parsed, meta = parse(day, payload)
        done += 1
        if parsed is None:
            missing.append(day)
            save_raw(day, [], meta)
        else:
            rows.extend((day, code, sub, val, unit) for code, sub, val, unit in parsed)
            save_raw(day, parsed, meta)
        if done % 200 == 0:
            print('  %s: дней %d, строк %d, пустых %d' % (day, done, len(rows), len(missing)), flush=True)
            json.dump({'last': day, 'days': done, 'rows': len(rows)}, open(STATE, 'w'))
        if limit and done >= limit:
            break
        time.sleep(sleep)
    return rows, missing, done


def write_canon(rows):
    """Запись в data.observation через COPY; возвращает (release_id, вставлено)."""
    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src = cur.execute("SELECT source_id FROM catalog.source WHERE source_code='moex'").fetchone()
            if src:
                src_id = src[0]
            else:
                src_id = cur.execute(
                    """INSERT INTO catalog.source (source_code,name_ru,url,publisher,reliability,is_active)
                       VALUES ('moex','Московская Биржа (ISS API)','https://iss.moex.com',
                               'ПАО Московская Биржа','official',true) RETURNING source_id""").fetchone()[0]
            rid_rf = cur.execute("SELECT region_id FROM catalog.region WHERE name_ru='Российская Федерация'").fetchone()[0]
            rel = cur.execute('SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s',
                              (src_id, RELEASE_LABEL)).fetchone()
            if rel:
                release_id = rel[0]
            else:
                release_id = cur.execute(
                    """INSERT INTO catalog.release (source_id,label,published_at,status,notes)
                       VALUES (%s,%s,now(),'loaded','кривая бескупонной доходности ОФЗ Мосбиржи: прямая загрузка ISS → канон')
                       RETURNING release_id""", (src_id, RELEASE_LABEL)).fetchone()[0]

            mids = {c: i for c, i in cur.execute(
                "SELECT metric_code, metric_id FROM catalog.metric WHERE metric_code LIKE 'moex__zcyc%'")}
            for code, (name, unit_id) in METRICS.items():
                if code in mids:
                    continue
                mids[code] = cur.execute(
                    """INSERT INTO catalog.metric (metric_code,name_ru,unit_id,source_id,frequency_id,
                           metric_type,is_derived,status,tags,description)
                       VALUES (%s,%s,%s,%s,%s,'primary',false,'active','{rates,ofz,yield_curve}',
                           'Мосбиржа, ISS API /iss/engines/stock/zcyc.json. Кривая бескупонной доходности ОФЗ '
                           'по модели Нельсона — Сигеля — Свенссона; точка дня — последний пересчёт торгового дня. '
                           'Разрез (sub_dimension) — срок в годах либо код параметра/выпуска.')
                       RETURNING metric_id""", (code, name, unit_id, src_id, FREQ_D)).fetchone()[0]
            conn.commit()

            obs = [(mids[code], rid_rf, day, FREQ_D, val, src_id, release_id, sub)
                   for day, code, sub, val, unit in rows if code in mids]
            if not obs:
                print('нет строк для записи: канон не тронут')
                return release_id, 0
            # предснятие пары «метрика — релиз» В ГРАНИЦАХ ОКНА прогона: идемпотентность
            # независимо от состава ключа, но без сноса более ранних дней того же релиза
            day_min, day_max = min(x[2] for x in obs), max(x[2] for x in obs)
            cur.execute("""DELETE FROM data.observation o USING unnest(%s::int[]) m
                           WHERE o.metric_id = m AND o.release_id = %s
                             AND o.period_start BETWEEN %s AND %s""",
                        (sorted(set(x[0] for x in obs)), release_id, day_min, day_max))
            cur.execute('DROP TABLE IF EXISTS _tmp_moex_zcyc')
            cur.execute('CREATE TEMP TABLE _tmp_moex_zcyc (metric_id int, region_id int, period_start date, '
                        'frequency_id int, value numeric, source_id int, release_id int, sub_dimension text)')
            buf = io.StringIO()
            for mid, rid, day, fr, val, sid, rls, sub in obs:
                buf.write('\t'.join(map(str, (mid, rid, day, fr, val, sid, rls, sub))) + '\n')
            buf.seek(0)
            with cur.copy('COPY _tmp_moex_zcyc FROM STDIN') as cp:
                cp.write(buf.read())
            cur.execute("""INSERT INTO data.observation
                (metric_id,region_id,period_start,period_end,frequency_id,value,assessment_type,
                 observation_status,source_id,release_id,sub_dimension)
                SELECT metric_id,region_id,period_start,period_start,frequency_id,value,'final',
                       'validated',source_id,release_id,sub_dimension FROM _tmp_moex_zcyc
                ON CONFLICT (metric_id,region_id,period_start,frequency_id,assessment_type,
                             sub_dimension,release_id) DO NOTHING""")
            cur.execute('DROP TABLE _tmp_moex_zcyc')
            conn.commit()
            n = cur.execute('SELECT count(*) FROM data.observation WHERE release_id=%s', (release_id,)).fetchone()[0]
    return release_id, n


def accept(start, end):
    """Приёмка: сверка канона с СОХРАНЁННЫМ сырьём по (дата, метрика, разрез)."""
    months = sorted({'%04d-%02d' % (d.year, d.month) for d in weekdays(start, end)})
    raw = []
    for m in months:
        raw.extend(load_raw(m))
    want = {}
    for rec in raw:
        day, rows = rec['meta']['date'], rec['rows']
        if not (start.isoformat() <= day <= end.isoformat()):
            continue
        for code, sub, val, _unit in rows:
            want[(dt.date.fromisoformat(day), code, sub)] = float(val)
    with db_tunnel.connect() as conn, conn.cursor() as cur:
        got = {(r[0], r[1], r[2]): float(r[3]) for r in cur.execute("""
            SELECT o.period_start, m.metric_code, o.sub_dimension, o.value
            FROM data.observation o JOIN catalog.metric m ON m.metric_id=o.metric_id
            WHERE m.metric_code LIKE 'moex__zcyc%%' AND o.period_start BETWEEN %s AND %s""",
            (start, end))}
    diff = [(k, want.get(k), got.get(k)) for k in set(want) | set(got)
            if abs((want.get(k) or 0) - (got.get(k) or 0)) > 1e-9]
    print('приёмка %s..%s: в сырье %d, в каноне %d, расхождений %d'
          % (start, end, len(want), len(got), len(diff)))
    for k, w, g in diff[:10]:
        print('   ', k, 'сырьё', w, 'канон', g)
    return len(diff)


def probe_start():
    d = dt.date(2013, 9, 1)
    first = None
    while d <= dt.date(2014, 2, 1):
        if d.weekday() < 5:
            payload = fetch(d.isoformat())
            parsed, _ = parse(d.isoformat(), payload)
            if parsed:
                first = d
                break
            time.sleep(0.1)
        d += dt.timedelta(days=1)
    print('первая дата с кривой:', first)
    return first


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='start')
    ap.add_argument('--to', dest='end')
    ap.add_argument('--sleep', type=float, default=0.12)
    ap.add_argument('--limit', type=int)
    ap.add_argument('--no-write', action='store_true')
    ap.add_argument('--accept', action='store_true')
    ap.add_argument('--probe-start', action='store_true')
    a = ap.parse_args()

    if a.probe_start:
        probe_start()
        return
    end = dt.date.fromisoformat(a.end) if a.end else dt.date.today()
    start = dt.date.fromisoformat(a.start) if a.start else end - dt.timedelta(days=10)
    if a.accept:
        accept(start, end)
        return
    print('сбор кривой ОФЗ %s..%s' % (start, end), flush=True)
    rows, missing, done = collect(start, end, sleep=a.sleep, limit=a.limit)
    print('дней %d | строк %d | дней без кривой %d' % (done, len(rows), len(missing)))
    if missing:
        print('  пустые:', ', '.join(missing[:10]), '…' if len(missing) > 10 else '')
    if a.no_write:
        print('режим без записи: канон не тронут')
        return
    release_id, n = write_canon(rows)
    print('release_id=%s | наблюдений в релизе: %d' % (release_id, n))
    accept(start, end)


if __name__ == '__main__':
    main()
