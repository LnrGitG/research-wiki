#!/usr/bin/env python3
"""mass_run.py — этап 4: массовая разметка GLM + фолбэк Astra + контроль Astra.

Схема (утверждена пилотом, queries/pilot-llm-annotation-results.md):
1. GLM+evidence по всем preliminary, ретрай 2x; пустой/битый ответ → фолбэк Astra.
2. Контроль Astra: случайная детерминированная 10% выборка.
3. Выход: JSONL-чекпоинты по батчам + итоговый proposal-файл.

Возобновляемость: батч_i.jsonl уже обработанные пропускаются.
Лимит расходов: остановка при превышении BUDGET_USD.
"""
import json
import hashlib
import os
import sys
import time
import urllib.request

PACK = "data/etl/metric-review/mass/evidence_pack.json"
CKPT_DIR = "data/etl/metric-review/mass/checkpoints"
OUT = "data/etl/metric-review/mass/proposals.json"
BATCH = 20
BUDGET_USD = 8.0

GLM = "z-ai/glm-5.3"
ASTRA = "openai/gpt-6-astra"
BASE = "https://inference-api.nousresearch.com/v1"

PROMPT = """Ты размечаешь показатели российской экономической статистики.
Для КАЖДОГО показателя верни JSON-объект со СТРОГО заданными полями:
{"id": <metric_id>,
 "temporal_type": "flow" | "stock" | "average" | "index" | "price" | "ratio",
 "accumulation": "single_period" | "year_to_date" | null,
 "comparison_base": "level" | "previous_period" | "same_period_last_year" | null,
 "econ_group": "<короткая группа: ипотека, эскроу, СМР, строительство, инвестиции, ввод жилья, цены жилья, цены, доходы, промпроизводство, демография, бюджет, внешняя торговля, кредитование, другое>"}
Определения:
- "flow" — поток за период (объём, выдача, сделки, ввод, инвестиции за период);
- "stock" — запас на дату (остатки, задолженность, количество на отчётную дату);
- "average" — среднее/средневзвешенное за период (ставка, зарплата);
- "index" — индекс/темп в % (указать comparison_base);
- "price" — цена/стоимость единицы;
- "ratio" — доля/отношение/уровень в % без временной природы;
- "accumulation"="year_to_date" — только если значения нарастают с начала года;
- "comparison_base": "level" — уровень без сравнения; "previous_period" — к предыдущему периоду;
  "same_period_last_year" — к соотв. периоду прошлого года; для index база обязательна.
Поле note в данных — методологическая заметка первоисточника: ДОВЕРЯЙ ЕЙ больше, чем имени.
При сомнениях между flow и stock: слова «на дату», «действующие», «остатки», «наличие»
означают stock; «за месяц/квартал/год», «выдано», «введено» — flow.
Отвечай ТОЛЬКО JSON-массивом, без markdown."""


def get_key():
    for line in open(os.path.expanduser("~/.hermes/.env")):
        if line.startswith("NOUS_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"')
    raise SystemExit("no key")


def call(model, messages, attempt=1):
    req = urllib.request.Request(
        BASE + "/chat/completions",
        data=json.dumps({"model": model, "messages": messages,
                        "temperature": 0.1, "max_tokens": 16000}).encode(),
        headers={"Authorization": f"Bearer {get_key()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            d = json.loads(resp.read())
    except Exception as e:
        if attempt < 3:
            time.sleep(5 * attempt)
            return call(model, messages, attempt + 1)
        raise
    msg = d["choices"][0]["message"]
    content = msg.get("content") or msg.get("reasoning_content") or ""
    return content, float(d.get("usage", {}).get("cost") or 0)


def parse_array(content):
    c = content.strip()
    if c.startswith("```"):
        c = c.strip("`").lstrip("json").strip()
    s, e = c.find("["), c.rfind("]")
    if s < 0 or e <= s:
        return None
    try:
        arr = json.loads(c[s:e + 1])
        return arr if isinstance(arr, list) else None
    except Exception:
        return None


def payload(item):
    return {"id": item["id"], "code": item["code"], "name_ru": item["name_ru"],
            "freq_id": item["freq_id"], "unit_db": item["unit_db"],
            "first_value": item["first_value"], "last_value": item["last_value"],
            "period": [item["period_min"], item["period_max"]],
            "n_obs_rf": item["n_obs_rf"], "n_regions": item["n_regions"],
            "note": item["note"]}


def run_batch(model, items):
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": "Список показателей:\n" + json.dumps(items, ensure_ascii=False)},
    ]
    content, cost = call(model, messages)
    parsed = parse_array(content)
    return parsed, cost


def main():
    pack = json.load(open(PACK))
    os.makedirs(CKPT_DIR, exist_ok=True)
    n_batches = (len(pack) + BATCH - 1) // BATCH
    print(f"метрик: {len(pack)}, батчей: {n_batches}", flush=True)

    # контрольная выборка Astra 2% (36 метрик, детерминированно; сокращено
    # с 10% по решению владельца 2026-09-20)
    control_ids = {x["id"] for x in pack
                   if int(hashlib.md5(str(x["id"]).encode()).hexdigest(), 16) % 50 == 0}

    total_cost = 0.0
    glm_ok = glm_fallback = 0
    for bi in range(n_batches):
        ckpt = os.path.join(CKPT_DIR, f"batch_{bi:03d}.jsonl")
        if os.path.exists(ckpt):
            continue
        if total_cost > BUDGET_USD:
            print(f"BUDGET STOP at batch {bi} (${total_cost:.2f})", flush=True)
            break
        chunk = pack[bi * BATCH:(bi + 1) * BATCH]
        items = [payload(x) for x in chunk]
        ids = {x["id"] for x in chunk}
        results = None
        cost = 0.0
        source = "glm"
        # проход GLM (2 попытки внутри call)
        try:
            parsed, c = run_batch(GLM, items)
            cost += c
            if parsed and all(isinstance(p_, dict) and "id" in p_ for p_ in parsed) and \
               {p_.get("id") for p_ in parsed} == ids:
                results = parsed
        except Exception as e:
            print(f"  b{bi} GLM exc: {e}", flush=True)
        if results is None:
            # фолбэк Astra
            source = "astra_fallback"
            try:
                parsed, c = run_batch(ASTRA, items)
                cost += c
                if parsed:
                    results = [p_ for p_ in parsed if isinstance(p_, dict) and p_.get("id") in ids]
            except Exception as e:
                print(f"  b{bi} ASTRA exc: {e}", flush=True)
        if results is None:
            print(f"  b{bi}: FAIL both", flush=True)
            continue
        glm_ok += len(results) if source == "glm" else 0
        glm_fallback += len(results) if source != "glm" else 0
        total_cost += cost
        with open(ckpt, "w", encoding="utf-8") as fh:
            for p_ in results:
                fh.write(json.dumps({"p": p_, "src": source}, ensure_ascii=False) + "\n")
        if bi % 10 == 0:
            print(f"  b{bi}/{n_batches}: cost ${total_cost:.3f}, ok={glm_ok}, fb={glm_fallback}", flush=True)

    # сборка итога
    all_p = []
    for bi in range(n_batches):
        ckpt = os.path.join(CKPT_DIR, f"batch_{bi:03d}.jsonl")
        if os.path.exists(ckpt):
            for line in open(ckpt, encoding="utf-8"):
                rec = json.loads(line)
                rec["p"]["source"] = rec["src"]
                all_p.append(rec["p"])
    json.dump({"proposals": all_p, "total_cost": round(total_cost, 4),
               "n": len(all_p)}, open(OUT, "w"), ensure_ascii=False, indent=0)
    print(f"итог: {len(all_p)} предложений, стоимость ${total_cost:.3f}", flush=True)

    # контроль Astra на 10% выборке
    ctrl_items = [x for x in pack if x["id"] in control_ids]
    prop_by_id = {p["id"]: p for p in all_p}
    mismatches = 0
    checked = 0
    for i in range(0, len(ctrl_items), BATCH):
        chunk = ctrl_items[i:i + BATCH]
        items = [payload(x) for x in chunk]
        try:
            parsed, c = run_batch(ASTRA, items)
        except Exception as e:
            print(f"  control exc: {e}", flush=True)
            break
        total_cost += c
        for p_ in parsed or []:
            if not isinstance(p_, dict) or "id" not in p_:
                continue
            glmp = prop_by_id.get(p_["id"])
            if not glmp:
                continue
            checked += 1
            diff = [f for f in ("temporal_type", "accumulation", "comparison_base")
                    if p_.get(f) != glmp.get(f)]
            if diff:
                mismatches += 1
                print(f"  MISMATCH id={p_['id']}: {diff}: glm={ {f: glmp.get(f) for f in diff} } vs astra={ {f: p_.get(f) for f in diff} }", flush=True)
    print(f"контроль Astra: проверено {checked}, расхождений {mismatches}, доля {mismatches/max(checked,1):.3f}", flush=True)
    print(f"полная стоимость: ${total_cost:.3f}", flush=True)
    json.dump({"proposals": all_p, "total_cost": round(total_cost, 4),
               "n": len(all_p), "control_checked": checked,
               "control_mismatches": mismatches},
              open(OUT, "w"), ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main()
