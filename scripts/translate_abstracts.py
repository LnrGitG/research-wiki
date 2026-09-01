#!/usr/bin/env python3
"""Translate paper abstracts (abstract + intro + conclusion excerpts) EN->RU via Yandex Translate API v2.

Reads raw/papers/*.txt, extracts Abstract/Introduction/Conclusion sections,
translates, writes papers/<slug>.abstract_ru.md + updates data/catalog.yaml
abstract_ru field (if entry has files.md matching).

Usage: python3 scripts/translate_abstracts.py <slug or pdf-name> ...
       python3 scripts/translate_abstracts.py --backfill   # all EN papers missing abstract_ru
"""
import sys, os, re, json, time, csv, urllib.request, urllib.error

BASE = '/home/lnr/research-wiki'
RAW = os.path.join(BASE, 'raw', 'papers')
PAPERS = os.path.join(BASE, 'papers')
CATALOG = os.path.join(BASE, 'data', 'catalog.yaml')

KEY = None
for line in open(os.path.expanduser('~/.hermes/.env')):
    if line.startswith('YANDEX_CLOUD_API_KEY='):
        KEY = line.split('=', 1)[1].strip()
assert KEY, 'YANDEX_CLOUD_API_KEY not found'

API = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
# NOTE: folderId must NOT be sent (400 mismatch with service-account folder)

def translate(texts, target='ru', retries=4):
    """Batch translate; max 10k chars per request. Returns list of strings."""
    out = []
    for chunk_start in range(0, len(texts), 40):
        chunk = texts[chunk_start:chunk_start + 40]
        joined = '\n<<<SEG>>>\n'.join(chunk)
        for attempt in range(retries):
            try:
                body = {"targetLanguageCode": target, "format": "PLAIN_TEXT",
                        "texts": [joined]}
                req = urllib.request.Request(API, data=json.dumps(body).encode(),
                                             headers={'Authorization': f'Api-Key {KEY}',
                                                      'Content-Type': 'application/json'})
                d = json.load(urllib.request.urlopen(req, timeout=60))
                seg = d['translations'][0]['text'].split('\n<<<SEG>>>\n')
                out.extend(seg)
                break
            except (urllib.error.HTTPError, urllib.error.URLError) as e:
                wait = 15 * (attempt + 1)
                print(f'  retry {attempt+1}: {str(e)[:80]}, sleep {wait}s', flush=True)
                time.sleep(wait)
        else:
            out.extend(['[перевод не удался]'] * len(chunk))
        time.sleep(0.3)
    return out

def extract_sections(text):
    """Extract Abstract, Introduction, Conclusion from raw text (last-match wins over TOC)."""
    sections = {}
    t = text
    matches = re.findall(r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*\n(.{200,6000}?)(?:\n\s*(?:JEL|Keywords|KEYWORDS)\b)', t, re.S)
    if not matches:
        # No Abstract heading (Cambridge style): opening paragraphs as proxy
        matches = [t[:3000]]
    if matches:
        # pick the match with most prose-like content (fewest TOC lines)
        def _toc_score(txt):
            lines = [l.strip() for l in txt.splitlines() if l.strip()]
            bad = sum(1 for l in lines if len(l) < 60 or l.endswith('\t') or re.search(r'\t\d+$', l) or l.isdigit())
            return bad / max(len(lines), 1)
        best = min(matches, key=_toc_score)
        sections['Аннотация'] = _strip_toc(best)
    concl = re.findall(r'(?:^|\n)\s*(?:\d+\.?\s+)?(?:Conclusions?|Final comments|Final Remarks|Заключение|Заключительные замечания)\s*\n(.{200,6000}?)(?:\n\s*(?:References|Литература|Appendix|Приложение|Библиография)\b|\Z)', t, re.S | re.I)
    if concl:
        sections['Заключение'] = _strip_toc(concl[-1])
    intro = re.findall(r'(?:^|\n)\s*1\.?\s+(?:Introduction|INTRODUCTION|Введение)\s*\n(.{500,5000}?)(?:\n\s*2\.?\s+[A-ZА-Я]|\n\s*(?:Data and|Данные и)\b)', t, re.S)
    if intro:
        sections['Введение'] = _strip_toc(intro[0])
    return sections

def find_txt_for_slug(slug):
    p = os.path.join(RAW, slug + '.txt')
    if os.path.exists(p):
        return p
    for f in os.listdir(RAW):
        if f.startswith(slug) and f.endswith('.txt'):
            return os.path.join(RAW, f)
    return None

def ru_ratio(s):
    if not s:
        return 0.0
    ru = sum(1 for c in s if '\u0400' <= c <= '\u04FF')
    return ru / max(len(s), 1)

def _strip_toc(sec):
    """Cut leading table-of-contents noise: skip until first long prose line."""
    lines = sec.splitlines()
    for i, l in enumerate(lines):
        ls = l.strip()
        if len(ls) > 60 and not ls.isdigit() and not re.match(r'^\d+[\.\t ]', ls):
            return '\n'.join(lines[i:])
    return sec

def process_slug(slug):
    txt_path = find_txt_for_slug(slug)
    if not txt_path:
        print(f'  no raw txt for {slug}')
        return False
    text = open(txt_path, encoding='utf-8', errors='ignore').read()
    sections = extract_sections(text)
    if not sections:
        print(f'  no sections found in {txt_path}')
        return False
    # Drop leading TOC/page-number noise: keep from first long prose line
    def _strip_toc(sec):
        lines = sec.splitlines()
        for i, l in enumerate(lines):
            ls = l.strip()
            if len(ls) > 60 and not re.match(r'^\d+[\t ]', ls) and not ls.isdigit():
                return '\n'.join(lines[i:])
        return sec
    sections = {k: _strip_toc(v) for k, v in sections.items()}
    names = list(sections.keys())
    translated = translate([sections[n][:6000] for n in names])
    lines = [f'# Машинный перевод ключевых разделов ({slug})', '',
             '> Яндекс.Переводчик, автоматический. Точные значения и коэффициенты — в основном резюме.', '']
    for n, tr in zip(names, translated):
        lines.append(f'## {n}')
        lines.append('')
        lines.append(tr.strip())
        lines.append('')
    out_path = os.path.join(PAPERS, f'{slug}.abstract_ru.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    # QC: cyrillic ratio
    full = '\n'.join(translated)
    rr = ru_ratio(full)
    status = 'OK' if rr > 0.5 else 'LOW-RU-RATIO(!)'
    print(f'  {slug}: {len(sections)} sections, {len(full)} chars, RU {rr:.0%} {status}')
    return rr > 0.5

def backfill():
    """All papers/<slug>.md that have raw txt but no abstract_ru yet and are mostly EN."""
    done, skipped = 0, 0
    for f in sorted(os.listdir(PAPERS)):
        if not f.endswith('.md') or f.endswith('.RU.md') or f.endswith('.abstract_ru.md'):
            continue
        slug = f[:-3]
        if os.path.exists(os.path.join(PAPERS, f'{slug}.abstract_ru.md')):
            skipped += 1
            continue
        txt = find_txt_for_slug(slug)
        if not txt:
            continue
        raw = open(txt, encoding='utf-8', errors='ignore').read()
        if ru_ratio(raw) > 0.5:
            continue  # already RU paper
        if len(raw) < 2000:
            continue
        print(f'[backfill] {slug}', flush=True)
        if process_slug(slug):
            done += 1
        else:
            skipped += 1
    print(f'backfill done: {done} translated, {skipped} skipped')

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args or args[0] == '--backfill':
        backfill()
    else:
        for slug in sys.argv[1:]:
            process_slug(slug)