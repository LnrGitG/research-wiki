#!/usr/bin/env python3
"""Сухой прогон миграции частоты квартал→месяц (A-7, решение — B-2).

Что за дефект. У 721 метрики объявлена квартальная частота (`core.metric.
frequency_id = 6`), а периоды в `data.observation` стоят месячные — в сетке есть
месяцы вне начал кварталов (февраль, март, май…). Дефект опять из прежнего
контура: частота бралась из паспорта группы, а не из фактической сетки периодов.

Что делает скрипт. Считает состав партии и последствия правки, ничего не меняя:
  * сколько метрик и наблюдений затронуто, по источникам и релизам;
  * сколько строк реально поменяет `frequency_id` (только те, где он равен 6);
  * есть ли столкновения с уже существующими строками частоты 5 по ключу
    `ux_observation` (metric, region, period_start, frequency, assessment_type,
    sub_dimension, release): столкновение = потеря строки, поэтому проверяется
    до правки;
  * контроль значений: правка касается только `frequency_id`, значения не
    читаются и не пишутся — равенство значений гарантируется конструкцией, и
    это фиксируется в отчёте как свойство операции, а не как проверка.

Почему без APPLY. Правка ключей уникальности наблюдений меняет чтение всех
потребителей (частотные срезы, свежесть, каталог витрины), поэтому исполнение
ждёт решения владельца по B-2 (`queries/task-queue.md`). Скрипт намеренно не
имеет режима APPLY: сначала отчёт, потом отдельная правка.

Запуск: python3 scripts/migrate_frequency_dryrun.py [--json <путь>]
"""

import argparse
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

CAND = """(SELECT m.metric_id FROM core.metric m WHERE m.frequency_id = 6
             AND EXISTS (SELECT 1 FROM data.observation o
                          WHERE o.metric_id = m.metric_id
                            AND date_part('month', o.period_start) NOT IN (1,4,7,10)))"""

TOTALS = """
    SELECT count(DISTINCT o.metric_id), count(*) FROM data.observation o
     WHERE o.metric_id IN {cand}"""
CHANGE = """
    SELECT count(*) FROM data.observation o
     WHERE o.metric_id IN {cand} AND o.frequency_id = 6"""
STAY = """
    SELECT count(*) FROM data.observation o
     WHERE o.metric_id IN {cand} AND o.frequency_id <> 6"""
COLLIDE = """
    SELECT count(*) FROM data.observation o
     WHERE o.metric_id IN {cand} AND o.frequency_id = 6
       AND EXISTS (SELECT 1 FROM data.observation d
                    WHERE d.metric_id = o.metric_id AND d.region_id = o.region_id
                      AND d.period_start = o.period_start AND d.frequency_id = 5
                      AND d.assessment_type IS NOT DISTINCT FROM o.assessment_type
                      AND d.sub_dimension IS NOT DISTINCT FROM o.sub_dimension
                      AND d.release_id IS NOT DISTINCT FROM o.release_id)"""
BY_SOURCE = """
    SELECT s.name_ru, count(DISTINCT o.metric_id), count(*)
      FROM data.observation o JOIN core.source s ON s.source_id = o.source_id
     WHERE o.metric_id IN {cand} AND o.frequency_id = 6
     GROUP BY 1 ORDER BY 3 DESC"""
BY_RELEASE = """
    SELECT r.label, count(DISTINCT o.metric_id), count(*)
      FROM data.observation o JOIN catalog.release r ON r.release_id = o.release_id
     WHERE o.metric_id IN {cand} AND o.frequency_id = 6
     GROUP BY 1 ORDER BY 3 DESC LIMIT 15"""
ALT1 = """SELECT count(DISTINCT o.metric_id), count(*) FROM data.observation o
   WHERE o.frequency_id = 6 AND o.metric_id IN
     (SELECT m.metric_id FROM core.metric m WHERE m.frequency_id = 6
        AND (SELECT count(DISTINCT date_part('month', o2.period_start)) FROM data.observation o2
              WHERE o2.metric_id = m.metric_id) > 4)"""
ALT2 = """SELECT count(DISTINCT o.metric_id), count(*) FROM data.observation o
   WHERE o.frequency_id = 6 AND o.metric_id IN
     (SELECT metric_id FROM data.observation GROUP BY metric_id
       HAVING count(DISTINCT date_part('month', period_start)) > 4)"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', default='')
    a = ap.parse_args()

    q = lambda sql: tunnel.query(sql.format(cand=CAND))
    n_metrics, n_obs = q(TOTALS)[0]
    will_change = q(CHANGE)[0][0]
    stays = q(STAY)[0][0]
    collide = q(COLLIDE)[0][0]

    print('Партия миграции частоты (квартал → месяц)')
    print('  кандидатов: метрик %s, наблюдений всего %s' % (n_metrics, n_obs))
    print('  поменяют frequency_id 6 → 5: %s строк' % will_change)
    print('  останутся с прежней частотой (в тех же метриках): %s строк' % stays)
    print('  столкновений с существующей строкой частоты 5 по ux_observation: %s' % collide)
    print('  значения: правка касается только поля frequency_id — равенство значений '
          'гарантируется конструкцией')

    print('\nПо источникам (строки, которые изменятся):')
    for name, m, n in q(BY_SOURCE):
        print('  %-34s метрик %-5s строк %s' % (str(name)[:34], m, n))
    print('\nПо релизам (топ-15):')
    for label, m, n in q(BY_RELEASE):
        print('  %-52s метрик %-5s строк %s' % (str(label)[:52], m, n))

    print('\nСверка с числом из реестра (B-2: «726 метрик, 472 730 наблюдений»):')
    for i, sql in enumerate((ALT1, ALT2), 1):
        m, n = tunnel.query(sql)[0]
        print('  определение %d: метрик %s, наблюдений %s' % (i, m, n))
    print('  рабочее определение (по m.frequency_id и месяцы вне начал кварталов): '
          'метрик %s, строк к правке %s' % (n_metrics, will_change))

    out = {'metrics': n_metrics, 'observations_total': n_obs, 'will_change': will_change,
           'stays': stays, 'collisions': collide, 'applied': False}
    if a.json:
        with io.open(a.json, 'w', encoding='utf-8') as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
        print('\nмашинный отчёт: %s' % a.json)
    print('\nПРАВКА НЕ ВЫПОЛНЯЛАСЬ: ждёт решения по B-2.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
