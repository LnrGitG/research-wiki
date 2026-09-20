#!/usr/bin/env python3
"""llm_batch.py — шаг 2 разметки: LLM-батч для flow/stock, value_kind, econ_group.

Использование: python3 llm_batch.py <model> [--base URL] [--key-var NOUS_API_KEY]
Модель отвечает строгим JSON по списку метрик из /tmp/llm_batch_test.json.
"""
import json
import os
import sys
import urllib.request

BATCH_FILE = "/tmp/llm_batch_test.json"
OUT_FILE = "/tmp/llm_out_{tag}.json"
TAG = sys.argv[1].replace('/', '_') if len(sys.argv) > 1 else "model"
MODEL = sys.argv[1] if len(sys.argv) > 1 else "glm-5.3-flash"
BASE = "https://inference-api.nousresearch.com/v1"

key = None
for line in open(os.path.expanduser("~/.hermes/.env")):
    if line.startswith("NOUS_API_KEY="):
        key = line.split("=", 1)[1].strip().strip('"')
if not key:
    sys.exit("NOUS_API_KEY not found")

PROMPT = """Ты размечаешь показатели российской макроэкономической статистики.
Для КАЖДОГО показателя верни JSON-объект со строго заданной схемой:
{
 "id": <metric_id как в списке>,
 "flow_stock": "flow" | "stock" | "ratio" | null,
 "value_kind": "point" | "cumulative" | "temp" | null,
 "econ_group": "<короткая группа: ипотека, СМР, демография, внешняя торговля, цены, доходы, пенсии и т.п.>",
 "parent_hint": <номер родительского пункта КЭП или null>,
 "confidence": <0..1>,
 "rationale": "<кратко, 1 фраза>"
}
Правила: "flow" — поток за период (объём работ, выдача, сделки, импорт/экспорт);
"stock" — запас на дату (остатки, задолженность, численность накопленная);
"ratio" — темп/индекс/доля/процент (temp). "mom"/"yoy" в имени означает
производный темп — это ratio/temp, а не сам поток. Если сомневаетесь — null
и confidence < 0.6. Отвечай ТОЛЬКО JSON-массивом без markdown."""


def batch_payload(rows):
    items = [
        {"id": int(r[0]), "code": r[1], "name": r[2], "freq": r[3],
         "stat_hint": json.loads(r[5]) if r[5] else None}
        for r in rows
    ]
    return [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": "Список показателей:\n" + json.dumps(items, ensure_ascii=False)},
    ]


def call(model, messages):
    import urllib.request
    req = urllib.request.Request(
        BASE + "/chat/completions",
        data=json.dumps({"model": model, "messages": messages,
                         "temperature": 0.1, "max_tokens": 16000}).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        d = json.loads(resp.read())
    msg = d["choices"][0]["message"]
    content_out = msg.get("content") or msg.get("reasoning_content") or ""
    return content_out, d.get("usage", {})


def parse(content):
    c = content.strip()
    if c.startswith("```"):
        c = c.strip("`").lstrip("json").strip()
    start, end = c.find("["), c.rfind("]")
    return json.loads(c[start:end + 1]) if start >= 0 and end > start else []


rows = json.load(open(BATCH_FILE))
msgs = batch_payload(rows)
content, usage = call(MODEL, msgs)
json.dump({"model": MODEL, "usage": usage, "raw": content}, open(OUT_FILE.format(tag=TAG), "w"), ensure_ascii=False, indent=1)
try:
    items = parse(content)
except Exception:
    items = []

# Скоринг
ids_expected = {int(r[0]) for r in rows}
got = {i.get("id") for i in items if isinstance(i, dict) and i.get("id") is not None}
valid = [i for i in items if isinstance(i, dict) and i.get("id") in ids_expected]
fs_filled = [i for i in valid if i.get("flow_stock") in ("flow", "stock", "ratio")]
conf = [float(i.get("confidence", 0)) for i in valid if i.get("confidence") is not None]
print(f"model={MODEL}")
print(f"coverage={len(got)}/{len(ids_expected)} valid_json={len(valid)}/{len(items)}")
print(f"flow_stock_filled={len(fs_filled)}")
print(f"avg_confidence={sum(conf)/len(conf):.2f}" if conf else "no confidence")
print(f"usage={usage}")
print("sample:")
for i in valid[:5]:
    print(" ", i.get("id"), i.get("flow_stock"), "|", i.get("econ_group"), "|", str(i.get("rationale"))[:60])