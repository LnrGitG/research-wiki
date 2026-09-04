#!/usr/bin/env python3
"""
Единая панель оперативных финансовых оценок девелоперов РФ

Схема записи (panel row):
    company:        название компании
    ticker:         тикер Мосбиржи (если есть)
    inn:            ИНН
    standard:       MSFO | RSBU
    period:         YYYYQn (квартал) | YYYY (год)
    metric:         revenue | ebitda | net_profit | debt | net_debt | equity | ...
    value:          числовое значение (млрд руб, если не указано иное)
    unit:           млрд_руб | млн_руб | pct | multiple
    source:         smartlab | fns_bonalog | corpbonds | marketpower | ir_pdf | nkr | expert_ra | freedom_fg | atsogoev
    source_url:     URL источника
    estimate_date:  дата оценки/отчёта (когда опубликовано)
    update_date:    дата обновления в нашей базе (сегодня)
    confidence:     primary (IR/первоисточник) | aggregator (Smart-Lab) | analyst (Freedom/atsogoev) | rating (НКР)

Источники:
1. Smart-Lab:    PIKK, SMLT, ETLN, LSRG, GLRX, GGRP, APRI, KROT (РСБУ+МСФО, квартал)
2. ФНС bo.nalog: 10 девелоперов (РСБУ, год) — collect_rsbu.py
3. CorpBonds:    разборы отчётов (из сниппетов/текстов)
4. marketpower:  IR-пресс-релизы
5. Freedom FG:   аналитические обзоры (smart-lab.ru/company/freedom_finance_global/blog/)
6. atsogoev:     разборы (smart-lab.ru/blog/)
7. НКР:          агрегаты 11 застройщиков (через СМИ)
8. Эксперт РА:   отраслевые обзоры
"""

import json
import urllib.request
import time
import re
import os
from datetime import datetime, date
from pathlib import Path
from lxml import html

TODAY = date.today().isoformat()

# ============================================================
#  ВСЕЛЕННАЯ КОМПАНИЙ
# ============================================================

COMPANIES = {
    # Публичные (Мосбиржа) — Smart-Lab квартал
    "PIKK":  {"name": "ПИК",              "ticker": "PIKK", "inn": "7713011336", "public": True},
    "SMLT":  {"name": "Самолёт",          "ticker": "SMLT", "inn": "9731004688", "public": True},
    "ETLN":  {"name": "Эталон",           "ticker": "ETLN", "inn": "7826009627", "public": True},
    "LSRG":  {"name": "ЛСР",              "ticker": "LSRG", "inn": "7805027146", "public": True},
    "GLRX":  {"name": "Глоракс",          "ticker": "GLRX", "inn": None,         "public": True},
    "GGRP":  {"name": "Джи Групп",        "ticker": "GGRP", "inn": None,         "public": True},
    "APRI":  {"name": "АПРИ",             "ticker": "APRI", "inn": "7709820278", "public": True},
    "KROT":  {"name": "КРОСТ",            "ticker": "KROT", "inn": "7702020992", "public": True},
    # Непубличные — только ФНС bo.nalog (годовая РСБУ)
    "A101":  {"name": "А101",             "ticker": None,   "inn": "7728270055", "public": False},
    "DARS":  {"name": "ДАРС",             "ticker": None,   "inn": "7713006328", "public": False},
    "BRUS":  {"name": "Брусника",         "ticker": None,   "inn": "6671376530", "public": False},
    "GLAV":  {"name": "Главстрой",        "ticker": None,   "inn": "7707765240", "public": False},
    "LEG":   {"name": "Легенда",          "ticker": None,   "inn": "7842004289", "public": False},
    "SDEV":  {"name": "Страна Девелопмент","ticker": None,  "inn": "7728835560", "public": False},
}

# ============================================================
#  МЕТРИКИ SMART-LAB
# ============================================================

SL_METRICS = {
    "Выручка":            ("revenue",       "млрд_руб"),
    "Операционная прибыль": ("operating_profit", "млрд_руб"),
    "Чистая прибыль":     ("net_profit",    "млрд_руб"),
    "Опер.денежный поток": ("ocf",          "млрд_руб"),
    "Процентные расходы": ("interest_exp",  "млрд_руб"),
    "Активы":             ("assets",        "млрд_руб"),
    "Долг":               ("debt",          "млрд_руб"),
    "Чистый долг":        ("net_debt",      "млрд_руб"),
    "Наличность":         ("cash",          "млрд_руб"),
    "Капитализация":      ("market_cap",    "млрд_руб"),
    "EV":                 ("ev",            "млрд_руб"),
    "Баланс стоимость":   ("book_value",    "млрд_руб"),
    "ROE":                ("roe",           "pct"),
    "ROA":                ("roa",           "pct"),
    "P/E":                ("pe",            "multiple"),
    "P/S":                ("ps",            "multiple"),
    "P/BV":               ("pbv",           "multiple"),
    "Чистая рентаб":      ("net_margin",    "pct"),
    "Контракты на продажу м":  ("contracts_sqm",  "тыс_м2"),
    "Контракты на продажу руб": ("contracts_rub", "млрд_руб"),
    "Доля ипотечных сделок":   ("mortgage_share", "pct"),
    "Средняя цена квадратного метра": ("avg_price_sqm", "тыс_руб_м2"),
    "Персонал":           ("employees",     "чел"),
}


def parse_value(val_str):
    if not val_str or val_str.strip() in ("", "?", "-"):
        return None
    s = val_str.strip()
    if s.endswith("%"):
        try:
            return float(s.replace("%", "").replace(",", ".").replace(" ", ""))
        except ValueError:
            return None
    s = s.replace("\xa0", "").replace(" ", "").replace(",", ".").replace("−", "-")
    try:
        return float(s)
    except ValueError:
        return None


def fetch_page(url, timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


# ============================================================
#  ИСТОЧНИК 1: Smart-Lab (квартальные РСБУ + МСФО)
# ============================================================

def collect_smartlab():
    """Сбор квартальной отчётности с Smart-Lab для всех тикеров"""
    rows = []
    tickers = [k for k, v in COMPANIES.items() if v.get("ticker")]

    for key in tickers:
        info = COMPANIES[key]
        ticker = info["ticker"]
        for std in ["RSBU", "MSFO"]:
            url = f"https://smart-lab.ru/q/{ticker}/f/q/{std}/"
            try:
                html_bytes = fetch_page(url)
                tree = html.fromstring(html_bytes)
                tables = tree.xpath('//table')
                if not tables:
                    continue

                table = tables[0]
                rows_html = table.xpath('.//tr')

                # Периоды
                periods = []
                for r in rows_html[:5]:
                    cells = r.xpath('.//td | .//th')
                    for c in cells:
                        txt = c.text_content().strip()
                        if re.match(r'\d{4}Q[1-4]', txt):
                            periods.append(txt)
                periods = list(dict.fromkeys(periods))  # unique preserve order
                if not periods:
                    continue

                # Даты отчётов
                report_dates = {}
                for r in rows_html:
                    cells = r.xpath('.//td | .//th')
                    vals = [c.text_content().strip() for c in cells]
                    if vals and 'дата отчета' in vals[0].lower():
                        for i, v in enumerate(vals[3:], 3):
                            if v and re.match(r'\d{2}\.\d{2}\.\d{4}', v):
                                idx = i - 3
                                if idx < len(periods):
                                    # Конвертируем DD.MM.YYYY → ISO
                                    dd, mm, yy = v.split(".")
                                    report_dates[periods[idx]] = f"{yy}-{mm}-{dd}"

                # Метрики
                for r in rows_html:
                    cells = r.xpath('.//td | .//th')
                    vals = [c.text_content().strip() for c in cells]
                    if len(vals) < 5 or not vals[0]:
                        continue

                    label = re.sub(r'\s+', ' ', vals[0].split('\n')[0].strip())
                    metric_key = None
                    metric_unit = None
                    for pattern, (mk, mu) in SL_METRICS.items():
                        if label.lower().startswith(pattern.lower()):
                            metric_key = mk
                            metric_unit = mu
                            break
                    if not metric_key:
                        continue

                    for i, v in enumerate(vals[3:], 3):
                        idx = i - 3
                        if idx >= len(periods):
                            break
                        val = parse_value(v)
                        if val is not None:
                            rows.append({
                                "company": info["name"],
                                "ticker": ticker,
                                "inn": info.get("inn"),
                                "standard": std,
                                "period": periods[idx],
                                "metric": metric_key,
                                "value": val,
                                "unit": metric_unit,
                                "source": "smartlab",
                                "source_url": url,
                                "estimate_date": report_dates.get(periods[idx]),
                                "update_date": TODAY,
                                "confidence": "aggregator",
                            })

                print(f"  ✅ {ticker:6s} {std:5s} {len(periods)} periods")
                time.sleep(1.5)
            except Exception as e:
                print(f"  ❌ {ticker:6s} {std:5s} ERROR: {e}")

    return rows


# ============================================================
#  ИСТОЧНИК 2: ФНС bo.nalog (годовая РСБУ) — из существующего JSON
# ============================================================

def collect_fns():
    """Загрузка данных ФНС из ранее собранного summary"""
    rows = []
    fns_file = Path("raw/rsbu/developers_rsbu_summary.json")
    if not fns_file.exists():
        print("  ⚠️ ФНС summary не найден, пропуск")
        return rows

    with open(fns_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # data — список объектов с ключами developer, inn, financials
    for entry in data:
        company_name = entry.get("developer", "")
        inn = entry.get("inn")
        for fin in entry.get("financials", []):
            period = fin.get("period")
            balance = fin.get("balance") or {}
            finresult = fin.get("financialResult") or {}
            metrics = {
                "revenue": (finresult.get("revenue"), "млрд_руб"),
                "net_profit": (finresult.get("net_profit"), "млрд_руб"),
                "total_assets": (balance.get("total_assets"), "млрд_руб"),
                "equity": (balance.get("equity"), "млрд_руб"),
                "long_term_debt": (balance.get("long_term_debt"), "млрд_руб"),
                "short_term_debt": (balance.get("short_term_debt"), "млрд_руб"),
                "total_debt": (balance.get("total_debt"), "млрд_руб"),
            }
            for metric, (value, unit) in metrics.items():
                if value is not None and isinstance(value, (int, float)):
                    # Конвертируем тыс. руб. → млрд руб.
                    value_mlr = value / 1e6
                    rows.append({
                        "company": company_name,
                        "ticker": None,
                        "inn": inn,
                        "standard": "RSBU",
                        "period": period,
                        "metric": metric,
                        "value": round(value_mlr, 3),
                        "unit": "млрд_руб",
                        "source": "fns_bonalog",
                        "source_url": "https://bo.nalog.gov.ru",
                        "estimate_date": None,
                        "update_date": TODAY,
                        "confidence": "primary",
                    })

    print(f"  ✅ ФНС: {len(rows)} записей")
    return rows


# ============================================================
#  ИСТОЧНИК 3: Аналитические обзоры (вручную кодированные)
# ============================================================

def collect_analyst_estimates():
    """Жёстко кодированные оценки из аналитических обзоров Freedom FG, atsogoev, НКР"""
    rows = []

    # === Freedom Finance Global (01.09.2026) — МСФО 6М26 ===
    freedom_data = [
        # company, metric, value, unit, source_url
        ("ПИК",      "revenue",      290.0,  "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("ПИК",      "revenue_yoy",  -12.0,  "pct",      "https://smart-lab.ru/blog/1346801.php"),
        ("ПИК",      "ebitda_adj",   29.9,   "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("ПИК",      "ebitda_yoy",   -10.0,  "pct",      "https://smart-lab.ru/blog/1346801.php"),
        ("ПИК",      "net_profit",   14.7,   "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("ПИК",      "net_profit_yoy", -54.0, "pct",     "https://smart-lab.ru/blog/1346801.php"),
        ("ПИК",      "net_debt_ebitda", 0.9, "multiple", "https://smart-lab.ru/blog/1346801.php"),
        ("Самолёт",  "revenue",      117.5,  "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("Самолёт",  "revenue_yoy",  -31.0,  "pct",      "https://smart-lab.ru/blog/1346801.php"),
        ("Самолёт",  "ebitda_adj",   41.8,   "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("Самолёт",  "ebitda_yoy",   -27.0,  "pct",      "https://smart-lab.ru/blog/1346801.php"),
        ("Самолёт",  "net_profit",   -22.3,  "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("Самолёт",  "net_debt_ebitda", 0.9, "multiple", "https://smart-lab.ru/blog/1346801.php"),
        ("ЛСР",      "revenue",      97.0,   "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("ЛСР",      "revenue_yoy",   0.7,   "pct",      "https://smart-lab.ru/blog/1346801.php"),
        ("ЛСР",      "net_profit",   -57.6,  "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("ЛСР",      "net_debt_ebitda", 2.8, "multiple", "https://smart-lab.ru/blog/1346801.php"),
        ("Глоракс",  "revenue",      27.0,   "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("Глоракс",  "revenue_yoy",  45.0,   "pct",      "https://smart-lab.ru/blog/1346801.php"),
        ("Глоракс",  "ebitda",       8.6,    "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("Глоракс",  "ebitda_yoy",   36.0,   "pct",      "https://smart-lab.ru/blog/1346801.php"),
        ("Глоракс",  "net_profit",    1.6,   "млрд_руб", "https://smart-lab.ru/blog/1346801.php"),
        ("Глоракс",  "net_debt_ebitda", 2.9, "multiple", "https://smart-lab.ru/blog/1346801.php"),
    ]
    for company, metric, value, unit, url in freedom_data:
        rows.append({
            "company": company, "ticker": None, "inn": None,
            "standard": "MSFO", "period": "2026Q2",
            "metric": metric, "value": value, "unit": unit,
            "source": "freedom_fg", "source_url": url,
            "estimate_date": "2026-09-01",
            "update_date": TODAY,
            "confidence": "analyst",
        })

    # === atsogoev (03.09.2026) — дополнительные метрики ===
    atsogoev_data = [
        ("ПИК",     "cash",          353.0,  "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("ПИК",     "escrow",        544.0,  "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("ПИК",     "total_debt",    875.0,  "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("ПИК",     "escrow_intake_yoy", -39.0, "pct",  "https://smart-lab.ru/blog/1347638.php"),
        ("Глоракс", "interest_paid",  7.8,   "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("Глоракс", "cash",           0.685, "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("ЛСР",     "impairment",    46.8,   "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("ЛСР",     "cash",           5.4,   "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("ЛСР",     "short_term_debt", 57.0, "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("АПРИ",    "revenue",       12.0,   "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("АПРИ",    "revenue_yoy",   30.0,   "pct",      "https://smart-lab.ru/blog/1347638.php"),
        ("АПРИ",    "net_profit",     0.121, "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("АПРИ",    "ebitda_margin", 40.0,   "pct",      "https://smart-lab.ru/blog/1347638.php"),
        ("АПРИ",    "interest_paid",  4.3,   "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("АПРИ",    "ocf",           -8.4,   "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("АПРИ",    "debt",          55.2,   "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("Эталон",  "revenue_restated_1h25", 60.2, "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
        ("Эталон",  "loss_restated_1h25",   -14.1, "млрд_руб", "https://smart-lab.ru/blog/1347638.php"),
    ]
    for company, metric, value, unit, url in atsogoev_data:
        rows.append({
            "company": company, "ticker": None, "inn": None,
            "standard": "MSFO", "period": "2026Q2",
            "metric": metric, "value": value, "unit": unit,
            "source": "atsogoev", "source_url": url,
            "estimate_date": "2026-09-03",
            "update_date": TODAY,
            "confidence": "analyst",
        })

    # === Эталон IFRS PDF (первоисточник, 27.08.2026) ===
    etalon_pdf_data = [
        ("Эталон", "revenue",        54.443, "млрд_руб"),
        ("Эталон", "net_profit",    -13.170, "млрд_руб"),
        ("Эталон", "ebitda_ltm",     25.327, "млрд_руб"),
        ("Эталон", "net_debt_adj",  140.356, "млрд_руб"),
        ("Эталон", "net_corp_debt",  72.749, "млрд_руб"),
        ("Эталон", "net_debt_ebitda",  5.5,  "multiple"),
        ("Эталон", "net_corp_debt_ebitda", 2.87, "multiple"),
        ("Эталон", "gross_debt",    196.252, "млрд_руб"),
        ("Эталон", "long_term_debt", 167.440, "млрд_руб"),
        ("Эталон", "short_term_debt", 28.812, "млрд_руб"),
        ("Эталон", "escrow",         48.545, "млрд_руб"),
        ("Эталон", "interest_exp",   20.574, "млрд_руб"),
        ("Эталон", "assets",        327.408, "млрд_руб"),
        ("Эталон", "equity",         28.869, "млрд_руб"),
        ("Эталон", "avg_interest_rate", 14.57, "pct"),
    ]
    for company, metric, value, unit in etalon_pdf_data:
        rows.append({
            "company": company, "ticker": "ETLN", "inn": "7826009627",
            "standard": "MSFO", "period": "2026Q2",
            "metric": metric, "value": value, "unit": unit,
            "source": "ir_pdf", "source_url": "https://www.etalongroup.com/investors/reports/",
            "estimate_date": "2026-08-27",
            "update_date": TODAY,
            "confidence": "primary",
        })

    # === НКР (09.07.2026) — агрегаты 11 застройщиков ===
    nkr_data = [
        ("11_застройщиков", "revenue_total", 2200.0, "млрд_руб", 15.0, "pct"),
        ("11_застройщиков", "debt_total",    3100.0, "млрд_руб", 30.0, "pct"),
        ("11_застройщиков", "escrow_coverage", 69.6, "pct",      None, None),
    ]
    for company, metric, value, unit, yoy, yoy_unit in nkr_data:
        rows.append({
            "company": company, "ticker": None, "inn": None,
            "standard": "MSFO", "period": "2025",
            "metric": metric, "value": value, "unit": unit,
            "source": "nkr", "source_url": "https://realty.ria.ru/20260709/nkr-2103898042.html",
            "estimate_date": "2026-07-09",
            "update_date": TODAY,
            "confidence": "rating",
        })
        if yoy is not None:
            rows.append({
                "company": company, "ticker": None, "inn": None,
                "standard": "MSFO", "period": "2025",
                "metric": f"{metric}_yoy", "value": yoy, "unit": yoy_unit,
                "source": "nkr", "source_url": "https://realty.ria.ru/20260709/nkr-2103898042.html",
                "estimate_date": "2026-07-09",
                "update_date": TODAY,
                "confidence": "rating",
            })

    # === CorpBonds (из сниппетов) ===
    corpbonds_data = [
        ("Самолёт",            "revenue_2025",  309.0, "млрд_руб", "https://corpbonds.ru/issuer_review/440", "2026"),
        ("Самолёт",            "ebitda_2025",    99.0, "млрд_руб", "https://corpbonds.ru/issuer_review/440", "2026"),
        ("ЛСР",                "revenue_1h25",   88.710, "млрд_руб", "https://corpbonds.ru/issuer_review/364", "2025"),
        ("ЛСР",                "ebitda_1h25",    14.306, "млрд_руб", "https://corpbonds.ru/issuer_review/364", "2025"),
        ("Легенда",            "revenue_2025",   26.478, "млрд_руб", "https://corpbonds.ru/issuer_review/457", "2026"),
        ("Легенда",            "ebitda_2025",     4.243, "млрд_руб", "https://corpbonds.ru/issuer_review/457", "2026"),
        ("Страна Девелопмент", "revenue_1h25",   27.548, "млрд_руб", "https://corpbonds.ru/issuer_review/407", "2025"),
        ("Страна Девелопмент", "ebitda_1h25",     6.954, "млрд_руб", "https://corpbonds.ru/issuer_review/407", "2025"),
    ]
    for company, metric, value, unit, url, year in corpbonds_data:
        rows.append({
            "company": company, "ticker": None, "inn": None,
            "standard": "MSFO", "period": year,
            "metric": metric, "value": value, "unit": unit,
            "source": "corpbonds", "source_url": url,
            "estimate_date": "2026-03-01",
            "update_date": TODAY,
            "confidence": "analyst",
        })

    print(f"  ✅ Аналитики: {len(rows)} записей")
    return rows


# ============================================================
#  ГЛАВНАЯ ФУНКЦИЯ
# ============================================================

def main():
    print("=" * 60)
    print("  ЕДИНАЯ ПАНЕЛЬ ФИНАНСОВЫХ ОЦЕНОК ДЕВЕЛОПЕРОВ")
    print("=" * 60)

    all_rows = []

    print("\n📡 Источник 1: Smart-Lab (квартальные РСБУ+МСФО)")
    all_rows.extend(collect_smartlab())

    print("\n📡 Источник 2: ФНС bo.nalog (годовая РСБУ)")
    all_rows.extend(collect_fns())

    print("\n📡 Источник 3: Аналитические обзоры + IR + рейтинги")
    all_rows.extend(collect_analyst_estimates())

    # Сохраняем
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    # Полная панель
    panel_file = output_dir / "developer_panel.json"
    with open(panel_file, "w", encoding="utf-8") as f:
        json.dump(all_rows, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Полная панель: {panel_file} ({len(all_rows)} записей)")

    # CSV для удобства
    import csv
    csv_file = output_dir / "developer_panel.csv"
    with open(csv_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "company", "ticker", "inn", "standard", "period",
            "metric", "value", "unit",
            "source", "source_url", "estimate_date", "update_date", "confidence"
        ])
        writer.writeheader()
        for row in all_rows:
            writer.writerow(row)
    print(f"💾 CSV: {csv_file}")

    # Сводка по источникам
    from collections import Counter
    by_source = Counter(r["source"] for r in all_rows)
    by_company = Counter(r["company"] for r in all_rows)
    by_std = Counter(r["standard"] for r in all_rows)
    by_conf = Counter(r["confidence"] for r in all_rows)

    print(f"\n{'='*60}")
    print(f"  СВОДКА")
    print(f"{'='*60}")
    print(f"Всего записей: {len(all_rows)}")
    print(f"\nПо источникам:")
    for s, c in by_source.most_common():
        print(f"  {s:20s} {c:5d}")
    print(f"\nПо компаниям:")
    for s, c in by_company.most_common():
        print(f"  {s:25s} {c:5d}")
    print(f"\nПо стандартам:")
    for s, c in by_std.most_common():
        print(f"  {s:8s} {c:5d}")
    print(f"\nПо типу источника:")
    for s, c in by_conf.most_common():
        print(f"  {s:12s} {c:5d}")


if __name__ == "__main__":
    main()