#!/bin/bash
# Настройка внешних подключений PostgreSQL к ВМ research-wiki (DataLens + внешний viewer).
# Выполняется НА ВМ. Идемпотентно, с бэкапом конфигов.
#
# Использование:  sudo bash setup_datalens.sh [<публичный-IP-ВМ>]
# Пароли ролей скрипт НЕ задаёт: их прогоняет отдельно из секретов Hermes,
# чтобы секрет не попал ни в аргументы, ни в журнал шелла.
#
# Шаги, каждый обязателен (пропуск даёт свою ошибку):
#   1. listen_addresses = '*'      — иначе снаружи порт не открывается;
#   2. свой УЦ + сертификат с IP SAN — snakeoil DataLens не принимает;
#   3. pg_hba: 7 диапазонов DataLens для datalens_ro + 0.0.0.0/0 для viewer;
#   4. права ролям — отдельным SQL из секретов.
set -e

PGVER=16
PUBIP="${1:-$(curl -s --max-time 5 ifconfig.me || true)}"
CONF=/etc/postgresql/$PGVER/main/postgresql.conf
HBA=/etc/postgresql/$PGVER/main/pg_hba.conf
CERTDIR=/etc/postgresql/$PGVER/main/certs
STAMP=$(date +%Y%m%d-%H%M%S)

if [ -z "$PUBIP" ]; then echo "не задан публичный IP (аргументом или через ifconfig.me)"; exit 1; fi
echo "Публичный IP ВМ: $PUBIP"

echo "=== 1. Бэкап конфигов ==="
cp -n "$CONF" "$CONF.bak-$STAMP"
cp -n "$HBA" "$HBA.bak-$STAMP"
ls -1 "$CONF.bak-$STAMP" "$HBA.bak-$STAMP"

echo "=== 2. listen_addresses = '*' ==="
sed -i "s|^#\?listen_addresses\s*=.*|listen_addresses = '*'|" "$CONF"
grep -E "^listen_addresses" "$CONF"

echo "=== 3. Сертификаты (свой УЦ, SAN с текущим IP) ==="
mkdir -p "$CERTDIR"; cd "$CERTDIR"
# Сертификат перевыпускается, если IP не совпадает с текущим: старый SAN после
# смены адреса ВМ ломает verify-full у DataLens.
if [ ! -f server.crt ] || ! openssl x509 -in server.crt -noout -ext subjectAltName | grep -q "$PUBIP"; then
  openssl req -new -x509 -days 3650 -nodes -newkey rsa:2048 \
    -keyout ca.key -out ca.crt -subj "/CN=research-wiki-local-ca" 2>/dev/null
  openssl req -new -nodes -newkey rsa:2048 \
    -keyout server.key -out server.csr -subj "/CN=$PUBIP" 2>/dev/null
  printf 'subjectAltName = IP:%s, IP:127.0.0.1, DNS:localhost\nextendedKeyUsage = serverAuth\n' "$PUBIP" > san.cnf
  openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
    -out server.crt -days 3650 -extfile san.cnf 2>/dev/null
  rm -f server.csr ca.srl
fi
chown postgres:postgres ca.key ca.crt server.key server.crt
chmod 600 ca.key server.key; chmod 644 ca.crt server.crt
openssl x509 -in server.crt -noout -subject -ext subjectAltName
echo "открытая часть УЦ для DataLens: $CERTDIR/ca.crt"

echo "=== 4. SSL в postgresql.conf ==="
sed -i "s|^#\?ssl\s*=.*|ssl = on|" "$CONF"
sed -i "s|^#\?ssl_cert_file\s*=.*|ssl_cert_file = '$CERTDIR/server.crt'|" "$CONF"
sed -i "s|^#\?ssl_key_file\s*=.*|ssl_key_file = '$CERTDIR/server.key'|" "$CONF"
sed -i "s|^#\?ssl_ca_file\s*=.*|ssl_ca_file = '$CERTDIR/ca.crt'|" "$CONF"
grep -E "^ssl(_cert_file|_key_file|_ca_file)? " "$CONF"

echo "=== 5. pg_hba: диапазоны DataLens + внешний viewer ==="
# Диапазоны из официальной документации DataLens; сверять при каждом прогоне.
sed -i '/# DataLens$/d'   "$HBA"
sed -i '/# ext-viewer$/d' "$HBA"
for r in 178.154.242.128/28 178.154.242.144/28 178.154.242.160/28 \
         178.154.242.176/28 178.154.242.192/28 178.154.242.208/28 130.193.60.0/28; do
  echo "host    research_wiki    datalens_ro    $r    scram-sha-256    # DataLens" >> "$HBA"
done
echo "host    research_wiki    viewer    0.0.0.0/0    scram-sha-256    # ext-viewer" >> "$HBA"
echo "host    research_wiki    viewer    ::/0         scram-sha-256    # ext-viewer" >> "$HBA"
tail -12 "$HBA"
echo "в security group должен быть открыт ingress TCP 5432 (правило «data lens»)"

echo "=== 6. Перезапуск и самотест ==="
systemctl restart postgresql
sleep 5
systemctl is-active postgresql
ss -tlnp | grep 5432 || true
echo | openssl s_client -connect 127.0.0.1:5432 -starttls postgres -CAfile "$CERTDIR/ca.crt" 2>/dev/null \
  | grep -E "Verify return code|subject="
echo "ГОТОВО (пароли ролей и права — отдельным SQL из секретов Hermes)"
