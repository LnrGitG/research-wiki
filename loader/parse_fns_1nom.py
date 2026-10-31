#!/usr/bin/env python3
"""Парсер ФНС 1-НОМ reg-xlsx -> staging v2_stage.fns_rows (конвейер №8, шаг 1).

Чтение xlsx идёт через scripts/xlsx_engine.py: движок по умолчанию fastexcel
(Rust/calamine), откат — --xlsx-engine openpyxl или XLSX_ENGINE=openpyxl.
Значения и номера строк совпадают с openpyxl (сверено по sha на выгрузке
1-НОМ 01.01.2025, 103 листа, 10 609 строк).
"""
import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../scripts")
import xlsx_engine  # noqa: E402

OUT = "/tmp/fns_staging.jsonl"


def classify_region(name):
    n = name.strip().rstrip()
    if not n or n.startswith("в том числе"): return None
    if n == "Российская Федерация": return "RF"
    if n.endswith("федеральный округ"): return "FO"
    return "SUBJECT"


def main(argv=None):
    ap = argparse.ArgumentParser(description="ФНС 1-НОМ reg-xlsx -> staging JSONL")
    ap.add_argument("--glob", default="/tmp/fns_raw_1nom*reg.xlsx",
                    help="маска файлов выгрузки (по умолчанию /tmp/fns_raw_1nom*reg.xlsx)")
    ap.add_argument("--out", default=OUT,
                    help=f"куда писать JSONL (по умолчанию {OUT})")
    xlsx_engine.add_engine_arg(ap)
    args = ap.parse_args(argv)
    engine = xlsx_engine.resolve_engine(args.xlsx_engine)

    files = sorted(glob.glob(args.glob))
    rows = []
    for f in files:
        base = os.path.basename(f)
        d = base.replace("1nom", "").replace("reg.xlsx", "")  # ddmmyy
        dd, mm, yy = d[:2], d[2:4], d[4:]
        snapshot = f"20{yy}-{mm}-{dd}"
        wb = xlsx_engine.open_workbook(f, engine=engine)
        for sheet in wb.sheetnames:
            for r in wb[sheet].iter_rows(min_row=9, values_only=True):
                if not r or r[0] is None:
                    continue
                name = str(r[0]).strip()
                if name.startswith("в том числе") or name in ("А",):
                    continue
                level = classify_region(name)
                if level is None:
                    continue
                # колонки: 0=имя, 1=ОКВЭД, 2=код строки, 3..=показатели
                okved = str(r[1]).strip() if r[1] else ""
                for ci in range(3, len(r)):
                    v = r[ci]
                    if v is None or v == "":
                        continue
                    try:
                        v = float(v)
                    except (TypeError, ValueError):
                        continue
                    rows.append({"snapshot": snapshot, "form": "1-NOM", "sheet": sheet,
                                 "level": level, "region_raw": name, "okved": okved,
                                 "col": ci - 2, "value": v})
        wb.close()

    with open(args.out, "w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("rows:", len(rows), "files:", len(files), "engine:", engine,
          "snapshots:", sorted({r['snapshot'] for r in rows}))


if __name__ == "__main__":
    main()
