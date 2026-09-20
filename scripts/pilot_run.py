#!/usr/bin/env python3
"""pilot_run.py — этап 3: прогон GLM vs Astra на пилотной выборке.

Два условия: name_only (имя+код+частота) и evidence (+методология, шапка,
значения). Выход: data/etl/metric-review/pilot/pilot_results.json
Метрики успеха: accuracy по temporal_type / accumulation / comparison_base,
доля валидных JSON, доля unknown-ответов, latency, стоимость.
"""
import json
import os
import sys
import time
import urllib.request

SAMPLE = "data/etl/metric-review/pilot/pilot_sample.json"
OUT = "data/etl/metric-review/pilot/pilot_results.json"
BASE = "https://inference-api.nousresearch.com/v1"
MODELS = ["z-ai/glm-5.3", "openai/gpt-6-astra"]
BATCH = 20

PROMPT = """Ты размечаешь показатели российской экономической статистики.
Для КАЖДОГО показателя верни JSON-объект со СТРОГО заданными полями:
{"id": <metric_id>,
 "temporal_type": "flow" | "stock" | "average" | "index" | "price" | "ratio",
 "accumulation": "single_period" | "year_to_date" | null,
 "comparison_base": "level" | "previous_period" | "same_period_last_year" | null}
Определения:
- "flow" — поток за период (объём, выдача, сделки, ввод, инвестиции за период);
- "stock" — запас на дату (остатки, задолженность, количество на отчётную дату);
- "average" — среднее/средневзвешенное за период (ставка, зарплата);
- "index" — индекс/темп в % (база сравнения обязательна);
- "price" — цена/стоимость единицы;
- "ratio" — доля/отношение без временной природы;
- "accumulation"="year_to_date" — только если значения нарастают с начала года;
- "comparison_base": "previous_period" — к предыдущему месяцу/кварталу;
  "same_period_last_year" — к соответствующему периоду прошлого года;
  "level" — уровень без сравнения (для flow/stock/average/price);
  для index — base обязательна, не null.
Если данных недостаточно — "unknown" в поле и id всё равно вернуть.
Отвечай ТОЛЬКО JSON-массивом, без markdown и пояснений."""


def get_key():
    for line in open(os.path.expanduser("~/.hermes/.env")):
        if line.startswith("NOUS_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"')
    raise SystemExit("no NOUS_API_KEY")


def call(model, messages, attempt=1):
    req = urllib.request.Request(
        BASE + "/chat/completions",
        data=json.dumps({"model": model, "messages": messages,
                         "temperature": 0.1, "max_tokens": 16000}).encode(),
        headers={"Authorization": f"Bearer {get_key()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            d = json.loads(resp.read())
    except Exception:
        if attempt < 3:
            time.sleep(5 * attempt)
            return call(model, messages, attempt + 1)
        raise
    msg = d["choices"][0]["message"]
    content = msg.get("content") or msg.get("reasoning_content") or ""
    if msg.get("content") is None and msg.get("reasoning_content"):
        content = msg["reasoning_content"]  # reasoning-модель без финального ответа
        # искать в reasoning массив JSON
    return content, d.get("usage", {})


def parse_array(content):
    c = content.strip()
    if c.startswith("```"):
        c = c.strip("`").lstrip("json").strip()
    s, e = c.find("["), c.rfind("]")
    if s < 0 or e <= s:
        return None
    try:
        return json.loads(c[s:e + 1])
    except Exception:
        return None


def item_payload(item, condition):
    base = {"id": item["id"], "code": item["code"], "name_ru": item["name_ru"],
            "freq_id": item["freq_id"]}
    if condition == "evidence":
        base["unit_db"] = item["unit_db"]
        base["values"] = {"first": item["first_value"], "last": item["last_value"],
                          "n_obs_rf": item["n_obs_rf"]}
        base["period"] = [item["period_min"], item["period_max"]]
        if item["evidence_note"]:
            base["source_note"] = item["evidence_note"]
    return base


def run_condition(model, condition, sample):
    results, invalid_batches, cost, t0 = [], 0, 0.0, time.time()
    dump_dir = os.path.join(os.path.dirname(OUT), "raw_dumps")
    for i in range(0, len(sample), BATCH):
        chunk = sample[i:i + BATCH]
        items = [item_payload(x, condition) for x in chunk]
        messages = [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": "Список показателей:\n" + json.dumps(items, ensure_ascii=False)},
        ]
        try:
            content, usage = call(model, messages)
        except Exception as e:
            invalid_batches += 1
            print(f"  FAIL {model}/{condition} batch {i//BATCH}: {e}", flush=True)
            continue
        parsed = parse_array(content)
        if parsed is None:
            invalid_batches += 1
            os.makedirs(dump_dir, exist_ok=True)
            tag = f"{model.split('/')[1]}_{condition}_{i//BATCH}.txt"
            with open(os.path.join(dump_dir, tag), "w") as fh:
                fh.write(content[:20000])
            print(f"  PARSE-FAIL {model}/{condition} batch {i//BATCH} -> raw_dumps/{tag}", flush=True)
            continue
        cost += float(usage.get("cost") or 0)
        for p_ in parsed:
            if isinstance(p_, dict) and "id" in p_:
                results.append(p_)
    return {"model": model, "condition": condition, "results": results,
            "invalid_batches": invalid_batches, "cost": round(cost, 4),
            "latency_s": round(time.time() - t0, 1)}


def score(preds, sample):
    gold = {x["id"]: x for x in sample}
    fields = ["temporal_type", "accumulation", "comparison_base"]
    per_field = {f: {"correct": 0, "answered": 0, "unknown": 0} for f in fields}
    crit_errors = []
    for p_ in preds:
        g = gold.get(p_["id"])
        if not g:
            continue
        for f in fields:
            pv = p_.get(f)
            if pv in (None, "unknown", "null"):
                per_field[f]["unknown"] += 1
            else:
                per_field[f]["answered"] += 1
                gv = g["gold"][f]
                if str(pv) == gv:
                    per_field[f]["correct"] += 1
                elif f == "temporal_type":
                    crit_errors.append((g["code"], pv, gv, g["tricky"]))
    n = len([x for x in preds if x["id"] in gold])
    out = {}
    for f in fields:
        pf = per_field[f]
        out[f] = {"accuracy_of_answered": round(pf["correct"] / pf["answered"], 3) if pf["answered"] else None,
                  "answered": pf["answered"], "unknown": pf["unknown"], "n": n}
    return out, crit_errors


def main():
    sample = json.load(open(SAMPLE))
    holdout = [x for x in sample if x["holdout"]]
    tuning = [x for x in sample if not x["holdout"]]
    all_out = []
    for model in MODELS:
        for cond in ("name_only", "evidence"):
            print(f"== {model} / {cond} ==", flush=True)
            res_t = run_condition(model, cond, tuning)
            res_h = run_condition(model, cond, holdout)
            sc_t, ce_t = score(res_t["results"], tuning)
            sc_h, ce_h = score(res_h["results"], holdout)
            all_out.append({
                "model": model, "condition": cond,
                "tuning": {"scores": sc_t, "critical_errors": ce_t, "invalid_batches": res_t["invalid_batches"],
                           "cost": res_t["cost"], "latency_s": res_t["latency_s"]},
                "holdout": {"scores": sc_h, "critical_errors": ce_h, "invalid_batches": res_h["invalid_batches"],
                            "cost": res_h["cost"], "latency_s": res_h["latency_s"]},
            })
            print(f"  tuning: {json.dumps(sc_t, ensure_ascii=False)}", flush=True)
            print(f"  holdout: {json.dumps(sc_h, ensure_ascii=False)}", flush=True)
    json.dump(all_out, open(OUT, "w"), ensure_ascii=False, indent=1)
    total_cost = sum(x["tuning"]["cost"] + x["holdout"]["cost"] for x in all_out)
    print(f"\nзаписано {OUT}; суммарная стоимость ${total_cost:.3f}")


if __name__ == "__main__":
    main()
