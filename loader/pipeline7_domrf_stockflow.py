#!/usr/bin/env python3
"""Конвейер №7: ДОМ.РФ statseries stock/flow/permits/readiness → v2 (PG→PG, на ВМ)."""
import json
import psycopg

def main():
    con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
    cur = con.cursor()
    cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code='domrf-statseries'")
    ds_id = cur.fetchone()[0]
    cur.execute("INSERT INTO v2.load_run (dataset_id, source_file, file_sha256, parser_version, status) VALUES (%s,%s,%s,'pipeline7-domrf-stockflow@M2','partial') RETURNING run_id", (ds_id, "staging.rosstat_construction__domrf_indicators (stock/flow/permits/readiness)", "pg2pg-domrf-statseries-stockflow-v1"))
    run_id = cur.fetchone()[0]
    con.commit()

    # (indicator_code, data_type) → (metric_code, name, domain, unit_id)
    metrics = {
      ("01_01_01","stock"): ("domrf_stock_bld_cnt",  "ДОМ.РФ: строящиеся МКД по 214-ФЗ, шт (на дату)", 1, 4),
      ("01_01_02","stock"): ("domrf_stock_bld_m2",   "ДОМ.РФ: строящиеся МКД по 214-ФЗ, общая площадь, м2 (на дату)", 1, 7),
      ("01_01_04","stock"): ("domrf_stock_flats_cnt","ДОМ.РФ: строящиеся МКД по 214-ФЗ, квартир, шт (на дату)", 1, 4),
      ("01_02_01","flow"):  ("domrf_flow_bld_cnt",   "ДОМ.РФ: МКД в проектах с проектными декларациями, шт (за период)", 1, 4),
      ("01_02_02","flow"):  ("domrf_flow_bld_m2",    "ДОМ.РФ: МКД с проектными декларациями, общая площадь, м2 (за период)", 1, 7),
      ("01_02_04","flow"):  ("domrf_flow_flats_cnt", "ДОМ.РФ: МКД с проектными декларациями, квартир, шт (за период)", 1, 4),
      ("01_04_01","permits_stock"): ("domrf_permits_stock_cnt", "ДОМ.РФ: действующие разрешения на строительство МКД, шт", 1, 4),
      ("01_04_02","permits_stock"): ("domrf_permits_stock_m2",  "ДОМ.РФ: действующие разрешения на строительство МКД, общая площадь, м2", 1, 7),
      ("01_04_04","permits_stock"): ("domrf_permits_stock_liv_m2","ДОМ.РФ: действующие разрешения, жилая площадь, м2", 1, 7),
      ("01_04_01","permits_flow"):  ("domrf_permits_flow_cnt",  "ДОМ.РФ: выданные разрешения на строительство МКД, шт (за период)", 1, 4),
      ("01_04_02","permits_flow"):  ("domrf_permits_flow_m2",   "ДОМ.РФ: выданные разрешения, общая площадь, м2 (за период)", 1, 7),
      ("01_04_04","permits_flow"):  ("domrf_permits_flow_liv_m2","ДОМ.РФ: выданные разрешения, жилая площадь, м2 (за период)", 1, 7),
    }
    for (native, dt), (mcode, name, dom, unit) in metrics.items():
        cur.execute("SELECT metric_id FROM v2.metric WHERE metric_code=%s", (mcode,))
        row = cur.fetchone()
        if row: mid = row[0]
        else:
            cur.execute("INSERT INTO v2.metric (metric_code, name_ru, domain_id, unit_id, frequency_id, priority) VALUES (%s,%s,%s,%s,2,'core') RETURNING metric_id", (mcode, name, dom, unit))
            mid = cur.fetchone()[0]
        cur.execute("SELECT 1 FROM v2.metric_dataset_map WHERE metric_id=%s AND dataset_id=%s", (mid, ds_id))
        if not cur.fetchone():
            cur.execute("INSERT INTO v2.metric_dataset_map (metric_id, dataset_id, native_code, native_unit, scale_factor) VALUES (%s,%s,%s,%s,1)", (mid, ds_id, native+":"+dt, {"4":"count","7":"m2"}[str(unit)]))
    con.commit()

    # readiness РФ: 2 метрики (по file_name-разрезу: 'Объем строящегося жилья в РФ, млн. кв. м' и 'Уровень строительной готовности')
    # region_name там сломан (тип значения); берём по indicator_code '2 РФ стройготовность' и '5 Регионы стройготовность' с фильтром по имени
    cur.execute("SELECT metric_id FROM v2.metric WHERE metric_code='domrf_uf_volume_mln_m2'")
    row = cur.fetchone()
    if row: uf_mid = row[0]
    else:
        cur.execute("INSERT INTO v2.metric (metric_code, name_ru, domain_id, unit_id, frequency_id, priority) VALUES ('domrf_uf_volume_mln_m2','ДОМ.РФ: объем строящегося жилья РФ, млн м2',1,6,2,'core') RETURNING metric_id")
        uf_mid = cur.fetchone()[0]
    cur.execute("SELECT metric_id FROM v2.metric WHERE metric_code='domrf_readiness_rf'")
    row = cur.fetchone()
    if row: rd_mid = row[0]
    else:
        cur.execute("INSERT INTO v2.metric (metric_code, name_ru, domain_id, unit_id, frequency_id, priority) VALUES ('domrf_readiness_rf','ДОМ.РФ: уровень строительной готовности, доля',1,9,2,'core') RETURNING metric_id")
        rd_mid = cur.fetchone()[0]
    cur.execute("SELECT 1 FROM v2.metric_dataset_map WHERE metric_id=%s AND dataset_id=%s", (uf_mid, ds_id))
    if not cur.fetchone():
        cur.execute("INSERT INTO v2.metric_dataset_map (metric_id, dataset_id, native_code, native_unit, scale_factor) VALUES (%s,%s,'2 РФ стройготовность:объем','млн м2',1)", (uf_mid, ds_id))
    cur.execute("SELECT 1 FROM v2.metric_dataset_map WHERE metric_id=%s AND dataset_id=%s", (rd_mid, ds_id))
    if not cur.fetchone():
        cur.execute("INSERT INTO v2.metric_dataset_map (metric_id, dataset_id, native_code, native_unit, scale_factor) VALUES (%s,%s,'2 РФ стройготовность:готовность','share',1)", (rd_mid, ds_id))
    con.commit()

    ins_total = 0
    for (native, dt), (mcode, name, dom, unit) in metrics.items():
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
        WHERE s.indicator_code = %s AND s.data_type = %s AND s.value IS NOT NULL
          AND (s.region_name IN ('Российская Федерация','Россия') OR r.region_id IS NOT NULL OR r2.region_id IS NOT NULL)
        ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""", (mid, fid, run_id, native, dt))
        ins_total += cur.rowcount
        con.commit()
        print(mcode, cur.rowcount)

    # readiness: 2 агрегата РФ (по indicator_name в поле file_name)
    cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current)
    SELECT %s, 1, 2, s.date::date, s.value, s.value, %s, TRUE
    FROM staging.rosstat_construction__domrf_indicators s
    WHERE s.indicator_code = '2 РФ стройготовность' AND s.region_name = 'Объем строящегося жилья в Российской Федерации, млн. кв. м' AND s.value IS NOT NULL
    ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""", (uf_mid, run_id))
    print("uf_volume", cur.rowcount); ins_total += cur.rowcount; con.commit()
    cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current)
    SELECT %s, 1, 2, s.date::date, s.value*100, s.value, %s, TRUE
    FROM staging.rosstat_construction__domrf_indicators s
    WHERE s.indicator_code = '2 РФ стройготовность' AND s.region_name = 'Уровень строительной готовности, %%' AND s.value IS NOT NULL
    ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""", (rd_mid, run_id))
    print("readiness", cur.rowcount); ins_total += cur.rowcount; con.commit()

    cur.execute("UPDATE v2.load_run SET status='ok', rows_parsed=%s, rows_inserted=%s, rows_rejected=0 WHERE run_id=%s", (ins_total, ins_total, run_id))
    con.commit()
    print(json.dumps({"run_id": run_id, "inserted": ins_total}))
    con.close()

main()
