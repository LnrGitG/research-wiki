#!/usr/bin/env python3
"""Загрузчик ЦБ VFS 0420218 в v2 (staging → observation)."""
import hashlib, json, re, sys, glob, datetime, unicodedata
import openpyxl
import psycopg

SHEET_MAP = {
  ("02_06","в рублях"): ("cbr_izhk_count_m", None),
  ("02_06","итого"): ("cbr_izhk_count_m", None),
  ("02_07","в рублях"): ("cbr_izhk_volume_m", None),
  ("02_07","итого"): ("cbr_izhk_volume_m", None),
  ("02_08","ставка в рублях"): ("cbr_izhk_rate_m", None),
  ("02_08","срок в руб"): ("cbr_izhk_term_m", None),
  ("02_09","в рублях"): ("cbr_izhk_debt_m", None),
  ("02_09","итого"): ("cbr_izhk_debt_m", None),
  ("02_15","в рублях"): ("cbr_izhk_ddu_volume_m", None),
  ("02_42","в рублях"): (None, None),  # ИЖС-кол-во: отдельная ветка
  ("02_43","в рублях"): (None, None),  # ИЖС-объём
  ("02_44","в рублях"): (None, None),  # доля ИЖС
  ("02_45","ставка в рублях"): (None, None),  # ставка ИЖС
}
MON = {"Январь":1,"Февраль":2,"Март":3,"Апрель":4,"Май":5,"Июнь":6,"Июль":7,
       "Август":8,"Сентябрь":9,"Октябрь":10,"Ноябрь":11,"Декабрь":12}

def datekey(v):
    if isinstance(v, datetime.datetime): return (v.year, v.month)
    if isinstance(v, str):
        m = re.match(r"(\S+)\s+(\d{4})", v.strip())
        if m and m.group(1) in MON: return (int(m.group(2)), MON[m.group(1)])

def num(x):
    if x is None: return None
    s = str(x).replace(" ","").replace(",",".")
    try: return float(s)
    except: return None

def parse_file(path, run_id):
    rows = []
    base = None
    for f in sorted(glob.glob("/home/ubuntu/research-wiki-private/raw/cbr/vfs/02_*.xlsx")):
        prefix = f.split("/")[-1][:5]
        if prefix not in ("02_04","02_05","02_06","02_07","02_08","02_09","02_15","02_42","02_43","02_44","02_45"): continue
        wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
        for sn in wb.sheetnames:
            key = (prefix, sn)
            if key not in SHEET_MAP: continue
            metric_code = SHEET_MAP[key][0]
            if metric_code is None: continue
            grid = list(wb[sn].iter_rows(values_only=True))
            hdr_i = next((i for i,r in enumerate(grid[:8]) if len([c for c in r[1:] if c is not None])>3), None)
            if hdr_i is None: continue
            hdr = grid[hdr_i]
            for r_ in grid:
                nm = str(r_[0]).strip() if r_[0] else ""
                if not nm: continue
                for j in range(1, len(hdr)):
                    dk = datekey(hdr[j])
                    if dk is None: continue
                    val = num(r_[j])
                    if val is None: continue
                    # идемпотентный хеш строки
                    sha = hashlib.sha256(f"{f}|{sn}|{nm}|{dk}|{val}".encode()).hexdigest()[:64]
                    rows.append((prefix, metric_code, nm, f"{dk[0]}-{dk[1]:02d}-01", val, "cbr_vfs", run_id, sha))
        wb.close()
    return rows

def main():
    con = psycopg.connect("host=localhost port=5432 dbname=research_wiki user=wiki")
    cur = con.cursor()
    cur.execute("SELECT dataset_id FROM v2.dataset WHERE dataset_code='cbr-vfs-0420218'")
    ds_id = cur.fetchone()
    if ds_id is None:
        cur.execute("SELECT source_id FROM v2.source WHERE source_code='cbr'")
        cur.execute("INSERT INTO v2.dataset (source_id, dataset_code, name_ru, is_active) VALUES ((SELECT source_id FROM v2.source WHERE source_code='cbr'),'cbr-vfs-0420218','Форма 0420218',TRUE) RETURNING dataset_id")
        ds_id = cur.fetchone()
    else: ds_id = ds_id[0]
    sha_file = hashlib.sha256(open("/dev/stdin","rb").read() if False else b"run-init").hexdigest()
    cur.execute("""INSERT INTO v2.load_run (dataset_id, source_file, file_sha256, parser_version, status)
        VALUES (%s,'raw/cbr/vfs/02_*',%s,'parser-cbr-vfs@M2','partial') RETURNING run_id""", (ds_id, sha_file))
    run_id = cur.fetchone()[0]
    con.commit()
    rows = parse_file(None, run_id)
    print("parsed rows:", len(rows))
    # запись в staging COPY-батчем
    from io import StringIO
    buf = StringIO()
    for r_ in rows:
        buf.write("|".join(str(x) if x is not None else "" for x in r_) + "\n")
    buf.seek(0)
    cur.copy_expert("COPY v2_stage.stg_rows (dataset_code, metric_native, region_name_raw, period_raw, value_raw, unit_native, run_id, row_sha256) FROM STDIN WITH (FORMAT csv, DELIMITER '|')", buf)
    con.commit()
    cur.execute("SELECT count(*) FROM v2_stage.stg_rows WHERE run_id=%s", (run_id,))
    print("staged:", cur.fetchone()[0])
    print(json.dumps({"run_id": run_id, "rows_parsed": len(rows)}))

if __name__ == "__main__":
    main()
