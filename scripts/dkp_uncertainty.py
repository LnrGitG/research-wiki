# -*- coding: utf-8 -*-
"""dkp_uncertainty.py — LLM-извлечение мнений о неопределённости в dkp.

Вариант B из queries/dkp-uncertainty-layer-design.md: из коммуникационного
стека заседания (пресс-релиз + заявление + Резюме) извлекаются
dkp.uncertainty_item четырёх видов:
- risk_balance — баланс про/дезинфляционных рисков;
- open_question — открытый вопрос регулятора;
- conditionality — развилка «условие => следствие»;
- calibration — ordinal-оценка степени (ДКУ, ожидания, разрыв).

Правила (как в dkp_llm_arguments.py): разворотные заседания — manual-only;
дедуп по (meeting_id, md5(text_raw)); эмбеддинг — Yandex text-search-doc.
"""
import hashlib
import json
import re
import subprocess
import sys
import time

import requests

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query, execute

API = "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding"
FOLDER = "b1gpe14c599s44v5dacm"
BASE = "https://ollama.com/v1"
MODEL = "gpt-oss:120b"
CLASSIFIER = "llm:gpt-oss-120b:uncertainty_v1"
DRY = "--dry" in sys.argv

MANUAL_ONLY_DATES = {"2014-12-17", "2022-02-28", "2022-03-18", "2023-07-21",
                     "2025-07-25"}

SYS_PROMPT = """Ты извлекаешь мнения Банка России о НЕОПРЕДЕЛЁННОСТИ из текстов
решений по ключевой ставке (пресс-релиз, заявление Председателя, Резюме).
Найди все позиции четырёх видов:

- risk_balance: баланс рисков («проинфляционные риски выросли и преобладают
  над дезинфляционными») — направление доминирующих рисков;
- open_question: открытый вопрос («потребуется больше данных, чтобы оценить…»,
  «неясно, в какой мере…») — что регулятор сам считает неизвестным;
- conditionality: развилка («если X, то Y», «по мере X снижение возобновится»)
  — условие и следствие раздельно;
- calibration: оценка степени («жесткость несколько снизилась», «спрос
  остается повышенным, но замедляется»).

Для каждой позиции верни JSON-объект:
{"kind": "risk_balance|open_question|conditionality|calibration",
 "variable": "fuel|power_capacity|budget|demand|credit|labour|fx|external|inflation_expect|transmission|inflation_now|other",
 "direction": "proinflation|disinflation|two_sided",
 "horizon": "short|medium|long",
 "premise": "условие (для conditionality, иначе null)",
 "consequence": "следствие (для conditionality, иначе null)",
 "text_raw": "точная цитата из текста, 1-3 предложения",
 "text_short": "суть до 140 символов",
 "source_doc": "press_release|chair_statement|minutes",
 "confidence_note": "оценка уверенности регулятора или null"}

Правила: только явные позиции текста, не додумывай; цитата дословно;
variable — ближайший из словаря; если позиций нет — верни [].
Верни ТОЛЬКО JSON-массив без пояснений."""


def load_ollama_key():
    for line in open("/home/lnr/.hermes/.env", encoding="utf-8"):
        if line.startswith("OLLAMA_API_KEY"):
            return line.split("=", 1)[1].strip()
    return None


_KEY = None


def llm_extract(sys_prompt, user_prompt):
    global _KEY
    if _KEY is None:
        _KEY = load_ollama_key()
    for attempt in range(3):
        try:
            r = requests.post(
                BASE + "/chat/completions",
                headers={"Authorization": "Bearer " + _KEY},
                json={"model": MODEL,
                      "messages": [{"role": "system", "content": sys_prompt},
                                   {"role": "user", "content": user_prompt}],
                      "temperature": 0.1, "max_tokens": 8000},
                timeout=600)
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
            print("  HTTP", r.status_code, r.text[:150])
        except Exception as e:
            print("  llm retry", attempt + 1, str(e)[:120])
        time.sleep(5 + attempt * 8)
    return None


def parse_json_array(text):
    """JSON-массив (терпимо к ```-блокам и обрезке)."""
    if not text:
        return None
    m = re.search(r"\[.*", text, re.S)
    if not m:
        return None
    raw = m.group(0)
    for end in range(len(raw), 0, -1):
        try:
            v = json.loads(raw[:end])
            if isinstance(v, list):
                return v
        except json.JSONDecodeError:
            continue
    return None


def api_key():
    for line in open("/home/lnr/.hermes/.env", encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("нет ключа YANDEX_CLOUD_API_KEY")


KEY = api_key()
_ecache = {}


def embed(text, retries=3):
    h = hashlib.sha256(text.encode()).hexdigest()[:16]
    if h in _ecache:
        return _ecache[h]
    body = json.dumps({"modelUri": "emb://%s/text-search-doc/latest" % FOLDER,
                       "text": text[:4000]}, ensure_ascii=False)
    for attempt in range(retries):
        r = subprocess.run(["curl", "-s", "-m", "40", "-X", "POST", API,
                            "-H", "Authorization: Api-Key " + KEY,
                            "-H", "Content-Type: application/json",
                            "--data-binary", "@-"],
                           input=body, capture_output=True, text=True)
        try:
            v = json.loads(r.stdout).get("embedding")
            if v and len(v) == 256:
                _ecache[h] = v
                return v
        except (json.JSONDecodeError, AttributeError):
            pass
        time.sleep(1.5 * (attempt + 1))
    return []


def esc(s):
    return s.replace("'", "''")


def insert_items(meeting_id, items, stmt_ids):
    n = 0
    for a in items:
        if not isinstance(a, dict):
            continue
        kind = a.get("kind")
        if kind not in ("risk_balance", "open_question", "conditionality",
                        "calibration"):
            continue
        var = (a.get("variable") or "other").strip().lower()[:40]
        direction = a.get("direction") if a.get("direction") in (
            "proinflation", "disinflation", "two_sided") else "two_sided"
        horizon = a.get("horizon") if a.get("horizon") in (
            "short", "medium", "long") else "medium"
        traw = (a.get("text_raw") or "").strip()
        if not traw or len(traw) < 15:
            continue
        dup = query("SELECT 1 FROM dkp.uncertainty_item WHERE meeting_id=%s "
                    "AND md5(text_raw)=md5('%s')" % (meeting_id, esc(traw)))
        if dup:
            continue
        tshort = (a.get("text_short") or "").strip()[:140] or None
        src = a.get("source_doc") or "press_release"
        if src not in stmt_ids:
            src = "press_release" if "press_release" in stmt_ids else next(iter(stmt_ids))
        sid = stmt_ids.get(src)
        minutes_id = stmt_ids.get("minutes") if src == "minutes" else None
        premise = (a.get("premise") or "").strip() or None
        consequence = (a.get("consequence") or "").strip() or None
        cnote = (a.get("confidence_note") or "").strip() or None
        emb = [] if DRY else embed(traw)
        emb_sql = "ARRAY[%s]::vector" % ",".join(str(x) for x in emb) if emb else "NULL"
        span = {"press_release": "пресс-релиз", "chair_statement": "заявление",
                "minutes": "Резюме"}.get(src, src)
        sql = ("INSERT INTO dkp.uncertainty_item "
               "(meeting_id, statement_id, minutes_id, kind, variable, direction, "
               "horizon, premise, consequence, text_raw, text_short, source_span, "
               "confidence_note, embedding, classifier_version) "
               "VALUES (%s, %s, %s, '%s', '%s', '%s', '%s', %s, %s, '%s', %s, '%s', %s, %s, '%s')"
               ) % (meeting_id, sid or "NULL", minutes_id or "NULL",
                    kind, esc(var), direction, horizon,
                    ("'" + esc(premise) + "'") if premise else "NULL",
                    ("'" + esc(consequence) + "'") if consequence else "NULL",
                    esc(traw),
                    ("'" + esc(tshort) + "'") if tshort else "NULL",
                    span, ("'" + esc(cnote) + "'") if cnote else "NULL",
                    emb_sql, CLASSIFIER)
        if not DRY:
            execute(sql)
        n += 1
    return n


def main():
    meetings = query("""
        SELECT m.meeting_id, m.meeting_date::text FROM dkp.meeting m
        WHERE EXISTS (SELECT 1 FROM dkp.statement s WHERE s.meeting_id=m.meeting_id
                      AND s.kind='press_release')
        ORDER BY m.meeting_date""")
    stats = {"ok": 0, "skip_manual": 0, "skip_done": 0, "no_text": 0, "fail": 0,
             "items": 0, "seen": 0}
    for mid, mdate in meetings:
        stats["seen"] += 1
        mdate_s = str(mdate)[:10]
        if mdate_s in MANUAL_ONLY_DATES:
            stats["skip_manual"] += 1
            continue
        n_have = query("SELECT count(*) FROM dkp.uncertainty_item WHERE meeting_id=%s" % mid)[0][0]
        if n_have > 0:
            stats["skip_done"] += 1
            continue
        texts, stmt_ids = {}, {}
        for kind in ("press_release", "chair_statement"):
            r = query("SELECT statement_id, body FROM dkp.statement "
                      "WHERE meeting_id=%s AND kind='%s'" % (mid, kind))
            if r and r[0][1]:
                texts[kind] = r[0][1]
                stmt_ids[kind] = r[0][0]
        rm = query("SELECT minutes_id, body FROM dkp.minutes WHERE meeting_id=%s" % mid)
        if rm and rm[0][1]:
            texts["minutes"] = rm[0][1]
            stmt_ids["minutes"] = rm[0][0]
        if not texts:
            print("no_text %s %s" % (mid, mdate_s))
            stats["no_text"] += 1
            continue
        user = "\n\n".join(
            "=== %s ===\n%s" % ({"press_release": "ПРЕСС-РЕЛИЗ",
                                 "chair_statement": "ЗАЯВЛЕНИЕ ПРЕДСЕДАТЕЛЯ",
                                 "minutes": "РЕЗЮМЕ ОБСУЖДЕНИЯ"}[k], v[:14000])
            for k, v in texts.items())
        ans = llm_extract(SYS_PROMPT, user)
        items = parse_json_array(ans)
        if items is None:
            print("FAIL parse %s %s" % (mid, mdate_s))
            stats["fail"] += 1
            continue
        n = insert_items(mid, items, stmt_ids)
        print("+ %s %s: %d items" % (mid, mdate_s, n))
        stats["ok"] += 1
        stats["items"] += n
    print("\nИТОГ:", stats)


if __name__ == "__main__":
    main()