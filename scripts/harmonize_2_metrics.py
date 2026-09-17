#!/usr/bin/env python3
"""
Гармонизация: рубеж 2 — метрики (core.metric).

Собирает показатели из всех таблиц staging, генерирует устойчивые коды
(готовый код источника, если есть; иначе первые буквы названия) и
записывает в core.metric.

Идемпотентно: повторный запуск обновляет записи по metric_code.

Запуск:  python3 harmonize_2_metrics.py [--dry-run]
"""
import os, sys, re, json
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
import psycopg
from metric_codes import make_code, uniquify
from unit_parser import unit_from_text, resolve_unit

DSN = os.environ.get("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")

# ── единица (сырой текст) → код справочника core.unit ───────────────
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
    'тыс. ед': 'ths_units', 'чел.': 'persons', 'тыс. чел.': 'ths_persons',
}

# ── частота по умолчанию для группы ────────────────────────────────
GROUP_FREQ = {
    'rosstat_observations': 'A',
    'domrf_stock': 'M', 'domrf_flow': 'M', 'domrf_ddu': 'M',
    'domrf_sales_meters': 'M', 'domrf_sales_pct': 'M',
    'domrf_permits_stock': 'M', 'domrf_permits_flow': 'M',
    'domrf_readiness': 'M', 'domrf_sales': 'M', 'domrf_mortgage': 'M',
    'domrf_summary': 'A',
    'cbr_mortgage': 'M', 'cbr_escrow': 'M', 'cbr_corporate': 'M',
    'rosstat_panel': 'A',
    'dev_ifrs': 'Q',
    'rosstat_housing_input': 'M',
    'rosstat_prices_regional': 'A',
    'rosstat_deals': 'Q',
    'rosstat_ikv': 'Q',
    'domrf_price_index': 'M',
}

# ── источник по группе ──────────────────────────────────────────────
GROUP_SOURCE = {
    'rosstat_observations': 'rosstat', 'rosstat_panel': 'rosstat',
    'rosstat_housing_input': 'rosstat', 'rosstat_prices_regional': 'rosstat',
    'rosstat_deals': 'rosreestr', 'rosstat_ikv': 'rosstat',
    'cbr_mortgage': 'cbr', 'cbr_escrow': 'cbr', 'cbr_corporate': 'cbr',
    'dev_ifrs': 'smartlab',
    'domrf_price_index': 'domrf',
}
for k in list(GROUP_FREQ):
    if k.startswith('domrf'):
        GROUP_SOURCE.setdefault(k, 'domrf')


def ru_unit_to_code(u, *extra_texts):
    """Определить код единицы: сначала точное совпадение, затем разбор текста."""
    if u:
        exact = UNIT_MAP.get(str(u).strip().lower())
        if exact:
            return exact
    return resolve_unit(extra_texts[0] if extra_texts else None, u, *extra_texts)


def collect(cur):
    """Собрать показатели из staging: [(group, name, unit, given_code, src_hint)]."""
    out = []

    # 1. observations + справочник indicators
    cur.execute("""SELECT id, indicator_name, unit, category
                   FROM staging.rosstat_construction__indicators ORDER BY id""")
    ind_meta = {r[0]: (r[1], r[2], r[3]) for r in cur.fetchall()}
    # ВАЖНО: в этом справочнике поле unit часто содержит не единицу,
    # а скобочную пометку или продолжение названия (артефакт парсинга) —
    # поэтому единицу ищем и в тексте названия через unit_parser.
    cur.execute("""SELECT DISTINCT indicator_id FROM staging.rosstat_construction__observations
                   WHERE indicator_id IS NOT NULL ORDER BY 1""")
    for (iid,) in cur.fetchall():
        name, unit, cat = ind_meta.get(iid, (None, None, None))
        nm = (name or '').strip()
        # где название — число, берём текст из unit (сдвиг колонок при парсинге)
        if not nm or nm.isdigit():
            nm = (unit or '').strip() or f'показатель {iid}'
            unit = ''
        out.append(('rosstat_observations', nm, unit, None))

    # 2. domrf — по (data_type, indicator_code, indicator_name)
    cur.execute("""SELECT DISTINCT data_type, indicator_name, indicator_code, unit
                   FROM staging.rosstat_construction__domrf_indicators
                   WHERE indicator_name IS NOT NULL ORDER BY 1, 3""")
    for dt, nm, code, unit in cur.fetchall():
        out.append(('domrf_' + str(dt), nm, unit, code))

    # 3. ЦБ — из cbr_lending (он полнее по числу строк)
    for tbl, pref in (('mortgage_monthly', 'cbr_mortgage'),
                      ('escrow_monthly', 'cbr_escrow'),
                      ('corporate_monthly', 'cbr_corporate')):
        cur.execute(f"""SELECT DISTINCT indicator, unit
                        FROM staging.cbr_lending__{tbl}
                        WHERE indicator IS NOT NULL ORDER BY 1""")
        for nm, unit in cur.fetchall():
            out.append((pref, nm, unit, None))

    # 4. panel — коды уже есть
    cur.execute("""SELECT DISTINCT indicator_name, indicator_code, unit
                   FROM staging.regions_panel__panel
                   WHERE indicator_name IS NOT NULL ORDER BY 2""")
    for nm, code, unit in cur.fetchall():
        out.append(('rosstat_panel', nm, unit, code))

    # 5. dev_ifrs
    cur.execute("SELECT DISTINCT metric FROM staging.developers_ifrs__dev_ifrs "
                "WHERE metric IS NOT NULL ORDER BY 1")
    for (nm,) in cur.fetchall():
        out.append(('dev_ifrs', nm, None, None))

    # 6. ввод жилья (оперативно)
    cur.execute("""SELECT DISTINCT indicator, unit
                   FROM staging.rosstat_construction__housing_input_operational_monthly
                   WHERE indicator IS NOT NULL ORDER BY 1""")
    for nm, unit in cur.fetchall():
        out.append(('rosstat_housing_input', nm, unit, None))

    # 7. цены по регионам
    cur.execute("""SELECT DISTINCT 'Цена '||market||' рынка жилья, '||unit
                   FROM staging.rosstat_construction__housing_prices_regional
                   WHERE market IS NOT NULL""")
    for (nm,) in cur.fetchall():
        out.append(('rosstat_prices_regional', nm, None, None))

    # 8. Росреестр — сделки и аренда
    for col, nm in (('n_deals', 'Количество сделок (ДКП и ДДУ), регион, квартал'),
                    ('median_price_per_sqm', 'Медианная цена сделки за м²'),
                    ('n_dkp', 'Количество сделок по ДКП')):
        out.append(('rosstat_deals', nm, None, None))

    # 9. ИКВ по регионам
    out.append(('rosstat_ikv', 'Инвестиции в основной капитал, млн руб., регион, квартал', None, None))

    # 10. индекс цен ДОМ.РФ
    out.append(('domrf_price_index', 'Индекс цен на жильё ДОМ.РФ, регион, месяц', None, None))

    return out


def main():
    dry = '--dry-run' in sys.argv
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    print("Сбор показателей из staging…", flush=True)
    items = collect(cur)
    print(f"  собрано: {len(items)}")

    # единицы и частоты → id
    cur.execute("SELECT unit_code, unit_id FROM core.unit")
    units = dict(cur.fetchall())
    cur.execute("SELECT frequency_code, frequency_id FROM core.frequency")
    freqs = dict(cur.fetchall())

    # генерация кодов
    used = set()
    planned = []
    for grp, name, unit, given in items:
        code = uniquify(make_code(name, given), used)
        ucode = ru_unit_to_code(unit, name) or 'unknown'
        fcode = GROUP_FREQ.get(grp, 'A')
        planned.append({
            'group': grp, 'name': name.strip()[:300], 'code': code,
            'unit_code': ucode, 'freq_code': fcode,
            'unit_id': units.get(ucode), 'freq_id': freqs.get(fcode),
            'source': GROUP_SOURCE.get(grp, 'rosstat'),
        })

    print(f"  кодов: {len(planned)}, коллизий: {sum(1 for p in planned if '_' in p['code'][-3:])}")
    print(f"  без unit_id: {sum(1 for p in planned if not p['unit_id'])}")
    print(f"  без freq_id: {sum(1 for p in planned if not p['freq_id'])}")

    by_src = Counter(p['source'] for p in planned)
    print(f"  по источникам: {dict(by_src)}")

    if dry:
        print("\n--- СУХОЙ ПРОГОН, образцы ---")
        for p in planned[:12]:
            print(f"  {p['code']:16} {p['source']:10} {p['unit_code']:12} {p['name'][:50]}")
        json.dump(planned, open('/tmp/metrics_planned_final.json','w'), ensure_ascii=False, indent=1)
        print("\nплан сохранён: /tmp/metrics_planned_final.json")
        conn.close()
        return

    # запись
    print("\nЗапись в core.metric…", flush=True)
    n_ins = n_upd = 0
    for p in planned:
        if not p['unit_id'] or not p['freq_id']:
            continue
        cur.execute("""
            INSERT INTO core.metric (metric_code, name_ru, unit_id, frequency_id,
                                     metric_type, is_derived, status, tags)
            VALUES (%s, %s, %s, %s, 'primary', false, 'active', %s)
            ON CONFLICT (metric_code) DO UPDATE SET
                name_ru = EXCLUDED.name_ru, unit_id = EXCLUDED.unit_id,
                frequency_id = EXCLUDED.frequency_id
            RETURNING (xmax = 0) AS inserted
        """, (p['code'], p['name'], p['unit_id'], p['freq_id'], [p['group']]))
        row = cur.fetchone()
        if row and row[0]:
            n_ins += 1
        else:
            n_upd += 1
    conn.commit()
    print(f"  вставлено: {n_ins}, обновлено: {n_upd}")

    cur.execute("SELECT count(*) FROM core.metric")
    print(f"\n  core.metric: {cur.fetchone()[0]}")
    cur.execute("""SELECT m.metric_code, m.name_ru, s.source_code, u.unit_code
                   FROM core.metric m
                   LEFT JOIN core.unit u ON u.unit_id=m.unit_id
                   LEFT JOIN core.source s ON s.source_code = ANY(
                       ARRAY(SELECT jsonb_array_elements_text(to_jsonb(m.tags))))
                   LIMIT 0""")
    cur.execute("""SELECT metric_code, name_ru FROM core.metric ORDER BY metric_id LIMIT 8""")
    print("\nпервые записи:")
    for c, n in cur.fetchall():
        print(f"  {c:16} {n[:62]}")
    conn.close()


if __name__ == '__main__':
    main()
