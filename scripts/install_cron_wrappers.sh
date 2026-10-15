#!/bin/bash
# install_cron_wrappers.sh — идемпотентно слинковать .sh-обёртки cron-джобов
# из репозитория в ~/.hermes/scripts/.
#
# Зачем: cron-джобы no_agent ссылаются на обёртку по имени относительно
# ~/.hermes/scripts/ (например script=rosstat_industrial_job.sh), а сами
# обёртки заведены в scripts/ репозитория. После переезда ВМ или сборки
# нового профиля линки теряются, и джобы молча падают с «Script not found»
# (инцидент 08–15.10.2026: так отвалились пять ингест-джобов и сторож
# свежести). Скрипт восстанавливает линки одной командой.
#
# Использование: bash scripts/install_cron_wrappers.sh
set -euo pipefail

SRC="$HOME/research-wiki-private/scripts"
DST="$HOME/.hermes/scripts"
mkdir -p "$DST"

n=0
for f in "$SRC"/*_job.sh; do
    [ -e "$f" ] || continue
    ln -sf "$f" "$DST/$(basename "$f")"
    n=$((n + 1))
done

echo "cron-обёртки: слинковано $n"
for f in "$DST"/*_job.sh; do
    [ -L "$f" ] && printf '  %s -> %s\n' "$(basename "$f")" "$(readlink "$f")"
done
