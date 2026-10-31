#!/usr/bin/env python3
"""Где расходится результат разбора одного скрипта под двумя движками."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
script, func = sys.argv[1], sys.argv[2]
files = json.loads(sys.argv[3])
out = {}
for eng in ("openpyxl", "fastexcel"):
    cp = subprocess.run([sys.executable, os.path.join(HERE, "_xlsx_verify_call.py"),
                         script, func, json.dumps(files), eng],
                        capture_output=True, text=True, cwd=ROOT)
    print(eng, "->", cp.stdout.strip()[-200:] or cp.stderr.strip()[-400:])
    if cp.stdout.strip():
        out[eng] = json.loads(cp.stdout.strip().splitlines()[-1])
if len(out) == 2:
    print("sha:", out["openpyxl"].get("sha"), out["fastexcel"].get("sha"),
          "n:", out["openpyxl"].get("n"), out["fastexcel"].get("n"),
          "bytes:", out["openpyxl"].get("bytes"), out["fastexcel"].get("bytes"))
