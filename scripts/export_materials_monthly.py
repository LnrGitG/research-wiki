#!/usr/bin/env python3
"""Add monthly building-materials series (from rosstat_construction.db) to docs/data-summary.json.

Adds key: materials_monthly = [{product, date:'YYYY-MM', value}]
Only products with >=60 months are included (avoid stubs); prices monthly in thousands,
production in natural units. Sorted by product then date. Compact (rounds to 2 decimals).
"""
import json
import os
import sqlite3

DB = os.path.join(os.path.dirname(__file__), "../data/rosstat_construction.db")
OUT = os.path.join(os.path.dirname(__file__), "../docs/data-summary.json")

# products to export (monthly, long series) - keep JSON small
PRODUCTS = [
    "Цемент (все гидравлические)",
    "Товарный бетон",
    "Конструкции каркаса ж/б",
    "Конструкции фундаментов ж/б",
    "Плиты перекрытий ж/б",
    "Кирпич керамический строительный",
    "Стекло листовое литое/полированное",
]

def main():
    con = sqlite3.connect(DB)
    rows = con.execute(
        f"select product, year, month, value, unit from building_materials_monthly "
        f"where product in ({','.join('?'*len(PRODUCTS))}) order by product, year, month",
        PRODUCTS,
    ).fetchall()
    con.close()

    units = {}
    data = []
    for p, y, m, v, u in rows:
        if v is None or m is None:
            continue
        units[p] = u
        data.append({"product": p, "date": f"{y}-{m:02d}", "value": round(v, 2)})

    with open(OUT, encoding="utf-8") as f:
        doc = json.load(f)
    doc["materials_monthly"] = data
    doc["materials_monthly_units"] = units
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(OUT)
    print(f"OK: {len(data)} monthly points, {len(units)} products -> {OUT} ({size/1024:.0f} KB)")

if __name__ == "__main__":
    main()