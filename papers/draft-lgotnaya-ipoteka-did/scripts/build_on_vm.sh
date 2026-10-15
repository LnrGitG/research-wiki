#!/usr/bin/env bash
# Сборка статьи на ВМ YC (профиль monitor-хост): там есть rmarkdown, pandoc и
# TeX Live, поэтому используется полный путь rmarkdown::render, а не обходной
# knitr + pandoc, как на VPS.
#
# Что делает: копирует скрипты и файлы статьи на ВМ, запускает экспорт таблиц
# и рисунков из базы (локальный PostgreSQL на ВМ), собирает PDF, забирает его
# обратно в каталог статьи.
#
# Требования на ВМ: R с rmarkdown, pandoc, texlive-xetex (xelatex),
# texlive-lang-cyrillic, fonts-liberation, python-venv с pandas/numpy/matplotlib/psycopg.
#
# Запуск: bash scripts/build_on_vm.sh
set -euo pipefail

HOST="${PAPER_VM_HOST:?задайте PAPER_VM_HOST=пользователь@адрес-ВМ}"
KEY="${PAPER_VM_KEY:-$HOME/.ssh/paper_vm_key}"
SSH="ssh -i $KEY -o StrictHostKeyChecking=no $HOST"
SCP="scp -i $KEY -o StrictHostKeyChecking=no"
LOCAL="$(cd "$(dirname "$0")/.." && pwd)"

echo "== 1. передача файлов на ВМ"
$SSH 'mkdir -p ~/paper/scripts ~/paper/tables ~/paper/figures'
$SCP "$HOME/personal/scripts/did_all_regions.py" "$HOME/personal/scripts/ufo_did_controls.py" \
     "$HOME/personal/scripts/export_for_paper.py" "$HOST:~/paper/scripts/"
$SCP "$LOCAL/paper.Rmd" "$LOCAL/refs.bib" "$LOCAL/preamble.tex" "$HOST:~/paper/"

echo "== 2. экспорт таблиц и рисунков + сборка PDF на ВМ"
$SSH 'cd ~/paper && PGHOST=127.0.0.1 PGPORT=5432 PGDATABASE=research_wiki PGUSER=wiki \
      PAPER_DIR=~/paper ~/venv/bin/python3 scripts/export_for_paper.py && \
      Rscript -e "rmarkdown::render(\"paper.Rmd\", output_format=\"pdf_document\", quiet=TRUE)"'

echo "== 3. возврат артефактов"
$SCP "$HOST:~/paper/paper.pdf" "$LOCAL/paper_vm.pdf"
$SCP "$HOST:~/paper/tables/*" "$LOCAL/tables/"
$SCP "$HOST:~/paper/figures/*" "$LOCAL/figures/"

echo "== готово: $LOCAL/paper_vm.pdf"