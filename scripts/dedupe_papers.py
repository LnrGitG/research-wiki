#!/usr/bin/env python3
"""
Удаление дублей md-файлов в papers/ с починкой ссылок.

Дубли возникли из-за двойной конвертации PDF: один и тот же исходник
превращался в два md — старый стиль имени («Имя. Заголовок с пробелами»)
и новый («Имя-Заголовок-через-дефисы»).

Порядок:
  1. Пересчитать группы дублей по нормализованному телу.
  2. Построить карту: удаляемый_stem → канонический_stem.
  3. Починить wikilinks, ссылающиеся на удаляемые файлы.
  4. Удалить файлы.
  5. Отчёт.

Безопасность: сухой прогон по умолчанию; удаление — с --apply.
"""
import os, re, glob, json, hashlib, collections, argparse, shutil, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
os.chdir(REPO)

def split_fm(s):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', s, re.S)
    return (s[m.end():] if m else s)

def body_hash(path):
    s = open(path, encoding='utf-8', errors='replace').read()
    body = split_fm(s)
    norm = re.sub(r'\s+', ' ', re.sub(r'[#*`>\[\]()|_]', ' ', body)).strip().lower()
    return hashlib.sha256(norm.encode()).hexdigest()[:16]

def canon_score(path, size):
    name = os.path.basename(path)
    s = 0.0
    if re.match(r'^[\w-]+\.md$', name, re.UNICODE) and ' ' not in name: s += 10
    if '. ' in name: s -= 5
    if re.match(r'^\d+[.-]', name): s -= 2
    s += min(size / 100000, 3)
    return s

def find_dupes():
    pats = ['papers/**/*.md', 'concepts/*.md', 'queries/*.md', 'reviews/*.md',
            'annotations/*.md', 'entities/*.md', 'comparisons/*.md', 'news/*.md', '*.md']
    files = sorted(set(f for p in pats for f in glob.glob(p, recursive=True) if 'raw/' not in f))
    by = collections.defaultdict(list)
    for f in files:
        try: sz = os.path.getsize(f)
        except Exception: continue
        by[body_hash(f)].append((f, sz))
    kept, dropped = [], []
    for h, g in by.items():
        if len(g) == 1: kept.append(g[0][0]); continue
        g2 = sorted(g, key=lambda x: canon_score(x[0], x[1]), reverse=True)
        kept.append(g2[0][0]); dropped.extend(x[0] for x in g2[1:])
    return kept, dropped

def build_rename(kept, dropped):
    kept_by_hash = {}
    for k in kept: kept_by_hash[body_hash(k)] = k
    ren = {}
    for dp in dropped:
        kp = kept_by_hash.get(body_hash(dp))
        if kp: ren[os.path.splitext(os.path.basename(dp))[0]] = os.path.splitext(os.path.basename(kp))[0]
    return ren

def fix_links(rename, apply=False):
    """Заменить [[...старый_stem...]] на канонический."""
    fixed_files, n_links = 0, 0
    for f in glob.glob('**/*.md', recursive=True):
        if 'raw/' in f or '_archive' in f: continue
        try: s = open(f, encoding='utf-8', errors='replace').read()
        except Exception: continue
        orig = s
        def repl(m):
            nonlocal n_links
            inner, alias = m.group(1), m.group(2) or ''
            parts = inner.split('/')
            stem = parts[-1]
            if stem in rename:
                parts[-1] = rename[stem]
                n_links += 1
                return '[[' + '/'.join(parts) + alias + ']]'
            return m.group(0)
        s = re.sub(r'\[\[([^\]|]+)(\|[^\]]*)?\]\]', repl, s)
        if s != orig:
            fixed_files += 1
            if apply:
                open(f, 'w', encoding='utf-8').write(s)
    return fixed_files, n_links

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='выполнить (по умолчанию сухой прогон)')
    a = ap.parse_args()

    kept, dropped = find_dupes()
    print(f"канонических: {len(kept)} | дублей: {len(dropped)}")
    print(f"объём дублей: {sum(os.path.getsize(p) for p in dropped)/1e6:.1f} МБ")

    rename = build_rename(kept, dropped)
    print(f"карта переименований: {len(rename)} записей")

    ff, nl = fix_links(rename, apply=a.apply)
    print(f"\nссылок починено: {nl} в {ff} файлах {'(ПРИМЕНЕНО)' if a.apply else '(СУХОЙ ПРОГОН)'}")

    if a.apply:
        # бэкап-манифест
        man = REPO / 'data' / 'dupes_removed.json'
        json.dump({
            'removed': dropped, 'kept': kept, 'rename_map': rename,
            'when': datetime.datetime.now().isoformat(),
        }, open(man, 'w'), ensure_ascii=False, indent=1)
        # удаление
        n = 0; freed = 0
        for p in dropped:
            try:
                freed += os.path.getsize(p)
                os.remove(p); n += 1
            except Exception as e:
                print(f"  ! не удалён {p}: {e}")
        print(f"\nудалено файлов: {n}, освобождено: {freed/1e6:.1f} МБ")
        print(f"манифест: {man}")
    else:
        print("\n(сухой прогон — для удаления добавь --apply)")
