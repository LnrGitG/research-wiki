#!/usr/bin/env bash
# Выгрузка показателя fedstat (ЕМИСС) через резидентное окно.
#
# Кнопка «Скачать» — это POST /indicator/<id>/download с одноразовым Struts-токеном
# и cookie сессии; без токена приходит «CSRF блокировка», `data.do?format=excel`
# отдаёт 302. Токен берём GET-ом страницы показателя, затем POST с теми же cookie.
#
# Окно (tailscale exit node на ноутбуке) открывается на время выгрузки и снимается
# по trap: пока оно открыто, через ноутбук идёт весь исходящий трафик VPS.
#
#   scripts/fedstat_indicator_fetch.sh 34118 /tmp/34118.xls
set -uo pipefail

ID="${1:?укажите номер показателя ЕМИСС}"
OUT="${2:-/tmp/fedstat_${ID}.xls}"
export SUDO_ASKPASS="${SUDO_ASKPASS:-$HOME/.hermes/scripts/sudo_askpass.sh}"
NODE="${NODE:-100.114.29.93}"
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
JAR="$(mktemp)"

cleanup() {
  sudo -A tailscale set --exit-node= >/dev/null 2>&1
  rm -f "$JAR"
}
trap cleanup EXIT INT TERM

IP_BEFORE="$(curl -s -m 10 https://api.ipify.org || true)"
sudo -A tailscale set --exit-node="$NODE" --exit-node-allow-lan-access >/dev/null 2>&1 || {
  echo "не удалось включить exit node $NODE"; exit 65; }
for _ in $(seq 1 15); do
  sleep 2
  IP="$(curl -s -m 8 https://api.ipify.org || true)"
  [ -n "$IP" ] && [ "$IP" != "$IP_BEFORE" ] && break
done
echo "окно: ${IP_BEFORE:-?} → ${IP:-?}"

curl -s -m 40 -c "$JAR" -o /tmp/fedstat_page_${ID}.html -w "страница: %{http_code}\n" \
  -A "$UA" -H "Accept-Language: ru-RU,ru;q=0.9" "https://www.fedstat.ru/indicator/${ID}"

TOKEN="$(grep -o 'name="token" value="[^"]*"' /tmp/fedstat_page_${ID}.html | head -1 | sed 's/.*value="//;s/"//')"
[ -z "$TOKEN" ] && { echo "токен не найден — страница не открылась"; exit 66; }
echo "токен получен"

curl -s -m 180 -L -c "$JAR" -b "$JAR" -o "$OUT" \
  -w "файл: %{http_code}, %{size_download} байт, %{content_type}\n" \
  -A "$UA" -H "Accept-Language: ru-RU,ru;q=0.9" \
  -H "Referer: https://www.fedstat.ru/indicator/${ID}" \
  --data-urlencode "struts.token.name=token" --data-urlencode "token=$TOKEN" \
  --data-urlencode "id=${ID}" --data-urlencode "format=excel" \
  "https://www.fedstat.ru/indicator/${ID}/download"

# `file` на этом хосте отсутствует — проверяем сигнатуру сами
if [ -s "$OUT" ]; then
  SIG="$(head -c 8 "$OUT" | od -An -tx1 | tr -d ' \n')"
  case "$SIG" in
    d0cf11e0a1b11ae1) echo "формат: OLE2/xls ✓" ;;
    504b0304*)        echo "формат: xlsx (zip) — xlrd не прочтёт, нужен openpyxl" ;;
    *)                echo "формат неизвестен (сигнатура $SIG) — вероятно HTML-ошибка, проверить $JAR" ;;
  esac
fi
