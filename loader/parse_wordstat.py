#!/usr/bin/env python3
"""Парсер Wordstat (CSV 20 фраз x 5 групп, неделя) → v2 (ws_phrases_raw + композит S2-S5)."""
import csv, json, hashlib, datetime
import psycopg

RUN_FILE = "/home/ubuntu/sandbox_datasets/wordstat_weekly_construction.csv"
S2_S5 = {"S2_ihb", "S3_ihb", "S4_ihb", "S5_ihb"}

def main():
    con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
    cur = con.cursor()
    cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code='yandex-wordstat'")
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO v2.dataset (source_id, dataset_code, name_ru, is_active) VALUES ((SELECT source_id FROM v2.source WHERE source_code='yandex'),'yandex-wordstat','Wordstat',TRUE) RETURNING dataset_id")
        ds_id = cur.fetchone()[0]
    else: ds_id = row[0]
    sha = hashlib.sha256(open(RUN_FILE,'rb').read()).hexdigest()
    cur.execute("""INSERT INTO v2.load_run (dataset_id, source_file, file_sha256, parser_version, status)
    VALUES (%s,%s,%s,'parser-wordstat@M2','partial') RETURNING run_id""", (ds_id, RUN_FILE, sha))
    run_id = cur.fetchone()[0]
    con.commit()
    cur.execute("SELECT metric_code, metric_id, frequency_id FROM v2.metric WHERE metric_code IN ('ws_phrases_raw','ws_composite_s25')")
    mm = {r[0]: (r[1], r[2]) for r in cur.fetchall()}
    rid = 1  # РФ
    inserted = 0
    with open(RUN_FILE, newline='', encoding='utf-8') as fh:
        rd = csv.DictReader(fh)
        for rec in rd:
            per = rec['date'].strip()[:10]
            grp = rec['group'].strip()
            val = rec['count']
            mid, fid = mm['ws_phrases_raw']
            cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current, quality_flags)
            VALUES (%s,%s,%s,%s,%s,%s,%s,TRUE,'{}') ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""",
            (mid, rid, fid, per, float(val), float(val), run_id))
            inserted += cur.rowcount
    # композит S2-S5: sum(share) по неделям (lead-1m репликация — сырые значения, композит отдельно)
    comp = {}
    with open(RUN_FILE, newline='', encoding='utf-8') as fh:
        rd = csv.DictReader(fh)
        for rec in rd:
            if rec['group'].strip() in S2_S5:
                per = rec['date'].strip()[:10]
                comp[per] = comp.get(per, 0.0) + float(rec['share'])
    mid, fid = mm['ws_composite_s25']
    n_comp = 0
    for per, val in sorted(comp.items()):
        cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current)
        VALUES (%s,%s,%s,%s,%s,%s,%s,TRUE) ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""",
        (mid, rid, fid, per, val, val, run_id))
        n_comp += cur.rowcount
    con.commit()
    cur.execute("UPDATE v2.load_run SET status='ok', rows_parsed=%s, rows_inserted=%s WHERE run_id=%s", (inserted+n_comp, inserted+n_comp, run_id))
    con.commit()
    print(json.dumps({"run_id": run_id, "phrases": inserted, "composite_weeks": n_comp}))

if __name__ == '__main__':
    main()