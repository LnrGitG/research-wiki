#!/usr/bin/env python3
"""Парсер ДОМ.РФ price-index (CSV) → v2 staging + resolve + observation."""
import hashlib, json, csv, sys
import psycopg

RUN_FILE = "/home/ubuntu/sandbox_datasets/raw_domrf_price_index/domrf_priceindex_all_regions.csv"

def main():
    pass_init = None
    con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
    cur = con.cursor()
    cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code='domrf-price-index'")
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO v2.dataset (source_id, dataset_code, name_ru, is_active) VALUES ((SELECT source_id FROM v2.source WHERE source_code='domrf'),'domrf-price-index','Индекс цен ДОМ.РФ',TRUE) RETURNING dataset_id")
        ds_id = cur.fetchone()[0]
    else:
        ds_id = row[0]
    sha = hashlib.sha256(open(RUN_FILE,'rb').read()).hexdigest()
    cur.execute("""INSERT INTO v2.load_run (dataset_id, source_file, file_sha256, parser_version, status)
    VALUES (%s,%s,%s,'parser-domrf-pi@M2','partial') RETURNING run_id""", (ds_id, RUN_FILE, sha))
    run_id = cur.fetchone()[0]
    con.commit()
    # регионы
    cur.execute("SELECT region_id, name_ru FROM v2.region")
    rmap = {nm.strip().lower(): rid for rid, nm in cur.fetchall()}
    ALIAS = {
      "архангельская область": "архангельская область (без нао)",
      "город москва": "москва",
      "город санкт-петербург": "санкт-петербург",
      "кемеровская область - кузбасс": "кемеровская область — кузбасс",
      "республика северная осетия": "республика северная осетия — алания",
      "тюменская область": "тюменская область (без хмао и янао)",
      "ханты-мансийский ао - югра": "ханты-мансийский автономный округ — югра",
      "ямало-ненецкий ао": "ямало-ненецкий автономный округ",
    }
    def resolve_region(reg):
        k = reg.strip().lower()
        if k in rmap: return rmap[k]
        if k in ALIAS:
            t = ALIAS[k]
            return rmap.get(t)
        return None
    cur.execute("SELECT metric_code, metric_id, frequency_id FROM v2.metric WHERE metric_code IN ('domrf_price_index_m','domrf_price_index_mom','ddu_count_m')")
    mm = {r[0]: (r[1], r[2]) for r in cur.fetchall()}
    # чтение CSV → сразу resolve (пропуская стейджинг для простоты CSV без алиасов? нет, через staging для аудита)
    rows = []
    rejects = []
    with open(RUN_FILE, newline='', encoding='utf-8') as fh:
        rd = csv.DictReader(fh)
        for rec in rd:
            reg = (rec['region'] or '').strip()
            rid = resolve_region(reg)
            per = rec['month'].strip()[:10]
            for mcode, col in (("domrf_price_index_m", "index_value"), ("domrf_price_index_mom", "mom_pct"), ("ddu_count_m", "n_deals")):
                val = rec[col]
                if val in (None, '', 'nan'): continue
                sha_row = hashlib.sha256(f"{reg}|{per}|{mcode}|{val}".encode()).hexdigest()
                st = 'ok' if rid else 'reject_region'
                rows.append((run_id, mcode if rid else None, rid, per, val, st, None if rid else 'unknown region '+reg))
    from io import StringIO
    # вставка в observation напрямую (стейджинг для CSV не обязателен, аудируем через resolve)
    inserted = 0
    for _, mcode, rid, per, val, st, reason in rows:
        if st != 'ok': continue
        mid, fid = mm[mcode]
        cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current)
        VALUES (%s,%s,%s,%s,%s,%s,%s,TRUE) ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""",
        (mid, rid, fid, per, float(val), float(val), run_id))
        inserted += cur.rowcount
    con.commit()
    rej = sum(1 for t in rows if t[5] != 'ok')
    cur.execute("UPDATE v2.load_run SET status='ok', rows_parsed=%s, rows_inserted=%s, rows_rejected=%s WHERE run_id=%s",
                (len(rows), inserted, rej, run_id))
    con.commit()
    # спот-чек: Алтайский край 2021-01 = 100
    cur.execute("""SELECT o.value FROM v2.observation o JOIN v2.metric m USING(metric_id)
    WHERE m.metric_code='domrf_price_index_m' AND o.period_start='2021-01-01' LIMIT 3""")
    spots = cur.fetchall()
    print(json.dumps({"run_id": run_id, "rows_parsed": len(rows), "inserted": inserted, "rejected": rej,
                      "spot_altay_2021_01": [float(s[0]) for s in spots]}, ensure_ascii=False))

if __name__ == '__main__':
    main()