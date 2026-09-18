#!/usr/bin/env python3
"""
Рубеж 6: остаток staging → core.observation_v2 (42 таблицы, 49 729 строк).

Все таблицы однотипны: период + значение + измерение. Особенности:

- `snapshot` у ФНС (profitorg, 1-НОМ, НДФЛ) — это ДАТА съёма, и она НЕ всегда
  квартальная: кроме 01/04/07/10 встречаются 20200407, 20201123, 20210829,
  20221230. Период = (год, квартал из месяца), а полная дата уходит в
  подразрез как «снапшот: YYYYMMDD», иначе строки схлопываются.
- `quarter` у ДАС Росстата — формат 'Q1'..'Q4', не число.
- У региональных таблиц Росреестра есть `region_code` — выносим в подразрез,
  он надёжнее названия.
- Колонка `source` внутри staging = первичная публикация → в release_id.
- Порядковый номер строки дописывается ТОЛЬКО строкам с реально
  повторяющимся ключом (механизм рубежа 5).

Запуск:  python3 harmonize_6_rosstat_extra.py           # прогон
         SIMULATE=1 python3 harmonize_6_rosstat_extra.py # только симуляция
"""
import collections
import os
import re
import sys

import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from metric_codes import code_from_name, uniquify

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
TARGET = "core.observation_v2"
CUR_YEAR = 2026
ST = "staging."
TAG = "stage6"
SIMULATE = os.environ.get("SIMULATE") == "1"

# (таблица, источник, разбор периода, колонка региона, измерение-код,
#  колонки-разрезы, [(шаблон названия, колонка значения)])
GROUPS = [
 ("rosreestr_deals__fns_profitorg_key_quarterly", "fns", "snap", "region", None,
  ["field"], [("__field__", "value")]),
 ("rosreestr_deals__rosstat_ind_prod_regions", "rosstat", "ym", "region", None,
  [], [("Индекс промышленного производства, % к соответствующему месяцу", "yoy_pct")]),
 ("rosreestr_deals__domrf_price_index", "domrf", "ym", "region", None,
  [], [("Индекс цен на жильё ДОМ.РФ", "index_value"),
       ("Индекс цен на жильё ДОМ.РФ, % к предыдущему месяцу", "mom_pct"),
       ("Число сделок, ДОМ.РФ", "n_deals")]),
 ("rosreestr_deals__rosstat_buildings_yearbook", "rosstat", "a", "region", None,
  ["metric"], [("__metric__", "value")]),
 ("rosreestr_deals__housing_backlog_ratio_annual", "rosstat", "a", "region", None,
  [], [("Отношение запаса строящегося жилья к вводу, %", "value")]),
 ("rosreestr_deals__housing_input_annual", "rosstat", "a", "region", None,
  [], [("Ввод жилья, тыс. м² (годовой ряд)", "value")]),
 ("rosreestr_deals__fns_annual_regional", "fns", "a", "region", None,
  ["form", "metric"], [("__metric__", "value")]),
 ("rosstat_construction__das_construction_sentiment_quarterly", "rosstat", "yq", None, None,
  ["indicator", "subtype"], [("__indicator__", "value")]),
 ("rosreestr_deals__deals_by_region_quarter", "rosreestr", "yq", "region", "region_code",
  [], [("Количество сделок (ДКП и ДДУ), регион, квартал", "n_deals"),
       ("Количество сделок ДКП, регион, квартал", "n_dkp"),
       ("Медианная цена сделки за м², регион, квартал", "median_price_per_sqm"),
       ("Медианная цена ДКП за м², регион, квартал", "median_dkp_per_sqm"),
       ("Медианная цена ДДУ за м², регион, квартал", "median_ddu_per_sqm")]),
 ("rosreestr_deals__rents_by_region_quarter", "rosreestr", "yq", "region", "region_code",
  [], [("Количество договоров аренды, регион, квартал", "n_rents"),
       ("Медианная ставка аренды за м², регион, квартал", "median_rate_per_sqm"),
       ("Медианная площадь арендуемого жилья, регион, квартал", "median_area")]),
 ("rosstat_construction__construction_machinery", "rosstat", "a", "region_name", None,
  ["machine_type"], [("Парк строительной техники, единиц", "count_total"),
                     ("Доля техники с истёкшим сроком службы, %", "pct_expired_service"),
                     ("Доля техники зарубежного производства, %", "pct_foreign_made")]),
 ("rosreestr_deals__gdp_use_quarterly", "rosstat", "pq", None, None,
  ["series"], [("__series__", "value")]),
 ("rosreestr_deals__gdp_use_ifo_quarterly", "rosstat", "pq", None, None,
  ["series"], [("__series__ (ИФО)", "ifo")]),
 ("developers_ifrs__dev_ifrs", "smartlab", "a_str", None, None,
  ["company", "ticker", "freq", "metric"], [("МСФО девелоперов: __metric__", "value")]),
 ("rosreestr_deals__fns_1nom_okved_f_quarterly", "fns", "snapdate", "region", None,
  ["metric"], [("__metric__", "value")]),
 ("rosreestr_deals__rosstat_ind_prod_saar", "rosstat", "ym", None, None,
  ["section"], [("Промпроизводство, % к предыдущему месяцу (факт)", "mom_fact"),
                ("Промпроизводство, % к предыдущему месяцу (SAAR)", "mom_saar"),
                ("Промпроизводство, % к базовому периоду (факт)", "base_fact"),
                ("Промпроизводство, % к базовому периоду (SAAR)", "base_saar")]),
 ("rosstat_construction__construction_employment", "rosstat", "a", "region_name", None,
  [], [("Численность занятых в строительстве, тыс. чел.", "employment_thousands"),
       ("Доля занятых в строительстве, %", "share_of_total_pct")]),
 ("rosreestr_deals__fns_ndfl_regional", "fns", "snapdate", "region", None,
  ["field"], [("__field__", "value")]),
 ("rosreestr_deals__rosstat_buildings_annual", "rosstat", "a", None, None,
  ["label"], [("__label__", "value")]),
 ("rosreestr_deals__rosstat_nonres_buildings", "rosstat", "a", None, None,
  ["breakout"], [("Ввод нежилых зданий, тыс. шт.", "count_thousands"),
                 ("Ввод нежилых зданий, млн м²", "area_mln_m2")]),
 ("rosstat_construction__materials_production_rf", "rosstat", "a", None, None,
  ["product_name"], [("Производство (РФ): __product_name__", "value")]),
 ("rosstat_construction__materials_import", "rosstat", "a", None, None,
  ["product_name"], [("Импорт стройматериалов: __product_name__", "value")]),
 ("rosstat_construction__materials_capacity_utilization", "rosstat", "a", None, None,
  ["product_name"], [("Загрузка мощностей: __product_name__", "utilization_pct")]),
 ("rosstat_construction__machinery_production", "rosstat", "a", None, None,
  ["product_name"], [("Производство техники: __product_name__", "value")]),
 ("rosstat_construction__machinery_import", "rosstat", "a", None, None,
  ["product_name"], [("Импорт техники: __product_name__", "value")]),
 ("rosstat_construction__materials_production_fd", "rosstat", "a", None, None,
  ["federal_district", "product_name"], [("Производство по округам: __product_name__", "value")]),
 ("rosreestr_deals__fns_rf_annual", "fns", "a", None, None,
  ["form", "metric"], [("__metric__ (РФ)", "rf_value_bln_rub")]),
 ("rosstat_construction__construction_volume_monthly_rf", "rosstat", "y_m", None, None,
  ["period_label"], [("Объём работ «Строительство», млрд руб.", "value_bln_rub"),
                     ("Объём работ «Строительство», % к соотв. периоду", "yoy_pct"),
                     ("Объём работ «Строительство», % к пред. периоду", "mom_pct")]),
 ("rosstat_construction__construction_contracts_monthly_rf", "rosstat", "y_m", None, None,
  [], [("Заключено договоров строительного подряда, млрд руб.", "contracts_bln_rub"),
       ("Обеспеченность договорами подряда, месяцев", "backlog_months")]),
 ("rosreestr_deals__deals_rf_quarterly", "rosreestr", "yq", None, None,
  [], [("Количество сделок (ДКП и ДДУ), РФ, квартал", "n"),
       ("Количество сделок ДКП, РФ, квартал", "ndkp")]),
 ("rosreestr_deals__rents_rf_quarterly", "rosreestr", "yq", None, None,
  [], [("Количество договоров аренды, РФ, квартал", "n")]),
 ("rosstat_construction__prom_products_monthly", "rosstat", "y_m", None, None,
  ["product"], [("Промпродукция, месяц: __product__", "value_month"),
                ("Промпродукция, пред. месяц: __product__", "value_prev_month"),
                ("Промпродукция, накопленным итогом: __product__", "value_ytd")]),
 ("rosstat_construction__building_materials_indices_monthly", "rosstat", "y_m", None, None,
  ["product"], [("Стройматериалы, % к соотв. периоду: __product__", "yoy_pct"),
                ("Стройматериалы, % к пред. месяцу: __product__", "mom_pct")]),
 ("rosstat_construction__buildings_completed_by_type", "rosstat", "yperiod", None, None,
  ["building_type"], [("Введено зданий, единиц (__building_type__)", "buildings_count"),
                      ("Введено зданий, тыс. м² (__building_type__)", "total_area_ksq_m")]),
 ("rosstat_construction__investment_fixed_capital_quarterly", "rosstat", "yq_rf", "region_name", None,
  [], [("Инвестиции в основной капитал, млрд руб. (оперативные)", "value_bln_rub"),
       ("Инвестиции в основной капитал, % к соотв. периоду (оперативные)", "yoy_pct")]),
 ("rosreestr_deals__rosstat_buildings_vvod", "rosstat", "ym", None, None,
  ["category"], [("Ввод зданий, единиц (__category__)", "buildings_count"),
                 ("Ввод зданий, тыс. м² (__category__)", "total_area_ths_m2")]),
 ("rosreestr_deals__rosstat_production_capacity_vvod", "rosstat", "ym", None, None,
  ["section", "unit"], [("Ввод мощностей: __section__", "total"),
                        ("Ввод мощностей, новое строительство: __section__", "new_construction"),
                        ("Ввод мощностей, реконструкция: __section__", "reconstruction")]),
 ("rosreestr_deals__ikv_region_quarter", "rosstat", "yq", "region", None,
  [], [("Инвестиции в основной капитал, млн руб., регион, квартал (росстат-источник)", "value_mln")]),
 ("rosreestr_deals__ikv_region_quarter_pct", "rosstat", "y_q_only", "region", None,
  [], [("Инвестиции в основной капитал, % к соотв. периоду, регион", "pct")]),
 ("rosstat_construction__das_construction_sentiment_quarterly", "rosstat", "yq", None, None,
  ["indicator"], [("ДАННЫЕ ПРОПУСТИТЬ", "value")]),
]


def norm(s):
    return '' if s is None else re.sub(r'\s+', ' ', str(s)).strip().lower()


def parse_period(kind, row):
    """Возвращает (год, месяц) либо None. Квартал кодируем месяцем 1/4/7/10."""
    g = row.get
    y = g('year') or g('report_year')
    if kind == 'a':
        return (int(y), 0) if y else None
    if kind == 'a_str':
        per = str(g('period') or '')
        mq = re.match(r'^(\d{4})Q(\d)', per)
        if mq:
            return (int(mq.group(1)), {1: 1, 2: 4, 3: 7, 4: 10}[int(mq.group(2))])
        m = re.match(r'^(\d{4})', per)
        return (int(m.group(1)), 0) if m else None
    if kind == 'yq':
        q = g('quarter') if g('quarter') is not None else g('q')
        if q is None:
            return None
        m = re.match(r'^Q(\d)', str(q))
        qi = int(m.group(1)) if m else (int(q) if str(q).isdigit() else None)
        if qi is None or not y:
            return None
        return (int(y), {1: 1, 2: 4, 3: 7, 4: 10}[qi])
    if kind == 'y_q_only':
        q = g('q')
        return (int(y), {1: 1, 2: 4, 3: 7, 4: 10}[int(q)]) if y and q else None
    if kind == 'yq_rf':
        q = g('quarter')
        return (int(y), {1: 1, 2: 4, 3: 7, 4: 10}[int(q)]) if y and q else None
    if kind == 'y_m':
        m = g('month') or g('report_month')
        return (int(y), int(m)) if y and m else None
    if kind == 'ym':
        m = re.match(r'^(\d{4})-(\d{2})', str(g('month') or g('period') or ''))
        return (int(m.group(1)), int(m.group(2))) if m else None
    if kind == 'pq':
        m = re.match(r'^(\d{4})-Q(\d)', str(g('period') or ''))
        return (int(m.group(1)), {1: 1, 2: 4, 3: 7, 4: 10}[int(m.group(2))]) if m else None
    if kind in ('snap', 'snapdate'):
        s = str(g('snapshot') or g('snapshot_date') or '')
        m = re.match(r'^(\d{4})(\d{2})(\d{2})?', s)
        if not m:
            return None
        mm = int(m.group(2))
        qm = {1: 1, 2: 1, 3: 1, 4: 4, 5: 4, 6: 4, 7: 7, 8: 7, 9: 7, 10: 10, 11: 10, 12: 10}.get(mm, 0)
        return (int(m.group(1)), qm)
    if kind == 'yperiod':
        y2 = g('report_year')
        return (int(y2), 0) if y2 else None
    return None


def period_start(kind, row, ps):
    """Дата начала периода."""
    y, m = ps
    if m == 0:
        return "%04d-01-01" % y
    return "%04d-%02d-01" % (y, m)


def period_end(kind, ps):
    y, m = ps
    if m == 0:
        return "%04d-12-31" % y
    if m in (1, 4, 7, 10):
        return "%04d-%02d-30" % (y, m + 2)
    return "%04d-%02d-%02d" % (y, m, 28)


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    cur.execute("SELECT source_code, source_id FROM core.source")
    src_ids = dict(cur.fetchall())
    cur.execute("SELECT frequency_code, frequency_id FROM core.frequency")
    freq_ids = dict(cur.fetchall())
    cur.execute("SELECT unit_code, unit_id FROM core.unit")
    unit_ids = dict(cur.fetchall())
    cur.execute("SELECT region_id, name_ru FROM core.region")
    reg, canon = {}, {}
    for ri, n in cur.fetchall():
        reg[norm(n)] = ri
        canon[ri] = n
    cur.execute("SELECT alias, region_id FROM meta.region_alias")
    for a, ri in cur.fetchall():
        reg.setdefault(norm(a), ri)
    RU = reg.get('российская федерация')
    cur.execute("SELECT metric_id, name_ru FROM core.metric")
    by_name = {norm(nm): mid for mid, nm in cur.fetchall()}
    cur.execute("SELECT metric_code FROM core.metric")
    used = {r[0] for r in cur.fetchall()}

    def ensure_release(sid, label):
        cur.execute("""SELECT release_id FROM core.release
                       WHERE source_id=%s AND release_label=%s""", (sid, label))
        r = cur.fetchone()
        if r:
            return r[0]
        cur.execute("""INSERT INTO core.release
            (source_id, release_label, published_at, status, notes)
            VALUES (%s, %s, now(), 'loaded', %s) RETURNING release_id""",
            (sid, str(label)[:200], 'Рубеж 6: первичный источник'))
        rid = cur.fetchone()[0]
        conn.commit()
        return rid

    # идемпотентность
    if not SIMULATE:
        cur.execute("""SELECT count(*) FROM core.observation_v2 o
                       WHERE EXISTS (SELECT 1 FROM core.metric m
                         WHERE m.metric_id=o.metric_id AND m.tags @> ARRAY[%s])""", (TAG,))
        n = cur.fetchone()[0]
        if n:
            print("удаляю прошлый прогон рубежа 6: %s" % format(n, ','), flush=True)
            cur.execute("""DELETE FROM core.observation_v2 o
                           WHERE EXISTS (SELECT 1 FROM core.metric m
                             WHERE m.metric_id=o.metric_id AND m.tags @> ARRAY[%s])""", (TAG,))
            conn.commit()

    total = 0
    print("%-50s %8s %8s %6s" % ("таблица", "строк", "готово", "потеря"))
    print("-" * 76)
    for tbl, src, per, regcol, codecol, dims, metrics in GROUPS:
        if metrics and metrics[0][0] == "ДАННЫЕ ПРОПУСТИТЬ":
            continue
        sid = src_ids.get(src)
        if not sid:
            print("ПРОПУСК %s: нет источника %s" % (tbl, src))
            continue
        cur.execute('SELECT * FROM staging."%s"' % tbl)
        cols = [d.name for d in cur.description]
        rows = cur.fetchall()
        cnt = collections.Counter()
        prepared = []
        for raw in rows:
            row = dict(zip(cols, raw))
            ps = parse_period(per, row)
            if ps is None:
                continue
            parts = []
            rid = None
            if regcol:
                rn = row.get(regcol)
                rid = reg.get(norm(rn)) if rn else None
                if rid and rn and canon.get(rid) and norm(canon[rid]) != norm(rn):
                    # БЕЗ обрезки: поле входит в ключ наблюдения, а названия
                    # различаются и после 100-го символа. Обрезка дала бы
                    # тихую потерю (та же ошибка, что в рубеже 3б на 2 970 строк).
                    parts.append('состав: %s' % str(rn))
                if not rid and rn:
                    parts.append('категория: %s' % str(rn))
            rid = rid or RU
            if codecol and row.get(codecol) is not None:
                parts.append('%s: %s' % (codecol, row[codecol]))
            for d in dims:
                v = row.get(d)
                if v is not None and str(v).strip() not in ('', 'None'):
                    # без обрезки — поле входит в ключ
                    parts.append('%s: %s' % (d, str(v)))
            if per in ('snap', 'snapdate'):
                s = str(row.get('snapshot') or row.get('snapshot_date') or '')
                if len(s) >= 8:
                    parts.append('снапшот: %s' % s[:8])
            u = row.get('unit')
            if u and str(u).strip() not in ('', 'None', 'ND'):
                parts.append('ед.: %s' % str(u)[:40])
            rel = str(row.get('source') or '').strip()
            sub = ' | '.join(parts)
            for tmpl, vcol in metrics:
                if vcol not in row or row[vcol] is None:
                    continue
                nm = tmpl
                for d in (dims + ['indicator', 'metric', 'series', 'label', 'field',
                                  'product', 'category', 'building_type', 'section',
                                  'product_name', 'breakout', 'machine_type', 'subtype',
                                  'federal_district', 'period_label', 'company', 'form', 'ticker']):
                    nm = nm.replace('__%s__' % d, str(row.get(d)))
                cnt[(norm(nm), rid, rel, ps, sub)] += 1
                prepared.append((nm, rid, rel, ps, sub, row[vcol]))

        loss = sum(v - 1 for v in cnt.values() if v > 1)
        if SIMULATE:
            print("%-50s %8s %8s %6d%s" % (tbl.split('__')[-1][:50], format(len(rows), ','),
                                           format(len(prepared), ','), loss,
                                           '' if loss == 0 else '  <-- РАЗОБРАТЬ'))
            total += loss
            continue

        # запись
        cur.execute("DROP TABLE IF EXISTS tmp_h6")
        cur.execute("""CREATE TEMP TABLE tmp_h6 (
            metric_id int, region_id int, frequency_id int,
            period_start date, period_end date, value numeric,
            assessment_type text, observation_status text,
            source_id int, release_id int, sub_dimension text, rn bigint)""")
        rel_cache, batch, rn, ins = {}, [], 0, 0
        freq = freq_ids.get('Q') or freq_ids.get('A')
        for nm, rid, rel, ps, sub, val in prepared:
            k = norm(nm)
            mid = by_name.get(k)
            if not mid:
                code = uniquify(code_from_name(str(nm)), used)
                cur.execute("""INSERT INTO core.metric
                    (metric_code, name_ru, unit_id, frequency_id, metric_type, status, tags)
                    VALUES (%s, %s, %s, %s, 'primary', 'active', %s)
                    ON CONFLICT (metric_code) DO UPDATE SET name_ru=EXCLUDED.name_ru
                    RETURNING metric_id""",
                    (code, str(nm)[:200], unit_ids.get('unknown'), freq, [TAG]))
                mid = cur.fetchone()[0]
                by_name[k] = mid
                conn.commit()
            if rel not in rel_cache:
                rel_cache[rel] = ensure_release(sid, rel) if rel else \
                    ensure_release(sid, '%s ряды' % src)
            rn += 1
            batch.append((mid, rid, freq, period_start(per, None, ps), period_end(per, ps),
                          val, 'final' if ps[0] < CUR_YEAR else 'preliminary', 'validated',
                          sid, rel_cache[rel], sub, rn))
            ins += 1
            if len(batch) >= 20000:
                cur.executemany("""INSERT INTO tmp_h6 VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", batch)
                conn.commit()
                batch = []
        if batch:
            cur.executemany("""INSERT INTO tmp_h6 VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", batch)
            conn.commit()
        cur.execute("""INSERT INTO core.observation_v2
            (metric_id, region_id, frequency_id, period_start, period_end, value,
             assessment_type, observation_status, source_id, release_id, sub_dimension)
            SELECT metric_id, region_id, frequency_id, period_start, period_end, value,
                   assessment_type, observation_status, source_id, release_id,
                   CASE WHEN c = 1 THEN sub_dimension
                        ELSE coalesce(sub_dimension || ' | ', '') || 'строка ' || ord END
            FROM (SELECT t.*,
                     count(*) OVER (PARTITION BY metric_id, region_id, frequency_id,
                         period_start, source_id, release_id, assessment_type, sub_dimension) AS c,
                     row_number() OVER (PARTITION BY metric_id, region_id, frequency_id,
                         period_start, source_id, release_id, assessment_type, sub_dimension
                         ORDER BY rn) AS ord
                  FROM tmp_h6 t) z
            ON CONFLICT (metric_id, region_id, frequency_id, period_start, source_id,
                         release_id, assessment_type, sub_dimension) DO NOTHING""")
        conn.commit()
        cur.execute("SELECT count(*) FROM tmp_h6")
        wrote = cur.fetchone()[0]
        cur.execute("DROP TABLE tmp_h6")
        conn.commit()
        total += ins
        print("%-50s %8s %8s %6d" % (tbl.split('__')[-1][:50], format(len(rows), ','),
                                     format(wrote, ','), loss), flush=True)

    print("-" * 76)
    if SIMULATE:
        print("СИМУЛЯЦИЯ: суммарная потеря %d" % total)
    else:
        print("подготовлено: %s" % format(total, ','))
        cur.execute("SELECT count(*) FROM core.observation_v2")
        print("core.observation_v2: %s" % format(cur.fetchone()[0], ','))
    conn.close()


if __name__ == "__main__":
    main()
