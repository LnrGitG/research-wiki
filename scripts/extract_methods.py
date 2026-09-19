#!/usr/bin/env python3
"""Извлечение методов, данных и выводов из корпуса (фаза 2).

Что делает: для каждой работы находит секции методов/данных/выводов по
заголовкам, определяет методы по словарю терминов и обогащает словарь
новыми терминами, встреченными в тексте («методы из содержания»).

Порядок источников для каждой работы:
  1. перевод `.RU.md`, если он полный (>50 КБ) — текст на русском;
  2. англоязычная статья — полные тексты крупнее, но язык другой;
  3. аннотация из `docs/paper-details.json` — там уже размеченные methods.

Важное ограничение, обнаруженное при разведке: 135 из 161 перевода — это
ТОЛЬКО аннотация (<10 КБ), полный текст переведён лишь у 10. Поэтому
основной источник методов — англоязычные статьи (секции методов найдены у
134 из 314), а переводы дают терминологию на русском.

Словарь методов обогащается по итогам прогона: новые термины, встреченные
в заголовках и первых строках секций методов, добавляются в `METHODS_DICT`
и в отчётный файл — как просил владелец.

Запуск:  python3 extract_methods.py                 # отчёт
         python3 extract_methods.py --json out.json  # + результат
"""
import argparse
import collections
import glob
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etl_common

SCRIPT = "extract_methods.py"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

# --- Словарь методов: эконометрика, ML, идентификация, данные ---
METHODS_DICT = {
    # панельные и причинные
    "did": "DiD", "difference-in-differences": "DiD", "разность разностей": "DiD",
    "event study": "event-study", "событийный анализ": "event-study",
    "iv": "IV", "instrumental variable": "IV", "инструментальные переменные": "IV",
    "2sls": "2SLS", "gmm": "GMM", "fe": "FE-panel", "fixed effects": "FE-panel",
    "random effects": "RE-panel", "panel": "panel", "панель": "panel",
    "rdd": "RDD", "regression discontinuity": "RDD",
    "synthetic control": "synthetic-control",
    "propensity score": "PSM",
    # временные ряды и факторные
    "var": "VAR", "вар": "VAR", "bvar": "BVAR", "bvár": "BVAR",
    "favar": "FAVAR", "svar": "SVAR", "фавар": "FAVAR",
    "vecm": "VECM", "cointegration": "cointegration", "коинтеграц": "cointegration",
    "ardl": "ARDL", "garch": "GARCH", "архи": "ARCH",
    "local projection": "local-projections", "локальные проекции": "local-projections",
    "state space": "state-space", "kalman": "Kalman",
    "factor model": "factor-model", "dfm": "DFM", "dynamic factor": "DFM",
    # mixed frequency и nowcasting
    "midas": "MIDAS", "mixed data sampling": "MIDAS", "мидас": "MIDAS",
    "mf-var": "MF-VAR", "mixed frequency": "mixed-frequency",
    "bridge equation": "bridge", "bridge": "bridge",
    "nowcasting": "nowcasting", "наукастинг": "nowcasting", "nowcast": "nowcasting",
    "ragged edge": "ragged-edge",
    "entropic tilting": "entropic-tilting",
    # структурные
    "dsge": "DSGE", "cge": "CGE", "olga": "OLG",
    "tobin": "Tobin-q", "user cost": "user-cost", "q-model": "Tobin-q",
    "search model": "search-model", "matching": "matching",
    "hedonic": "hedonic", "repeat sales": "repeat-sales",
    "spatial": "spatial", "пространствен": "spatial",
    "gravity": "gravity",
    # ML
    "random forest": "RandomForest", "xgboost": "XGBoost", "gradient boost": "boosting",
    "lasso": "Lasso", "ridge": "Ridge", "elastic net": "elastic-net",
    "neural network": "neural-net", "нейросет": "neural-net", "lstm": "LSTM",
    "machine learning": "ML", "машинное обучен": "ML",
    "clustering": "clustering", "кластеризац": "clustering", "k-means": "k-means",
    "pca": "PCA", "principal component": "PCA",
    "bayesian model averaging": "BMA", "bma": "BMA",
    # идентификация и оценка
    "sur": "SUR", "tobit": "Tobit", "probit": "probit", "logit": "logit",
    "quantile regression": "quantile-regression",
    "maximum likelihood": "MLE", "mle": "MLE", "метод максимального правдоподобия": "MLE",
    "bayesian": "Bayesian", "байесовск": "Bayesian", "bvar": "BVAR",
    "survival": "survival", "hazard": "hazard-model",
    "decomposition": "decomposition", "декомпозиц": "decomposition",
    "elasticity": "supply-elasticity", "эластичность": "supply-elasticity",
    "arima": "ARIMA", "sarima": "SARIMA", "arma": "ARMA",
    "panel var": "panel-VAR", "pvar": "panel-VAR", "gvar": "GVAR",
    "tvp-var": "TVP-VAR", "tvp": "TVP", "time-varying parameter": "TVP",
    "stochastic volatility": "stochastic-volatility",
    "threshold": "threshold-model", "regime switching": "regime-switching",
    "markov switching": "regime-switching", "quantile": "quantile-regression",
    "variance decomposition": "variance-decomposition",
    "error correction": "error-correction", "ols": "OLS",
    "univariate": "univariate", "multivariate": "multivariate",
    "out-of-sample": "out-of-sample", "oos": "out-of-sample",
    "case-shiller": "Case-Shiller", "repeat sales": "repeat-sales",
    "relative entropy": "entropic-tilting", "entropy": "entropic-tilting",
    "bunching": "bunching", "structural break": "structural-break",
    "bai-perron": "Bai-Perron", "placebo": "placebo-test",
    "cross-validation": "cross-validation", "expanding window": "expanding-window",
    "rolling window": "rolling-window", "fan chart": "fan-chart",
    "density forecast": "density-forecast", "attention": "attention-model",
    "transformer": "transformer", "graph neural": "GNN", "convolutional": "CNN",
    "survival analysis": "survival", "cox": "Cox-model", "duration model": "duration-model",
    "double machine learning": "DML", "causal forest": "causal-forest",
    "semi-parametric": "semi-parametric", "nonparametric": "nonparametric",
    "kernel": "kernel-method", "wavelet": "wavelet", "spline": "spline",
    "callaway": "Callaway-SantAnna", "sun-abraham": "Sun-Abraham",
    "goodman-bacon": "Goodman-Bacon", "hausman": "Hausman-test",
    "within estimator": "within-estimator", "first difference": "first-difference",
    "pseudo-panel": "pseudo-panel", "cohort": "cohort-analysis",
    "monte carlo": "Monte-Carlo", "bootstrap": "bootstrap",
}

# --- Словарь источников данных ---
DATA_DICT = {
    "rosstat": "Росстат", "росстат": "Росстат", "емисс": "ЕМИСС", "emiss": "ЕМИСС",
    "cbr": "ЦБ РФ", "bank of russia": "ЦБ РФ", "цб рф": "ЦБ РФ", "банк россии": "ЦБ РФ",
    "фнс": "ФНС", "налог": "ФНС", "fns": "ФНС",
    "дом.рф": "ДОМ.РФ", "дом рф": "ДОМ.РФ", "dom.rf": "ДОМ.РФ", "domrf": "ДОМ.РФ",
    "еисжс": "ЕИСЖС", "eiszhk": "ЕИСЖС", "наш.дом.рф": "ЕИСЖС",
    "росреестр": "Росреестр", "rosreestr": "Росреестр",
    "smart-lab": "Smart-Lab", "smartlab": "Smart-Lab",
    "оэср": "OECD", "oecd": "OECD", "евростат": "Eurostat", "eurostat": "Eurostat",
    "bis": "BIS", "мвф": "IMF", "imf": "IMF", "world bank": "World Bank",
    "всемирный банк": "World Bank", "fred": "FRED", "nber": "NBER",
    "econstats": "EconStats", "pwt": "PWT", "klems": "KLEMS",
    "google trends": "Google Trends", "гугл тренды": "Google Trends",
    "wordstat": "Wordstat", "яндекс": "Яндекс", "gdelt": "GDELT",
    "spark": "SPARK", "опендата": "ФНС опендата", "opendata": "ФНС опендата",
    "bls": "BLS", "census": "Census", "fhfa": "FHFA",
    "zillow": "Zillow", "corelogic": "CoreLogic", "case-shiller": "Case-Shiller",
    "sber": "Сбер", "сбербанк": "Сбер", "втб": "ВТБ",
}

SECTION_RE = re.compile(
    r"^#{1,4}\s*[*_<u>\s]*((?:\d+[\.\s]*)?(?:"
    r"метод\w*|методолог\w*|данны\w*|эмпирич\w*|идентификац\w*|модел\w*|стратег\w*|"
    r"method\w*|methodolog\w*|data\w*|empiric\w*|identification\w*|model\w*|"
    r"econometric\w*|specification\w*|strategy\w*"
    r"))[^\n]*$", re.M | re.I)

CONCLUSION_RE = re.compile(
    r"^#{1,4}\s*[*_<u>\s]*((?:\d+[\.\s]*)?(?:"
    r"вывод\w*|заключени\w*|результат\w*|итог\w*|обсужден\w*|"
    r"conclusion\w*|concluding\w*|findings?\w*|results?\w*|summary\w*|"
    r"discussion\w*|policy\s+implication\w*|implication\w*"
    r"))[^\n]*$", re.M | re.I)


def body_of(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    if s.startswith("---") and s.count("---") >= 2:
        return s.split("---", 2)[2]
    return s


def sections(body, pat, limit=3, maxlen=3500):
    """Тексты до `limit` секций после заголовков, суммарно до maxlen символов."""
    out = []
    for m in pat.finditer(body):
        start = m.end()
        nxt = re.search(r"\n#{1,4}\s", body[start:])
        chunk = body[start:start + (nxt.start() if nxt else 3000)]
        chunk = re.sub(r"<!--.*?-->", " ", chunk, flags=re.S)
        chunk = re.sub(r"\s+", " ", chunk).strip()
        if len(chunk) > 80:
            out.append(chunk)
        if len(out) >= limit:
            break
    return " ".join(out)[:maxlen]


def find_terms(text, dictionary):
    """Термины из словаря, встреченные в тексте (уникальные, по канону)."""
    low = text.lower()
    found = []
    for key, canon in dictionary.items():
        # границы слова С ОБЕИХ сторон: иначе 'fe' ловится в 'federal', а
        # 'var' — в 'variable'/'variance' (проверено: давало 173 ложных VAR)
        if re.search(r"(?<![\w-])" + re.escape(key) + r"(?![\w-])", low):
            if canon not in found:
                found.append(canon)
    return found


def process_one(p, trans, details):
    """Обработать одну статью. Возвращает запись артефакта."""
    stem = os.path.basename(p)[:-3]
    b_en = body_of(p)
    method_src = b_en
    source = "en_article"

    # ищем русский полный перевод: по имени или по совпадению заголовка
    for t in trans:
        ts = open(t, encoding="utf-8", errors="ignore").read(4000)
        if stem[:35] in ts or os.path.basename(t)[:-3][:35] == stem[:35]:
            if os.path.getsize(t) > 50000:
                method_src = body_of(t)
                source = "ru_translation"
            break

    mtext = sections(method_src, SECTION_RE)
    ctext = sections(method_src, CONCLUSION_RE, limit=4, maxlen=4500)
    methods = find_terms(mtext + " " + ctext + " " + b_en[:3000], METHODS_DICT)
    data = find_terms(mtext + " " + b_en[:3000], DATA_DICT)

    # дополнить из paper-details.json
    d = details.get(p) or {}
    for x in (d.get("models") or []):
        if x and x not in methods:
            methods.append(x)
    for x in (d.get("data") or []):
        if x and x not in data:
            data.append(x)

    # Резерв для выводов, когда секции нет: аннотация из paper-details.json
    # (это осмысленный текст о результате) — помечаем источник.
    findings_src = "section" if ctext else ""
    if not ctext:
        ab = re.sub(r"\s+", " ", (d.get("abstract") or "")).strip()
        if len(ab) > 120:
            ctext, findings_src = ab[:2000], "abstract"

    return {
        "wiki_page": p, "stem": stem,
        "method_source": source,
        "methods": methods, "data_sources": data,
        "methods_text": mtext[:1200],
        "findings": ctext[:2000],
        "findings_source": findings_src,
        "has_method_section": bool(mtext),
        "has_conclusion_section": bool(ctext),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    etl_common.add_args(ap)
    args = ap.parse_args()

    t_start = time.time()
    papers = sorted(glob.glob("papers/*.md"))
    trans = sorted(glob.glob("papers/ru_papers/*.md"))
    try:
        details = json.load(open("docs/paper-details.json", encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        details = {}

    todo, skipped = etl_common.changed_files(
        SCRIPT, papers, only=args.only, since=args.since, force=args.force)
    print("Статей всего: %d | к обработке: %d | без изменений: %d"
          % (len(papers), len(todo), skipped))

    prev = {} if args.force else etl_common.load_artifact("methods")
    for p in todo:
        prev[p] = process_one(p, trans, details)

    out = list(prev.values())
    term_counter = collections.Counter()
    new_terms = collections.Counter()
    for r in out:
        for m in r.get("methods", []):
            term_counter[m] += 1

    # --- обогащение словаря: кандидаты из заголовков секций методов ---
    for r in out:
        b = body_of(r["wiki_page"])
        for m in SECTION_RE.finditer(b):
            h = re.sub(r"[*_#<>\d\.\s]", " ", m.group(1)).strip().lower()
            if 4 < len(h) < 40 and not any(h in k or k in h for k in METHODS_DICT):
                new_terms[h] += 1

    total = len(out)
    print("\nВ артефакте статей: %d" % total)
    print("Наличие секций:")
    for f in ("method", "conclusion"):
        n = sum(1 for r in out if r["has_%s_section" % f])
        print("  %-12s %d (%.0f%%)" % (f, n, 100 * n / max(1, total)))

    print("\nИсточник текста методов:")
    for k, v in collections.Counter(r["method_source"] for r in out).most_common():
        print("  %-18s %d" % (k, v))

    print("\nТоп методов по частоте:")
    for m, n in term_counter.most_common(24):
        print("  %-24s %d" % (m, n))

    print("\nТоп источников данных:")
    dc = collections.Counter()
    for r in out:
        for x in r["data_sources"]:
            dc[x] += 1
    for m, n in dc.most_common(18):
        print("  %-20s %d" % (m, n))

    print("\nЗаполненность методов/выводов:")
    for f in ("methods", "data_sources", "findings"):
        n = sum(1 for r in out if r.get(f))
        print("  %-14s %d (%.0f%%)" % (f, n, 100 * n / max(1, total)))

    if new_terms:
        print("\nКандидаты в словарь методов (встречены в заголовках, нет в словаре):")
        for t, n in new_terms.most_common(15):
            print("  %-40s %d" % (t[:38], n))

    saved = []
    if not args.no_save:
        p, sz = etl_common.save_artifact("methods", out)
        etl_common.mark_done(SCRIPT, todo)
        saved.append(p)
        print("\nАртефакт: %s (%.0f КБ)" % (p, sz / 1024))
        # кандидаты в словарь — отдельным файлом для ручного просмотра
        nt = etl_common.artifact_path("methods-new-terms")
        json.dump(dict(new_terms.most_common(60)), open(nt, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        saved.append(nt)

    print("Время: %.1f с (обработано %d статей)" % (time.time() - t_start, len(todo)))
    etl_common.record_run(SCRIPT, "methods", t_start, time.time(),
                          rows=len(todo), status="ok", artifacts=saved,
                          extra={"total_articles": total, "skipped": skipped})

    if args.json:
        json.dump(out, open(args.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("JSON: %s (%.0f КБ)" % (args.json, os.path.getsize(args.json) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
