# -*- coding: utf-8 -*-
"""Полная сверка: дневной ряд ключевой ставки hd_base (2013-2026) против БД.

Строит авторитетную лестницу ступеней из дневного ряда, сравнивает с
dkp.rate_level и цепочкой dkp.decision. Выход: /tmp/keyrate_full.txt + отчёт.
"""
import datetime
import sys

import requests
import urllib3

urllib3.disable_warnings()

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
r = requests.post("https://www.cbr.ru/hd_base/KeyRate/",
                  headers=UA, timeout=120, verify=False,
                  data={"UniDbQuery.Posted": "True",
                        "UniDbQuery.From": "01.09.2013",
                        "UniDbQuery.To": "25.09.2026"})
r.raise_for_status()
rows = re.findall(r"<td>\s*(\d{2}\.\d{2}\.\d{4})\s*</td>\s*<td[^>]*>\s*([\d,]+)\s*</td>",
                  r.text) if (re := __import__("re")) else []
series = sorted((datetime.datetime.strptime(d, "%d.%m.%Y").date(),
                 float(v.replace(",", "."))) for d, v in rows)
print(f"дневной ряд: {len(series)} точек, {series[0][0]}..{series[-1][0]}")

# Авторитетная лестница: дни изменения
auth = [(series[0][0], series[0][1])]
for i in range(1, len(series)):
    if series[i][1] != series[i - 1][1]:
        auth.append((series[i][0], series[i][1]))
print(f"авторитетных ступеней: {len(auth)}")
with open("/tmp/keyrate_ladder.txt", "w", encoding="utf-8") as f:
    for d, v in auth:
        f.write(f"{d};{v}\n")

def alevel_at(d):
    lv = None
    for frm, v in auth:
        if frm <= d:
            lv = v
        else:
            break
    return lv

# 1) Сверка цепочки решений: rate_new == уровень на след. рабочий день
def next_business_day(d):
    d += datetime.timedelta(days=1)
    while d.weekday() >= 5:
        d += datetime.timedelta(days=1)
    return d

print("\n== Сверка dkp.decision против дневного ряда:")
rows = query("""
    SELECT d.decision_id, m.meeting_date, d.rate_prev, d.rate_new, d.action
    FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
    ORDER BY m.meeting_date""")
bad = []
for did, md, prev, new, action in rows:
    d = md if isinstance(md, datetime.date) else datetime.date.fromisoformat(str(md)[:10])
    eff = next_business_day(d)
    lv_eff = alevel_at(eff)
    lv_today = alevel_at(d)
    new_f = float(new) if new is not None else None
    prev_f = float(prev) if prev is not None else None
    ok_new = new_f == lv_eff
    ok_prev = prev_f == lv_today
    if not (ok_new and ok_prev):
        bad.append((str(d), did, prev_f, new_f, lv_today, lv_eff))
print(f"расхождений: {len(bad)} из {len(rows)}")
for b in bad:
    print(f"  {b[0]} decision {b[1]}: записано prev={b[2]} new={b[3]}; факт: на дату={b[4]} на вступление={b[5]}")

# 2) Сверка лестницы rate_level против авторитетной
print("\n== Сверка dkp.rate_level против дневного ряда (только точки изменения):")
lv_rows = query("""SELECT effective_from, value FROM dkp.rate_level
                   WHERE rate_code='key_rate' ORDER BY effective_from""")
lv_map = {str(f): float(v) for f, v in lv_rows}
auth_map = {str(d): v for d, v in auth}
all_dates = sorted(set(lv_map) | set(auth_map))
diffs = []
for d in all_dates:
    a, l = auth_map.get(d), lv_map.get(d)
    if a != l:
        diffs.append((d, a, l))
print(f"расхождений лестниц: {len(diffs)}")
for d, a, l in diffs:
    print(f"  {d}: авторитетно={a} в БД={l}")