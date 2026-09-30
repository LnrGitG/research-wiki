#!/usr/bin/env python3
"""REPU-РФ v2: полный бэкаст по методу Chen-Mo-Tang-Li 2023 на GDELT DOC API.

Отличие от пилота scripts/repu_housing_pilot.py (там был GKG-корпус на
6 дней сентября 2026): тройной булев запрос «(жильё) (политика)
(неопределённость)» выполняется на стороне GDELT на всём таймлайне
2017-01-01 .. сегодня. Тон считается по статьям, попавшим во все три фильтра
одновременно — это точный аналог метода Chen, где считалась доля статей,
удовлетворяющих тройному словарю.

Запрос (кавычки-фразы и OR по каждому фильтру):
  (housing OR mortgage OR "real estate")
  (policy OR regulation OR decree OR subsidy OR ban)
  (uncertainty OR uncertain OR unstable OR volatile OR unpredictable)
  Russia

Выход:
  data/processed/repu_housing_doc_daily.csv — date, volume, tone
  data/processed/repu_housing_doc_monthly.csv — month, mean_volume, mean_tone,
      repu_index (z по всему ряду)
Контрольные события выводятся в stdout для ручной сверки.
"""
import csv
import json
import os
import statistics
import subprocess
import time
from datetime import datetime, timezone
from urllib.parse import quote

BASE = "https://api.gdeltproject.org/api/v2/doc/doc"
OUT_DAILY = os.path.join(os.path.dirname(__file__), "../data/processed/repu_housing_doc_daily.csv")
OUT_MONTH = os.path.join(os.path.dirname(__file__), "../data/processed/repu_housing_doc_monthly.csv")

QUERY = ("(housing OR mortgage OR \"real estate\") "
         "(policy OR regulation OR decree OR subsidy OR ban) "
         "(uncertainty OR uncertain OR unstable OR volatile OR unpredictable) "
         "Russia")
START_YEAR = 2017


def fetch(url, retries=5):
    for a in range(retries):
        r = subprocess.run(["curl", "-s", "--max-time", "120", url],
                           capture_output=True, text=True, timeout=150)
        body = r.stdout.strip()
        if body.startswith("Please limit requests"):
            wait = 15 * (a + 1)
            print(f"  rate-limit, ждём {wait}s", flush=True)
            time.sleep(wait)
            continue
        if body.startswith("{"):
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                pass
        time.sleep(8 * (a + 1))
    return None


def get_series(mode, start, end):
    url = (f"{BASE}?query={quote(QUERY)}&mode={mode}&format=json"
           f"&startdatetime={start}&enddatetime={end}")
    d = fetch(url)
    if not d:
        return {}
    out = {}
    for series in d.get("timeline", []):
        for p in series.get("data", []):
            out[p["date"][:8]] = p.get("value", 0.0)
    return out


def main():
    os.makedirs(os.path.dirname(OUT_DAILY), exist_ok=True)
    vol, tone = {}, {}
    now = datetime.now(timezone.utc)
    n = 0
    for year in range(START_YEAR, now.year + 1):
        start = f"{year}0101000000"
        end = f"{year}1231235959" if year < now.year else now.strftime("%Y%m%d%H%M%S")
        v = get_series("timelinevol", start, end)
        time.sleep(12)
        t = get_series("timelinetone", start, end)
        time.sleep(12)
        vol.update(v)
        tone.update(t)
        n += len(v)
        print(f"{year}: vol {len(v)}, tone {len(t)} (итого {n})", flush=True)

    days = sorted(set(vol) | set(tone))
    with open(OUT_DAILY, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "volume", "tone"])
        for d in days:
            w.writerow([d, vol.get(d, ""), tone.get(d, "")])
    print(f"DONE daily -> {OUT_DAILY} ({len(days)} дней)", flush=True)

    # Нормировка объёма (0..1) в z-шкалу для сопоставимости с тоном
    vv = [x for x in vol.values() if x != ""]
    v_mu = statistics.mean(vv) if vv else 0.0
    v_sd = statistics.pstdev(vv) if vv else 1.0
    # Месячная агрегация
    months = {}
    for d in sorted(set(vol) | set(tone)):
        m = d[:6]
        months.setdefault(m, {"v": [], "t": []})
        if d in vol and vol[d] != "":
            months[m]["v"].append(float(vol[d]))
        if d in tone and tone[d] != "":
            months[m]["t"].append(float(tone[d]))
    mv = [statistics.mean(m["v"]) for m in months.values() if m["v"]]
    mt = [statistics.mean(m["t"]) for m in months.values() if m["t"]]
    t_mu, t_sd = statistics.mean(mt), (statistics.pstdev(mt) or 1.0)

    rows = []
    for m in sorted(months):
        d = months[m]
        v = statistics.mean(d["v"]) if d["v"] else None
        t = statistics.mean(d["t"]) if d["t"] else None
        rz = (t - t_mu) / t_sd if t is not None else 0.0
        rows.append([m, round(v, 6) if v is not None else "", round(t, 4) if t is not None else "", round(rz, 3)])
    with open(OUT_MONTH, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["month", "mean_volume", "mean_tone", "repu_index"])
        w.writerows(rows)
    print(f"DONE monthly -> {OUT_MONTH} ({len(rows)} месяцев)", flush=True)

    # Контрольные события: индекс в месяце события и через 1-2 месяца после
    ctrl = {
        "2020-04": "запуск льготной ипотеки 6,5%",
        "2020-11": "продление льготной на 2021",
        "2021-06": "изменение условий",
        "2022-03": "расширение семейной после 01.03",
        "2023-01": "правки, закрытие с 01.07.2023",
        "2024-06": "анонс закрытия массовой льготной",
        "2024-07": "закрытие массовой льготной",
    }
    idx = {r[0]: r[3] for r in rows}
    print("\n== Контрольные события (repu_index месяца, +1, +2):")
    for ym, label in ctrl.items():
        if ym in idx:
            i = sorted(idx).index(ym)
            ms = sorted(idx)
            nxt1 = idx[ms[i + 1]] if i + 1 < len(ms) else ""
            nxt2 = idx[ms[i + 2]] if i + 2 < len(ms) else ""
            print(f"   {ym}: {idx[ym]:+.2f} | +1: {nxt1} | +2: {nxt2} | {label}")
        else:
            print(f"   {ym}: нет данных | {label}")


if __name__ == "__main__":
    main()