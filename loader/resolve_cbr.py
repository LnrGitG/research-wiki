#!/usr/bin/env python3
"""Резолвер staging → v2.observation для cbr-vfs."""
import psycopg, json
con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
cur = con.cursor()
run_id = int(__import__("sys").argv[1])
# резолв: metric_native -> metric_code; region_name_raw -> region_id
cur.execute("""SELECT m.metric_code, m.metric_id, u.unit_id, f.frequency_id
FROM v2.metric m JOIN v2.unit u USING(unit_id) JOIN v2.frequency f USING(frequency_id)
WHERE m.metric_code LIKE 'cbr_%'""")
mmap = {r[0]: (r[1], r[2], r[3]) for r in cur.fetchall()}
cur.execute("SELECT region_id, name_ru FROM v2.region")
rmap = {}
for rid, nm in cur.fetchall():
    rmap[nm.strip().lower()] = rid
# алиасы «срез»-строк, которые НЕ регионы
SKIP = {"российская федерация","центральный федеральный округ","северо-западный федеральный округ",
 "южный федеральный округ","северо-кавказский федеральный округ","приволжский федеральный округ",
 "уральский федеральный округ","сибирский федеральный округ","дальневосточный федеральный округ",
 "республика крым","севастополь","белгородская область"}
# Белгородская - регион, нужен. Скипать только ФО и РФ
SKIP = {"российская федерация","центральный федеральный округ","северо-западный федеральный округ",
 "южный федеральный округ","северо-кавказский федеральный округ","приволжский федеральный округ",
 "уральский федеральный округ","сибирский федеральный округ","дальневосточный федеральный округ",
 "новые территории","донецкая народная республика","луганская народная республика",
 "запорожская область","херсонская область"}
cur.execute("SELECT stg_id, metric_native, region_name_raw, period_raw, value_raw FROM v2_stage.stg_rows WHERE run_id=%s", (run_id,))
ok = rej = 0
resolve_rows = []
for sid, mn, rn, pr, vr in cur.fetchall():
    mn = mn.strip(); rn = (rn or "").strip(); 
    if mn not in mmap:
        rej += 1; resolve_rows.append((sid, None, None, None, None, "reject_metric", "unknown metric "+mn)); continue
    if rn.lower() in SKIP:
        rej += 1; resolve_rows.append((sid, None, None, None, None, "reject_region", "aggregate "+rn)); continue
    rid = rmap.get(rn.lower())
    if rid is None:
        rej += 1; resolve_rows.append((sid, None, None, None, None, "reject_region", "unknown region "+rn)); continue
    mid, uid, fid = mmap[mn]
    try:
        val = float(vr)
    except: 
        rej += 1; resolve_rows.append((sid, None, None, None, None, "reject_period", "bad value "+str(vr))); continue
    ok += 1
    resolve_rows.append((sid, mid, rid, pr[:10], val, "ok", None))
# массовая запись resolve
from io import StringIO
buf = StringIO()
for t in resolve_rows:
    buf.write("|".join("" if x is None else str(x) for x in t) + "\n")
buf.seek(0)
with cur.copy("COPY v2_stage.stg_resolve (stg_id, metric_code, region_id, period_start, value, status, reject_reason) FROM STDIN WITH (FORMAT csv, DELIMITER " + chr(39) + "|" + chr(39) + ")") as cp:
    cp.write(buf.read())
con.commit()
print(json.dumps({"resolved_ok": ok, "rejected": rej}))
