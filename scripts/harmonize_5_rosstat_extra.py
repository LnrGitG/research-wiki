#!/usr/bin/env python3
"""
Рубеж 5: остальные ряды Росстата и доп. выгрузка ЦБ.

Переносятся таблицы `staging`, не охваченные рубежами 3б и 4. Все они
однотипны: период (год / месяц / квартал / дата) + значение + измерение
(регион, показатель, продукт, рынок) + единица.

Структуры (разведка 18.09.2026):

    housing_prices_quarterly        8 815   регион, год, квартал, рынок, цена
    housing_prices_regional         2 919   регион, год, рынок, цена
    unfinished_construction_regional 6 970  регион, год, показатель, значение
    building_completions_regional   2 367   регион, год, показатель, значение
    building_materials_monthly      2 456   продукт, год, месяц, значение
    average_wage_monthly_regional  15 120   регион, год, месяц, зарплата
    gdp_vds_quarterly_okved         6 248   раздел ОКВЭД, год, квартал, ряд
    real_wage_index_annual_regional 2 415   регион, год, индекс
    cbr_api_mortgage              121 320   показатель, регион, валюта, дата

Ключ наблюдения: (метрика, регион, частота, период, источник, релиз,
версия оценки, подразрез). Подразрез собирает всё, что различает строки:
рынок, валюту, вид ряда, продукт. Перед прогоном — симуляция ключа.

Запуск:
    PGDSN="host=localhost port=5432 ..." python3 harmonize_5_rosstat_extra.py
"""
import collections
import os
import re
import sys
from datetime import date

import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from metric_codes import code_from_name, uniquify

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
TARGET = os.environ.get("TARGET_TABLE", "core.observation_v2")
CUR_YEAR = 2026

ST = "staging."

# Конфигурация: (таблица, источник, выражение периода, колонка значения,
#               колонка единицы, колонки измерения для подразреза,
#               название метрики либо выражение, тег)
GROUPS = [
    dict(tbl="rosstat_construction__housing_prices_quarterly", src="rosstat",
         period="q", val="price_per_sqm", unit="unit",
         dims=["region_name", "market"],
         name="Цена 1 кв. м жилья, квартальная", tag="stage5"),
    dict(tbl="rosstat_construction__housing_prices_regional", src="rosstat",
         period="a", val="price_per_sqm", unit="unit",
         dims=["region_name", "market"],
         name="Цена 1 кв. м жилья, годовая", tag="stage5"),
    dict(tbl="rosstat_construction__unfinished_construction_regional", src="rosstat",
         period="a", val="value", unit="unit",
         dims=["region_name", "indicator"],
         name="__indicator__", tag="stage5"),
    dict(tbl="rosstat_construction__building_completions_regional", src="rosstat",
         period="a", val="value", unit="unit",
         dims=["region_name", "indicator"],
         name="__indicator__", tag="stage5"),
    dict(tbl="rosstat_construction__building_materials_monthly", src="rosstat",
         period="m", val="value", unit="unit",
         dims=["product"],
         name="__product__", tag="stage5"),
    dict(tbl="rosstat_construction__average_wage_monthly_regional", src="rosstat",
         period="m", val="wage_rub", unit=None,
         dims=["region_name"],
         name="Среднемесячная начисленная зарплата", tag="stage5"),
    dict(tbl="rosstat_construction__gdp_vds_quarterly_okved", src="rosstat",
         period="q", val="value", unit="unit",
         dims=["section_name", "series", "okved_section"],
         name="ВДС по разделам ОКВЭД2, квартальная", tag="stage5"),
    dict(tbl="rosstat_construction__real_wage_index_annual_regional", src="rosstat",
         period="a", val="real_wage_index", unit=None,
         dims=["region_name"],
         name="Индекс реальной заработной платы", tag="stage5"),
    dict(tbl="rosstat_construction__cbr_api_mortgage", src="cbr",
         period="date", val="value", unit="unit",
         dims=["region_name", "currency", "indicator_name"],
         name="__indicator_named__", tag="stage5"),
]


def norm(s):
    return '' if s is None else re.sub(r'\s+', ' ', str(s)).strip().lower()


_USED_CODES = set()


def make_panel_code(name):
    """Код метрики из названия: транслитерация, при коллизии — суффикс."""
    base = code_from_name(name, max_len=26)
    code = uniquify(base, _USED_CODES, max_len=32)
    _USED_CODES.add(code)
    return code


def parse_period(kind, row, get):
    """-> (period_start, period_end, freq_code)"""
    if kind == 'date':
        s = str(get('date') or '')[:10]
        m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', s)
        if m:
            y, mo = int(m.group(1)), int(m.group(2))
            st = date(y, mo, 1)
            nx = date(y + (mo == 12), 1 if mo == 12 else mo + 1, 1)
            return st, date.fromordinal(nx.toordinal() - 1), 'M'
        return None, None, None
    y = get('year')
    if y is None:
        return None, None, None
    y = int(y)
    if kind == 'm':
        mo = int(get('month') or 1)
        st = date(y, mo, 1)
        nx = date(y + (mo == 12), 1 if mo == 12 else mo + 1, 1)
        return st, date.fromordinal(nx.toordinal() - 1), 'M'
    if kind == 'q':
        q = get('quarter')
        q = int(str(q).lstrip('Qq') or 1) if q is not None else 1
        ms = {1: (1, 3), 2: (4, 6), 3: (7, 9), 4: (10, 12)}.get(q, (1, 3))
        return date(y, ms[0], 1), date(y, ms[1], 28), 'Q'
    return date(y, 1, 1), date(y, 12, 31), 'A'


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    cur.execute("SELECT source_id, source_code FROM core.source")
    src_ids = {c: i for i, c in cur.fetchall()}
    cur.execute("SELECT frequency_id, frequency_code FROM core.frequency")
    freq_ids = {c: i for i, c in cur.fetchall()}
    cur.execute("SELECT unit_id, unit_code FROM core.unit")
    unit_ids = {c: i for i, c in cur.fetchall()}

    cur.execute("SELECT region_id, name_ru FROM core.region")
    reg = {norm(n): i for i, n in cur.fetchall()}
    cur.execute("SELECT alias, region_id FROM meta.region_alias")
    for a, rid in cur.fetchall():
        reg.setdefault(norm(a), rid)
    ru_id = reg.get('российская федерация')

    cur.execute("SELECT metric_id, name_ru FROM core.metric")
    by_name = {norm(nm): mid for mid, nm in cur.fetchall()}
    cur.execute("SELECT metric_code FROM core.metric")
    _USED_CODES.update(r[0] for r in cur.fetchall())

    total_ins = 0
    for g in GROUPS:
        tbl = ST + '"' + g['tbl'] + '"'
        cur.execute(f'SELECT count(*) FROM {tbl}')
        n_src = cur.fetchone()[0]
        sid = src_ids.get(g['src'])
        if not sid:
            print(f"ПРОПУСК {g['tbl']}: нет источника {g['src']}", file=sys.stderr)
            continue

        # релиз для этого источника
        cur.execute("""SELECT release_id FROM core.release
                       WHERE source_id=%s ORDER BY release_id LIMIT 1""", (sid,))
        r = cur.fetchone()
        if r:
            rel_id = r[0]
        else:
            cur.execute("""INSERT INTO core.release
                           (source_id, release_label, published_at, status, notes)
                           VALUES (%s, %s, now(), 'loaded', %s) RETURNING release_id""",
                        (sid, f'{g["src"]} ряды', 'Рубеж 5'))
            rel_id = cur.fetchone()[0]
            conn.commit()

        rconn = psycopg.connect(DSN)
        rcur = rconn.cursor(name='cur_' + g['tbl'][-20:])
        rcur.itersize = 10000
        rcur.execute(f'SELECT * FROM {tbl}')
        colnames = [d.name for d in rcur.description]

        batch = []
        ins = 0
        no_per = 0
        seq = {}
        for raw in rcur:
            row = dict(zip(colnames, raw))

            def get(k, _r=row):
                return _r.get(k)

            ps, pe, fcode = parse_period(g['period'], row, get)
            if not ps:
                no_per += 1
                continue

            # измерение -> подразрез
            parts = []
            rname = get('region_name')
            rid = reg.get(norm(rname)) if rname else None
            # Разный СОСТАВ региона сводится к одному region_id: «Архангельская
            # область» и «Архангельская область без авт. округа» — это один
            # регион-код, но разные наблюдения с разными значениями. Без
            # выноса исходного написания в подразрез строки схлопываются
            # (проверено симуляцией: 316 строк по зарплате, 2 520 по ЦБ).
            if rid and rname:
                canon = None
                cur.execute("SELECT name_ru FROM core.region WHERE region_id=%s", (rid,))
                r0 = cur.fetchone()
                canon = r0[0] if r0 else None
                if canon and norm(canon) != norm(rname):
                    parts.append(f'состав: {str(rname)[:110]}')
            for d in g['dims']:
                v = get(d)
                if d == 'region_name':
                    continue
                if v is not None and str(v).strip() not in ('', 'None'):
                    parts.append(f'{d}: {str(v)[:100]}')
            if not rid and rname:
                rid = ru_id
                parts.append(f'категория: {str(rname)[:80]}')
            rid = rid or ru_id
            u = get(g['unit']) if g['unit'] else None
            if u and str(u).strip() not in ('', 'None', 'ND'):
                parts.append(f'ед.: {str(u)[:40]}')

            # метрика
            nm_template = g['name']
            if nm_template == '__indicator__':
                nm = f"{g['tbl'].split('__')[1]}: {get('indicator')}"
            elif nm_template == '__product__':
                nm = f"Производство: {get('product')}"
            elif nm_template == '__indicator_named__':
                nm = get('indicator_name') or 'показатель ЦБ'
            else:
                nm = nm_template
            k = norm(nm)
            mid = by_name.get(k)
            if not mid:
                # Код строим из названия через транслитерацию (как в рубеже 2).
                # Простое вырезание не-ASCII давало пустые коды вида 's5_' или
                # 's5_1' — кириллица в названиях вырезалась целиком.
                code = make_panel_code(str(nm))
                cur.execute("""INSERT INTO core.metric
                    (metric_code, name_ru, unit_id, frequency_id, metric_type, status, tags)
                    VALUES (%s, %s, %s, %s, 'primary', 'active', %s)
                    ON CONFLICT (metric_code) DO UPDATE SET name_ru=EXCLUDED.name_ru
                    RETURNING metric_id""",
                    (code, str(nm)[:200], unit_ids.get('count'),
                     freq_ids.get(fcode), ['stage5']))
                mid = cur.fetchone()[0]
                by_name[k] = mid
                conn.commit()

            # Защита от схлопывания: порядковый номер строки внутри таблицы.
            # Различить их штатными полями нельзя (значения совпадают), а
            # потеря реальна — проверено симуляцией ключа до прогона.
            seq[(g['tbl'],)] = seq.get((g['tbl'],), 0) + 1
            parts.append(f'строка {seq[(g["tbl"],)]}')
            subdim_final = ' | '.join(parts)

            val = get(g['val'])
            fid = freq_ids.get(fcode) or freq_ids.get('A')
            atype = 'final' if ps.year < CUR_YEAR else 'preliminary'
            batch.append((mid, rid, fid, ps, pe, val, atype, 'validated',
                          sid, rel_id, subdim_final))
            ins += 1
            if len(batch) >= 50000:
                cur.executemany("""INSERT INTO core.observation_v2
                    (metric_id, region_id, frequency_id, period_start, period_end,
                     value, assessment_type, observation_status, source_id,
                     release_id, sub_dimension)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (metric_id, region_id, frequency_id, period_start,
                                 source_id, release_id, assessment_type, sub_dimension)
                    DO NOTHING""", batch)
                conn.commit()
                batch = []
        if batch:
            cur.executemany("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end,
                 value, assessment_type, observation_status, source_id,
                 release_id, sub_dimension)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (metric_id, region_id, frequency_id, period_start,
                             source_id, release_id, assessment_type, sub_dimension)
                DO NOTHING""", batch)
            conn.commit()
        rcur.close()
        rconn.close()
        total_ins += ins
        print(f"  {g['tbl'][-38:]:40} строк={n_src:>8,} подготовлено={ins:>8,} "
              f"без периода={no_per}", flush=True)

    print(f"\nвсего подготовлено: {total_ins:,}")
    cur.execute(f"SELECT count(*) FROM {TARGET}")
    print(f"{TARGET}: {cur.fetchone()[0]:,}")
    cur.execute("SELECT count(*) FROM core.metric")
    print(f"метрик: {cur.fetchone()[0]:,}")
    conn.close()


if __name__ == "__main__":
    main()
