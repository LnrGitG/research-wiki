#!/usr/bin/env python3
"""Сбор данных datamarts.roskazna.ru (Федеральное казначейство) — кассовое исполнение ФБ.

datamarts.roskazna.ru недоступен с VPS (SSL handshake failure) — вероятно требует
российского TLS-сертификата. Запуск через ВМ YC (hermes peer run yc).

Альтернатива: roskazna.gov.ru (доступен с VPS) — но это HTML-сайт, не API.
"""
import urllib.request, ssl, json, sys, os, hashlib
sys.path.insert(0, os.path.expanduser("~/research-wiki-private/scripts"))
from db_tunnel import query, execute

SOURCE_ID = 33  # roskazna

def main():
    # Создать метрики
    metrics = {}
    for code, name, unit_id in [
        ("roskazna_fb_execution_0501_m", "Кассовое исполнение ФБ по разделу 0501 (жилищное хоз-во), млн руб.", 11),
        ("roskazna_fb_execution_0502_m", "Кассовое исполнение ФБ по разделу 0502 (коммунальное хоз-во), млн руб.", 11),
        ("roskazna_fb_execution_total_m", "Кассовое исполнение ФБ (итого), млн руб.", 11),
    ]:
        r = query(f"SELECT metric_id FROM catalog.metric WHERE metric_code='{code}'")
        if r:
            metrics[code] = r[0][0]
            print(f"{code}: metric_id={r[0][0]}")
        else:
            print(f"{code}: NOT FOUND — creating")
            execute(f"""INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id, frequency_id, status, is_active)
                VALUES ('{code}', '{name}', {unit_id}, {SOURCE_ID}, 5, 'active', true)
                ON CONFLICT (metric_code) DO NOTHING""")
            r = query(f"SELECT metric_id FROM catalog.metric WHERE metric_code='{code}'")
            metrics[code] = r[0][0]
            print(f"  created: metric_id={r[0][0]}")

    # Попытка доступа к datamarts.roskazna.ru
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    urls_to_try = [
        "https://datamarts.roskazna.ru",
        "https://datamarts.roskazna.ru/api/v1/data",
        "https://roskazna.gov.ru/api/data",
        "https://roskazna.gov.ru/execution/",
    ]

    accessible = False
    for url in urls_to_try:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            resp = urllib.request.urlopen(req, context=ctx, timeout=10)
            data = resp.read()
            print(f"OK {url}: {len(data)} bytes")
            accessible = True
        except Exception as e:
            print(f"FAIL {url}: {type(e).__name__}: {e}")

    if not accessible:
        print("\n⚠️  datamarts.roskazna.ru недоступен с этого хоста.")
        print("Скрипт подготовлен. Для сбора данных:")
        print("1. Запустить через ВМ YC: hermes peer run yc --idempotency-key roskazna-1")
        print("2. Или вручную скачать отчёты с datamarts.roskazna.ru")
        print("3. Или использовать roskazna.gov.ru (HTML-скрапинг)")
        print("\nМетрики созданы в каталоге, но наблюдения не загружены.")
        return

    # ⚠️ БЛОКЕР: datamarts.roskazna.ru — WordPress + Krista BI-дашборд.
    # Отчёты рендерятся в браузере через JS (bi-dashboard-3.13.2.min.js).
    # API-эндпоинты (/data/queryRequest, /reporting/request) проксируются через
    # redirect/localhost/ и требуют JS-контекст (WebReports.Hosts.CmsHost).
    # Простой HTTP-скрапинг невозможен — нужен headless-браузер (Playwright/Selenium).
    #
    # UUID отчёта расходов по разделам: 904ee4e6-a701-44e9-a74b-b9537b6be6cb
    # Страница: /razdely/rashody/rashody-po-razdelam-podrazdelam/rashody-po-razdelam-i-podrazdelam/
    # Параметры: paramPeriod (дата), разделы 0501/0502
    #
    # Альтернативные пути:
    # 1. Headless-браузер на ВМ YC (Playwright + Chromium)
    # 2. Ручная выгрузка XLSX через web-интерфейс datamarts.roskazna.ru
    # 3. minfin.gov.ru — отчёты об исполнении ФБ (HTML/PDF)
    # 4. ЕИС «Бюджет» — API через fedstat.ru (если доступен)
    print("\n⚠️  datamarts.roskazna.ru требует JS-рендеринга (Krista BI).")
    print("Метрики созданы в каталоге, но наблюдения не загружены.")
    print("Альтернативы: headless-браузер (Playwright) или ручная выгрузка XLSX.")


if __name__ == "__main__":
    main()