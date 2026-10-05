#!/usr/bin/env python3
"""Этап 1 (контур БАКЕТ): ДОМ.РФ statseries → catalog + data.observation.

Источники: логика pipeline6/7 (разрезы метрик) 1:1; данные —
staging.rosstat_construction__domrf_indicators (857 862 строк, зеркальный
слепок SQLite, живёт в PG на ВМ). Эталон сверки — v2.observation (is_current),
он остаётся; точка возврата — DELETE по release_id переноса.
"""
import sys, os, json, datetime as dt
sys.path.insert(0, os.path.dirname(__file__))
import db_tunnel

RELEASE_LABEL = "domrf-statseries 2026-09-21 (перенос из v2, этап 1)"

# Маппинг v2.unit_id → catalog.unit_id (проверено запросом 05.10.2026)
UNIT_MAP = {2: 38, 4: 29, 5: 12, 6: 30, 7: 16, 9: 37}  # rub, count(шт), pct, index, ths_sqm, ratio

P6 = [
    # (native_indicator_code, metric_code, v2_unit_id)
    ("3 Регионы реализация метры", "domrf_sales_m2_level", 7),
    ("4 Регионы реализация %",     "domrf_sales_pct_level", 5),
    ("01_03_01", "domrf_ddu_active_cnt", 4),
    ("01_03_02", "domrf_ddu_active_m2", 7),
    ("01_03_03", "domrf_ddu_active_rub", 2),
    ("01_03_04", "domrf_ddu_escrow_cnt", 4),
    ("01_03_05", "domrf_ddu_escrow_m2", 7),
    ("01_03_06", "domrf_ddu_escrow_rub", 2),
]
P7 = [
    # ((code, data_type), metric_code, unit_id, name)
    (("01_01_01","stock"), "domrf_stock_bld_cnt", 4, "ДОМ.РФ: строящиеся МКД по 214-ФЗ, шт (на дату)"),
    (("01_01_02","stock"), "domrf_stock_bld_m2", 7, "ДОМ.РФ: строящиеся МКД по 214-ФЗ, общая площадь, м2"),
    (("01_01_04","stock"), "domrf_stock_flats_cnt", 4, "ДОМ.РФ: строящиеся МКД, квартир, шт (на дату)"),
    (("01_02_01","flow"), "domrf_flow_bld_cnt", 4, "ДОМ.РФ: МКД в проектах с декларациями, шт (за период)"),
    (("01_02_02","flow"), "domrf_flow_bld_m2", 7, "ДОМ.РФ: МКД с декларациями, общая площадь, м2 (за период)"),
    (("01_02_04","flow"), "domrf_flow_flats_cnt", 4, "ДОМ.РФ: МКД с декларациями, квартир, шт (за период)"),
    (("01_04_01","permits_stock"), "domrf_permits_stock_cnt", 4, "ДОМ.РФ: действующие разрешения на строительство МКД, шт"),
    (("01_04_02","permits_stock"), "domrf_permits_stock_m2", 7, "ДОМ.РФ: действующие разрешения, общая площадь, м2"),
    (("01_04_04","permits_stock"), "domrf_permits_stock_liv_m2", 7, "ДОМ.РФ: действующие разрешения, жилая площадь, м2"),
    (("01_04_01","permits_flow"), "domrf_permits_flow_cnt", 4, "ДОМ.РФ: выданные разрешения на строительство МКД, шт (за период)"),
    (("01_04_02","permits_flow"), "domrf_permits_flow_m2", 7, "ДОМ.РФ: выданные разрешения, общая площадь, м2 (за период)"),
    (("01_04_04","permits_flow"), "domrf_permits_flow_liv_m2", 7, "ДОМ.РФ: выданные разрешения, жилая площадь, м2 (за период)"),
]
# v2-эталон готовности (80 строк, value ≈ 40.9565 при value_native ≈ 0.4096): v2 брал
# значение-долю ('Уровень строительной готовности, %' при value<1) и умножал на 100.
# В staging под этим именем есть срезы-двойники (92.68 — не доля); фильтр value<1.
READINESS = [
    ("domrf_uf_volume_mln_m2","ДОМ.РФ: объем строящегося жилья РФ, млн м2",6,
     "Объем строящегося жилья в Российской Федерации, млн. кв. м","s.value"),
    ("domrf_readiness_rf","ДОМ.РФ: уровень строительной готовности, доля",9,
     "Уровень строительной готовности, %","s.value*100"),
]

def main():
    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src_id = cur.execute("SELECT source_id FROM catalog.source WHERE source_code ILIKE '%domrf%'").fetchone()[0]
            region_ru = cur.execute("SELECT region_id FROM catalog.region WHERE region_code='ru'").fetchone()[0]
            rel = cur.execute("SELECT release_id FROM catalog.release WHERE label=%s",(RELEASE_LABEL,)).fetchone()
            release_id = rel[0] if rel else cur.execute("""INSERT INTO catalog.release
                (source_id,label,published_at,status,notes) VALUES (%s,%s,%s,'loaded','перенос из v2 (этап 1); сырьё staging.rosstat_construction__domrf_indicators, выгрузка 2026-09-21') RETURNING release_id""",
                (src_id, RELEASE_LABEL, dt.date(2026,9,21))).fetchone()[0]
            # частота: у v2 fid=2 → код?
            fc = cur.execute("""SELECT f.freq_code FROM v2.frequency f
                JOIN v2.metric m ON m.frequency_id=f.frequency_id
                WHERE m.metric_code='domrf_stock_bld_cnt'""").fetchone()
            fid = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code=%s",(fc[0],)).fetchone()[0]
            conn.commit()
            print(f"source={src_id} release={release_id} частота: v2={fc[0]} → catalog={fid}")

            def ensure_metric(code, name, unit):
                r = cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s",(code,)).fetchone()
                if r: return r[0]
                rid = cur.execute("""INSERT INTO catalog.metric
                    (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                    VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                    (code,name,unit,src_id,fid)).fetchone()[0]
                conn.commit(); return rid

            REGION_SQL = """LOWER(REPLACE(s.region_name, chr(1105), chr(1077))) =
                  LOWER(REPLACE(cr.name_ru, chr(1105), chr(1077)))"""
            ALIAS2_SQL = """LOWER(REPLACE(s.region_name, chr(1105), chr(1077))) =
                  CASE LOWER(s.region_name)
                    WHEN 'архангельская область' THEN LOWER(REPLACE('архангельская область (без нао)', chr(1105), chr(1077)))
                    WHEN 'тюменская область' THEN LOWER(REPLACE('тюменская область (без хмао и янао)', chr(1105), chr(1077))) END"""

            report={}; total=0
            jobs=[]
            for native,(mcode,u) in zip([x[0] for x in P6],[ (x[1],x[2]) for x in P6]):
                jobs.append((mcode, "reg", native, None, u, f"ДОМ.РФ statseries: {native}"))
            for (_native_dtp, mcode, u, name) in P7:
                jobs.append((mcode,"reg",_native_dtp[0],_native_dtp[1],u,name))
            for mcode,name,u,fname,expr in READINESS:
                jobs.append((mcode,"ready",None,None,u,name))

            for mcode,kind,native,dtp,u,name in jobs:
                mid=ensure_metric(mcode,name,UNIT_MAP[u])
                if kind=="reg":
                    wh="AND s.data_type=%s" if dtp else ""
                    cur.execute(f"""INSERT INTO data.observation
                        (metric_id,region_id,period_start,frequency_id,value,
                         assessment_type,observation_status,source_id,release_id,sub_dimension)
                        SELECT %s,
                          CASE WHEN s.region_name IN ('Российская Федерация','Россия') THEN %s
                               ELSE COALESCE(cr.region_id, cr2.region_id) END,
                          s.date::date,%s,s.value,'final','validated',%s,%s,''
                        FROM staging.rosstat_construction__domrf_indicators s
                        LEFT JOIN catalog.region cr ON {REGION_SQL}
                        LEFT JOIN catalog.region cr2 ON {ALIAS2_SQL}
                        WHERE s.indicator_code=%s {wh} AND s.value IS NOT NULL
                          AND (s.region_name IN ('Российская Федерация','Россия')
                               OR cr.region_id IS NOT NULL OR cr2.region_id IS NOT NULL)
                        ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                     assessment_type,sub_dimension,release_id) DO NOTHING""",
                        (mid,region_ru,fid,src_id,release_id,native,*((dtp,) if dtp else ())))
                else:
                    fname,expr = next((f,e) for m2,n2,u2,f,e in READINESS if m2==mcode)
                    extra = "AND s.value < 1" if mcode == "domrf_readiness_rf" else ""
                    cur.execute(f"""INSERT INTO data.observation
                        (metric_id,region_id,period_start,frequency_id,value,
                         assessment_type,observation_status,source_id,release_id,sub_dimension)
                        SELECT %s,%s,s.date::date,%s,{expr},'final','validated',%s,%s,''
                        FROM staging.rosstat_construction__domrf_indicators s
                        WHERE s.indicator_code='2 РФ стройготовность' AND s.region_name=%s
                          AND s.value IS NOT NULL {extra}
                        ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                     assessment_type,sub_dimension,release_id) DO NOTHING""",
                        (mid,region_ru,fid,src_id,release_id,fname))
                ins=cur.rowcount; conn.commit()
                cur.execute("""SELECT count(*) FROM v2.observation o JOIN v2.metric m
                    ON m.metric_id=o.metric_id WHERE m.metric_code=%s AND o.is_current""",(mcode,))
                ref=cur.fetchone()[0]
                cur.execute("SELECT count(*) FROM data.observation WHERE metric_id=%s",(mid,))
                got=cur.fetchone()[0]
                v="OK" if got==ref else f"РАСХОЖДЕНИЕ {ref}→{got}"
                report[mcode]={"inserted":ins,"v2_ref":ref,"canon":got,"verdict":v}; total+=ins
                print(f"  {mcode:<32} ins={ins:>7,} v2={ref:>7,} → {v}")
            print(f"\nИТОГО: {total:,}")
            bad=[k for k,v in report.items() if v["verdict"]!="OK"]
            print("сверка:", "ВСЕ СХОДЯТСЯ" if not bad else f"РАСХОЖДЕНИЙ {len(bad)}: {bad[:5]}")
            json.dump(report,open("/tmp/domrf_transfer.json","w"),ensure_ascii=False,indent=1)

if __name__=="__main__":
    main()