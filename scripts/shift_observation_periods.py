#!/usr/bin/env python3
"""Сдвиг периодов наблюдений (исправление систематических сдвигов дат).

Два режима, оба исправляют ошибку размещения значения по времени:

  B-4  --metric vdzznnrf --years -1
       Ряд зданий по РФ (88 наблюдений, 2000–2021) записан годом позже: 2019-01-01
       хранил 326,7 (значение 2020 года по сборнику), 2020-01-01 — 403,1 (2021),
       2021-01-01 — 434,1 (2022). Сдвиг вызван конвенцией прежнего контура «период =
       год публикации».

  B-5  --prefix cbrmon --months 1
       Семья ЦБ-мониторинга (307 368 наблюдений) записана месяцем раньше: данные
       ЦБ за октябрь 2026 (−9,5003) стояли на 2026-09-01, за сентябрь (−6,1928) —
       на 2026-08-01. Сдвиг давал `period_str()` в cbr_monitoring_canon.py: он брал
       дату публикации (dt + 1 месяц) и вычитал два месяца.

Почему не прямым UPDATE. Уникальный индекс `ux_observation` включает
`period_start`, поэтому строка, уезжающая на соседний период, сталкивается с той,
что ещё не уехала; а таблица разбита на партиции по `period_start`, так что
обходной «сдвиг в пустую область» тоже невозможен — партиции там нет. Поэтому
строки копируются с новыми датами во временную таблицу, старые удаляются, новые
вставляются обратно с сохранением `observation_id` — всё одной транзакцией.

Запуск: python3 scripts/shift_observation_periods.py [--metric X | --prefix Y]
       [--years N | --months N] [--freq 3|5|6] [--period YYYY-MM-DD ...]
       [--check] [--apply]
Без --apply — сухой прогон с дампом и печатью до/после.

`--period` ограничивает выборку одним периодом (повторяемый) — нужен там, где
сдвинута не вся метрика, а одна её колонка-год (пример: `vdzrfg`, где первая
колонка сборника помечена 2010, а данные в ней за 2015).
"""

import argparse
import csv
import gzip
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATTC = os.path.join(REPO, 'attic')


def period_list(args):
    """Значения --period: только даты вида YYYY-MM-DD (иначе — стоп).

    Список подставляется в текст SQL (в shift() он собирается строкой), поэтому
    формат проверяется здесь, а не «доверяем аргументу».
    """
    out = []
    for p in (args.period or []):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', p):
            raise SystemExit('--period ждёт дату вида YYYY-MM-DD, получено %r' % p)
        out.append(p)
    return out


def where(args):
    if args.metric:
        cond, params = 'm.metric_code = %s', [args.metric]
    else:
        cond, params = 'm.metric_code LIKE %s', [args.prefix + '%']
    if args.freq:
        cond += ' AND o.frequency_id = %s'
        params.append(args.freq)
    if period_list(args):
        cond += ' AND o.period_start = ANY(%s::date[])'
        params.append(period_list(args))
    return cond, params


def select_sql(args, extra=''):
    cond, params = where(args)
    return ("""SELECT o.observation_id, m.metric_code, o.region_id,
                      o.period_start::text, o.period_end::text,
                      coalesce(o.sub_dimension, ''), o.value::text
               FROM data.observation o JOIN core.metric m USING(metric_id)
               WHERE %s %s""" % (cond, extra)), params


def stats(args):
    sql, params = select_sql(args, """AND o.observation_id IN (
            SELECT observation_id FROM data.observation)""")
    return tunnel.query("""SELECT count(*), min(o.period_start), max(o.period_start)
        FROM data.observation o JOIN core.metric m USING(metric_id)
        WHERE %s""" % where(args)[0], where(args)[1])[0]


def dump(args, path):
    sql, params = select_sql(args)
    rows = tunnel.query(sql, params)
    with gzip.open(path, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['observation_id', 'metric_code', 'region_id', 'period_start',
                    'period_end', 'sub_dimension', 'value'])
        for r in rows:
            w.writerow([str(x) if x is not None else '' for x in r])
    return len(rows)


def shift(args, months):
    """Переписать периоды одной транзакцией: temp-копия, удаление, вставка.

    Прямой UPDATE невозможен по двум причинам: уникальный индекс включает
    period_start (сосед уезжает на занятое место), а таблица разбита на партиции
    по period_start (промежуточная «пустая» область на +1000 лет партиции не имеет).
    Поэтому копируем строки с новыми датами во временную таблицу, удаляем старые
    и вставляем обратно с сохранением observation_id.
    """
    cond = ("m.metric_code = '%s'" % args.metric.replace("'", "''")) if args.metric \
        else ("m.metric_code LIKE '%s%%'" % args.prefix.replace("'", "''"))
    if args.freq:
        cond += ' AND o.frequency_id = %d' % args.freq
    if period_list(args):
        cond += " AND o.period_start = ANY(ARRAY[%s]::date[])" % ', '.join(
            "'%s'" % p for p in period_list(args))
    cols = ('observation_id, metric_id, region_id, period_start, period_end, value, '
            'observation_status, assessment_type, release_id, value_str, frequency_id, '
            'source_id, quality_flags, sub_dimension, notes, created_at')
    sql = """
    CREATE TEMP TABLE shift_tmp ON COMMIT DROP AS
    SELECT o.*,
           (o.period_start + make_interval(months => %(m)d))::date AS _ns,
           CASE WHEN o.period_end IS NULL THEN NULL
                ELSE (o.period_end + make_interval(months => %(m)d))::date END AS _ne
    FROM data.observation o JOIN core.metric m USING(metric_id)
    WHERE %(c)s;
    DELETE FROM data.observation o USING core.metric m
    WHERE o.metric_id = m.metric_id AND %(c)s;
    INSERT INTO data.observation (%(cols)s)
    SELECT observation_id, metric_id, region_id, _ns, _ne, value, observation_status,
           assessment_type, release_id, value_str, frequency_id, source_id,
           quality_flags, sub_dimension, notes, created_at
    FROM shift_tmp;
    """ % {'m': months, 'c': cond, 'cols': cols}
    tunnel.execute(sql)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--metric')
    ap.add_argument('--prefix')
    ap.add_argument('--years', type=int, default=0)
    ap.add_argument('--months', type=int, default=0)
    ap.add_argument('--freq', type=int, help='только эта частота (3=год, 5=мес, 6=кв)')
    ap.add_argument('--period', action='append',
                    help='только строки с этим period_start (YYYY-MM-DD), можно '
                         'повторять — для точечной правки (например, переклеить '
                         'только колонку-год, не трогая остальные)')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()
    if not (a.metric or a.prefix) or not (a.years or a.months):
        ap.error('нужны --metric/--prefix и --years/--months')
    months = a.years * 12 + a.months

    n, lo, hi = stats(a)
    print('затронуто наблюдений: %d, периоды %s .. %s, сдвиг %+d мес.' % (n, lo, hi, months))
    head = tunnel.query(*select_sql(a, 'ORDER BY o.observation_id LIMIT 3'))
    for r in head:
        print('   до: %s (%s) %s %s' % (r[3], r[6], r[0], r[5][:40]))

    if a.check:
        print('режим --check: ничего не меняем')
        return 0
    if not a.apply:
        print('СУХОЙ ПРОГОН (--apply для записи)')
        return 0

    os.makedirs(ATTC, exist_ok=True)
    tag = (a.metric or a.prefix) + '_shift%d' % months
    path = os.path.join(ATTC, 'shift_%s_before.csv.gz' % tag)
    print('дамп: %s (%d строк)' % (path, dump(a, path)))

    shift(a, months)
    n2, lo2, hi2 = stats(a)
    print('после: %d наблюдений, периоды %s .. %s' % (n2, lo2, hi2))
    for r in tunnel.query(*select_sql(a, 'ORDER BY o.period_start DESC LIMIT 3')):
        print('   после: %s %s %s' % (r[3], r[6], r[5][:40]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
