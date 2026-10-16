#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Мониторинг предприятий ЦБ: API/XLSX → канон напрямую (без SQLite-лендинга).

Заменяет связку cbr_monitoring_all_collect.py (SQLite rosstat_construction.db) +
transfer_cbr_monitoring.py (мост из SQLite в канон). Коды метрик, слаг, единицы и
частота берутся ИЗ transfer_cbr_monitoring.py (импортом), чтобы загрузчик писал в
те же метрики, а не плодил дубли.

Конвенция (из моста): код cbrmon__<dataset>__<size_group>__<adjustment>__<question>,
регион — РФ (сектор живёт в коде метрики), sub_dimension='', частоты M=5 / Q=6,
единицы: 'пунктов'→37 (ratio), '%'→12.

Датировка: месячные — API date минус 2 месяца; квартальные — по dt.

Идемпотентен. Точка возврата: DELETE data.observation по release_id + метрики cbrmon_.
"""
import datetime as dt
import io
import json
import os
import re
import ssl
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

# --- конвенция кодов/единиц (перенесена из transfer_cbr_monitoring.py, мост удалён) ---
UNIT_MAP = {'пунктов': 37, '%': 12}   # ratio = 37 (пункты индикатора), pct = 12
FREQ_M, FREQ_Q = 5, 6
SLUG_TRANS = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
    'я': 'ya',
}


def slug(s, maxlen=60):
    import unicodedata
    s = unicodedata.normalize('NFKC', s).strip().lower().replace('ё', 'е').replace('\xa0', ' ')
    s = ''.join(SLUG_TRANS.get(ch, ch) for ch in s)
    s = re.sub(r'[^a-z0-9]+', '_', s).strip('_')
    return s[:maxlen].rstrip('_')


def period_mq(p):
    """(period_start, freq_id) из '2002-01-01' | '2002Q1'."""
    if re.fullmatch(r'\d{4}Q[1-4]', p):
        y, q = int(p[:4]), int(p[5])
        return dt.date(y, 3 * (q - 1) + 1, 1).isoformat(), FREQ_Q
    y, m, d = map(int, p.split('-'))
    return dt.date(y, m, 1).isoformat(), FREQ_M

try:
    from openpyxl import load_workbook
except ImportError:  # pragma: no cover
    load_workbook = None

BASE = 'https://www.cbr.ru/dataservice'
FACTORS_XLSX = 'https://www.cbr.ru/Content/Document/File/194116/mp_survey_data_facts.xlsx'
RELEASE_LABEL = os.environ.get('CBR_MON_RELEASE', 'cbr-monitoring direct 2026-10-16')

SCOPE = [
    (25, list(range(58, 80)) + [140]),
    (28, [80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119]),
    (29, [81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120]),
    (30, [82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118, 121]),
]
MEASURES = [(118, 'Исходные данные'), (119, 'Сезонно скорректированные данные')]
GROUP_NAME = {28: 'Крупные', 29: 'Средние', 30: 'Малые и микро'}
QUART_RE = re.compile(r'(I{1,3}|IV)\s+квартал\s+(\d{4})')
QUART_NUM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}


def get_json(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return json.loads(urllib.request.urlopen(req, timeout=120, context=ctx).read().decode('utf-8', 'ignore'))


def period_str(r):
    """Период как в SQLite-лендинге: месячные 'YYYY-MM-01' (сдвиг -2), квартальные 'YYYYQn'."""
    dtt = (r.get('dt') or '').strip()
    mq = QUART_RE.match(dtt)
    if mq:
        return '%sQ%d' % (mq.group(2), QUART_NUM[mq.group(1)])
    y, m = int(r['date'][:4]), int(r['date'][5:7])
    m2, y2 = (m - 2, y) if m > 2 else (m + 10, y - 1)
    return '%04d-%02d-01' % (y2, m2)


def collect_api():
    """→ список (code, name, unit_text, period_str, value)."""
    out = []
    for pub_id, ds_ids in SCOPE:
        for ds_id in ds_ids:
            try:
                dsn = get_json('%s/datasets?publicationId=%d' % (BASE, pub_id))
                items = dsn if isinstance(dsn, list) else dsn.get('dataset', [])
                ds_name = next((d.get('dataset_name') or d.get('name')
                                for d in items if d.get('id') == ds_id), str(ds_id))
            except Exception as e:
                print('  датасет %s: имя не получено (%s)' % (ds_id, e))
                ds_name = str(ds_id)
            sg = 'Экономика всего' if pub_id == 25 else GROUP_NAME[pub_id]
            for mid, adj in MEASURES:
                try:
                    d = get_json('%s/data?y1=2002&y2=2026&datasetId=%d&publicationId=%d&measureId=%d'
                                 % (BASE, ds_id, pub_id, mid))
                except Exception as e:
                    if getattr(e, 'code', None) == 501:
                        continue
                    print('  ds%s m%s: %s' % (ds_id, mid, e))
                    continue
                rows = d.get('RawData', [])
                if not rows:
                    continue
                hdr = {h['id']: h['elname'] for h in d.get('headerData', [])}
                units = {u['id']: u['val'] for u in d.get('units', [])}
                for r in rows:
                    q = hdr.get(r['element_id'], str(r['element_id']))
                    unit = units.get(r['unit_id'], '')
                    code = 'cbrmon__%s__%s__%s__%s' % (slug(ds_name), slug(sg), slug(adj), slug(q))
                    name = '%s — %s / %s / %s (ЦБ мониторинг)' % (q, ds_name, sg, adj)
                    out.append((code, name, unit, period_str(r), r['obs_val']))
            print('  pub%d ds%d %s: всего строк %d' % (pub_id, ds_id, ds_name[:26], len(out)), flush=True)
    return out


def collect_factors():
    if load_workbook is None:
        return []
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(FACTORS_XLSX, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req, timeout=120, context=ctx).read()
    wb = load_workbook(io.BytesIO(data), read_only=True, data_only=True)
    rows = list(wb['Строительство'].iter_rows(values_only=True))
    factors = [str(x) for x in rows[3][1:8]]
    groups = [(1, 'Экономика всего'), (9, 'Крупные'), (17, 'Средние'), (25, 'Малые и микро')]
    out = []
    for r in rows[4:]:
        m = re.match(r'(\d)к(\d\d)', str(r[0]))
        if not m:
            continue
        per = '20%sQ%s' % (m.group(2), m.group(1))
        for gcol, gname in groups:
            for fi, f in enumerate(factors):
                idx = gcol + fi
                v = r[idx] if idx < len(r) else None
                if isinstance(v, (int, float)):
                    code = 'cbrmon__invest__%s__f__%s' % (slug(gname), slug(f))
                    name = '%s — инвестиционный фактор / %s (ЦБ опрос, %% доля)' % (f, gname)
                    out.append((code, name, '%', per, float(v)))
    return out


def main():
    print('сбор из API ЦБ…')
    rows = collect_api()
    rows += collect_factors()
    print('собрано строк:', len(rows))

    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src_id = cur.execute("SELECT source_id FROM catalog.source WHERE source_code='cbr'").fetchone()[0]
            rid_rf = cur.execute("SELECT region_id FROM catalog.region WHERE name_ru='Российская Федерация'").fetchone()[0]

            rel = cur.execute('SELECT release_id FROM catalog.release WHERE source_id=%s AND label=%s',
                              (src_id, RELEASE_LABEL)).fetchone()
            if rel:
                release_id = rel[0]
            else:
                release_id = cur.execute(
                    """INSERT INTO catalog.release (source_id,label,published_at,status,notes)
                       VALUES (%s,%s,%s,'loaded','мониторинг предприятий ЦБ: прямая загрузка из API/XLSX в канон')
                       RETURNING release_id""",
                    (src_id, RELEASE_LABEL, dt.date(2026, 10, 16))).fetchone()[0]
            conn.commit()

            mids = {c: m for c, m in cur.execute(
                "SELECT metric_code, metric_id FROM catalog.metric WHERE metric_code LIKE 'cbrmon_%'")}

            def ensure_metric(code, name, unit_id, freq_id):
                if code in mids:
                    return mids[code]
                cur.execute("""INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id,
                               frequency_id, metric_type, is_derived, status, tags)
                               VALUES (%s,%s,%s,%s,%s,'primary',false,'active','{cbr_survey}')
                               RETURNING metric_id""",
                            (code, name, unit_id, src_id, freq_id))
                mids[code] = cur.fetchone()[0]
                return mids[code]

            obs, miss = [], 0
            for code, name, unit, pstr, val in rows:
                if val is None:
                    continue
                uid = UNIT_MAP.get(unit)
                if uid is None:
                    miss += 1
                    continue
                ps, freq = period_mq(pstr)
                mid = ensure_metric(code, name, uid, freq)
                obs.append((mid, rid_rf, ps, freq, float(val)))
            conn.commit()
            print('к вставке строк:', len(obs), '| отказ unit:', miss, '| метрик всего:', len(mids))

            cur.execute('DROP TABLE IF EXISTS _tmp_cbrmon_direct')
            cur.execute('CREATE TEMP TABLE _tmp_cbrmon_direct (metric_id integer, region_id integer, '
                        'period_start date, frequency_id integer, value numeric, source_id integer, release_id integer)')
            buf = io.StringIO()
            for mid, rid, ps, fr, v in obs:
                buf.write('\t'.join(map(str, (mid, rid, ps, fr, v, src_id, release_id))) + '\n')
            buf.seek(0)
            with cur.copy('COPY _tmp_cbrmon_direct FROM STDIN') as cp:
                cp.write(buf.read())
            cur.execute("""
                INSERT INTO data.observation
                (metric_id,region_id,period_start,frequency_id,value,
                 assessment_type,observation_status,source_id,release_id,sub_dimension)
                SELECT metric_id,region_id,period_start,frequency_id,value,
                       'final','validated',source_id,release_id,''
                FROM _tmp_cbrmon_direct
                ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                             assessment_type,sub_dimension,release_id) DO NOTHING""")
            cur.execute('DROP TABLE _tmp_cbrmon_direct')
            conn.commit()
            n = cur.execute('SELECT count(*) FROM data.observation WHERE release_id=%s', (release_id,)).fetchone()[0]
            print('release_id=%s | наблюдений в релизе: %d' % (release_id, n))
            chk = cur.execute("""SELECT o.value FROM data.observation o JOIN catalog.metric m ON m.metric_id=o.metric_id
                WHERE m.metric_code='cbrmon__stroitelstvo__ekonomika_vsego__ishodnye_dannye__indikator_biznes_klimata_banka_rossii'
                  AND o.period_start='2026-04-01'""").fetchone()
            print('контроль ИБК Строительство 2026-04 (ожид. 11.1019):', chk[0] if chk else 'НЕТ')
            json.dump({'release_id': release_id}, open('/tmp/cbrmon_direct_state.json', 'w'))


if __name__ == '__main__':
    main()
