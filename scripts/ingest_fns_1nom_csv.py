#!/usr/bin/env python3
"""Инжест CSV-среза ФНС 1-НОМ (open data 7707329152-1nom) в core v2.

Источник: raw/fns/1nom_ГГГГММДД.csv — «О начисленных суммах на уплату страховых взносов
на обязательное социальное страхование по основным видам экономической деятельности
(форма №1-НОМ)», ФНС, тыс. руб., нарастающим итогом с начала года на дату снапшота.

Особенности файлов (проверено 26.09.2026):
- 50 файлов — ';'-разделитель, без кавычек; 2 файла (20250701, 20260101) — ',' с кавычками
  и дополнительной строкой кодов ОКВЭД ('1015.2', ...).
- число колонок различается по винтажам: 89 (2020), 91 (2025-2026), 105 (2024) — разбивка
  ОКВЭД менялась. Поэтому метрики привязаны к ПОЗИЦИИ колонки (G1…Gn), а метка берётся из
  современного справочника raw/fns/1nom_structure.csv для позиций 1..89; позиции выше 89
  помечаются как дореформенные.
- GA — код субъекта (в части файлов отсутствует), GB — название субъекта.

Частота: 6 (квартальная) для снапшотов 0401/0701/1001, 3 (годовая) для 0101.
"""
import csv
import glob
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'raw', 'fns')
STRUCT = os.path.join(RAW, '1nom_structure.csv')
RELEASE_LABEL = 'fns_1nom_okved_csv_2018-2026'
UNIT_THS_RUB = 15
MAX_POS = 105

ALIAS = {
    'республика марий-эл': 'республика марий эл', 'марий эл': 'республика марий эл',
    'республика северная осетия-алания': 'республика северная осетия — алания',
    'республика северная осетия - алания': 'республика северная осетия — алания',
    'северная осетия - алания': 'республика северная осетия — алания',
    'чувашская республика-чувашия': 'чувашская республика', 'чувашская республика': 'чувашская республика',
    'республика татарстан (татарстан)': 'республика татарстан', 'татарстан (татарстан)': 'республика татарстан',
    'республика адыгея (адыгея)': 'республика адыгея', 'адыгея (адыгея)': 'республика адыгея',
    'кемеровская область': 'кемеровская область — кузбасс',
    'кемеровская область - кузбасс': 'кемеровская область — кузбасс',
    'ханты-мансийский автономный округ - югра': 'ханты-мансийский автономный округ — югра',
    'ханты-мансийский ао - югра': 'ханты-мансийский автономный округ — югра',
    'ненецкий ао': 'ненецкий автономный округ', 'ямало-ненецкий ао': 'ямало-ненецкий автономный округ',
    'чукотский ао': 'чукотский автономный округ',
    'архангельская область': 'архангельская область (без нао)',
    'тюменская область': 'тюменская область (без хмао и янао)',
    'г. москва': 'москва', 'г.москва': 'москва', 'москва': 'москва',
    'г. санкт-петербург': 'санкт-петербург', 'г.санкт-петербург': 'санкт-петербург',
    'г. севастополь': 'севастополь', 'г.севастополь': 'севастополь',
    'город москва': 'москва', 'город санкт-петербург': 'санкт-петербург', 'город севастополь': 'севастополь',
    'ямало-hенецкий ао': 'ямало-ненецкий автономный округ',
    'ямало-hенецкий автономный округ': 'ямало-ненецкий автономный округ',
}


def norm(name):
    s = re.sub(r'\s+', ' ', str(name or '')).strip().lower().replace('\ufeff', '')
    return ALIAS.get(s, s)


def num(x):
    s = str(x or '').replace('\xa0', '').replace(' ', '').replace(',', '.')
    s = s.strip()
    if s in ('', '-', '–', 'x', 'X'):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def read_rows(path):
    raw = open(path, encoding='utf-8-sig', errors='replace').read()
    delim = ';' if raw.count(';') > raw.count(',') else ','
    return list(csv.reader(io.StringIO(raw), delimiter=delim))


def labels():
    out = {}
    if os.path.exists(STRUCT):
        for r in csv.reader(open(STRUCT, encoding='utf-8')):
            if r and r[0].startswith('G') and r[0] not in ('GA', 'GB'):
                pos = int(r[0][1:])
                out[pos] = re.sub(r'\s+', ' ', (r[2] if len(r) > 2 else '') or '').strip()
    return out


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
             'ФНС 1-НОМ, open data 7707329152-1nom: начисленные страховые взносы на ОСС по основным видам '
             'экономической деятельности, регионы x ОКВЭД-позиции, снапшоты 2018-2026, тыс. руб.'))
        release_id = cur.fetchone()[0]
    conn.commit()

    cur.execute("SELECT region_id, name_ru FROM core.region")
    by_name = {norm(n): rid for rid, n in cur.fetchall() if n}
    lib = labels()

    # метрики по позициям колонок
    cur.execute("SELECT metric_code, metric_id FROM core.metric WHERE metric_code LIKE 'fns_1nom_okved\\_%'")
    metrics = {c: i for c, i in cur.fetchall()}
    created = 0
    for pos in range(1, MAX_POS + 1):
        code = f'fns_1nom_okved_{pos}'
        if code in metrics:
            continue
        lab = lib.get(pos) or f'ОКВЭД-группа, позиция {pos} (дореформенная разбивка)'
        cur.execute("""INSERT INTO core.metric
            (metric_code, name_ru, description, frequency_id, unit_id, metric_type, is_derived, status)
            VALUES (%s, %s, %s, 6, %s, 'primary', FALSE, 'active') RETURNING metric_id""",
            (code, f'ФНС 1-НОМ: начислено страховых взносов на ОСС — {lab[:200]}',
             f'ФНС 1-НОМ (open data): начисленные страховые взносы на обязательное социальное страхование, '
             f'позиция колонки {pos} = {lab[:200]}. Нарастающим итогом с начала года, тыс. руб.',
             UNIT_THS_RUB))
        metrics[code] = cur.fetchone()[0]
        created += 1
    conn.commit()
    print('создано метрик:', created)

    files = sorted(f for f in glob.glob(os.path.join(RAW, '1nom_*.csv')) if 'structure' not in f)
    total, inserted, unmapped = 0, 0, {}
    for path in files:
        base = os.path.basename(path)
        y, m, d = base[5:9], base[9:11], base[11:13]
        period = f'{y}-{m}-{d}'
        freq = 3 if m == '01' else 6
        rows = read_rows(path)
        if not rows:
            continue
        hdr = rows[0]
        # данные начинаются со строки, где первый столбец — не 'GA'
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
            rid = by_name.get(norm(name))
            if rid is None:
                unmapped[name] = unmapped.get(name, 0) + 1
                continue
            for ci in range(2, len(r)):
                v = num(r[ci])
                if v is None:
                    continue
                pos = ci - 1
                if pos > MAX_POS:
                    continue
                mid = metrics.get(f'fns_1nom_okved_{pos}')
                if mid is None:
                    continue
                batch.append((mid, rid, freq, period, v))
            total += 1
        for i in range(0, len(batch), 500):
            chunk = batch[i:i + 500]
            cur.executemany("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end, value,
                 assessment_type, observation_status, source_id, release_id, sub_dimension)
                VALUES (%s, %s, %s, %s, %s, %s, 'final', 'validated', %s, %s, '')
                ON CONFLICT DO NOTHING""",
                [(m, r, fq, p, p, v, source_id, release_id) for m, r, fq, p, v in chunk])
            inserted += cur.rowcount if cur.rowcount and cur.rowcount > 0 else 0
        conn.commit()
        print(f'  {base}: строк-регионов {len(rows) - start}, точек в батче {len(batch)}')

    cur.execute("""SELECT count(*), count(DISTINCT region_id), count(DISTINCT metric_id),
        min(period_start)::date, max(period_start)::date
        FROM core.observation_v2 WHERE release_id=%s""", (release_id,))
    print('в релизе %s: точек %s, регионов %s, метрик %s, период %s..%s' % ((release_id,) + cur.fetchone()))
    if unmapped:
        print('не смаппированы:', sorted(unmapped.items(), key=lambda kv: -kv[1])[:8])


if __name__ == '__main__':
    main()