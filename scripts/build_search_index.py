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

# ── 1. Стеммер для русского (упрощённый Snowball) ────────────────────
# Полный Snowball для русского ~500 строк; здесь — практичная версия,
# покрывающая основные падежные окончания. Даёт recall без потери точности.
VOWELS = 'аеиоуыэюя'
PERFECTIVE_GERUND = ('вшись', 'вши', 'в', 'вся')
ADJECTIVE = ('ее', 'ие', 'ые', 'ое', 'ими', 'ыми', 'ей', 'ий', 'ый', 'ой',
             'ем', 'им', 'ым', 'ом', 'его', 'ого', 'ему', 'ому', 'их', 'ых',
             'ую', 'юю', 'ая', 'яя', 'ою', 'ею')
PARTICIPLE = ('ем', 'нн', 'вш', 'ющ', 'щ')
VERB = ('ила', 'ыла', 'ена', 'ейте', 'уйте', 'ите', 'или', 'ыли', 'ей',
        'уй', 'ил', 'ыл', 'им', 'ым', 'ен', 'ило', 'ыло', 'ено', 'ят',
        'ует', 'уют', 'ит', 'ыт', 'ены', 'ить', 'ыть', 'ишь', 'ую', 'ю')
NOUN = ('а', 'ев', 'ов', 'ие', 'ье', 'е', 'иями', 'ями', 'ами', 'еи', 'ии',
        'и', 'ией', 'ей', 'ой', 'ий', 'й', 'иям', 'ям', 'ием', 'ем', 'ам',
        'ом', 'о', 'у', 'ах', 'иях', 'ях', 'ы', 'ь', 'ию', 'ью', 'ю', 'ия',
        'ья', 'я')
SUPERLATIVE = ('ейш', 'ейше')
DERIVATIONAL = ('ост', 'ость')

def stem(word: str) -> str:
    """Упрощённый стеммер для русского + английского."""
    if not word: return word
    w = word.lower()
    # английский: простой суффиксный стеммер
    if re.fullmatch(r'[a-z]+', w):
        for suf in ('ingly','edly','ing','ed','ies','es','s'):
            if len(w) > len(suf) + 2 and w.endswith(suf):
                return w[:-len(suf)]
        return w
    if not re.fullmatch(r'[а-яё]+', w): return w
    if len(w) <= 3: return w
    # убираем мягкий знак и й в конце (частично)
    w = re.sub(r'[йь]$', '', w) if len(w) > 4 else w
    # прилагательные/причастия
    for suf in ADJECTIVE:
        if w.endswith(suf) and len(w) > len(suf) + 3:
            w = w[:-len(suf)]; break
    # глаголы
    for suf in VERB:
        if w.endswith(suf) and len(w) > len(suf) + 4:
            w = w[:-len(suf)]; break
    # существительные
    for suf in NOUN:
        if w.endswith(suf) and len(w) > len(suf) + 3:
            w = w[:-len(suf)]; break
    # усечение длинных «хвостов» (ость, ост)
    for suf in DERIVATIONAL:
        if w.endswith(suf) and len(w) > len(suf) + 4:
            w = w[:-len(suf)]; break
    return w

TOKEN_RE = re.compile(r'[а-яёa-z]{3,}')

def tokenize(text: str):
    """-> список стеммов"""
    return [stem(t) for t in TOKEN_RE.findall(text.lower())]

# ── 2. Сбор документов ───────────────────────────────────────────────
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
        docs.append({
            'path': f,
            'title': str(fm.get('title') or '').strip() or _first_heading(body) or os.path.basename(f),
            'cat': cat,
            'body': body,
            'norm_hash': hashlib.sha256(norm.encode()).hexdigest()[:16],
            'size': len(raw),
            'source_pdf': str(fm.get('source_pdf') or fm.get('local_path') or ''),
            'year': str(fm.get('year') or fm.get('date') or ''),
            'authors': fm.get('authors') or fm.get('author') or '',
        })
    return docs

def _first_heading(body):
    for line in body.splitlines():
        line = line.strip()
        if line.startswith('#'):
            return re.sub(r'^#+\s*', '', line).strip()
    return ''

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
    print("\nГотово. Список дедупликации: data/search_dedupe.json")
