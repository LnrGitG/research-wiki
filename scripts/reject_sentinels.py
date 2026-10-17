#!/usr/bin/env python3
"""Заглушки «нет данных» в каноне: пометить, а не держать числами.

Прежние лендинги кодировали «нет данных» магическими числами: −99 999 999 и
−77 777 777. Пример — численность занятых в строительстве Крыма и Севастополя за
2005–2014 годы, где в источнике прочерк. Пока такие значения лежат в каноне как
обычные, любая средняя, сумма, темп или карта по этим метрикам считаются неверно:
минус сто миллионов не выглядит как пропуск, он выглядит как выброс.

Витрина их уже отфильтровывает (`VAL_OK` в `build_metrics_catalog.py`), но в самой
базе они остаются — и любой прямой SQL их видит.

Что делает скрипт:
  * `--check` — только считает и печатает (ноль значений = молчит, годится для
    сторожа в cron);
  * `APPLY=1` — снимает дамп в `attic/sentinels_before.csv.gz` и помечает строки
    `observation_status='rejected'`. Значения не удаляются: лендинг
    `data/regions_panel.db` и сам канон хранят их для сверки.

Ровно два магических числа, а не «всё отрицательное»: у группы ЕМИСС есть
крупные отрицательные значения (−94,6 млн и подобные), природа которых не
проверена, — их скрипт не трогает и печатает отдельной строкой.

Запуск: python3 scripts/reject_sentinels.py [--check] [APPLY=1]
"""

import argparse
import csv
import gzip
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SENTINELS = (-99999999, -77777777)
DUMP = os.path.join(REPO, 'attic', 'sentinels_before.csv.gz')


def counts():
    """(всего строк-заглушек, разбивка по метрикам, прочие крупные минусы)."""
    total = tunnel.query("""SELECT count(*) FROM data.observation
                            WHERE value = ANY(%s)""", ([SENTINELS[0], SENTINELS[1]],))[0][0]
    live = tunnel.query("""SELECT count(*) FROM data.observation
                           WHERE value = ANY(%s)
                             AND observation_status <> 'rejected'""",
                        ([SENTINELS[0], SENTINELS[1]],))[0][0]
    by_metric = tunnel.query("""
        SELECT m.metric_code, left(m.name_ru, 60), count(*)
        FROM data.observation o JOIN core.metric m USING(metric_id)
        WHERE o.value = ANY(%s) GROUP BY 1,2 ORDER BY 3 DESC""",
        ([SENTINELS[0], SENTINELS[1]],))
    other = tunnel.query("""SELECT count(*), count(distinct metric_id)
                            FROM data.observation
                            WHERE value < -1000000
                              AND NOT (value = ANY(%s))""",
                         ([SENTINELS[0], SENTINELS[1]],))[0]
    return total, live, by_metric, other


def dump():
    rows = tunnel.query("""
        SELECT o.observation_id, o.metric_id, m.metric_code, o.region_id,
               o.period_start::text, o.value::text, o.observation_status,
               o.sub_dimension, r.release_label
        FROM data.observation o
        JOIN core.metric m USING(metric_id)
        LEFT JOIN core.release r USING(release_id)
        WHERE o.value = ANY(%s) ORDER BY m.metric_code, o.period_start""",
                        ([SENTINELS[0], SENTINELS[1]],))
    with gzip.open(DUMP, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['observation_id', 'metric_id', 'metric_code', 'region_id',
                    'period_start', 'value', 'observation_status', 'sub_dimension',
                    'release_label'])
        for r in rows:
            w.writerow([str(x) if x is not None else '' for x in r])
    return len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    total, live, by_metric, other = counts()
    print('заглушек в каноне: %d (без отметки «rejected»: %d)' % (total, live))
    if args.check:
        if live:
            print('ТРЕВОГА: заглушки без отметки — %d' % live)
            for code, name, n in by_metric[:5]:
                print('   %-14s %-54s %d' % ((code or '')[:14], (name or '')[:54], n))
            return 1
        return 0
    if by_metric:
        print('по метрикам (топ-6):')
        for code, name, n in by_metric[:6]:
            print('   %-14s %-54s %d' % ((code or '')[:14], (name or '')[:54], n))
    print('прочие крупные минусы (не заглушки, требуют проверки): %d в %d метриках'
          % (other[0], other[1]))
    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для отметки)')
        return 0
    n = dump()
    print('дамп: %s (%d строк)' % (DUMP, n))
    tunnel.execute("""UPDATE data.observation SET observation_status='rejected'
                      WHERE value = ANY(%s)
                        AND observation_status <> 'rejected'""",
                   ([SENTINELS[0], SENTINELS[1]],))
    total2, live2, _, _ = counts()
    print('после отметки: заглушек %d, без отметки %d' % (total2, live2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
