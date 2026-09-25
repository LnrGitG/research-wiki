import ssl, json, urllib.request, time, sqlite3, csv, os, shutil

HOST = "https://" + "xn--d1aqf" + ".xn--p1ai"  # дом.рф (punycode)
BASE = HOST + "/api/v2/priceindex/living/"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

DB = "/home/lnr/research-wiki-private/data/rosreestr_deals.db"
CSV_PATH = "/home/lnr/research-wiki-private/raw/domrf/price_index/domrf_priceindex_all_regions.csv"


def req(url, body=None, retries=3):
    data = json.dumps(body).encode() if body is not None else None
    hdr = {"Content-Type": "application/json"} if data else {}
    for i in range(retries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, data=data, headers=hdr),
                                       timeout=60, context=CTX)
            return json.load(r)
        except Exception as e:
            print("retry", i, e)
            time.sleep(3)
    raise RuntimeError("request failed: " + url)


full = req(BASE + "changesfull/")
json.dump(full, open("/tmp/changesfull.json", "w"))
dates = full["data"]["filter"]["dates"]
items = full["data"].get("items", [])
max_date = max(dates)  # "2026-08-01"
print("api max date:", max_date, "| n_items:", len(items))

con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute("select max(month) from domrf_price_index")
db_max = cur.fetchone()[0]
print("db max:", db_max)

if max_date <= db_max:
    print("NO UPDATES")
    raise SystemExit

y, m, _ = max_date.split("-")
date_to = f"{y}.{m}.01"
regions = [{"region": it["region"], "estateClass": "Все классы", "rooms": "Комнат", "id": i}
           for i, it in enumerate(items)]
body = {"regions": regions, "date_from": "2021.01.01", "date_to": date_to,
        "haveRF": True, "type": "def"}
chart = req(BASE + "mainchart/", body)
json.dump(chart, open("/tmp/mainchart.json", "w"))

rows = {}
data = chart["data"]["regions"]
for key, series in data.items():
    for it in series.get("items", []):
        mon = (it.get("month_dt") or "")[:10]
        if not mon:
            continue
        rows[(it["region"], mon)] = (it.get("index_value"), it.get("index_diff_month"),
                                     it.get("index_count_deal"))
print("fetched rows:", len(rows))

# старое состояние (для отчёта о ревизиях)
old = {}
cur.execute("select region, month, index_value from domrf_price_index")
for r, mo, v in cur.fetchall():
    old[(r, mo)] = v

new_keys, updated_keys, revisions = 0, 0, []
cur.execute("""create table if not exists domrf_price_index
    (region text, month text, index_value real, mom_pct real, n_deals integer,
     primary key (region, month))""")
for (r, mo), (val, mom, nd) in sorted(rows.items()):
    val = float(val) if val not in (None, "") else None
    mom = float(mom) if mom not in (None, "") else None
    nd = int(nd) if nd not in (None, "") else None
    oldv = old.get((r, mo))
    if oldv is not None:
        updated_keys += 1
        try:
            if oldv is not None and val is not None and abs(val - float(oldv)) > 0.1:
                revisions.append((r, mo, oldv, val))
        except (TypeError, ValueError):
            pass
    else:
        new_keys += 1
    cur.execute("insert or replace into domrf_price_index (region, month, index_value, mom_pct, n_deals, source, ingested) values (?,?,?,?,?,'domrf_priceindex_api',CURRENT_TIMESTAMP)",
                (r, mo, val, mom, nd))
con.commit()
print("new rows:", new_keys, "| existing keys refreshed:", updated_keys)
print("revisions >0.1:", len(revisions))
for r in revisions[:20]:
    print("REV", r)
cur.execute("select max(month), count(*) from domrf_price_index")
print("db now:", cur.fetchone())
con.close()

# CSV: полная перезапись из свежей выгрузки
os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
if os.path.exists(CSV_PATH):
    shutil.copy(CSV_PATH, CSV_PATH + ".bak")
with open(CSV_PATH, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["region", "month", "index_value", "mom_pct", "n_deals"])
    for (r, mo), (val, mom, nd) in sorted(rows.items()):
        w.writerow([r, mo, val, mom, nd])
print("csv written:", CSV_PATH, os.path.getsize(CSV_PATH))