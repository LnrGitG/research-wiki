#!/usr/bin/env python3
"""Семантический слой Metabase: метрики и сегменты через штатный REST API.

Почему метрики, а не меры: в build 0.64 определение меры (measure) не принимает
фильтры — они молча отбрасываются, и мера над широкой витриной считает среднее
по всем индикаторам сразу. Метрика (card.type = "metric") — отдельный объект:
полный одностадийный запрос с фильтрами, ровно одна агрегация и максимум одна
группировка. Она и есть единица семантического слоя.

Скрипт идемпотентен: находит метрику по имени в целевой коллекции и обновляет
её, а не создаёт дубль.

Запуск:
  python3 scripts/metabase_semantic_mcp.py --verify   # только проверить запросы
  python3 scripts/metabase_semantic_mcp.py --dry-run  # проверить, ничего не писать
  python3 scripts/metabase_semantic_mcp.py            # создать/обновить
Требует METABASE_API_KEY в ~/.hermes/.env; с VPS Metabase доступен по
тоннелю (127.0.0.1:13000), с ноутбука — напрямую (localhost:3000).
"""
import argparse
import json
import os
import sys

import requests

BASE = os.environ.get("MB_URL", "http://127.0.0.1:13000")
ENV = os.path.expanduser("~/.hermes/.env")
DB_ID = 2
TABLE_ID = 348          # derived.v_bi_observation
F_CODE, F_PERIOD, F_REGION, F_LEVEL, F_VALUE, F_SUB = 5280, 5285, 5290, 5292, 5300, 5302

COLLECTION_ID = 7        # Жильё, стройка и ипотека (research)
CANON_SOLD = "охват: регионы | статус: Всего"


def _f(fid, opts=None):
    return ["field", opts or {}, fid]


def _eq(fid, value):
    return ["=", {}, _f(fid), value]


def _neq(fid, value):
    return ["!=", {}, _f(fid), value]


def metric_query(agg, code, level, sub=None, exclude=(), breakout=None, window=None):
    """Одностадийный MBQL-запрос метрики: фильтры + одна агрегация + одна группировка."""
    filters = [_eq(F_CODE, code)]
    if level:
        filters.append(_eq(F_LEVEL, level))
    if sub:
        filters.append(_eq(F_SUB, sub))
    for ex in exclude:
        filters.append(_neq(F_REGION, ex))
    if window:
        filters.append(["between", {}, _f(F_PERIOD),
                        ["relative-datetime", -window, "month"],
                        ["relative-datetime", 0, "month"]])
    stage = {
        "lib/type": "mbql.stage/mbql",
        "source-table": TABLE_ID,
        "filters": filters,
        "aggregation": [[agg, {}, _f(F_VALUE)]],
    }
    if breakout in ("month", "quarter"):
        stage["breakout"] = [_f(F_PERIOD, {"temporal-unit": breakout})]
        stage["order-by"] = [["asc", {}, _f(F_PERIOD, {"temporal-unit": breakout})]]
    elif breakout == "region":
        stage["breakout"] = [_f(F_REGION)]
        stage["order-by"] = [["asc", {}, _f(F_REGION)]]
    return {"lib/type": "mbql/query", "database": DB_ID, "stages": [stage]}


# name, display, agg, code, level, sub, exclude, breakout, описание
METRICS = [
    ("СМР: ИФО объёма работ, % г/г (медиана)", "line", "median", "orvdssmpg", "region", None,
     ("ingushetia",), "month",
     "Медиана по субъектам: среднее ломается выбросами (Ингушетия 53 336 % в январе 2026, "
     "среднее по регионам доходило до 714 %), медиана устойчива. Источник: оперативная статистика Росстата."),
    ("СМР: объём работ накопит., млн руб.", "line", "sum", "orvdsningmr", "region", None,
     (), "month",
     "Сумма по субъектам, накопительно с начала года. Накопительный ряд: суммировать "
     "по месяцам нельзя, сравнивать только одноимённые месяцы."),
    ("Ввод жилых зданий, тыс. м²", "line", "sum", "vzszopmrvzs", "country", None,
     (), "month", "Общая площадь введённых жилых зданий за месяц (Росстат)."),
    ("Ввод нежилых зданий, тыс. м²", "line", "sum", "vzsnopmrvzs", "country", None,
     (), "month", "Общая площадь введённых нежилых зданий за месяц (Росстат)."),
    ("Ставка ИЖК, % годовых", "line", "avg", "cbr_izhk_rate_m", "country", None,
     (), "month", "Средневзвешенная ставка по ипотечным кредитам в рублях (ЦБ РФ)."),
    ("Выдачи ИЖК, млн руб. за месяц", "line", "sum", "cbr_izhk_volume_m", "country", None,
     (), "month", "Объём предоставленных ипотечных кредитов за месяц — поток."),
    ("Задолженность по ИЖК, млн руб.", "line", "sum", "cbr_izhk_debt_m", "country", None,
     (), "month", "Портфель ипотечных кредитов на начало месяца — запас, по месяцам не суммировать."),
    ("Реализация квартир, м²", "line", "sum", "rkop_3", "country", CANON_SOLD,
     (), "month",
     "Канонический срез «охват: регионы | статус: Всего»; в ЕИСЖС на регион-месяц "
     "до 432 подразрезов, без фильтра сумма завышается в десятки раз."),
    ("Строящееся жильё на эскроу, м²", "line", "sum", "01_01_06", "country", None,
     (), "month", "Запас: площадь МКД, строящихся с привлечением средств граждан (ЕИСЖС)."),
    ("Площадь по действующим ДДУ, м²", "line", "sum", "01_03_05", "country", None,
     (), "month", "Запас на дату по действующим договорам долевого участия (ЕИСЖС)."),
    ("Цена действующих ДДУ, млн руб.", "line", "sum", "01_03_06", "country", None,
     (), "month", "Денежный эквивалент проданного портфеля ДДУ (ЕИСЖС), запас на дату."),
    ("ИПЦ, % к предыдущему месяцу", "line", "avg", "emiss_31074_cpi_prevm_m", "country", None,
     (), "month", "Индекс потребительских цен, месячная динамика (Росстат/ЕМИСС)."),
    ("Уровень безработицы (МОТ), %", "line", "avg", "emiss_43062_unemp_q", "country", None,
     (), "quarter", "Квартальный уровень безработицы по методологии МОТ (Росстат/ЕМИСС)."),
    # региональные срезы: группировка по региону, окно 3 месяца
    ("Ставка ИЖК по регионам, % (ср. за 3 мес.)", "bar", "avg", "cbr_izhk_rate_m", "region", None,
     (), "region", "Средняя ставка ИЖК по субъектам за последние 3 месяца данных: "
                   "сглаживает отставание отдельных региональных рядов."),
    ("Выдачи ИЖК по регионам, млн руб. (за 3 мес.)", "bar", "sum", "cbr_izhk_volume_m", "region", None,
     (), "region", "Сумма выдач ИЖК по субъектам за последние 3 месяца — поток."),
    ("Задолженность по ИЖК по регионам, млн руб. (ср. за 3 мес.)", "bar", "avg",
     "cbr_izhk_debt_m", "region", None,
     (), "region", "Средний портфель ИЖК по субъектам за 3 месяца: запас усредняется, а не суммируется."),
    ("Реализация квартир по регионам, м² (за 3 мес.)", "bar", "sum", "rkop_3", "region", CANON_SOLD,
     (), "region", "Продажи в каноническом срезе, сумма за 3 месяца — поток."),
]

SEGMENTS = [
    ("Субъекты РФ", [["=", {}, _f(F_LEVEL), "region"]]),
    ("Россия в целом", [["=", {}, _f(F_LEVEL), "country"]]),
    ("Реализация квартир: канонический срез", [["=", {}, _f(F_SUB), CANON_SOLD]]),
]



def _ref_legacy(ref):
    """lib-форма ["field", opts, id] -> классическая ["field", id, opts]."""
    if isinstance(ref, list) and ref and ref[0] == "field" and len(ref) == 3:
        opts, fid = ref[1], ref[2]
        return ["field", fid, opts if opts else None]
    return ref


def _clause_legacy(cl):
    """Клауза фильтра/сортировки: ["op", {}, ...аргументы] -> ["op", ...аргументы]."""
    if isinstance(cl, list) and len(cl) >= 2 and isinstance(cl[1], dict) and not cl[1]:
        return [cl[0]] + [_ref_legacy(x) if isinstance(x, list) else x for x in cl[2:]]
    return cl


def to_legacy(query):
    """Запрос в классической форме MBQL — её принимает POST /api/dataset."""
    stage = dict(query["stages"][0])
    stage.pop("lib/type", None)
    if "filters" in stage:
        stage["filter"] = [_clause_legacy(c) for c in stage.pop("filters")]
    if "aggregation" in stage:
        stage["aggregation"] = [_clause_legacy(a) for a in stage["aggregation"]]
    if "breakout" in stage:
        stage["breakout"] = [_ref_legacy(b) for b in stage["breakout"]]
    if "order-by" in stage:
        stage["order-by"] = [_clause_legacy(o) for o in stage["order-by"]]
    return {"database": DB_ID, "type": "query", "query": stage}


class Api:
    def __init__(self):
        key = [l.split("=", 1)[1].strip() for l in open(ENV)
               if l.startswith("METABASE_API_KEY=")][0]
        self.s = requests.Session()
        self.s.headers.update({"x-api-key": key, "Content-Type": "application/json",
                               "Accept": "application/json"})

    def _req(self, method, path, **kw):
        kw.setdefault("timeout", 180)
        r = self.s.request(method, BASE + path, **kw)
        if r.status_code >= 400:
            raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text[:300]}")
        return r.json() if r.text.strip() else None

    def get(self, path, **kw):
        return self._req("GET", path, **kw)

    def post(self, path, payload):
        return self._req("POST", path, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    def put(self, path, payload):
        return self._req("PUT", path, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    def run_card(self, card_id):
        """Выполнить сохранённую карточку — проверка того, что реально лежит в метрике."""
        out = self.post(f"/api/card/{card_id}/query", {}) or {}
        data = out.get("data") or {}
        return out.get("status"), (data.get("rows") or [])


def existing_metrics(api):
    """id существующих метрик коллекции по имени."""
    out = api.get(f"/api/collection/{COLLECTION_ID}/items?models=metric&limit=200")
    items = (out or {}).get("data") or (out if isinstance(out, list) else []) or []
    return {i["name"]: i["id"] for i in items if i.get("name")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()

    api = Api()
    known = existing_metrics(api)
    print(f"существующих метрик: {len(known)}")

    created = updated = 0
    failed = []
    for name, display, agg, code, level, sub, exclude, brk, desc in METRICS:
        window = 3 if brk == "region" else None
        query = metric_query(agg, code, level, sub, exclude, brk, window)
        payload = {"name": name, "description": desc, "display": display,
                   "collection_id": COLLECTION_ID,
                   "dataset_query": query,
                   "visualization_settings": {}}
        try:
            if name in known:
                api.put(f"/api/card/{known[name]}", payload)
                card_id, action = known[name], "обновлена"
                updated += 1
            else:
                payload["type"] = "metric"
                out = api.post("/api/card", payload) or {}
                card_id, action = out.get("id"), "создана"
                created += 1
            status, rows = api.run_card(card_id)
            sample = rows[0] if rows else "пусто"
            ok = status == "completed" and len(rows) > 0
            print(f"  {name:<56} id={card_id} {action}, {status}, строк: {len(rows)}: {sample}")
            if not ok:
                failed.append((name, f"{status}: {len(rows)} строк"))
        except RuntimeError as e:
            failed.append((name, str(e)[:200]))
            print(f"  {name:<56} ОШИБКА: {str(e)[:140]}")
            continue
        if args.dry_run or args.verify:
            continue

    if not (args.dry_run or args.verify):
        for seg_name, filters in SEGMENTS:
            try:
                definition = {"lib/type": "mbql/query", "database": DB_ID,
                              "stages": [{"lib/type": "mbql.stage/mbql",
                                          "source-table": TABLE_ID, "filters": filters}]}
                out = api.post("/api/segment", {"name": seg_name, "table_id": TABLE_ID,
                                                "definition": definition,
                                                "description": "Сегмент семантического слоя: общий фильтр для метрик и вопросов."})
                print(f"сегмент «{seg_name}»: id={out.get('id')}")
            except RuntimeError as e:
                print(f"сегмент «{seg_name}»: {str(e)[:160]}")

    if not (args.dry_run or args.verify):
        keep = {m[0] for m in METRICS}
        for name, cid in existing_metrics(api).items():
            if name not in keep:
                try:
                    api.put(f"/api/card/{cid}", {"archived": True})
                    print(f"архивирована устаревшая метрика: {name} (id={cid})")
                except RuntimeError as e:
                    print(f"не удалось архивировать {name}: {str(e)[:100]}")

    print(f"\nитог: создано {created}, обновлено {updated}, ошибок {len(failed)}")
    for n, e in failed:
        print("  !", n, "->", e)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
