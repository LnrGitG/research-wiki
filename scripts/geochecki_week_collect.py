#!/usr/bin/env python3
"""Еженедельный сбор геочек ФНС (geochecki): /api/Metrics/bounds по сетке РФ.

Идемпотентен; выход /tmp/gc_geo/geo_week.json + geo_week.csv.
Сетка ~<400 тыс км2 на ячейку (лимит API 500 тыс), res 6-10 по площади.
Координаты запроса — Web-Mercator метры (формула из фронтенда ФНС).
"""
import csv as _csv
import json
import math
import os
import ssl
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone

BASE = "https://geochecki-vpd.nalog.gov.ru"
OUT_DIR = "/tmp/gc_geo"

def merc(lng, lat):
    """lng/lat → Web-Mercator метры."""
    x = 20037508.34 * lng / 180
    y = 20037508.34 * math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180) / 180
    return round(x, 2), round(y, 2)

def area_km2(lng1, lat1, lng2, lat2):
    """Площадь bbox В ЯКОРЯХ СЕРВЕРА (merc-метры r*o/1e6, как считает ФНС)."""
    ax, ay = merc(lng2, lat2)
    bx, by = merc(lng1, lat1)
    return abs(ax - bx) * abs(ay - by) / 1e6  # "км²" по ФНС

def res_for_area(a):
    """Таблица ФНС (r*o/1e6): >5e5 → skip; >5e4 → 6; >5e3 → 7; >500 → 8; >50 → 9; else 10."""
    if a > 500_000: return None
    if a > 50_000: return 6
    if a > 5_000: return 7
    if a > 500: return 8
    if a > 50: return 9
    return 10

# Сетка РФ: ячейки ≤ ~450 тыс км². lng × lat градусы.
# Шаги: 7° lng на широте 55° ≈ 445 км; lat 5° = 555 км. Произведение ~ 300 тыс км2.
# Обжитая полоса РФ: lat 41.5-67.5; ячейки ~300k км²
GRID_CELLS = [
  # (lng1, lat1, lng2, lat2) — подобраны вручную по заселённости
  (28, 43, 35, 48), (35, 43, 42, 48), (42, 43, 48.5, 48),
  (28, 48, 35, 54.5), (35, 48, 42, 54.5), (42, 48, 48.5, 54.5), (48.5, 48, 55.5, 54.5), (55.5, 48, 62.5, 54.5), (62.5, 48, 71, 54.5),
  (28, 54.5, 35, 61), (35, 54.5, 42, 61), (42, 54.5, 49, 61), (49, 54.5, 56, 61), (56, 54.5, 63, 61), (63, 54.5, 70, 61), (70, 54.5, 77, 61), (77, 54.5, 84.5, 61), (84.5, 54.5, 92, 61), (92, 54.5, 100, 61), (100, 54.5, 108, 61), (108, 54.5, 116, 61), (116, 54.5, 124, 61), (124, 54.5, 132, 61), (132, 54.5, 140, 61), (140, 54.5, 148, 61),
  (28, 61, 36, 67.5), (36, 61, 44, 67.5), (44, 61, 52, 67.5), (52, 61, 60, 67.5), (60, 61, 68, 67.5), (68, 61, 76, 67.5), (76, 61, 84, 67.5), (84, 61, 92, 67.5), (92, 61, 100, 67.5), (100, 61, 108, 67.5), (108, 61, 116, 67.5), (116, 61, 124, 67.5), (124, 61, 132, 67.5), (132, 61, 142, 67.5),
]
def build_grid():
    return [(f"cell_{i:02d}", l1, a1, l2, a2) for i, (l1, a1, l2, a2) in enumerate(GRID_CELLS)]

def fetch(bbox, res, retries=2):
    nex, ney = merc(bbox[2], bbox[3])
    swx, swy = merc(bbox[0], bbox[1])
    url = (BASE + f"/api/Metrics/bounds?NorthEast={nex}&NorthEast={ney}"
           f"&SouthWest={swx}&SouthWest={swy}&H3Resolution={res}")
    ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    for att in range(retries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0", "Accept": "application/json",
                "Referer": BASE + "/geochecks"}), timeout=45, context=ctx)
            b = r.read().decode()
            if b.startswith('"'): b = json.loads(b)
            d = json.loads(b)
            return d.get("features") or []
        except Exception:
            if att < retries - 1:
                time.sleep(8)
            else:
                raise

def load_grid():
    """Сетка из data/geochecki_grid.json (мерc-лимит <500k 'км²' ФНС) — фолбэк build_grid()."""
    p = "/tmp/geochecki_grid.json"
    if os.path.exists(p):
        raw = json.load(open(p))
        return [(f"cell_{i:03d}", *c) for i, c in enumerate(raw)]
    return build_grid()

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    today = date.today()
    monday = today - timedelta(days=today.weekday() + 7)
    sunday = monday + timedelta(days=6)
    print("period:", monday, "→", sunday, flush=True)
    all_feats = []
    all_known = set()
    lock = __import__("threading").Lock()
    def process(task):
        name, lng1, lat1, lng2, lat2 = task
        a = area_km2(lng1, lat1, lng2, lat2)
        res = res_for_area(a)
        t0 = time.time()
        try:
            fx = fetch((lng1, lat1, lng2, lat2), res)
        except Exception as e:
            print(f"{name}: ERR {repr(e)[:80]}", flush=True); return
        n_new = 0
        with lock:
            known = all_known
            for f in fx:
                h = f["properties"]["H3Id"]
                if h not in known:
                    known.add(h); all_feats.append(f); n_new += 1
        print(f"{name}: {len(fx)} hex ({n_new} new), res={res}, {round(a)}u, {time.time()-t0:.1f} c", flush=True)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(process, load_grid()))
    json.dump({"period_start": str(monday), "period_end": str(sunday),
               "collected_at": datetime.now(timezone.utc).isoformat(), "features": all_feats},
              open(os.path.join(OUT_DIR, "geo_week.json"), "w"), ensure_ascii=False)
    csv_path = os.path.join(OUT_DIR, "geo_week.csv")
    with open(csv_path, "w", newline="") as fh:
        w = _csv.writer(fh)
        w.writerow(["h3_id", "period_start", "period_end", "kkt_count", "receipt_total_count",
                    "revenue_intensity", "bills_intensity", "average_bill", "median_bill",
                    "cache_bill_pct", "is_ecommerce", "title", "top_categories", "hex_centroid"])
        for f in all_feats:
            p = f["properties"]
            geom = f.get("geometry") or {}
            coords = (geom.get("coordinates") or [[None]])[0]
            cx = (sum(c[0] for c in coords) / len(coords)) if coords and coords[0] else None
            cy = (sum(c[1] for c in coords) / len(coords)) if coords and coords[0] else None
            tc = p.get("TopCategories") or []
            w.writerow([p.get("H3Id"), p.get("PeriodStart"), p.get("PeriodEnd"),
                        json.dumps(p.get("KktCount")) if p.get("KktCount") else None,
                        p.get("ReceiptTotalCount"), p.get("RevenueIntensity"),
                        p.get("IntensityOfNumberBills"), p.get("AverageBill"),
                        p.get("MedianBill"), p.get("CacheBillPercent"),
                        p.get("IsEcommerce"), p.get("Title"),
                        json.dumps(tc, ensure_ascii=False)[:300] if tc else None,
                        f"{cx},{cy}" if cx else None])
    print("features total:", len(all_feats))
    print("csv:", csv_path, os.path.getsize(csv_path), "bytes")

if __name__ == "__main__":
    main()