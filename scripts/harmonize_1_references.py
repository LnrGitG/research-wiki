#!/usr/bin/env python3
"""
Гармонизация: рубеж 1 — справочники (source, unit, frequency).

Заполняет core.source, core.unit, core.frequency из фактических
значений в staging: источники берутся из колонок source, единицы —
из unit, частоты выводятся из структуры периода.

Идемпотентно: повторный запуск не создаёт дублей (проверка по коду).
"""
import os, sys, json
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import psycopg

DSN = os.environ.get("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))

# ── справочник источников: код → (название, издатель, url) ──────────
SOURCES = {
    'rosstat':      ('Росстат', 'Федеральная служба государственной статистики',
                     'https://rosstat.gov.ru'),
    'cbr':          ('Банк России', 'Центральный банк Российской Федерации',
                     'https://www.cbr.ru'),
    'domrf':        ('ДОМ.РФ', 'АО «ДОМ.РФ»', 'https://дом.рф'),
    'rosreestr':    ('Росреестр', 'Федеральная служба государственной регистрации',
                     'https://rosreestr.gov.ru'),
    'fns':          ('ФНС России', 'Федеральная налоговая служба',
                     'https://www.nalog.gov.ru'),
    'minfin':       ('Минфин России', 'Министерство финансов РФ',
                     'https://minfin.gov.ru'),
    'smartlab':     ('Smart-Lab', 'Smart-Lab (агрегатор отчётности)',
                     'https://smart-lab.ru'),
    'gks':          ('ЕМИСС / ГКС', 'Единая межведомственная информационно-статистическая система',
                     'https://fedstat.ru'),
    'gdelt':        ('GDELT', 'The GDELT Project', 'https://www.gdeltproject.org'),
    'yandex':       ('Яндекс Wordstat', 'Яндекс', 'https://wordstat.yandex.ru'),
}

# ── единицы измерения: код → (название, описание) ───────────────────
UNITS = {
    'mln_rub':      ('млн руб.', 'миллион рублей'),
    'bln_rub':      ('млрд руб.', 'миллиард рублей'),
    'rub':          ('руб.', 'рубль'),
    'ths_rub':      ('тыс. руб.', 'тысяча рублей'),
    'rub_per_sqm':  ('руб./м²', 'рублей за квадратный метр'),
    'ths_sqm':      ('тыс. м²', 'тысяча квадратных метров'),
    'mln_sqm':      ('млн м²', 'миллион квадратных метров'),
    'sqm':          ('м²', 'квадратный метр'),
    'units':        ('ед.', 'штук, единиц'),
    'ths_units':    ('тыс. ед.', 'тысяча единиц'),
    'pct':          ('%', 'процент'),
    'pct_pts':      ('п.п.', 'процентный пункт'),
    'index':        ('индекс', 'индексный показатель, базис указан отдельно'),
    'ratio':        ('коэф.', 'безразмерный коэффициент'),
    'persons':      ('чел.', 'человек'),
    'ths_persons':  ('тыс. чел.', 'тысяча человек'),
    'months':       ('мес.', 'месяцев'),
    'years':        ('лет', 'годы'),
    'count':        ('шт.', 'количество'),
    'unknown':      ('—', 'единица не определена'),
}

# ── частоты: код → (название, тип периода, месяцев в периоде) ───────
# Ограничения схемы: period_type ∈ {date, month, quarter, year, cumulative},
# months_per_period ∈ [1, 12]. Для дневной и недельной частоты схема не
# предусматривает отдельного типа — используем 'date' с months_per_period=1.
FREQS = {
    'A':  ('годовая', 'year', 12),
    'Q':  ('квартальная', 'quarter', 3),
    'M':  ('месячная', 'month', 1),
    'W':  ('недельная', 'date', 1),
    'D':  ('дневная', 'date', 1),
    'A_snap': ('годовая (снимок)', 'year', 12),
}

# ── сопоставление сырых единиц из staging с кодами ──────────────────
UNIT_MAP = {
    'млн руб': 'mln_rub', 'млн руб.': 'mln_rub', 'млн. руб': 'mln_rub',
    'млрд руб': 'bln_rub', 'млрд руб.': 'bln_rub',
    'руб': 'rub', 'руб.': 'rub', 'руб/м2': 'rub_per_sqm', 'руб/м²': 'rub_per_sqm',
    'руб. за м2': 'rub_per_sqm', 'руб./м²': 'rub_per_sqm', 'руб/кв.м': 'rub_per_sqm',
    'тыс. руб': 'ths_rub', 'тыс.руб': 'ths_rub', 'тыс.руб.': 'ths_rub',
    '%': 'pct', 'процент': 'pct', 'п.п.': 'pct_pts',
    'тыс. м2': 'ths_sqm', 'тыс. м²': 'ths_sqm', 'тыс.м2': 'ths_sqm',
    'м2': 'sqm', 'кв.м': 'sqm', 'кв. м': 'sqm',
    'ед': 'units', 'ед.': 'units', 'штук': 'units', 'единиц': 'units',
    'тыс. ед': 'ths_units',
    'чел.': 'persons', 'чел': 'persons', 'тыс. чел.': 'ths_persons',
}


def upsert_sources(cur, seen):
    """Заполнить core.source по кодам, встреченным в данных."""
    n = 0
    for code in sorted(seen):
        if code not in SOURCES:
            continue
        name, publisher, url = SOURCES[code]
        # reliability ограничен набором official/primary/secondary/derived/unknown
        reliability = 'official' if code in (
            'rosstat', 'cbr', 'domrf', 'rosreestr', 'fns', 'minfin', 'gks') else 'secondary'
        cur.execute("""
            INSERT INTO core.source (source_code, name_ru, publisher, url,
                                     reliability, is_active)
            VALUES (%s, %s, %s, %s, %s, true)
            ON CONFLICT (source_code) DO UPDATE SET
                name_ru = EXCLUDED.name_ru, publisher = EXCLUDED.publisher,
                url = EXCLUDED.url, reliability = EXCLUDED.reliability
        """, (code, name, publisher, url, reliability))
        n += cur.rowcount
    return n


def upsert_units(cur, seen):
    n = 0
    for code in sorted(seen):
        name, desc = UNITS.get(code, UNITS['unknown'])
        cur.execute("""
            INSERT INTO core.unit (unit_code, name_ru, description)
            VALUES (%s, %s, %s)
            ON CONFLICT (unit_code) DO UPDATE SET
                name_ru = EXCLUDED.name_ru, description = EXCLUDED.description
        """, (code, name, desc))
        n += cur.rowcount
    return n


def upsert_freqs(cur, seen):
    n = 0
    for code in sorted(seen):
        name, ptype, months = FREQS.get(code, FREQS['A'])
        cur.execute("""
            INSERT INTO core.frequency (frequency_code, name_ru, period_type, months_per_period)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (frequency_code) DO UPDATE SET
                name_ru = EXCLUDED.name_ru, period_type = EXCLUDED.period_type,
                months_per_period = EXCLUDED.months_per_period
        """, (code, name, ptype, months))
        n += cur.rowcount
    return n


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    # ── собираем фактические значения из staging ──
    print("Сбор значений из staging…", flush=True)

    # какие таблицы имеют нужные колонки
    def tables_with(col):
        cur.execute("""SELECT table_name FROM information_schema.columns
                       WHERE table_schema='staging' AND column_name=%s""", (col,))
        return [r[0] for r in cur.fetchall()]

    unit_tables = tables_with('unit')
    src_tables = tables_with('source')
    print(f"  таблиц с колонкой unit: {len(unit_tables)}")
    print(f"  таблиц с колонкой source: {len(src_tables)}")

    # единицы — по всем таблицам, где колонка есть
    raw_units = set()
    for t in unit_tables:
        cur.execute(f'SELECT DISTINCT lower(trim(unit)) FROM staging."{t}" '
                    f'WHERE unit IS NOT NULL AND trim(unit) <> %s', ('',))
        raw_units |= {r[0] for r in cur.fetchall()}
    raw_units = sorted(raw_units)
    unit_codes = set()
    unmapped = []
    for ru in raw_units:
        code = UNIT_MAP.get(ru)
        if code:
            unit_codes.add(code)
        else:
            unmapped.append(ru)
            unit_codes.add('unknown')
    print(f"  сырых единиц: {len(raw_units)}, распознано кодов: {len(unit_codes)}")
    if unmapped:
        print(f"  не распознано ({len(unmapped)}): {unmapped[:10]}")

    # источники — по всем таблицам, где колонка есть
    raw_sources = set()
    for t in src_tables:
        cur.execute(f'SELECT DISTINCT lower(trim(source)) FROM staging."{t}" '
                    f'WHERE source IS NOT NULL AND trim(source) <> %s', ('',))
        raw_sources |= {r[0] for r in cur.fetchall()}
    raw_sources = sorted(raw_sources)
    print(f"\n  сырых источников: {len(raw_sources)}")
    for s in raw_sources[:20]:
        print(f"    «{s[:60]}»")

    # определяем коды источников: ищем ключевые слова
    src_codes = set()
    for s in raw_sources:
        matched = None
        for k in ('росстат', 'rosstat', 'цб', 'cbr', 'банк россии', 'дом.рф', 'domrf',
                  'росреестр', 'rosreestr', 'фнс', 'fns', 'налог', 'минфин', 'minfin',
                  'smart-lab', 'smartlab', 'емисс', 'fedstat', 'gdelt'):
            if k in s:
                matched = {'росстат': 'rosstat', 'rosstat': 'rosstat',
                           'цб': 'cbr', 'cbr': 'cbr', 'банк россии': 'cbr',
                           'дом.рф': 'domrf', 'domrf': 'domrf',
                           'росреестр': 'rosreestr', 'rosreestr': 'rosreestr',
                           'фнс': 'fns', 'fns': 'fns', 'налог': 'fns',
                           'минфин': 'minfin', 'minfin': 'minfin',
                           'smart-lab': 'smartlab', 'smartlab': 'smartlab',
                           'емисс': 'gks', 'fedstat': 'gks', 'gdelt': 'gdelt'}[k]
                break
        src_codes.add(matched or 'rosstat')
    # плюс источники, известные по структуре таблиц
    src_codes |= {'rosstat', 'cbr', 'domrf', 'rosreestr', 'fns', 'smartlab'}
    print(f"  распознано кодов источников: {len(src_codes)}")

    # ── запись ──
    print("\nЗаполнение справочников…", flush=True)
    print(f"  core.source:    {upsert_sources(cur, src_codes)}")
    # записываем не только найденные в данных, но и весь поддерживаемый
    # набор — парсер единиц может выдать код, которого нет в исходных полях
    all_unit_codes = set(UNITS.keys()) | unit_codes
    print(f"  core.unit:      {upsert_units(cur, all_unit_codes)}")
    print(f"  core.frequency: {upsert_freqs(cur, {'A', 'Q', 'M', 'D'})}")
    conn.commit()

    # ── проверка ──
    print("\n=== ПРОВЕРКА ===")
    for t in ('source', 'unit', 'frequency'):
        cur.execute(f'SELECT count(*) FROM core.{t}')
        print(f"  core.{t}: {cur.fetchone()[0]}")
    cur.execute("SELECT source_code, name_ru FROM core.source ORDER BY source_id")
    print("\nисточники:")
    for c, n in cur.fetchall():
        print(f"    {c:12} {n}")
    cur.execute("SELECT frequency_code, name_ru, period_type FROM core.frequency ORDER BY frequency_id")
    print("\nчастоты:")
    for c, n, p in cur.fetchall():
        print(f"    {c:8} {n:14} ({p})")
    conn.close()


if __name__ == '__main__':
    main()
