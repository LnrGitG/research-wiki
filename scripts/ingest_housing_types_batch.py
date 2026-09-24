#!/usr/bin/env python3
"""Батч-инжест видов строительства в БД v2 (быстрая версия)."""
import os, sys, glob, sqlite3, calendar
import pandas as pd
sys.path.insert(0, os.path.expanduser('~/research-wiki-private/scripts'))
import db_tunnel

WORKDIR = os.path.expanduser('~/research-wiki-private')
SRC_STAT = 11

CAT_MAP = {
    'Жилые здания': ('b1_residential', 'Ввод зданий: жилые (С-1, накопительно с начала года)'),
    'Нежилые здания': ('b2_nonresidential', 'Ввод зданий: нежилые всего (С-1, накопительно)'),
    'Промышленные здания': ('b3_industrial', 'Ввод зданий: промышленные (С-1, накопительно)'),
    'Коммерческие здания': ('b4_commercial', 'Ввод зданий: коммерческие (С-1, накопительно)'),
    'Сельскохозяйственные здания': ('b5_agri', 'Ввод зданий: сельскохозяйственные (С-1, накопительно)'),
    'Административные здания': ('b6_admin', 'Ввод зданий: административные (С-1, накопительно)'),
    'Учебные здания': ('b7_education', 'Ввод зданий: учебные (С-1, накопительно)'),
    'Здравоохранение': ('b8_health', 'Ввод зданий: здравоохранение (С-1, накопительно)'),
    'Другие здания': ('b9_other', 'Ввод зданий: другие (С-1, накопительно)'),
    'Жилые и нежилые здания': ('b0_total', 'Ввод зданий: жилые и нежилые всего (С-1, накопительно)'),
    'построенные населением': ('bp_population', 'Ввод зданий: построено населением (С-1, накопительно)'),
    'построенные юридическими лицами': ('bc_legal', 'Ввод зданий: построено юридическими лицами (С-1, накопительно)'),
}

def main():
    db_tunnel.connect()
    rf_id = 1

    # --- кэши ---
    t0 = __import__('time').time()
    metrics = {r[0]: r[1] for r in db_tunnel.query(
        "SELECT metric_code, metric_id FROM core.metric WHERE metric_code LIKE 'rosstat_c1_%' OR metric_code LIKE 'rosstat_nonres_annual%' OR metric_code LIKE 'rosstat_housing_%';")}
    regions = {}
    for rid, name in db_tunnel.query("SELECT region_id, name_ru FROM core.region;"):
        regions[name] = rid
    # существующие наблюдения этих метрик
    existing = set()
    if metrics:
        ids = ','.join(str(v) for v in metrics.values())
        for mid, ps, rid in db_tunnel.query(
            f"SELECT DISTINCT metric_id, period_start, region_id FROM core.observation_v2 WHERE metric_id IN ({ids});"):
            existing.add((mid, ps, rid))
    print('caches built', round(__import__('time').time()-t0,1), 'metrics:', len(metrics), 'regions:', len(regions), 'existing obs:', len(existing))

    # --- релиз ---
    rel_rows = db_tunnel.query("SELECT release_id FROM core.release WHERE release_label='rosstat_housing_types_2026-09'")
    rel = rel_rows[0][0] if rel_rows else None
    print('release:', rel)
    rows_to_insert = []  # (metric_id, region_id, freq, period_start, period_end, value)

    def ensure_metric(code, name, freq, unit):
        if code in metrics:
            return metrics[code]
        rows_to_insert.append(('METRIC', code, name, freq, unit))
        return None  # вставим в DB отдельно

    # --- источник 1: С-1 по типам ---
    src = sqlite3.connect(os.path.join(WORKDIR, 'data/rosreestr_deals.db'))
    c1 = src.execute('SELECT period, category, buildings_count, area_th_m2 FROM rosstat_buildings_vvod').fetchall()
    new_metric_defs = {}
    for period, cat, cnt, area in c1:
        key = CAT_MAP.get(cat)
        if not key: continue
        slug, name = key
        ps = period + '-01'
        pe = period + '-28'  # приблизительно; уточним ниже
        import datetime
        d = datetime.date.fromisoformat(ps)
        pe = (datetime.date(d.year, d.month, calendar.monthrange(d.year, d.month)[1])).isoformat()
        if area is not None:
            code = f'rosstat_c1_{slug}_area'
            ensure_metric(code, name, 5, 16)
            new_metric_defs[code] = (name, 5, 16, f'С-1 (vv-zd-oper), {period}, накопительно; {cat}; тыс. кв. м, РФ')
            rows_to_insert.append((code, rf_id, 5, ps, pe, float(area)))
        if cnt is not None:
            code = f'rosstat_c1_{slug}_count'
            ensure_metric(code, name + ' — количество зданий', 5, 29)
            new_metric_defs[code] = (name + ' — количество зданий', 5, 29, f'С-1 (vv-zd-oper), {period}, накопительно; {cat}; ед., РФ')
            rows_to_insert.append((code, rf_id, 5, ps, pe, float(cnt)))
    src.close()
    print('C-1 rows collected:', len(rows_to_insert))

    # --- источник 2: годовые нежилые ---
    src = sqlite3.connect(os.path.join(WORKDIR, 'data/rosreestr_deals.db'))
    nr = src.execute('SELECT year, count_thousands, area_mln_m2 FROM rosstat_nonres_buildings').fetchall()
    src.close()
    for year, cnt, area in nr:
        ps = f'{year}-01-01'; pe = f'{year}-12-31'
        if area is not None:
            ensure_metric('rosstat_nonres_annual_area', 'Ввод нежилых зданий: площадь (год)', 3, 32)
            new_metric_defs['rosstat_nonres_annual_area'] = ('Ввод нежилых зданий: площадь (год)', 3, 32, 'Ежегодник Строительство в России; млн м², РФ')
            rows_to_insert.append(('rosstat_nonres_annual_area', rf_id, 3, ps, pe, float(area)))
        if cnt is not None:
            ensure_metric('rosstat_nonres_annual_count', 'Ввод нежилых зданий: количество (год)', 3, 44)
            new_metric_defs['rosstat_nonres_annual_count'] = ('Ввод нежилых зданий: количество (год)', 3, 44, 'Ежегодник; тыс. зданий, РФ')
            rows_to_insert.append(('rosstat_nonres_annual_count', rf_id, 3, ps, pe, float(cnt)))
    print('with annual rows:', len(rows_to_insert))

    # --- источник 3: jil_dom-oper ---
    path = sorted(glob.glob(os.path.join(WORKDIR, 'raw/rosstat/operational/jil_dom-oper_*.xls')))[-1]
    print('file:', os.path.basename(path))
    xls = pd.ExcelFile(path)
    months_ru = {'январь':1,'февраль':2,'март':3,'апрель':4,'май':5,'июнь':6,'июль':7,'август':8,'сентябрь':9,'октябрь':10,'ноябрь':11,'декабрь':12}
    import re
    n_obs = 0
    for sheet in xls.sheet_names:
        m = re.search(r'(\d{4})', sheet)
        mon = None
        for name, num in months_ru.items():
            if name in sheet: mon = num
        if not m or not mon: continue
        year = int(m.group(1)); period = f'{year}-{mon:02d}-01'
        d = pd.Timestamp(period)
        pe = (pd.Timestamp(year, mon, calendar.monthrange(year, mon)[1])).date().isoformat()
        df = pd.read_excel(xls, sheet_name=sheet, header=None)
        if df.shape[1] < 8:
            continue
        for i in range(len(df)):
            name = df.iloc[i, 0]
            if not isinstance(name, str) or not name.strip(): continue
            nm = name.strip().rstrip('1234567890 ')
            rid = regions.get(nm)
            if rid is None: continue
            try:
                v_tot = float(df.iloc[i, 3]); v_pop = float(df.iloc[i, 7])
            except (ValueError, TypeError): continue
            rows_to_insert.append(('rosstat_housing_total_m', rid, 5, period, pe, v_tot))
            rows_to_insert.append(('rosstat_housing_pop_m', rid, 5, period, pe, v_pop))
            n_obs += 1
    print('data rows total:', len(rows_to_insert), '(region-month pairs:', n_obs, ')')

    # --- вставка новых метрик ---
    new_codes = [r[1] for r in rows_to_insert if r[0] == 'METRIC']
    for r in rows_to_insert:
        if r[0] == 'METRIC':
            code, name, freq, unit = r[1], r[2], r[3], r[4]
            desc = new_metric_defs.get(code, ('',))[3]
            db_tunnel.execute(
                "INSERT INTO core.metric (metric_code, name_ru, description, frequency_id, unit_id, metric_type, is_derived, status) VALUES (%s,%s,%s,%s,%s,'primary',false,'active') ON CONFLICT (metric_code) DO NOTHING",
                (code, name, desc, freq, unit))
    if new_codes:
        qmarks = ','.join(['%s'] * len(new_codes))
        for code, mid in db_tunnel.query(f"SELECT metric_code, metric_id FROM core.metric WHERE metric_code IN ({qmarks});", tuple(new_codes)):
            metrics[code] = mid
        print('new metrics inserted:', len(new_codes))

    # --- фильтр существующих + батч-вставка наблюдений ---
    data_rows = [r for r in rows_to_insert if r[0] != 'METRIC']
    to_do = []
    for code, rid, freq, ps, pe, v in data_rows:
        mid = metrics.get(code)
        if mid is None:
            print('MISSING metric', code); continue
        key = (mid, ps, rid)
        if key in existing: continue
        existing.add(key)
        to_do.append((mid, rid, freq, ps, pe, v))
    print('to insert:', len(to_do))
    if to_do:
        CHUNK = 500
        for i in range(0, len(to_do), CHUNK):
            chunk = to_do[i:i+CHUNK]
            values = []
            params = []
            for mid, rid, freq, ps, pe, v in chunk:
                values.append('(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                params.extend([mid, rid, freq, ps, pe, v, 'raw', 'final', SRC_STAT, rel])
            sql = ("INSERT INTO core.observation_v2 (metric_id, region_id, frequency_id, period_start, period_end, value, observation_status, assessment_type, source_id, release_id) VALUES " + ','.join(values) +
                   " ON CONFLICT (metric_id, region_id, frequency_id, period_start, source_id, release_id, assessment_type, sub_dimension) DO NOTHING")
            db_tunnel.execute(sql, tuple(params))
            print('chunk', i//CHUNK+1, 'inserted', len(chunk), flush=True)

    # --- релиз loaded + итог ---
    db_tunnel.execute("UPDATE core.release SET status='loaded' WHERE release_id=%s", (rel,))
    print(db_tunnel.query("""SELECT m.metric_code, COUNT(o.obs_id) FROM core.metric m
        JOIN core.observation_v2 o ON o.metric_id=m.metric_id
        WHERE m.metric_code LIKE 'rosstat_c1_%' OR m.metric_code LIKE 'rosstat_nonres_annual%' OR m.metric_code LIKE 'rosstat_housing_%'
        GROUP BY 1 ORDER BY 1;"""))
    print('DONE')

if __name__ == '__main__':
    main()
