#!/usr/bin/env python3
"""Правка объявленной частоты метрик и наблюдений (B-2 и B-8).

Два направления одного дефекта: частота в каноне расходится с фактической сеткой
периодов.

  q2m (B-2): метрика объявлена квартальной (core.metric.frequency_id = 6), а в
      сетке есть месяцы вне начал кварталов. 723 метрики, 775 526 строк
      наблюдений с частотой 6 → 5.
  m2q (B-8): метрика объявлена месячной (5), а сетка квартальная — различных
      месяцев не больше четырёх при более чем четырёх периодах. 60 метрик,
      181 261 строка 5 → 6.

Что делает APPLY-прогон, по шагам:
  1) фиксирует контрольные суммы по каждой метрике ДО правки (число строк,
     сумма round(value,6), минимальный и максимальный период);
  2) пишет точку возврата — gzip-CSV со всеми observation_id, которые изменятся
     (возврат = UPDATE ... WHERE observation_id IN (дамп));
  3) проверяет столкновения по уникальному ключу ux_observation в целевом
     состоянии: столкновение означает потерю строки, при нём прогон падает;
  4) одной транзакцией меняет frequency_id у наблюдений и у самих карточек
     метрик (иначе дефект остаётся в справочнике);
  5) повторяет контрольные суммы ПОСЛЕ и сравнивает — значения и число строк
     обязаны совпасть до последнего знака.

Запуск:
    python3 scripts/migrate_frequency_apply.py --direction q2m           # отчёт
    APPLY=1 python3 scripts/migrate_frequency_apply.py --direction q2m  # правка
"""

import argparse
import csv
import gzip
import io
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAND_SQL = {
    'q2m': """
        SELECT m.metric_id FROM core.metric m
         WHERE m.frequency_id = 6
           AND EXISTS (SELECT 1 FROM data.observation o
                        WHERE o.metric_id = m.metric_id
                          AND date_part('month', o.period_start) NOT IN (1,4,7,10))""",
    'm2q': """
        SELECT m.metric_id FROM core.metric m
         WHERE m.frequency_id = 5
           AND m.metric_id IN (
               SELECT o.metric_id FROM data.observation o
                WHERE o.frequency_id = 5
                GROUP BY 1
               HAVING count(DISTINCT date_part('month', o.period_start)) <= 4
                  AND count(DISTINCT o.period_start) > 4)""",
}
SRC_FREQ = {'q2m': 6, 'm2q': 5}
DST_FREQ = {'q2m': 5, 'm2q': 6}


def ids(direction):
    return [r[0] for r in tunnel.query(CAND_SQL[direction])]


def checksums(metric_ids, freq):
    """Контрольные суммы по метрикам: (id, строк, сумма, min период, max период)."""
    return {r[0]: (r[1], r[2], r[3], r[4]) for r in tunnel.query("""
        SELECT metric_id, count(*), coalesce(sum(round(value::numeric, 6)), 0)::text,
               min(period_start)::text, max(period_start)::text
          FROM data.observation
         WHERE metric_id = ANY(%s) AND frequency_id = %s
         GROUP BY 1""", (metric_ids, freq))}


def collisions(metric_ids, src, dst):
    """Строки, которые после смены частоты совпадут с уже существующей строкой."""
    return tunnel.query("""
        SELECT count(*) FROM data.observation o
         WHERE o.frequency_id = %s AND o.metric_id = ANY(%s)
           AND EXISTS (SELECT 1 FROM data.observation d
                        WHERE d.metric_id = o.metric_id AND d.region_id = o.region_id
                          AND d.period_start = o.period_start AND d.frequency_id = %s
                          AND d.assessment_type IS NOT DISTINCT FROM o.assessment_type
                          AND d.sub_dimension IS NOT DISTINCT FROM o.sub_dimension
                          AND d.release_id IS NOT DISTINCT FROM o.release_id)""",
                        (src, metric_ids, dst))[0][0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--direction', choices=('q2m', 'm2q'), required=True)
    a = ap.parse_args()
    d = a.direction
    src, dst = SRC_FREQ[d], DST_FREQ[d]

    t0 = time.time()
    metric_ids = ids(d)
    print('направление %s: метрик %d, частота %d → %d' % (d, len(metric_ids), src, dst))
    if not metric_ids:
        print('нечего делать')
        return 0

    rows = tunnel.query("SELECT count(*) FROM data.observation WHERE metric_id = ANY(%s) AND frequency_id = %s",
                        (metric_ids, src))[0][0]
    print('строк к правке: %d' % rows)
    coll = collisions(metric_ids, src, dst)
    print('столкновений по ux_observation в целевом состоянии: %d' % coll)
    if coll:
        print('СТОП: правка потеряла бы %d строк' % coll)
        return 1

    before = checksums(metric_ids, src)
    print('контрольных сумм до правки: %d' % len(before))

    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для правки)')
        return 0

    stamp = time.strftime('%Y%m%d-%H%M%S')
    dump = os.path.join(REPO, 'attic', 'freq_%s_%s.csv.gz' % (d, stamp))
    os.makedirs(os.path.dirname(dump), exist_ok=True)
    ids_rows = tunnel.query("""SELECT observation_id FROM data.observation
                                WHERE metric_id = ANY(%s) AND frequency_id = %s
                                ORDER BY observation_id""", (metric_ids, src))
    with gzip.open(dump, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['observation_id'])
        for r in ids_rows:
            w.writerow([r[0]])
    print('точка возврата: %s (%d строк, %.1f МБ)'
          % (os.path.relpath(dump, REPO), len(ids_rows), os.path.getsize(dump) / 1e6))

    started = time.time()
    n_obs = tunnel.execute("""UPDATE data.observation SET frequency_id = %s
                               WHERE metric_id = ANY(%s) AND frequency_id = %s""",
                           (dst, metric_ids, src))
    n_met = tunnel.execute("UPDATE core.metric SET frequency_id = %s WHERE metric_id = ANY(%s)",
                           (dst, metric_ids))
    print('изменено: наблюдений %d, карточек %d, за %.1f с' % (n_obs, n_met, time.time() - started))

    after = checksums(metric_ids, dst)
    bad = [k for k in before if k not in after or before[k] != after[k]]
    print('сверка контрольных сумм: метрик %d, расхождений %d' % (len(before), len(bad)))
    for k in bad[:5]:
        print('   метрика %s: было %s, стало %s' % (k, before.get(k), after.get(k)))
    left = tunnel.query("""SELECT count(*) FROM data.observation
                            WHERE metric_id = ANY(%s) AND frequency_id = %s""", (metric_ids, src))[0][0]
    print('строк с прежней частотой осталось: %d (должно быть 0)' % left)
    print('итого %.1f с' % (time.time() - t0))
    return 0 if not bad and left == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
