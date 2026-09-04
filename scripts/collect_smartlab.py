#!/usr/bin/env python3
"""
Парсер Smart-Lab.ru — квартальная финансовая отчётность девелоперов (РСБУ + МСФО)

URL: smart-lab.ru/q/{TICKER}/f/q/{RSBU|MSFO}/
Возвращает: JSON с метриками по кварталам

Метрики:
- Выручка, Операционная прибыль, Чистая прибыль
- Активы, Долг, Чистый долг, Наличность
- OCF, Процентные расходы
- ROE, ROA, P/E, P/BV, Капитализация
- Контракты на продажу (м2, руб), Доля ипотеки, Средняя цена м2
"""

import json
import urllib.request
import time
import re
from pathlib import Path
from lxml import html

BASE = "https://smart-lab.ru"

# Тикеры публичных девелоперов на Мосбирже
TICKERS = {
    "PIKK": {"name": "ПИК", "inn": "7713011336"},
    "SMLT": {"name": "Самолёт", "inn": "9731004688"},
    "ETLN": {"name": "Эталон", "inn": "7826009627"},
    "LSRG": {"name": "ЛСР", "inn": "7805027146"},
}

# Метрики для извлечения (имя в таблице → ключ в JSON)
METRIC_MAP = {
    "Выручка": "revenue",
    "Операционная прибыль": "operating_profit",
    "Чистая прибыль": "net_profit",
    "Опер.денежный поток": "ocf",
    "Процентные расходы": "interest_expenses",
    "Активы": "assets",
    "Чистые активы": "net_assets",
    "Долг": "debt",
    "Наличность": "cash",
    "Чистый долг": "net_debt",
    "Капитализация": "market_cap",
    "EV": "ev",
    "Баланс стоимость": "book_value",
    "EPS": "eps",
    "ROE": "roe",
    "ROA": "roa",
    "P/E": "pe",
    "P/S": "ps",
    "P/BV": "pbv",
    "Чистая рентаб": "net_margin",
    "Рентаб EBITDA": "ebitda_margin",
    "Контракты на продажу м": "contracts_sqm",
    "Контракты на продажу руб": "contracts_rub",
    "Доля ипотечных сделок": "mortgage_share",
    "Средняя цена квадратного метра": "avg_price_sqm",
    "Персонал": "employees",
    "Себестоимость": "cogs",
    "Опер. расходы": "opex",
    "Расх на персонал": "staff_expenses",
    "Цена акции ао": "share_price",
    "Число акций ао": "shares_outstanding",
    "Free Float": "free_float",
    "Див доход, ао": "div_yield",
}

# Единицы измерения (для нормализации)
UNIT_MULTIPLIERS = {
    "млрд руб": 1e9,
    "млн руб": 1e6,
    "тыс.руб": 1e3,
    "млрд": 1e9,
    "млн": 1e6,
}


def parse_value(val_str):
    """Парсинг числового значения из строки таблицы"""
    if not val_str or val_str.strip() in ("", "?", "-"):
        return None

    s = val_str.strip()

    # Проценты
    if s.endswith("%"):
        try:
            return float(s.replace("%", "").replace(",", ".").replace(" ", ""))
        except ValueError:
            return None

    # Удаляем пробелы-разделители (1 222 → 1222)
    s = s.replace("\xa0", "").replace(" ", "")
    s = s.replace(",", ".")

    # Отрицательные числа
    s = s.replace("−", "-")

    try:
        return float(s)
    except ValueError:
        return None


def fetch_page(url):
    """Скачивание HTML страницы"""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "text/html,application/xhtml+xml"
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read()


def parse_table(html_bytes, ticker, standard):
    """Парсинг таблицы финансовой отчётности со Smart-Lab"""
    tree = html.fromstring(html_bytes)
    tables = tree.xpath('//table')
    if not tables:
        return None

    table = tables[0]
    rows = table.xpath('.//tr')

    # 1. Извлекаем периоды из заголовка
    periods = []
    for r in rows[:5]:
        cells = r.xpath('.//td | .//th')
        for c in cells:
            txt = c.text_content().strip()
            # Паттерн: 2025Q2, 2026Q1, etc.
            if re.match(r'\d{4}Q[1-4]', txt):
                periods.append(txt)

    if not periods:
        return None

    # Периоды могут дублироваться — берём уникальные
    seen = set()
    unique_periods = []
    for p in periods:
        if p not in seen:
            seen.add(p)
            unique_periods.append(p)
    periods = unique_periods

    # 2. Извлекаем даты отчёта
    report_dates = {}
    for r in rows:
        cells = r.xpath('.//td | .//th')
        vals = [c.text_content().strip() for c in cells]
        if vals and 'дата отчета' in vals[0].lower():
            # Значения начинаются с индекса 3 (после name, ?, пустой)
            for i, v in enumerate(vals[3:], 3):
                if v and re.match(r'\d{2}\.\d{2}\.\d{4}', v):
                    period_idx = i - 3
                    if period_idx < len(periods):
                        report_dates[periods[period_idx]] = v

    # 3. Извлекаем метрики
    data = {p: {} for p in periods}
    metric_data = {}

    for r in rows:
        cells = r.xpath('.//td | .//th')
        vals = [c.text_content().strip() for c in cells]
        if len(vals) < 4 or not vals[0]:
            continue

        metric_label = vals[0].split('\n')[0].strip()
        # Очищаем от всплывающих подсказок
        metric_label = re.sub(r'\s+', ' ', metric_label)

        # Ищем точное совпадение в METRIC_MAP
        metric_key = None
        for pattern, key in METRIC_MAP.items():
            # Точное совпадение начала строки (избегаем "Долг" → "Чистый долг")
            if metric_label.lower().startswith(pattern.lower()):
                metric_key = key
                break

        if not metric_key:
            continue

        # Значения по периодам (начинаются с индекса 3)
        for i, v in enumerate(vals[3:], 3):
            period_idx = i - 3
            if period_idx < len(periods):
                val = parse_value(v)
                if val is not None:
                    data[periods[period_idx]][metric_key] = val

    # 4. Формируем результат
    result = {
        "ticker": ticker,
        "standard": standard,
        "company": TICKERS.get(ticker, {}).get("name", ticker),
        "periods": periods,
        "report_dates": report_dates,
        "data": data,
    }

    return result


def collect_ticker(ticker, output_dir):
    """Сбор данных для одного тикера (РСБУ + МСФО)"""
    print(f"\n{'='*50}")
    print(f"  {ticker} ({TICKERS[ticker]['name']})")
    print(f"{'='*50}")

    results = {}

    for standard in ["RSBU", "MSFO"]:
        url = f"{BASE}/q/{ticker}/f/q/{standard}/"
        print(f"  Fetching: {url}")

        try:
            html_bytes = fetch_page(url)
            result = parse_table(html_bytes, ticker, standard)

            if result:
                print(f"  {standard}: {len(result['periods'])} periods")
                for p in result["periods"]:
                    d = result["data"].get(p, {})
                    rev = d.get("revenue")
                    net = d.get("net_profit")
                    debt = d.get("debt")
                    print(f"    {p}: rev={rev}, net={net}, debt={debt}")

                results[standard] = result

                # Сохраняем
                outfile = output_dir / f"{ticker.lower()}_{standard.lower()}.json"
                with open(outfile, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)
                print(f"  Saved: {outfile}")
            else:
                print(f"  {standard}: NO DATA")

        except Exception as e:
            print(f"  {standard}: ERROR {e}")

        time.sleep(2)  # Rate limit

    return results


def main():
    output_dir = Path("raw/smartlab")
    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = {}
    for ticker in TICKERS:
        try:
            results = collect_ticker(ticker, output_dir)
            all_results[ticker] = results
        except Exception as e:
            print(f"  FATAL: {e}")
        time.sleep(1)

    # Сводный файл
    summary = {}
    for ticker, standards in all_results.items():
        for std, data in standards.items():
            if data and data.get("data"):
                for period, metrics in data["data"].items():
                    key = f"{ticker}_{std}_{period}"
                    summary[key] = {
                        "ticker": ticker,
                        "company": TICKERS[ticker]["name"],
                        "standard": std,
                        "period": period,
                        "report_date": data.get("report_dates", {}).get(period),
                        **metrics,
                    }

    outfile = output_dir / "developers_quarterly_summary.json"
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n\nSummary: {outfile}")
    print(f"Total records: {len(summary)}")

    # Печать сводки
    print(f"\n{'Ticker':<6} {'Std':<5} {'Period':<8} {'Revenue':>10} {'Net Profit':>12} {'Debt':>10} {'D/E':>8}")
    print("-" * 65)
    for key, v in sorted(summary.items()):
        rev = v.get("revenue")
        net = v.get("net_profit")
        debt = v.get("debt")
        equity = v.get("book_value")
        de = (debt / equity) if debt and equity and equity != 0 else None
        print(f"{v['ticker']:<6} {v['standard']:<5} {v['period']:<8} {rev or 0:>10.2f} {net or 0:>12.2f} {debt or 0:>10.1f} {de or 0:>8.2f}")


if __name__ == "__main__":
    main()