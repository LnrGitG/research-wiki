#!/bin/bash
# install_cron_wrappers.sh — разложить launcher-обёртки cron-джобов в
# ~/.hermes/scripts/.
#
# Зачем: cron-джобы no_agent ссылаются на обёртку по имени относительно
# ~/.hermes/scripts/ (например script=rosstat_industrial_job.sh), а сами
# обёртки заведены в scripts/ репозитория. После переезда ВМ или сборки
# нового профиля обёртки в ~/.hermes/scripts/ пропадают, и джобы молча
# падают с «Script not found» (инцидент 08–15.10.2026: так отвалились
# пять ингест-джобов и сторож свежести).
#
# ВАЖНО: cron-движок блокирует скрипт, если он симлинк, ведущий за пределы
# ~/.hermes/scripts/ («script path resolves outside the scripts directory»),
# поэтому здесь генерируются НАСТОЯЩИЕ файлы-launcher'ы, которые через
# subprocess/exec вызывают обёртку из репозитория. Источник правды остаётся
# один — scripts/ репозитория; здесь только тонкие launcher'ы.
#
# Использование: bash scripts/install_cron_wrappers.sh
set -euo pipefail

SRC="$HOME/research-wiki-private/scripts"
DST="$HOME/.hermes/scripts"
mkdir -p "$DST"

# обёртки-джобы плюс отдельные скрипты, на которые ссылаются cron-задания
targets=( "$SRC"/*_job.sh "$SRC"/metric_card_rebuild.sh )

n=0
for f in "${targets[@]}"; do
    [ -e "$f" ] || continue
    name="$(basename "$f")"
    dst="$DST/$name"
    case "$name" in
        *.sh)
            # реальный launcher вместо симлинка
            rm -f "$dst"
            {
                printf '#!/bin/bash\n'
                printf '# launcher, сгенерирован scripts/install_cron_wrappers.sh -> %s\n' "$f"
                printf 'exec bash "%s" "$@"\n' "$f"
            } > "$dst"
            chmod +x "$dst"
            ;;
        *)
            printf 'skip (не .sh): %s\n' "$name"
            continue
            ;;
    esac
    n=$((n + 1))
done

echo "cron-обёртки: разложено $n launcher'ов"
for f in "$DST"/*_job.sh "$DST"/metric_card_rebuild.sh; do
    [ -f "$f" ] && printf '  %s\n' "$(basename "$f")"
done
