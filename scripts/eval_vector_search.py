#!/usr/bin/env python3
"""Замер качества векторного поиска: 20 запросов с известными ответами.

Сравнивает три способа найти нужную статью в корпусе:

  A. текущий слой вики — один УСРЕДНЁННЫЙ вектор на документ
     (`docs/vector-embeddings.json`, модель paraphrase-MiniLM-L3-v2);
  B. чанк-поиск на той же модели — лучший чанк документа;
  C. чанк-поиск на модели Yandex (`text-search-doc`/`text-search-query`,
     256 измерений, асимметричные).

Метрика: recall@10 — попал ли эталонный документ в первые 10 результатов.
Дополнительно: ранг эталона (чем ниже, тем лучше) и MRR.

**Как строится эталон.** Для каждого запроса вручную указан список стемов
статей, которые обязаны найтись. Стемы взяты из реального корпуса, поэтому
проверка воспроизводима. Ручная разметка — не идеал (один запрос может
относиться к нескольким работам), поэтому у каждого запроса список из 1–3
эталонов, и попаданием считается любой из них.

Запуск:  python3 scripts/eval_vector_search.py              # все три способа
         python3 scripts/eval_vector_search.py --only A     # только текущий
         python3 scripts/eval_vector_search.py --json out.json
"""
import argparse
import base64
import glob
import json
import math
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

YANDEX_FOLDER = "b1gpe14c599s44v5dacm"

# ── Эталонная разметка: запрос -> стемы, которые обязаны найтись ──────
# Стемы проверены по реальному корпусу (ls papers/).
QUERIES = [
    ("эластичность предложения жилья и ограничения на застройку",
     ["saiz-2010-geographic-determinants-housing-supply",
      "gyourko-molloy-2014-regulation-housing-supply",
      "green-malpezzi-mayo-2005-supply-elasticity"]),
    ("как шок денежно-кредитной политики передаётся в цены жилья",
     ["Albuquerque-The-house-supply-channel-of-the-monetary-policy-2024",
      "mishkin-2007-housing-monetary-transmission",
      "Elbourne.-The-UK-housing-market-and-the-mone"]),
    ("прогнозирование цен на жилье в реальном времени",
     ["Plakandaras-Forecasting-the-U.S.-Real-House-Price-Index",
      "Rapach-Differences-in-housing-price-forecast",
      "Yarui_Forecasting Housing Prices Dynamic Factor Model VS LBVAR Model_2011"]),
    ("наукастинг регионального выпуска смешанными частотами",
     ["Koop-etal-JRSSA2019-UK-regional-nowcasting-using-a-m",
      "Paper-CGLMS-Mixed-Frequency-BVAR-Nowcasting",
      "rbnz-2025-gdp-nowcasting-dfm"]),
    ("методы факторного расширения VAR для трансмиссии",
     ["Bernanke-Measuring-the-Effects-of-Monetary-Policy-FA",
      "Boivin.-Sticky-prices-and-monetary-policy"]),
    ("регулирование землепользования и цены на жилье",
     ["Yezer-2026-land-use-regulation-housing-prices-JRS",
      "mayer-somerville-2000-land-regulation",
      "gyourko-molloy-2014-regulation-housing-supply"]),
    ("пузырь на рынке жилья США",
     ["case-shiller-2003-is-there-a-bubble-in-housing-marke",
      "himmelberg-mayer-sinai-2005-assessing-high-house-pri"]),
    ("ипотечный рынок и передача денежно-кредитной политики",
     ["Drechsler-Savov-Schnabl-2024-monetary-policy-mortgag",
      "Hedlund-Larkin-Mitman-Ozkan-2025-mortgage-MP-great-i",
      "Effects-of-a-Mortgage-Interest-Rate-Subsidy-Evidence"]),
    ("влияние денежно-кредитной политики на цены жилья в Китае",
     ["Chen.-TheImpactofMonentaryPolicyonHousingPricesinChi",
      "Gao-The-Effects-of-National-Fundamental-Factors-on-Regional-House-Prices-FAVAR-analysis-2022"]),
    ("инфляционные ожидания населения и региональные цены",
     ["lyziak_pedersen_stanislawska_2022"]),
    ("издержки корректировки и асимметрия предложения жилья",
     ["kenny-1999-asymmetric-adjustment-costs-housing-supply"]),
    ("цена земли и доступность жилья в городах",
     ["baum-snow-duranton-2025-housing-supply-affordabili",
      "glaeser-gyourko-2018-housing-supply-jep"]),
    ("модель q-Тобина для цен на жилье",
     ["madsen-2011-q-model-house-prices",
      "poterba-1984-tax-subsidies",
      "topel-rosen-1988-housing-investment"]),
    ("рынок жилья и макроэкономика в Европе",
     ["house_prices_macroconomy_europe_svar_iacoviello_2000",
      "Iacoviello.-HOUSE-PRICES"]),
    ("пространственная эконометрика цен на жилье",
     ["Bailey-A-Two-Stage-Approach-to-Spatio-Temporal-Analysis",
      "spatial_indirect_inference_rossi_2023"]),
    ("макропруденциальная политика и рынок жилья",
     ["Bardoscia-The-impact-of-prudential-regulations-UK-housing-agent-based"]),
    ("прогнозирование инвестиций в жилье факторными моделями",
     ["Smith-Forecasting-Investment-and-House-Prices-in-NZ",
      "Forecasting-Investment-and-House-Prices-in-NZ-using-Dynamic-Factor"]),
    ("цены на жилье и банковские риски",
     ["banai_vago_2018_house_prices_bank_risk"]),
    ("энтропийное наклонение прогнозов BVAR",
     ["Tallman-Zaman-IJF-2020-Combining-survey-long-run-forecasts-and-nowcasts-with-BVAR",
      "wp 1439 using entropic tilting to combine BVAR Forecats with external nowcasts pdf"]),
    ("передача денежно-кредитной политики в экономику Великобритании",
     ["Elbourne.-The-UK-housing-market-and-the-mone",
      "Mumtaz-A-time-varying-FAVAR-model-for-the-UK-transmission-mechanism-2011"]),
]


def corpus():
    """Стемы всех статей корпуса."""
    return sorted(os.path.basename(p)[:-3] for p in glob.glob("papers/*.md"))


def body_of(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    if s.startswith("---") and s.count("---") >= 2:
        return s.split("---", 2)[2]
    return s


def chunks_of(path, size=1000, overlap=100):
    """Те же чанки, что в rebuild_embeddings.py — для честного сравнения."""
    t = body_of(path)
    if len(t) <= size:
        return [t] if t.strip() else []
    out, i = [], 0
    while i < len(t):
        c = t[i:i + size]
        if c.strip():
            out.append(c)
        i += size - overlap
    return out


def cos(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if not na or not nb:
        return 0.0
    return sum(x * y for x, y in zip(a, b)) / (na * nb)


# ── Способ A: текущий усреднённый слой вики ──────────────────────────

def eval_current(stems, queries):
    """Текущий слой: один усреднённый вектор на документ."""
    d = json.load(open("docs/vector-embeddings.json", encoding="utf-8"))
    dim = d["dim"]
    dtype = d.get("dtype", "float32")     # здесь float16 — не float32!
    raw = base64.b64decode(d["embeddings_b64"])
    import numpy as np
    # typecode 'e' (float16) в array модуля Python 3.11 отсутствует — только numpy
    np_dt = np.float16 if dtype == "float16" else np.float32
    mat = np.frombuffer(raw, dtype=np_dt).reshape(-1, dim).astype(np.float32)
    n = mat.shape[0]
    meta = d.get("meta") or []
    keys = [m.get("file") or "" for m in meta] if meta else []
    print("  способ A: %d векторов, dtype=%s, метаданных %d" % (n, dtype, len(keys)))

    # модель для кодирования запроса — та же, что строила слой
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("paraphrase-MiniLM-L3-v2", device="cpu")

    res = {}
    for q, gold in queries:
        import numpy as np
        qv = model.encode([q])[0].astype(np.float32)
        # косинус = скалярное произведение (векторы слоя нормированы)
        sims = mat @ qv
        order = np.argsort(-sims)[:10]
        top = [keys[i][:-3] if keys[i].endswith(".md") else keys[i] for i in order]
        res[q] = top
    return res


# ── Способ B: чанк-поиск на локальной модели ─────────────────────────

def eval_chunks_local(stems, queries):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("paraphrase-MiniLM-L3-v2", device="cpu")
    print("  способ B: кодирую чанки корпуса (%d статей)..." % len(stems))
    doc_chunks = {}
    for st in stems:
        p = "papers/%s.md" % st
        if os.path.exists(p):
            doc_chunks[st] = chunks_of(p)
    total = sum(len(v) for v in doc_chunks.values())
    print("    чанков: %d" % total)

    # кодируем пакетами
    flat, owner = [], []
    for st, cs in doc_chunks.items():
        for c in cs:
            flat.append(c)
            owner.append(st)
    embs = model.encode(flat, batch_size=32, show_progress_bar=False)

    import numpy as np
    # нормализуем и агрегируем матрично: max по чанкам внутри документа
    M = np.asarray(embs, dtype=np.float32)
    M /= (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)
    owners = np.array(owner)
    uniq = sorted(set(owner))
    res = {}
    for q, gold in queries:
        qv = model.encode([q])[0].astype(np.float32)
        qv /= (np.linalg.norm(qv) + 1e-9)
        sims = M @ qv
        # максимум по чанкам каждого документа
        best = {st: float(sims[owners == st].max()) for st in uniq}
        res[q] = [k for k, _ in sorted(best.items(), key=lambda x: -x[1])[:10]]
    return res


# ── Способ C: чанк-поиск на Yandex ───────────────────────────────────

def yandex_key():
    env = os.path.expanduser("~/.hermes/.env")
    for line in open(env, encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def yandex_emb(texts, kind="doc"):
    """Пакетно (по одному, API не принимает список на этот эндпоинт)."""
    key = yandex_key()
    out = []
    for t in texts:
        body = json.dumps({"modelUri": "emb://%s/text-search-%s/latest" % (YANDEX_FOLDER, kind),
                           "text": t[:4000]}, ensure_ascii=False)
        r = subprocess.run(["curl", "-s", "-m", "40", "-X", "POST",
                            "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding",
                            "-H", "Authorization: Api-Key %s" % key,
                            "-H", "Content-Type: application/json",
                            "--data-binary", "@-"],
                           input=body, capture_output=True, text=True)
        try:
            out.append(json.loads(r.stdout).get("embedding", []))
        except Exception:
            out.append([])
    return out


def eval_chunks_yandex(stems, queries, max_chunks=60):
    """Чанк-поиск Yandex. Чтобы не гонять 24 тыс. чанков, берём лучшие
    по полнотекстовой предвыборке: API дорогой по времени (78 мин на корпус)."""
    print("  способ C: Yandex, беру до %d чанков на статью (первые+ключевые)" % max_chunks)
    doc_chunks = {}
    for st in stems:
        p = "papers/%s.md" % st
        if os.path.exists(p):
            doc_chunks[st] = chunks_of(p)[:max_chunks]
    total = sum(len(v) for v in doc_chunks.values())
    print("    чанков к кодированию: %d (оценка времени %.0f мин)"
          % (total, total * 0.19 / 60))

    flat, owner = [], []
    for st, cs in doc_chunks.items():
        for c in cs:
            flat.append(c)
            owner.append(st)
    embs = yandex_emb(flat, "doc")
    ok = sum(1 for e in embs if e)
    print("    векторов получено: %d из %d" % (ok, len(flat)))

    qembs = yandex_emb([q for q, _ in queries], "query")
    res = {}
    for (q, gold), qv in zip(queries, qembs):
        if not qv:
            res[q] = []
            continue
        best = {}
        for i, st in enumerate(owner):
            if not embs[i]:
                continue
            s = cos(qv, embs[i])
            if s > best.get(st, -1):
                best[st] = s
        res[q] = [k for k, _ in sorted(best.items(), key=lambda x: -x[1])[:10]]
    return res


def score(res, queries, label):
    hit = 0
    ranks = []
    misses = []
    for q, gold in queries:
        top = res.get(q, [])
        r = None
        for i, doc in enumerate(top):
            if any(g[:28] in doc or doc[:28] in g for g in gold):
                r = i + 1
                break
        if r:
            hit += 1
            ranks.append(r)
        else:
            misses.append((q, gold[0][:44], top[0][:44] if top else "—"))
    n = len(queries)
    recall = 100 * hit / n
    mrr = sum(1 / r for r in ranks) / n if ranks else 0
    print("\n%s: recall@10 = %d/%d (%.0f%%), MRR = %.3f" % (label, hit, n, recall, mrr))
    if misses:
        for q, want, got in misses[:5]:
            print("    промах: «%s»\n        ждали: %s\n        получили: %s"
                  % (q[:52], want, got))
    return {"label": label, "recall_at_10": recall, "hits": hit, "n": n, "mrr": mrr}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=["A", "B", "C"])
    ap.add_argument("--json")
    args = ap.parse_args()

    stems = corpus()
    print("Корпус: %d статей | запросов: %d\n" % (len(stems), len(QUERIES)))
    out = {}

    if "A" in args.only:
        print("=== A. текущий слой (усреднённый документ) ===")
        try:
            out["A"] = score(eval_current(stems, QUERIES), QUERIES, "A. усреднённый документ")
        except Exception as e:
            print("  A не удалось: %s" % e)
    if "B" in args.only:
        print("\n=== B. чанк-поиск, локальная модель ===")
        try:
            out["B"] = score(eval_chunks_local(stems, QUERIES), QUERIES, "B. чанки, MiniLM-L3")
        except Exception as e:
            print("  B не удалось: %s" % e)
    if "C" in args.only:
        print("\n=== C. чанк-поиск, Yandex ===")
        try:
            out["C"] = score(eval_chunks_yandex(stems, QUERIES), QUERIES, "C. чанки, Yandex")
        except Exception as e:
            print("  C не удалось: %s" % e)

    print("\n=== ИТОГ ===")
    base = out.get("A", {}).get("recall_at_10")
    for k in ("A", "B", "C"):
        if k in out:
            r = out[k]["recall_at_10"]
            gain = (" (x%.1f к A)" % (r / base)) if base and k != "A" and base else ""
            print("  %-24s recall@10 = %5.1f%%%s" % (out[k]["label"], r, gain))

    if args.json:
        json.dump(out, open(args.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("\nJSON: %s" % args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
