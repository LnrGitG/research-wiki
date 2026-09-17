#!/usr/bin/env python3
"""
Построение полнотекстового поискового индекса для research-wiki.

Что делает:
  1. Собирает все md-страницы (papers/, concepts/, queries/, reviews/, ...).
  2. Дедуплицирует: один PDF, сконвертированный дважды, даёт два md —
     оставляем канонический экземпляр.
  3. Токенизирует с русским стеммингом, строит инвертированный индекс.
  4. Сохраняет: индекс (термин → документы+частоты) и корпус абзацев
     (для сниппетов). Оба — сжатые gzip.

Формат вывода (docs/):
  search-index.json.gz  — {meta, docs, terms}
  search-corpus.json.gz — массив абзацев для сниппетов

Запуск: python3 scripts/build_search_index.py
"""
import os, re, glob, gzip, json, hashlib, collections, yaml
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
os.chdir(REPO)
OUT = REPO / "docs"

# ── 1. Лемматизация через pymorphy3 ──────────────────────────────────
# pymorphy3 даёт одинаковую нормальную форму для всех словоформ
# («предложения» и «предложение» → «предложение»), чего самодельный
# стеммер не обеспечивал. Словарь форм→лемм выгружается на клиент,
# чтобы браузер лемматизировал запрос тем же способом.
import pymorphy3
_MORPH = pymorphy3.MorphAnalyzer()
_LEMMA_CACHE = {}

def lemma(word: str) -> str:
    """Нормальная форма слова. Английский — без изменений (кроме -s)."""
    w = word.lower()
    if re.fullmatch(r'[a-z]+', w):
        # англ.: лёгкий суффиксный стемминг
        for suf in ('ingly', 'edly', 'ing', 'ed', 'ies', 'es', 's'):
            if len(w) > len(suf) + 2 and w.endswith(suf):
                return w[:-len(suf)]
        return w
    if not re.fullmatch(r'[а-яё]+', w):
        return w
    l = _LEMMA_CACHE.get(w)
    if l is None:
        l = _MORPH.parse(w)[0].normal_form
        _LEMMA_CACHE[w] = l
    return l

def stem(word: str) -> str:
    """Совместимость: синоним lemma()."""
    return lemma(word)

TOKEN_RE = re.compile(r'[а-яёa-z]{3,}')

def tokenize(text: str):
    """-> список лемм"""
    return [lemma(t) for t in TOKEN_RE.findall(text.lower())]

# ── 2. Сбор документов ───────────────────────────────────────────────

def _clean_title(t: str) -> str:
    """Убрать markdown-разметку, HTML, сноски из заголовка."""
    t = re.sub(r'<[^>]+>', '', t)                  # HTML-теги
    t = re.sub(r'[*_~`>]+', '', t)                 # markdown-выделение
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t) # ссылки
    t = re.sub(r'^#+\s*', '', t)                   # решётки
    t = re.sub(r'<sup>.*?</sup>', '', t)
    t = re.sub(r'\s+', ' ', t).strip(' .,;:—-')
    return t

# служебные шапки, которые не годятся в заголовок
_JUNK = re.compile(
    r'^(УДК|ББК|JEL|DOI|СЕРИЯ|NBER|Working\s+Paper|Рабочий\s+документ|'
    r'ОРИГИНАЛЬНАЯ\s+СТАТЬЯ|Резюме|Abstract|Аннотация|Препринт|Preprint|'
    r'Research\s+Paper|Discussion\s+Paper|Staff\s+Report|'
    r'[А-Я\s\-]{18,}$)'                       # сплошной капс длиннее 18
, re.I)

def _first_heading(body: str) -> str:
    """Первый осмысленный заголовок: пропускает служебные шапки."""
    for line in body.splitlines()[:80]:
        line = line.strip()
        if not line.startswith('#'):
            continue
        t = _clean_title(line)
        if not t or len(t) < 8:
            continue
        if _JUNK.match(t):
            continue
        return t
    return ''

def _looks_like_filename(t: str) -> bool:
    return bool(re.search(r'\.(md|pdf|RU|RU\.md)$', t, re.I)) or bool(re.match(r'^[\w\-]{25,}$', t))

def _fallback_title(path: str) -> str:
    """Человекочитаемое имя из имени файла, если заголовка нет."""
    n = os.path.basename(path)
    n = re.sub(r'\.(RU\.)?md$', '', n, flags=re.I)
    n = n.replace('-', ' ').replace('_', ' ').strip()
    # убираем ведущие номера и «Копия -»
    n = re.sub(r'^(копия\s*[-–]\s*|\d+[.\s]+)', '', n, flags=re.I)
    return n[:120] if n else os.path.basename(path)

def split_frontmatter(s):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', s, re.S)
    if m:
        try: fm = yaml.safe_load(m.group(1)) or {}
        except: fm = {}
        return fm, s[m.end():]
    return {}, s

def collect():
    pats = ['papers/**/*.md', 'concepts/*.md', 'queries/*.md', 'reviews/*.md',
            'annotations/*.md', 'entities/*.md', 'comparisons/*.md', 'news/*.md',
            'templates/*.md', '*.md']
    files = []
    for p in pats:
        files += glob.glob(p, recursive=True)
    files = sorted(set(f for f in files if 'raw/' not in f and not f.startswith('_archive')))

    docs = []
    for f in files:
        try: raw = open(f, encoding='utf-8', errors='replace').read()
        except Exception: continue
        fm, body = split_frontmatter(raw)
        # тип документа
        cat = 'paper' if f.startswith('papers/ru_papers') else (
              'paper' if f.startswith('papers/') else
              'query' if f.startswith('queries/') else
              'concept' if f.startswith('concepts/') else
              'review' if f.startswith('reviews/') else
              'entity' if f.startswith('entities/') else
              'other')
        # нормализованное тело для сравнения дублей
        norm = re.sub(r'\s+', ' ', re.sub(r'[#*`>\[\]()|_]', ' ', body)).strip().lower()
        # заголовок: frontmatter → первый осмысленный заголовок → имя файла
        title = _clean_title(str(fm.get('title') or ''))
        if not title or len(title) < 8 or _looks_like_filename(title) or _JUNK.match(title):
            title = _first_heading(body)
        if not title:
            title = _fallback_title(f)
        docs.append({
            'path': f,
            'title': title,
            'cat': cat,
            'body': body,
            'norm_hash': hashlib.sha256(norm.encode()).hexdigest()[:16],
            'size': len(raw),
            'source_pdf': str(fm.get('source_pdf') or fm.get('local_path') or ''),
            'year': str(fm.get('year') or fm.get('date') or ''),
            'authors': fm.get('authors') or fm.get('author') or '',
        })
    return docs

# ── 3. Дедупликация ──────────────────────────────────────────────────
def canon_score(d):
    """Который из дублей оставить: нормализованные имена > старый стиль."""
    name = os.path.basename(d['path'])
    s = 0.0
    if re.match(r'^[\w-]+\.md$', name, re.UNICODE) and ' ' not in name: s += 10
    if '. ' in name: s -= 5
    if re.match(r'^\d+[.-]', name): s -= 2
    s += min(d['size'] / 100000, 3)
    return s

def dedupe(docs):
    by_hash = collections.defaultdict(list)
    for d in docs: by_hash[d['norm_hash']].append(d)
    canon, dropped = [], []
    for h, group in by_hash.items():
        if len(group) == 1:
            canon.append(group[0]); continue
        g = sorted(group, key=canon_score, reverse=True)
        canon.append(g[0]); dropped.extend(g[1:])
    return canon, dropped

# ── 4. Индекс и корпус ───────────────────────────────────────────────
def build_index(docs):
    # абзацы для сниппетов
    corpus = []          # corpus[doc_i] = [абзац1, абзац2, ...]
    term_index = collections.defaultdict(lambda: collections.defaultdict(int))
    # term -> {doc_i: tf}

    for i, d in enumerate(docs):
        body = d['body']
        # абзацы: разделители — пустые строки; режем слишком длинные
        paras = []
        for p in re.split(r'\n\s*\n', body):
            p = ' '.join(p.split())
            if not p: continue
            if len(p) > 1200:  # длинные режем по предложениям
                sents = re.split(r'(?<=[.!?])\s+', p)
                cur = ''
                for s in sents:
                    if len(cur) + len(s) > 1000:
                        if cur: paras.append(cur)
                        cur = s
                    else: cur = (cur + ' ' + s).strip()
                if cur: paras.append(cur)
            else:
                paras.append(p)
        corpus.append(paras[:200])   # не больше 200 абзацев на документ

        for pi, para in enumerate(paras[:200]):
            toks = tokenize(para)
            for t in set(toks):
                term_index[t][i] += 1

    # в разреженный вид: term -> [[doc_i, tf], ...] отсортировано
    terms = {}
    for t, m in term_index.items():
        lst = sorted(m.items())
        terms[t] = lst
    # метаданные документов
    meta_docs = [{
        'p': d['path'], 't': d['title'][:160], 'c': d['cat'],
        'y': d['year'][:12], 'a': str(d['authors'])[:80] if d['authors'] else '',
        'n': len(corpus[i]),
    } for i, d in enumerate(docs)]
    return terms, corpus, meta_docs

# ── 5. main ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Сбор документов...")
    docs = collect()
    print(f"  найдено md: {len(docs)}")

    print("Дедупликация...")
    canon, dropped = dedupe(docs)
    print(f"  канонических: {len(canon)} | отброшено дублей: {len(dropped)}")
    print(f"  объём отброшенного: {sum(d['size'] for d in dropped)/1e6:.1f} МБ")

    print("Построение индекса...")
    terms, corpus, meta_docs = build_index(canon)
    print(f"  терминов: {len(terms):,}")
    print(f"  документов: {len(meta_docs)}")
    total_paras = sum(len(c) for c in corpus)
    print(f"  абзацев: {total_paras:,}")

    OUT.mkdir(exist_ok=True)
    # индекс
    idx = {
        'meta': {
            'built': __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M'),
            'docs': len(meta_docs), 'terms': len(terms),
            'deduped': len(dropped), 'generator': 'build_search_index.py',
        },
        'docs': meta_docs,
        'terms': terms,
    }
    p1 = OUT / 'search-index.json.gz'
    with gzip.open(p1, 'wt', encoding='utf-8', compresslevel=9) as f:
        json.dump(idx, f, ensure_ascii=False, separators=(',', ':'))
    # корпус абзацев
    p2 = OUT / 'search-corpus.json.gz'
    with gzip.open(p2, 'wt', encoding='utf-8', compresslevel=9) as f:
        json.dump(corpus, f, ensure_ascii=False, separators=(',', ':'))

    for p in (p1, p2):
        print(f"  {p.name}: {p.stat().st_size/1e6:.2f} МБ")

    # сохранём список дублей для отчёта
    json.dump({'kept': [d['path'] for d in canon],
               'dropped': [d['path'] for d in dropped]},
              open(REPO/'data/search_dedupe.json','w'), ensure_ascii=False, indent=1)

    # ── 6. Словарь форм→лемм для клиента ────────────────────────────
    # Браузер не имеет pymorphy3, поэтому отдаём ему отображение
    # «словоформа → лемма», чтобы запрос лемматизировался одинаково
    # с индексом. Хранится только то, что реально меняется.
    print("\nСловарь форм→лемм...")
    forms = set()
    for d in canon:
        forms.update(t.lower() for t in TOKEN_RE.findall(d['body']))
    fmap = {}
    for w in forms:
        l = lemma(w)
        if l != w:
            fmap[w] = l
    p3 = OUT / 'search-lemmas.json.gz'
    with gzip.open(p3, 'wt', encoding='utf-8', compresslevel=9) as f:
        json.dump(fmap, f, ensure_ascii=False, separators=(',', ':'))
    print(f"  пар: {len(fmap):,} | {p3.name}: {p3.stat().st_size/1e6:.3f} МБ")

    print("\nГотово. Список дедупликации: data/search_dedupe.json")
