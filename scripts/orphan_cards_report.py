#!/usr/bin/env python3
"""Сторож «активная карточка без наблюдений» (A-6).

Зачем. В каноне живут карточки метрик, заведённые под будущие ряды: карточка
есть, наблюдений нет. Само по себе это не дефект — это план. Дефект начинается,
когда такая карточка считается «активной» и попадает в витрину: читатель видит
метрику, открывает её и не находит ни одной точки. На 17.10.2026 таких карточек
58 (после списания 23 пустых дублей `cbrmon`, где смысловым двойником оказалась
карточка «/ Экономика всего /»).

Что делает. Раз в месяц печатает сводку по активным карточкам без наблюдений с
разбивкой по семействам кодов (по префиксу до первого `_`), чтобы было видно,
какой план буксует: `cbrmon__stroitelst*`, `pm*`/`pn*`/`ppm*`, `vmd*`/`vmn*`.
Полный список с именами пишется в `queries/orphan-cards-ГГГГММ.md`.

Режимы:
    --check   короткая сводка в stdout (для ежедневного джоба свежести)
    (без флага) полный отчёт: печать + файл в queries/

Сторож не чинит и не удаляет ничего: карточка-заготовка — решение владельца,
а не техническая правка.
"""

import argparse
import io
import os
import sys
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQL = """
    SELECT m.metric_code, m.name_ru, m.frequency_id, m.metric_type,
           coalesce(array_to_string(m.tags, ','), ''), m.created_at::text
      FROM core.metric m
     WHERE m.status = 'active'
       AND NOT EXISTS (SELECT 1 FROM data.observation o WHERE o.metric_id = m.metric_id)
     ORDER BY 1
"""


def family(code, tags):
    """Семейство карточки: теги без служебного `v2`, иначе префикс кода.

    Теги размечены содержательно (`stage6` — промпродукция, `housing,mortgage` —
    ипотека), поэтому дают осмысленные группы там, где префикс кода уникален.
    """
    t = ','.join(x for x in (tags or '').split(',') if x and x != 'v2')
    return t or (code.split('_')[0] if '_' in code else code)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()

    rows = tunnel.query(SQL)
    total = len(rows)
    fam = Counter(family(r[0], r[4]) for r in rows)

    if a.check:
        if total == 0:
            return 0
        top = ', '.join('%s %d' % (k, v) for k, v in fam.most_common(4))
        print('Карточки без наблюдений: %d активных (семейства: %s)' % (total, top))
        return 0

    now = datetime.now(timezone.utc)
    path = os.path.join(REPO, 'queries', 'orphan-cards-%s.md' % now.strftime('%Y%m'))
    lines = ['# Активные карточки метрик без наблюдений — %s' % now.strftime('%d.%m.%Y'), '',
             'Всего: **%d**. Группировка по содержательным тегам (служебный `v2` отброшен):' % total, '']
    for k, v in fam.most_common():
        lines.append('- `%s` — %d' % (k, v))
    lines += ['', '| код | имя | частота | тип |', '|---|---|---|---|']
    for code, name, freq, mtype, _tags, _created in rows:
        lines.append('| `%s` | %s | %s | %s |'
                     % (code, (name or '')[:90].replace('|', '/'), freq, mtype))
    lines += ['', 'Карточка без наблюдений — это заготовка под будущий ряд, а не мусор;',
              'удаление или понижение статуса решает владелец. Смысловые двойники',
              'проверяются отдельно: так снялись 23 пустые копии `cbrmon` («все группы»).', '']
    with io.open(path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines))

    print('Активных карточек без наблюдений: %d' % total)
    for k, v in fam.most_common(6):
        print('  %-28s %d' % (k, v))
    print('отчёт: %s' % os.path.relpath(path, REPO))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
