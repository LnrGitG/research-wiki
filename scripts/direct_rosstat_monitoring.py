#!/usr/bin/env python3
"""Загрузчик регионального монитора Росстата в канон (P1: жилищное ядро).

Источник: https://rosstat.gov.ru/folder/11109 → info-stat-MM-YYYY.zip
(«Информация для ведения мониторинга социально-экономического положения
субъектов РФ»). Внутри — 15 разделов, 53 файла, 132 листа; на листе одна
широкая таблица: годы блоками в шапке, внутри годы месяцы или кварталы,
в строках РФ, федеральные округа и субъекты (включая территориальные
варианты «с НАО» / «без НАО»).

Запуск:
    python3 scripts/direct_rosstat_monitoring.py --dir <распакованный архив>
    APPLY=1 python3 scripts/direct_rosstat_monitoring.py --dir ... --files 10-05 03-01

Правила:
  * метрика = (файл, лист, показатель); имя собирается из строки-заголовка
    листа, при неоднозначности дополняется именем листа;
  * тип ряда фиксируется по тексту заголовка: level | index_mom | index_yoy |
    index_ytd | share — смешивать их в одном ряду нельзя;
  * ключ идемпотентности — релиз из имени архива плюс имя файла, запись с
    prune=True по парам (метрика, релиз): в ux_observation входит
    sub_dimension, а Postgres считает NULL-ы различными, поэтому повторный
    прогон без снятия удваивает строки;
  * по умолчанию dry-run, запись только при APPLY=1.
"""
import os
import re
import sys
import glob
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from direct_core import Writer  # noqa: E402

# --- разбор файлов ---------------------------------------------------------

CAP = None   # (год, месяц) выпуска; более поздние периоды — артефакт шапки
YEAR_RE = re.compile(r'^((?:19|20)\d\d)\s*(?:год|г\.?)?\s*[\d\)\s]*$')
MONTHS = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
          'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
QUARTERS = {'i квартал': 1, 'ii квартал': 4, 'iii квартал': 7, 'iv квартал': 10,
            '1 квартал': 1, '2 квартал': 4, '3 квартал': 7, '4 квартал': 10}


def clean(s):
    if s is None:
        return ''
    s = str(s).replace('\xa0', ' ').replace('\n', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(' ', '').replace(',', '.')
    if not s or s in ('-', '—', '...', 'x'):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def read_rows(path):
    """Список листов: [(имя листа, [строки значений])]."""
    out = []
    if path.lower().endswith('.xls'):
        import xlrd
        wb = xlrd.open_workbook(path)
        for sh in wb.sheets():
            rows = [[sh.cell_value(r, c) for c in range(sh.ncols)]
                    for r in range(sh.nrows)]
            out.append((sh.name, rows))
    else:
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for ws in wb.worksheets:
            rows = [list(r) for r in ws.iter_rows(values_only=True)]
            out.append((ws.title, rows))
        wb.close()
    return out


def find_header(rows):
    """(индекс строки годов, [индексы строк периодов]) либо (None, [])."""
    # год ищем только среди текстовых ячеек: числовые значения вида 2016
    # (тысячи рублей) иначе ложно опознаются как «2016 год»
    year_idx, n = None, 0
    for i, row in enumerate(rows[:12]):
        ys = [int(YEAR_RE.match(clean(v)).group(1))
              for v in row[:200]
              if isinstance(v, str) and YEAR_RE.match(clean(v))]
        if len(ys) >= 2 and len(ys) > n:
            year_idx, n = i, len(ys)
    if year_idx is None:
        return None, []
    per = []
    j = year_idx + 1
    while j < min(year_idx + 3, len(rows)):
        row = rows[j]
        hits = 0
        for v in row[:200]:
            if not isinstance(v, str):
                continue
            t = clean(v).lower()
            if not t:
                continue
            if t in QUARTERS or t in ('год', 'i полугодие', 'полугодие'):
                hits += 1
                continue
            head = t.split('-')[0].strip()
            if head in MONTHS:
                hits += 1
        if hits >= 3:
            per.append(j)
            j += 1
        else:
            break
    return year_idx, per


def column_periods(rows, year_idx, per_rows):
    """{индекс колонки: (год, месяц)}; месяц 0 — годовой период."""
    years, cur = {}, None
    for ci, v in enumerate(rows[year_idx]):
        m = YEAR_RE.match(clean(v)) if isinstance(v, str) else None
        if m:
            cur = int(m.group(1))
        if cur:
            years[ci] = cur
    cols, kinds = {}, set()
    if per_rows:
        for ci, y in years.items():
            label = None
            for ri in per_rows:
                if ci < len(rows[ri]):
                    t = clean(rows[ri][ci]).lower() if isinstance(rows[ri][ci], str) else ''
                    if t:
                        label = t
                        break
            if not label:
                continue
            if label in QUARTERS:
                cols[ci] = (y, QUARTERS[label])
                kinds.add('Q')
                continue
            if label == 'год':
                cols[ci] = (y, 0)
                kinds.add('A')
                continue
            if label in ('i полугодие', 'полугодие'):
                cols[ci] = (y, 6)
                kinds.add('Q')
                continue
            parts = [p.strip() for p in label.split('-')]
            if parts[0] in MONTHS:
                m = MONTHS.index(parts[0]) + 1
                if len(parts) > 1 and parts[-1] in MONTHS:
                    m = MONTHS.index(parts[-1]) + 1
                cols[ci] = (y, m)
                kinds.add('M')
    else:
        for ci, y in years.items():
            cols[ci] = (y, 0)
        kinds.add('A')
    freq = 'Q' if 'Q' in kinds else ('M' if 'M' in kinds else 'A')
    return cols, freq


# --- регионы ---------------------------------------------------------------

REGION_FIX = {
    'г. москва': 'москва',
    'г. санкт-петербург': 'санкт-петербург',
    'г. севастополь': 'севастополь',
    'кемеровская область': 'кемеровская область — кузбасс',
    'республика северная осетия - алания': 'республика северная осетия — алания',
    'архангельская область': 'архангельская область (с нао)',
    'архангельская область без автономного округа': 'архангельская область (без нао)',
    'тюменская область': 'тюменская область (с хмао и янао)',
    'тюменская область без автономных округов': 'тюменская область (без хмао и янао)',
    'ненецкий автономный округ': 'ненецкий автономный округ',
    'ханты-мансийский автономный округ - югра': 'ханты-мансийский автономный округ — югра',
    'ямало-ненецкий автономный округ': 'ямало-ненецкий автономный округ',
}
REGION_HINT = re.compile(r'област|край|республик|округ|москва|петербург|'
                         r'севастопол|федерация|чукотск', re.I)


def region_key(label):
    s = clean(label).lower()
    s = re.sub(r'\s*\d\)?\s*$', '', s)          # сноски: «Российская Федерация1»
    s = re.sub(r'^в том числе:?\s*', '', s)     # подстроки автономных округов
    s = re.sub(r',?\s*млрд\.?\s*(руб\w*)', '', s)      # «РФ млрд. рублей»
    s = re.sub(r',?\s*млн\.?\s*руб\w*', '', s)
    s = re.sub(r',\s*млн\.?\s*кв\.?\s*метр.*$', '', s)  # «РФ, млн. кв. метров»
    s = re.sub(r'\s*\d+\s*$', '', s)
    s = s.replace('ё', 'е')
    return REGION_FIX.get(s, s)


# --- единицы и тип ряда ----------------------------------------------------

UNIT_RULES = [
    (r'млн\.?\s*руб', 'mln_rub'),
    (r'тыс\.?\s*руб', 'ths_rub'),
    (r'рублей за кв\.?\s*метр|руб\.? за кв\.?\s*м|на конец квартала, рублей', 'rub_per_sqm'),
    (r'тыс\.?\s*кв\.?\s*метр', 'ths_sqm'),
    (r'млн\.?\s*кв\.?\s*метр', 'mln_sqm'),
    (r'кв\.?\s*метр', 'sqm'),
    (r'тыс\.?\s*человек', 'ths_persons'),
    (r'человек', 'persons'),
    (r'млн\.?\s*тонн|тыс\.?\s*тонн', 'ths_tonnes'),
    (r'процент', 'pct'),
    (r'%', 'pct'),
]


def unit_of(texts):
    blob = ' '.join(clean(t) for t in texts if t).lower()
    for pat, code in UNIT_RULES:
        if re.search(pat, blob):
            return code
    return 'unknown'


def series_type(title, unit):
    t = clean(title).lower()
    if 'к соответствующему периоду' in t or 'к соответств. периоду' in t:
        return 'index_yoy'
    if 'к соответствующему месяц' in t:
        return 'index_yoy'
    if 'к предыдущему месяцу' in t:
        return 'index_mom'
    if 'к декабрю' in t:
        return 'index_ytd'
    if 'доля' in t or 'в % к общему' in t or 'удельный вес' in t:
        return 'share'
    if unit == 'pct':
        return 'index_yoy'
    return 'level'


def freq_of(cols, path):
    months = {m for _, m in cols.values()}
    if months and any(m not in (0, 1, 4, 7, 10) for m in months):
        return 'M'
    if months and any(m in (1, 4, 7, 10) for m in months):
        return 'Q'
    return 'A'


# --- сборка строк ----------------------------------------------------------

CONT_RE = re.compile(r'^(в\s*%|млн|тыс|продолжение|за счет)', re.I)


def sheet_rows(path, sheet_name, rows, file_tag, base_title=None, file_code=''):
    year_idx, per_rows = find_header(rows)
    if year_idx is None:
        return [], None
    cols, freq = column_periods(rows, year_idx, per_rows)
    if not cols:
        return [], None
    ps_list = list(cols.values())
    blocks = {}
    if len(ps_list) != len(set(ps_list)):
        # несколько показателей в одном листе: периоды повторяются по блокам
        order = sorted(cols.items())
        bid, prev = 0, None
        for ci, ps in order:
            if prev is not None and ps <= prev:
                bid += 1
            blocks[ci] = bid
            prev = ps
    start = max(per_rows) + 1 if per_rows else year_idx + 1

    # заголовок показателя и подсказка единицы — первые строки листа
    head = [clean(r[0]) for r in rows[:3] if r]
    head = [h for h in head if h and h.lower() != 'продолжение']
    title = head[0] if head else sheet_name
    title = re.sub(r'\s*\d$', '', title).strip()
    unit = unit_of(head[:2] + [sheet_name])
    stype = series_type(title, unit)

    # листы-продолжения не несут названия показателя — наследуют его от первого
    head_title = title
    if base_title and CONT_RE.match(title):
        head_title = base_title
        name = 'Росстат. Монитор %s: %s — %s' % (file_code, base_title, title)
    else:
        name = 'Росстат. Монитор %s: %s' % (file_code, title)
    if stype != 'level':
        name += ' (%s)' % stype

    def block_title(bid):
        cis = [ci for ci, b in blocks.items() if b == bid]
        if not cis:
            return ''
        c0 = min(cis)
        for ri in range(max(0, year_idx - 3), year_idx):
            v = rows[ri][c0] if c0 < len(rows[ri]) else None
            if isinstance(v, str) and clean(v):
                return clean(v)
        return ''

    out, seen = [], set()
    for row in rows[start:]:
        label = clean(row[0]) if row else ''
        if not label or not REGION_HINT.search(label):
            continue
        key = region_key(label)
        if key in seen:
            continue
        seen.add(key)
        # строка РФ в части листов дана в млн кв. м, а субъекты — в тыс. кв. м:
        # единицу и имя метрики правим построчно, иначе масштаб врёт в 1000 раз
        row_unit, row_name = unit, name
        if re.search(r'млрд', label, re.I):
            row_unit = 'bln_rub'
            row_name = '%s (РФ, млрд руб.)' % name
        elif re.search(r',\s*млн', label, re.I):
            row_unit = 'mln_rub' if row_unit == 'mln_rub' else row_unit
        if blocks:
            row_name = name
        if re.search(r',\s*млн', label, re.I):
            row_unit = 'mln_sqm'
            row_name = '%s (РФ, млн кв. м)' % name
        for ci, ps in cols.items():
            if ci >= len(row):
                continue
            if CAP and (ps[0], ps[1]) > CAP:
                continue
            if blocks:
                bt = block_title(blocks[ci])
                row_name = '%s — %s' % (name, bt) if bt else '%s — блок %d' % (name, blocks[ci] + 1)
            v = num(row[ci])
            if v is None:
                continue
            out.append({'region_key': key, 'region_label': label, 'ps': ps,
                        'value': v, 'metric': row_name, 'unit': row_unit,
                        'freq': freq, 'type': stype})
    return out, {'title': head_title, 'sheet_title': title, 'unit': unit,
                 'type': stype, 'cols': len(cols), 'start': start}


def release_cap(path):
    """Период выпуска из имени каталога: rel-2026-09 / info-stat-09-2026."""
    base = os.path.basename(os.path.normpath(path))
    m = re.search(r'(?:rel-)?(20\d{2})-(\d{2})$', base)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    m = re.search(r'info-stat-(\d{2})-(20\d{2})', base)
    if m:
        return (int(m.group(2)), int(m.group(1)))
    return None


def main(argv):
    global CAP
    apply = os.environ.get('APPLY') == '1'
    root = None
    only = []
    i = 1
    while i < len(argv):
        if argv[i] == '--dir':
            root = argv[i + 1]
            i += 2
        elif argv[i] == '--files':
            only = argv[i + 1].split(',')
            i += 2
        else:
            i += 1
    if not root:
        print('нужен --dir с распакованным архивом')
        return 2

    CAP = release_cap(root)
    rel_tag = os.path.basename(root.rstrip('/'))
    w = Writer(tag='rosstat_monitor', simulate=not apply)
    reg_by_name = {k: v for k, v in w.reg.items()}

    files = sorted(glob.glob(os.path.join(root, '**', '*.xls*'), recursive=True))
    if only:
        files = [f for f in files if any(o in os.path.basename(f) for o in only)]
    print('файлов к разбору: %d, режим %s' % (files and len(files),
                                              'ЗАПИСЬ' if apply else 'dry-run'))

    total_rows, total_ins, missed_regions, per_file = 0, 0, set(), []
    skipped = []
    for path in files:
        stem = os.path.splitext(os.path.basename(path))[0]
        section = os.path.basename(os.path.dirname(path))
        release = '%s: %s' % (rel_tag, stem[:150])
        rows_all = []
        base_title = None
        for sheet_name, rows in read_rows(path):
            code = stem.split()[0] if stem else ''
            got, meta = sheet_rows(path, sheet_name, rows, stem, base_title, code)
            if (meta and meta.get('title') and base_title is None
                    and not CONT_RE.match(meta['title'])):
                base_title = meta['title']
            if not got:
                continue
            # имя метрики уникализируем внутри файла по имени листа
            names = {g['metric'] for g in got}
            for g in got:
                rid = reg_by_name.get(g['region_key'])
                if rid is None:
                    missed_regions.add(g['region_key'])
                    continue
                rows_all.append({'metric_name': g['metric'], 'value': g['value'],
                                 'ps': g['ps'], 'region': rid,
                                 'freq': g['freq'], 'unit': g['unit'],
                                 'source': 'rosstat', 'release': release,
                                 'sub': None})
        if not rows_all:
            print('  %-58s нет данных' % stem[:58])
            continue
        prep, ins, confl, newm = w.ingest(rows_all, group=section,
                                          verbose=False, prune=True)
        total_rows += prep
        total_ins += ins
        per_file.append((stem, len(rows_all), prep, ins, newm))
        print('  %-58s строк %6d подгот %6d вставл %6d метрик %3d'
              % (stem[:58], len(rows_all), prep, ins, newm))

    w.close()
    print('\nитого строк %d, подготовлено %d, вставлено %d'
          % (total_rows, sum(p[2] for p in per_file), total_ins))
    if skipped:
        print('\nпропущены многоблочные листы (%d) — нужен ручной маппинг блоков:' % len(skipped))
        for sk in skipped:
            print('   ', sk)
    if missed_regions:
        print('не опознаны регионы (%d):' % len(missed_regions))
        for m in sorted(missed_regions)[:20]:
            print('   ', m)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
