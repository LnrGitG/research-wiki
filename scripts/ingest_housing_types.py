#!/usr/bin/env python3
"""Инжест рядов по видам жилищного и нежилого строительства в БД v2.

Источники (локальные, уже в репозитории):
1. data/rosreestr_deals.db → rosstat_buildings_vvod — С-1 по типам
   зданий РФ (жилые/нежилые/детализация, население vs юрлица),
   накопительно 2026-03, 2026-06 → rosstat_btype_* (freq 5=мес,
   unit 16 тыс. м² / 29 шт.), флаг накопительности в description.
2. data/rosreestr_deals.db → rosstat_nonres_buildings — годовые
   нежилые 2000–2024 → rosstat_nonres_annual_area (freq 3 год,
   unit 32 млн м²) и _count (unit 44 тыс. ед.).
3. raw/rosstat/operational/jil_dom-oper_07-2026.xls — ввод жилья
   по регионам: всего и населением (ИЖС), накопительно + месяц,
   % г/г → rosstat_housing_total_m / _pop_m (unit 16), региональный
   разрез (region_id lookup), июль 2026 лист.

Правила: метрики не дублируются (metric_code уникален); наблюдения
не перезаписываются (insert if not exists); регион РФ = region_id
из core.region 'Российская Федерация'.
"""
import os
import glob
import sqlite3
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel

WORKDIR = os.path.expanduser('~/research-wiki-private')
SRC_STAT = 11  # Росстат
CAT_MAP = {
    'Жилые здания': ('b1_residential', 16),
    'Нежилые здания': ('b2_nonresidential', 16),
    'Промышленные здания': ('b3_industrial', 16),
    'Коммерческие здания': ('b4_commercial', 16),
    'Сельскохозяйственные здания': ('b5_agri', 16),
    'Административные здания': ('b6_admin', 16),
    'Учебные здания': ('b7_education', 16),
    'Здравоохранение': ('b8_health', 16),
    'Другие здания': ('b9_other', 16),
    'Жилые и нежилые здания': ('b0_total', 16),
    'построенные населением': ('bp_population', 16),
    'построенные юридическими лицами': ('bc_legal', 16),
}
NAME_RU = {
    'b1_residential': 'Ввод зданий: жилые (С-1, накопительно с начала года)',
    'b2_nonresidential': 'Ввод зданий: нежилые всего (С-1, накопительно)',
    'b3_industrial': 'Ввод зданий: промышленные (С-1, накопительно)',
    'b4_commercial': 'Ввод зданий: коммерческие (С-1, накопительно)',
    'b5_agri': 'Ввод зданий: сельскохозяйственные (С-1, накопительно)',
    'b6_admin': 'Ввод зданий: административные (С-1, накопительно)',
    'b7_education': 'Ввод зданий: учебные (С-1, накопительно)',
    'b8_health': 'Ввод зданий: здравоохранение (С-1, накопительно)',
    'b9_other': 'Ввод зданий: другие (С-1, накопительно)',
    'b0_total': 'Ввод зданий: жилые и нежилые всего (С-1, накопительно)',
    'bp_population': 'Ввод зданий: построено населением (С-1, накопительно)',
    'bc_legal': 'Ввод зданий: построено юридическими лицами (С-1, накопительно)',
}


def ensure_metric(code, name_ru, frequency_id, unit_id, source_id, description=''):
    row = db_tunnel.query(
        "SELECT metric_id FROM core.metric WHERE metric_code=%s", (code,))
    if row:
        return row[0][0]
    db_tunnel.execute(
        """INSERT INTO core.metric
           (metric_code, name_ru, description, frequency_id, unit_id,
            metric_type, is_derived, status)
           VALUES (%s,%s,%s,%s,%s,'primary',false,'active')""",
        (code, name_ru, description, frequency_id, unit_id))
    row = db_tunnel.query(
        "SELECT metric_id FROM core.metric WHERE metric_code=%s", (code,))
    return row[0][0]


def obs_exists(metric_id, region_id, period_start, freq):
    row = db_tunnel.query(
        """SELECT 1 FROM core.observation_v2
           WHERE metric_id=%s AND region_id=%s AND period_start=%s
             AND frequency_id=%s LIMIT 1""",
        (metric_id, region_id, period_start, freq))
    return bool(row)


def ensure_release(source_id, label, notes):
    """Найти или создать релиз; вернуть release_id."""
    row = db_tunnel.query(
        "SELECT release_id FROM core.release WHERE release_label=%s AND source_id=%s",
        (label, source_id))
    if row:
        return row[0][0]
    db_tunnel.execute(
        """INSERT INTO core.release
           (source_id, release_label, ingested_at, status, notes)
           VALUES (%s,%s,now(),'registered',%s)""",
        (source_id, label, notes))
    row = db_tunnel.query(
        "SELECT release_id FROM core.release WHERE release_label=%s AND source_id=%s",
        (label, source_id))
    return row[0][0]


def insert_obs(metric_id, region_id, period_start, value, freq=5, release_id=None):
    if value is None:
        return 0
    if not obs_exists(metric_id, region_id, period_start, freq):
        # period_end: конец месяца/квартала/года
        from datetime import date
        import calendar
        d = date.fromisoformat(period_start) if isinstance(period_start, str) else period_start
        if freq == 3:
            pe = date(d.year, 12, 31)
        elif freq == 6:
            pe = date(d.year, d.month, calendar.monthrange(d.year, d.month)[1])
        else:
            pe = date(d.year, d.month, calendar.monthrange(d.year, d.month)[1])
        db_tunnel.execute(
            """INSERT INTO core.observation_v2
               (metric_id, region_id, frequency_id, period_start, period_end, value,
                observation_status, assessment_type, source_id, release_id)
               VALUES (%s,%s,%s,%s,%s,%s,'raw','final',%s,%s)""",
            (metric_id, region_id, freq, d, pe, value, SRC_STAT, release_id))
        return 1
    return 0


def region_id_rf():
    row = db_tunnel.query(
        "SELECT region_id FROM core.region WHERE name_ru='Российская Федерация' LIMIT 1")
    return row[0][0]


def ingest_c1_buildings(rf_id, rel):
    """С-1 по типам зданий из SQLite rosreestr_deals.db."""
    src = sqlite3.connect(os.path.join(WORKDIR, 'data/rosreestr_deals.db'))
    rows = src.execute(
        'SELECT period, category, buildings_count, area_th_m2 FROM rosstat_buildings_vvod').fetchall()
    n_area, n_cnt = 0, 0
    for period, cat, cnt, area in rows:
        key = CAT_MAP.get(cat)
        if not key:
            print('  skip category:', cat)
            continue
        slug, unit_area = key
        ps = period + '-01'
        if area is not None:
            mid = ensure_metric(
                f'rosstat_c1_{slug}_area', NAME_RU[slug], 5, 16,
                f'Источник: форма C-1 (vv-zd-oper), период {period}, накопительно с начала года; '
                f'категория {cat}; РФ')
            n_area += insert_obs(mid, rf_id, ps, float(area), freq=5, release_id=rel)
        if cnt is not None:
            mid = ensure_metric(
                f'rosstat_c1_{slug}_count', NAME_RU[slug] + ' — количество зданий',
                5, 29,
                f'Источник: форма C-1 (vv-zd-oper), период {period}, накопительно; {cat}, ед.')
            n_cnt += insert_obs(mid, rf_id, ps, float(cnt), freq=5, release_id=rel)
    src.close()
    return n_area, n_cnt


def ingest_nonres_annual(rf_id, rel):
    """Годовые нежилые 2000–2024."""
    src = sqlite3.connect(os.path.join(WORKDIR, 'data/rosreestr_deals.db'))
    rows = src.execute(
        'SELECT year, count_thousands, area_mln_m2, breakout FROM rosstat_nonres_buildings').fetchall()
    n_area, n_cnt = 0, 0
    for year, cnt, area, br in rows:
        if area is not None:
            mid = ensure_metric(
                'rosstat_nonres_annual_area',
                'Ввод нежилых зданий: площадь (год, Росстат/РСЕ)', 3, 32,
                'Годовые ряды, ежегодник Строительство в России, табл. 18.6; млн м²')
            n_area += insert_obs(mid, rf_id, f'{year}-01-01', float(area), freq=3, release_id=rel)
        if cnt is not None:
            mid = ensure_metric(
                'rosstat_nonres_annual_count',
                'Ввод нежилых зданий: количество (год, Росстат/РСЕ)', 3, 44,
                'Годовые ряды; тыс. зданий')
            n_cnt += insert_obs(mid, rf_id, f'{year}-01-01', float(cnt), freq=3, release_id=rel)
    src.close()
    return n_area, n_cnt


def ingest_jil_dom(rf_id, rel):
    """jil_dom-oper: всего жильё + населением, месячный ввод, по регионам."""
    path = sorted(glob.glob(os.path.join(
        WORKDIR, 'raw/rosstat/operational/jil_dom-oper_*.xls')))[-1]
    print('file:', os.path.basename(path))
    xls = pd.ExcelFile(path)
    sheets = [s for s in xls.sheet_names if '2026' in s or '2025' in s]
    sheet = sheets[-1] if sheets else xls.sheet_names[1]
    print('sheet:', sheet)
    df = pd.read_excel(xls, sheet_name=sheet, header=None)
    # колонки: 0 регион, 1 cum_total, 2 % cum, 3 month_total, 4 % м/м г/г,
    #          5 cum_pop, 6 % cum, 7 month_pop, 8 % г/г
    # месяц из заголовка листа: например 'июль 2026' → period
    import re
    m = re.search(r'(\d{4})', sheet)
    months_ru = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5,
                 'июнь': 6, 'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10,
                 'ноябрь': 11, 'декабрь': 12}
    mon = None
    for name, num in months_ru.items():
        if name in sheet:
            mon = num
    year = int(m.group(1))
    if mon is None:
        print('cannot parse month from sheet', sheet)
        return 0, 0
    period = f'{year}-{mon:02d}-01'
    n_total, n_pop = 0, 0
    for i in range(len(df)):
        name = df.iloc[i, 0]
        if not isinstance(name, str) or not name.strip():
            continue
        name = name.strip().rstrip('1234567890 ')
        if name.startswith('Российская Федерация') or 'федеральный округ' in name.lower():
            continue  # только субъекты; РФ и ФО отдельно
        rid = None
        # поиск региона
        for cand in (name, name.replace(' (без НАО)', ''), name + ''):
            row = db_tunnel.query(
                "SELECT region_id FROM core.region WHERE name_ru=%s LIMIT 1", (cand,))
            if row:
                rid = row[0][0]
                break
        if rid is None:
            continue
        try:
            v_tot = float(df.iloc[i, 3])  # месячный ввод всего
            v_pop = float(df.iloc[i, 7])  # месячный ввод населением
        except (ValueError, TypeError):
            continue
        mid_t = ensure_metric(
            'rosstat_housing_total_m',
            'Ввод жилья всего, месяц (Росстат, jil_dom-oper)', 5, 16,
            'Помесячный ввод жилья, тыс. кв. м, по регионам; оперативные данные')
        mid_pop = ensure_metric(
            'rosstat_housing_pop_m',
            'Ввод жилья населением (ИЖС), месяц (Росстат, jil_dom-oper)', 5, 16,
            'Помесячный ввод жилья населением, тыс. кв. м; ИЖС-компонента')
        n_total += insert_obs(mid_t, rid, period, v_tot, release_id=rel)
        n_pop += insert_obs(mid_pop, rid, period, v_pop, release_id=rel)
    return n_total, n_pop


def main():
    db_tunnel.connect()
    rf_id = db_tunnel.query(
        "SELECT region_id FROM core.region WHERE name_ru='Российская Федерация' LIMIT 1")[0][0]
    print('RF region_id:', rf_id)
    rel = ensure_release(
        SRC_STAT, 'rosstat_housing_types_2026-09',
        'Виды строительства в БД v2: С-1 по типам зданий (накопительно 2026), '
        'нежилые годовые, jil_dom-oper помесячно по регионам (июль 2026)')
    print('release_id:', rel)

    a, c = ingest_c1_buildings(rf_id, rel)
    print(f'C-1 buildings: area rows {a}, count rows {c}')
    a, c = ingest_nonres_annual(rf_id, rel)
    print(f'nonres annual: area rows {a}, count rows {c}')
    a, c = ingest_jil_dom(rf_id, rel)
    print(f'jil-dom regions month: total rows {a}, pop rows {c}')

    db_tunnel.execute("UPDATE core.release SET status='loaded' WHERE release_id=%s", (rel,))

    # итог
    rows = db_tunnel.query(
        """SELECT m.metric_code, COUNT(o.obs_id) FROM core.metric m
           JOIN core.observation_v2 o ON o.metric_id=m.metric_id
           WHERE m.metric_code LIKE 'rosstat_c1_%' OR m.metric_code LIKE 'rosstat_nonres_annual%'
              OR m.metric_code LIKE 'rosstat_housing_%'
           GROUP BY 1 ORDER BY 1;""")
    print('=== результат ===')
    for r in rows:
        print(r)


if __name__ == '__main__':
    main()