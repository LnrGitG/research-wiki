#!/usr/bin/env python3
"""Парсер СберИндекс (7 parquet, выгрузка 2026-09-21) → v2. Housing-ядро: 12 метрик."""
import hashlib, json, glob, os, sys
import psycopg
import pyarrow.parquet as pq
import pandas as pd

RAW_GLOB = "/home/ubuntu/sandbox_datasets/raw_sberindex/*.parquet"

FILES = {
  "dinamika-tsen-obyavlenii": ("sber_px_list_{side}",  "price_type",   {"Первичный рынок":"primary","Вторичный рынок":"secondary"}, None, None),
  "predlozheniya-nedvizhimosti": ("sber_offers_cnt_{side}", "offer_type", {"Первичный рынок":"primary","Вторичный рынок":"secondary"}, None, None),
  "real_estate_deals": ("sber_deal_px_median_{side}", "realty", {"Первичный":"primary","Вторичный":"secondary"}, None, None),
  "residential_real_estate_prices": ("sber_res_px_{nov}_{side}", "real_estate_type", {"Первичный рынок":"primary","Вторичный рынок":"secondary"}, "real_estate_novelty", {"Всего":"total","Построенные менее 5 лет назад":"new5","Построенные более 5 лет назад":"old5"}),
}

ALIAS = {
  "архангельская область": "архангельская область (без нао)",
  "кемеровская область - кузбасс": "кемеровская область — кузбасс",
  "тюменская область": "тюменская область (без хмао и янао)",
}

def main():
    con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
    cur = con.cursor()
    cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code='sberindex'")
    ds_id = cur.fetchone()[0]
    cur.execute("SELECT region_id, name_ru FROM v2.region")
    rmap = {nm.strip().lower(): rid for rid, nm in cur.fetchall()}
    def resolve_region(reg):
        k = reg.strip().lower().replace("ё","е")
        if k in rmap: return rmap[k]
        k2 = ALIAS.get(k)
        if k2: return rmap.get(k2.lower().replace("ё","е"))
        return None
    cur.execute("SELECT metric_code, metric_id, frequency_id FROM v2.metric WHERE metric_code LIKE 'sber_%'")
    mm = {r[0]: (r[1], r[2]) for r in cur.fetchall()}
    cur.execute("SELECT m.metric_code, mdm.native_code FROM v2.metric m JOIN v2.metric_dataset_map mdm USING(metric_id) WHERE mdm.dataset_id=%s", (ds_id,))
    native_to_code = {native: code for code, native in cur.fetchall()}
    total_ins = 0; total_rej = 0; report = {}
    run_id = None
    # ревизия: гасим все прежние run-ы этого датасета (версионность: ревизия добавляет версию, старую гасим)
    cur.execute("UPDATE v2.observation o SET is_current=FALSE FROM v2.load_run r WHERE o.run_id=r.run_id AND r.dataset_id=%s AND o.is_current", (ds_id,))
    con.commit()
    for path in sorted(glob.glob(RAW_GLOB)):
        base = os.path.basename(path)
        sha = hashlib.sha256(open(path,'rb').read()).hexdigest()
        cur.execute("INSERT INTO v2.load_run (dataset_id, source_file, file_sha256, parser_version, status) VALUES (%s,%s,%s,'parser-sberindex@M2','partial') RETURNING run_id", (ds_id, base, sha))
        run_id = cur.fetchone()[0]; con.commit()
        df = pq.read_table(path).to_pandas()
        stem = base.split("_ru_")[0]
        if stem not in FILES:
            report[base] = "skipped (non-housing, вне ядра)"
            cur.execute("UPDATE v2.load_run SET status='ok', rows_parsed=0, rows_inserted=0, rows_rejected=0 WHERE run_id=%s", (run_id,)); con.commit()
            continue
        tmpl, dim, sides, nov_col, nov_map = FILES[stem]
        inserted = 0; rejected = 0
        for _, rec in df.iterrows():
            side = sides.get(rec[dim]) if dim is not None else None
            if side is None: continue  # разрезы вне ядра (бизнес/эконом-комфорт)
            if nov_col is not None:
                nov = nov_map.get(rec[nov_col])
                if nov is None: continue
                mcode = tmpl.format(nov=nov, side=side)
            else:
                mcode = tmpl.format(side=side)
            if mcode not in mm: rejected += 1; continue
            reg = rec["ref_area"]
            rid = None if reg == "Россия" else resolve_region(reg)
            if rid is None and reg != "Россия":
                rejected += 1; continue
            # РФ строка: region_id=1
            if reg == "Россия":
                # РФ как регион-агрегат: загружаем в отдельные агрегатные строки? Пока РФ → region_id=1 (is_aggregate)
                rid = 1
            per = str(rec["period"])[:10]
            if stem in ("dinamika-tsen-obyavlenii","predlozheniya-nedvizhimosti"):
                per = per  # 1-е число как есть
            else:
                # end-of-month: привести к 1-му числу следующего... нет — оставить 1-е число того же месяца? 
                # Единая конвенция v2: period_start = первый день месяца. end-of-month → заменить день на 01
                d = pd.to_datetime(rec["period"])
                per = f"{d.year:04d}-{d.month:02d}-01"
            mid, fid = mm[mcode]
            val = float(rec["value"])
            cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current)
            VALUES (%s,%s,%s,%s,%s,%s,%s,TRUE) ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""",
            (mid, rid, fid, per, val, val, run_id))
            inserted += cur.rowcount
        con.commit()
        rej_n = rejected
        cur.execute("UPDATE v2.load_run SET status='ok', rows_parsed=%s, rows_inserted=%s, rows_rejected=%s WHERE run_id=%s", (len(df), inserted, rej_n, run_id))
        con.commit()
        total_ins += inserted; total_rej += rej_n
        report[base] = {"run_id": run_id, "inserted": inserted, "rejected": rej_n}
    # спот-чек: РФ медианная цена сделки вторичка последний месяц
    cur.execute("""SELECT o.period_start, o.value FROM v2.observation o JOIN v2.metric m USING(metric_id)
    WHERE m.metric_code='sber_deal_px_median_secondary' AND o.region_id=1 ORDER BY o.period_start DESC LIMIT 2""")
    spots = cur.fetchall()
    print(json.dumps({"inserted": total_ins, "rejected": total_rej, "report": report, "spot_rus_median_secondary": spots}, ensure_ascii=False, default=str))
    con.close()

if __name__ == "__main__":
    main()
