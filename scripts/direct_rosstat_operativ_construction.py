#!/usr/bin/env python3
"""Load Rosstat operational construction work by region (Operativ_MM.xlsx) to canonical DB.

Источник: raw/rosstat/data/Operativ_<MM>_<YYYY>.xlsx. Файл обновляется Росстатом
в конце месяца (последняя публикация — 28.10.2026) и содержит четыре листа:

  1 — уровень: объём работ по «Строительству», накопительно с начала года, млн руб.
  2 — индексы: накопительно с начала года, в % к соответствующему периоду 2025 г.
  3 — индексы: месяц, в % к соответствующему месяцу 2025 г.
  4 — индексы: месяц, в % к предыдущему месяцу

Ранее загружался только лист 1 (уровни), из-за чего в каноне не было ни одной
региональной индексной серии СМР — то есть считался объём, но не темп. Здесь
разбираются все четыре листа; каждая пара «лист → смысл» заводится отдельной
метрикой (уровень в млн руб. и индексы в % — разные единицы, схлопывать нельзя).

Dry-run по умолчанию; APPLY=1 — запись. Загрузчик идемпотентен: метка релиза
строится из имени файла и отметки «Обновлено» внутри него, а перед записью
снимаются строки пары «метрика — релиз» (PRUNE по умолчанию). Снятие обязательно:
листы 3 и 4 идут без подразреза, а Postgres считает NULL-ы в уникальном индексе
различными — без снятия повторный прогон удваивает ряды (проверено 29.10.2026:
лист 3 и лист 4 получили по 1 566 строк вместо 783).

Проверки перед записью (падаем, а не пишем молча):
  * все ожидаемые листы и все непустые месяцы присутствуют;
  * ни одна строка источника не осталась без региона (unmapped);
  * нет дублей ключа (регион, период, подразрез) внутри пачки;
  * территориальные варианты (Архангельская с НАО / без НАО, Тюменская с ХМАО
    и ЯНАО / без) на месте — иначе разрез молча схлопнется.
"""
import os
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from direct_core import Writer          # noqa: E402
from db_tunnel import query            # noqa: E402

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / 'raw' / 'rosstat' / 'data'

SHEET_SPECS = {
    '1': dict(
        metric='Объем работ по виду деятельности «Строительство», накопительным итогом с начала года, млн руб.',
        unit='mln_rub', cumulative=True),
    '2': dict(
        metric='Объем работ по виду деятельности «Строительство», накопительным итогом, '
               'в % к соответствующему периоду предыдущего года',
        unit='pct', cumulative=True),
    '3': dict(
        metric='Объем работ по виду деятельности «Строительство», '
               'в % к соответствующему месяцу предыдущего года',
        unit='pct', cumulative=False),
    '4': dict(
        metric='Объем работ по виду деятельности «Строительство», в % к предыдущему месяцу',
        unit='pct', cumulative=False),
}

MONTH_NUM = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
             'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11,
             'декабрь': 12}
MONTH_NOM = {v: k for k, v in MONTH_NUM.items()}

ALIASES = {
    'Российская Федерация': 'Российская Федерация',
    'г. Москва': 'Москва', 'г. Санкт-Петербург': 'Санкт-Петербург', 'г. Севастополь': 'Севастополь',
    'Республика Северная Осетия - Алания': 'Республика Северная Осетия — Алания',
    'Еврейская авт. область': 'Еврейская автономная область',
    'Чукотский авт. округ': 'Чукотский автономный округ',
    'Кемеровская область': 'Кемеровская область — Кузбасс',
    'Краснодарский край (с учетом ФТ "Сириус")': 'Краснодарский край',
    'Архангельская область': 'Архангельская область (с НАО)',
    'Архангельская область без авт. округа': 'Архангельская область (без НАО)',
    'Ненецкий авт. округ': 'Ненецкий автономный округ',
    'Тюменская область': 'Тюменская область (с ХМАО и ЯНАО)',
    'Тюменская область без авт. округов': 'Тюменская область (без ХМАО и ЯНАО)',
    'Ханты-Мансийский авт. округ': 'Ханты-Мансийский автономный округ — Югра',
    'Ямало-Ненецкий авт. округ': 'Ямало-Ненецкий автономный округ',
}
# Rows with explicit "with AO included" territorial scope are published alongside
# their component regions. The source file's notation encodes scope, so keep it.
ALIAS_REGION_IDS = {
    'Архангельская область': 199,
    'Архангельская область без авт. округа': 30,
    'Тюменская область': 200,
    'Тюменская область без авт. округов': 70,
}
SKIP = {'А', 'Центральный федеральный округ', 'Северо-Западный федеральный округ',
        'Южный федеральный округ', 'Северо-Кавказский федеральный округ',
        'Приволжский федеральный округ', 'Уральский федеральный округ',
        'Сибирский федеральный округ', 'Дальневосточный федеральный округ'}
EXPECTED_TERRITORIAL = {
    'Архангельская область', 'Ненецкий авт. округ', 'Архангельская область без авт. округа',
    'Тюменская область', 'Ханты-Мансийский авт. округ', 'Ямало-Ненецкий авт. округ',
    'Тюменская область без авт. округов',
}


def norm(s):
    return re.sub(r'\s+', ' ', str(s or '')).strip()


def num(v):
    """Число из ячейки; пустое, прочерк и текст → None."""
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    return float(s) if re.match(r'^[-+]?\d*\.?\d+$', s) else None


def latest_file():
    """Свежий Operativ_<MM>_<YYYY>.xlsx по номеру месяца/года в имени (не по mtime)."""
    best = None
    for p in RAW.glob('Operativ_*_*.xlsx'):
        m = re.match(r'^Operativ_(\d{2})_(\d{4})\.xlsx$', p.name)
        if not m:
            continue
        key = (int(m.group(2)), int(m.group(1)))
        if best is None or key > best[0]:
            best = (key, p)
    if best is None:
        raise FileNotFoundError('в %s нет файлов Operativ_MM_YYYY.xlsx' % RAW)
    return best[1]


def source_stamp(wb):
    """Отметка «Обновлено: 28.10.2026» из листа «Содержание» → '2026-10-28'."""
    for row in wb['Содержание'].iter_rows(values_only=True):
        for value in row:
            if isinstance(value, str) and 'Обновлено' in value:
                m = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', value)
                if m:
                    return '%s-%s-%s' % (m.group(3), m.group(2), m.group(1))
                raise ValueError('не разобрана отметка обновления: %r' % value)
    raise ValueError('в листе «Содержание» нет отметки «Обновлено»')


def parse_sheet(ws, sheet_no, year, regions):
    """(строки, имена строк источника). Колонки определяются по шапке месяцев."""
    header, header_idx = None, None
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if row and any(isinstance(v, str) and norm(v).lower() in MONTH_NUM for v in row[1:4]):
            header, header_idx = row, i
            break
    if header is None:
        raise RuntimeError('лист %s: не найдена шапка с месяцами' % sheet_no)
    cols = {}
    for ci, v in enumerate(header):
        if ci == 0 or not isinstance(v, str):
            continue
        label = norm(v).lower()
        words = [w for w in re.split(r'[-\u2013\s]+', label) if w]
        months = [MONTH_NUM[w] for w in words if w in MONTH_NUM]
        if not months:
            continue
        cumulative = SHEET_SPECS[sheet_no]['cumulative']
        cols[ci] = (months[-1], cumulative)

    rows, unmatched, names = [], [], set()
    for row in ws.iter_rows(min_row=header_idx + 1, values_only=True):
        if not row or not isinstance(row[0], str):
            continue
        raw = re.sub(r'\d+\)$', '', norm(row[0])).strip()
        if raw.startswith('в том числе: '):
            raw = norm(raw.replace('в том числе: ', '', 1))
        if raw in SKIP or raw.endswith(':') or re.match(r'^\d', raw):
            continue
        names.add(raw)
        name = ALIASES.get(raw, raw)
        if raw in ALIAS_REGION_IDS:
            rid = ALIAS_REGION_IDS[raw]
        else:
            rid = regions.get(name)
            if rid is None:
                unmatched.append(raw)
                continue
        if name == 'Российская Федерация':
            continue                      # РФ и округа считаются отдельными сериями
        for ci, (month, cumulative) in cols.items():
            if ci >= len(row):
                continue
            value = num(row[ci])
            if value is None:
                continue
            sub = ('накопительно: январь–%s' % MONTH_NOM[month]) if cumulative else None
            rows.append(dict(metric_name=SHEET_SPECS[sheet_no]['metric'], value=value,
                             ps=(year, month), region=rid, sub=sub, freq='M',
                             source='rosstat', release=None,
                             unit=SHEET_SPECS[sheet_no]['unit']))
    if unmatched:
        raise RuntimeError('лист %s: не сопоставлены строки %r' % (sheet_no, sorted(set(unmatched))))
    return rows, names


def build():
    path = latest_file()
    m = re.match(r'^Operativ_(\d{2})_(\d{4})\.xlsx$', path.name)
    month, year = int(m.group(1)), int(m.group(2))
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        missing = [s for s in SHEET_SPECS if s not in wb.sheetnames]
        if missing:
            raise RuntimeError('в %s нет листов %r' % (path.name, missing))
        stamp = source_stamp(wb)
        release = 'Росстат Operativ_%02d.xlsx, обновлено %s' % (month, stamp)
        regions = {r[0]: int(r[1]) for r in query('SELECT name_ru, region_id FROM catalog.region WHERE is_active')}
        if not regions:
            raise RuntimeError('catalog.region вернул пустой список активных регионов')
        rows = []
        for sheet_no in SHEET_SPECS:
            part, names = parse_sheet(wb[sheet_no], sheet_no, year, regions)
            if not EXPECTED_TERRITORIAL.issubset(names):
                raise RuntimeError('лист %s: нет территориальных вариантов %r'
                                   % (sheet_no, sorted(EXPECTED_TERRITORIAL - names)))
            keys = [(r['region'], r['ps'], r['sub']) for r in part]
            if len(keys) != len(set(keys)):
                raise RuntimeError('лист %s: дубли ключа (регион, период, подразрез)' % sheet_no)
            print('лист %s: строк=%d регионов=%d месяцев=%s'
                  % (sheet_no, len(part), len({r['region'] for r in part}),
                     sorted({r['ps'][1] for r in part})))
            rows.extend(part)
        for r in rows:
            r['release'] = release
    finally:
        wb.close()
    print('source=%s; release=%r; всего строк=%d' % (path.name, release, len(rows)))
    print('округов пропущено=8; РФ пропущена (отдельная серия); территориальные варианты сохранены')
    bash = [r for r in rows if r['region'] == regions.get('Республика Башкортостан')]
    print('spot Башкортостан:', [(r['ps'], r['sub'], r['value'], r['metric_name'][-30:]) for r in bash][-4:])
    return rows


if __name__ == '__main__':
    w = Writer(tag='rosstat_operativ_construction', simulate=os.environ.get('APPLY') != '1')
    try:
        recs = build()
        out = w.ingest(recs, group='rosstat_operativ_construction', prune=True)
        print('prepared=%d inserted=%d conflicts=%d new_metrics=%d' % out)
        if os.environ.get('APPLY') != '1':
            print('DRY RUN; set APPLY=1 to write')
    finally:
        w.close()
