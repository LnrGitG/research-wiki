#!/usr/bin/env python3
"""Загрузка ВРП в core.observation_v2 из официального файла Росстата VRP_s1998.xlsx.

Что берём (листы файла):
  1–2  ВРП по субъектам РФ в текущих основных ценах, млн руб. (1998–2015 и 2016–2024) → grp_level
  3–4  ВРП на душу населения, руб. (1998–2010 и 2016–2024)                        → grp_pc
  5–6  Индексы физического объёма ВРП, % к предыдущему году (1998–2016 и 2017–2024) → grp_ifo

Особенности:
  * первая строка данных — сумма по субъектам РФ (это ВРП, не ВВП), далее федеральные округа,
    затем субъекты; ФО вставляем как есть (уровень federal_district) — учитывать, что при
    суммировании они дают двойной счёт;
  * названия вида «в т.ч. Ненецкий авт. округ», «Архангельская область без Ненецкого авт.округа»
    и «в т.ч. Ханты-Мансийский автономный округ-Югра» требуют явных алиасов;
  * периоды годовые: period_start = 1 января, period_end = 31 декабря.

Запуск: python3 scripts/ingest_grp.py [--file путь]
"""
import argparse
import os
import re
import sys

import openpyxl

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402

DEFAULT_FILE = os.path.join(REPO, 'raw', 'rosstat', 'accounts', 'VRP_s1998.xlsx')
SOURCE_CODE = 'rosstat'
RELEASE_LABEL = 'rosstat_grp_annual_1998-2024'
FREQ_ANNUAL = 3

METRICS = {
    'grp_level': ('ВРП по субъектам РФ, млн руб. (текущие основные цены)', 11),
    'grp_pc': ('ВРП на душу населения, руб.', 38),
    'grp_ifo': ('ИФО ВРП, % к предыдущему году', 12),
}

ALIAS = {
    'валовой региональный продукт по субъектам российской федерации': 1,
    'в т.ч. ненецкий авт. округ': 31,
    'в т.ч. ханты-мансийский автономный округ-югра': 71,
    'архангельская область без ненецкого авт.округа': 30,
    'в том числе ненецкий автономный округ': 31,
    'в том числе ханты-мансийский автономный округ - югра': 71,
    'в т.ч. ханты-мансийский авт. округ-югра': 71,
    'в т.ч. ханты-мансийский авт.округ-югра': 71,
}


def norm(s):
    s = str(s).lower().replace('ё', 'е').replace('–', '-').replace('—', '-')
    s = s.replace('г.', '').replace('город ', '')
    s = re.sub(r'\(.*?\)', ' ', s)
    s = re.sub(r'[^а-яa-z0-9 -]', '', s)
    s = re.sub(r'\s*-\s*', '-', s)
    return re.sub(r'\s+', ' ', s).strip()


def year_of(cell):
    m = re.match(r'^(\d{4})', str(cell or '').strip())
    return int(m.group(1)) if m else None


ALIAS_N = {}  # заполняется в main после определения norm()


def parse_sheet(ws):
    """-> (год -> {region_id: значение}), список непознанных подписей."""
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return {}, []
    header = None
    for i, r in enumerate(rows[:6]):
        years = [year_of(c) for c in r]
        if sum(1 for y in years if y) >= 4:
            header, header_idx = years, i
            break
    if header is None:
        return {}, []
    out, unknown = {}, []
    for r in rows[header_idx + 1:]:
        label = r[0]
        if not isinstance(label, str) or not label.strip():
            continue
        if label.strip().startswith(('1)', '2)', '3)', '4)', '5)')) or 'Данные' in label[:30]:
            continue
        key = norm(label)
        if key.startswith('валовой региональный продукт по субъектам российской федерации'):
            rid = 1  # строка-итог по субъектам РФ
        else:
            rid = ALIAS_N.get(key) or REGIONS.get(key)
        if not rid:
            unknown.append(label.strip())
            continue
        for c, y in enumerate(header):
            if not y or c >= len(r):
                continue
            v = r[c]
            if isinstance(v, (int, float)):
                out.setdefault(y, {})[rid] = float(v)
    return out, unknown


def ensure_metric(code, name, unit_id):
    row = db_tunnel.query('SELECT metric_id FROM core.metric WHERE metric_code=%s', (code,))
    if row:
        return row[0][0]
    db_tunnel.execute("""INSERT INTO core.metric (metric_code, name_ru, description, unit_id,
        frequency_id, metric_type, status, tags)
        VALUES (%s,%s,%s,%s,%s,'primary','active', ARRAY['rosstat','grp','regional'])""",
        (code, name, 'Валовой региональный продукт (Росстат, годовая оценка, файл VRP_s1998.xlsx)',
         unit_id, FREQ_ANNUAL))
    return db_tunnel.query('SELECT metric_id FROM core.metric WHERE metric_code=%s', (code,))[0][0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--file', default=DEFAULT_FILE)
    args = ap.parse_args()
    if not os.path.exists(args.file):
        sys.exit('нет файла: ' + args.file)

    db_tunnel.connect()
    global REGIONS, ALIAS_N
    ALIAS_N = {norm(k): v for k, v in ALIAS.items()}
    REGIONS = {}
    for rid, name, short, level in db_tunnel.query('SELECT region_id, name_ru, short_name, level FROM core.region'):
        for k in (name, short):
            if k:
                REGIONS.setdefault(norm(k), rid)
    for alias, rid in db_tunnel.query('SELECT alias, region_id FROM meta.region_alias'):
        REGIONS.setdefault(norm(alias), rid)

    src_id = db_tunnel.query('SELECT source_id FROM core.source WHERE source_code=%s', (SOURCE_CODE,))[0][0]
    rel = db_tunnel.query('SELECT release_id FROM core.release WHERE source_id=%s AND release_label=%s',
                          (src_id, RELEASE_LABEL))
    if rel:
        release_id = rel[0][0]
    else:
        db_tunnel.execute("""INSERT INTO core.release (source_id, release_label, published_at, status, notes)
            VALUES (%s,%s, now(), 'loaded', 'ВРП по субъектам РФ, годовые уровни, на душу, ИФО')""",
            (src_id, RELEASE_LABEL))
        release_id = db_tunnel.query('SELECT release_id FROM core.release WHERE source_id=%s AND release_label=%s',
                                     (src_id, RELEASE_LABEL))[0][0]

    wb = openpyxl.load_workbook(args.file, read_only=True, data_only=True)
    series = {'grp_level': ['1', '2'], 'grp_pc': ['3', '4'], 'grp_ifo': ['5', '6']}
    total, unknown_all = 0, {}
    conn = db_tunnel.connect()
    with conn.cursor() as cur:
        for code, sheets in series.items():
            metric_id = ensure_metric(code, METRICS[code][0], METRICS[code][1])
            data, unknown = {}, []
            for sh in sheets:
                if sh not in wb.sheetnames:
                    continue
                d, u = parse_sheet(wb[sh])
                unknown += u
                for y, vals in d.items():
                    data.setdefault(y, {}).update(vals)
            unknown_all[code] = sorted(set(unknown))
            rows = []
            for y, vals in sorted(data.items()):
                for rid, v in vals.items():
                    rows.append((metric_id, rid, FREQ_ANNUAL, f'{y}-01-01', f'{y}-12-31', v,
                                 'validated', src_id, release_id))
            cur.executemany("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end, value,
                 observation_status, source_id, release_id)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT DO NOTHING""", rows)
            conn.commit()
            years = sorted(data)
            print(f'{code}: точек {len(rows)}, регионов {max((len(v) for v in data.values()), default=0)}, '
                  f'годы {years[0] if years else "—"}..{years[-1] if years else "—"}')
            total += len(rows)
    wb.close()

    for code, unk in unknown_all.items():
        if unk:
            print(f'{code}: не сопоставлено {len(unk)}: {unk[:6]}')
    print('всего вставлено точек:', total)
    print('контроль: ВРП РФ 2024 =', db_tunnel.query("""
        SELECT o.value FROM core.observation_v2 o JOIN core.metric m USING (metric_id)
        JOIN core.region r USING (region_id) WHERE m.metric_code='grp_level' AND r.region_id=1
          AND o.period_start='2024-01-01'"""))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())