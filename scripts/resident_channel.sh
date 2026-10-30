#!/usr/bin/env bash
# Резидентный канал: запуск на ноутбуке (WSL/Linux/macOS).
#
# Что делает: поднимает локальный HTTP-прокси на 127.0.0.1 и пробрасывает его
# назад на VPS через обратный SSH-туннель. После этого VPS видит прокси на
# 127.0.0.1:18080 и выходит в сеть с домашнего адреса Уфанет — то, что нужно для
# api.hh.ru, fedstat.ru (ЕМИСС) и дом.рф, закрытых для датацентр-IP.
#
# Запуск одной командой (скрипт забирается с VPS по SSH, копировать руками не надо):
#
#   ssh lnr@45.157.117.125 'cat ~/research-wiki-private/scripts/resident_channel.sh' | bash
#
# С параметрами:
#
#   ... | bash -s -- --port 18080 --token <TOKEN>
#
# Важно: перед запуском выключить VPN — иначе «резидентным» окажется адрес
# VPN-выхода, и api.hh.ru всё равно ответит 403. Скрипт печатает внешний адрес
# и предупреждает, если он не похож на домашний.
#
# Остановить — Ctrl-C: туннель и прокси снимаются вместе.
set -uo pipefail

VPS="${VPS:-lnr@45.157.117.125}"
PORT=18080
TOKEN=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --port) PORT="$2"; shift 2 ;;
    --token) TOKEN="$2"; shift 2 ;;
    --vps) VPS="$2"; shift 2 ;;
    *) echo "неизвестный параметр: $1" >&2; exit 64 ;;
  esac
done

need() { command -v "$1" >/dev/null 2>&1 || { echo "нет $1 — установите и повторите" >&2; exit 69; }; }
need ssh
need python3
need curl

TMP="$(mktemp -d)"
PROXY_PID=""
cleanup() {
  [[ -n "$PROXY_PID" ]] && kill "$PROXY_PID" 2>/dev/null
  rm -rf "$TMP"
}
trap cleanup EXIT INT TERM

echo "[1/4] забираю прокси с VPS"
if ! ssh -o ConnectTimeout=15 "$VPS" 'cat ~/research-wiki-private/scripts/resident_proxy.py' > "$TMP/resident_proxy.py"; then
  echo "не удалось прочитать прокси с $VPS (нет SSH-доступа?)" >&2
  exit 70
fi
[[ -s "$TMP/resident_proxy.py" ]] || { echo "получен пустой файл прокси" >&2; exit 71; }

echo "[2/4] внешний адрес без туннеля"
IP_NOW="$(curl -s -m 10 https://ipinfo.io/ip || true)"
echo "      ${IP_NOW:-не определён}"
case "$IP_NOW" in
  45.157.117.125|89.169.*|153.51.*) echo "      ВНИМАНИЕ: это адрес датацентра/VPN — выключите VPN, иначе канал бесполезен" ;;
esac

echo "[3/4] локальный прокси 127.0.0.1:${PORT}"
python3 "$TMP/resident_proxy.py" --port "$PORT" ${TOKEN:+--token "$TOKEN"} &
PROXY_PID=$!
sleep 1
kill -0 "$PROXY_PID" 2>/dev/null || { echo "прокси не поднялся (порт занят?)" >&2; exit 72; }

echo "[4/4] обратный туннель на $VPS"
echo "      на VPS проверить:  scripts/resident_check.sh ${PORT}${TOKEN:+ $TOKEN}"
echo "      остановить:        Ctrl-C"
exec ssh -N -T \
  -o ExitOnForwardFailure=yes \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -R "127.0.0.1:${PORT}:127.0.0.1:${PORT}" \
  "$VPS"
