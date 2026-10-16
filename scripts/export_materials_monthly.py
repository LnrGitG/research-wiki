#!/usr/bin/env python3
"""Add monthly building-materials series to docs/data-summary.json.

Источник — канон PostgreSQL (`data.observation` + `catalog.metric`), не SQLite:
таблица `building_materials_monthly` в `data/rosstat_construction.db` более не
существует (SQLite-лендинг выведен из эксплуатации 16.10.2026).

Дедупликация (важно). Под месячными метриками (`frequency_id=5`) лежат ещё и
годовые итоги: релиз 29 «Rosstat Proizvodstvo_god (annual file)» записал
годовые значения, приклеенные к 1 января, и они сталкиваются с январскими
месячными. Месячный ряд берётся правилом: приоритет релизам, отличным от
годового (release_id=29), а среди оставшихся — наименьшее значение (годовой
итог на порядок-два больше месячного). Правило сверено с прежним SQLite-рядом
значение-в-значение: 967/967 точек, 0 расхождений и 0 потерь.

Adds key: materials_monthly = [{product, date:'YYYY-MM', value}]
Only products with >=60 months are included (avoid stubs). Sorted by product
then date. Compact (rounds to 2 decimals).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../docs/data-summary.json")

# (подпись продукта в JSON, код метрики канона, единица)
PRODUCTS = [
    ("Цемент (все гидравлические)",        "ptvg",  "тыс.т"),
    ("Товарный бетон",                     "ptb",   "тыс.м3"),
    ("Конструкции каркаса ж/б",            "pkk",   "м3"),
    ("Конструкции фундаментов ж/б",        "pkf",   "м3"),
    ("Плиты перекрытий ж/б",               "ppp",   "тыс.м3"),
    ("Кирпич керамический строительный",   "pkks",  "млн усл.кирп"),
    ("Стекло листовое литое/полированное", "psllp", "тыс.м2"),
]

ANNUAL_RELEASE = 29   # «Proizvodstvo_god (annual file)» — годовые итоги под месячной метрикой
MIN_MONTHS = 60       # отсекаем ряды-заглушки

SQL = """
SELECT DISTINCT ON (o.period_start) o.period_start, o.value
FROM data.observation o
JOIN catalog.metric m ON m.metric_id = o.metric_id
WHERE m.metric_code = %s
ORDER BY o.period_start, (o.release_id = %s), o.value
"""


def main():
    units = {}
    data = []
    for label, code, unit in PRODUCTS:
        rows = query(SQL, (code, ANNUAL_RELEASE))
        pts = [(p, v) for p, v in rows if v is not None]
        if len(pts) < MIN_MONTHS:
            print(f"  пропуск {label!r} [{code}]: всего {len(pts)} точек (< {MIN_MONTHS})")
            continue
        units[label] = unit
        for p, v in pts:
            data.append({"product": label, "date": p.strftime("%Y-%m"),
                         "value": round(float(v), 2)})

    data.sort(key=lambda x: (x["product"], x["date"]))

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
