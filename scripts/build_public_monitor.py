#!/usr/bin/env python3
"""Публичная витрина жилищного рынка: снапшот из PostgreSQL в JSON для GitHub Pages.

Витрина статическая: браузер читает docs/public-monitor.json и рисует графики
на клиенте, никакого доступа к базе у публичного контура нет.

Запуск:  python3 scripts/build_public_monitor.py            # собрать JSON
         python3 scripts/build_public_monitor.py --check    # только проверить

Источник — derived.v_bi_observation (схема data + catalog + derived).
Агрегаты по РФ: если в базе есть строка уровня country — берётся она,
иначе медиана (для индексов и ставок) или сумма (для объёмов) по субъектам.
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as d  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "public-monitor.json")

# code, заголовок, единица, способ агрегата по РФ, частота, примечание
METRICS = [
    ("orvdssmpg", "Объём работ «Строительство», % г/г", "%", "median", "M",
     "ИФО по ВЭД «Строительство» к соответствующему месяцу; медиана по субъектам устойчива к выбросам."),
    ("orvdsningmr", "Объём работ «Строительство», накопит.", "млн руб.", "sum", "M",
     "Накопительно с начала года; по РФ — сумма по субъектам."),
    ("vzszopmrvzs", "Ввод жилых зданий", "тыс. м²", "sum", "M",
     "Общая площадь введённых жилых зданий за месяц (Росстат)."),
    ("vzsnopmrvzs", "Ввод нежилых зданий", "тыс. м²", "sum", "M",
     "Общая площадь введённых нежилых зданий за месяц (Росстат)."),
    ("cbr_izhk_rate_m", "Ставка ИЖК", "% годовых", "weighted_hint", "M",
     "Средневзвешенная ставка по ипотечным кредитам в рублях (ЦБ РФ)."),
    ("cbr_izhk_volume_m", "Выдачи ИЖК за месяц", "млн руб.", "sum", "M",
     "Объём предоставленных ипотечных кредитов (ЦБ РФ)."),
    ("cbr_izhk_debt_m", "Задолженность по ИЖК", "млн руб.", "sum", "M",
     "Портфель ипотечных кредитов на начало месяца (ЦБ РФ)."),
    ("rkop_3", "Реализация квартир", "м²", "sum", "M",
     "Объём проданных площадей, канонический срез «регионы / Всего» (ЕИСЖС)."),
    ("01_01_06", "Строящееся жильё на эскроу", "м²", "country", "M",
     "Площадь МКД, строящихся с привлечением средств граждан, на дату (ЕИСЖС)."),
    ("01_03_06", "Цена действующих ДДУ", "млн руб.", "country", "M",
     "Суммарная цена действующих договоров долевого участия (ЕИСЖС)."),
    ("emiss_31074_cpi_prevm_m", "ИПЦ, % к предыдущему месяцу", "%", "median", "M",
     "Индекс потребительских цен, месячная динамика (Росстат/ЕМИСС)."),
    ("emiss_43062_unemp_q", "Уровень безработицы (МОТ)", "%", "median", "Q",
     "Квартальный уровень безработицы (Росстат/ЕМИСС)."),
]

SUBDIM = {"rkop_3": "охват: регионы | статус: Всего"}
LIMIT = {"M": 72, "Q": 24}


def fetch_region_series(code, freq, sub):
    """Ряды по субъектам: одна точка на регион-период (свежий релиз)."""
    flt_sub = " AND (metric_code <> %s OR sub_dimension = %s)" if sub else ""
    params = [code]
    if sub:
        params += [code, sub]
    sql = f"""
        SELECT DISTINCT ON (region_code, period_start)
               region_code, region_name, period_start, value
        FROM derived.v_bi_observation
        WHERE metric_code = %s
          AND region_level = 'region'
          AND value IS NOT NULL
          AND period_start >= CURRENT_DATE - INTERVAL '{int(LIMIT[freq] * 1.34)} months'
          {flt_sub}
        ORDER BY region_code, period_start, release_id DESC
    """
    return d.query(sql, tuple(params))


def fetch_country_series(code, freq, sub):
    flt_sub = " AND (metric_code <> %s OR sub_dimension = %s)" if sub else ""
    params = [code]
    if sub:
        params += [code, sub]
    sql = f"""
        SELECT DISTINCT ON (period_start) period_start, value
        FROM derived.v_bi_observation
        WHERE metric_code = %s
          AND region_level IN ('country', 'aggregate')
          AND value IS NOT NULL
          AND period_start >= CURRENT_DATE - INTERVAL '{int(LIMIT[freq] * 1.34)} months'
          {flt_sub}
        ORDER BY period_start, release_id DESC
    """
    return d.query(sql, tuple(params))


def aggregate(rows_by_region, mode):
    """Свод по РФ из региональных рядов: медиана или сумма по периодам."""
    per_period = {}
    for code, pts in rows_by_region.items():
        for period, value in pts:
            per_period.setdefault(period, []).append(float(value))
    out = []
    for period in sorted(per_period):
        vals = sorted(per_period[period])
        if mode == "sum":
            out.append([period, round(sum(vals), 2)])
        elif mode == "median":
            n = len(vals)
            med = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
            out.append([period, round(med, 2)])
        else:  # Для ставок и долей: медиана как описательный индикатор
            n = len(vals)
            med = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
            out.append([period, round(med, 2)])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="не писать файл, только отчёт")
    args = ap.parse_args()

    if not d.available():
        print("нет доступа к БД (тоннель 15432 не поднят)")
        return 2

    regions = d.query(
        "SELECT region_code, name_ru FROM catalog.region "
        "WHERE level = 'region' AND (valid_to IS NULL OR valid_to > CURRENT_DATE) "
        "ORDER BY name_ru"
    )

    metrics_meta, series = [], {}
    for code, title, unit, agg, freq, note in METRICS:
        sub = SUBDIM.get(code)
        rows = fetch_region_series(code, freq, sub)
        by_region = {}
        for rc, _rn, period, value in rows:
            by_region.setdefault(rc, []).append([period.isoformat(), float(value)])
        for pts in by_region.values():
            pts.sort(key=lambda x: x[0])
            del pts[:-LIMIT[freq]]

        country = fetch_country_series(code, freq, sub)
        if country:
            rf = [[p.isoformat(), float(v)] for p, v in sorted(country)][-LIMIT[freq]:]
            rf_source = "country"
        else:
            rf = aggregate(by_region, "sum" if agg == "sum" else "median")[-LIMIT[freq]:]
            rf_source = agg if agg != "weighted_hint" else "median"

        series[code] = {"by_region": by_region, "rf": rf, "rf_source": rf_source}
        metrics_meta.append({
            "code": code, "title": title, "unit": unit, "freq": freq, "note": note,
            "regions": len(by_region), "last_rf": rf[-1][0] if rf else None,
        })
        print(f"{code:<26} регионов={len(by_region):>3} точек РФ={len(rf):>3} "
              f"край={rf[-1][0] if rf else '-':<10} ({rf_source})")

    payload = {
        "generated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "research_wiki (Росстат, ЦБ РФ, ЕИСЖС/дом.рф); сборка на VPS, витрина статическая",
        "metrics": metrics_meta,
        "regions": [{"code": c, "name": n} for c, n in regions],
        "series": series,
    }

    if args.check:
        print(json.dumps({k: (len(v) if isinstance(v, (list, dict)) else v)
                          for k, v in payload.items()}, ensure_ascii=False))
        return 0

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, OUT)
    size = os.path.getsize(OUT)
    print(f"записано {OUT} ({size / 1024:.0f} КиБ), регионов {len(payload['regions'])}, "
          f"метрик {len(payload['metrics'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
