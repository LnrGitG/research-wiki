#!/usr/bin/env python3
"""mass_control_fallback.py — обратный контроль фолбэк-ответов.

340 метрик ответил Astra (фолбэк). Проверка Astra-же ответов Astra неинформативна,
поэтому выборка 36 фолбэков переразмечается GLM (по тому же evidence-пакету)
и сверяется. Расхождения → needs_review.
Выход: data/metric-review/mass/fallback_control.json
"""
import json
import os
import time
import urllib.request

PROPOSALS = "data/metric-review/mass/proposals.json"
PACK = "data/etl/metric-review/mass/evidence_pack.json"
OUT = "data/metric-review/mass/fallback_control.json"
GLM = "glm-5.3-flash"  # кросс-контроль через Ollama Cloud (у Nous кредиты GLM исчерпаны; Ollama: $0.15/$0.50)
SAMPLE_N = 36
BATCH = 8
BASE = "https://ollama.com/v1"

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
- "index" — индекс/темп в % (указать comparison_base);
- "price" — цена/стоимость единицы;
- "ratio" — доля/отношение/уровень в % без временной природы;
- "accumulation"="year_to_date" — только если значения нарастают с начала года;
- "comparison_base": "level" — уровень; "previous_period" — к предыдущему периоду;
  "same_period_last_year" — к соотв. периоду прошлого года; для index база обязательна.
Поле note — методологическая заметка первоисточника: ДОВЕРЯЙ ЕЙ больше, чем имени.
Отвечай ТОЛЬКО JSON-массивом, без markdown."""


def get_key():
    for line in open(os.path.expanduser("~/.hermes/.env")):
        if line.startswith("OLLAMA_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"')


def call(messages, attempt=1):
    req = urllib.request.Request(
        BASE + "/chat/completions",
        data=json.dumps({"model": GLM, "messages": messages,
                         "temperature": 0.1, "max_tokens": 8000}).encode(),
        headers={"Authorization": f"Bearer {get_key()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            d = json.loads(resp.read())
    except Exception:
        if attempt < 3:
            time.sleep(5 * attempt)
            return call(messages, attempt + 1)
        raise
    msg = d["choices"][0]["message"]
    return msg.get("content") or msg.get("reasoning_content") or "", float(d.get("usage", {}).get("cost") or 0)


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
            "note": item["note"]}


def main():
    props = {p["id"]: p for p in json.load(open(PROPOSALS))["proposals"]}
    pack = {x["id"]: x for x in json.load(open(PACK))}
    fallback_ids = sorted(pid for pid, p in props.items() if p["source"] == "astra_fallback")
    print(f"фолбэк-метрик: {len(fallback_ids)}", flush=True)
    # детерминированная выборка 36
    sample_ids = [pid for i, pid in enumerate(fallback_ids) if i % (len(fallback_ids) // SAMPLE_N or 1) == 0][:SAMPLE_N]
    print(f"выборка: {len(sample_ids)}", flush=True)

    checked, mismatches, cost_total = 0, [], 0.0
    for i in range(0, len(sample_ids), BATCH):
        chunk_ids = sample_ids[i:i + BATCH]
        items = [payload(pack[pid]) for pid in chunk_ids]
        try:
            content, cost = call([
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": "Список показателей:\n" + json.dumps(items, ensure_ascii=False)}])
        except Exception as e:
            print(f"  exc batch {i}: {e}", flush=True)
            continue
        cost_total += cost
        parsed = parse_array(content)
        if not parsed:
            open(f"/tmp/fb_raw_{i}.txt", "w").write(content)
            print(f"  parse-fail batch {i} (raw сохранён в /tmp/fb_raw_{i}.txt)", flush=True)
            continue
        for p_ in parsed:
            if not isinstance(p_, dict) or "id" not in p_:
                continue
            astra = props.get(p_["id"])
            if not astra:
                continue
            checked += 1
            diff = {f: (astra.get(f), p_.get(f))
                    for f in ("temporal_type", "accumulation", "comparison_base")
                    if astra.get(f) != p_.get(f)}
            if diff:
                mismatches.append({"id": p_["id"], "code": pack[p_["id"]]["code"],
                                   "diff": diff,
                                   "name": pack[p_["id"]]["name_ru"][:60]})
        print(f"  batch {i//BATCH}: checked={checked}", flush=True)

    out = {"glm_checks": checked, "mismatches": mismatches,
           "mismatch_rate": round(len(mismatches) / max(checked, 1), 3),
           "cost": round(cost_total, 4)}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"итог: проверено {checked}, расхождений {len(mismatches)} ({out['mismatch_rate']}), cost ${cost_total:.4f}", flush=True)


if __name__ == "__main__":
    main()