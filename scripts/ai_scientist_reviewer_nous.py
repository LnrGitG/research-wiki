#!/usr/bin/env python3
"""Адаптер Automated Reviewer из Sakana AI-Scientist к Nous-эндпоинту.

Оригинал: https://github.com/SakanaAI/AI-Scientist (ai_scientist/perform_review.py),
лицензия The AI Scientist Source Code License — при использовании требуется
раскрывать применение ИИ в рукописи.

Что делает адаптер: берёт из исходника репозитория тексты промптов (NeurIPS-форма,
инструкции, системные сообщения рецензента и area chair) через разбор AST, шлёт
N независимых рецензий в OpenAI-совместимый Nous-эндпоинт, затем сводит их
мета-ревью в роли area chair и усредняет числовые оценки — так же, как upstream.

Запуск:
  python3 scripts/ai_scientist_reviewer_nous.py \
      --pdf papers/draft-export-project-macro-screen/export-project-macro-screen-draft.pdf \
      --out data/ai-scientist-review-20261018.json --n 5
"""

import argparse
import ast
import json
import os
import re
import sys
import textwrap
from concurrent.futures import ThreadPoolExecutor

import fitz
from openai import OpenAI

DEFAULT_BASE = os.environ.get("NOUS_BASE_URL", "https://inference-api.nousresearch.com/v1")
DEFAULT_MODEL = os.environ.get("NOUS_MODEL", "deepseek/deepseek-v4.1-flash")
MAX_TOKENS = 4096

SCORE_FIELDS = [
    ("Originality", 4), ("Quality", 4), ("Clarity", 4), ("Significance", 4),
    ("Soundness", 4), ("Presentation", 4), ("Contribution", 4),
    ("Overall", 10), ("Confidence", 5),
]


def load_prompts(repo: str) -> dict:
    """Достаёт строковые константы модуля без импорта (зависимости не нужны)."""
    src = open(os.path.join(repo, "ai_scientist/perform_review.py"), encoding="utf-8").read()
    tree = ast.parse(src)

    out = {}

    def ev(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return ev(node.left) + ev(node.right)
        if isinstance(node, ast.Name):
            return out[node.id]          # ссылка на ранее определённую константу
        raise ValueError(type(node))

    # два прохода: константы могут ссылаться на объявленные выше по файлу
    assigns = [n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1
               and isinstance(n.targets[0], ast.Name)]
    for _ in range(2):
        for node in assigns:
            try:
                out[node.targets[0].id] = ev(node.value)
            except (ValueError, KeyError):
                pass
    return out


def pdf_text(path: str) -> str:
    doc = fitz.open(path)
    return "\n".join(p.get_text() for p in doc)


def extract_json(s: str):
    m = re.search(r"```json\s*(.*?)```", s, re.S)
    raw = m.group(1) if m else s
    m2 = re.search(r"\{.*\}", raw, re.S)
    if not m2:
        return None
    try:
        return json.loads(m2.group(0))
    except json.JSONDecodeError:
        return None


def salvage_meta(s: str) -> dict:
    """Спасает поля мета-ревью, когда модель не дала корректный JSON."""
    out = {}
    for key in ("Summary", "Decision", "Overall", "Confidence", "Originality",
                "Quality", "Clarity", "Significance", "Soundness", "Presentation",
                "Contribution"):
        m = re.search(rf'"{key}"\s*:\s*(\d+(?:\.\d+)?|"[^"]*"|\{{)', s)
        if not m:
            continue
        v = m.group(1)
        if v.startswith('"'):
            out[key] = v.strip('"')
        elif v == "{":
            # массив строк в квадратных скобках либо объект — берём до закрытия блока
            blk = s[m.end():]
            items = re.findall(r'"([^"]{10,400})"', blk[:4000])
            if items:
                out[key] = items
        else:
            out[key] = float(v) if "." in v else int(v)
    return out


def call(client, model, system, user, temperature):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        temperature=temperature,
        max_tokens=MAX_TOKENS,
    )
    return r.choices[0].message.content


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--repo", default="/tmp/AI-Scientist")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--temperature", type=float, default=0.75)
    a = ap.parse_args()

    key = os.environ.get("NOUS_API_KEY")
    if not key:
        sys.exit("NOUS_API_KEY не задан")
    client = OpenAI(api_key=key, base_url=DEFAULT_BASE)
    p = load_prompts(a.repo)

    text = pdf_text(a.pdf)
    form = p["neurips_form"]
    system = p["reviewer_system_prompt_neg"]
    prompt = form + "\nHere is the paper you are asked to review:\n```\n" + text + "\n```"

    print(f"PDF: {len(text)} знаков; модель {a.model}; рецензий {a.n}", flush=True)

    def one(i):
        """Одна рецензия с добором при неудачном разборе JSON."""
        for attempt, temp in enumerate((a.temperature, max(0.2, a.temperature - 0.45))):
            raw = call(client, a.model, system, prompt, temp)
            j = extract_json(raw or "")
            if j is not None:
                if attempt:
                    print(f"рецензия {i+1}: разобрана со 2-й попытки", flush=True)
                return j
        print(f"рецензия {i+1}: JSON не разобран (2 попытки)", flush=True)
        return None

    with ThreadPoolExecutor(max_workers=min(a.n, 3)) as ex:
        parsed = list(ex.map(one, range(a.n)))
    reviews = [r for r in parsed if r is not None]
    print(f"разобрано рецензий: {len(reviews)}/{a.n}", flush=True)
    if not reviews:
        sys.exit("ни одна рецензия не разобрана")

    meta_text = form + "".join(
        f"\nReview {i+1}/{len(reviews)}:\n```\n{json.dumps(r, ensure_ascii=False)}\n```\n"
        for i, r in enumerate(reviews)
    )
    meta_sys = p["meta_reviewer_system_prompt"].format(reviewer_count=len(reviews))
    meta, meta_raw = {}, ""
    for temp in (a.temperature, max(0.2, a.temperature - 0.45)):
        meta_raw = call(client, a.model, meta_sys, meta_text, temp)
        meta = extract_json(meta_raw or "") or salvage_meta(meta_raw or "")
        if meta:
            break
    if not meta:
        print("мета-ревью: JSON не разобран, поля извлечены частично", flush=True)

    agg = {}
    for f, hi in SCORE_FIELDS:
        vals = [r.get(f) for r in reviews if isinstance(r.get(f), (int, float))]
        if vals:
            agg[f] = round(sum(vals) / len(vals), 2)
        elif isinstance(meta.get(f), (int, float)):
            agg[f] = meta[f]

    decisions = [r.get("Decision") for r in reviews if r.get("Decision")]
    out = {
        "source": "SakanaAI/AI-Scientist perform_review (NeurIPS form), адаптер к Nous",
        "pdf": a.pdf,
        "model": a.model,
        "n_reviews": len(reviews),
        "ensemble_mean": agg,
        "votes": {d: decisions.count(d) for d in set(decisions)},
        "meta": meta,
        "reviews": reviews,
        "raw_meta": meta_raw,
    }
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("\n=== сводка ===")
    for f, _ in SCORE_FIELDS:
        print(f"{f:13s} {agg.get(f)}")
    print("голоса:", out["votes"])
    print("решение (мета):", meta.get("Decision"))
    print("сохранено:", a.out)


if __name__ == "__main__":
    main()
