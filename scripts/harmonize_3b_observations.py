#!/usr/bin/env python3
"""
Гармонизация: рубеж 3б — наблюдения (core.observation).

Переносит строки из staging в целевую модель:
  * регион определяется по справочнику (алиасы + имена);
  * нерегиональные подписи (годы, кварталы, виды работ) → sub_dimension,
    регион при этом «Российская Федерация»;
  * показатель берётся из core.metric по названию или коду;
  * период разбирается в period_start/period_end;
  * версия оценки: 'final' для закрытых периодов, 'preliminary' для текущего года.

Запуск: python3 harmonize_3b_observations.py [--group NAME] [--dry-run]
"""
import os, sys, re, json, collections
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
import psycopg

DSN = os.environ.get("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
CUR_YEAR = 2026

# ── единица: сырой текст → код core.unit ────────────────────────────
import csv
def _load_unit_map():
    from unit_parser import UNIT_IN_TEXT
    return UNIT_IN_TEXT

UNITS_SIMPLE = {
    'млн руб': 'mln_rub', 'млн руб.': 'mln_rub', 'млрд руб': 'bln_rub',
    'руб': 'rub', 'руб.': 'rub', '%': 'pct', 'процент': 'pct',
    'тыс. м2': 'ths_sqm', 'тыс. м²': 'ths_sqm', 'м2': 'sqm', 'кв.м': 'sqm',
    'ед': 'units', 'ед.': 'units', 'count': 'units', 'шт': 'units',
    'млн м2': 'mln_sqm', 'млн м²': 'mln_sqm', 'mln_rub': 'mln_rub',
    'млн руб': 'mln_rub', 'rub_per_sqm': 'rub_per_sqm', 'pct': 'pct',
}

SUB_DIM_PATTERNS = [
    (r'^\d{4}(\.0)?\d?\)?$', 'год'),          # 2002.0, 20251)
    (r'^[IVX]+ квартал$', 'квартал'),          # I квартал
    (r'^(строительство|cтроительство|производство|работы|разборка|разработка)',
     'вид работ'),                             # виды строительных работ
]

# Латинские буквы, визуально совпадающие с кириллицей: встречаются внутри
# русских слов («Федеpация» с латинской p, «кваpтиp» с латинскими p).
# Без нормализации такие подписи не сопоставляются ни с регионом, ни с алиасом.
HOMOGLYPHS = str.maketrans({
    'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'K': 'К', 'M': 'М',
    'O': 'О', 'P': 'Р', 'T': 'Т', 'X': 'Х', 'a': 'а', 'c': 'с', 'e': 'е',
    'o': 'о', 'p': 'р', 'x': 'х', 'y': 'у',
})


def dehomoglyph(s):
    """Заменить латинские двойники кириллицей, если слово выглядит русским."""
    if s is None:
        return ''
    t = str(s)
    # применяем, только если в строке есть кириллица и нет длинных латинских слов
    if re.search(r'[\u0400-\u04ff]', t) and not re.search(r'[a-z]{4,}', t):
        return t.translate(HOMOGLYPHS)
    return t


def sub_dimension_of(raw):
    """Вернуть (вид подразряда, значение) либо (None, None)."""
    s = str(raw).strip()
    for pat, kind in SUB_DIM_PATTERNS:
        if re.match(pat, s, re.I):
            return kind, s
    return None, None


def parse_period(row):
    """Разобрать период по доступным полям -> (period_start, period_end)."""
    g = row.get
    # месячные
    if g('report_date'):
        s = str(g('report_date'))[:10]
        m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
        if m:
            y, mo = int(m.group(1)), int(m.group(2))
            start = date(y, mo, 1)
            end = date(y + (mo == 12), 1 if mo == 12 else mo + 1, 1)
            return start, date.fromordinal(end.toordinal() - 1), 'M'
    if g('report_year') and g('report_month'):
        y, mo = int(g('report_year')), int(g('report_month'))
        start = date(y, mo, 1)
        end = date(y + (mo == 12), 1 if mo == 12 else mo + 1, 1)
        return start, date.fromordinal(end.toordinal() - 1), 'M'
    # квартальные
    if g('year') and g('q'):
        y, q = int(g('year')), int(g('q'))
        ms = {1: (1, 3), 2: (4, 6), 3: (7, 9), 4: (10, 12)}[q]
        return date(y, ms[0], 1), date(y, ms[1], 28), 'Q'
    if g('year') and g('quarter'):
        y, q = int(g('year')), int(g('quarter'))
        ms = {1: (1, 3), 2: (4, 6), 3: (7, 9), 4: (10, 12)}[q]
        return date(y, ms[0], 1), date(y, ms[1], 28), 'Q'
    # индекс цен: 'YYYY-MM'
    if g('month') and re.match(r'^\d{4}-\d{2}', str(g('month'))):
        y, mo = int(str(g('month'))[:4]), int(str(g('month'))[5:7])
        start = date(y, mo, 1)
        end = date(y + (mo == 12), 1 if mo == 12 else mo + 1, 1)
        return start, date.fromordinal(end.toordinal() - 1), 'M'
    # годовые
    for k in ('year', 'period'):
        v = g(k)
        if v is not None and re.match(r'^\d{4}', str(v)):
            y = int(str(v)[:4])
            return date(y, 1, 1), date(y, 12, 31), 'A'
    # периоды вида '2019Q1'
    return None, None, None


def assessment_of(period_start):
    """Версия оценки: текущий год — предварительная, прошлые — окончательная."""
    if period_start and period_start.year >= CUR_YEAR:
        return 'preliminary'
    return 'final'



INSERT_SQL = """
    INSERT INTO core.observation
      (metric_id, region_id, frequency_id, period_start, period_end,
       value, assessment_type, observation_status, source_id, release_id,
       quality_flags, sub_dimension)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'{}',%s)
    ON CONFLICT (metric_id, region_id, frequency_id, period_start,
                 source_id, release_id, assessment_type, sub_dimension)
    DO NOTHING
"""


def _flush(cur, conn, batch):
    """Записать порцию строк в core.observation."""
    cur.executemany(INSERT_SQL, batch)
    conn.commit()


def main():
    dry = '--dry-run' in sys.argv
    only = None
    if '--group' in sys.argv:
        only = sys.argv[sys.argv.index('--group') + 1]

    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    # ── справочники ──
    cur.execute("SELECT region_code, region_id FROM core.region")
    region_by_code = dict(cur.fetchall())
    cur.execute("SELECT alias, region_id FROM meta.region_alias")
    alias_map = {str(a).lower().strip(): r for a, r in cur.fetchall()}
    cur.execute("SELECT name_ru, region_id FROM core.region")
    name_map = {str(n).lower().strip(): r for n, r in cur.fetchall()}
    cur.execute("SELECT metric_code, metric_id, name_ru FROM core.metric")
    metric_rows = cur.fetchall()
    metric_by_code = {c: i for c, i, _ in metric_rows}
    # ВАЖНО: ключом служит НОРМАЛИЗОВАННОЕ название — тем же norm(),
    # что применяется к значению из staging. Если хранить сырое название,
    # расхождение в сносках («1)») и пробелах теряет строки.
    metric_by_name = {}
    cur.execute("SELECT source_code, source_id FROM core.source")
    source_ids = dict(cur.fetchall())
    cur.execute("SELECT source_id, release_id FROM core.release")
    release_by_source = dict(cur.fetchall())
    cur.execute("SELECT frequency_code, frequency_id FROM core.frequency")
    freq_ids = dict(cur.fetchall())

    RU = region_by_code.get('ru')

    def norm(s):
        s = str(s or '').strip().replace('\u00a0', ' ')
        s = re.sub(r'\s+', ' ', s)
        s = re.sub(r'\d\)\s*$', '', s)
        return s.strip().lower()

    # словарь названий метрик — по нормализованному ключу
    for c, i, n in metric_rows:
        k = norm(n)
        if k and k not in metric_by_name:
            metric_by_name[k] = i
    print(f"справочники: регионов={len(region_by_code)}, алиасов={len(alias_map)}, "
          f"метрик по названию={len(metric_by_name)}")

    def resolve_region(raw):
        """-> (region_id, sub_dimension)"""
        k = norm(raw)
        rid = alias_map.get(k) or name_map.get(k)
        if rid:
            return rid, ''
        # повторная попытка после снятия гомоглифов («Федеpация» → «Федерация»)
        dh = dehomoglyph(raw)
        if dh != raw:
            k2 = norm(dh)
            rid = alias_map.get(k2) or name_map.get(k2)
            if rid:
                return rid, ''
            raw = dh
            k = k2
        kind, val = sub_dimension_of(raw)
        if kind:
            return RU, f'{kind}: {val}'
        # остальное — категории объектов (виды мощностей, типы зданий):
        # это легитимный подразрез, а не территориальная привязка
        return RU, f'категория: {str(raw)[:80]}'

    # ── группы к переносу ──
    groups = [
        dict(name='rosstat_observations', tbl='rosstat_construction__observations',
             src='rosstat', metric_col=None,
             sql="""SELECT o.indicator_id, o.region_name, o.period, o.value, o.source_file,
                           i.indicator_name
                    FROM staging.rosstat_construction__observations o
                    LEFT JOIN staging.rosstat_construction__indicators i ON i.id=o.indicator_id""",
             key=lambda r: r['indicator_name']),
        dict(name='cbr_mortgage', tbl='cbr_lending__mortgage_monthly',
             src='cbr', sql="""SELECT region_name, report_date, indicator, value, unit
                               FROM staging.cbr_lending__mortgage_monthly""",
             key=lambda r: r['indicator']),
        dict(name='cbr_escrow', tbl='cbr_lending__escrow_monthly',
             src='cbr', sql="""SELECT region_name, report_date, indicator, value, unit
                               FROM staging.cbr_lending__escrow_monthly""",
             key=lambda r: r['indicator']),
        dict(name='cbr_corp', tbl='cbr_lending__corporate_monthly',
             src='cbr', sql="""SELECT region_name, report_date, indicator, value, unit
                               FROM staging.cbr_lending__corporate_monthly""",
             key=lambda r: r['indicator']),
        dict(name='panel', tbl='regions_panel__panel',
             src='rosstat', sql="""SELECT region_name, year, value, unit,
                                          indicator_code, indicator_name
                                   FROM staging.regions_panel__panel""",
             key=lambda r: r['indicator_code']),
        dict(name='housing_input', tbl='rosstat_construction__housing_input_operational_monthly',
             src='rosstat', sql="""SELECT region_name, report_year, report_month, indicator,
                                          value, unit
                                   FROM staging.rosstat_construction__housing_input_operational_monthly""",
             key=lambda r: r['indicator']),
        dict(name='deals', tbl='rosreestr_deals__deals_by_region_quarter',
             src='rosreestr',
             sql="""SELECT region, year, quarter, n_deals, median_price_per_sqm
                    FROM staging.rosreestr_deals__deals_by_region_quarter""",
             key=lambda r: 'Количество сделок (ДКП и ДДУ), регион, квартал'),
        dict(name='ikv', tbl='rosreestr_deals__ikv_region_quarter',
             src='rosstat',
             sql="""SELECT region, year, q, value_mln FROM staging.rosreestr_deals__ikv_region_quarter""",
             key=lambda r: 'Инвестиции в основной капитал, млн руб., регион, квартал'),
        dict(name='price_idx', tbl='rosreestr_deals__domrf_price_index',
             src='domrf',
             sql="""SELECT region, month, index_value FROM staging.rosreestr_deals__domrf_price_index""",
             key=lambda r: 'Индекс цен на жильё ДОМ.РФ, регион, месяц'),
    ]

    report = {}
    for g in groups:
        if only and only != g['name']:
            continue
        print(f"\n=== {g['name']} ===", flush=True)
        # Читаем потоково: на VDS ~960 МБ памяти, загрузка таблицы целиком
        # (panel — 309 тыс. строк) убивала процесс по OOM (код 137).
        cur.execute(f"SELECT count(*) FROM ({g['sql']}) _cnt")
        total_rows = cur.fetchone()[0]
        print(f"  строк: {total_rows:,}")

        sid = source_ids.get(g['src'])
        rel_id = release_by_source.get(sid)
        if not sid or not rel_id:
            print(f"  ПРОПУСК: нет источника/релиза для {g['src']}")
            continue

        ins = skipped_no_metric = skipped_no_period = 0
        ins_committed = 0
        batch = []
        # Чтение — отдельным соединением: коммит писателя завершает
        # транзакцию и уничтожает серверный курсор (InvalidCursorName),
        # поэтому чтение и запись обязаны быть разведены.
        rconn = psycopg.connect(DSN)
        rcur = rconn.cursor(name='cur_' + g['name'])
        rcur.itersize = 20000
        rcur.execute(g['sql'])
        colnames = [d.name for d in rcur.description]
        for raw_row in rcur:
            r = dict(zip(colnames, raw_row))
            mkey = norm(g['key'](r))
            mid = metric_by_name.get(mkey) or metric_by_code.get(mkey)
            if not mid:
                skipped_no_metric += 1
                continue
            raw_region = r.get('region_name') or r.get('region')
            rid_, subdim = resolve_region(raw_region)
            ps, pe, fcode = parse_period(r)
            if not ps:
                skipped_no_period += 1
                continue
            fid = freq_ids.get(fcode) or freq_ids.get('A')
            val = r.get('value')
            if val is None:
                for k in ('n_deals', 'index_value', 'value_mln', 'value'):
                    if r.get(k) is not None:
                        val = r[k]
                        break
            batch.append((mid, rid_, fid, ps, pe, val, 'final' if ps.year < CUR_YEAR
                          else 'preliminary', 'validated', sid, rel_id, subdim))
            ins += 1
            # коммитим порциями: одна транзакция на 300 тыс. строк держит
            # блокировки и копит память на серверной стороне
            if not dry and len(batch) >= 50000:
                _flush(cur, conn, batch)
                ins_committed += len(batch)
                batch = []

        print(f"  готово к вставке: {ins:,}")
        print(f"  без метрики: {skipped_no_metric}")
        print(f"  без периода: {skipped_no_period}")

        if not dry and batch:
            _flush(cur, conn, batch)
            ins_committed += len(batch)
            batch = []
        if not dry:
            print(f"  отправлено в базу: {ins_committed:,}")
        rcur.close()
        rconn.close()

        report[g['name']] = dict(rows=total_rows, prepared=ins,
                                 no_metric=skipped_no_metric, no_period=skipped_no_period)

    print("\n=== ИТОГ ===")
    print(json.dumps(report, ensure_ascii=False, indent=1))
    cur.execute("SELECT count(*) FROM core.observation")
    print(f"\ncore.observation: {cur.fetchone()[0]:,}")
    conn.close()


if __name__ == '__main__':
    main()
