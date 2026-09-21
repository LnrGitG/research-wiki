#!/usr/bin/env python3
"""Конвейер №6: ДОМ.РФ statseries (sales/ddu regional) staging → v2.observation (PG→PG)."""
import json, hashlib, sys
import psycopg

def main():
    con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
    cur = con.cursor()
    cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code='domrf-statseries'")
    ds_id = cur.fetchone()[0]
    sha = "pg2pg-domrf-statseries-sales-ddu-v1"
    cur.execute("INSERT INTO v2.load_run (dataset_id, source_file, file_sha256, parser_version, status) VALUES (%s,%s,%s,'pipeline6-domrf-statseries@M2','partial') RETURNING run_id", (ds_id, "staging.rosstat_construction__domrf_indicators (sales+ddu regional)", sha))
    run_id = cur.fetchone()[0]
    con.commit()

    metrics = {
      "3 Регионы реализация метры": ("domrf_sales_m2_level", 7),
      "4 Регионы реализация %": ("domrf_sales_pct_level", 5),
      "01_03_01": ("domrf_ddu_active_cnt", 4),
      "01_03_02": ("domrf_ddu_active_m2", 7),
      "01_03_03": ("domrf_ddu_active_rub", 2),
      "01_03_04": ("domrf_ddu_escrow_cnt", 4),
      "01_03_05": ("domrf_ddu_escrow_m2", 7),
      "01_03_06": ("domrf_ddu_escrow_rub", 2),
    }
    ins_total = 0
    for native, (mcode, unit_id) in metrics.items():
        cur.execute("SELECT metric_id, frequency_id FROM v2.metric WHERE metric_code=%s", (mcode,))
        mid, fid = cur.fetchone()
        cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current)
        SELECT %s,
          CASE WHEN s.region_name IN ('Российская Федерация','Россия') THEN 1
               ELSE COALESCE(r.region_id, r2.region_id) END,
          %s, s.date::date, s.value, s.value, %s, TRUE
        FROM staging.rosstat_construction__domrf_indicators s
        LEFT JOIN v2.region r ON LOWER(REPLACE(s.region_name, chr(1105), chr(1077))) = LOWER(REPLACE(r.name_ru, chr(1105), chr(1077)))
        LEFT JOIN v2.region r2 ON LOWER(REPLACE(s.region_name, chr(1105), chr(1077))) =
          CASE LOWER(s.region_name)
            WHEN 'архангельская область' THEN LOWER(REPLACE('архангельская область (без НАО)', chr(1105), chr(1077)))
            WHEN 'тюменская область' THEN LOWER(REPLACE('тюменская область (без ХМАО и ЯНАО)', chr(1105), chr(1077)))
          END
        WHERE s.indicator_code = %s AND s.value IS NOT NULL
          AND (s.region_name IN ('Российская Федерация','Россия') OR r.region_id IS NOT NULL OR r2.region_id IS NOT NULL)
        ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""", (mid, fid, run_id, native))
        ins_total += cur.rowcount
        con.commit()
        print(mcode, cur.rowcount)
    cur.execute("UPDATE v2.load_run SET status='ok', rows_parsed=%s, rows_inserted=%s, rows_rejected=0 WHERE run_id=%s", (ins_total, ins_total, run_id))
    con.commit()
    print(json.dumps({"run_id": run_id, "inserted": ins_total}))
    con.close()

main()
