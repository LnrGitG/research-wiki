#!/usr/bin/env python3
"""Дашборд «Семантический слой»: карточки — готовые метрики, без SQL в карточках.

Идемпотентно: дашборд ищется по имени в целевой коллекции, карточки-метрики
переиспользуются по имени; повторный прогон не плодит дубли.

Запуск: python3 scripts/metabase_semantic_dashboard.py
"""
import json
import os
import sys

import requests

BASE = os.environ.get("MB_URL", "http://127.0.0.1:13000")
ENV = os.path.expanduser("~/.hermes/.env")
COLLECTION_ID = 7
DASH_NAME = "Семантический слой: индикаторы жилья и ипотеки"

LAYOUT = [  # (имя метрики, колонка, row, size_x, size_y)
    ("СМР: ИФО объёма работ, % г/г (медиана)", 0, 0, 12, 6),
    ("СМР: объём работ накопит., млн руб.", 12, 0, 12, 6),
    ("Ввод жилых зданий, тыс. м²", 0, 6, 12, 6),
    ("Ввод нежилых зданий, тыс. м²", 12, 6, 12, 6),
    ("Ставка ИЖК, % годовых", 0, 12, 12, 6),
    ("Выдачи ИЖК, млн руб. за месяц", 12, 12, 12, 6),
    ("Задолженность по ИЖК, млн руб.", 0, 18, 12, 6),
    ("Реализация квартир, м²", 12, 18, 12, 6),
    ("Строящееся жильё на эскроу, м²", 0, 24, 12, 6),
    ("Площадь по действующим ДДУ, м²", 12, 24, 12, 6),
    ("Цена действующих ДДУ, млн руб.", 0, 30, 12, 6),
    ("ИПЦ, % к предыдущему месяцу", 12, 30, 12, 6),
    ("Уровень безработицы (МОТ), %", 0, 36, 12, 6),
    ("Ставка ИЖК по регионам, % (ср. за 3 мес.)", 0, 42, 24, 7),
    ("Выдачи ИЖК по регионам, млн руб. (за 3 мес.)", 0, 49, 24, 7),
    ("Задолженность по ИЖК по регионам, млн руб. (ср. за 3 мес.)", 0, 56, 24, 7),
    ("Реализация квартир по регионам, м² (за 3 мес.)", 0, 63, 24, 7),
]


class Api:
    def __init__(self):
        key = [l.split("=", 1)[1].strip() for l in open(ENV)
               if l.startswith("METABASE_API_KEY=")][0]
        self.s = requests.Session()
        self.s.headers.update({"x-api-key": key, "Content-Type": "application/json"})

    def req(self, method, path, payload=None):
        r = self.s.request(method, BASE + path, timeout=120,
                           data=json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None)
        if r.status_code >= 400:
            raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text[:200]}")
        return r.json() if r.text.strip() else None


def main() -> int:
    api = Api()
    items = api.req("GET", f"/api/collection/{COLLECTION_ID}/items?models=metric&limit=200")["data"]
    metric_ids = {i["name"]: i["id"] for i in items}
    missing = [n for n, *_ in LAYOUT if n not in metric_ids]
    if missing:
        print("нет метрик:", missing)
        return 1

    dashes = api.req("GET", f"/api/collection/{COLLECTION_ID}/items?models=dashboard&limit=200")["data"]
    dash = next((d for d in dashes if d["name"] == DASH_NAME), None)
    if dash:
        dash_id = dash["id"]
        api.req("PUT", f"/api/dashboard/{dash_id}", {"name": DASH_NAME,
                "description": "Витрина семантического слоя: каждая карточка — сохранённая метрика "
                               "с фильтрами и единым определением, SQL в карточках нет.",
                "collection_id": COLLECTION_ID})
        print(f"дашборд существует: id={dash_id}")
    else:
        dash = api.req("POST", "/api/dashboard", {"name": DASH_NAME, "collection_id": COLLECTION_ID,
                      "description": "Витрина семантического слоя: каждая карточка — сохранённая "
                                     "метрика с фильтрами и единым определением, SQL в карточках нет."})
        dash_id = dash["id"]
        print(f"дашборд создан: id={dash_id}")

    current = api.req("GET", f"/api/dashboard/{dash_id}")
    by_card = {dc.get("card_id"): dc for dc in current.get("dashcards", []) if dc.get("card_id")}

    dashcards, created, updated = [], 0, 0
    for idx, (name, col, row, sx, sy) in enumerate(LAYOUT):
        card_id = metric_ids[name]
        existing = by_card.get(card_id)
        if existing:
            dc_id = existing["id"]
            updated += 1
        else:
            dc_id = -(idx + 1)
            created += 1
        dashcards.append({"id": dc_id, "card_id": card_id, "row": row, "col": col,
                          "size_x": sx, "size_y": sy, "parameter_mappings": [],
                          "visualization_settings": {}})

    # карточки, которых больше нет в раскладке, уходят с дашборда
    keep = {metric_ids[n] for n, *_ in LAYOUT}
    for card_id, dc in by_card.items():
        if card_id not in keep:
            dashcards.append({"id": dc["id"], "card_id": None})

    api.req("PUT", f"/api/dashboard/{dash_id}", {"dashcards": dashcards})

    final = api.req("GET", f"/api/dashboard/{dash_id}")
    cards = [dc for dc in final.get("dashcards", []) if dc.get("card_id")]
    print(f"карточек-метрик на дашборде: {len(cards)} (создано {created}, обновлено {updated})")
    for dc in cards[:3]:
        print("  пример:", dc["card"]["name"], "| display:", dc["card"].get("display"))
    print(f"\nдашборд: {BASE}/dashboard/{dash_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
