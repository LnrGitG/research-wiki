#!/usr/bin/env python3
"""Этап 3: сбор РСБУ-панели 10 девелоперов (bo.nalog.gov.ru) → firm-level nowcast блок.
Метрики: выручка (2110), прибыль от продаж (2200), чистая прибыль (2400), активы (1600/actives).
Формат: годовые БФО + промежуточные (если есть) с actualBfoDate → real-time vintage.
Выход: data/developers_rsbu.csv (company, period, metric, value, actual_date).
API не агрессивный: 10 компаний × ~4 запроса, sleep 3с.
"""
import sys, json, time, csv
sys.path.insert(0, '/home/lnr/research-wiki/scripts')
from collect_rsbu import DEVELOPERS, find_organization, get_bfo

LINES = {"2110": "revenue", "2200": "op_profit", "2400": "net_profit"}

rows = []
for name, meta in DEVELOPERS.items():
    try:
        org = find_organization(meta["inn"])
        if not org:
            print(f"[{name}] org not found"); continue
        org_id = org["id"]
        bfo = get_bfo(org_id)
        for item in bfo:
            period = str(item.get("period", ""))
            actual = item.get("actualBfoDate", "")
            actives = item.get("actives")
            if actives:
                rows.append({"company": name, "period": period, "metric": "assets",
                             "value": float(actives), "actual_date": actual})
            # строки ОФР: typeCorrections[].correction.balance (2110, 2200, 2400, 1600)
            tc_list = item.get("typeCorrections") or []
            for tc in tc_list:
                corr = tc.get("correction") or {}
                bal = corr.get("balance") or {}
                fr = corr.get("financialResult") or {}
                mapping_bal = {"current1600": "assets_full"}
                mapping_fr = {"current2110": "revenue", "previous2110": "revenue_prev",
                              "current2200": "op_profit", "current2400": "net_profit"}
                for fld, metric in mapping_bal.items():
                    val = bal.get(fld)
                    if val:
                        rows.append({"company": name, "period": period, "metric": metric,
                                     "value": float(val), "actual_date": actual})
                for fld, metric in mapping_fr.items():
                    val = fr.get(fld)
                    if val:
                        rows.append({"company": name, "period": period, "metric": metric,
                                     "value": float(val), "actual_date": actual})
        print(f"[{name}] ok, bfo items: {len(bfo)}")
    except Exception as e:
        print(f"[{name}] ERR {str(e)[:70]}")
    time.sleep(3)

# Дебаг-структура для первого item, если строки ОФР не нашлись в data.*
if rows and not any(r['metric'] == 'revenue' for r in rows):
    print("WARN: строки ОФР не найдены — вывести структуру первого item")
    org = find_organization(DEVELOPERS['ПИК']['inn']); bfo = get_bfo(org['id'])
    print(json.dumps(bfo[0], ensure_ascii=False)[:1500])

with open('/home/lnr/research-wiki/data/developers_rsbu.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=["company", "period", "metric", "value", "actual_date"])
    w.writeheader(); w.writerows(rows)
print("saved:", len(rows), "-> data/developers_rsbu.csv")