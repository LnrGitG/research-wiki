#!/usr/bin/env python3
"""Этап A расширенной рамки прогноза жилья (задача t_3546a0c7).

Загружает в research_wiki три региональных ряда ЦБ:
  1. public.cbr_ihk_total  — ИЖК ВСЕГО (ипотечные жилищные кредиты) по субъектам:
     количество (02_10) и объём (02_11), лист «в рублях».
  2. public.cbr_mortgage_terms — средневзвешенный СРОК кредита (мес.), файл 02_13,
     лист «срок в руб» (в базе прежде лежала только ставка — cbr_mortgage_rates).

Дополняет public.cbr_ihk_ddu (ДДУ) — разность «ИЖК всего − ИЖК ДДУ» даёт прокси
вторичного рынка (этап B дизайна). Отличие от public.cbr_housing_loans: там ЖИК
(02_06/02_07, включая неипотечные жилищные кредиты), здесь именно ИЖК.

Схема таблиц как у cbr_ihk_ddu: level/fed_okrug/region/period/metric/value,
period = 'YYYY-MM'. Уровни: RF, federal_district, region, okrug, nested.

Идемпотентно: TRUNCATE + INSERT по таблице, ON CONFLICT DO NOTHING в каталоге.

Запуск:
    ~/.hermes/hermes-agent/venv/bin/python3 scripts/load_cbr_ihk_total_terms.py
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_tunnel as dbt
import load_cbr_primary_market as lpm

ROOT = Path(__file__).resolve().parent.parent
VFS_DIR = ROOT / "raw" / "cbr" / "vfs"
BASE_URL = "https://www.cbr.ru/vfs/statistics/BankSector/Mortgage/%s.xlsx"

# (таблица, файл, лист, метрика)
FILES = [
    ("cbr_ihk_total",        "02_10_Quantity_mortgage",  "в рублях",    "count"),
    ("cbr_ihk_total",        "02_11_New_loans_mortgage", "в рублях",    "volume"),
    ("cbr_mortgage_terms",   "02_13_Rates_mortgage",     "срок в руб",  "term"),
]

# (v2_id, core_id, metric_code, name_ru, unit_v2, unit_core, unit_canonical,
#  table, metric)
METRICS = [
    (58072, 71954, "cbr_ihk_total_count_reg_m",
     "ИЖК всего, количество (рег.)",
     4, 29, "count", "cbr_ihk_total", "count"),
    (58073, 71955, "cbr_ihk_total_volume_reg_m",
     "ИЖК всего, объём (рег.)",
     1, 11, "mln_rub", "cbr_ihk_total", "volume"),
    (58074, 71956, "cbr_mortgage_term_reg_m",
     "Средневзвешенный срок ИЖК, месяцы (рег.)",
     8, 33, "months", "cbr_mortgage_terms", "term"),
]

RUN_TAG = "cbr-ihk-total-terms-20261002"
DS_ID = 18
DS_CODE = "cbr-ihk-total"

DDL = """
CREATE TABLE IF NOT EXISTS public.{tbl} (
    level      text NOT NULL,
    fed_okrug  text,
    region     text NOT NULL,
    period     text NOT NULL,
    metric     text NOT NULL,
    value      double precision
);
CREATE INDEX IF NOT EXISTS {tbl}_region_period_idx ON public.{tbl} (region, period);
CREATE INDEX IF NOT EXISTS {tbl}_metric_idx ON public.{tbl} (metric);
"""


def download(fname):
    dst = VFS_DIR / (fname + ".xlsx")
    import ssl
    import urllib.request
    req = urllib.request.Request(BASE_URL % fname, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120, context=ssl.create_default_context()) as r:
        data = r.read()
    dst.write_bytes(data)
    return dst, hashlib.sha256(data).hexdigest()


def main():
    dbt.available(verbose=True)
    VFS_DIR.mkdir(parents=True, exist_ok=True)

    parsed = {}
    file_meta = []
    for tbl, fname, sheet, metric in FILES:
        path, sha = download(fname)
        rows = lpm.parse_sheet(path, sheet, metric)
        months = sorted({r[3] for r in rows})
        parsed.setdefault(tbl, []).extend(rows)
        file_meta.append((tbl, metric, fname, sha, len(rows), months[0], months[-1], len(months)))
        print("%-20s %-32s %-8s rows=%-6d months=%d (%s..%s)" %
              (tbl, fname, metric, len(rows), len(months), months[0], months[-1]))

    with dbt.connect() as c:
        with c.cursor() as cur:
            for tbl in parsed:
                cur.execute(DDL.format(tbl=tbl))
                cur.execute("TRUNCATE public.%s" % tbl)
                cur.execute("GRANT SELECT ON public.%s TO viewer" % tbl)
            for tbl, rows in parsed.items():
                cur.executemany(
                    "INSERT INTO public.%s (level, fed_okrug, region, period, metric, value) "
                    "VALUES (%%s,%%s,%%s,%%s,%%s,%%s)" % tbl, rows)
        c.commit()

    # ── v2 регистрация ────────────────────────────────────────────────────
    with dbt.connect() as c:
        with c.cursor() as cur:
            cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code=%s", (DS_CODE,))
            row = cur.fetchone()
            if row:
                ds_id = row[0]
            else:
                cur.execute("""INSERT INTO v2.dataset
                    (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
                    VALUES (%s, (SELECT source_id FROM v2.source WHERE source_code='cbr'),
                            %s, %s, 'https://cbr.ru/vfs/statistics/BankSector/Mortgage/', 'monthly', true)""",
                    (DS_ID, DS_CODE,
                     "ЦБ РФ — ИЖК всего по субъектам (02_10/02_11) и средневзвешенный срок (02_13)"))
                ds_id = DS_ID

            for v2_id, core_id, code, name, u2, ucore, ucanon, tbl, metric in METRICS:
                cur.execute("""INSERT INTO v2.metric
                    (metric_id, metric_code, name_ru, definition_ru, domain_id, unit_id,
                     frequency_id, is_aggregate, priority)
                    VALUES (%s,%s,%s,%s,4,%s,2,false,'primary')
                    ON CONFLICT (metric_id) DO NOTHING""",
                    (v2_id, code, name,
                     "Источник: ЦБ РФ, файлы 02_10/02_11 (ИЖК всего) и 02_13 лист «срок в руб». "
                     "Таблица public.%s, метрика '%s'." % (tbl, metric), u2))
                cur.execute("""INSERT INTO v2.metric_dataset_map
                    (metric_id, dataset_id, native_code, scale_factor)
                    VALUES (%s,%s,%s,1)
                    ON CONFLICT (metric_id, dataset_id) DO NOTHING""",
                    (v2_id, ds_id, "%s:%s" % (tbl, metric)))

            cur.execute("SELECT coalesce(max(run_id),0) FROM v2.load_run")
            next_run = cur.fetchone()[0] + 1
            cur.execute("SELECT run_id, source_file FROM v2.load_run WHERE dataset_id=%s", (ds_id,))
            existing = {r[1]: r[0] for r in cur.fetchall()}
            run_ids = []
            for tbl, metric, fname, sha, nrows, mn, mx, ndep in file_meta:
                sf = "%s.xlsx" % fname
                if sf in existing:
                    run_ids.append(existing[sf])
                    continue
                cur.execute("""INSERT INTO v2.load_run
                    (run_id, dataset_id, source_file, file_sha256, source_published_at, parser_version,
                     status, rows_parsed, rows_inserted, notes)
                    VALUES (%s,%s,%s,%s,%s,'load_cbr_ihk_total_terms@v1','ok',%s,%s,%s)
                    RETURNING run_id""",
                    (next_run, ds_id, sf, sha,
                     (mx + "-01") if re.match(r"\d{4}-\d{2}$", mx) else None,
                     nrows, nrows, "таблица public.%s, метрика %s, глубина %s..%s" % (tbl, metric, mn, mx)))
                run_ids.append(cur.fetchone()[0])
                next_run += 1
        c.commit()

    print("\nv2 dataset_id =", ds_id, "load_run ids =", run_ids)
    return ds_id, run_ids, parsed, file_meta


CORE_TAGS = ["v2", "housing", "mortgage", "cbr", "secondary"]


def register_core(ds_id, file_meta):
    depth = {}
    for tbl, metric, fname, sha, nrows, mn, mx, ndep in file_meta:
        depth[(tbl, metric)] = (ndep, mx)
    with dbt.connect() as c:
        with c.cursor() as cur:
            for v2_id, core_id, code, name, u2, ucore, ucanon, tbl, metric in METRICS:
                cur.execute("""INSERT INTO core.metric
                    (metric_id, metric_code, name_ru, short_name_ru, description,
                     unit_id, frequency_id, metric_type, is_derived, status, tags)
                    OVERRIDING SYSTEM VALUE
                    VALUES (%s,%s,%s,%s,%s,%s,5,'primary',false,'active',%s)
                    ON CONFLICT (metric_id) DO NOTHING""",
                    (core_id, code, name, name[:60],
                     "ЦБ РФ, файлы 02_10/02_11 (ИЖК всего) и 02_13 «срок в руб»; "
                     "таблица public.%s, метрика '%s'." % (tbl, metric),
                     ucore, CORE_TAGS))
                ndep, mx = depth[(tbl, metric)]
                cur.execute("""INSERT INTO derived.catalog_facets
                    (metric_id, measure, unit_canonical, seasonally_adjusted, domain,
                     freshness, last_obs_at, depth_obs, is_aggregate, run_id)
                    VALUES (%s,'level',%s,false,'credit','fresh',%s,%s,false,%s)
                    ON CONFLICT (metric_id) DO NOTHING""",
                    (core_id, ucanon, mx + "-01", ndep, RUN_TAG))
                cur.execute("""INSERT INTO v2.freshness
                    (metric_id, last_obs_at, obs_count, freshness, expected_next)
                    VALUES (%s,%s,%s,'fresh',%s)
                    ON CONFLICT (metric_id) DO UPDATE
                      SET last_obs_at=EXCLUDED.last_obs_at, obs_count=EXCLUDED.obs_count,
                          freshness=EXCLUDED.freshness, updated_at=now()""",
                    (v2_id, mx + "-01", ndep, None))
            cur.execute("SELECT setval(pg_get_serial_sequence('core.metric','metric_id'), "
                        "(SELECT max(metric_id) FROM core.metric))")
        c.commit()
    print("core.metric + catalog_facets + v2.freshness зарегистрированы")


def acceptance(run_ids):
    checks = []

    def add(kind, passed, detail):
        checks.append((kind, bool(passed), detail))
        print("  [%s] %-44s %s" % ("OK " if passed else "FAIL", kind, detail))

    print("\n=== ПРИЁМКА ===")
    for tbl in ("cbr_ihk_total", "cbr_mortgage_terms"):
        n_subj = dbt.query("SELECT count(DISTINCT region) FROM public.%s "
                           "WHERE level IN ('region','okrug')" % tbl)[0][0]
        n_reg = dbt.query("SELECT count(DISTINCT region) FROM public.%s WHERE level='region'" % tbl)[0][0]
        add("%s:субъектов>=85" % tbl, n_subj >= 85, "субъектов=%d (region=%d)" % (n_subj, n_reg))
        nmon = dbt.query("SELECT count(DISTINCT period) FROM public.%s" % tbl)[0][0]
        add("%s:глубина=92" % tbl, nmon == 92, "месяцев=%d" % nmon)
        for (metric,) in dbt.query("SELECT DISTINCT metric FROM public.%s ORDER BY 1" % tbl):
            if metric in ("rate", "term", "share"):
                continue
            bad = dbt.query("""
                WITH rf AS (SELECT period, value FROM public.{t} WHERE level='RF' AND metric=%s),
                     sm AS (SELECT period, sum(value) v FROM public.{t} WHERE level='region' AND metric=%s GROUP BY period)
                SELECT count(*) FROM rf JOIN sm USING(period)
                WHERE abs(rf.value - sm.v) > greatest(0.005*abs(rf.value), 1.5)
            """.format(t=tbl), (metric, metric))[0][0]
            add("%s:%s сумма(region)=РФ" % (tbl, metric), bad == 0,
                "расхождений сверх допуска: %d из %d мес" % (bad, nmon))

    # контрольные точки (строка РФ)
    for tbl, metric, period, exp, tol in [
            ("cbr_ihk_total", "count", "2019-01", 81054.0, 0.5),
            ("cbr_ihk_total", "count", "2026-08", 86447.0, 0.5),
            ("cbr_ihk_total", "volume", "2019-01", 173119.0, 0.5),
            ("cbr_ihk_total", "volume", "2026-08", 380633.0, 0.5),
            ("cbr_mortgage_terms", "term", "2019-01", 206.9, 0.05),
            ("cbr_mortgage_terms", "term", "2026-08", 285.7, 0.05)]:
        got = dbt.query("SELECT value FROM public.%s WHERE level='RF' AND metric=%%s AND period=%%s"
                        % tbl, (metric, period))
        got = got[0][0] if got else None
        add("контроль %s/%s/%s" % (tbl, metric, period),
            got is not None and abs(got - exp) <= tol, "файл=%.4g ожидание=%.4g" % (got or -1, exp))

    with dbt.connect() as c:
        with c.cursor() as cur:
            cur.execute("DELETE FROM v2.load_check WHERE run_id = ANY(%s) AND checked_by='agent'", (list(run_ids),))
            cur.execute("SELECT coalesce(max(check_id),0) FROM v2.load_check")
            nxt = cur.fetchone()[0] + 1
            for run_id in run_ids:
                for kind, passed, detail in checks:
                    cur.execute("""INSERT INTO v2.load_check
                        (check_id, run_id, check_kind, check_detail, passed, checked_by)
                        VALUES (%s,%s,%s,%s,%s,'agent')""",
                        (nxt, run_id, kind, json.dumps({"detail": detail}, ensure_ascii=False), passed))
                    nxt += 1
        c.commit()
    n_pass = sum(1 for _, p, _ in checks if p)
    print("\nитог: %d/%d проверок пройдено" % (n_pass, len(checks)))
    return {"passed": n_pass, "total": len(checks)}


if __name__ == "__main__":
    ds_id, run_ids, parsed, file_meta = main()
    register_core(ds_id, file_meta)
    acceptance(run_ids)
