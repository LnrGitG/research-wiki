#!/usr/bin/env python3
"""Этап 1.3: СберИндекс (7 parquet, срез 21.09) → catalog + data.observation.

Вход: /home/ubuntu/sandbox_datasets/raw_sberindex/*.parquet (ВМ).
Логика — 1:1 из parse_sberindex.py (шаблоны, алиасы, период-конвенция, РФ-агрегат).
Загружаем parquet с ВМ в память по SSH (cat | pq.read_table), вставка — executemany.
Точка возврата: DELETE WHERE release_id=<новый>.
"""
import sys, os, io, glob, json, hashlib, subprocess, datetime as dt
sys.path.insert(0, os.path.dirname(__file__))
import db_tunnel

RELEASE_LABEL = "sberindex 2026-09-21 (перенос из v2, этап 1.3)"
SSH = ["ssh", "-o", "BatchMode=yes", "-i", "/home/lnr/.ssh/id_yc",
       "ubuntu@89.169.168.214"]
RAW_DIR = "/home/ubuntu/sandbox_datasets/raw_sberindex/"

FILES = {
    "dinamika-tsen-obyavlenii": ("sber_px_list_{side}", "price_type",
        {"Первичный рынок":"primary","Вторичный рынок":"secondary"}, None, None),
    "predlozheniya-nedvizhimosti": ("sber_offers_cnt_{side}", "offer_type",
        {"Первичный рынок":"primary","Вторичный рынок":"secondary"}, None, None),
    "real_estate_deals": ("sber_deal_px_median_{side}", "realty",
        {"Первичный":"primary","Вторичный":"secondary"}, None, None),
    "residential_real_estate_prices": ("sber_res_px_{nov}_{side}", "real_estate_type",
        {"Первичный рынок":"primary","Вторичный рынок":"secondary"}, "real_estate_novelty",
        {"Всего":"total","Построенные менее 5 лет назад":"new5","Построенные более 5 лет назад":"old5"}),
}
ALIAS = {
    "архангельская область": "архангельская область (без нао)",
    "кемеровская область - кузбасс": "кемеровская область — кузбасс",
    "тюменская область": "тюменская область (без хмао и янао)",
}
UNIT_MAP = {3: 14, 4: 29, 2: 38}
NAMES = {  # metric_code → (name, v2_unit_id)
    "sber_px_list_primary":     ("СберИндекс: средняя цена предложения (объявления), первичный рынок, тыс. руб./м2", 3),
    "sber_px_list_secondary":   ("СберИндекс: средняя цена предложения (объявления), вторичный рынок, тыс. руб./м2", 3),
    "sber_offers_cnt_primary":  ("СберИндекс: число офферов, первичный рынок, шт", 4),
    "sber_offers_cnt_secondary":("СберИндекс: число офферов, вторичный рынок, шт", 4),
    "sber_deal_px_median_primary":  ("СберИндекс: медианная цена сделки, первичный рынок, руб./м2", 2),
    "sber_deal_px_median_secondary":("СберИндекс: медианная цена сделки, вторичный рынок, руб./м2", 2),
    "sber_res_px_new5_primary":  ("СберИндекс: средняя цена предложения, новостройки (<5 лет), первичный рынок, тыс. руб./м2", 3),
    "sber_res_px_new5_secondary":("СберИндекс: средняя цена предложения, новостройки (<5 лет), вторичный рынок, тыс. руб./м2", 3),
    "sber_res_px_old5_primary":  ("СберИндекс: средняя цена предложения, старый фонд (>5 лет), первичный рынок, тыс. руб./м2", 3),
    "sber_res_px_old5_secondary":("СберИндекс: средняя цена предложения, старый фонд (>5 лет), вторичный рынок, тыс. руб./м2", 3),
    "sber_res_px_total_primary":  ("СберИндекс: средняя цена предложения, всего, первичный рынок, тыс. руб./м2", 3),
    "sber_res_px_total_secondary":("СберИндекс: средняя цена предложения, всего, вторичный рынок, тыс. руб./м2", 3),
}


def main():
    import pyarrow.parquet as pq
    import pandas as pd
    files = subprocess.run(SSH + ["ls", RAW_DIR], capture_output=True, text=True).stdout.split()
    print("файлов на ВМ:", len(files))
    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src = cur.execute("SELECT source_id FROM catalog.source WHERE source_code ILIKE '%smartlab%' OR source_code ILIKE '%sber%'").fetchone()
            src_id = src[0] if src else cur.execute("""INSERT INTO catalog.source (source_code,name_ru) VALUES ('sberindex','СберИндекс') RETURNING source_id""").fetchone()[0]
            freq_m = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='M'").fetchone()[0]
            rel = cur.execute("SELECT release_id FROM catalog.release WHERE label=%s",(RELEASE_LABEL,)).fetchone()
            release_id = rel[0] if rel else cur.execute("""INSERT INTO catalog.release
                (source_id,label,published_at,status,notes) VALUES (%s,%s,%s,'loaded','перенос СберИндекс (этап 1.3); сырьё ВМ parquet, срез 2026-09-21') RETURNING release_id""",
                (src_id, RELEASE_LABEL, dt.date(2026,9,21))).fetchone()[0]
            conn.commit()
            # регион-карта + РФ
            region_ru = cur.execute("SELECT region_id FROM catalog.region WHERE region_code='ru'").fetchone()
            region_ru = region_ru[0] if region_ru else max((r[0] for r in cur.execute("SELECT region_id FROM catalog.region")), default=None)+1
            rmap = {nm.strip().lower().replace("ё","е"): rid for rid, nm in
                    cur.execute("SELECT region_id, name_ru FROM catalog.region").fetchall()}
            def resolve_region(reg):
                k = reg.strip().lower().replace("ё","е")
                if k in rmap: return rmap[k]
                k2 = ALIAS.get(k)
                if k2: return rmap.get(k2.lower().replace("ё","е"))
                return None
            # метрики: создать при отсутствии
            midmap = {}
            for mc,(name,v2u) in NAMES.items():
                r = cur.execute("SELECT metric_id FROM catalog.metric WHERE metric_code=%s",(mc,)).fetchone()
                if r: midmap[mc]=r[0]
                else:
                    midmap[mc]=cur.execute("""INSERT INTO catalog.metric
                        (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                        VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                        (mc,name,UNIT_MAP[v2u],src_id,freq_m)).fetchone()[0]
                    conn.commit()
            rows=[]; skipped_files=[]
            for f in files:
                path = RAW_DIR+f
                base = f
                stem = base.split("_ru_")[0]
                if stem not in FILES:
                    skipped_files.append(base); continue
                tmpl, dim, sides, nov_col, nov_map = FILES[stem]
                # читать parquet через ssh stdout
                r2 = subprocess.run(SSH + ["cat", path], capture_output=True)
                buf = io.BytesIO(r2.stdout); tbl = pq.read_table(buf)
                df = tbl.to_pandas()
                sha = hashlib.sha256(r2.stdout).hexdigest()
                ins_per_file=0; rej=0
                for _, rec in df.iterrows():
                    side = sides.get(rec[dim]) if dim in df.columns else None
                    if side is None: continue
                    if nov_col is not None:
                        nov = nov_map.get(rec[nov_col])
                        if nov is None: continue
                        mcode = tmpl.format(nov=nov, side=side)
                    else:
                        mcode = tmpl.format(side=side)
                    if mcode not in midmap: rej+=1; continue
                    reg = rec["ref_area"]
                    if reg == "Россия": rid = region_ru
                    else:
                        rid = resolve_region(reg)
                        if rid is None: rej+=1; continue
                    d = pd.to_datetime(rec["period"])
                    per = f"{d.year:04d}-{d.month:02d}-01"
                    val = float(rec["value"])
                    rows.append((midmap[mcode], rid, per, freq_m, val, src_id, release_id))
                print(f"  {base[:-40]}… sha={sha[:10]} строк={len(df)} parsed={ins_per_file}")
            print("строк собрано:", len(rows), "| файлов вне housing-ядра:", skipped_files)
            # executemany пачками
            B=4000; inserted=0
            for i in range(0,len(rows),B):
                cur.executemany("""INSERT INTO data.observation
                    (metric_id,region_id,period_start,frequency_id,value,
                     assessment_type,observation_status,source_id,release_id,sub_dimension)
                    VALUES (%s,%s,%s,%s,%s,'final','validated',%s,%s,'')
                    ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                 assessment_type,sub_dimension,release_id) DO NOTHING""", rows[i:i+B])
                inserted += cur.rowcount
                print(f"  пакет {i//B+1}: нараст.={inserted:,}", flush=True)
            conn.commit()
            # сверка по-метрично
            bad=[]; total_ref=0
            for mc, mid in midmap.items():
                ref = cur.execute("""SELECT count(*) FROM v2.observation o JOIN v2.metric m
                    ON m.metric_id=o.metric_id WHERE m.metric_code=%s AND o.is_current""",(mc,)).fetchone()[0]
                got = cur.execute("SELECT count(*) FROM data.observation WHERE metric_id=%s",(mid,)).fetchone()[0]
                total_ref += ref
                ok = got==ref
                if not ok: bad.append((mc, ref, got))
                print(f"  {mc:<30} canon={got:>6,} v2={ref:>6,} {'OK' if ok else 'РАСХ'}")
            print(f"\nИТОГО canon={inserted:,} (по метрикам сумма может отличаться), v2-эталон={total_ref:,}")
            print("расхождений:", len(bad), bad[:5])

if __name__ == "__main__":
    main()