#!/usr/bin/env bash
# Резидентный канал: проверка со стороны VPS.
#
# Смысл проверки не «отвечает ли источник», а «откуда он видит запрос». Прокси,
# поднятый на VPS, тоже вернёт 200 с cbr.ru — но api.hh.ru даст 403, потому что
# выход остался датацентровым. Поэтому скрипт сначала сравнивает внешний IP
# напрямую и через канал: совпали — канал несёт наш же адрес, и доверять его
# результатам по блокирующим источникам нельзя.
#
# Использование:
#   scripts/resident_check.sh                 # порт 18080, без токена
#   scripts/resident_check.sh 18080 TOKEN     # порт и токен прокси
#   scripts/resident_check.sh --json          # машинночитаемый вывод
set -uo pipefail

PORT="${1:-18080}"
TOKEN="${2:-}"
JSON=0
[[ "${1:-}" == "--json" ]] && JSON=1 && PORT="${2:-18080}" && TOKEN="${3:-}"

PROXY="http://127.0.0.1:${PORT}"
AUTH=()
[[ -n "$TOKEN" ]] && AUTH=(-U "${TOKEN}:")
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36'

probe() {  # probe <url> <proxy|direct> → "код|секунды"
  local url="$1" mode="$2" args=(-s -m 20 -o /dev/null -w '%{http_code}|%{time_total}')
  [[ "$mode" == proxy ]] && args+=(-x "$PROXY" "${AUTH[@]}")
  curl "${args[@]}" -A "$UA" "$url" 2>/dev/null || echo "000|-"
}

ip_via() {  # ip_via <proxy|direct>
  local mode="$1" args=(-s -m 20)
  [[ "$mode" == proxy ]] && args+=(-x "$PROXY" "${AUTH[@]}")
  curl "${args[@]}" https://ipinfo.io/ip 2>/dev/null | tr -d '\r\n'
}

say() { [[ $JSON -eq 0 ]] && printf '%s\n' "$1"; }

CHANNEL=down
RC=0
if curl -s -m 5 -o /dev/null -x "$PROXY" "${AUTH[@]}" http://ipinfo.io/ip; then
  CHANNEL=up
else
  RC=3
fi

say "канал: ${PROXY} — ${CHANNEL}"

IP_DIRECT="$(ip_via direct)"
IP_PROXY=""
[[ $CHANNEL == up ]] && IP_PROXY="$(ip_via proxy)"
say "внешний IP: напрямую ${IP_DIRECT:-?} | через канал ${IP_PROXY:-?}"
if [[ -n "$IP_PROXY" && "$IP_PROXY" == "$IP_DIRECT" ]]; then
  say "ВНИМАНИЕ: адрес через канал совпал с адресом VPS — это не резидентный выход"
fi

declare -A URLS=(
  [api.hh.ru]='https://api.hh.ru/vacancies?text=test&per_page=1'
  [fedstat.ru]='https://www.fedstat.ru/'
  [дом.рф]='https://наш.дом.рф/analytics/priceindex'
  [cbr.ru]='https://www.cbr.ru/'
)
say ""
say "источник      напрямую   через канал   вывод"
for name in api.hh.ru fedstat.ru дом.рф cbr.ru; do
  d="$(probe "${URLS[$name]}" direct)"
  p="$(probe "${URLS[$name]}" proxy)"
  dc="${d%%|*}"; pc="${p%%|*}"
  verdict="—"
  if [[ "$CHANNEL" != up ]]; then
    verdict="канал не поднят"
  elif [[ "$dc" == "403" && "$pc" == "200" ]]; then
    verdict="резидентный выход работает"
  elif [[ "$dc" == "403" && "$pc" == "403" ]]; then
    verdict="канал есть, но выход тоже закрыт (VPN?)"
    RC=2
  elif [[ "$dc" == "200" && "$pc" == "200" ]]; then
    verdict="источник доступен и так"
  elif [[ "$pc" == "000" ]]; then
    verdict="нет ответа через канал"
    RC=2
  fi
  say "$(printf '%-12s  %-9s  %-12s  %s' "$name" "$dc" "$pc" "$verdict")"
done

if [[ $JSON -eq 1 ]]; then
  printf '{"channel":"%s","ip_direct":"%s","ip_proxy":"%s","rc":%d}\n' \
    "$CHANNEL" "$IP_DIRECT" "$IP_PROXY" "$RC"
fi
exit $RC
