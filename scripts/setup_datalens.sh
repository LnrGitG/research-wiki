#!/bin/bash
# Подготовка PostgreSQL на ВМ research-db к подключению из Yandex DataLens.
# Выполняется НА ВМ. Идемпотентно, с бэкапом конфигов.
set -e

PGVER=16
CONF=/etc/postgresql/$PGVER/main/postgresql.conf
HBA=/etc/postgresql/$PGVER/main/pg_hba.conf
STAMP=$(date +%Y%m%d-%H%M%S)

echo "=== 1. Бэкап конфигов ==="
sudo cp -n "$CONF" "$CONF.bak-$STAMP"
sudo cp -n "$HBA" "$HBA.bak-$STAMP"
echo "  $CONF.bak-$STAMP"
echo "  $HBA.bak-$STAMP"

echo ""
echo "=== 2. listen_addresses: localhost -> * ==="
sudo sed -i "s|^#\?listen_addresses\s*=.*|listen_addresses = '*'|" "$CONF"
sudo -u postgres grep -E "^listen_addresses" "$CONF"

echo ""
echo "=== 3. Роль datalens_ro (только чтение) ==="
PW=$(head -c 32 /dev/urandom | base64 | tr -d '/+=' | head -c 24)
sudo -u postgres psql -v ON_ERROR_STOP=1 <<SQL
DO \$\$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='datalens_ro') THEN
    CREATE ROLE datalens_ro LOGIN PASSWORD '$PW';
  ELSE
    ALTER ROLE datalens_ro LOGIN PASSWORD '$PW';
  END IF;
END
\$\$;
SQL
echo "  роль datalens_ro готова"

echo ""
echo "=== 4. Права: только SELECT на core/staging/meta/derived ==="
sudo -u postgres psql -v ON_ERROR_STOP=1 -d research_wiki <<'SQL'
GRANT CONNECT ON DATABASE research_wiki TO datalens_ro;
GRANT USAGE ON SCHEMA core, staging, meta, derived TO datalens_ro;
GRANT SELECT ON ALL TABLES IN SCHEMA core, staging, meta, derived TO datalens_ro;
ALTER DEFAULT PRIVILEGES IN SCHEMA core, staging, meta, derived
  GRANT SELECT ON TABLES TO datalens_ro;
SQL
echo "  права выданы"

echo ""
echo "=== 5. pg_hba: доступ с диапазонов DataLens ==="
# Диапазоны из официальной документации Yandex DataLens
RANGES="178.154.242.176/28 178.154.242.192/28 178.154.242.208/28 178.154.242.128/28 178.154.242.144/28 178.154.242.160/28 130.193.60.0/28"
# удаляем прежние наши строки, если были
sudo sed -i '/# DataLens$/d' "$HBA"
for r in $RANGES; do
  echo "host    all    all    $r    scram-sha-256    # DataLens" | sudo tee -a "$HBA" > /dev/null
done
sudo grep -c "DataLens" "$HBA" | xargs echo "  добавлено строк:"

echo ""
echo "=== 6. Пароль для DataLens -> файл ==="
CRED=/home/ubuntu/datalens_credentials.txt
umask 077
{
  echo "Yandex DataLens — параметры подключения"
  echo "Создано: $(date)"
  echo ""
  echo "Тип:            PostgreSQL"
  echo "Имя хоста:      89.169.168.214"
  echo "Порт:           5432"
  echo "База данных:    research_wiki"
  echo "Пользователь:   datalens_ro"
  echo "Пароль:         $PW"
  echo "SSL/TLS:        выключить (сертификат самоподписанный)"
  echo ""
  echo "Уровень SQL-запросов: 'SQL на чтение' (если нужны QL-чарты)"
} > "$CRED"
chmod 600 "$CRED"
echo "  $CRED"

echo ""
echo "=== 7. Перезапуск PostgreSQL ==="
sudo systemctl restart postgresql
sleep 4
sudo -u postgres psql -tAc "SHOW listen_addresses;" | xargs echo "  listen_addresses:"
sudo systemctl is-active postgresql | xargs echo "  статус:"

echo ""
echo "=== 8. Проверка: слушает ли порт наружу ==="
ss -tlnp 2>/dev/null | grep 5432 || sudo ss -tlnp | grep 5432

echo ""
echo "ГОТОВО"
