#!/usr/bin/env python3
"""Векторный слой на модели Yandex Cloud — чанк-уровень вместо усреднения.

Зачем: текущий слой вики хранит **один усреднённый вектор на документ**
(`doc_emb = np.mean(embs, axis=0)`), поэтому поиск возвращает документ целиком,
а не нужный абзац. Среднее по чанкам стирает локальность: для статьи на 350 КБ
выходит одна точка, одинаково далёкая от запроса про идентификацию шока и про
калибровку модели. Здесь каждый чанк получает свой вектор.

Почему Yandex: корпус преимущественно английский (313 статей), а запросы
русские. Кросс-язычный поиск проверен 19.09 — 3 из 3 попаданий. Модели
**асимметричные**: документ кодируется `text-search-doc`, запрос —
`text-search-query`, что для поиска точнее одного общего энкодера.
Размерность 256 против 384 у прежней `paraphrase-MiniLM-L3-v2`.

Объём и время: около 24 215 чанков по 1000 символов, замерено 0,19 с на
запрос — около 78 минут на весь корпус. Поэтому:

  * **кэш по sha256 текста чанка** — повторный запуск не пересчитывает
    посчитанное, и обрыв не теряет работу;
  * **прогресс пишется после каждой порции** — можно запускать частями;
  * **сбой одного чанка не роняет прогон** — пустой вектор помечается и
    пропускается.

Формат вывода (`data/etl/embeddings-yandex.json`):

    {"model": "text-search-doc", "dim": 256, "built": "<ISO>",
     "docs": {"<stem>": {"chunks": ["<текст>", ...],
                          "vectors": [[...], ...]}}}

Текст чанка хранится рядом с вектором намеренно: без текста вектор
бесполезен для показа результата, а собрать его обратно из статьи
дороже, чем сохранить.

Запуск:  python3 scripts/build_yandex_embeddings.py              # инкремент
         python3 scripts/build_yandex_embeddings.py --rebuild     # с нуля
         python3 scripts/build_yandex_embeddings.py --only paper  # один стем
         python3 scripts/build_yandex_embeddings.py --limit 40    # проба
         python3 scripts/build_yandex_embeddings.py --status      # прогресс
"""
import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))

# ID КАТАЛОГА, не облака: в ~/.hermes/.env лежит YANDEX_CLOUD_ID с ID облака,
# при его использовании API отвечает «folder does not match service account».
FOLDER = "b1gpe14c599s44v5dacm"
API = "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding"

# Лимит входа по замерам: 8 000 символов проходят, 20 000 отвергаются.
MAX_INPUT = 4000
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

ART = os.path.join(REPO, "data", "etl", "embeddings-yandex.json")
CACHE = os.path.join(REPO, "data", "etl", "yandex-embed-cache.json")


def log(m):
    print(m, flush=True)


def api_key():
    for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8"):
        if line.startswith("YANDEX_CLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("YANDEX_CLOUD_API_KEY не найден в ~/.hermes/.env")


KEY = None


def embed(text, kind="doc", retries=3):
    """Один вызов API. Пустой список при неудаче — вызывающий пропустит."""
    global KEY
    if KEY is None:
        KEY = api_key()
    body = json.dumps({"modelUri": "emb://%s/text-search-%s/latest" % (FOLDER, kind),
                       "text": text[:MAX_INPUT]}, ensure_ascii=False)
    for attempt in range(retries):
        r = subprocess.run(["curl", "-s", "-m", "40", "-X", "POST", API,
                            "-H", "Authorization: Api-Key %s" % KEY,
                            "-H", "Content-Type: application/json",
                            "--data-binary", "@-"],
                           input=body, capture_output=True, text=True)
        try:
            v = json.loads(r.stdout).get("embedding")
            if v:
                return v
        except (json.JSONDecodeError, AttributeError):
            pass
        # мягкий ретрай: rate limit и сетевые сбои лечатся паузой
        time.sleep(1.5 * (attempt + 1))
    return []


def body_of(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    if s.startswith("---") and s.count("---") >= 2:
        return s.split("---", 2)[2]
    return s


def chunks_of(path):
    t = body_of(path)
    if len(t) <= CHUNK_SIZE:
        return [t] if t.strip() else []
    out, i = [], 0
    while i < len(t):
        c = t[i:i + CHUNK_SIZE]
        if c.strip():
            out.append(c)
        i += CHUNK_SIZE - CHUNK_OVERLAP
    return out


def text_hash(t):
    return hashlib.sha256(t.encode("utf-8", "ignore")).hexdigest()[:24]


def load_json(p, default):
    if not os.path.exists(p):
        return default
    try:
        return json.load(open(p, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def save_json(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    json.dump(obj, open(tmp, "w", encoding="utf-8"), ensure_ascii=False)
    os.replace(tmp, p)


def list_papers():
    """Статьи корпуса + записки и переводы — как в прежнем слое вики."""
    import glob
    out = []
    for pat, kind in (("papers/*.md", "paper"),
                      ("papers/ru_papers/*.md", "paper_ru"),
                      ("queries/*.md", "query")):
        for p in sorted(glob.glob(pat)):
            out.append((os.path.basename(p)[:-3], p, kind))
    return out


def status():
    art = load_json(ART, {})
    cache = load_json(CACHE, {})
    docs = art.get("docs", {})
    n_chunks = sum(len(d.get("chunks", [])) for d in docs.values())
    n_vec = sum(len(d.get("vectors", [])) for d in docs.values())
    log("Слой: %s" % ART)
    if docs:
        log("  документов: %d | чанков: %d | векторов: %d | dim: %s"
            % (len(docs), n_chunks, n_vec, art.get("dim")))
        log("  построен: %s" % art.get("built", "?"))
    else:
        log("  слой пуст")
    log("  кэш векторов: %d записей (%.1f МБ)"
        % (len(cache), os.path.getsize(CACHE) / 1e6 if os.path.exists(CACHE) else 0))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true", help="игнорировать слой и кэш")
    ap.add_argument("--only", nargs="*", default=None, help="только эти стемы")
    ap.add_argument("--limit", type=int, default=0, help="обработать N документов (проба)")
    ap.add_argument("--force", action="store_true",
                    help="пересобрать выбранные документы, даже если число чанков совпало (текст мог измениться)")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    if args.status:
        return status()

    t0 = time.time()
    papers = list_papers()
    if args.only:
        want = set(args.only)
        papers = [x for x in papers if x[0] in want]

    art = {} if args.rebuild else load_json(ART, {})
    docs = art.get("docs", {})
    cache = {} if args.rebuild else load_json(CACHE, {})

    # что уже сделано: документ есть и векторов столько же, сколько чанков
    todo = []
    for stem, path, kind in papers:
        ch = chunks_of(path)
        prev = docs.get(stem)
        if prev and len(prev.get("vectors", [])) == len(ch) and not args.rebuild and not args.force:
            continue
        todo.append((stem, path, kind, ch))
    if args.limit:
        todo = todo[:args.limit]

    total_chunks = sum(len(x[3]) for x in todo)
    fresh = sum(1 for _, _, _, ch in todo for c in ch if text_hash(c) not in cache)
    log("Документов к обработке: %d | чанков: %d | новых вызовов API: %d"
        % (len(todo), total_chunks, fresh))
    log("Оценка времени новых вызовов: %.1f мин (0,19 с/шт)" % (fresh * 0.19 / 60))
    if not todo:
        log("Всё уже посчитано — нечего делать.")
        return status()

    done_calls = 0
    for idx, (stem, path, kind, ch) in enumerate(todo, 1):
        vecs = []
        for c in ch:
            h = text_hash(c)
            v = cache.get(h)
            if not v:
                v = embed(c, "doc")
                done_calls += 1
                if v:
                    cache[h] = v
                if done_calls % 25 == 0:
                    save_json(CACHE, cache)     # прогресс не теряется при обрыве
            vecs.append(v or [])
        docs[stem] = {"path": path, "kind": kind, "chunks": ch, "vectors": vecs}
        if idx % 10 == 0 or idx == len(todo):
            save_json(CACHE, cache)
            art["docs"] = docs
            art["model"] = "text-search-doc"
            art["dim"] = 256
            art["built"] = time.strftime("%Y-%m-%dT%H:%M:%S")
            save_json(ART, art)
            log("  [%d/%d] %s — чанков %d, вызовов всего %d, прошло %.1f мин"
                % (idx, len(todo), stem[:40], len(ch), done_calls, (time.time()-t0)/60))

    save_json(CACHE, cache)
    art["docs"] = docs
    art["model"] = "text-search-doc"
    art["dim"] = 256
    art["kind"] = "chunk-level"
    art["built"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    save_json(ART, art)

    log("\nГотово: документов %d, чанков %d, вызовов API %d, время %.1f мин"
        % (len(docs), sum(len(d.get("chunks", [])) for d in docs.values()),
           done_calls, (time.time()-t0)/60))
    log("Слой: %s (%.1f МБ)" % (ART, os.path.getsize(ART)/1e6))
    return 0


if __name__ == "__main__":
    sys.exit(main())
