#!/usr/bin/env python3
"""Прямой загрузчик: приложение к сборнику «Строительство в России» → канон.

Сырьё — приложения к сборнику, распакованные рядом с архивом:
  * `raw/rosstat/yearbooks/Stroit_Pril_2022/Приложение к сборнику (информация в
    разрезе субъектов Российской Федерации) 2022/R_10_2_4_pril.xlsx` (данные за 2021),
  * `raw/rosstat/yearbooks/Stroit_Pril_2024/R_10_2_4_pril.xlsx` (данные за 2023).

Таблица 2.11 «Наличие и состав парка основных строительных машин» (на конец года):
строка «Российская Федерация», далее федеральные округа и субъекты; по каждому виду
машин две колонки — «всего, шт.» и «из них с истёкшим сроком службы, %».

Метрики берём существующие, чтобы не плодить карточки:
  * `pste` — «Парк строительной техники, единиц» (колонка «всего, шт.»),
  * `dtiss` — «Доля техники с истёкшим сроком службы, %» (колонка «из них … %»).
Подразрез: `machine_type: <ключ> | ед.: <единица>`; ключи повторяют прежние
английские (`excavators`, `bulldozers`, `cranes_mobile`, `loaders`), потому что
прежний контур размечал ими те же строки.

Что меняется против прежнего контура и почему это не правка смысла ряда:
  1) частота. Прежние строки помечены КВАРТАЛОМ (`frequency_id` 6), хотя таблица —
     «на конец года»; соседняя таблица 2.10 в том же приложении помечена годовой
     (метрика `y477140028`, `frequency_id` 3). Ставим `A`. Значения и привязка
     периода (1 января года, следующего за отчётным) не меняются — тот же порядок,
     что у SAAR и индексов по субъектам.
  2) `sub_dimension` дополняется единицей измерения (урок 16.10.2026).

Релизы — те, в которых строки лежат сейчас (`Stroit_Pril_2022/R_10_2_4_pril.xlsx`,
`Stroit_Pril_2024/R_10_2_4_pril.xlsx`), иначе ряд оказался бы под двумя релизами.

Отдельный вопрос владельцу (в каноне НЕ трогаем): рядом с этими региональными
строками лежат РФ-значения тех же величин из PDF/docx («Stroit_2022.pdf Table 2.26»,
«Stroit_2024/R-2-4 Table 2.26») с округлением до сотен — 14 500 против 14 502
экскаваторов; предлагается снять их как менее точный дубль.

Запуск: python3 scripts/direct_stroit_pril.py [APPLY=1] [PRUNE=period]
"""

import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer                                  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YB = os.path.join(REPO, 'raw', 'rosstat', 'yearbooks')
SOURCE = 'rosstat'
FREQ = 'A'

FILES = [
    (os.path.join(YB, 'Stroit_Pril_2022',
                  'Приложение к сборнику (информация в разрезе субъектов '
                  'Российской Федерации) 2022', 'R_10_2_4_pril.xlsx'),
     'Stroit_Pril_2022/R_10_2_4_pril.xlsx', 2021),
    (os.path.join(YB, 'Stroit_Pril_2024', 'R_10_2_4_pril.xlsx'),
     'Stroit_Pril_2024/R_10_2_4_pril.xlsx', 2023),
]

# ключевое слово в шапке → ключ подразреза
MACHINES = [('экскаватор', 'excavators'),
            ('бульдозер', 'bulldozers'),
            ('краны передвижн', 'cranes_mobile'),
            ('погрузчик', 'loaders')]

# (имя метрики, признак колонки, единица измерения, метка единицы)
MEASURES = [('Парк строительной техники, единиц', 'всего', 'count', 'ед.: шт.'),
            ('Доля техники с истёкшим сроком службы, %', 'из них', 'pct', 'ед.: %')]


def number(v):
    """Число из ячейки; прочерк и пустое → None."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(',', '.')
    if not s or s in ('-', '–', '—'):
        return None
    return float(s) if re.match(r'^-?\d+(\.\d+)?$', s) else None


def sheet_2_11(ws):
    """(cols, rows): колонки по видам машин и строки данных таблицы 2.11."""
    rows = list(ws.iter_rows(values_only=True))
    hdr = None
    for i, r in enumerate(rows[:12]):
        if r and sum(1 for c in r if c and any(k in str(c).lower()
                                               for k, _ in MACHINES)) >= 2:
            hdr = i
            break
    if hdr is None:
        return None, None
    units = rows[hdr + 1] if hdr + 1 < len(rows) else ()
    cols = {}
    for c, v in enumerate(rows[hdr]):
        if not v:
            continue
        low = str(v).lower()
        for key, code in MACHINES:
            if key in low and code not in cols:
                # колонка «всего» и колонка «из них … %» различаются подписью ниже
                first, second = c, c + 1
                u1 = str(units[first]).lower() if first < len(units) and units[first] else ''
                u2 = str(units[second]).lower() if second < len(units) and units[second] else ''
                if 'всего' in u2 or 'из них' in u1:
                    first, second = second, first
                cols[code] = {'всего': first, 'из них': second}
    first_row = None
    for i, r in enumerate(rows):
        if r and str(r[0] or '').strip().lower().startswith('российская федерация'):
            first_row = i
            break
    if first_row is None:
        return None, None
    data = []
    for r in rows[first_row:]:
        name = str(r[0]).strip() if r and r[0] else ''
        if not name or name.startswith('1)') or name.lower().startswith('по данным'):
            break
        if name.endswith(':') or name.lower() in ('в том числе', 'из них', 'итого'):
            continue          # подзаголовок внутри таблицы, а не территория
        data.append((name, r))
    return cols, data


def parse(w):
    """Записи канона из таблицы 2.11 по всем файлам приложения.

    Регион разрешается сразу (`resolve_region`): писатель канона получает
    идентификатор региона, а части подразреза («состав: …») — из того же
    механизма, что и у остальных прямых загрузчиков.
    """
    recs, report = [], []
    for path, release, year in FILES:
        if not os.path.exists(path):
            report.append('нет файла: %s' % path)
            continue
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for ws in wb.worksheets:
            if not ws.title.startswith('2.11'):
                continue
            cols, data = sheet_2_11(ws)
            if cols is None:
                report.append('%s: шапку 2.11 не разобрали' % release)
                continue
            n, unknown = 0, set()
            for name, r in data:
                rid, parts = w.resolve_region({'region': name}, 'region', None)
                for p in parts:
                    if p.startswith('категория: '):
                        unknown.add(name)
                extra = ' | '.join(parts)
                for mname, kind, unit, ulabel in MEASURES:
                    for key, code in MACHINES:
                        cc = cols.get(code)
                        if cc is None:
                            continue
                        col = cc[kind]
                        val = number(r[col]) if col < len(r) else None
                        if val is None:
                            continue
                        sub = 'machine_type: %s | %s' % (code, ulabel)
                        if extra:
                            sub = '%s | %s' % (extra, sub)
                        recs.append(dict(metric_name=mname, value=val,
                                         ps=(year, 0), region=rid, sub=sub,
                                         freq=FREQ, source=SOURCE, unit=unit,
                                         release=release))
                        n += 1
            report.append('%s (%d): строк %d, записей %d, машин %s'
                          % (release, year, len(data), n, ', '.join(sorted(cols))))
            if unknown:
                report.append('   не опознаны как регион: %s' % ', '.join(sorted(unknown)))
        wb.close()
    return recs, report


def legacy_keys():
    """Ключи «метрика — регион — период» из канона ДО записи (сверка разбора).

    Ограничиваемся релизами приложения: у `pste` есть ещё РФ-строки из PDF/docx
    («Table 2.26», 2020 и 2022) — они к этой таблице не относятся и сверку бы
    засоряли.
    """
    import db_tunnel as tunnel
    rows = tunnel.query("""SELECT m.metric_code, o.region_id, o.period_start::text
                           FROM data.observation o JOIN core.metric m USING(metric_id)
                           JOIN core.release r USING(release_id)
                           WHERE m.metric_code IN ('pste', 'dtiss')
                             AND r.release_label = ANY(%s)""",
                        ([rel for _, rel, _ in FILES],))
    return set((r[0], r[1], r[2]) for r in rows)


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = os.environ.get('PRUNE', '')
    w = Writer(tag='direct_stroit_pril')
    recs, report = parse(w)
    for line in report:
        print('  ' + line)
    print('записей: %d' % len(recs))

    # сверка с прежним контуром: ключи (метрика, регион, период) — что разбор
    # потерял и что добавил. Подразрез здесь намеренно не участвует: он меняется
    # («ед.: …»), и сверка с ним не поймала бы подмену значения.
    before = legacy_keys()
    codes = {'Парк строительной техники, единиц': 'pste',
             'Доля техники с истёкшим сроком службы, %': 'dtiss'}
    mine = set()
    for r in recs:
        mine.add((codes[r['metric_name']], r['region'],
                  '%04d-01-01' % r['ps'][0]))   # ps=(год, 0) → период = 1 января
    lost, added = before - mine, mine - before
    print('сверка: прежних ключей %d | разбор потерял %d | добавил %d'
          % (len(before), len(lost), len(added)))
    if lost:
        print('   ПОТЕРЯНО: %s' % sorted(lost)[:12])
    if added:
        print('   ДОБАВЛЕНО: %s' % sorted(added)[:12])
    if not apply:
        print('СУХОЙ ПРОГОН (APPLY=1 для записи)')
        w.close()
        return 0
    if prune:
        dest = os.path.join(REPO, 'attic', 'stroit_park_before.csv.gz')
        if os.path.exists(dest):
            print('точка возврата уже есть: %s' % dest)
        else:
            n = w.dump_group(['Парк строительной техники, единиц',
                              'Доля техники с истёкшим сроком службы, %'],
                             dest, delete=False)
            print('точка возврата: %s (%d строк)' % (dest, n))
    prep, ins, conf, new = w.ingest(recs, group='', prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, new))
    w.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
