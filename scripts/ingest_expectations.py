#!/usr/bin/env python3
"""Инжест инфляционных ожиданий в БД v2 (релиз 97):
1) inFOM-медианы (7 рядов x 32 мес, янв 2024 - авг 2026) из Infl_exp_26-08.xlsx;
2) макроопрос аналитиков ЦБ (медианы ИПЦ/КС/ВВП по горизонтам, 43 опроса с 2021-05).
Источники:
  raw/cbr/Infl_exp_26-08.xlsx (cbr.ru, статистика inFOM, лист «Данные для графиков»);
  raw/cbr/macro_survey_full.xlsx (cbr.ru/statistics/ddkp/mo_br, full.xlsx).
Запуск: python3 scripts/ingest_expectations.py [--collect]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def extract_infom():
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(REPO, 'raw/cbr/Infl_exp_26-08.xlsx'),
                                read_only=True, data_only=True)
    ws = wb['Данные для графиков']
    rows = list(ws.iter_rows(max_row=130, max_col=93, values_only=True))
    hdr = rows[108]
    series = {
        'infom_observed_median_m': (109, 'Инфляция, наблюдаемая населением, медиана, %'),
        'infom_expected_1y_median_m': (110, 'Инфляционные ожидания населения на год вперёд, медиана, %'),
        'infom_expected_5y_median_m': (111, 'Инфляционные ожидания населения на 5 лет, медиана, %'),
        'infom_observed_savers_m': (114, 'Наблюдаемая инфляция, имеющие сбережения, медиана, %'),
        'infom_observed_nonsavers_m': (115, 'Наблюдаемая инфляция, не имеющие сбережений, медиана, %'),
        'infom_expected_1y_savers_m': (118, 'Ожидания на год, имеющие сбережения, медиана, %'),
        'infom_expected_1y_nonsavers_m': (119, 'Ожидания на год, не имеющие сбережений, медиана, %'),
    }
    out = []
    for code, (li, name) in series.items():
        r = rows[li]
        for j in range(92):
            d, v = hdr[j + 1], r[j + 1]
            if d is not None and v is not None:
                out.append((code, name, str(d.date()), float(v)))
    return out


def extract_macro_survey():
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(REPO, 'raw/cbr/macro_survey_full.xlsx'),
                                read_only=True, data_only=True)
    sheets = {'1': 'macro_survey_cpi_dec_yoy', '3': 'macro_survey_key_rate_avg',
              '4': 'macro_survey_gdp_yoy'}
    out = []
    for s, code in sheets.items():
        ws = wb[s]
        rows = list(ws.iter_rows(max_row=88, max_col=47, values_only=True))
        hdr_i = next(i for i, r in enumerate(rows[:10])
                     if r[3] and 'Прогнозный период' in str(r[3]))
        hdr = rows[hdr_i]
        poll_dates = {j: hdr[j] for j in range(4, 47) if hdr[j] is not None}
        med_start = None
        for i in range(hdr_i + 1, hdr_i + 12):
            r = rows[i]
            if r[1] and 'Медиана' in str(r[1]):
                med_start = i
                continue
            if med_start is not None and r[3]:
                horizon = r[3]
                for j, pd_ in poll_dates.items():
                    v = r[j] if j < len(r) else None
                    if v is not None and str(v) not in ('-', ''):
                        try:
                            out.append((code, str(pd_)[:10], str(horizon)[:10], float(v)))
                        except (ValueError, TypeError):
                            pass
    return out


def ensure_metric(cur, code, name, freq_id, unit_id, metric_type='primary', description=''):
    cur.execute("""SELECT metric_id FROM core.metric WHERE metric_code=%s""", (code,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO core.metric (metric_code, name_ru, description, frequency_id,
        unit_id, metric_type, is_derived, status)
        VALUES (%s, %s, %s, %s, %s, %s, FALSE, 'active') RETURNING metric_id""",
        (code, name, description, freq_id, unit_id, metric_type))
    return cur.fetchone()[0]


def ensure_release(cur, source_id, label):
    cur.execute("""SELECT release_id FROM core.release WHERE release_label=%s""", (label,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO core.release (source_id, release_label, published_at, status)
        VALUES (%s, %s, '2026-09-25', 'registered') RETURNING release_id""", (source_id, label))
    return cur.fetchone()[0]


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    conn = db_tunnel.connect()
    cur = conn.cursor()

    if mode in ('all', 'infom'):
        data = extract_infom()
        rel = ensure_release(cur, 7, 'cbr_infom_expectations_2026-09')
        for code, name, d, v in data:
            mid = ensure_metric(cur, code, name, 5, 12, 'primary',
                                'inFOM для Банка России, медианные оценки (лист «Данные для графиков»)')
            cur.execute("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end, value,
                 assessment_type, observation_status, source_id, release_id)
                VALUES (%s, 1, 5, %s, %s, %s, 'final', 'raw', 7, %s)
                ON CONFLICT DO NOTHING""", (mid, d, d, v, rel))
        print('infom точек:', len(data))
    if mode in ('all', 'survey'):
        data = extract_macro_survey()
        rel = ensure_release(cur, 7, 'cbr_macro_survey_2026-09')
        for code, pd_, horizon, v in data:
            mid = ensure_metric(cur, code, 'Макроопрос аналитиков ЦБ, медиана прогноза', 5, 12,
                                'primary', 'cbr.ru/statistics/ddkp/mo_br, full.xlsx, медианы по горизонтам')
            cur.execute("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end, value,
                 assessment_type, observation_status, source_id, release_id, sub_dimension)
                VALUES (%s, 1, 5, %s, %s, %s, 'final', 'raw', 7, %s, %s)
                ON CONFLICT DO NOTHING""", (mid, pd_, pd_, v, rel, horizon))
        print('survey точек:', len(data))
    conn.commit()
    cur.execute("""UPDATE core.release SET status='loaded'
        WHERE release_label IN ('cbr_infom_expectations_2026-09','cbr_macro_survey_2026-09')
        AND status='registered'""")
    conn.commit()
    print('готово')


if __name__ == '__main__':
    main()