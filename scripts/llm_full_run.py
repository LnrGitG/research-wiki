#!/usr/bin/env python3
"""llm_full_run.py — шаг 2 полный: LLM-разметка спорных метрик батчами по 20 через GPT-6 Astra.

Запуск на ВМ: nohup python3 ~/specs/llm_full_run.py > /tmp/llm_full.log 2>&1 &
Пишет llm-поля в derived.metric_enrichment; прогресс в /tmp/llm_full_progress.json.
Устойчивость: чекпоинт по батчам, ретрай 3×, при сбое батча — пропуск и лог.
"""
import json
import os
import time
import urllib.request

import psycopg2
import psycopg2.extras

BASE = "https://inference-api.nousresearch.com/v1"
MODEL = "openai/gpt-6-astra"
BATCH = 20
PROGRESS_FILE = "/tmp/llm_full_progress.json"

PROMPT = """Ты размечаешь показатели российской макроэкономической статистики.
Для КАЖДОГО показателя верни JSON-объект:
{"id": <metric_id>, "flow_stock": "flow"|"stock"|"ratio"|null,
 "value_kind": "point"|"cumulative"|"temp"|null,
 "econ_group": "<короткая группа: ипотека, СМР, демография, внешняя торговля, цены, доходы, пенсии, стройматериалы, жильё, кредитование и т.п.>",
 "confidence": <0..1>, "rationale": "<1 фраза>"}
Правила: "flow" — поток за период (объём, выдача, сделки, импорт, ввод);
"stock" — запас на дату (остатки, задолженность, численность);
"ratio" — темп/индекс/доля/процент (temp). "mom"/"yoy" в имени = производный
темп → ratio/temp. Сомневаешься — null и confidence<0.6.
Отвечай ТОЛЬКО JSON-массивом без markdown."""


def get_key():
    for path in (os.path.expanduser("~/.hermes/.env"), os.path.expanduser("~/agent/.env")):
        try:
            for line in open(path):
                if line.startswith("NOUS_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"')
        except OSError:
            continue
    raise SystemExit("NOUS_API_KEY not found")


KEY = get_key()


def call(messages, attempt=1):
    req = urllib.request.Request(
        BASE + "/chat/completions",
        data=json.dumps({"model": MODEL, "messages": messages,
                         "temperature": 0.1, "max_tokens": 16000}).encode(),
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            d = json.loads(resp.read())
    except Exception as e:
        if attempt < 3:
            time.sleep(5 * attempt)
            return call(messages, attempt + 1)
        raise
    msg = d["choices"][0]["message"]
    return (msg.get("content") or msg.get("reasoning_content") or ""), d.get("usage", {})


def parse(content):
    c = content.strip()
    if c.startswith("```"):
        c = c.strip("`").lstrip("json").strip()
    s, e = c.find("["), c.rfind("]")
    return json.loads(c[s:e + 1]) if 0 <= s < e else []


def main():
    conn = psycopg2.connect(host="127.0.0.1", port=5432, user="wiki", dbname="research_wiki")
    cur = conn.cursor()
    cur.execute("""
        SELECT e.metric_id, m.metric_code, m.name_ru, m.frequency_id,
               e.stat_profile
        FROM derived.metric_enrichment e
        JOIN core.metric m ON m.metric_id = e.metric_id
        WHERE e.flow_stock IS NULL
        ORDER BY e.metric_id
    """)
    metrics = cur.fetchall()
    total = len(metrics)
    print(f"metrics to label: {total}", flush=True)

    done_ids, cost_total = [], 0.0
    if os.path.exists(PROGRESS_FILE):
        p = json.load(open(PROGRESS_FILE))
        done_ids = p.get("done_ids", [])
        cost_total = p.get("cost_total", 0.0)
    done_set = set(done_ids)
    todo = [m for m in metrics if m[0] not in done_set]

    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        items = [{"id": m[0], "code": m[1], "name": m[2],
                  "freq": m[3], "stat": m[4]} for m in chunk]
        messages = [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": "Список:\n" + json.dumps(items, ensure_ascii=False)},
        ]
        t0 = time.time()
        try:
            content, usage = call(messages)
        except Exception as e:
            print(f"batch {i//BATCH}: CALL FAIL {e}", flush=True)
            continue
        try:
            parsed = parse(content)
        except Exception as e:
            print(f"batch {i//BATCH}: PARSE FAIL {e}", flush=True)
            continue
        valid = [p_ for p_ in parsed if isinstance(p_, dict) and p_.get("id") in {m[0] for m in chunk}]
        # запись
        for p_ in valid:
            cur.execute("""
                UPDATE derived.metric_enrichment
                SET flow_stock=%s, value_kind=%s, econ_group=%s,
                    ai_model=%s, ai_confidence=%s
                WHERE metric_id=%s
            """, (p_.get("flow_stock"), p_.get("value_kind"), p_.get("econ_group"),
                  MODEL, float(p_.get("confidence", 0.5)) if p_.get("confidence") is not None else 0.5,
                  p_["id"]))
        conn.commit()
        cost_total += usage.get("cost", 0.0) if usage else 0.0
        done_ids.extend([p_["id"] for p_ in valid])
        json.dump({"done_ids": done_ids, "cost_total": cost_total}, open(PROGRESS_FILE, "w"))
        print(f"batch {i//BATCH + 1}/{(len(todo)+BATCH-1)//BATCH}: +{len(valid)} "
              f"({time.time()-t0:.0f}s, cost ${cost_total:.3f})", flush=True)
        time.sleep(2)  # мягкий темп против rate limit (50 RPM)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()