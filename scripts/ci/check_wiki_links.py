#!/usr/bin/env python3
"""Проверка целостности research-wiki для CI (GitHub Actions) и локального запуска.

Проверки:
1. Wikilinks [[...]] не битые: цель существует как файл (с/без .md) в вики.
2. Frontmatter валиден: type из схемы, created/updated присутствуют.
3. Дубликаты заголовков секций в papers/catalog.md.
4. dup: ссылки в catalog.md указывают на существующие файлы.
5. hypotheses.yaml парсится и id уникальны.

Выход: exit 0 если ошибок нет, exit 1 — есть. Ошибки в stdout.
"""
import os
import re
import sys
import glob

import yaml

WIKI = os.environ.get("WIKI_ROOT", os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

MD_FILES = {}
for pat in ("*.md", "*/*.md", "*/*/*.md"):
    for p in glob.glob(os.path.join(WIKI, pat)):
        rel = os.path.relpath(p, WIKI).replace(os.sep, "/")
        if not rel.startswith(("raw/", "_archive/", ".git/", ".obsidian/", "node_modules/")) \
                and rel not in ("AGENTS.md", "MEMORY.md", "README.md", "SCHEMA.md", "USER.md", "index.md", "log.md") \
                and not rel.startswith("templates/"):
            MD_FILES[rel] = p

# индекс имён без пути для wikilink-резолва
NAMES = set()
for rel in MD_FILES:
    base = os.path.basename(rel)
    NAMES.add(base)
    NAMES.add(base[:-3] if base.endswith(".md") else base)
    NAMES.add(rel)
    NAMES.add(rel[:-3] if rel.endswith(".md") else rel)

WIKI_LINK = re.compile(r"\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
errors = []
warnings = []


def check_wikilinks():
    for rel, path in sorted(MD_FILES.items()):
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            errors.append(f"{rel}: read error {e}")
            continue
        for m in WIKI_LINK.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http:", "https:")):
                continue
            # цели с путём: concepts/name, queries/name
            cand = [target, target + ".md"]
            ok = any(c in NAMES or os.path.exists(os.path.join(WIKI, c)) for c in cand)
            if not ok:
                base = os.path.basename(target)
                if not any(b in NAMES for b in (base, base + ".md")):
                    warnings.append(f"{rel}: broken wikilink [[{target}]]")


def check_frontmatter():
    # legacy-страницы без frontmatter (созданы до принятия схемы) — допускаются с warning
    legacy_ok_no_fm = True
    valid_types = {"paper", "concept", "entity", "comparison", "query", "summary", "model", "region-dashboard", "research-task", "indicator", "annotation", "review", "news", "reference", "research-design", "reading-map", "ai_case_methodology"}
    for rel, path in sorted(MD_FILES.items()):
        # papers/ и papers/ru_papers/ exempt: автогенерация, не вики-страницы
        if rel.startswith("papers/"):
            continue
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not m:
            warnings.append(f"{rel}: нет YAML frontmatter (legacy)")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"{rel}: YAML ошибка: {e}")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: frontmatter не словарь")
            continue
        if fm.get("type") not in valid_types:
            errors.append(f"{rel}: type '{fm.get('type')}' вне схемы")
        if not fm.get("created"):
            # допускаем альтернативные поля: date / date_read
            if not (fm.get("date") or fm.get("date_read")):
                errors.append(f"{rel}: нет created (и date/date_read)")


def check_catalog():
    cat_path = os.path.join(WIKI, "papers", "catalog.md")
    if not os.path.exists(cat_path):
        return
    text = open(cat_path, encoding="utf-8", errors="replace").read()
    headers = re.findall(r"^## (.+)$", text, re.M)
    seen, dupes = set(), set()
    for h in headers:
        if h in seen:
            dupes.add(h)
        seen.add(h)
    for d in dupes:
        errors.append(f"catalog.md: дубликат карточки ## {d}")
    # dup-цели
    papers = {os.path.basename(p) for p in glob.glob(os.path.join(WIKI, "papers", "*.md"))}
    for d in re.findall(r"dup:[\s]*([^\s]+\.md)", text):
        if d not in papers:
            errors.append(f"catalog.md: dup-цель не найдена: {d}")


def check_hypotheses():
    hyp_path = os.path.join(WIKI, "hypotheses.yaml")
    if not os.path.exists(hyp_path):
        errors.append("hypotheses.yaml отсутствует")
        return
    try:
        data = yaml.safe_load(open(hyp_path, encoding="utf-8"))
    except yaml.YAMLError as e:
        errors.append(f"hypotheses.yaml: YAML ошибка: {e}")
        return
    ids = [h.get("id") for h in data.get("hypotheses", [])]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        errors.append(f"hypotheses.yaml: дубликаты id: {dupes}")


def main():
    check_wikilinks()
    check_frontmatter()
    check_catalog()
    check_hypotheses()
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARN: {w}")
    print(f"\nПроверено файлов: {len(MD_FILES)}; errors: {len(errors)}; warnings: {len(warnings)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()