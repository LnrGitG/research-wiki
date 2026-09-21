#!/usr/bin/env python3
import psycopg, json
con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
cur = con.cursor()
run_id = int(__import__("sys").argv[1])
# ok-строки → observation (is_current=TRUE). Конфликт UNIQUE (metric, region, freq, period, run) пропускаем
cur.execute("""SELECT r.metric_code, r.region_id, r.period_start, r.value
FROM v2_stage.stg_resolve r WHERE r.run_ref IS NULL AND r.status='ok'""") if False else None
cur.execute("""SELECT m.metric_id, m.metric_code, u.unit_id, f.frequency_id FROM v2.metric m JOIN v2.unit u USING(unit_id) JOIN v2.frequency f USING(frequency_id) WHERE m.metric_code LIKE 'cbr_%'""")
mmap = {r[1]: (r[0], r[2], r[3]) for r in cur.fetchall()}
cur.execute("""SELECT s.metric_native, r.region_id, r.period_start, r.value
FROM v2_stage.stg_resolve r JOIN v2_stage.stg_rows s USING(stg_id)
WHERE r.status='ok' AND s.run_id=%s""", (run_id,))
inserted = 0
for mn, rid, per, val in cur.fetchall():
    mid, uid, fid = mmap[mn]
    cur.execute("""INSERT INTO v2.observation (metric_id, region_id, frequency_id, period_start, value, value_native, run_id, is_current)
    VALUES (%s,%s,%s,%s,%s,%s,%s,TRUE) ON CONFLICT (metric_id, region_id, frequency_id, period_start, run_id) DO NOTHING""",
    (mid, rid, fid, per, val, val, run_id))
    inserted += cur.rowcount
con.commit()
# спот-чек: Белгородская, Т_16 июнь 993
cur.execute("""SELECT o.value FROM v2.observation o
JOIN v2.metric m ON m.metric_id=o.metric_id
WHERE m.metric_code='cbr_izhk_count_m' AND o.region_id=10 AND o.period_start='2026-06-01'""")
spot = cur.fetchone()
print(json.dumps({"inserted": inserted, "spot_belgorod_izhk_count_2026-06": spot[0] if spot else None, "expected": 993}))
# статусы run
cur.execute("UPDATE v2.load_run SET status='ok', rows_parsed=(SELECT count(*) FROM v2_stage.stg_rows WHERE run_id=%s), rows_inserted=%s, rows_rejected=(SELECT count(*) FROM v2_stage.stg_resolve WHERE status!='ok') WHERE run_id=%s", (run_id, inserted, run_id))
con.commit()
# счётчики v2
cur.execute("SELECT count(*) FROM v2.observation")
print("total observation:", cur.fetchone()[0])
