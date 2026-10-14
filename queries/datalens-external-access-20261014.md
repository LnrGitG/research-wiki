# Внешние подключения к research_wiki после замены ВМ (14.10.2026)

Записка фиксирует, как восстановлен внешний доступ к базе после того, как ВМ
`research-db` (зона `ru-central1-b`) стала недоступна, а база переехала на
`research-db-2` (зона `ru-central1-e`, публичный адрес 153.51.117.18). Прежний
адрес 89.169.168.214 в подключениях больше не работает: и тоннель, и объект
DataLens указывали на него.

## Что настроено на ВМ

Идемпотентный скрипт — `scripts/setup_datalens.sh` (переписан: принимает публичный
IP аргументом, сам поднимает TLS, сертификат перевыпускает при смене адреса).

| Параметр | Значение |
|---|---|
| `listen_addresses` | `*` (порт 5432 слушается на 0.0.0.0 и [::]) |
| TLS | `ssl = on`, свой УЦ `research-wiki-local-ca`, серверный сертификат `CN=153.51.117.18` |
| SAN сертификата | `IP:153.51.117.18, IP:127.0.0.1, DNS:localhost` |
| Открытая часть УЦ | `db_docs/certs/pg-ca.crt` (то же, что в DataLens) |
| `pg_hba` для `datalens_ro` | 7 подсетей DataLens (`178.154.242.128/28`, `.144/28`, `.160/28`, `.176/28`, `.192/28`, `.208/28`, `130.193.60.0/28`), `scram-sha-256` |
| `pg_hba` для `viewer` | `0.0.0.0/0` и `::/0` на базу `research_wiki`, `scram-sha-256` |
| Security group | ingress TCP 5432 «data lens» (0.0.0.0/0), ingress TCP 22 |

Роль `datalens_ro` остаётся read-only и не влияет на тарификацию DataLens: рабочее
место занимает человек, а не роль PostgreSQL. Пароли ролей `datalens_ro` и `viewer`
заданы из секретов Hermes (`DATALENS_RO_PASSWORD`, `DB_VIEWER_PASSWORD`); в репозиторий
и в переписку они не попадают. Роль `agent_ro` оставлена без пароля — она работает
только через тоннель/локально.

Права: `USAGE` + `SELECT ON ALL TABLES/SEQUENCES` + `ALTER DEFAULT PRIVILEGES` для
обеих ролей по рабочим схемам (`data`, `catalog`, `derived`, `core`, `ops`, `meta`,
`kb`, `dkp`, `graph`, `pipeline`, `marts`, плюс пустые `staging`, `v2`, `v2_stage`).

## Проверка (не отчёт, а факты)

С VPS (адрес 45.157.117.125 — вне диапазонов DataLens) библиотекой psycopg2:

- `viewer`, `sslmode=verify-full`, корень `db_docs/certs/pg-ca.crt` → **OK**:
  `user=viewer`, адрес сервера `10.132.0.4`, `ssl=True`, `catalog.metric` = 17 805 строк.
- `viewer`, `sslmode=require` → **OK** (TLS включён).
- `datalens_ro` с того же VPS → **отказ**: `FATAL: no pg_hba.conf entry for host
  "45.157.117.125", user "datalens_ro"` — то есть роль DataLens доступна только с
  подсетей сервиса, порт открыт не «всем как всем».
- `viewer` с заведомо неверным паролем → `password authentication failed` (scram работает).

Со стороны DataLens: объект подключения `rte58ecof5t4a` (`research-wiki-pg` в воркбуке
`wxaisbjylfeif`) переведён с 89.169.168.214 на 153.51.117.18 через
`POST /rpc/updateConnection`. Приёмка — обновление схемы четырёх датасетов
(`validateDataset` с `updates[0].action = refresh_source`), то есть реальное исполнение
SQL сервером DataLens по новому адресу с TLS:

| Датасет | Источник | Полей в ответе |
|---|---|---|
| `ds_rf_trend` (`swfpu2izqtsab`) | `PG_SUBSELECT` на `core.observation_v2` + `core.metric` | 5 |
| `ds_region_monthly` (`mq9joqmxxxnu5`) | `PG_SUBSELECT` | 8 |
| `ds_region_rating` (`48r16b0n8djqn`) | `PG_SUBSELECT` | 8 |
| `db_health` (`im5fktvy1uqm1`) | `PG_SUBSELECT` | 4 |

Все четыре датасета — через то же подключение `rte58ecof5t4a`, обновление прошло
без ошибок, число полей совпадает с записью сборки от 29.09.2026.

## Особенности API, которые стоит помнить

- `updateConnection` принимает тело `{connectionId, data: <ConnectionUpdate>}`; для
  postgres набор полей — из схемы `postgres2`. Успешный вызов возвращает **пустое тело**
  (204), поэтому `json.loads` на ответе падает — это **не** признак ошибки; факт
  применения проверять через `getConnection`.
- `getConnection` **не возвращает** `ssl_ca`, хотя принимает его при обновлении:
  наличие доверенного УЦ подтверждается только рабочей проверкой схемы датасета.
- `ssl_ca` принимается исключительно как data-URI:
  `data:application/x-x509-ca-cert;base64,<...>`.
- Датасеты, созданные в папку (а не в воркбук), в `getWorkbookEntries` не видны —
  искать через `listDirectory {path: "datasets/"}`.

## Что осталось на выбор владельца

- Правило security group на 5432 сейчас открыто на `0.0.0.0/0` (наследие прежней
  схемы, когда `viewer` ходил снаружи). Если внешний `viewer` с произвольных адресов
  не нужен, правило сужается до 7 подсетей DataLens плюс адрес VPS — конфигурация
  `pg_hba` к этому готова.
- Юниты-тоннели на прежний адрес (`hermes2-tunnel`, `jupyter-tunnel`, `xrdp-tunnel`,
  `code-server-tunnel`) не переводились: они не про базу, решение за владельцем.
