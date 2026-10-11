#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Воспроизводимый сбор количественной привязки §4 статьи
"Гибридный режим ДКП с селективными опциями".

Источники (все — первичные публикации Банка России, кроме ВВП):
  * Экспорт сырой нефти, нефтепродуктов, природного газа, СПГ:
    https://www.cbr.ru/vfs/statistics/credit_statistics/trade/*.xls
  * Внешняя торговля товарами (итог, ФОБ, млн долл.):
    https://www.cbr.ru/vfs/statistics/credit_statistics/trade/trade.xls
  * Платёжный баланс РФ, аналитическое представление (экспорт товаров):
    https://www.cbr.ru/vfs/statistics/credit_statistics/bop/bal_of_payments_ap.xlsx
  * ВВП, текущие цены в долл. США (знаменатель для «доли в ВВП»):
    World Bank API, индикатор NY.GDP.MKTP.CD

Запуск:  python3 collect_energy_export.py
Вывод:   data/energy_export_series.csv + печать таблицы.
"""
import csv
import io
import os
import re
import sys
import urllib.request

import xlrd
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
CACHE = os.path.join(DATA, "_raw")
UA = "Mozilla/5.0"

TRADE = "https://www.cbr.ru/vfs/statistics/credit_statistics/trade/"
BOP = "https://www.cbr.ru/vfs/statistics/credit_statistics/bop/"

# имя файла ЦБ -> (лист, человекочитаемое имя товара)
COMMODITIES = {
    "crude_oil.xls": ("нефть", "Сырая нефть (ТН ВЭД 2709)"),
    "oil_products.xls": ("нефтепродукты", "Нефтепродукты (2710)"),
    "gas.xls": ("газ", "Природный газ (2711)"),
    "Liquefied-Gas.xls": ("сжиженный газ", "Сжиженный природный газ"),
}


def fetch(url, dest):
    """Скачать url в dest, если файла ещё нет (кэш в data/_raw)."""
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        blob = r.read()
    if blob[:1] == b"<":  # HTML вместо бинарника = ошибка/редирект
        raise RuntimeError(f"Получен HTML вместо файла: {url}")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(blob)
    return dest


def annual_values(path, sheet):
    """Годовые значения стоимости (млн долл.) из блока до первого квартального."""
    ws = xlrd.open_workbook(path).sheet_by_name(sheet)
    out = {}
    for i in range(ws.nrows):
        c1 = ws.cell_value(i, 1) if ws.ncols > 1 else ""
        if not isinstance(c1, str):
            continue
        m = re.match(r"^\s*(\d{4})\s*г\.?\s*$", c1.strip())
        if not m:
            continue
        y = int(m.group(1))
        nums = [ws.cell_value(i, j) for j in range(2, ws.ncols)
                if isinstance(ws.cell_value(i, j), float) and ws.cell_value(i, j) != 0.0]
        if nums and y not in out:          # первый (=годовой) блок
            out[y] = nums[1] if len(nums) > 1 else 0.0  # 2-я колонка = стоимость
    return out


def quarterly_2021(path, sheet):
    """Сумма четырёх кварталов 2021 г. — последний опубликованный год ряда."""
    ws = xlrd.open_workbook(path).sheet_by_name(sheet)
    s = 0.0
    for i in range(ws.nrows):
        c1 = ws.cell_value(i, 1) if ws.ncols > 1 else ""
        if isinstance(c1, str) and "2021" in c1 and "квартал" in c1.lower():
            nums = [ws.cell_value(i, j) for j in range(2, ws.ncols)
                    if isinstance(ws.cell_value(i, j), float) and ws.cell_value(i, j) != 0.0]
            if len(nums) > 1:
                s += nums[1]
    return s


def goods_exports(path):
    """Годовой экспорт товаров (млн долл., ФОБ) — лист «Годовые» trade.xls."""
    ws = xlrd.open_workbook(path).sheet_by_name("Годовые")
    out = {}
    for i in range(ws.nrows):
        v0 = ws.cell_value(i, 0)
        if isinstance(v0, float) and 2000 <= v0 <= 2030:
            out[int(v0)] = ws.cell_value(i, 1)
    return out


def bop_goods_exports(path):
    """Экспорт товаров из платёжного баланса (аналитическое представление)."""
    ws = load_workbook(path, read_only=True, data_only=True)["Годы"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[4]
    cols = {}
    for j, h in enumerate(hdr):
        if isinstance(h, str) and "г." in h:
            try:
                cols[int(h.split()[0])] = j
            except ValueError:
                pass
    out = {}
    for r in rows:
        lbl = r[0] if r and isinstance(r[0], str) else None
        if lbl and lbl.strip().lower() == "экспорт":
            for y, j in cols.items():
                out.setdefault(y, r[j])
            break
    return out


def gdp_usd():
    url = ("https://api.worldbank.org/v2/country/RUS/indicator/"
           "NY.GDP.MKTP.CD?format=json&per_page=60&date=2014:2025")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    import json
    with urllib.request.urlopen(req, timeout=60) as r:
        body = json.loads(r.read().decode("utf-8"))
    return {int(x["date"]): x["value"] for x in body[1] if x["value"]}


def main():
    os.makedirs(CACHE, exist_ok=True)
    energy = {}
    for fn, (sheet, label) in COMMODITIES.items():
        path = fetch(TRADE + fn, os.path.join(CACHE, fn))
        ann = annual_values(path, sheet)
        ann[2021] = quarterly_2021(path, sheet)  # год не опубликован — берём сумму кварталов
        energy[label] = ann

    trade_path = fetch(TRADE + "trade.xls", os.path.join(CACHE, "trade.xls"))
    goods = goods_exports(trade_path)

    bop_path = fetch(BOP + "bal_of_payments_ap.xlsx",
                     os.path.join(CACHE, "bal_of_payments_ap.xlsx"))
    bop_goods = bop_goods_exports(bop_path)

    gdp = gdp_usd()

    years = list(range(2015, 2026))
    rows = []
    for y in years:
        vals = {lbl: energy[lbl].get(y) for lbl in energy}
        total = sum(v for v in vals.values() if v)
        g = goods.get(y) or bop_goods.get(y)
        rows.append({
            "year": y,
            "crude_oil": vals["Сырая нефть (ТН ВЭД 2709)"],
            "oil_products": vals["Нефтепродукты (2710)"],
            "gas": vals["Природный газ (2711)"],
            "lng": vals["Сжиженный природный газ"],
            "energy_total": total if total else None,
            "goods_exports": g,
            "share_of_exports_pct": round(100 * total / g, 1) if (total and g) else None,
            "gdp_usd_mn": gdp.get(y),
            "share_of_gdp_pct": round(100 * total * 1e6 / gdp[y], 1) if (total and gdp.get(y)) else None,
        })

    out = os.path.join(DATA, "energy_export_series.csv")
    os.makedirs(DATA, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    hdr = f"{'год':<6}{'нефть':>10}{'нефтепр':>10}{'газ':>9}{'СПГ':>8}{'итого':>10}{'экспорт':>10}{'доля%':>8}{'доля ВВП%':>11}"
    print(hdr)
    for r in rows:
        def fmt(v, w, d=0):
            return f"{v:>{w}.{d}f}" if v is not None else " " * (w - 1) + "—"
        print(f"{r['year']:<6}{fmt(r['crude_oil'], 10)}{fmt(r['oil_products'], 10)}"
              f"{fmt(r['gas'], 9)}{fmt(r['lng'], 8)}{fmt(r['energy_total'], 10)}"
              f"{fmt(r['goods_exports'], 10)}{fmt(r['share_of_exports_pct'], 8, 1)}"
              f"{fmt(r['share_of_gdp_pct'], 11, 1)}")
    print("\nCSV:", out)


if __name__ == "__main__":
    sys.exit(main())