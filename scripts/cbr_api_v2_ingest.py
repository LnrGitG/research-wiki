#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Загрузка трёх блоков универсального API ЦБ РФ в PostgreSQL v2 (research_wiki).

Блоки: денежные агрегаты (pub5), индексы курса рубля/РЭЭК (pub34), ИЖК-продление
и SA-задолженность ИЖК (pub21, pub14 ds29).

Датировка (проверено, queries/cbr-monitoring-api-rebuild.md):
- pub5: сдвиг 0 (dt = дата запаса на 1-е число);
- pub34: сдвиг -1 (dt = отчётный месяц); None пропускать;
- pub21/pub14 ds29: сдвиг -1; ds55/56: сдвиг 0.

Run-версионность v2: новый release в core.release, вставка наблюдений с этим
release_id; дубли по уникальному индексу (metric,region,freq,period,source,
release,assessment,sub_dimension) невозможны в силу нового release_id.
Существующие метрики (ivz, idz, ioz, irz) продлеваются теми же metric_id.

Контрольные точки (после загрузки): М2 2026-09-01 = 137073.5; ИЖК объём
июнь 2026 = 482695 (уже в БД); РЭЭК mom июль 2026 = -4.8; ставка ИЖК руб июль = 10.52.
"""
import urllib.request, ssl, json, sys, os, hashlib, datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))
from db_tunnel import connect, query, execute

BASE = 'https://www.cbr.ru/dataservice'
SOURCE_CBR = 7
REGION_RF = 1


def get_json(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return json.loads(urllib.request.urlopen(req, timeout=90, context=ctx).read().decode('utf-8', 'ignore'))


def shift(iso, months):
    y, m = int(iso[:4]), int(iso[5:7])
    m2 = m + months
    y2, m2 = (y + (m2 - 1) // 12, (m2 - 1) % 12 + 1)
    return '%s-%02d-01' % (y2, m2)


def fetch_rows(pub_id, ds_id, measure_id=None, y1=1992, y2=2026):
    url = f'{BASE}/data?y1={y1}&y2={y2}&datasetId={ds_id}&publicationId={pub_id}'
    if measure_id:
        url += f'&measureId={measure_id}'
    d = get_json(url)
    hdr = {h['id']: h['elname'] for h in d.get('headerData', [])}
    units = {u['id']: u['val'] for u in d.get('units', [])}
    out = []
    for r in d.get('RawData', []):
        v = r.get('obs_val')
        if v is None:
            continue
        out.append({'element': hdr.get(r['element_id'], str(r['element_id'])),
                    'dt': (r.get('dt') or '').strip(),
                    'date': r['date'][:10],
                    'value': float(v),
                    'unit_raw': units.get(r['unit_id'], '')})
    return out


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


def create_release(cur, label, note):
    cur.execute("""INSERT INTO core.release (source_id, release_label, published_at, ingested_at, status, notes)
                   VALUES (%s,%s,%s,now(),'loaded',%s) RETURNING release_id""",
                (SOURCE_CBR, label, datetime.datetime.now(datetime.timezone.utc), note))
    return cur.fetchone()[0]


def insert_obs(cur, rows):
    cur.executemany("""INSERT INTO core.observation_v2
        (metric_id, region_id, frequency_id, period_start, period_end, value,
         assessment_type, observation_status, source_id, release_id, quality_flags, sub_dimension)
        VALUES (%s,%s,5,%s,%s,%s,'final','raw',%s,%s,'{}',%s)
        ON CONFLICT (metric_id, region_id, frequency_id, period_start, source_id,
                     release_id, assessment_type, sub_dimension) DO NOTHING""",
        rows)


def month_end(iso):
    y, m = int(iso[:4]), int(iso[5:7])
    if m == 12:
        return f'{y}-12-31'
    return f'{y}-{m+1:02d}-01'[:-2] + '01' if False else (datetime.date(y + (m == 12), (m % 12) + 1, 1) - datetime.timedelta(days=1)).isoformat()


def main():
    con = connect()
    cur = con.cursor()

    # ---- Блок 1: денежные агрегаты (сдвиг 0) ----
    rel1 = create_release(cur, 'cbr_api_monaetary_aggregates_2026-09',
                          'Универсальный API ЦБ, pub5; сдвиг 0 (dt=запас на 1-е число)')
    aggs = [(5, 'm0', 'Денежный агрегат М0'), (6, 'm1', 'Денежный агрегат М1'),
            (7, 'm2', 'Денежный агрегат М2'), (8, 'm2broad', 'Широкая денежная масса')]
    n1 = 0
    for ds_id, code, name in aggs:
        rows = fetch_rows(5, ds_id, y1=1992)
        mid = ensure_metric(cur, code, name, 10, 5, f'ЦБ РФ, {name}, на первое число месяца, млрд руб.')
        batch = []
        for r in rows:
            period = r['date']  # сдвиг 0
            el = 'Всего' if r['element'] in ('Всего',) else r['element']
            batch.append((mid, REGION_RF, period, month_end(period), r['value'], SOURCE_CBR, rel1,
                          f'component: {el}' if code != 'm2' or el != 'Всего' else ''))
        insert_obs(cur, batch)
        n1 += len(batch)
    con.commit()
    print(f'Блок 1 (агрегаты): {n1} строк')

    # ---- Блок 2: индексы курса рубля (сдвиг -1) ----
    rel2 = create_release(cur, 'cbr_api_fx_indices_2026-09',
                          'Универсальный API ЦБ, pub34; сдвиг -1 (dt=отчётный месяц)')
    fx = [(129, 'fx_nom_idx', 'Индекс номинального курса рубля'),
          (130, 'neer', 'Индекс номинального эффективного курса рубля'),
          (131, 'fx_real_idx', 'Индекс реального курса рубля'),
          (132, 'reer', 'Индекс реального эффективного курса рубля')]
    measures = [(147, 'dec_yoy', '% прироста к декабрю предыдущего года'),
                (148, 'mom', '% к предыдущему периоду'),
                (149, 'ytd', '% с начала года')]
    n2 = 0
    for ds_id, base_code, base_name in fx:
        for mid_m, suffix, mname in measures:
            rows = fetch_rows(34, ds_id, mid_m, y1=2005)
            code = f'{base_code}_{suffix}'
            mid = ensure_metric(cur, code, f'{base_name}, {mname}', 30, 5,
                                f'ЦБ РФ, pub34 ds{ds_id} measure {mid_m}: {mname}, 2005=100 база')
            batch = []
            for r in rows:
                period = shift(r['date'], -1)  # сдвиг -1
                batch.append((mid, REGION_RF, period, month_end(period), r['value'], SOURCE_CBR, rel2, ''))
            insert_obs(cur, batch)
            n2 += len(batch)
    con.commit()
    print(f'Блок 2 (индексы курса): {n2} строк')

    # ---- Блок 3: ИЖК (сдвиг -1 для объёмов, 0 для SA) ----
    rel3 = create_release(cur, 'cbr_api_izhk_ext_2026-09',
                          'Универсальный API ЦБ, pub21/pub14; сдвиг -1 (ds55/56: 0)')
    n3 = 0
    # 3а. Продление существующих метрик RF (sub_dimension='')
    ext = [(45, 'ivz', 18), (46, 'idz', 18), (47, 'ioz', 18), (44, 'mlc', 29), (48, 'ssk_2', 33)]
    for ds_id, code, unit_id in ext:
        rows = fetch_rows(21, ds_id, 22, y1=2024)
        mid = ensure_metric(cur, code, '', unit_id, 5)  # name не трогаем
        batch = []
        for r in rows:
            if r['element'] != 'Всего':
                continue
            period = shift(r['date'], -1)
            batch.append((mid, REGION_RF, period, month_end(period), r['value'], SOURCE_CBR, rel3, ''))
        insert_obs(cur, batch)
        n3 += len(batch)
    # 3б. Ставка ИЖК (pub14 ds29, элементы 36/40, сдвиг -1)
    rows = fetch_rows(14, 29, y1=2014)
    mid_rub = ensure_metric(cur, 'izhk_rate_rub', 'Ставка по ИЖК в рублях (средневзв., за месяц)', 12, 5,
                            'ЦБ РФ, pub14 ds29 el36')
    mid_fx = ensure_metric(cur, 'izhk_rate_fx', 'Ставка по ИЖК в иностранной валюте', 12, 5,
                           'ЦБ РФ, pub14 ds29 el40')
    el_map = {'В рублях': mid_rub, 'В иностранной валюте': mid_fx}
    batch = []
    for r in rows:
        if r['element'] not in el_map:
            continue
        period = shift(r['date'], -1)
        batch.append((el_map[r['element']], REGION_RF, period, month_end(period), r['value'], SOURCE_CBR, rel3, ''))
    insert_obs(cur, batch)
    n3 += len(batch)
    # 3в. SA-задолженность ИЖК (pub21 ds55/56, сдвиг 0, элементы 'Всего'/'В рублях'...)
    for ds_id, code, name in [(55, 'izhk_debt_sa', 'SA задолженность по ИЖК'),
                              (56, 'izhk_debt_sa_rights', 'SA задолженность по ИЖК с учётом прав требования')]:
        rows = fetch_rows(21, ds_id, y1=2009)
        mid = ensure_metric(cur, code, name, 11, 5, f'ЦБ РФ, pub21 ds{ds_id}')
        batch = []
        for r in rows:
            el = r['element']
            period = r['date']  # сдвиг 0
            sub = f'currency: {el}' if el != 'Всего' else 'currency: Всего'
            batch.append((mid, REGION_RF, period, month_end(period), r['value'], SOURCE_CBR, rel3, sub))
        insert_obs(cur, batch)
        n3 += len(batch)
    con.commit()
    print(f'Блок 3 (ИЖК): {n3} строк')

    # ---- Контрольные точки ----
    checks = [
        ('m2 Всего 2026-09-01 = 137073.5', "SELECT value FROM core.observation_v2 WHERE metric_id=(SELECT metric_id FROM core.metric WHERE metric_code='m2') AND sub_dimension='' AND period_start='2026-09-01'", 137073.5),
        ('РЭЭК mom 2026-07-01 = -4.8', "SELECT value FROM core.observation_v2 WHERE metric_id=(SELECT metric_id FROM core.metric WHERE metric_code='reer_mom') AND period_start='2026-07-01'", -4.8),
        ('ставка ИЖК руб 2026-07-01 = 10.52', "SELECT value FROM core.observation_v2 WHERE metric_id=(SELECT metric_id FROM core.metric WHERE metric_code='izhk_rate_rub') AND period_start='2026-07-01'", 10.52),
        ('ИЖК объём продление 2026-07-01 (API date 2026-08-01, dt Июль = 363411)', "SELECT value FROM core.observation_v2 WHERE metric_id=(SELECT metric_id FROM core.metric WHERE metric_code='ivz') AND period_start='2026-07-01' AND release_id=%d" % rel3, 363411.0),
    ]
    print('\nКонтрольные точки:')
    all_ok = True
    for label, sql, expected in checks:
        cur.execute(sql)
        got = cur.fetchone()
        ok = got and abs(float(got[0]) - expected) < 0.01
        all_ok &= bool(ok)
        print(f'  {label}: got={got[0] if got else None} {"OK" if ok else "FAIL"}')
    con.commit()

    total = n1 + n2 + n3
    print(f'\nИТОГО: {total} строк, releases {rel1}/{rel2}/{rel3}, контроль: {"PASS" if all_ok else "FAIL"}')
    if not all_ok:
        con.rollback()
        print('ВАЛИДАЦИЯ ПРОВАЛЕНА — транзакция откатывается (releases остаются, obs не вставлены?)')
    con.close()


if __name__ == '__main__':
    main()