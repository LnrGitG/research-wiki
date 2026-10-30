#!/usr/bin/env bash
# Резидентное окно через tailscale exit node (ноутбук) на время проверки.
#
# Зачем отдельный скрипт. Пока exit node включён, через ноутбук идёт ВЕСЬ
# исходящий трафик VPS, включая SSH к ВМ и вызовы модели. Поэтому окно всегда
# ограничено: enable → работа → disable в trap, даже если работа упала. Вывод
# пишется в файл, чтобы его можно было забрать, не глядя в терминал.
#
# Использование:
#   scripts/resident_window.sh check               # только проверка источников
#   scripts/resident_window.sh hh                  # снять hh-выгрузки в /tmp
#   LIMIT=600 scripts/resident_window.sh hold      # держать окно (интерактив)
set -uo pipefail

export SUDO_ASKPASS="${SUDO_ASKPASS:-$HOME/.hermes/scripts/sudo_askpass.sh}"
NODE="${NODE:-100.114.29.93}"          # DESKTOP-485MNGE (ноутбук, Уфанет)
OUT="${OUT:-/tmp/resident_window.log}"
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36'
MODE="${1:-check}"

log() { printf '%s %s\n' "$(date -u +%H:%M:%S)" "$*" | tee -a "$OUT"; }

cleanup() {
  sudo -A tailscale set --exit-node= >/dev/null 2>&1
  log "окно закрыто, exit node снят"
}
trap cleanup EXIT INT TERM

: > "$OUT"
IP_BEFORE="$(curl -s -m 10 https://api.ipify.org || true)"
log "адрес до окна: ${IP_BEFORE:-?}"

if ! sudo -A tailscale set --exit-node="$NODE" --exit-node-allow-lan-access >/dev/null 2>&1; then
  log "не удалось включить exit node $NODE (sudo/askpass?)"
  exit 65
fi

IP_AFTER=""
for _ in $(seq 1 15); do
  sleep 2
  IP_AFTER="$(curl -s -m 8 https://api.ipify.org || true)"
  [[ -n "$IP_AFTER" && "$IP_AFTER" != "$IP_BEFORE" ]] && break
done
log "адрес в окне: ${IP_AFTER:-?}"

probe() {  # probe <name> <url>  → код
  local name="$1" url="$2" code
  code="$(curl -s -m 25 -o /dev/null -w '%{http_code}' -A "$UA" "$url" || echo 000)"
  log "источник $name: $code"
}

case "$MODE" in
  check)
    probe api.hh.ru 'https://api.hh.ru/vacancies?text=test&per_page=1'
    probe fedstat.ru 'https://www.fedstat.ru/'
    probe дом.рф 'https://наш.дом.рф/analytics/priceindex'
    log "фрагмент ответа hh: $(curl -s -m 25 -A "$UA" \
      'https://api.hh.ru/vacancies?text=%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80&per_page=1' \
      | head -c 200)"
    ;;
  hh)
    D=/tmp/hh_dump; mkdir -p "$D"
    for q in "строитель" "инженер ПТО" "арматурщик" "каменщик" "прораб" "сметчик"; do
      f="$D/$(echo "$q" | tr ' ' '_').json"
      curl -s -m 40 -A "$UA" -G 'https://api.hh.ru/vacancies' \
        --data-urlencode "text=$q" --data-urlencode 'per_page=1' \
        --data-urlencode 'area=113' -o "$f" || log "сбой $q"
      log "hh $q → $(wc -c < "$f") байт"
      sleep 1
    done
    ;;
  hold)
    log "окно удерживается $(( ${LIMIT:-600} / 60 )) мин"
    sleep "${LIMIT:-600}"
    ;;
  *)
    log "неизвестный режим: $MODE"
    exit 64
    ;;
esac
