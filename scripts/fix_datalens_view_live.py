#!/usr/bin/env python3
"""Витрина DataLens должна читать живые справочники, а не замороженные копии.

Инцидент 17.10.2026. Представление `core.v_datalens_observations` было
пересоздано 04.10.2026 при переключении `core` на представления над
`catalog`/`data` — и в его определении остались ссылки на исходные таблицы,
переименованные в `*_legacy`. Те таблицы заморожены снимком на дату
переключения, поэтому всё, что заведено после, читается как NULL:

  * метрик только в `metric_legacy` — 739 (у всех наблюдений НОЛЬ, это мёртвые
    карточки снятых разделов);
  * метрик только в живом `core.metric` — 1671, у 1642 есть наблюдения, всего
    1 097 972 строки; в витрине они шли с пустым кодом и именем;
  * так же мимо витрины проходили 127 релизов и 6 источников, заведённых после
    переключения.

Скрипт сохраняет прежнее определение в `attic/`, пересоздаёт представление на
живых справочниках и проверяет: число строк не изменилось, пустых кодов метрик
не осталось, метрики после переключения видны. Потерь быть не может: все
идентификаторы, которых нет в живых таблицах, наблюдений не имеют.

Запуск: python3 scripts/fix_datalens_view_live.py [APPLY=1]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(REPO, 'attic', 'datalens_view_before.sql')

LIVE = """CREATE OR REPLACE VIEW core.v_datalens_observations AS
 SELECT o.obs_id,
    o.period_start,
    o.period_end,
    (EXTRACT(year FROM o.period_start))::integer AS year,
    (EXTRACT(month FROM o.period_start))::integer AS month,
    (EXTRACT(quarter FROM o.period_start))::integer AS quarter,
    f.frequency_code,
    f.name_ru AS frequency_name,
    m.metric_code,
    m.name_ru AS metric_name,
    m.short_name_ru AS metric_short_name,
    m.metric_type,
    m.is_derived,
    m.tags AS metric_tags,
    u.unit_code,
    u.name_ru AS unit_name,
    r.region_code,
    r.name_ru AS region_name,
    r.level AS region_level,
    r.oktmo,
    o.value,
    o.value_str,
    o.sub_dimension,
    o.assessment_type,
    o.observation_status,
    o.quality_flags,
    s.source_code,
    s.name_ru AS source_name,
    rl.release_label,
    rl.published_at
   FROM ((((((core.observation_v2 o
     LEFT JOIN core.metric m ON ((m.metric_id = o.metric_id)))
     LEFT JOIN core.region r ON ((r.region_id = o.region_id)))
     LEFT JOIN core.frequency f ON ((f.frequency_id = o.frequency_id)))
     LEFT JOIN core.unit u ON ((u.unit_id = m.unit_id)))
     LEFT JOIN core.source s ON ((s.source_id = o.source_id)))
     LEFT JOIN core.release rl ON ((rl.release_id = o.release_id)));"""


def diagnostics():
    total, noname = tunnel.query("""
        SELECT count(*), count(*) FILTER (WHERE metric_code IS NULL)
        FROM core.v_datalens_observations""")[0]
    probe = tunnel.query("""
        SELECT count(*) FROM core.v_datalens_observations
        WHERE metric_code IN ('uvcrsozrvout', 'rcrsornzp', 'iokmrrk')""")[0][0]
    return total, noname, probe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='сторож: молчит, если пустых ярлыков нет')
    args = ap.parse_args()
    total, noname, probe = diagnostics()
    if args.check:
        if noname:
            print('ВИТРИНА: %s строк без кода метрики из %s'
                  % (format(noname, ','), format(total, ',')))
            return 1
        return 0
    print('до правки: строк %s, без кода метрики %s, новых метрик видно %s'
          % (format(total, ','), format(noname, ','), probe))
    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для правки представления)')
        return 0
    old = tunnel.query(
        "SELECT pg_get_viewdef('core.v_datalens_observations'::regclass)")[0][0]
    with open(SNAP, 'w', encoding='utf-8') as fh:
        fh.write(old)
    print('прежнее определение сохранено: %s' % SNAP)
    tunnel.execute(LIVE)
    print('представление пересоздано на живых справочниках')
    total2, noname2, probe2 = diagnostics()
    print('после правки: строк %s, без кода метрики %s, новых метрик видно %s'
          % (format(total2, ','), format(noname2, ','), probe2))
    ok = (total2 == total and noname2 == 0 and probe2 >= probe)
    print('ИТОГ:', 'ПРОШЛО' if ok else 'ТРЕБУЕТ ВНИМАНИЯ')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
