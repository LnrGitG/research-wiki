#!/usr/bin/env python3
"""Забор дневного ряда ключевой ставки с hd_base/KeyRate (POST UniDbQuery).

Ряд сохраняется в файл: сначала проверяем полноту и правдоподобие, запись в
базу — отдельным шагом. Ступени должны совпадать с уже известной лестницей
dkp.rate_level (64 ступени), иначе ряд забирать нельзя.

Сверка: ключевые точки истории ставки.
  13.09.2013 — 5,50 (введение инструмента)
  16.12.2014 — 17,00 (пик)
  28.02.2022 — 20,00 (экстренное повышение)
  24.07.2026 — 14,00 (последнее известное)
"""
import json
import re
import ssl
import urllib.parse
import urllib.request

OUT = "/home/lnr/research-wiki-private/data/cbr_key_rate_daily.json"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

URL = "https://www.cbr.ru/hd_base/KeyRate/"
ROW_RE = re.compile(r"(\d{2})\.(\d{2})\.(\d{4})</td>\s*<td[^>]*>\s*([\d\s,]+?)\s*</td>")


def fetch(d1, d2):
    form = urllib.parse.urlencode({
        "UniDbQuery.Posted": "True",
        "UniDbQuery.From": d1,
        "UniDbQuery.To": d2,
    }).encode()
    req = urllib.request.Request(
        URL, data=form,
        headers={"User-Agent": "Mozilla/5.0",
                 "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=120, context=CTX) as r:
        return r.read().decode("utf-8", "ignore")


def parse(html):
    out = {}
    for dd, mm, yyyy, val in ROW_RE.findall(html):
        iso = f"{yyyy}-{mm}-{dd}"
        v = float(val.replace("\xa0", "").replace(" ", "").replace(",", "."))
        out[iso] = v
    return out


print("=== забор всего ряда ===")
rows = {}
for lo, hi in (("01.09.2013", "31.12.2019"), ("01.01.2020", "04.10.2026")):
    html = fetch(lo, hi)
    part = parse(html)
    print(f"   {lo}..{hi}: {len(part)} точек")
    rows.update(part)

dates = sorted(rows)
print(f"\n   всего точек: {len(dates)}")
print(f"   диапазон: {dates[0]} .. {dates[-1]}")

# ступени: где значение менялось
steps = []
prev = None
for d in dates:
    if rows[d] != prev:
        steps.append((d, rows[d]))
        prev = rows[d]
print(f"   ступеней: {len(steps)}")

print("\n=== контрольные точки ===")
checks = [("2013-09-13", 5.50), ("2014-12-16", 17.00), ("2022-02-28", 20.00),
          ("2026-07-24", 14.00), ("2026-10-02", 14.00)]
for d, want in checks:
    got = rows.get(d)
    mark = "совпало" if got == want else "РАСХОЖДЕНИЕ"
    print(f"   {d}: ожидалось {want}, получено {got} — {mark}")

print("\n=== первые и последние ступени ===")
for s in steps[:4]:
    print("   ", s)
print("    ...")
for s in steps[-4:]:
    print("   ", s)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"source": URL, "fetched_for": "2013-09-13..2026-10-04",
               "daily": rows, "steps": steps}, f, ensure_ascii=False)
print(f"\n   сохранено: {OUT}")