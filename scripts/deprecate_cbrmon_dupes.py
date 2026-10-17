#!/usr/bin/env python3
"""Пометить пустые карточки-дубли «все группы» в семье cbrmon.

Разбор 17.10.2026. В каноне 1395 карточек ЦБ-мониторинга, у 1372 есть данные.
Пустуют 24 карточки, в имени которых стоит «все группы». Источника у них нет:
API ЦБ отдаёт «Мониторинг предприятий» тремя публикациями — 25 «Данные
мониторинга всего» (датасеты по секторам: Экономика всего, Промышленность, …,
Строительство), 27 «Данные мониторинга по группам предприятий» (28 Крупные,
29 Средние, 30 Малые и микро) и 37 «Факторы…». Разреза «все группы» в API нет,
а смысловой двойник каждой такой карточки уже заполнен — карточка с
«/ Экономика всего /» в имени (для строительства это 29 карточек на группу).

Поэтому пустые дубли переводятся в status='deprecated' (не удаляются: карточка
остаётся, чтобы старые ссылки не повисли, и вернуть её — одна строка UPDATE).
Скрипт печатает пары «пустая карточка → заполненный двойник» и падает, если
двойник не найден (тогда это не дубль, а пропуск, и его надо разбирать отдельно).

Запуск: python3 scripts/deprecate_cbrmon_dupes.py [APPLY=1]
"""

import csv
import gzip
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP = os.path.join(REPO, 'attic', 'cbrmon_vse_before.csv.gz')


def empty_cards():
    return tunnel.query("""
        SELECT m.metric_id, m.metric_code, m.name_ru
        FROM core.metric m
        WHERE m.metric_code LIKE 'cbrmon%'
          AND m.name_ru LIKE '%все группы%'
          AND NOT EXISTS (SELECT 1 FROM data.observation o
                          WHERE o.metric_id = m.metric_id)
        ORDER BY m.name_ru""")


def twin_of(name):
    """Заполненный двойник: то же имя с «Экономика всего» вместо «все группы»."""
    alt = name.replace('все группы', 'Экономика всего')
    rows = tunnel.query("""
        SELECT m.metric_id, m.metric_code, left(m.name_ru, 80)
        FROM core.metric m
        WHERE m.metric_code LIKE 'cbrmon%%' AND m.name_ru = %s
          AND EXISTS (SELECT 1 FROM data.observation o WHERE o.metric_id = m.metric_id)""",
                        (alt,))
    return rows[0] if rows else None


def main():
    cards = empty_cards()
    print('пустых карточек «все группы»: %d' % len(cards))
    pairs, orphans = [], []
    for mid, code, name in cards:
        tw = twin_of(name)
        if tw:
            pairs.append((mid, code, name, tw))
        else:
            orphans.append((mid, code, name))
    for mid, code, name, tw in pairs:
        print('   %s\n      → %s (наблюдений у двойника: %s)'
              % (name[:96], tw[1], tunnel.query(
                  'SELECT count(*) FROM data.observation WHERE metric_id=%s',
                  (tw[0],))[0][0]))
    for mid, code, name in orphans:
        print('   БЕЗ ДВОЙНИКА: %s' % name[:96])
    print('пар: %d, сирот: %d' % (len(pairs), len(orphans)))
    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для пометки deprecated)')
        return 0
    if orphans:
        print('ОСТАНОВ: есть карточки без двойника — сначала разобрать их')
        return 1
    with gzip.open(DUMP, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['metric_id', 'metric_code', 'name_ru', 'status'])
        for mid, code, name, _tw in pairs:
            w.writerow([mid, code, name, 'active'])
    print('дамп: %s (%d строк)' % (DUMP, len(pairs)))
    ids = tuple(mid for mid, _, _, _ in pairs)
    tunnel.execute("""UPDATE core.metric SET status='deprecated'
                      WHERE metric_id = ANY(%s)""", (list(ids),))
    left = tunnel.query("""SELECT count(*) FROM core.metric
                           WHERE metric_code LIKE 'cbrmon%%'
                             AND name_ru LIKE '%%все группы%%' AND status <> 'deprecated'""")[0][0]
    print('активных карточек «все группы» осталось: %d' % left)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
