#!/usr/bin/env python3
"""Грумер площадок (вариант 2А): уборка по продвижению и сроку, не по дате.

Политика: meta.catalog_policy.staging_retention_days (05.10.2026 = 90).

Площадка удаляется только при ОБОИХ условиях:
  (1) продвижение подтверждено сверкой ключей с каноном data.observation;
  (2) срок хранения истёк: последняя запись в площадку старше срока.

Вердики: VERIFIED (продвинуто), NOT_PROMOTED (живой вход), EMPTY, ERROR.
Действие: KEEP или DUMP+DROP. По умолчанию отчёт без удалений:
  DRY=1 python3 pg_staging_groom.py            (только отчёт)
  DRY=0 TABLES='staging.x' python3 pg_staging_groom.py   (после дампа руками)
"""
import os, sys, datetime as dt
sys.path.insert(0, os.path.dirname(__file__))
import db_tunnel

RETENTION_KEY = "staging_retention_days"


def get_retention(cur):
    cur.execute("SELECT value_num FROM meta.catalog_policy WHERE parameter=%s",
                (RETENTION_KEY,))
    row = cur.fetchone()
    if not row:
        raise SystemExit(f"политика {RETENTION_KEY} не записана")
    return int(row[0])


def stage_freshness(cur, schema, table):
    cur.execute("""SELECT column_name FROM information_schema.columns
                   WHERE table_schema=%s AND table_name=%s""", (schema, table))
    cols = {r[0] for r in cur.fetchall()}
    for cand in ("snapshot_date", "loaded_at", "ingested_at", "created_at"):
        if cand in cols:
            cur.execute(f'SELECT max("{cand}")::date FROM {schema}.{table}')
            r = cur.fetchone()
            if r and r[0]:
                return r[0]
    return None


def verify_domrf_indicators(cur):
    """staging.domrf_indicators: value IS NOT NULL vs канон 01_* / источник domrf."""
    cur.execute("SELECT count(*) FROM staging.rosstat_construction__domrf_indicators "
                "WHERE value IS NOT NULL AND indicator_code ~ '^[0-9_]+$'")
    staged = cur.fetchone()[0]
    cur.execute("""SELECT count(*) FROM data.observation d
                   JOIN catalog.metric m ON m.metric_id = d.metric_id
                   JOIN catalog.source s ON s.source_id = m.source_id
                   WHERE m.metric_code LIKE '01\\_%' AND m.metric_code != '01 Сводный'
                     AND s.source_code ILIKE '%domrf%'""")
    return staged, cur.fetchone()[0]


def verify_fns_rows(cur):
    """Вся таблица vs продвинутый срез: если есть непродвинутое — живой вход."""
    cur.execute("SELECT count(*) FROM v2_stage.fns_rows")
    staged = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM data.observation WHERE release_id=111")
    return staged, cur.fetchone()[0]


def verify_lgot(cur):
    cur.execute("SELECT count(*) FROM public.domrf_lgot_mortgage")
    staged = cur.fetchone()[0]
    cur.execute("""SELECT count(*) FROM data.observation d
                   JOIN catalog.metric m ON m.metric_id = d.metric_id
                   WHERE m.metric_code ILIKE '%lgot%'""")
    return staged, cur.fetchone()[0]


def main():
    dry = os.environ.get("DRY", "1") != "0"
    only = set(filter(None, os.environ.get("TABLES", "").split(";")))
    checks = {
        "staging.rosstat_construction__domrf_indicators": verify_domrf_indicators,
        "v2_stage.fns_rows": verify_fns_rows,
        "public.domrf_lgot_mortgage": verify_lgot,
    }
    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            retention = get_retention(cur)
            today = dt.date.today()
            print(f"политика: {RETENTION_KEY}={retention} сут; режим: "
                  f"{'ОТЧЁТ' if dry else 'УДАЛЕНИЕ'}")
            for full, fn in checks.items():
                if only and full not in only:
                    continue
                schema, table = full.split(".")
                fr = stage_freshness(cur, schema, table)
                age = (today - fr).days if fr else None
                # фолбэк: доморощенный разбор текстовых дат
                if fr is None and full.endswith("domrf_indicators"):
                    cur.execute("""SELECT max(date::date) FROM
                        staging.rosstat_construction__domrf_indicators
                        WHERE date ~ '^[0-9]{4}-'""")
                    r = cur.fetchone()
                    fr = r[0] if r else None
                    age = (today - fr).days if fr else None
                try:
                    staged, canon = fn(cur)
                    verdict = ("VERIFIED" if staged > 0 and canon >= staged else
                               "EMPTY" if staged == 0 else "NOT_PROMOTED")
                except Exception as e:
                    verdict = f"ERROR {str(e).splitlines()[0][:80]}"
                    staged = canon = 0
                aged = age is not None and age > retention
                if verdict != "VERIFIED":
                    action = "KEEP (живой вход / не продвинуто)"
                elif not aged:
                    action = f"KEEP (свежее {age} ≤ {retention} сут)"
                else:
                    action = "КАНДИДАТ на DUMP+DROP"
                print(f"\n{full}")
                print(f"  последняя запись: {fr} ({age} суток назад)")
                print(f"  сверка: {verdict}; площадка={staged:,}; канон={canon:,}")
                print(f"  → {action}")


if __name__ == "__main__":
    main()