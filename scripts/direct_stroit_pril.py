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

Таблицы 2.6, 2.7, 2.8, 2.9 (занятость, условия труда, распределение по зарплате)
разбираются из `R_10_2_3_pril.xlsx` того же приложения. Метрики 2.6 и 2.9 в каноне
есть (`y477140044`, `y477140048`), 2.7 и 2.8 — новые. Годы таблицы 2.6 пересекаются
между сборниками (в приложении 2024 года есть и 2005-2021), поэтому год закреплён
за САМЫМ РАННИМ сборником, где он встречается: 2005-2021 из сборника 2022 года,
2022-2023 из сборника 2024 года — как в прежнем контуре; значения из позднего
сборника сверяются и печатаются как ревизии (в канон не пишутся).

Пустые ячейки пропускаются. В прежнем каноне на их месте стояли сентинелы
(−99 999 999 и −77 777 777, например численность работающих в Крыму и Севастополе
за 2005-2014 годы); они сняты вместе с перезаписью группы. Источник сентинелов —
лендинг `data/regions_panel.db` (27 807 значений) — остаётся, если понадобится
вернуть их для сверки.

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

# Второй блок того же приложения — занятость и оплата труда (R_10_2_3_pril.xlsx).
# Релизы здесь НЕ метки файлов: строки 2.6 и 2.9 лежат в каноне под релизами
# сборника, и запись под другим ярлыком задвоила бы ряд.
FILES_23 = [
    (os.path.join(YB, 'Stroit_Pril_2022',
                  'Приложение к сборнику (информация в разрезе субъектов '
                  'Российской Федерации) 2022', 'R_10_2_3_pril.xlsx'),
     'Строительство в России 2022', 2021),
    (os.path.join(YB, 'Stroit_Pril_2024', 'R_10_2_3_pril.xlsx'),
     'Строительство в России 2024', 2023),
]

NAME_EMP = ('Среднегодовая численность работников организаций, занятых '
            'в строительстве')
NAME_WAGE = ('Средняя начисленная заработная плата работников строительных '
             'организаций по категориям персонала')
NAME_HAZ = ('Удельный вес численности работников строительных организаций, '
            'занятых на работах с вредными и (или) опасными условиями труда, %')
NAME_WDIST = ('Распределение численности работников строительных организаций '
              'по размерам начисленной заработной платы, %')
UNIT_EMP = 'ед.: Тысяч человек'

# ключевое слово в шапке → ключ подразреза
MACHINES = [('экскаватор', 'excavators'),
            ('бульдозер', 'bulldozers'),
            ('краны передвижн', 'cranes_mobile'),
            ('погрузчик', 'loaders')]

# (имя метрики, признак колонки, единица измерения, метка единицы)
NAME_PARK = 'Парк строительной техники, единиц'
NAME_AGE = 'Доля техники с истёкшим сроком службы, %'

MEASURES = [(NAME_PARK, 'всего', 'count', 'ед.: шт.'),
            (NAME_AGE, 'из них', 'pct', 'ед.: %')]


def norm_space(v):
    """Строка без переводов строк и кратных пробелов (шапки xlsx)."""
    return re.sub(r'\s+', ' ', str(v)).strip()


def _rid(name):
    """Идентификатор региона и части подразреза — через механизм Writer.

    Инициализируется в main() (см. `set_resolver`): до этого обращения нет.
    """
    return _RESOLVER(name)


_RESOLVER = None


def set_resolver(fn):
    global _RESOLVER
    _RESOLVER = fn


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


def row_of_first_region(rows):
    """Номер строки «Российская Федерация» (начало данных) или None."""
    for i, r in enumerate(rows):
        if r and str(r[0] or '').strip().lower().startswith('российская федерация'):
            return i
    return None


def data_rows(rows, start):
    """Строки территорий: от «Российской Федерации» до сноски."""
    if start is None:
        return []
    out = []
    for r in rows[start:]:
        name = str(r[0]).strip() if r and r[0] else ''
        if not name or name.startswith('1)') or name.lower().startswith('по данным'):
            break
        if name.endswith(':') or name.lower() in ('в том числе', 'из них', 'итого'):
            continue                 # подзаголовок, а не территория
        out.append((name, r))
    return out


def years_in_header(rows):
    """(номер строки шапки, {колонка: год}) — годы ищем по виду «20xx»."""
    for i, r in enumerate(rows[:8]):
        found = {}
        for c, v in enumerate(r or ()):
            if v is None:
                continue
            m = re.fullmatch(r'(20\d{2})(\.0)?', str(v).strip())
            if m:
                found[c] = int(m.group(1))
        if len(found) >= 3:
            return i, found
    return None, {}


def year_owner_map():
    """Какие годы таблицы 2.6 берём из какого сборника.

    Сборники пересекаются (в приложении 2024 года есть и 2005-2021), поэтому год
    закрепляем за САМЫМ РАННИМ сборником, где он встречается — как в прежнем
    контуре: 2005-2021 из сборника 2022 года, 2022-2023 из сборника 2024 года.
    Значения из более позднего сборника сверяем и печатаем расхождения.
    """
    owner = {}
    for idx, (path, _, _) in enumerate(FILES_23):
        if not os.path.exists(path):
            continue
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for ws in wb.worksheets:
            if ws.title.startswith('2.6'):
                _, years = years_in_header(list(ws.iter_rows(values_only=True)))
                for y in set(years.values()):
                    owner.setdefault(y, idx)
        wb.close()
    return owner


def table_2_6(ws, label, idx, owner, taken, rev):
    """2.6 — среднегодовая численность работников: годы идут колонками."""
    rows = list(ws.iter_rows(values_only=True))
    _, years = years_in_header(rows)
    start = row_of_first_region(rows)
    out = []
    for name, r in data_rows(rows, start):
        rid = None
        for c, y in years.items():
            val = number(r[c]) if c < len(r) else None
            if val is None:
                continue
            if rid is None:
                rid, parts = _rid(name)
            key = (y, rid)
            if owner.get(y) != idx:
                # год принадлежит другому сборнику: сверяем ревизию значения
                prev = taken.get(y, {}).get(key)
                if prev is not None and abs(prev - val) > 1e-9:
                    rev.append((y, rid, prev, val))
                continue
            sub = UNIT_EMP + ('' if not parts else ' | ' + ' | '.join(parts))
            out.append(dict(metric_name=NAME_EMP, value=val, ps=(y, 0), region=rid,
                            sub=sub, freq=FREQ, source=SOURCE, unit='persons',
                            release=label))
            taken.setdefault(y, {})[key] = val
    return out


def table_2_9(ws, label, year):
    """2.9 — средняя начисленная заработная плата по категориям персонала."""
    rows = list(ws.iter_rows(values_only=True))
    hdr = next((i for i, r in enumerate(rows[:8]) if r and any(
        isinstance(c, str) and 'все работники' in c.lower() for c in r)), None)
    if hdr is None:
        return []
    cats = {}
    for c, v in enumerate(rows[hdr]):
        if v and str(v).strip() and c > 0:
            # «в том числе» — не категория, а подпись группы: имя категории
            # лежит строкой ниже (руководители, специалисты, …)
            if norm_space(v).lower() in ('в том числе', 'из них'):
                continue
            cats[c] = norm_space(v)
    for c, v in enumerate(rows[hdr + 1] if hdr + 1 < len(rows) else ()):
        if v and str(v).strip() and c > 0 and c not in cats:
            cats[c] = str(v).strip()
    start = row_of_first_region(rows)
    out = []
    for name, r in data_rows(rows, start):
        rid, parts = _rid(name)
        for c, cat in cats.items():
            val = number(r[c]) if c < len(r) else None
            if val is None:
                continue
            sub = 'подраздел: %s | ед.: руб.' % cat
            if parts:
                sub = ' | '.join(parts) + ' | ' + sub
            out.append(dict(metric_name=NAME_WAGE, value=val, ps=(year, 0),
                            region=rid, sub=sub, freq=FREQ, source=SOURCE,
                            unit='rub', release=label))
    return out


def table_2_7(ws, label, year):
    """2.7 — доля занятых на работах с вредными условиями, по факторам."""
    rows = list(ws.iter_rows(values_only=True))
    hdr = next((i for i, r in enumerate(rows[:8]) if r and any(
        isinstance(c, str) and 'занятые на работах' in c.lower() for c in r)), None)
    if hdr is None or hdr + 2 >= len(rows):
        return []
    groups, factors = rows[hdr + 1], rows[hdr + 2]
    gname = {}
    for c, v in enumerate(groups or ()):
        if v and str(v).strip():
            gname[c] = str(v).strip()
    start = row_of_first_region(rows)
    out = []
    for name, r in data_rows(rows, start):
        rid, parts = _rid(name)
        total = number(r[1]) if len(r) > 1 else None
        if total is not None:
            sub = 'фактор: всего | ед.: %'
            if parts:
                sub = ' | '.join(parts) + ' | ' + sub
            out.append(dict(metric_name=NAME_HAZ, value=total, ps=(year, 0),
                            region=rid, sub=sub, freq=FREQ, source=SOURCE,
                            unit='pct', release=label))
        group = None
        for c in range(2, len(factors or ())):
            if c in gname:
                group = gname[c]
            v = factors[c] if c < len(factors) else None
            if not v or not str(v).strip():
                continue
            val = number(r[c]) if c < len(r) else None
            if val is None:
                continue
            sub = 'фактор: %s | ед.: %%' % norm_space(v)
            if group:
                sub = 'группа: %s | %s' % (norm_space(group), sub)
            if parts:
                sub = ' | '.join(parts) + ' | ' + sub
            out.append(dict(metric_name=NAME_HAZ, value=val, ps=(year, 0),
                            region=rid, sub=sub, freq=FREQ, source=SOURCE,
                            unit='pct', release=label))
    return out


def table_2_8(ws, label, year):
    """2.8 — распределение численности по размерам начисленной зарплаты."""
    rows = list(ws.iter_rows(values_only=True))
    hdr = next((i for i, r in enumerate(rows[:8]) if r and sum(
        1 for c in r if isinstance(c, str) and c.strip().lower().startswith(
            ('до ', 'от ', 'свыше'))) >= 3), None)
    if hdr is None:
        return []
    br = {}
    for c, v in enumerate(rows[hdr]):
        if v and str(v).strip() and c > 0:
            br[c] = norm_space(v)
    start = row_of_first_region(rows)
    out = []
    for name, r in data_rows(rows, start):
        rid, parts = _rid(name)
        for c, label_br in br.items():
            val = number(r[c]) if c < len(r) else None
            if val is None:
                continue
            sub = 'интервал: %s | ед.: %%' % label_br
            if parts:
                sub = ' | '.join(parts) + ' | ' + sub
            out.append(dict(metric_name=NAME_WDIST, value=val, ps=(year, 0),
                            region=rid, sub=sub, freq=FREQ, source=SOURCE,
                            unit='pct', release=label))
    return out


def parse_23(w):
    """Записи таблиц 2.6, 2.7, 2.8, 2.9 из приложения (занятость и оплата труда)."""
    seen, rev, recs, report = {}, [], [], []
    owner = year_owner_map()
    for path, label, year in FILES_23:
        if not os.path.exists(path):
            report.append('нет файла: %s' % path)
            continue
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for ws in wb.worksheets:
            title = ws.title
            if title.startswith('2.6'):
                part = table_2_6(ws, label, FILES_23.index((path, label, year)), owner, seen, rev)
            elif title.startswith('2.9'):
                part = table_2_9(ws, label, year)
            elif title.startswith('2.7'):
                part = table_2_7(ws, label, year)
            elif title.startswith('2.8'):
                part = table_2_8(ws, label, year)
            else:
                continue
            if part:
                recs += part
                report.append('  %s / %s: записей %d' % (label, title.strip(), len(part)))
        wb.close()
    if rev:
        report.append('ревизии прежних лет (в канон не пишем, как и прежний контур):')
        for y, rid, old, new in rev[:8]:
            report.append('   %d регион %s: было %s, в новом сборнике %s'
                          % (y, rid, old, new))
    return recs, report


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


ALL_NAMES = None


def name_codes():
    """{имя метрики: код} по тем метрикам группы, что уже есть в каноне."""
    import db_tunnel as tunnel
    global ALL_NAMES
    ALL_NAMES = [NAME_PARK, NAME_AGE, NAME_EMP, NAME_WAGE, NAME_HAZ, NAME_WDIST]
    rows = tunnel.query('SELECT metric_code, name_ru FROM core.metric WHERE name_ru = ANY(%s)',
                        (ALL_NAMES,))
    return dict((r[1], r[0]) for r in rows)


def metric_names():
    """Имена метрик группы, которые уже есть в каноне."""
    return set(name_codes().keys())


def legacy_keys():
    """Ключи «метрика — регион — период» из канона ДО записи (сверка разбора).

    Ограничиваемся релизами приложения: у `pste` есть ещё РФ-строки из PDF/docx
    («Table 2.26», 2020 и 2022) — они к этой таблице не относятся и сверку бы
    засоряли.
    """
    import db_tunnel as tunnel
    out = set()
    rows = tunnel.query("""SELECT m.metric_code, o.region_id, o.period_start::text
                           FROM data.observation o JOIN core.metric m USING(metric_id)
                           JOIN core.release r USING(release_id)
                           WHERE m.metric_code IN ('pste', 'dtiss')
                             AND r.release_label = ANY(%s)""",
                        ([rel for _, rel, _ in FILES],))
    out |= set((r[0], r[1], r[2]) for r in rows)
    rows = tunnel.query("""SELECT m.metric_code, o.region_id, o.period_start::text
                           FROM data.observation o JOIN core.metric m USING(metric_id)
                           JOIN core.release r USING(release_id)
                           WHERE m.name_ru = ANY(%s)
                             AND r.release_label = ANY(%s)""",
                        ([NAME_EMP, NAME_WAGE], [rel for _, rel, _ in FILES_23]))
    out |= set((r[0], r[1], r[2]) for r in rows)
    return out


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = os.environ.get('PRUNE', '')
    w = Writer(tag='direct_stroit_pril')
    set_resolver(lambda name: w.resolve_region({'region': name}, 'region', None))
    recs, report = parse(w)
    more, rep2 = parse_23(w)
    recs += more
    report += rep2
    for line in report:
        print('  ' + line)
    print('записей: %d' % len(recs))

    # сверка с прежним контуром: ключи (метрика, регион, период) — что разбор
    # потерял и что добавил. Подразрез здесь намеренно не участвует: он меняется
    # («ед.: …»), и сверка с ним не поймала бы подмену значения.
    before = legacy_keys()
    new_names = set([NAME_HAZ, NAME_WDIST]) - metric_names()
    codes = name_codes()
    mine = set()
    fresh = 0
    for r in recs:
        nm = r['metric_name']
        if nm in new_names:
            fresh += 1
            continue
        mine.add((codes.get(nm, nm), r['region'],
                  '%04d-01-01' % r['ps'][0]))   # ps=(год, 0) → период = 1 января
    lost, added = before - mine, mine - before
    print('сверка: прежних ключей %d | разбор потерял %d | добавил %d'
          % (len(before), len(lost), len(added)))
    print('новые метрики (в каноне их не было): записей %d' % fresh)
    if lost:
        print('   ПОТЕРЯНО: %s' % sorted(lost)[:12])
    if added:
        print('   ДОБАВЛЕНО: %s' % sorted(added)[:12])
    if not apply:
        print('СУХОЙ ПРОГОН (APPLY=1 для записи)')
        w.close()
        return 0
    if prune:
        dest = os.path.join(REPO, 'attic', 'stroit_pril_before.csv.gz')
        if os.path.exists(dest):
            print('точка возврата уже есть: %s' % dest)
        else:
            n = w.dump_group([NAME_PARK, NAME_AGE, NAME_EMP, NAME_WAGE,
                              NAME_HAZ, NAME_WDIST], dest, delete=False)
            print('точка возврата: %s (%d строк)' % (dest, n))
    prep, ins, conf, new = w.ingest(recs, group='', prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, new))
    w.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
