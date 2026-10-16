#!/usr/bin/env bash
# Сборка PDF проекта статьи. Порядок разделов: титул/аннотации, протокол, рукопись.
set -euo pipefail
cd "$(dirname "$0")"

VENV=/home/lnr/.hermes/hermes-agent/venv
PANDOC="$VENV/lib/python3.11/site-packages/pypandoc/files/pandoc"
export PATH="/home/lnr/.TinyTeX/bin/x86_64-linux:$PATH"

OUT_MD="combined.md"
OUT_PDF="export-project-macro-screen-draft.pdf"

{
  printf '%s\n' '---' \
    'title: "Льготное финансирование экспортного инфраструктурного проекта"' \
    'subtitle: "Условный стресс-тест финансовой и макроэкономической совместимости — проект статьи, без расчётов"' \
    'date: "13 октября 2026"' \
    'lang: ru-RU' \
    '---' '' \
    '# Аннотация (RU)' ''
  sed '1{/^# Abstract/d}' abstract-en.md >/dev/null 2>&1 || true

  # Русская аннотация из draft-ru.md
  awk '/^## Аннотация/{f=1;next} /^## Abstract/{f=0} f' draft-ru.md
  printf '\n# Abstract (EN)\n\n'
  sed '1{/^# Abstract/d}' abstract-en.md
  printf '\n\\newpage\n\n'
  cat README.md
  printf '\n\\newpage\n\n'
  cat draft-ru.md
} > "$OUT_MD"

"$PANDOC" "$OUT_MD" \
  --pdf-engine=xelatex \
  -V mainfont="DejaVu Serif" \
  -V sansfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V geometry:margin=2.2cm \
  -V fontsize=10pt \
  -V colorlinks=true \
  -V linkcolor=NavyBlue \
  --toc --toc-depth=2 \
  -o "$OUT_PDF"

ls -l "$OUT_PDF"
