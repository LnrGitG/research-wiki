#!/usr/bin/env bash
# Сборка PDF статьи (pandoc + xelatex, стек на VPS: ~/.TinyTeX + pypandoc_binary).
# Конвертация Markdown -> LaTeX (.tex) и PDF; таблица экспорта в §4.1 идёт longtable/booktabs.
set -euo pipefail
cd "$(dirname "$0")"

PANDOC="$HOME/.hermes/hermes-agent/venv/lib/python3.11/site-packages/pypandoc/files/pandoc"
SRC="draft-ru.md"
OUT="draft-hybrid-mp-regime.pdf"
TEX="draft-ru.tex"

# Промежуточный LaTeX (standalone) — читаемая и версионируемая разметка верстки.
"$PANDOC" "$SRC" -o "$TEX" \
  --standalone \
  --toc --toc-depth=2 \
  --include-in-header=preamble.tex

"$PANDOC" "$SRC" -o "$OUT" \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V mainfont="Liberation Serif" \
  -V monofont="Liberation Mono" \
  -V fontsize=11pt \
  -V lang=russian \
  --include-in-header=preamble.tex

echo "Собрано: $TEX и $OUT"
