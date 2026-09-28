#!/usr/bin/env python3
"""Инжест прогнозов роста ВВП России от МВФ (WEO/DataMapper) и Всемирного банка (WDI).

Читает сырые JSON из raw/gdp/ (их готовит fetch_gdp_forecasts.py), регистрирует
источники и метрики в схеме core, создаёт релиз (винтаж) и заливает наблюдения
в core.observation_v2 с дисциплиной винтажностей:

  * каждый винтаж (release) привязан к дате публикации/обновления;
  * ON CONFLICT DO NOTHING делает повторный запуск идемпотентным;
  * assessment_type отражает природу значения (final / forecast).

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/ingest_gdp_forecasts.py
"""
import json
import sys
from datetime import date, datetime
from pathlib import Path

# DB utilities (db_tunnel лежит рядом, в scripts/)
from db_tunnel import query, execute, execute_many, available

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / 'raw' / 'gdp'

IMF_CODE = 'imf'
WB_CODE = 'worldbank'

IMF_METRIC = 'gdp_growth_fc_imf'
WB_METRIC = 'gdp_growth_fc_wb_wdi'

REGION_RU = 1          # core.region: 'ru' — Российская Федерация (country)
FREQ_ANNUAL = 3        # core.frequency: 'A'
UNIT_PCT = 12          # core.unit: 'pct'


def ensure_source(code, name_ru, url, publisher=None):
    rows = query("SELECT source_id, reliability FROM core.source WHERE source_code = %s", (code,))
    if rows:
        # Источник мог быть заведён раньше без оценки надёжности — доводим её.
        if not rows[0][1]:
            execute("UPDATE core.source SET reliability = 'official' WHERE source_id = %s", (rows[0][0],))
        return rows[0][0]
    execute(
        "INSERT INTO core.source (source_code, name_ru, publisher, url, reliability) "
        "VALUES (%s, %s, %s, %s, 'official')",
        (code, name_ru, publisher or name_ru, url),
    )
    return query("SELECT source_id FROM core.source WHERE source_code = %s", (code,))[0][0]


def ensure_metric(code, name_ru, short_name_ru, description, unit_id, frequency_id, metric_type='primary'):
    rows = query("SELECT metric_id FROM core.metric WHERE metric_code = %s", (code,))
    if rows:
        # Согласованность типа метрики: значения получены напрямую из источника.
        execute("UPDATE core.metric SET metric_type = %s WHERE metric_code = %s AND metric_type <> %s",
                (metric_type, code, metric_type))
        return rows[0][0]
    execute(
        "INSERT INTO core.metric (metric_code, name_ru, short_name_ru, description, "
        "unit_id, frequency_id, metric_type, status) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, 'active')",
        (code, name_ru, short_name_ru, description, unit_id, frequency_id, metric_type),
    )
    return query("SELECT metric_id FROM core.metric WHERE metric_code = %s", (code,))[0][0]


def ensure_release(label, source_id, published_at, notes, url=None):
    rows = query("SELECT release_id, status FROM core.release WHERE source_id = %s AND release_label = %s",
                 (source_id, label))
    if rows:
        # Винтаж уже зарегистрирован; данные загружены — фиксируем статус.
        if rows[0][1] != 'loaded':
            execute("UPDATE core.release SET status = 'loaded' WHERE release_id = %s", (rows[0][0],))
        return rows[0][0]
    execute(
        "INSERT INTO core.release (source_id, release_label, published_at, url, notes, status) "
        "VALUES (%s, %s, %s, %s, %s, 'loaded')",
        (source_id, label, published_at, url, notes),
    )
    return query("SELECT release_id FROM core.release WHERE release_label = %s", (label,))[0][0]


def assessment_for_year(year, current_year):
    """Год <= прошлого — фактическое значение (final), иначе прогноз (forecast)."""
    return 'final' if year <= current_year - 1 else 'forecast'


OBS_SQL = """
    INSERT INTO core.observation_v2
        (metric_id, region_id, frequency_id, period_start, period_end, value, value_str,
         assessment_type, observation_status, source_id, release_id, quality_flags,
         sub_dimension, notes)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'validated', %s, %s, '{}', '', %s)
    ON CONFLICT DO NOTHING
"""


def ingest_imf():
    json_path = RAW_DIR / 'imf.json'
    if not json_path.exists():
        print('IMF JSON not found', file=sys.stderr)
        return 0
    data = json.loads(json_path.read_text(encoding='utf-8'))
    values = data.get('values', {})
    # Нормализованный файл хранит ряд напрямую; полный ответ DataMapper — вложенно.
    if 'NGDP_RPCH' in values:
        values = values['NGDP_RPCH'].get('RUS', data.get('RUS', {}))
    if not values:
        print('IMF: empty RUS series', file=sys.stderr)
        return 0
    source_id = ensure_source(IMF_CODE, 'Международный валютный фонд', 'https://www.imf.org',
                              publisher='IMF')
    metric_id = ensure_metric(IMF_METRIC, 'Прогноз роста ВВП РФ (МВФ, WEO)',
                              'GDP рост (МВФ)', 'Real GDP growth forecast for Russia, IMF WEO/DataMapper',
                              UNIT_PCT, FREQ_ANNUAL)
    today = date.today()
    label = f'imf_weo_{today.isoformat()}_gdp'
    release_id = ensure_release(label, source_id, today, f'WEO vintage {today.isoformat()}',
                                url='https://www.imf.org/external/datamapper/NGDP_RPCH@WEO/RUS')
    rows = []
    for year_str, val in values.items():
        try:
            year = int(year_str)
        except ValueError:
            continue
        rows.append((
            metric_id, REGION_RU, FREQ_ANNUAL,
            date(year, 1, 1), date(year, 12, 31),
            val, None if val is None else repr(float(val)),
            assessment_for_year(year, today.year), source_id, release_id,
            f'IMF WEO vintage {today.isoformat()}',
        ))
    execute_many(OBS_SQL, rows)
    return len(rows)


def ingest_wb():
    json_path = RAW_DIR / 'wb.json'
    if not json_path.exists():
        print('WB JSON not found', file=sys.stderr)
        return 0
    data = json.loads(json_path.read_text(encoding='utf-8'))
    if not isinstance(data, list) or len(data) < 2:
        print('Unexpected WB format', file=sys.stderr)
        return 0
    meta, records = data[0], data[1]
    lastupdated = meta.get('lastupdated') or date.today().isoformat()
    source_id = ensure_source(WB_CODE, 'Всемирный банк', 'https://data.worldbank.org',
                              publisher='World Bank')
    metric_id = ensure_metric(WB_METRIC, 'Прогноз роста ВВП РФ (Всемирный банк, WDI)',
                              'GDP рост (ВБ)', 'Real GDP growth for Russia, World Bank WDI (NY.GDP.MKTP.KD.ZG)',
                              UNIT_PCT, FREQ_ANNUAL)
    label = f'wb_wdi_{lastupdated}_gdp'
    release_id = ensure_release(label, source_id, lastupdated, f'WDI vintage {lastupdated}',
                                url='https://api.worldbank.org/v2/country/RUS/indicator/NY.GDP.MKTP.KD.ZG')
    rows = []
    for rec in records:
        year = int(rec.get('date'))
        val = rec.get('value')
        if val is None:
            continue
        rows.append((
            metric_id, REGION_RU, FREQ_ANNUAL,
            date(year, 1, 1), date(year, 12, 31),
            val, repr(float(val)),
            assessment_for_year(year, date.today().year), source_id, release_id,
            f'WDI vintage {lastupdated}',
        ))
    execute_many(OBS_SQL, rows)
    return len(rows)


def main():
    if not available(verbose=True):
        print('DB tunnel not available', file=sys.stderr)
        sys.exit(1)
    imf_n = ingest_imf()
    wb_n = ingest_wb()
    print(f'Rows written attempt: IMF={imf_n}, WB={wb_n}')
    for code in (IMF_METRIC, WB_METRIC):
        cnt = query(
            "SELECT count(*) FROM core.observation_v2 o JOIN core.metric m USING (metric_id) "
            "WHERE m.metric_code = %s", (code,),
        )[0][0]
        print(f'  {code}: {cnt} rows in DB')


if __name__ == '__main__':
    main()