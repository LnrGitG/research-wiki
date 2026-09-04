#!/usr/bin/env python3
"""
Сборщик бухгалтерской отчётности (РПБУ/РСБУ) девелоперов с bo.nalog.gov.ru

API ФНС:
1. Поиск: GET /advanced-search/organizations?inn={INN}&page=0&pageSize=5
2. BFO: GET /nbo/organizations/{org_id}/bfo/?period={YYYY}
3. Скачать XML: GET /download/original/{correctionId}?isCb=false (может быть закрыт)

Доступные данные через API (JSON):
- Баланс (форма 0710001): строки 1100-1700 (внеоборотные/оборотные активы, капитал, долг)
- ОФР (форма 0710002): строки 2110-2400 (выручка, прибыль от продаж, чистая прибыль)
- Отчёт о движении денежных средств: не всегда доступен

Ограничения:
- Глубина: 6 последних отчётных периодов (3 года)
- Скачивание исходного XML: "Organization closed for public use" для некоторых компаний
- Данные в JSON: полные (все статьи баланса и ОФР)
"""

import json
import urllib.request
import urllib.parse
import time
import os
import sys
from pathlib import Path

BASE_URL = "https://bo.nalog.gov.ru"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"{BASE_URL}/organizations-card/0"
}

# Реестр девелоперов: name → INN
# Источник: Приложение 2 ДОМ.РФ, e-disclosure, открытые источники
DEVELOPERS = {
    "ПИК":       {"inn": "7713011336", "group": "ПАО «ПИК СЗ»", "okved": "41.20"},
    "Самолёт":   {"inn": "9731004688", "group": "ПАО «ГК Самолёт»", "okved": "70.22"},
    "А101":      {"inn": "7704810149", "group": "ООО «А101»", "okved": "68.10.23"},
    "Эталон":    {"inn": "7826009627", "group": "АО «Эталон»", "okved": "68.20.2"},
    "ДАРС":      {"inn": "2322028526", "group": "ООО «ДАРС»", "okved": "41.2"},
    "АПРИ":      {"inn": "7810708323", "group": "АО «АПРИ»", "okved": "68.20"},
    "ЛСР":       {"inn": "7716957114", "group": "ООО «ЛСР»", "okved": "41.20"},
    "Главстрой": {"inn": "7715918377", "group": "ООО «Главстрой»", "okved": "43.22"},
    "Брусника":  {"inn": "7000003653", "group": "ООО «Сибакадемстрой»", "okved": "41.20"},
    "Крост":     {"inn": "0411103450", "group": "ООО «Крост-3»", "okved": "68.20.2"},
}


def fetch_json(url, retries=3):
    """GET request with retries"""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read())
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise


def find_organization(inn):
    """Поиск организации по ИНН → org_id"""
    url = f"{BASE_URL}/advanced-search/organizations?inn={inn}&page=0&pageSize=5"
    data = fetch_json(url)
    if data.get("content"):
        return data["content"][0]
    return None


def get_bfo(org_id, period=None):
    """Получить БФО (баланс + ОФР) для организации"""
    url = f"{BASE_URL}/nbo/organizations/{org_id}/bfo/"
    if period:
        url += f"?period={period}"
    data = fetch_json(url)
    return data


def extract_financials(bfo_data):
    """Извлечь ключевые финансовые метрики из BFO JSON"""
    results = []
    for item in bfo_data:
        period = item.get("period")
        for tc in item.get("typeCorrections", []):
            corr = tc.get("correction", {})
            if not corr:
                continue

            balance = corr.get("balance") or {}
            finresult = corr.get("financialResult") or {}

            # Баланс (форма 0710001) — тыс. руб.
            non_current_assets = balance.get("current1100")     # Внеоборотные активы
            current_assets = balance.get("current1200")         # Оборотные активы
            total_assets = balance.get("current1700")           # Валюта баланса
            long_term_debt = balance.get("current1410")         # Долгосрочные заемные средства
            short_term_debt = balance.get("current1510")        # Краткосрочные заемные средства
            equity = balance.get("current1300")                 # Капитал и резервы

            # ОФР (форма 0710002) — тыс. руб.
            revenue = finresult.get("current2110")              # Выручка
            operating_profit = finresult.get("current2200")     # Прибыль (убыток) от продаж
            net_profit = finresult.get("current2400")           # Чистая прибыль (убыток)

            # Метрики
            total_debt = (long_term_debt or 0) + (short_term_debt or 0)
            de_ratio = total_debt / equity if equity and equity != 0 else None

            okved_info = item.get("organizationInfo", {}) or {}
            result = {
                "period": period,
                "correction_id": corr.get("id"),
                "balance": {
                    "non_current_assets": non_current_assets,
                    "current_assets": current_assets,
                    "total_assets": total_assets,
                    "equity": equity,
                    "long_term_debt": long_term_debt,
                    "short_term_debt": short_term_debt,
                    "total_debt": total_debt,
                },
                "income_statement": {
                    "revenue": revenue,
                    "operating_profit": operating_profit,
                    "net_profit": net_profit,
                },
                "ratios": {
                    "debt_to_equity": de_ratio,
                },
                "okved2": (okved_info.get("okved2") or {}).get("name") if isinstance(okved_info.get("okved2"), dict) else okved_info.get("okved2"),
                "knd": item.get("knd"),
            }
            results.append(result)
    return results


def collect_developer(name, inn, output_dir):
    """Собрать БФО для одного девелопера"""
    print(f"\n{'='*60}")
    print(f"  {name} (ИНН: {inn})")
    print(f"{'='*60}")

    # 1. Поиск организации
    org = find_organization(inn)
    if not org:
        print(f"  NOT FOUND")
        return None

    org_id = org["id"]
    print(f"  Organization ID: {org_id}")
    print(f"  Name: {org['shortName']}")
    print(f"  OKVED2: {org.get('okved2', 'N/A')}")

    # 2. Получаем BFO
    bfo_data = get_bfo(org_id)
    print(f"  BFO records: {len(bfo_data)}")

    # 3. Извлекаем финансовые метрики
    financials = extract_financials(bfo_data)

    # 4. Сохраняем
    result = {
        "developer": name,
        "inn": inn,
        "organization": {
            "id": org_id,
            "name": org["shortName"],
            "okved2": org.get("okved2"),
            "status": org.get("statusCode"),
        },
        "bfo_count": len(bfo_data),
        "financials": financials,
    }

    outfile = output_dir / f"{name.lower()}_rsbu.json"
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  Saved: {outfile}")

    # 5. Печать сводки
    print(f"\n  {'Period':<8} {'Revenue':>12} {'Net Profit':>12} {'Total Assets':>14} {'D/E':>8}")
    print(f"  {'-'*60}")
    for fin in sorted(financials, key=lambda x: x["period"]):
        rev = fin["income_statement"]["revenue"]
        net = fin["income_statement"]["net_profit"]
        assets = fin["balance"]["total_assets"]
        de = fin["ratios"]["debt_to_equity"]
        print(f"  {fin['period']:<8} {rev or 0:>12.0f} {net or 0:>12.0f} {assets or 0:>14.0f} {de or 0:>8.2f}")

    return result


def main():
    output_dir = Path("raw/rsbu")
    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = []
    for name, info in DEVELOPERS.items():
        inn = info.get("inn")
        if not inn:
            print(f"\n  {name}: SKIP (no INN — {info.get('note', '')})")
            continue

        try:
            result = collect_developer(name, inn, output_dir)
            if result:
                all_results.append(result)
        except Exception as e:
            print(f"  ERROR: {e}")

        time.sleep(1)  # Rate limit

    # Сохраняем агрегированный файл
    if all_results:
        outfile = output_dir / "developers_rsbu_summary.json"
        with open(outfile, "w", encoding="utf-8") as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        print(f"\n\nSummary saved: {outfile}")
        print(f"Total developers collected: {len(all_results)}")


if __name__ == "__main__":
    main()