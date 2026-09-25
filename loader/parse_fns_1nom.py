#!/usr/bin/env python3
"""Парсер ФНС 1-НОМ reg-xlsx -> staging v2_stage.fns_rows (конвейер №8, шаг 1)."""
import sys, os, json, glob, hashlib
import openpyxl
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../scripts")

OUT = "/tmp/fns_staging.jsonl"

def classify_region(name):
    n = name.strip().rstrip()
    if not n or n.startswith("в том числе"): return None
    if n == "Российская Федерация": return "RF"
    if n.endswith("федеральный округ"): return "FO"
    return "SUBJECT"

def main():
    files = sorted(glob.glob("/tmp/fns_raw_1nom*reg.xlsx"))
    rows = []
    for f in files:
        snap = None
        base = os.path.basename(f)
        d = base.replace("1nom","").replace("reg.xlsx","")  # ddmmyy
        dd, mm, yy = d[:2], d[2:4], d[4:]
        snapshot = f"20{yy}-{mm}-{dd}"
        wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
        for sheet in wb.sheetnames:
            ws = wb[sheet]
            for r in wb[sheet].iter_rows(min_row=9, values_only=True):
                if not r or r[0] is None: continue
                name = str(r[0]).strip()
                if name.startswith("в том числе") or name in ("А",): continue
                level = classify_region(name)
                if level is None: continue
                # колонки: 0=имя, 1=ОКВЭД, 2=код строки, 3..=показатели
                okved = str(r[1]).strip() if r[1] else ""
                line_code = sheet
                for ci in range(3, len(r)):
                    v = r[ci]
                    if v is None or v == "": continue
                    try: v = float(v)
                    except: continue
                    rows.append({"snapshot": snapshot, "form": "1-NOM", "sheet": sheet,
                                 "level": level, "region_raw": name, "okved": okved,
                                 "col": ci - 2, "value": v})
        wb.close()
    with open(OUT, "w") as fh:
        for r in rows: fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("rows:", len(rows), "snapshots:", sorted({r['snapshot'] for r in rows}))

if __name__ == "__main__":
    main()
