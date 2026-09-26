#!/usr/bin/env python3
"""Выравнивание ФНС 1-НОМ по кодам ОКВЭД вместо позиций колонок.

Проблема: разбивка ОКВЭД в open-data выгрузках 1-НОМ менялась (89 колонок в 2020,
105 в 2024, 91 в 2025-2026), поэтому позиционная привязка метрик делает сквозной
ряд 2018-2026 некорректным.

Решение: для каждого винтажа скачивается его собственный справочник
https://data.nalog.ru/opendata/7707329152-1nom/structure-ГГГГММДД.csv, из него
строится соответствие «позиция колонки -> метка ОКВЭД», метка нормализуется в
канонический ключ (напр. «Код по ОКВЭД F 41-43 строительство» -> F4143), и
значения грузятся уже в метрики по ключам: fns_1nom_okved_<ключ>.

Старые позиционные метрики (fns_1nom_okved_<число>) помечаются deprecated.
"""
import csv
import glob
import io
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'raw', 'fns')
CACHE = os.path.join(RAW, 'structure')
UA = {'User-Agent': 'Mozilla/5.0 (hermes-research)'}
RELEASE_LABEL = 'fns_1nom_okved_by_code_2018-2026'
UNIT_THS_RUB = 15

ALIAS = {
    'республика марий-эл': 'республика марий эл', 'марий эл': 'республика марий эл',
    'республика северная осетия-алания': 'республика северная осетия — алания',
    'республика северная осетия - алания': 'республика северная осетия — алания',
    'северная осетия - алания': 'республика северная осетия — алания',
    'чувашская республика-чувашия': 'чувашская республика', 'чувашская республика': 'чувашская республика',
    'республика татарстан (татарстан)': 'республика татарстан', 'татарстан (татарстан)': 'республика татарстан',
    'республика адыгея (адыгея)': 'республика адыгея', 'адыгея (адыгея)': 'республика адыгея',
    'кемеровская область': 'кемеровская область — кузбасс', 'кемеровская область - кузбасс': 'кемеровская область — кузбасс',
    'ханты-мансийский автономный округ - югра': 'ханты-мансийский автономный округ — югра',
    'ханты-мансийский ао - югра': 'ханты-мансийский автономный округ — югра',
    'ненецкий ао': 'ненецкий автономный округ', 'ямало-ненецкий ао': 'ямало-ненецкий автономный округ',
    'ямало-hенецкий ао': 'ямало-ненецкий автономный округ', 'чукотский ао': 'чукотский автономный округ',
    'архангельская область': 'архангельская область (без нао)', 'тюменская область': 'тюменская область (без хмао и янао)',
    'г. москва': 'москва', 'г.москва': 'москва', 'город москва': 'москва', 'москва': 'москва',
    'г. санкт-петербург': 'санкт-петербург', 'г.санкт-петербург': 'санкт-петербург', 'город санкт-петербург': 'санкт-петербург',
    'г. севастополь': 'севастополь', 'г.севастополь': 'севастополь', 'город севастополь': 'севастополь',
}


def norm_name(name):
    return ALIAS.get(re.sub(r'\s+', ' ', str(name or '')).strip().lower().replace('\ufeff', ''),
                     re.sub(r'\s+', ' ', str(name or '')).strip().lower().replace('\ufeff', ''))


def norm_label(s):
    return re.sub(r'\s+', ' ', str(s or '').replace('\ufeff', '')).strip(' ;"').strip()


def key_of(label):
    """Канонический ключ ОКВЭД из русской метки."""
    t = norm_label(label)
    m = re.search(r'ОКВЭД[а-я]*\s*[:\-]?\s*([A-ZА-Я])\s*([0-9][0-9\.\-]*)', t)
    if m:
        letter = m.group(1).upper().replace('А', 'A').replace('В', 'B').replace('С', 'C').replace('Е', 'E').replace('Н', 'H')
        digits = re.sub(r'[^0-9]', '', m.group(2))
        if letter == 'A' and not re.match(r'^[A-Z]', m.group(1)):
            letter = 'A'
        return f'{letter}{digits}' if digits else letter
    if 'не распределен' in t.lower() or 'не распред' in t.lower():
        return 'NOTDIST'
    if 'физическим лицам' in t.lower() and 'предпринимател' in t.lower():
        return 'INDIVIDUALS'
    if 'остальные виды' in t.lower():
        return 'OTHER_ACTIVITY'
    return 'SLUG_' + re.sub(r'[^0-9a-zа-я]+', '_', t.lower())[:40].strip('_')


def structure_rows(date, modern_index=None):
    """Позиция колонки -> (метка, ключ) для винтажа ГГГГММДД.

    modern_index: {нормализованная метка -> ключ} по современным винтажам; используется,
    чтобы сопоставить старые метки без кода ОКВЭД (2018-2020) с современными ключами.
    """
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f'structure-{date}.csv')
    if not os.path.exists(path):
        url = f'https://data.nalog.ru/opendata/7707329152-1nom/structure-{date}.csv'
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                open(path, 'wb').write(r.read())
        except Exception as e:
            return {}, f'{type(e).__name__}: {str(e)[:60]}'
    raw = open(path, encoding='utf-8-sig', errors='replace').read()
    delim = ';' if raw.count(';') > raw.count(',') else ','
    out = {}
    for row in csv.reader(io.StringIO(raw), delimiter=delim):
        cells = [norm_label(c) for c in row]
        gi = next((i for i, c in enumerate(cells) if re.fullmatch(r'G\d+', c)), None)
        if gi is None:
            continue
        pos = int(cells[gi][1:])
        tail = [c for c in cells[gi + 1:] if c]
        descr = next((c for c in tail if 'ОКВЭД' in c), '')
        if not descr:
            descr = next((c for c in tail if len(c) > 12), '')
        if not descr:
            descr = next((c for c in cells if 'ОКВЭД' in c or 'виды' in c.lower()), '')
        key = key_of(descr)
        if key.startswith('SLUG_') and modern_index:
            t = re.sub(r'\s+', ' ', descr.lower()).strip()
            key = modern_index.get(t) or next(
                (k for lab, k in modern_index.items() if t and (t in lab or lab in t) and len(t) > 12), key)
        out[pos] = (descr, key)
    return out, None


def read_data(path):
    raw = open(path, encoding='utf-8-sig', errors='replace').read()
    delim = ';' if raw.count(';') > raw.count(',') else ','
    return list(csv.reader(io.StringIO(raw), delimiter=delim))


def num(x):
    s = str(x or '').replace('\xa0', '').replace(' ', '').replace(',', '.').strip()
    if s in ('', '-', '–', 'x', 'X'):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def main():
    conn = db_tunnel.connect()
    cur = conn.cursor()
    cur.execute("SELECT source_id FROM core.source WHERE source_code='fns'")
    source_id = cur.fetchone()[0]
    cur.execute("SELECT release_id FROM core.release WHERE release_label=%s", (RELEASE_LABEL,))
    row = cur.fetchone()
    if row:
        release_id = row[0]
    else:
        cur.execute("""INSERT INTO core.release (source_id, release_label, published_at, status, notes)
            VALUES (%s, %s, '2026-09-26', 'loaded', %s) RETURNING release_id""",
            (source_id, RELEASE_LABEL,
             'ФНС 1-НОМ по кодам ОКВЭД: пер-винтажные справочники structure-ГГГГММДД.csv, значения '
             'начисленных страховых взносов на ОСС, тыс. руб., метрики по каноническим ключам ОКВЭД'))
        release_id = cur.fetchone()[0]
    conn.commit()

    cur.execute("SELECT region_id, name_ru FROM core.region")
    by_name = {norm_name(n): rid for rid, n in cur.fetchall() if n}

    files = sorted(f for f in glob.glob(os.path.join(RAW, '1nom_*.csv')) if 'structure' not in f)
    dates = [os.path.basename(f)[5:13] for f in files]

    # 1) справочники по винтажам; современные (2025+) — первыми, чтобы разрешать старые метки
    modern_dates = [d for d in dates if d >= '20250101']
    maps, problems = {}, {}
    modern_index = {}
    for d in sorted(modern_dates):
        m, err = structure_rows(d)
        if m:
            maps[d] = m
            for _pos, (lab, key) in m.items():
                t = re.sub(r'\s+', ' ', (lab or '').lower()).strip()
                if t and not key.startswith('SLUG_'):
                    modern_index.setdefault(t, key)
        else:
            problems[d] = err
    for d in dates:
        if d in maps:
            continue
        m, err = structure_rows(d, modern_index=modern_index)
        if m:
            maps[d] = m
        else:
            problems[d] = err
    print(f'справочников получено: {len(maps)} из {len(dates)}; современный индекс меток: {len(modern_index)}')
    if problems:
        print('без справочника:', list(problems.items())[:5])
    keys_by_vintage = {d: sorted({k for _p, (_l, k) in m.items() if not k.startswith("SLUG_")}) for d, m in maps.items()}
    slug_counts = {d: sum(1 for _p, (_l, k) in m.items() if k.startswith('SLUG_')) for d, m in maps.items()}
    print('несопоставленных (SLUG) позиций по винтажам:', {d: c for d, c in list(slug_counts.items())[:6]})

    # 2) канонические ключи: ключ -> лучшая метка (из самого свежего винтажа)
    key_label = {}
    for d in sorted(maps):
        for pos, (lab, key) in maps[d].items():
            key_label[key] = lab or key_label.get(key, '')
    print('канонических ключей ОКВЭД:', len(key_label))

    # 3) метрики по ключам
    cur.execute("SELECT metric_code, metric_id FROM core.metric WHERE metric_code LIKE 'fns_1nom_key\\_%'")
    metrics = {c: i for c, i in cur.fetchall()}
    created = 0
    for key, lab in key_label.items():
        code = f'fns_1nom_key_{key}'
        if code in metrics:
            continue
        cur.execute("""INSERT INTO core.metric
            (metric_code, name_ru, description, frequency_id, unit_id, metric_type, is_derived, status)
            VALUES (%s, %s, %s, 6, %s, 'primary', FALSE, 'active') RETURNING metric_id""",
            (code, f'ФНС 1-НОМ: взносы на ОСС — {lab[:200]}',
             f'ФНС 1-НОМ (open data), канонический ключ ОКВЭД {key}: {lab[:200]}. '
             f'Начисленные страховые взносы на ОСС, тыс. руб., нарастающим итогом с начала года. '
             f'Привязка по пер-винтажным справочникам structure-ГГГГММДД.csv.',
             UNIT_THS_RUB))
        metrics[code] = cur.fetchone()[0]
        created += 1
    conn.commit()
    print('создано метрик по ключам:', created)

    # 4) загрузка значений
    total_pts, skipped_vintage = 0, {}
    for path in files:
        base = os.path.basename(path)
        d = base[5:13]
        smap = maps.get(d)
        if not smap:
            skipped_vintage[base] = 'нет справочника'
            continue
        period = f'{d[:4]}-{d[4:6]}-{d[6:8]}'
        freq = 3 if d[4:6] == '01' else 6
        rows = read_data(path)
        start = 1
        while start < len(rows) and str(rows[start][0]).strip().upper() in ('GA', ''):
            start += 1
        batch = []
        for r in rows[start:]:
            if len(r) < 3:
                continue
            name = None
            for ci in (1, 0):
                if ci < len(r) and r[ci] and not re.match(r'^[\d\s.,]+$', str(r[ci]).strip()):
                    name = str(r[ci]).strip()
                    break
            if not name:
                continue
            rid = by_name.get(norm_name(name))
            if rid is None:
                continue
            for ci in range(2, len(r)):
                v = num(r[ci])
                if v is None:
                    continue
                pos = ci - 1
                key = smap.get(pos, (None, None))[1]
                if not key or key.startswith('SLUG_'):
                    continue
                mid = metrics.get(f'fns_1nom_key_{key}')
                if mid is None:
                    continue
                batch.append((mid, rid, freq, period, v))
        for i in range(0, len(batch), 500):
            chunk = batch[i:i + 500]
            cur.executemany("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end, value,
                 assessment_type, observation_status, source_id, release_id, sub_dimension)
                VALUES (%s, %s, %s, %s, %s, %s, 'final', 'validated', %s, %s, '')
                ON CONFLICT DO NOTHING""",
                [(m, r, fq, p, p, v, source_id, release_id) for m, r, fq, p, v in chunk])
        conn.commit()
        total_pts += len(batch)
        print(f'  {base}: точек {len(batch)}')
    if skipped_vintage:
        print('пропущены винтажи:', skipped_vintage)

    # 5) старые позиционные метрики — в deprecated
    cur.execute("""UPDATE core.metric SET status='deprecated',
        description = COALESCE(description,'') || ' | ЗАМЕНЕНО 2026-09-26: позиционная привязка '
        'некорректна между винтажами ОКВЭД; используйте fns_1nom_key_*'
        WHERE metric_code ~ '^fns_1nom_okved_[0-9]+$' AND status <> 'deprecated'""")
    print('позиционных метрик переведено в deprecated:', cur.rowcount)
    conn.commit()

    cur.execute("""SELECT count(*), count(DISTINCT region_id), count(DISTINCT metric_id),
        min(period_start)::date, max(period_start)::date FROM core.observation_v2 WHERE release_id=%s""", (release_id,))
    print('в релизе %s: точек %s, регионов %s, метрик %s, период %s..%s' % ((release_id,) + cur.fetchone()))

    cur.execute("""SELECT r.name_ru, o.period_start::date, o.value::numeric(20,0)
        FROM core.observation_v2 o JOIN core.metric m USING (metric_id) JOIN core.region r USING (region_id)
        WHERE o.release_id=%s AND m.metric_code='fns_1nom_key_L68' AND r.name_ru='Москва'
        ORDER BY o.period_start DESC LIMIT 4""", (release_id,))
    print('КТ L68 (операции с недвижимостью), Москва:', cur.fetchall())


if __name__ == '__main__':
    main()