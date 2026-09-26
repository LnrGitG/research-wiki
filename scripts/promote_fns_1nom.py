#!/usr/bin/env python3
"""Промоушен ФНС 1-НОМ из staging в core (v2).

Источник данных: v2_stage.fns_rows, форма '1nom', лист '1010' — канонический срез
«всего» по видам налогов (остальные листы — отраслевые детализации, чьи метки пока
не идентифицированы; их сумма в 2,2 раза превышает лист 1010 из-за вложенных групп).

Метрики: core.metric fns_1nom_<col_code> (38 кодов существовали пустыми, 21 и 37
создаются здесь). Частота 3 = годовая, единица 15 = тыс. руб. (проверено по якорю:
транспортный налог РФ 229 954 245 тыс. руб = 230 млрд руб, что соответствует
известному порядку величины).

Идемпотентность: ON CONFLICT DO NOTHING по (metric_id, region_id, frequency_id,
period_start, source_id, release_id, assessment_type, sub_dimension).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

RELEASE_LABEL = 'fns_1nom_1010_promote_2026-09'
SHEET = '1010'
FORM = '1nom'
FREQ_YEAR = 3
UNIT_THS_RUB = 15

ALIAS = {
    'республика марий-эл': 'республика марий эл',
    'республика северная осетия-алания': 'республика северная осетия — алания',
    'республика северная осетия - алания': 'республика северная осетия — алания',
    'чувашская республика-чувашия': 'чувашская республика',
    'республика татарстан (татарстан)': 'республика татарстан',
    'республика адыгея (адыгея)': 'республика адыгея',
    'кемеровская область': 'кемеровская область — кузбасс',
    'кемеровская область - кузбасс': 'кемеровская область — кузбасс',
    'ханты-мансийский автономный округ - югра': 'ханты-мансийский автономный округ — югра',
    'ханты-мансийский ао - югра': 'ханты-мансийский автономный округ — югра',
    'ненецкий ао': 'ненецкий автономный округ',
    'ямало-ненецкий ао': 'ямало-ненецкий автономный округ',
    'чукотский ао': 'чукотский автономный округ',
    'архангельская область': 'архангельская область (без нао)',
    'тюменская область': 'тюменская область (без хмао и янао)',
    'г. москва': 'москва',
    'г.москва': 'москва',
    'г. санкт-петербург': 'санкт-петербург',
    'г.санкт-петербург': 'санкт-петербург',
    'г. севастополь': 'севастополь',
    'г.севастополь': 'севастополь',
}


def norm(name):
    s = re.sub(r'\s+', ' ', str(name or '')).strip().lower()
    return ALIAS.get(s, s)


def main():
    conn = db_tunnel.connect()
    cur = conn.cursor()

    # источник
    cur.execute("SELECT source_id FROM core.source WHERE source_code='fns'")
    row = cur.fetchone()
    if not row:
        raise SystemExit('нет источника fns в core.source')
    source_id = row[0]

    # релиз
    cur.execute("SELECT release_id FROM core.release WHERE release_label=%s", (RELEASE_LABEL,))
    row = cur.fetchone()
    if row:
        release_id = row[0]
        print('релиз уже есть:', release_id)
    else:
        cur.execute("""INSERT INTO core.release (source_id, release_label, published_at, status, notes)
            VALUES (%s, %s, '2026-09-26', 'loaded', %s) RETURNING release_id""",
            (source_id, RELEASE_LABEL,
             'Промоушен ФНС 1-НОМ (лист 1010, «всего») из v2_stage.fns_rows: начислено/поступило по видам налогов, '
             'уровни РФ/ФО/субъект, снапшоты 2025-01-01 и 2026-01-01, единица тыс. руб.'))
        release_id = cur.fetchone()[0]
    conn.commit()

    # справочник регионов
    cur.execute("SELECT region_id, name_ru, level FROM core.region")
    by_name, by_level = {}, {}
    for rid, name, level in cur.fetchall():
        if not name:
            continue
        by_name[norm(name)] = (rid, level)
        by_level.setdefault(level, []).append((rid, norm(name)))

    # метрики: существующие коды + создание пропущенных
    cur.execute("SELECT metric_code, metric_id FROM core.metric WHERE metric_code LIKE 'fns_1nom\\_%'")
    metrics = {c: i for c, i in cur.fetchall()}

    cur.execute("""SELECT DISTINCT col_code, col_name FROM v2_stage.fns_rows
        WHERE form_code=%s AND sheet_code=%s AND col_code ~ '^[0-9]+$'""", (FORM, SHEET))
    colnames = {c: (n or '') for c, n in cur.fetchall()}

    created = []
    for col, name in sorted(colnames.items(), key=lambda kv: int(kv[0])):
        code = f'fns_1nom_{col}'
        if code in metrics:
            continue
        clean = re.sub(r'\s+', ' ', str(name)).strip()[:300] or f'ФНС 1-НОМ, графа {col}'
        cur.execute("""INSERT INTO core.metric
            (metric_code, name_ru, description, frequency_id, unit_id, metric_type, is_derived, status)
            VALUES (%s, %s, %s, %s, %s, 'primary', FALSE, 'active') RETURNING metric_id""",
            (code, clean, f'ФНС 1-НОМ (лист 1010, «всего»), графа {col}: {clean}', FREQ_YEAR, UNIT_THS_RUB))
        metrics[code] = cur.fetchone()[0]
        created.append(code)
    conn.commit()
    print('создано метрик:', created)

    # наблюдения
    cur.execute("""SELECT snapshot_date, level_code, region_raw, col_code, value_num
        FROM v2_stage.fns_rows
        WHERE form_code=%s AND sheet_code=%s AND value_num IS NOT NULL AND col_code ~ '^[0-9]+$'""",
        (FORM, SHEET))
    staged = cur.fetchall()
    print('строк staging:', len(staged))

    batch, unmapped, skipped = [], {}, 0
    for snap, level, region_raw, col, value in staged:
        metric_id = metrics.get(f'fns_1nom_{col}')
        if metric_id is None:
            skipped += 1
            continue
        if level == 'rf':
            rid = 1
        else:
            rid, _ = by_name.get(norm(region_raw), (None, None))
        if rid is None:
            unmapped[region_raw] = unmapped.get(region_raw, 0) + 1
            continue
        batch.append((metric_id, rid, snap, value))

    for i in range(0, len(batch), 500):
        chunk = batch[i:i + 500]
        cur.executemany("""INSERT INTO core.observation_v2
            (metric_id, region_id, frequency_id, period_start, period_end, value,
             assessment_type, observation_status, source_id, release_id, sub_dimension)
            VALUES (%s, %s, %s, %s, %s, %s, 'final', 'validated', %s, %s, '')
            ON CONFLICT DO NOTHING""",
            [(m, r, FREQ_YEAR, p, p, v, source_id, release_id) for m, r, p, v in chunk])
        conn.commit()

    print('вставлено (попыток):', len(batch), '| пропущено без метрики:', skipped)
    if unmapped:
        print('не смаппированы регионы:', sorted(unmapped.items(), key=lambda kv: -kv[1])[:10])

    cur.execute("""SELECT count(*), count(DISTINCT o.region_id), count(DISTINCT o.metric_id)
        FROM core.observation_v2 o WHERE o.release_id=%s""", (release_id,))
    print('в релизе %s: точек %s, регионов %s, метрик %s' % ((release_id,) + cur.fetchone()))

    cur.execute("""SELECT o.period_start::date, o.value::numeric(20,2)
        FROM core.observation_v2 o JOIN core.metric m USING (metric_id)
        WHERE m.metric_code='fns_1nom_26' AND o.region_id=1 ORDER BY o.period_start""")
    print('КТ: транспортный налог РФ (fns_1nom_26):', cur.fetchall())


if __name__ == '__main__':
    main()