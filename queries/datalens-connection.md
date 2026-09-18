# Подключение Yandex DataLens к research_wiki

## Параметры подключения

| Поле | Значение |
|---|---|
| Тип | PostgreSQL |
| Имя хоста | `89.169.168.214` (публичный IP ВМ `research-db`) |
| Порт | `5432` |
| База данных | **`research_wiki`** |
| Пользователь | `datalens_ro` |
| Пароль | в `/home/ubuntu/datalens_credentials.txt` на ВМ (chmod 600) |
| SSL/TLS | **выключить** (сертификат самоподписанный) |
| Уровень SQL-запросов | «SQL на чтение» — если нужны QL-чарты |

Имя базы — `research_wiki`, не `research_db`.

## Что было сделано на ВМ

Скрипт: `scripts/setup_datalens.sh` (идемпотентен, делает бэкап конфигов).

1. `listen_addresses`: `localhost` → `*` (PostgreSQL слушал только локально).
2. Создана роль `datalens_ro` с правом только `SELECT` на схемы
   `core`, `staging`, `meta`, `derived` — плюс `ALTER DEFAULT PRIVILEGES`,
   чтобы права распространялись на будущие таблицы.
3. В `pg_hba.conf` добавлен доступ с семи IPv4-диапазонов DataLens
   (из официальной документации):
   `178.154.242.128/28`, `.144/28`, `.160/28`, `.176/28`, `.192/28`,
   `.208/28`, `130.193.60.0/28`.
4. Перезапуск PostgreSQL, проверка `LISTEN 0.0.0.0:5432`.

Бэкапы конфигов: `/etc/postgresql/16/main/*.bak-<дата>`.

## Проверки

- Роль `datalens_ro` читает `core.observation_v2` — 1 091 497 строк.
- Подключение **снаружи** по публичному IP проверено: работает, `staging`
  доступен (305 130 строк).
- Посторонний IP отклоняется (`no pg_hba.conf entry`) — доступ ограничен
  диапазонами DataLens, не открыт всему интернету.

## Известный риск: SSL

Документация DataLens противоречива. Страница «Подключение к источнику
данных» требует сертификат, подписанный удостоверяющим центром:
«Вы не сможете создать подключение в DataLens, если на стороне БД
используется самоподписанный SSL-сертификат». При этом страница создания
подключения к PostgreSQL содержит переключатель **TLS** (выключен →
`sslmode=prefer`).

На ВМ стоит самоподписанный `ssl-cert-snakeoil.pem`, выданных УЦ нет.

**Порядок действий:** в форме подключения выключить TLS и нажать «Проверить
подключение». Если DataLens откажет из-за сертификата — варианты:
1. получить сертификат Let's Encrypt на домен (нужен домен, у ВМ только
   `epd1a9b94f8pskro2uh9.auto.internal` — внутреннее имя, публичного нет);
2. поднять Managed PostgreSQL с опцией «Доступ из DataLens» и перелить
   данные (в облаке таких кластеров сейчас нет).

## Откат

```bash
sudo cp /etc/postgresql/16/main/postgresql.conf.bak-<дата> /etc/postgresql/16/main/postgresql.conf
sudo cp /etc/postgresql/16/main/pg_hba.conf.bak-<дата> /etc/postgresql/16/main/pg_hba.conf
sudo systemctl restart postgresql
sudo -u postgres psql -c "DROP ROLE datalens_ro;"
```

## Замечания по безопасности

- Роль только для чтения: `SELECT` на четырёх схемах, без прав на запись.
- Порт 5432 открыт **не** всему интернету: security group `ssh-access-sg`
  пропускает `0.0.0.0/0`, но фактическое ограничение задаёт `pg_hba.conf`
  по диапазонам DataLens.
- Пароль хранится только на ВМ в файле с правами 600; в репозиторий и в
  переписку не попадает. При необходимости легко ротируется:
  `ALTER ROLE datalens_ro PASSWORD '<новый>'`.

---

## Представление для датасета

Помимо сырых таблиц создано представление `core.v_datalens_observations` —
наблюдения с подставленными человекочитаемыми названиями. Оно избавляет от
ручной настройки связей в датасете: `core.observation_v2` хранит числовые
идентификаторы (`metric_id`, `region_id`), а в графиках нужны названия.

Скрипт: `scripts/make_datalens_view.py` (идемпотентен, `CREATE OR REPLACE VIEW`).

Состав (29 колонок, сгруппированы по смыслу):

| группа | колонки |
|---|---|
| когда | `period_start`, `period_end`, `year`, `month`, `quarter`, `frequency_code`, `frequency_name` |
| что | `metric_code`, `metric_name`, `metric_short_name`, `metric_type`, `is_derived`, `metric_tags`, `unit_code`, `unit_name` |
| где | `region_code`, `region_name`, `region_level`, `oktmo` |
| значение | `value`, `value_str`, `sub_dimension`, `assessment_type`, `observation_status`, `quality_flags` |
| откуда | `source_code`, `source_name`, `release_label`, `published_at` |

Соединения: `metric`, `region`, `frequency`, `unit`, `source`, `release` — все
через `LEFT JOIN`, чтобы наблюдение не терялось при отсутствии справочной записи.

Проверки:

```
строк:                              1 091 497
без названия метрики или региона:           0
метрик:                                   421
регионов:                                  97
источников:                                 4
```

Контрольный пример (`y477050017` / Вологодская область / 2024) через
представление возвращает те же 6 направлений инвестиций с подписями.

Права: `GRANT SELECT ON core.v_datalens_observations TO datalens_ro`.

### Как строить датасет

1. Подключение — `research_wiki` (уже настроено).
2. В датасете выбрать таблицу `core.v_datalens_observations`.
3. Связи настраивать не нужно — названия уже подставлены.
4. Измерения: `region_name`, `metric_name`, `year`, `sub_dimension`, `source_name`.
5. Показатель: `value`.

Оговорка: для исследовательских срезов бывает нужно соединять с другими
таблицами (`staging.regions_panel__panel`, `core.metric` целиком) — они тоже
доступны роли, `SELECT` выдан на все четыре схемы.
