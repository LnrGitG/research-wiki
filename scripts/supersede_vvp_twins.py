#!/usr/bin/env python3
"""Снять карточки-двойники группы «использование ВВП» (A-4).

Что за дефект. В релизе 55 `gdp-quarters-of-use-1995-1kv-2026-elementy-
ispolzovaniya-vvp-2` лежат ДВЕ карточки с одним и тем же рядом: `vvp`
(«ВВП в постоянных ценах (элементы использования), млрд руб.») и `vvp_2`
(«Валовой внутренний продукт»). Значения совпадают до последнего знака
(61 наблюдение, 0 расхождений), подразрез одинаковый. То же в релизе 57:
`vvpi` и `vvpi_2` (57 общих наблюдений, 0 расхождений). Источник дефекта —
двойная разметка при переносе: одно имя дал гармонайзер по описанию ряда,
другое — по имени ряда в источнике.

Почему это опасно. Агрегат по релизу или по источнику удваивает ВВП: любой
потребитель, суммирующий наблюдения группы, получает двойной счёт. Поэтому
двойники помечаются `superseded`, а их карточки — `deprecated`; удаления нет,
дамп снят, возврат — один UPDATE.

Запуск: python3 scripts/supersede_vvp_twins.py [APPLY=1]
"""

import csv
import gzip
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP = os.path.join(REPO, 'attic', 'vvp_twins_before.csv.gz')
PAIRS = [('vvp_2', 'vvp'), ('vvpi_2', 'vvpi')]


def obs(code):
    return dict((str(r[0])[:10], float(r[1])) for r in tunnel.query("""
        SELECT o.period_start, o.value FROM data.observation o
        JOIN core.metric m ON m.metric_id = o.metric_id
        WHERE m.metric_code = %s ORDER BY 1""", (code,)))


def main():
    report, total = [], 0
    for twin, keep in PAIRS:
        a, b = obs(twin), obs(keep)
        common = sorted(set(a) & set(b))
        diffs = [k for k in common if abs(a[k] - b[k]) > 1e-9]
        only = sorted(set(a) - set(b))
        report.append('%s → %s: общих %d, расхождений %d, только у двойника %d'
                      % (twin, keep, len(common), len(diffs), len(only)))
        if diffs or only:
            print('СТОП: %s не является полным двойником %s' % (twin, keep))
            for line in report:
                print('   ', line)
            return 1
        total += len(common)
    for line in report:
        print('   ', line)
    print('итого под снятие: %d наблюдений в %d карточках' % (total, len(PAIRS)))

    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для пометки)')
        return 0

    os.makedirs(os.path.dirname(DUMP), exist_ok=True)
    rows = tunnel.query("""
        SELECT m.metric_code, o.observation_id, o.region_id, o.period_start::text,
               o.value::text, o.observation_status, m.status
        FROM data.observation o JOIN core.metric m ON m.metric_id = o.metric_id
        WHERE m.metric_code = ANY(%s) ORDER BY 1, 4""", ([t for t, _ in PAIRS],))
    with gzip.open(DUMP, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['metric_code', 'observation_id', 'region_id', 'period_start',
                    'value', 'observation_status', 'metric_status'])
        for r in rows:
            w.writerow([str(x) if x is not None else '' for x in r])
    print('дамп: %s (%d строк)' % (DUMP, len(rows)))

    n = tunnel.execute("""
        UPDATE data.observation o SET observation_status = 'superseded'
        FROM core.metric m
        WHERE o.metric_id = m.metric_id AND m.metric_code = ANY(%s)
          AND o.observation_status <> 'superseded'""", ([t for t, _ in PAIRS],))
    tunnel.execute("UPDATE core.metric SET status = 'deprecated' WHERE metric_code = ANY(%s)",
                   ([t for t, _ in PAIRS],))
    print('помечено наблюдений superseded: %d' % n)
    for code in [t for t, _ in PAIRS] + [k for _, k in PAIRS]:
        r = tunnel.query("""SELECT m.metric_code, m.status,
                count(*) FILTER (WHERE o.observation_status = 'superseded'),
                count(*) FILTER (WHERE o.observation_status <> 'superseded')
            FROM core.metric m LEFT JOIN data.observation o ON o.metric_id = m.metric_id
            WHERE m.metric_code = %s GROUP BY 1, 2""", (code,))
        for x in r:
            print('   %-8s карточка %-10s superseded %-3s действующих %s' % (x[0], x[1], x[2], x[3]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
