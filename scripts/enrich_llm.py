#!/usr/bin/env python3
"""enrich_llm.py — шаг 2 разметки: LLM-семантика батчами по 20 метрик.

Вход: derived.metric_enrichment (шаг 1, stat_only) + core.metric.
Evidence-пакет на метрику (пилот 2026-09-20: evidence поднимает acc 0.85->1.00):
имя, код, частота, единица, source, first/last значения, период, stat (CV, AC1),
flow_stock-подсказка из шага 1.
Задача LLM: flow_stock (flow/stock/ratio/index/level), value_kind,
econ_group, econ_tags (3-6), описание (<=140 знаков).
Модель: glm-5.3-flash через ollama-cloud (OpenAI-compatible). Ретрай x2, при
двух подряд пустых ответах батч помечается и пропускается (стоп-правило: 3 подряд
сбойных батча -> остановка).
Запуск на ВМ: OLLAMA_API_KEY=... PGHOST=127.0.0.1 PGUSER=wiki ~/.venvs/sandbox/bin/python3 enrich_llm.py [--limit N] [--batch 20]
"""
import json
import os
import re
import sys
import time

import psycopg2
import psycopg2.extras
import requests

BASE = "https://ollama.com/v1"
MODEL = "glm-5.3-flash"
BATCH = 10
SCHEMA_KEYS = ["flow_stock", "value_kind", "econ_group", "econ_tags", "description"]

PROMPT_SYS = """Ты размечаешь экономические ряды РФ (строительство и жильё — приоритет).
Для каждой метрики верни СТРОГО JSON-объект вида:
{"id": <metric_id>, "flow_stock": "flow|stock|ratio|index|level", "value_kind": "point|cumulative|temp|average",
 "econ_group": "<короткая группа: ipoteka|eskrow|smr|vvod|ceny|ddu|stock|dengi|kurs|stavki|makro|demografia|drugoe>",
 "econ_tags": ["тег", ...], "description": "<описание <=140 знаков>"}
Правила: flow — поток за период (выдача, сделки, ввод, объём работ); stock — запас на дату
(остатки, задолженность, действующие ДДУ, строящиеся дома «в составе проектов», площадь с выданными ЗОС);
ratio — ставки, доли, проценты; index — индексы (база сравнения); level — прочие уровни.
«В составе проектов», «с выданными ЗОС», «действующие» = stock. Темпы/приросты = ratio+temp.
Используй evidence: единица, первые/последние значения, AC1/CV. Ответ — только JSON-массив этих объектов, без пояснений."""

def evidence(m):
    parts = [f"id={m['metric_id']}", f"код={m['metric_code']}", f"имя={m['name_ru']}",
             f"частота={m['freq']}", f"источник={m['source_code']}", f"единица={m['unit_code']}"]
    if m.get("first_last"):
        parts.append(f"значения={m['first_last']}")
    sp = m.get("stat") or {}
    if sp.get("cv") is not None: parts.append(f"CV={round(sp['cv'],3)}")
    if sp.get("ac1") is not None: parts.append(f"AC1={round(sp['ac1'],3)}")
    if m.get("heuristic_fs"): parts.append(f"шаг1={m['heuristic_fs']}")
    if m.get("quality"): parts.append(f"качестro={m['quality']}")
    return "; ".join(str(p) for p in parts)

def call_llm(batch_metrics, api_key):
    lines = "\n".join(evidence(m) for m in batch_metrics)
    user = f"Разметь метрики:\n{lines}\nВерни JSON-массив длиной {len(batch_metrics)}."
    r = requests.post(f"{BASE}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": MODEL, "temperature": 0.1, "max_tokens": 6000, "stream": False,
              "messages": [{"role": "system", "content": PROMPT_SYS},
                           {"role": "user", "content": user}]}, timeout=180)
    r.raise_for_status()
    data = r.json()
    msg = data["choices"][0]["message"]
    if not (msg.get("content") or "").strip():
        dbg = {"reason_len": len(msg.get("reasoning") or ""), "finish": data["choices"][0].get("finish_reason")}
        raise ValueError(f"empty content {dbg}")
    return msg["content"]

def parse_json(text):
    m = re.search(r"\[.*\]", text, re.S)
    if not m:
        raise ValueError("no json array")
    arr = json.loads(m.group(0))
    out = {}
    for item in arr:
        if not isinstance(item, dict) or "id" not in item: continue
        mid = int(item["id"])
        fs = item.get("flow_stock")
        if fs not in ("flow","stock","ratio","index","level"): continue
        out[mid] = {"flow_stock": fs,
                    "value_kind": item.get("value_kind") if item.get("value_kind") in ("point","cumulative","temp","average") else None,
                    "econ_group": item.get("econ_group"), "econ_tags": item.get("econ_tags") or [],
                    "description": (item.get("description") or "")[:140]}
    return out

def upsert(conn, results, model):
    with conn.cursor() as cur:
        for mid, r_ in results.items():
            cur.execute("""UPDATE derived.metric_enrichment
                SET flow_stock=%s, value_kind=%s, econ_group=%s, econ_tags=%s::jsonb,
                    ai_model=%s, ai_confidence=%s, enriched_at=now()
                WHERE metric_id=%s""",
                (r_["flow_stock"], r_["value_kind"], r_["econ_group"],
                 psycopg2.extras.Json(r_["econ_tags"]), model, 0.8, mid))
    conn.commit()

def main():
    limit = None
    if "--limit" in sys.argv: limit = int(sys.argv[sys.argv.index("--limit")+1])
    api_key = os.environ["OLLAMA_API_KEY"]
    conn = psycopg2.connect(host=os.environ.get("PGHOST","127.0.0.1"),
        port=int(os.environ.get("PGPORT","5432")),
        user=os.environ.get("PGUSER","wiki"), dbname=os.environ.get("PGDATABASE","research_wiki"))
    q = """
    SELECT e.metric_id, m.metric_code, m.name_ru, m.frequency_id, m.tags::text AS tags,
           e.stat_profile::text, e.quality_flags::text, e.flow_stock AS heuristic_fs,
           (SELECT u.unit_code FROM core.unit u WHERE u.unit_id=m.unit_id) AS unit_code,
           (SELECT s.source_code FROM core.observation_v2 o JOIN core.source s ON s.source_id=o.source_id
             WHERE o.metric_id=m.metric_id LIMIT 1) AS source_code,
           (SELECT string_agg(format('%s=%s', to_char(o.period_start,'YYYY-MM'), o.value), ', ' ORDER BY o.period_start)
              FROM (SELECT DISTINCT ON (period_start) period_start, value FROM core.observation_v2
                     WHERE metric_id=e.metric_id AND value IS NOT NULL ORDER BY period_start, release_id DESC) o
              WHERE o.period_start >= DATE '2015-01-01') AS recent,
           (SELECT o.value FROM core.observation_v2 o WHERE o.metric_id=e.metric_id AND o.value IS NOT NULL
             ORDER BY o.period_start DESC LIMIT 1) AS last_val,
           e.stat_profile::text AS statp, e.quality_flags::text AS qfp
    FROM derived.metric_enrichment e JOIN core.metric m USING(metric_id)
    WHERE e.flow_stock IS NULL AND m.status='active'
    ORDER BY e.metric_id
    """
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(q)
        rows = cur.fetchall()
    if limit: rows = rows[:limit]
    print(f"метрик к разметке: {len(rows)}")
    batches = [rows[i:i+BATCH] for i in range(0, len(rows), BATCH)]
    fails_streak = 0
    done = skipped = 0
    for bi, batch in enumerate(batches):
        for m in batch:
            m["freq"] = {2:"мес",3:"год"}.get(m["frequency_id"], "мес" if m["frequency_id"]==5 else "кварт")
            sp = json.loads(m.pop("statp") or "{}")
            m["stat"] = {"cv": sp.get("cv"), "ac1": sp.get("ac1")}
            m["quality"] = ",".join((json.loads(m.pop("qfp") or "{}")).keys())
            rec = m.pop("recent") or ""
            tail = rec[-120:] if rec else ""
            first = rec.split(", ")[0] if rec else ""
            m["first_last"] = f"{first} ... {m['last_val']} (посл.)" if m.get("last_val") is not None else (tail or "нет данных")
        ok = False
        for attempt in (1, 2):
            try:
                content = call_llm(batch, api_key)
                if not content.strip():
                    print(f"батч {bi}: пустой ответ (попытка {attempt})"); continue
                res = parse_json(content)
                if len(res) >= len(batch) // 2:
                    upsert(conn, res, f"llm:{MODEL}:attempt{attempt}")
                    done += len(res); ok = True; break
                print(f"батч {bi}: разобрано {len(res)} из {len(batch)}")
            except Exception as ex:
                print(f"батч {bi} ошибка (попытка {attempt}): {ex}")
        if not ok:
            skipped += len(batch); fails_streak += 1
            if fails_streak >= 3:
                print("СТОП: 3 подряд сбойных батча"); break
        else:
            fails_streak = 0
        if (bi+1) % 10 == 0: print(f"прогресс: батч {bi+1}/{len(batches)}, размечено {done}, пропущено {skipped}")
    print(f"ИТОГ: размечено={done} пропущено={skipped} батчей={len(batches)}")

if __name__ == "__main__":
    main()
