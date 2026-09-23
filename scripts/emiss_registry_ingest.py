#!/usr/bin/env python3
"""Инжест реестра ЕМИСС (17 CSV из fedstatAPIr) в PostgreSQL v2 на ВМ research-db.

Схема фактическая (schema-live):
- core.release: release_label + source_id + status
- core.metric: metric_code/name_ru/short_name_ru/unit_id/frequency_id/metric_type
- core.observation_v2: уник. индекс (metric,region,freq,period_start,source,release,assessment,sub_dimension)
Дизайн:
- metric_code = emiss_<id>; срезы -> sub_dimension 'A | B | ...'
- регион: только s_OKATO == 'Российская Федерация' (region_id 1, region_code 'ru')
- freq: месяц -> 5; 'январь-декабрь' -> 3; накопленные -> 5 + quality_flags
- value numeric; пустые/'…' пропускаются
"""
import csv, os, re, json, glob
import psycopg2

DB = dict(dbname='research_wiki', user='wiki', host='localhost', port=5432)
REG = '/home/ubuntu/sandbox_datasets/emiss_registry'
RELEASE = 'emiss_registry_batch1_2026-09'
SOURCE = 'fedstat_emiss'

MONTHS = {'январь':1,'февраль':2,'март':3,'апрель':4,'май':5,'июнь':6,'июль':7,
          'август':8,'сентябрь':9,'октябрь':10,'ноябрь':11,'декабрь':12}
UNIT_MAP = [('миллиард руб','bln_rub'),('миллион руб','mln_rub'),('млн руб','mln_rub'),
            ('тысяча руб','ths_rub'),('процентный пункт','pct_pts'),('процент','pct'),
            ('рубл','rub'),('тысяча человек','ths_persons'),('человек','persons'),
            ('коэффициент','ratio'),('индекс','index'),('единица','units')]
REGION_LABELS = {'Российская Федерация': 'РФ',
                 'Российская Федерация без учета новых субъектов (с 01.01.2023)': 'РФ-без-новых-субъектов'}

def parse_period(period, year):
    p = period.strip().lower()
    if p in MONTHS:
        m = MONTHS[p]
        return 5, f"{year}-{m:02d}-01", f"{year}-{m:02d}-28", []
    m = re.match(r'^([а-я]+)-([а-я]+)$', p)
    if m and m.group(1) in MONTHS and m.group(2) in MONTHS:
        m1, m2 = MONTHS[m.group(1)], MONTHS[m.group(2)]
        if m1 == 1 and m2 == 12:
            return 3, f"{year}-01-01", f"{year}-12-31", []
        return 5, f"{year}-{m2:02d}-01", f"{year}-{m2:02d}-28", [f"cumulative_jan_{m2:02d}"]
    return None, None, None, []

def unit_id_for(cur, ei):
    ei_l = ei.strip().lower()
    for k, code in UNIT_MAP:
        if k in ei_l:
            cur.execute("SELECT unit_id FROM core.unit WHERE unit_code=%s", (code,))
            r = cur.fetchone()
            if r: return r[0], code
    cur.execute("SELECT unit_id FROM core.unit WHERE unit_code='unknown'")
    return cur.fetchone()[0], 'unknown'

def main():
    conn = psycopg2.connect(**DB)
    cur = conn.cursor()
    # source
    cur.execute("SELECT source_id FROM core.source WHERE source_code=%s", (SOURCE,))
    r = cur.fetchone()
    if r: source_id = r[0]
    else:
        cur.execute("INSERT INTO core.source (source_code, name_ru, url) VALUES (%s,%s,%s) RETURNING source_id",
                    (SOURCE, 'ЕМИСС (fedstat.ru)', 'https://www.fedstat.ru'))
        source_id = cur.fetchone()[0]
    # release
    cur.execute("SELECT release_id FROM core.release WHERE release_label=%s", (RELEASE,))
    r = cur.fetchone()
    if r: release_id = r[0]
    else:
        cur.execute("""INSERT INTO core.release (source_id, release_label, status, notes)
                       VALUES (%s,%s,'parsed','Реестр владельца: финансы компаний, рынок труда, потребактивность, промышленность') RETURNING release_id""",
                    (source_id, RELEASE))
        release_id = cur.fetchone()[0]
    files = sorted(glob.glob(os.path.join(REG, '*.csv')))
    print(f"files: {len(files)}")
    stats = {}
    for path in files:
        eid = os.path.basename(path)[:-4]
        with open(path, encoding='utf-8') as f:
            rd = csv.DictReader(f)
            rows = list(rd)
        if not rows:
            stats[eid] = 'EMPTY'; continue
        cols = [c for c in rows[0].keys() if c.startswith('s_') and not c.startswith('s_OKATO')]
        title = (rows[0].get('s_POK') or rows[0].get('s_OKVED2') or '').strip() or f'emiss_{eid}'
        metric_code = f'emiss_{eid}'
        cur.execute("SELECT metric_id FROM core.metric WHERE metric_code=%s", (metric_code,))
        r = cur.fetchone()
        if r: metric_id = r[0]
        else:
            unit, _ = unit_id_for(cur, rows[0]['EI'])
            cur.execute("""INSERT INTO core.metric (metric_code, name_ru, short_name_ru, unit_id, frequency_id, metric_type, tags)
                           VALUES (%s,%s,%s,%s,5,'primary',%s) RETURNING metric_id""",
                        (metric_code, title[:250], title[:80], unit, ['emiss','registry_batch1']))
            metric_id = cur.fetchone()[0]
        n_ins, n_skip = 0, 0
        for row in rows:
            if row['s_OKATO'] not in REGION_LABELS:
                n_skip += 1; continue
            reg_label = REGION_LABELS[row['s_OKATO']]
            year = row['Time'].strip()
            if not year.isdigit():
                n_skip += 1; continue
            year = int(year)
            freq, ps, pe, flags = parse_period(row['PERIOD'], year)
            if ps is None:
                n_skip += 1; continue
            raw = (row['ObsValue'] or '').replace(',', '.').replace('…','').strip()
            try:
                val = float(raw)
            except ValueError:
                n_skip += 1; continue
            dim_parts = [row.get(c, '').strip() for c in cols if row.get(c, '').strip()]
            sub = ' | '.join([reg_label] + dim_parts)
            cur.execute("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end, value, sub_dimension,
                 source_id, release_id, assessment_type, observation_status, quality_flags)
                VALUES (%s,1,%s,%s,%s,%s,%s,%s,%s,'final','raw',%s)
                ON CONFLICT DO NOTHING""",
                (metric_id, freq, ps, pe, val, sub, source_id, release_id, flags))
            n_ins += cur.rowcount
        stats[eid] = (n_ins, n_skip)
        print(f"{eid}: ins={n_ins} skip={n_skip}", flush=True)
        conn.commit()
    cur.execute("UPDATE core.release SET status='loaded' WHERE release_id=%s", (release_id,))
    conn.commit()
    tot = sum(v[0] for v in stats.values() if isinstance(v, tuple))
    print(f"TOTAL inserted: {tot}")
    print(json.dumps(stats, ensure_ascii=False))

if __name__ == '__main__':
    main()