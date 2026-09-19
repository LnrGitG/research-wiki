#!/usr/bin/env python3
"""Поиск по чанк-слою Yandex: находит ФРАГМЕНТ, а не документ целиком.

Отличие от прежнего поиска вики: тот возвращал документ (один усреднённый
вектор на файл), здесь возвращается конкретный фрагмент текста с указанием
статьи и позиции. Это и есть смысл перехода на чанк-уровень.

Запрос кодируется моделью `text-search-query`, документ — `text-search-doc`.
Асимметричность важна: Yandex обучал эти модели парно, и смешивать их
стороны нельзя — при кодировании запроса моделью для документов точность
падает.

Примеры:

    python3 scripts/yandex_chunk_search.py "передача шока ставки в цены жилья"
    python3 scripts/yandex_chunk_search.py "эластичность предложения" -k 5
    python3 scripts/yandex_chunk_search.py --doc saiz-2010 "цена земли"
    python3 scripts/yandex_chunk_search.py "энтропийное наклонение" --full
"""
import argparse
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

FOLDER = "b1gpe14c599s44v5dacm"
API = "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding"
ART = os.path.join(REPO, "data", "etl", "embeddings-yandex.json")


def api_key():
    for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("YANDEX_CLOUD_API_KEY не найден")


def embed_query(text):
    body = json.dumps({"modelUri": "emb://%s/text-search-query/latest" % FOLDER,
                       "text": text[:4000]}, ensure_ascii=False)
    r = subprocess.run(["curl", "-s", "-m", "40", "-X", "POST", API,
                        "-H", "Authorization: Api-Key %s" % api_key(),
                        "-H", "Content-Type: application/json",
                        "--data-binary", "@-"],
                       input=body, capture_output=True, text=True)
    try:
        return json.loads(r.stdout).get("embedding", [])
    except json.JSONDecodeError:
        return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-k", type=int, default=8, help="сколько фрагментов показать")
    ap.add_argument("--doc", default=None, help="искать только в этом документе")
    ap.add_argument("--full", action="store_true", help="показать фрагмент целиком")
    ap.add_argument("--max-per-doc", type=int, default=2,
                    help="не больше N фрагментов из одной статьи")
    args = ap.parse_args()

    if not os.path.exists(ART):
        raise SystemExit("Слой не построен: %s. Запустите build_yandex_embeddings.py" % ART)
    art = json.load(open(ART, encoding="utf-8"))
    docs = art.get("docs", {})
    if not docs:
        raise SystemExit("Слой пуст")

    import numpy as np
    qv = np.asarray(embed_query(args.query), dtype=np.float32)
    if qv.size == 0:
        raise SystemExit("Не удалось получить вектор запроса")

    hits = []
    for stem, d in docs.items():
        if args.doc and args.doc not in stem:
            continue
        for i, (chunk, vec) in enumerate(zip(d.get("chunks", []), d.get("vectors", []))):
            if not vec:
                continue
            v = np.asarray(vec, dtype=np.float32)
            # векторы нормированы, поэтому косинус = скалярное произведение
            hits.append((float(qv @ v), stem, i, chunk))
    if not hits:
        print("Ничего не найдено.")
        return 0

    hits.sort(key=lambda x: -x[0])

    # ограничение на число фрагментов из одной статьи: иначе топ заполняется
    # одной длинной работой и теряется обзор корпуса
    picked, per_doc = [], {}
    for h in hits:
        c = per_doc.get(h[1], 0)
        if c >= args.max_per_doc:
            continue
        picked.append(h)
        per_doc[h[1]] = c + 1
        if len(picked) >= args.k:
            break

    n_docs = len(set(h[1] for h in hits))
    print("Запрос: «%s»" % args.query)
    print("Пространство поиска: %d документов, %d фрагментов\n" % (n_docs, len(hits)))
    for score, stem, idx, chunk in picked:
        text = chunk if args.full else chunk[:320].replace("\n", " ")
        print("%.3f  %s  [фрагмент %d]" % (score, stem[:58], idx))
        print("       %s%s\n" % (text.strip(), "…" if not args.full and len(chunk) > 320 else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
