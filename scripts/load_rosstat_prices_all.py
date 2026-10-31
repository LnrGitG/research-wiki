#!/usr/bin/env python3
"""Этап A расширенной рамки прогноза жилья (задача t_3546a0c7), часть 2:
средние цены 1 кв.м жилья Росстата ПО ВСЕМ СУБЪЕКТАМ.

Источник: квартальные публикации Росстата «Средние цены на рынке жилья»
(файлы sred_cen_perv_* / sred_cen_vtor_* на rosstat.gov.ru/storage/mediabank).
Первый лист после «Содержание»: «в целом по субъекту РФ» (в файлах 4kv — лист
«1»). Берём колонку «Все типы квартир» по каждому кварталу.

Глубина: 4kv-2021…4kv-2025 (по 4 квартала) + 2kv-2026 (2 квартала) =
2021Q1…2026Q2, 22 квартала, ~93 региона × 2 рынка.

Загружает public.rosstat_housing_prices_all (market, region, level, quarter, price),
регистрирует в v2 (dataset 19, метрики 17/18 через metric_dataset_map) и прогоняет
приёмку.

Запуск:
    ~/.hermes/hermes-agent/venv/bin/python3 scripts/load_rosstat_prices_all.py
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_tunnel as dbt  # noqa: E402
import xlsx_engine  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "raw" / "rosstat" / "prices"

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4}

# (market, путь, год)
FILES = [
    ("primary",   P / "annual" / "p2021.xlsx", 2021),
    ("primary",   P / "annual" / "p2022.xlsx", 2022),
    ("primary",   P / "annual" / "p2023.xlsx", 2023),
    ("primary",   P / "annual" / "p2024.xlsx", 2024),
    ("primary",   P / "annual" / "p2025.xlsx", 2025),
    ("primary",   P / "sred_cen_perv_2kv-2026.xlsx", 2026),
    ("secondary", P / "annual" / "v2021.xlsx", 2021),
    ("secondary", P / "annual" / "v2022.xlsx", 2022),
    ("secondary", P / "annual" / "v2023.xlsx", 2023),
    ("secondary", P / "annual" / "v2024.xlsx", 2024),
    ("secondary", P / "annual" / "v2025.xlsx", 2025),
    ("secondary", P / "sred_cen_vtor_2kv-2026.xlsx", 2026),
]

RUN_TAG = "rosstat-housing-prices-all-20261002"
DS_ID = 19
DS_CODE = "rosstat-housing-prices-all-q"


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).replace(" ", "").replace("\xa0", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def classify(label):
    up = label.strip().upper()
    if "РОССИЙСКАЯ ФЕДЕРАЦИЯ" in up:
        return "RF"
    if up.endswith("ФЕДЕРАЛЬНЫЙ ОКРУГ"):
        return "federal_district"
    return "region"


def parse_prices(path, year, market, engine=None):
    wb = xlsx_engine.open_workbook(path, engine=engine)
    data_sheets = [s for s in wb.sheetnames if s != "Содержание"]
    ws = wb[data_sheets[0]]
    grid = list(ws.iter_rows(values_only=True))
    wb.close()

    # строка с кварталами
    qrow_i = None
    for i, r in enumerate(grid[:10]):
        if any(isinstance(c, str) and re.match(r"^(I|II|III|IV)\s+квартал", c.strip()) for c in r):
            qrow_i = i
            break
    if qrow_i is None:
        raise RuntimeError("no quarter header in %s" % path)
    qrow = grid[qrow_i]
    qcols = []
    for j, c in enumerate(qrow):
        if isinstance(c, str):
            m = re.match(r"^(I|II|III|IV)\s+квартал", c.strip())
            if m:
                qcols.append((j, ROMAN[m.group(1)]))

    out = []
    for r in grid[qrow_i + 1:]:
        if not r or r[0] is None:
            continue
        lab = str(r[0]).strip()
        m = re.match(r"^[\d\s]+-\s*(.+)$", lab)
        if not m:
            continue
        region = re.sub(r"\s+", " ", m.group(1)).strip()
        if not region or "субъект" in region.lower():
            continue
        level = classify(region)
        for j, q in qcols:
            v = num(r[j]) if j < len(r) else None
            if v is None:
                continue
            out.append((market, region, level, "%dQ%d" % (year, q), v))
    return out, len(qcols)


def build(engine=None):
    parsed = {}
    file_meta = []
    for market, path, year in FILES:
        rows, nq = parse_prices(path, year, market, engine=engine)
        qs = sorted({r[3] for r in rows})
        parsed.setdefault((market, path.name), []).extend(rows)
        file_meta.append((market, path, year, nq))
        print("%-9s %-32s кварталов=%d rows=%-6d depth=%s..%s" %
              (market, path.name, nq, len(rows), qs[0], qs[-1]))
    return parsed, file_meta


DDL = """
CREATE TABLE IF NOT EXISTS public.rosstat_housing_prices_all (
    market   text NOT NULL,
    region   text NOT NULL,
    level    text NOT NULL,
    quarter  text NOT NULL,
    price    double precision
);
CREATE INDEX IF NOT EXISTS rhpa_region_idx ON public.rosstat_housing_prices_all (region, quarter);
CREATE INDEX IF NOT EXISTS rhpa_market_idx ON public.rosstat_housing_prices_all (market);
"""


def load(parsed):
    rows = []
    seen = set()
    for (market, fname), rs in parsed.items():
        for market_, region, level, quarter, v in rs:
            key = (market_, region, quarter)
            if key in seen:
                continue
            seen.add(key)
            rows.append((market_, region, level, quarter, v))
    rows.sort(key=lambda x: (x[0], x[1], x[3]))
    with dbt.connect() as c:
        with c.cursor() as cur:
            cur.execute(DDL)
            cur.execute("TRUNCATE public.rosstat_housing_prices_all")
            cur.execute("GRANT SELECT ON public.rosstat_housing_prices_all TO viewer")
            cur.executemany(
                "INSERT INTO public.rosstat_housing_prices_all (market, region, level, quarter, price) "
                "VALUES (%s,%s,%s,%s,%s)", rows)
        c.commit()
    return rows


def register_v2(file_meta):
    with dbt.connect() as c:
        with c.cursor() as cur:
            cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code=%s", (DS_CODE,))
            row = cur.fetchone()
            if row:
                ds_id = row[0]
            else:
                cur.execute("""INSERT INTO v2.dataset
                    (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
                    VALUES (%s, (SELECT source_id FROM v2.source WHERE source_code='rosstat'),
                            %s, %s, 'https://rosstat.gov.ru/statistics/price', 'quarterly', true)""",
                    (DS_ID, DS_CODE,
                     "Росстат — средние цены 1 кв.м жилья по ВСЕМ субъектам (первичка/вторичка, квартальные)"))
                ds_id = DS_ID
            # метрики 17/18 — расширение в общероссийский разрез
            for mid, native, name in [
                    (17, "rosstat_housing_prices_all:price_new_m2", "Цена 1 кв.м, первичный рынок (все субъекты)"),
                    (18, "rosstat_housing_prices_all:price_secondary_m2", "Цена 1 кв.м, вторичный рынок (все субъекты)")]:
                cur.execute("""INSERT INTO v2.metric_dataset_map
                    (metric_id, dataset_id, native_code, scale_factor)
                    VALUES (%s,%s,%s,1)
                    ON CONFLICT (metric_id, dataset_id) DO NOTHING""", (mid, ds_id, native))

            cur.execute("SELECT coalesce(max(run_id),0) FROM v2.load_run")
            nxt = cur.fetchone()[0] + 1
            run_ids = []
            for market, path, year, nq in file_meta:
                sha = hashlib.sha256(path.read_bytes()).hexdigest()
                cur.execute("""INSERT INTO v2.load_run
                    (run_id, dataset_id, source_file, file_sha256, source_published_at, parser_version,
                     status, rows_parsed, rows_inserted, notes)
                    VALUES (%s,%s,%s,%s,%s,'load_rosstat_prices_all@v1','ok',%s,%s,%s)
                    RETURNING run_id""",
                    (nxt, ds_id, path.name, sha, "%d-12-31" % year, nq * 93, nq * 93,
                     "Росстат средние цены, %s, год %d, кварталов %d" % (market, year, nq)))
                run_ids.append(cur.fetchone()[0])
                nxt += 1
        c.commit()
    return ds_id, run_ids


def acceptance(run_ids):
    checks = []

    def add(kind, passed, detail):
        checks.append((kind, bool(passed), detail))
        print("  [%s] %-42s %s" % ("OK " if passed else "FAIL", kind, detail))

    print("\n=== ПРИЁМКА ===")
    for market in ("primary", "secondary"):
        n_subj = dbt.query("SELECT count(DISTINCT region) FROM public.rosstat_housing_prices_all "
                           "WHERE market=%s AND level='region'", (market,))[0][0]
        add("%s:субъектов>=85" % market, n_subj >= 85, "регионов=%d" % n_subj)
        nq = dbt.query("SELECT count(DISTINCT quarter) FROM public.rosstat_housing_prices_all WHERE market=%s",
                       (market,))[0][0]
        qs = dbt.query("SELECT min(quarter), max(quarter) FROM public.rosstat_housing_prices_all WHERE market=%s",
                       (market,))[0]
        add("%s:глубина=22 (2021Q1..2026Q2)" % market, nq == 22 and qs == ("2021Q1", "2026Q2"),
            "кварталов=%d (%s..%s)" % (nq, qs[0], qs[1]))
        add("%s:строка РФ присутствует" % market,
            dbt.query("SELECT count(*) FROM public.rosstat_housing_prices_all WHERE market=%s AND level='RF'",
                      (market,))[0][0] > 0, "RF-строк: %d" % dbt.query(
                "SELECT count(*) FROM public.rosstat_housing_prices_all WHERE market=%s AND level='RF'", (market,))[0][0])

    for market, q, exp in [("primary", "2021Q1", 83177.29), ("primary", "2026Q1", 219521.77),
                           ("primary", "2026Q2", 221973.62),
                           ("secondary", "2021Q1", 67826.0), ("secondary", "2026Q1", 143953.0),
                           ("secondary", "2026Q2", 146470.0)]:
        got = dbt.query("SELECT price FROM public.rosstat_housing_prices_all "
                        "WHERE market=%s AND level='RF' AND quarter=%s", (market, q))
        got = got[0][0] if got else None
        add("контроль %s РФ %s" % (market, q), got is not None and abs(got - exp) <= 1.0,
            "файл=%.4g ожидание=%.4g" % (got or -1, exp))

    with dbt.connect() as c:
        with c.cursor() as cur:
            cur.execute("DELETE FROM v2.load_check WHERE run_id = ANY(%s) AND checked_by='agent'", (list(run_ids),))
            cur.execute("SELECT coalesce(max(check_id),0) FROM v2.load_check")
            n = cur.fetchone()[0] + 1
            for rid in run_ids:
                for kind, passed, detail in checks:
                    cur.execute("""INSERT INTO v2.load_check
                        (check_id, run_id, check_kind, check_detail, passed, checked_by)
                        VALUES (%s,%s,%s,%s,%s,'agent')""",
                        (n, rid, kind, json.dumps({"detail": detail}, ensure_ascii=False), passed))
                    n += 1
        c.commit()
    npass = sum(1 for _, p, _ in checks if p)
    print("\nитог: %d/%d проверок пройдено" % (npass, len(checks)))
    return {"passed": npass, "total": len(checks)}


def rf_print():
    print("\n== РФ-контроль из файлов ==")
    for market, q in [("primary", "2021Q1"), ("primary", "2026Q1"), ("primary", "2026Q2"),
                      ("secondary", "2021Q1"), ("secondary", "2026Q1"), ("secondary", "2026Q2")]:
        print("  ", market, q, dbt.query(
            "SELECT price FROM public.rosstat_housing_prices_all WHERE market=%s AND level='RF' AND quarter=%s",
            (market, q)))


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Средние цены жилья Росстата по субъектам")
    xlsx_engine.add_engine_arg(ap)
    args = ap.parse_args()
    engine = xlsx_engine.resolve_engine(args.xlsx_engine)
    print("движок чтения xlsx:", engine)
    parsed, file_meta = build(engine)
    rows = load(parsed)
    print("\nвсего строк в таблице:", len(rows))
    ds_id, run_ids = register_v2(file_meta)
    print("v2 dataset_id =", ds_id, "load_run ids =", run_ids)
    rf_print()
    acceptance(run_ids)
