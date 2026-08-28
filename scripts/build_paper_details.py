#!/usr/bin/env python3
"""Build docs/paper-details.json: metadata for the vector-search detail modal.

For each indexed document (papers, RU papers, queries) extract:
- title (RU title when catalog entry matches, else from frontmatter)
- authors, year, venue/journal, url (original source)
- abstract / key findings (first Abstract section, trimmed)
- data sources mentioned (Data section keywords), econometric models (regex on body)
- tags (from catalog.yaml by id, else from frontmatter tags)
- viewer URL (relative viewer.html?p=...)
- catalog id (when matched) for the "открыть карточку" link

Output: docs/paper-details.json keyed by viewer path (the same key vector-search uses).
"""
import glob
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "docs/paper-details.json")

# econometric / model keywords (EN + RU)
MODEL_PATTERNS = [
    ("hedonic", r"гедоническ|hedonic"),
    ("repeat-sales", r"repeat.sales|повторных продаж"),
    ("supply-elasticity", r"elasticity of (housing )?supply|эластичност.*предложен"),
    ("panel", r"panel (data|regression|model)|панельн"),
    ("IV", r"instrumental variable|инструментальн"),
    ("DiD", r"difference-in-difference|разность разностей|diff-in-diff"),
    ("RDD", r"regression discontinuity|разрыв"),
    ("VAR/FAVAR", r"\bFAVAR\b|\bVAR\b|факторн.*векторн"),
    ("MIDAS", r"\bMIDAS\b"),
    ("DSGE", r"\bDSGE\b"),
    ("ARDL", r"\bARDL\b"),
    ("PCA", r"principal component|главных компонент|\bPCA\b"),
    ("machine-learning", r"machine learning|машинн.*обучен|random forest|gradient boosting"),
    ("simulation", r"calibration|калибровк|simulation|имитац"),
    ("event-study", r"event study|событийный"),
    ("GARCH", r"GARCH"),
    ("spatial-econometrics", r"spatial (lag|error|Durbin)|пространственн.*эконометр"),
    ("Bayesian", r"Bayesian|байесовск"),
    ("timeseries-filters", r"Hodrick-Prescott|\bHP filter\b|Kalman|фильтр Калман"),
    ("structural-model", r"structural model|структурн.*модел"),
]

# data source keywords (EN + RU)
DATA_PATTERNS = [
    ("Rosstat", r"Росстат|Rosstat"),
    ("CBR", r"Центральн\w+ банк|Банк России|ЦБ РФ|\bCBR\b|Central Bank of Russia"),
    ("ЕИСЖС", r"ЕИСЖС|Единая информационная система жилищного строительства|naideno наш дом|наш\.дом\.рф"),
    ("ДОМ.РФ", r"ДОМ\.РФ|Dom\.RF"),
    ("Rosreestr", r"Росреестр|Rosreestr"),
    ("ACS/перепись", r"American Community Survey|ACS\b"),
    ("census", r"census|перепис"),
    ("FHFA", r"FHFA"),
    ("Zillow", r"Zillow"),
    ("CoreLogic", r"CoreLogic"),
    ("LiBO", r"Credit Bureau|кредитных историй|БКИ"),
    ("SPARK", r"СПАРК|SPARK"),
    ("ЕМИСС", r"ЕМИСС|EMISS"),
    ("NOSTROY", r"НОСТРОЙ|NOSTROY"),
    ("GDELT", r"GDELT"),
    ("Wordstat", r"Wordstat|Вордстат|Yandex Wordstat"),
    ("Google Trends", r"Google Trends"),
    ("admin-data", r"administrative data|административн.*данн"),
    ("survey-data", r"survey|опросн|обследован"),
    ("geospatial", r"GIS|геопространственн|satellite|спутников|OpenStreetMap"),
]

# Sections that carry abstract / findings
ABS_HEADERS = re.compile(
    r"^#{1,3}\s*\**\s*(abstract|аннотация|ключевые (выводы|положения)|key (contributions|findings)|non-technical summary|executive summary|основные (выводы|результаты))\b.*$",
    re.M | re.I,
)
SECTION_RE = re.compile(r"^#{1,3} .*$(.*?)^(?=#{1,3} |\Z)", re.M | re.S)


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return {}, text
    fm_text = text[3:end]
    body = text[end + 4:]
    fm = {}
    # lenient key: scalar-or-list extraction
    lines = fm_text.split("\n")
    key = None
    for ln in lines:
        m = re.match(r"^([A-Za-zА-Яа-я_][\w -]*):(.*)$", ln)
        if m and not ln.startswith((" ", "\t")):
            key = m.group(1).strip().lower().replace(" ", "_")
            rest = m.group(2).strip()
            if rest:
                fm[key] = rest.strip("\"'* ")
            else:
                fm[key] = []
        elif key is not None and ln.startswith(("  - ", "- ")):
            v = ln.strip().lstrip("- ").strip()
            if v:
                if isinstance(fm.get(key), list):
                    fm[key].append(v.strip("\"*"))
                else:
                    fm[key] = [fm[key], v.strip("\"'* ")]
        elif key is not None and ln.startswith(" ") and fm.get(key) == []:
            fm[key] = ln.strip()
    return fm, body


def first_section(body, header_re):
    m = header_re.search(body)
    if not m:
        return ""
    nxt = re.compile(r"^#{1,3} ", re.M)
    start = m.end()
    m2 = nxt.search(body, start)
    seg = body[start:m2.start() if m2 else start + 3000]
    return re.sub(r"\s+", " ", seg).strip()


def find_patterns(body, patterns):
    found = []
    for label, pat in patterns:
        if re.search(pat, body, re.I):
            found.append(label)
    return found


def main():
    import yaml
    catalog = yaml.safe_load(open(os.path.join(ROOT, "data/catalog.yaml"), encoding="utf-8"))
    # catalog by md path
    cat_by_md = {}
    # catalog by pdf basename (frontmatter source_pdf stem)
    cat_by_pdf = {}
    for s in catalog.get("sources", []):
        files = s.get("files") or {}
        if isinstance(files, dict):
            md = files.get("md")
            if md:
                cat_by_md[md] = s
            for fk, fv in files.items():
                if isinstance(fv, str) and fv.endswith(".pdf"):
                    cat_by_pdf[os.path.basename(fv)[:-4]] = s
        # also direct pdf field on source
        pdf = s.get("pdf") or (s.get("files") or {}).get("pdf") if isinstance(s.get("files"), dict) else None
        if isinstance(s.get("pdf"), str):
            cat_by_pdf[os.path.basename(s["pdf"])[:-4]] = s

    files = (
        glob.glob(os.path.join(ROOT, "papers/*.md"))
        + glob.glob(os.path.join(ROOT, "papers/ru_papers/*.RU.md"))
        + glob.glob(os.path.join(ROOT, "queries/*.md"))
    )
    out = {}
    for path in files:
        rel = os.path.relpath(path, ROOT)
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        cat = cat_by_md.get(rel)
        if not cat:
            # try via frontmatter source_pdf stem
            src = str(fm.get("source_pdf") or "")
            stem = os.path.basename(src)[:-4] if src else None
            if stem and stem in cat_by_pdf:
                cat = cat_by_pdf[stem]
            # else try own basename stem
            else:
                stem2 = os.path.basename(rel)[:-3]  # strip .md
                if stem2 in cat_by_pdf:
                    cat = cat_by_pdf[stem2]
        title = None
        if cat and cat.get("title"):
            title = cat["title"]
        elif fm.get("title"):
            title = re.sub(r"\*+", "", str(fm["title"]))
        else:
            m = re.search(r"^#{1,2} (.+)$", body, re.M)
            title = m.group(1) if m else os.path.basename(rel)

        authors = cat.get("authors") if cat and cat.get("authors") else fm.get("authors")
        if isinstance(authors, str):
            authors = [authors]
        year = (cat.get("date", "") if cat else "")[:4] or str(fm.get("year", ""))
        venue = None
        if cat:
            venue = cat.get("venue") or cat.get("journal") or cat.get("publisher")
        if not venue and fm.get("journal"):
            venue = fm["journal"]

        url = None
        if cat and cat.get("url"):
            url = cat["url"]
        elif fm.get("url"):
            url = str(fm["url"])
        elif fm.get("links") and isinstance(fm.get("links"), dict):
            url = fm["links"].get("working_paper") or fm.get("links").get("paper")

        abs_text = first_section_cache = first_section_cache = None
        abs_text = first_abs_section(body)
        # models & data from whole body (cheap regex, capped)
        body_cap = body[:80000]
        models = find_patterns(body_cap, MODEL_PATTERNS)
        data = find_patterns(body_cap, DATA_PATTERNS)
        tags = None
        if cat and cat.get("tags"):
            tags = cat["tags"][:12]
        elif fm.get("tags") and isinstance(fm["tags"], list):
            tags = [str(t) for t in fm["tags"]][:12]

        out[rel] = {
            "t": title,
            "authors": authors or [],
            "year": year if (year := year) else "",
            "venue": venue,
            "url": url,
            "abstract": (abs_text[:1200] if abs_text else ""),
            "models": models,
            "data": data,
            "tags": tags or [],
            "cat_id": cat.get("id") if cat else None,
            "type": (cat.get("type") if cat else None) or fm.get("type"),
        }
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"OK: {len(out)} docs -> {OUT} ({os.path.getsize(OUT)/1024:.0f} KB)")


def first_abs_section(body):
    for hm in ABS_HEADERS.finditer(body):
        nxt = re.compile(r"^#{1,3} ", re.M)
        start = hm.end()
        m2 = nxt.search(body, start)
        seg = body[start:m2.start() if m2 else start + 2500]
        seg = re.sub(r"\s+", " ", seg).strip()
        if len(seg) > 80:
            return seg
    # fallback: first paragraph after H1
    m = re.search(r"^#{1,2} .*$\n+(.{80,900})", body, re.M)
    return re.sub(r"\s+", " ", m.group(1)) if m else ""


if __name__ == "__main__":
    main()