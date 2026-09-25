# -*- coding: utf-8 -*-
"""
dkp_llm_arguments.py — шаг 2 dkp-дорожной карты: LLM-разметка аргументов
по решениям ДКП из полных текстов коммуникационного стека.

Вход: dkp.statement (press_release + chair_statement) и dkp.minutes (полные
тела) для каждого заседания с решением. Модель: gpt-oss:120b (ollama-cloud),
classifier_version='llm:gpt-oss-120b:prompt_v1'.
Выход: dkp.argument (block, direction, text_raw, text_short, statement_id,
source_span, time_ref='present', concern/conditionality при явности).

Рубрикатор блоков (из manual_v1): demand, credit, labour, inflation_now,
inflation_forecast, inflation_expect, fx, external, fiscal, budget_rule,
transmission, risk_infl, output, signal, rationale.
Directions: hawkish (проинфляционное давление/жестче), dovish, neutral.
Разворотные заседания (17.12.2014, 28.02.2022, 21.07.2023, 25.07.2025 и
внеплановые) — НЕ размечать (пометка manual-only).

--limit=N, --meeting=<id>, --dry
"""
import sys
import json
import time
import re

import requests

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query, execute  # noqa: E402

BASE = "https://ollama.com/v1"
MODEL = "gpt-oss:120b"
CLASSIFIER = "llm:gpt-oss-120b:prompt_v1"
DRY = "--dry" in sys.argv

MANUAL_ONLY_MEETINGS = set()  # заполняется ниже датами разворотных

# разворотные заседания (по датам) — ручная разметка, LLM не трогает
MANUAL_ONLY_DATES = {"2014-12-17", "2022-02-28", "2022-03-18", "2023-07-21",
                     "2025-07-25"}


def load_key():
    for path in ("/home/lnr/.hermes/.env",):
        for line in open(path, encoding="utf-8"):
            if line.startswith("OLLAMA_API_KEY"):
                return line.split("=", 1)[1].strip()
    return None


_KEY = None


def llm_classify(sys_prompt, user_prompt, max_tokens=8000):
    global _KEY
    if _KEY is None:
        _KEY = load_key()
    for attempt in range(3):
        try:
            r = requests.post(
                BASE + "/chat/completions",
                headers={"Authorization": "Bearer " + _KEY},
                json={"model": MODEL,
                      "messages": [{"role": "system", "content": sys_prompt},
                                   {"role": "user", "content": user_prompt}],
                      "temperature": 0.1, "max_tokens": max_tokens},
                timeout=600)
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
            print("  HTTP", r.status_code, r.text[:150])
        except Exception as e:
            print("  llm retry", attempt + 1, str(e)[:120])
        time.sleep(5 + attempt * 8)
    return None


def parse_json_answer(text):
    """JSON-массив из ответа LLM (терпимо к ```-блокам и обрезке)."""
    if not text:
        return None
    m = re.search(r"\[.*", text, re.S)
    if not m:
        m2 = re.search(r"\{.*\}", text, re.S)
        if m2:
            try:
                return [json.loads(m2.group(0))]
            except Exception:
                return None
        return None
    s = m.group(0)
    # нормализуем нестандартные символы, ломающие json.loads
    s = s.replace("‑", "-").replace("–", "-").replace("—", "-")
    for attempt_s in (s, s[:s.rfind("}") + 1] + "]"):
        for cand in (attempt_s,):
            try:
                return json.loads(cand)
            except Exception:
                pass
        # обрезанный массив: закрыть по последнему полному объекту
        idx = s.rfind("}")
        while idx > 0:
            cand = s[:idx + 1] + "]"
            try:
                return json.loads(cand)
            except Exception:
                idx = s.rfind("}", 0, idx)
    return None


SYS_PROMPT = """Ты размечаешь аргументы денежно-кредитной политики Банка России
по текстам решений (пресс-релиз, заявление Председателя, Резюме обсуждения).
Для каждого содержательного утверждения-аргумента верни СТРОГО JSON-объект:
{"block": "<рубрика>", "direction": "hawkish|neutral|dovish",
 "text_raw": "<сжатая суть 1-2 предложениями своими словами, <=200 знаков>",
 "span": "<ссылка на источник: релиз §N / заявление ~середина / резюме §N>",
 "concern": "uncertainty или null", "conditionality": "<условие или пусто>"}
НЕ выводи поле text_short — оно не нужно (экономит токены ответа).

Рубрики block (одна из): demand (внутренний спрос, потребление, инвестиции),
credit (кредитование), labour (рынок труда, зарплаты), inflation_now
(текущая инфляция и устойчивый рост цен), inflation_forecast (прогноз
инфляции), inflation_expect (инфляционные ожидания), fx (курс рубля),
external (внешние условия, нефть, санкции, мировые ставки), fiscal
(бюджетная политика, дефицит), budget_rule (бюджетное правило), transmission
(трансмиссия, чувствительность к ставке), risk_infl (риски вокруг прогноза),
output (выпуск, мощности, разрыв выпуска), signal (сигнал о дальнейших шагах).

direction: hawkish — фактор требует сохранения/повышения жесткости (проинфляционное
давление, риск незаякоривания ожиданий); dovish — фактор позволяет смягчение
(замедление инфляции, охлаждение спроса); neutral — констатация без явного вектора.
Механическая конвенция: «инфляция замедляется быстрее прогноза» = dovish;
«инфляционное давление остается высоким» = hawkish; «спрос повышенный» = hawkish;
«спрос охлаждается» = dovish.

Правила: (1) каждое утверждение с новым содержанием — отдельный аргумент, не
дублировать; (2) фразы «Дискуссия:», «отдельные участники» — тоже аргументы
(concern='uncertainty' если спорные); (3) не выделять банальные вводные («Добрый
день»); (4) 10-25 аргументов на заседание; (5) span — краткая проверяемая ссылка.
Ответ — ТОЛЬКО JSON-массив объектов, без пояснений."""


def build_user_prompt(meeting_id, date, texts):
    parts = [f"Заседание {date} (meeting_id={meeting_id}). Тексты:"]
    for label, body in texts:
        cut = body[:14000]
        parts.append(f"\n=== {label} ===\n{cut}")
    parts.append("\nРазметь аргументы. Ответ — только JSON-массив.")
    return "\n".join(parts)


def main():
    limit = 1000
    single = None
    for a in sys.argv:
        if a.startswith("--limit="):
            limit = int(a.split("=")[1])
        if a.startswith("--meeting="):
            single = int(a.split("=")[1])

    meetings = query("""
        SELECT m.meeting_id, m.meeting_date::text, d.decision_id, d.action
        FROM dkp.meeting m JOIN dkp.decision d USING (meeting_id)
        WHERE m.meeting_date >= '2024-02-01'
        ORDER BY m.meeting_date""")
    stats = {"ok": 0, "skip_manual": 0, "skip_done": 0, "no_text": 0, "fail": 0,
             "args": 0}

    for mid, mdate, did, action in meetings:
        if single and mid != single:
            continue
        if mdate in MANUAL_ONLY_DATES:
            print(f"skip manual-only {mdate}")
            stats["skip_manual"] += 1
            continue
        # дедуп: manual_v1 приоритетен — LLM-разметку не добавляем поверх
        n_manual = query(
            "SELECT count(*) FROM dkp.argument a JOIN dkp.decision d USING (decision_id) "
            "WHERE d.meeting_id=%s AND a.classifier_version='manual_v1'" % mid)[0][0]
        if n_manual > 0:
            print(f"skip {mdate}: manual_v1 уже есть ({n_manual})")
            stats["skip_done"] += 1
            continue
        if n_existing_check(did) > 0:
            stats["skip_done"] += 1
            continue
        # собрать тексты
        texts = []
        for kind in ("press_release", "chair_statement"):
            r = query("SELECT body FROM dkp.statement WHERE meeting_id=%s AND kind='%s'"
                      % (mid, kind))
            if r and r[0][0]:
                texts.append((kind, r[0][0]))
        r = query("SELECT body FROM dkp.minutes WHERE meeting_id=%s" % mid)
        if r and r[0][0]:
            texts.append(("minutes", r[0][0]))
        if not texts:
            print(f"no text {mid} {mdate}")
            stats["no_text"] += 1
            continue
        user = build_user_prompt(mid, mdate, texts)
        if DRY:
            print(f"[dry] {mid} {mdate} texts={len(texts)} chars={sum(len(t[1]) for t in texts)}")
            stats["ok"] += 1
            continue
        ans = llm_classify(SYS_PROMPT, user)
        args = parse_json_answer(ans)
        if not args:
            print(f"FAIL parse {mid} {mdate}")
            stats["fail"] += 1
            continue
        inserted = insert_args(did, mid, args)
        print(f"+ {mid} {mdate}: {inserted}/{len(args)} args")
        stats["ok"] += 1
        stats["args"] += inserted
        if inserted == 0:
            stats["fail"] += 1

    print("\nИТОГ:", stats)
    return 0


def n_existing_check(did):
    r = query("SELECT count(*) FROM dkp.argument WHERE decision_id=%s AND classifier_version='%s'"
              % (did, CLASSIFIER))
    return r[0][0]


def insert_args(did, mid, args):
    """Вставка аргументов; statement_id по span (простая эвристика)."""
    n = 0
    # map kind -> statement_id
    stmap = {}
    r = query("SELECT statement_id, kind FROM dkp.statement WHERE meeting_id=%s" % mid)
    for sid, kind in r:
        stmap[kind] = sid
    for a in args:
        block = a.get("block") or ""
        direction = a.get("direction") or "neutral"
        if block not in ("demand", "credit", "labour", "inflation_now",
                         "inflation_forecast", "inflation_expect", "fx",
                         "external", "fiscal", "budget_rule", "transmission",
                         "risk_infl", "output", "signal"):
            block = "output" if block == "growth" else block
        if block not in ("demand", "credit", "labour", "inflation_now",
                         "inflation_forecast", "inflation_expect", "fx",
                         "external", "fiscal", "budget_rule", "transmission",
                         "risk_infl", "output", "signal"):
            print("    unknown block:", block)
            continue
        if direction not in ("hawkish", "dovish", "neutral"):
            direction = "neutral"
        text_raw = (a.get("text_raw") or "").strip()
        if not text_raw:
            continue
        span = (a.get("span") or "").strip() or None
        # statement_id: если span упоминает резюме/заявление — соотнести
        statement_id = None
        if span:
            sl = span.lower()
            if "резюме" in sl or "minutes" in sl:
                r = query("SELECT minutes_id FROM dkp.minutes WHERE meeting_id=%s" % mid)
                statement_id = -r[0][0] if r else None  # отрицательные = minutes
            elif "заявлен" in sl:
                statement_id = stmap.get("chair_statement")
            elif "релиз" in sl or "пресс-релиз" in sl:
                statement_id = stmap.get("press_release")
        tshort = (a.get("text_short") or "").strip()[:140] or None
        if tshort is None and text_raw:
            tshort = text_raw[:140]
        concern = a.get("concern") if a.get("concern") in ("uncertainty",) else None
        cond = (a.get("conditionality") or "").strip() or None
        sql = ("INSERT INTO dkp.argument "
               "(decision_id, statement_id, block, direction, text_raw, text_short, "
               "source_doc_code, source_span, classifier_version, time_ref, "
               "concern, conditionality) "
               "VALUES (" + str(did) + "," +
               (str(statement_id) if statement_id else "NULL") + ",'" +
               block.replace("'", "''") + "','" + direction + "','" +
               text_raw.replace("'", "''") + "'," +
               (("'" + tshort.replace("'", "''") + "'") if tshort else "NULL") + ",NULL," +
               (("'" + span.replace("'", "''") + "'") if span else "NULL") + ",'" +
               CLASSIFIER + "','present'," +
               (("'" + concern + "'") if concern else "NULL") + "," +
               (("'" + cond.replace("'", "''") + "'") if cond else "NULL") + ")")
        execute(sql)
        n += 1
    return n


if __name__ == "__main__":
    sys.exit(main())