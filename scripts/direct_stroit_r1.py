#!/usr/bin/env python3
"""Ввод в действие зданий по Российской Федерации, год — из сборника в канон.

Источник: `raw/rosstat/yearbooks/Stroit_2024/R-1.docx`, таблица 1.3, блок
«Ввод в действие зданий» (три строки): число зданий (тыс.), общий строительный
объём (млн м³), общая площадь (млн м²). Годы в шапке: 2010, 2019, 2020, 2021,
2022, 2023. За 2023 год строительный объём в сборнике не публикуется («–»,
сноска 6: показатель исключён из формы разрешения на ввод приказом Минстроя
от 03.06.2022).

Почему отдельная метрика, а не дополнение `vdzznnrf`. Тот ряд (88 наблюдений,
2000–2021) **сдвинут на год**: 2019-01-01 хранит 326,7 (по сборнику это 2020
год), 2020-01-01 — 403,1 (2021 год), 2021-01-01 — 434,1 (2022 год). Причина —
конвенция прежнего контура «период = год публикации». Пока сдвиг не исправлен
решением владельца (пункт A-8 в queries/task-queue.md), новый ряд пишется
отдельной карточкой с корректными годами и явными единицами в подразрезе;
загрузчик печатает сверку с `vdzznnrf`, чтобы сдвиг был виден числом.

Запуск: python3 scripts/direct_stroit_r1.py [APPLY=1] [PRUNE=period]
"""

import csv
import gzip
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel                                  # noqa: E402
import docx                                                 # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCX = os.path.join(REPO, 'raw', 'rosstat', 'yearbooks', 'Stroit_2024', 'R-1.docx')
RELEASE = 'Stroit_2024/R-1 Table 1.3'
SOURCE = 'rosstat'
METRIC = 'Ввод в действие зданий (Российская Федерация, год)'
DUMP = os.path.join(REPO, 'attic', 'stroit_r1_before.csv.gz')

# строка сборника → (подразрез, единица в каноне)
ROWS = [
    ('число зданий, тыс', 'показатель: число зданий | ед.: тыс. шт.', 'thousand_pcs'),
    ('общий строительный объем зданий', 'показатель: общий строительный объём | ед.: млн м3', 'million_m3'),
    ('общая площадь зданий, млн', 'показатель: общая площадь | ед.: млн м2', 'million_m2'),
]


def number(x):
    if x is None:
        return None
    s = str(x).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    if not s or s in ('-', '–', '—', '...'):
        return None
    s = re.sub(r'[^0-9.\-]', '', s)
    try:
        return float(s)
    except ValueError:
        return None


def parse():
    d = docx.Document(DOCX)
    # нужная таблица — та, где первая колонка начинается с «Ввод в действие зданий:»
    table = None
    for t in d.tables:
        if t.rows and 'ввод в действие зданий' in t.rows[0].cells[0].text.strip().lower():
            table = t
            break
        if t.rows and 'ввод в действие зданий' in ' '.join(
                c.text for c in t.rows[1].cells).lower():
            table = t
            break
    if table is None:
        raise SystemExit('таблица «Ввод в действие зданий» не найдена')
    header = [c.text.strip() for c in table.rows[0].cells]
    years = {}
    for i, h in enumerate(header):
        if re.fullmatch(r'20\d{2}', h):
            years[i] = int(h)
    recs, report = [], []
    found = {}
    in_block = False
    for row in table.rows:
        name = row.cells[0].text.strip().lower().replace('\xa0', ' ')
        if name.startswith('ввод в действие зданий'):
            in_block = True
            continue
        if not in_block:
            continue
        if name.startswith('ввод в действие сооружений'):
            break
        for key, sub, unit in ROWS:
            if name.startswith(key) and key not in found:
                found[key] = True
                for col, year in years.items():
                    val = number(row.cells[col].text)
                    if val is None:
                        report.append('пропуск: %s / %s — нет значения' % (key, year))
                        continue
                    recs.append(dict(metric_name=METRIC, value=val, ps=(year, 0),
                                     region='Российская Федерация', sub=sub,
                                     freq='A', source=SOURCE, unit=unit,
                                     release=RELEASE))
    missing = [k for k, _, _ in ROWS if k not in found]
    if missing:
        report.append('не найдены строки: %s' % ', '.join(missing))
    return recs, report


def shifted_evidence(recs):
    """Сверка с vdzznnrf: показать, что тот ряд сдвинут на год."""
    old = tunnel.query("""
        SELECT EXTRACT(year FROM o.period_start)::int, o.value
        FROM data.observation o JOIN core.metric m USING(metric_id)
        WHERE m.metric_code = 'vdzznnrf'
          AND o.sub_dimension = 'категория: Количество зданий, тыс.'
          AND EXTRACT(year FROM o.period_start) BETWEEN 2019 AND 2021""")
    mine = {r['ps'][0]: r['value'] for r in recs
            if r['sub'].startswith('показатель: число зданий')}
    out = []
    for year, val in sorted(old):
        same = mine.get(year)
        prev = mine.get(year - 1)
        out.append('   %d: vdzznnrf %s | R-1 %s | R-1 за %d: %s'
                   % (year, val, same, year - 1, prev))
    return out


def main():
    recs, report = parse()
    print('разобрано записей: %d' % len(recs))
    for r in report:
        print('  ', r)
    for line in shifted_evidence(recs):
        print(line)
    stats = {}
    for r in recs:
        stats[r['sub']] = stats.get(r['sub'], 0) + 1
    for k, v in stats.items():
        print('   %-52s %d' % (k, v))
    if os.environ.get('APPLY') != '1':
        print('СУХОЙ ПРОГОН (APPLY=1 для записи)')
        return 0
    with gzip.open(DUMP, 'wt', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['metric_code', 'region_id', 'period', 'sub_dimension', 'value'])
        for r in tunnel.query("""
                SELECT m.metric_code, o.region_id, o.period_start::text,
                       o.sub_dimension, o.value::text
                FROM data.observation o JOIN core.metric m USING(metric_id)
                WHERE m.name_ru = %s""", (METRIC,)):
            w.writerow([str(x) if x is not None else '' for x in r])
    print('дамп прежнего состояния: %s' % DUMP)
    from direct_core import Writer  # noqa: E402  (общий писатель канона)
    w = Writer(tag='direct_stroit_r1')
    for r in recs:                      # регион — через механизм Writer (рубеж 6)
        rid, parts = w.resolve_region({'region': r.get('region')}, 'region', None)
        r['region'] = rid          # ingest ждёт идентификатор в поле region
        if parts:
            r['sub'] = '%s | %s' % (r['sub'], ' | '.join(parts))
    prep, ins, conf, new = w.ingest(recs, group='', prune=os.environ.get('PRUNE', ''))
    w.close()
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, new))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
