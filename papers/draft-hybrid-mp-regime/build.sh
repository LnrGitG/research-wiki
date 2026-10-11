#!/usr/bin/env bash
# Сборка PDF статьи (pandoc + xelatex, стек на VPS: ~/.TinyTeX + pypandoc_binary).
# Статья текстовая: без citeproc, таблиц и рисунков — прямая конвертация Markdown.
set -euo pipefail
cd "$(dirname "$0")"

PANDOC="$HOME/.hermes/hermes-agent/venv/lib/python3.11/site-packages/pypandoc/files/pandoc"
SRC="draft-ru.md"
OUT="draft-hybrid-mp-regime.pdf"

"$PANDOC" "$SRC" -o "$OUT" \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V mainfont="Liberation Serif" \
  -V monofont="Liberation Mono" \
  -V fontsize=11pt \
  -V lang=russian \
  --include-in-header=preamble.tex

echo "Собрано: $OUT"
