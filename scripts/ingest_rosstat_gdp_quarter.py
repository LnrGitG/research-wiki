#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Свежая точка Росстата: ИФО ВВП за квартал (первичная публикация).

Регистрирует винтаж (core.release) под конкретную публикацию Росстата и
добавляет наблюдение в метрику `vvpi` («Валовой внутренний продукт (ИФО)»,
индекс физического объёма к соответствующему кварталу прошлого года, %).

Дисциплина винтажностей: каждая публикация Росстата — отдельный релиз, поэтому
предварительная и первая оценки одного квартала сосуществуют (уникальный индекс
observation_v2 включает release_id), а повторный запуск идемпотентен
(ON CONFLICT DO NOTHING).

Пример (II квартал 2026, первая оценка 11.09.2026):
    python3 scripts/ingest_rosstat_gdp_quarter.py \
        --period 2026Q2 --value 101.3 --assessment preliminary \
        --published 2026-09-11 --release rosstat_gdp_2026q2_first_estimate \
        --url https://rosstat.gov.ru/folder/313/document/290165 \
        --notes "первая оценка: ИФО 101,3%, номинал 56166,3 млрд руб, дефлятор 112,5%; предварительная 12.08.2026 — те же 101,3%"
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_tunnel import query, execute, available

SOURCE_ROSSTAT = 11          # core.source: 'rosstat'
REGION_RU = 1
FREQ_QUARTER = 6             # core.frequency: 'Q'
METRIC_CODE = 'vvpi'
SUB_DIMENSION = 'series: Валовой внутренний продукт'
VALID_ASSESSMENT = {'flash', 'preliminary', 'revised', 'final', 'nowcast', 'forecast', 'estimated'}


def parse_period(text):
    m = re.fullmatch(r'(\d{4})[QКqк](\d)', text.strip())
    if not m:
        raise ValueError(f'период задан неверно: {text!r}, ожидается вид 2026Q2')
    year, q = int(m.group(1)), int(m.group(2))
    if q not in (1, 2, 3, 4):
        raise ValueError('квартал должен быть 1..4')
    month = (q - 1) * 3 + 1
    start = date(year, month, 1)
    end = date(year + (q == 4), (month + 2) % 12 + 1, 1)
    from datetime import timedelta
    end = end - timedelta(days=1)
    return start, end


def quarter_end_month(period_start):
    m = period_start.month
    return m + 2


def ensure_release(label, published_at, notes, url):
    rows = query("SELECT release_id, status FROM core.release WHERE source_id=%s AND release_label=%s",
                 (SOURCE_ROSSTAT, label))
    if rows:
        release_id = rows[0][0]
        if rows[0][1] not in ('loaded', 'validated', 'parsed'):
            execute("UPDATE core.release SET status='loaded' WHERE release_id=%s", (release_id,))
        return release_id, False
    release_id = query(
        "INSERT INTO core.release (source_id, release_label, published_at, url, notes, status) "
        "VALUES (%s,%s,%s,%s,%s,'loaded') RETURNING release_id",
        (SOURCE_ROSSTAT, label, published_at, url, notes))[0][0]
    return release_id, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--period', required=True, help='например 2026Q2')
    ap.add_argument('--value', required=True, type=float, help='ИФО ВВП, % к соответствующему кварталу прошлого года')
    ap.add_argument('--assessment', default='preliminary', choices=sorted(VALID_ASSESSMENT))
    ap.add_argument('--published', required=True, help='дата публикации, YYYY-MM-DD')
    ap.add_argument('--release', required=True, help='метка винтажа в core.release')
    ap.add_argument('--url', default=None)
    ap.add_argument('--notes', default='')
    args = ap.parse_args()

    if not available(verbose=True):
        print('Нет доступа к БД (тоннель не поднят)', file=sys.stderr)
        return 1

    start, end = parse_period(args.period)
    published = date.fromisoformat(args.published)

    metric = query("SELECT metric_id, unit_id, frequency_id FROM core.metric WHERE metric_code=%s",
                   (METRIC_CODE,))
    if not metric:
        print(f'метрика {METRIC_CODE} не найдена', file=sys.stderr)
        return 1
    metric_id, unit_id, freq_id = metric[0]

    release_id, created = ensure_release(args.release, published, args.notes, args.url)

    sql = """INSERT INTO core.observation_v2
               (metric_id, region_id, frequency_id, period_start, period_end, value,
                assessment_type, observation_status, source_id, release_id,
                quality_flags, sub_dimension, notes)
             VALUES (%s,%s,%s,%s,%s,%s,%s,'validated',%s,%s,'{}',%s,%s)
             ON CONFLICT (metric_id, region_id, frequency_id, period_start, source_id,
                          release_id, assessment_type, sub_dimension) DO NOTHING"""
    execute(sql, (metric_id, REGION_RU, FREQ_QUARTER, start, end, args.value,
                  args.assessment, SOURCE_ROSSTAT, release_id, SUB_DIMENSION, args.notes or None))

    row = query("""SELECT o.period_start, o.period_end, o.value, o.assessment_type, o.release_id
                   FROM core.observation_v2 o
                   WHERE o.metric_id=%s AND o.period_start=%s AND o.release_id=%s
                     AND o.assessment_type=%s""",
                (metric_id, start, release_id, args.assessment))
    print(f"release_id={release_id} (новый винтаж: {'да' if created else 'нет'}), "
          f"метрика={METRIC_CODE}, unit_id={unit_id}, freq_id={freq_id}")
    print(f"запись: {row[0] if row else 'НЕ НАЙДЕНА'}")
    return 0


if __name__ == '__main__':
    sys.exit(main())