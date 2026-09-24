#!/usr/bin/env python3
"""Разбор медианных рядов рис. 1 inFOM PDF (ЦБ/инФОМ) -> CSV.

Метод (отработан 24.09.2026, задача t_e8d80e8e):
1) Из текстового слоя берём 99 числовых подписей вида 'd,d' и 33 подписи
   месяцев (координаты через PyMuPDF get_text('words')).
2) Линии рис. 1 — три векторных пути с разными цветами (серый/красный/
   оранжевый); их сегменты 'l' дают 33 точки на серию.
3) Ось Y линейна: калибровка v = A*y + B по однозначным парам «точка пути —
   ближайшая подпись» (95 из 99, остаток <= 0,07 п.п.).
4) Подписи привязываются к сериям по колонке месяца и ошибке |ось - подпись|;
   все 99 пар подтверждаются с ошибкой <= 0,07.

Запуск: python3 scripts/model_sitrep_infom_parse.py [in.pdf] [out.csv]
По умолчанию: raw/cbr/inFOM_26-09.pdf -> data/model_sitrep_infom_medians.csv
"""
import csv
import re
import sys
from pathlib import Path

import fitz

NUM_RE = re.compile(r"^\d{1,2},\d$")
MONTH_RE = re.compile(r"^(янв|фев|мар|апр|май|июн|июл|авг|сен|окт|ноя|дек)\.(24|25|26)$")
ORDER = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
COLOR_NAMES = {
    (0.49796292185783386, 0.49803921580314636, 0.49793240427970886): "observed",
    (0.8709999918937683, 0.0, 0.10999999940395355): "expected_1y",
    (0.9179999828338623, 0.7289999723434448, 0.0): "expected_5y",
}


def mkey(t):
    m, y = t.split(".")
    return (int(y), ORDER.index(m))


def main(pdf_path, out_path):
    doc = fitz.open(pdf_path)
    page = doc[0]
    words = page.get_text("words")
    months, nums = [], []
    for x0, y0, x1, y1, w, *_ in words:
        if MONTH_RE.match(w):
            months.append((x0, y0, w))
        elif NUM_RE.match(w):
            nums.append(((x0 + x1) / 2, (y0 + y1) / 2, w))
    cols = {}
    for x, y, t in months:
        if t not in cols or y < cols[t][1]:
            cols[t] = (x, y)
    col_names = sorted(cols.keys(), key=mkey)
    col_x = [cols[t][0] for t in col_names]
    y_top_months = min(y for x, y, t in months)

    series_pts = {}
    for p in page.get_drawings():
        r = p["rect"]
        npts = sum(1 for it in p["items"] if it[0] == "l")
        if r.y1 < y_top_months and npts >= 30 and p["color"] in COLOR_NAMES:
            pts = []
            for it in p["items"]:
                if it[0] == "l":
                    if not pts:
                        pts.append(it[1])
                    pts.append(it[2])
            series_pts[COLOR_NAMES[p["color"]]] = pts

    # калибровка оси по однозначным парам «точка—подпись»
    pairs = []
    for pts in series_pts.values():
        for pt in pts:
            best, bd = None, 1e9
            for nx, ny, v in nums:
                d = (nx - pt.x) ** 2 + (ny - pt.y) ** 2
                if d < bd:
                    best, bd = v, d
            if bd**0.5 < 22:
                pairs.append((pt.y, float(best.replace(",", "."))))

    def fit(data):
        n = len(data)
        sy = sum(y for y, v in data)
        sv = sum(v for y, v in data)
        syy = sum(y * y for y, v in data)
        syv = sum(y * v for y, v in data)
        A = (n * syv - sy * sv) / (n * syy - sy * sy)
        return A, (sv - A * sy) / n

    data = pairs[:]
    A, B = fit(data)
    kept = [(y, v) for y, v in data if abs(A * y + B - v) < 0.15]
    A, B = fit(kept)
    kept2 = [(y, v) for y, v in kept if abs(A * y + B - v) < 0.08]
    A, B = fit(kept2)
    resid = max(abs(A * y + B - v) for y, v in kept2)
    print(f"калибровка оси: v = {A:.6f}*y + {B:.3f} (n={len(kept2)}, resid<={resid:.3f})")

    # подписи по колонкам; значение серии = ближайшая по значению подпись колонки
    lbl_by_col = {}
    for nx, ny, v in nums:
        i = min(range(33), key=lambda j: abs(col_x[j] - nx))
        lbl_by_col.setdefault(i, []).append(v)

    rows = []
    max_err = 0.0
    for i, name in enumerate(col_names):
        rec = {"month": name}
        for cname in ("observed", "expected_1y", "expected_5y"):
            pt = series_pts[cname][i]
            v_ax = A * pt.y + B
            lbls = lbl_by_col.get(i, [])
            v_lbl = min(
                (float(s.replace(",", ".")) for s in lbls),
                key=lambda f: abs(v_ax - f),
            ) if lbls else v_ax
            err = abs(v_ax - v_lbl)
            max_err = max(max_err, err)
            rec[cname] = f"{v_lbl:.1f}".replace(".", ",")
        rows.append(rec)
    print(f"макс. ошибка подписи: {max_err:.3f}")

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        wcsv = csv.DictWriter(
            f, fieldnames=["month", "observed", "expected_1y", "expected_5y"]
        )
        wcsv.writeheader()
        wcsv.writerows(rows)
    print(f"saved: {out} ({len(rows)} строк)")


if __name__ == "__main__":
    repo = Path.home() / "research-wiki-private"
    pdf = sys.argv[1] if len(sys.argv) > 1 else repo / "raw/cbr/inFOM_26-09.pdf"
    out = sys.argv[2] if len(sys.argv) > 2 else repo / "data/model_sitrep_infom_medians.csv"
    main(str(pdf), str(out))