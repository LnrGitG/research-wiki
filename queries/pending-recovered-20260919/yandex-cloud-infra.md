## Фазовая работа с чекпойнтами
Многофазные инфраструктурные работы (развёртывание ВМ/БД, миграция) вести
фазами и **останавливаться на границе фазы для доклада и проверки**, а не
прогонять все фазы подряд. Формат отчёта на границе: что сделано, что
проверено и чем именно, какие расхождения с планом обнаружены, что
следующее. Пользователь явно просит такие остановки («остановись после Ф<N>
для проверки») и ожидает, что фаза доведена до проверяемого состояния.
Перед остановкой — не оставлять работу в промежуточном состоянии: либо
фаза закрыта, либо явно сказано, где именно прервано.
1. **yc CLI** — основной путь. Авторизация сервисным аккаунтом через authorized key (`yc config list` показывает блок `service-account-key`) даёт полный доступ к Compute/VPC/Storage/IAM. Различать два ключа: `AQVN…` API-ключ в `.env` — только Translate/Vision/S3-sign (Compute → 401); authorized key сервисного аккаунта в `~/.config/yandex-cloud/` — всё остальное.
2. **REST с IAM-токеном** (`yc iam create-token`) — когда нужен прямой HTTP.
3. **MCP Toolkit** (`@yandex-cloud/mcp -s toolkit`) — опционален, покрытие то же.
## Первичная настройка yc CLI
- Бинарь обычно в `~/yandex-cloud/bin/yc`, но в `PATH` его нет: `.bashrc` подключает `path.bash.inc`, а неинтерактивные shell-сессии его не читают. Постоянное решение — симлинк: `ln -sf ~/yandex-cloud/bin/yc ~/.local/bin/yc` (плюс `docker-credential-yc`). После этого `yc` доступен без export.
## Грабли yc CLI (проверено)
- **Флаг правила SG**: свойство называется `v4-cidrs=`, не `cidr=`. Рабочая форма:
  `yc vpc security-group update-rules <SG_ID> --add-rule "direction=egress,protocol=any,from-port=0,to-port=65535,v4-cidrs=0.0.0.0/0"`.
- **EGRESS обязателен**: группа с одними INGRESS-правилами блокирует и ответный трафик — входящий SYN доходит, ответный SYN-ACK не уходит, соединение висит до таймаута. Симптом «ВМ жива, порт открыт, но ssh/nc не подключаются» = нет egress-правила.
- **Образ по family не находится**: `--create-boot-disk image-family=ubuntu-2404-lts` → `Image not found`. Сначала взять ID: `yc compute image get-latest-from-family ubuntu-2404-lts --folder-id standard-images --format json`, затем `image-id=<id>`.
- **ssh-keys в метаданных**: инлайн `--metadata ssh-keys=…` молча не применяется. Работает `--metadata-from-file ssh-keys=/tmp/key.txt` (файл в формате `user:ssh-ed25519 AAAA… comment`). Проверять через `yc compute instance get <id> --full` — в `--format json` блок метаданных не виден.
- **Вход по ключу отключён OS Login**: при `serial_port_settings.ssh_authorization: OS_LOGIN` ключ из метаданных не действует, `yc compute ssh` требует организации. Переключать при создании: `--serial-port-settings ssh-authorization=instance_metadata`.
- **user-data выполняется один раз на instance**. Добавление user-data к уже созданной ВМ ничего не делает (cloud-init помнит instance-id). Нужен пересозданный инстанс или явный `cloud-init clean && cloud-init`.
- **Скрипт в метаданных искажается**: спецсимволы ломаются при передаче. Всегда кодировать: `B64=$(base64 -w0 script.sh)` и в user-data писать `echo "$B64" | base64 -d > /tmp/s.sh; bash /tmp/s.sh`.
## Управление ВМ, когда SSH недоступен
Порт 22 YC-ВМ заблокирован для зарубежных адресов гео-фильтром (проверка через check-host.net: российский узел подключается за ~35 мс, Германия/США — таймаут), при этом из России SSH работает. Если рабочий хост зарубежный — канал управления строить через S3-бакет.
Схема (проверена): systemd-сервис с бесконечным циклом опрашивает бакет, забирает `_cmd/command.sh`, сравнивает его md5 со сохранённым хешем, выполняет и выгружает вывод в `_cmd/output.txt`.
Ключевые моменты:
- **GET, не HEAD**: HEAD-запрос к объекту с IAM-токеном не отдаёт etag — сравнение по хешу скачанного файла надёжнее.
- **IAM-токен из метаданных**: `curl -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token`. С ним S3 API работает **без статических ключей** — заголовок `X-YaCloud-SubjectToken: $T`.
- Обмен работает в обе стороны (PUT/GET/list проверены и с ВМ, и с зарубежного VDS) — отдельный статический ключ не нужен.
- Ограничение: команды идут от root, доступ к бакету = выполнение кода. Для одного пользователя приемлемо; при расширении доступа — подписывать команды.
Полный рецепт с bootstrap-скриптом: `references/vm-management-without-ssh.md`.
- `references/vm-management-without-ssh.md` — канал управления через S3-бакет: bootstrap, агент, диагностика.
## DataLens: доступ по API
Роли DataLens назначаются **на организацию**, а не на каталог. Консоль облака открывается на
уровне облака/каталога: всё добавленное в разделе прав там ложится на каталог, и API отвечает
`Auth denied` на все методы, включая `getCurrentUser` (SA не может прочитать даже организацию).
`add-access-binding` на организацию из-под SA → `Permission denied`.
Даже с верными правами бесплатный тариф даёт **1 рабочее место на организацию**, а у сервисного
аккаунта места нет → API отвечает `LICENSE_IS_REQUIRED`. Прочитать состояние лицензий
(`getLicenses`/`getLicensesLimit`) SA может, назначить — нет. Полная матрица кодов ошибок,
пробы и сценарий ручной сборки датасета: `references/datalens-api-auth.md`.
- `references/datalens-api-auth.md` — DataLens API: уровень назначения ролей, матрица кодов отказа, лицензии/рабочие места, подключение к PostgreSQL (pg_hba + TLS), гигиена ключей SA.
Облако Ленара: Translate/OCR API-ключ (AQVN…) живёт в `~/.hermes/.env`, его скоуп = Translate + Vision + S3-sign, **не Compute** (Compute по нему → 401; Resource Manager требует Bearer IAM-токен, API-ключ не подходит). Сценарий «тяжёлые БД»: бакет + ВМ.
**Но это ограничение только API-ключа.** Авторизованный ключ сервисного аккаунта (RSA, `yc config` → `service-account-key`) даёт `yc` CLI полный доступ, включая Compute: ВМ создаются/удаляются/перезапускаются командами, Object Storage и VPC — тоже. Проверять фактически: `yc iam create-token` + `yc compute instance list` — если оба отвечают, ключ полный. Ставить `yc` в PATH: симлинк в `~/.local/bin/yc`, иначе в non-interactive shell Hermes `~/.bashrc` не читается и бинарь «не находится».
5. **S3-канал команд** — основной способ управления ВМ, когда SSH недоступен (см. ниже). Годится и для start/stop, и для выполнения произвольных команд.
1. **yc CLI** — основной путь. Бинарь `~/yandex-cloud/bin/yc` (не в PATH по умолчанию: симлинк в `~/.local/bin/yc`, он в PATH). Авторизация — ключ сервисного аккаунта (`~/.config/yandex-cloud/config.yaml`), NOT OAuth: `service-account-key` + `cloud-id` + `folder-id`. Проверено: `yc iam create-token` → OK, Compute/VPC/Storage/IAM доступны (SA `compute-as` несёт `editor`, `compute.editor/operator`, `storage.admin/editor/viewer`, `iam.serviceAccounts.admin`).
2. **MCP Toolkit** (`@yandex-cloud/mcp -s toolkit`, stdio, OAuth) — резерв.
3. REST с API-ключом `AQVN…` — только Translate/Vision/S3; для Compute не годится (401).
`yc` в PATH: если команда не найдена — это не «CLI не установлен», а отсутствие симлинка; `ln -sf ~/yandex-cloud/bin/yc ~/.local/bin/yc` (там же `docker-credential-yc`).
## Сетевая доступность из YC (ru-central1) — замерено
Ключевой вывод: **география YC-IP не совпадает с географией домашнего RU-IP.** Что открыто с бытового провайдера (или с третьесторонних RU-нод), может быть закрыто из датацентра. Проверять фактически, не обобщать.
- **Telegram НЕДОСТУПЕН** из YC: `api.telegram.org`, `web.telegram.org`, `t.me`, `telegram.org` → `errno 101 Network is unreachable`. Блокировка по SNI на уровне DPI: часть IP Telegram отвечает на TCP, но TLS-рукопожатие виснет. **Следствие: gateway с Telegram-каналом в YC не переносить** — оставлять на зарубежном VDS, направлять трафик туннелем, если понадобится обратное.
- **Зарубежные LLM geo-блокированы**: OpenAI → 403 `unsupported_country_region_territory`, OpenRouter → 403 `Access denied by security policy`, Anthropic → 403, Google AI → 403. **Ollama Cloud → 200, Moonshot → 401 (доступен, нужен ключ)** — то есть провайдер по умолчанию работает, а fallback на OpenRouter из YC не сработает.
- **RU-источники открыты** (ради чего YC и нужен): fedstat.ru (ЕМИСС), rosstat.gov.ru, cbr.ru, bo.nalog.gov.ru, clearspending.ru, zakupki.gov.ru, roschart.ru → все 200. Резидентный IP закрывает гео-блок ЕМИСС без обратного туннеля с ноутбука.
- **Инфраструктурное открыто**: github.com, api.github.com, huggingface.co, pypi.org, registry.npmjs.org, storage.yandexcloud.net, oauth.yandex.ru. `storage.googleapis.com` → 400 (не 403 — жив, но требует корректного запроса).
- Полная таблица замеров + рецепт зондирования: `references/yc-network-reachability.md`.
## Pitfall: Security Group только с INGRESS блокирует EGRESS ⚠️
В YC при наличии хотя бы одного правила группы весь остальной трафик **блокируется по умолчанию**, включая ответный. Группа с единственным `INGRESS TCP 22` даёт эффект «порт 22 не отвечает, SSH виснет по таймауту, при этом ВМ живая и в консоли дошла до логина» — входящий SYN доходит, ответный SYN-ACK наружу не уходит.
Параметр называется **`v4-cidrs`**, не `cidr` — `cidr=` отбивается `unknown property 'cidr'`. Проверять после правки: `yc vpc security-group get <id> --format json`.
Диагностический признак «это сеть, а не sshd»: ВМ `RUNNING`, serial console показывает `reached target multi-user` и приглашение логина, а `nc -vz <ip> 22` даёт таймаут. Если при этом порт закрыт и с внешних нод — смотреть правила SG, а не sshd.
## Pitfall: создание ВМ — образ и метаданные
- `--create-boot-disk image-family=ubuntu-2404-lts` → `NotFound`: семейства видны только из каталога образов. Либо `image-id=<id>` напрямую, либо `--folder-id standard-images` при поиске: `yc compute image get-latest-from-family ubuntu-2404-lts --folder-id standard-images`.
- Ключ в метаданные не всегда садится через `--metadata "ssh-keys=lnr:<pub>"` (команда отвечает `done`, а метаданные пусты). Рабочий путь — файлом: `printf 'lnr:%s' "$(cat ~/.ssh/id_yc.pub)" > /tmp/k.txt` и `yc compute instance update <id> --metadata-from-file ssh-keys=/tmp/k.txt`.
- `yc compute instance get` **не показывает** `metadata` и вообще урезан; для метаданных — `--full` или `--format json | jq`.
- Вход по SSH на образе `ubuntu-2404-lts-oslogin` ограничен OS Login: `serial-port-settings.ssh_authorization: OS_LOGIN`, а `yc compute ssh --login <user>` падает `OS login info not found for subject`, если у SA нет роли на организацию (`oslogin get-settings` → PermissionDenied). Переключение на ключи из метаданных: `--serial-port-settings ssh-authorization=instance_metadata` + ключ в метаданные, затем restart.
## Размер и стоимость ВМ (цены РФ с НДС, 720 ч/мес)
| 4×100% IceLake, 8 ГБ, 60 ГБ SSD, CVoS 1 год | ~5 500 |
| Managed PostgreSQL (мин. кластер 1 хост 2/8 + 100 ГБ SSD) | ~7 200 |
## Recipe: зондирование сети из облачного IP без SSH
Когда SSH недоступен (зарубежный IP, нет ключей, OS Login) — прогнать проверки через cloud-init и прочитать результат из serial console:
1. Скрипт-зонд → base64 → `user-data` (метаданные манглят многострочный скрипт, base64 обязателен).
2. `yc compute instance create --name <probe> --preemptible --metadata-from-file user-data=/tmp/ci.sh`.
3. Через ~90 с: `yc compute instance get-serial-port-output <id>` → grep по маркерам.
4. **Удалить зонд сразу** — прерываемая ВМ тикает, пока живёт.
Устанавливать `curl` явно: в минимальном образе его нет, и проверки вернут пустые коды без ошибки. Готовый рецепт и скрипт — `references/yc-network-reachability.md`.
## Третьесторонняя проверка доступности (когда свой IP мешает)
`check-host.net` отвечает за любую географию, в отличие от собственного канала:
# → request_id; затем:
То же с `check-http?host=https://<url>`. Полезно, чтобы отличить «источник закрыт для меня» от «источник закрыт для всех». Именно так установлено, что порт 22 YC-ВМ открыт из РФ и закрыт из DE/US. Без `node=` выборка случайна и RU-нод может не оказаться — указывать явно.
- `references/yc-network-reachability.md` — замеры доступности из YC + скрипт-зонд через serial console.
**Ключ сервисного аккаунта ≠ API-ключ.** Для Compute/VPC/IAM нужен *authorized key* сервисного аккаунта (`yc iam key create`, RSA_2048), а не AQVN-ключ. Проверять наличие: `yc config list` (показывает `service-account-key.id`). При наличии такого ключа `yc` CLI даёт ПОЛНЫЙ доступ к Compute/VPC/Storage — создание ВМ, диски, группы безопасности, бакеты. MCP Toolkit и Cloud Functions для этого не нужны.
`yc` может не быть в `PATH` (бинарь в `~/yandex-cloud/bin/yc`, а non-interactive shell не читает `.bashrc`). Лечится симлинком: `ln -sf ~/yandex-cloud/bin/yc ~/.local/bin/yc` — `~/.local/bin` уже в PATH.
1. **`yc` CLI** — основной путь при наличии authorized key сервисного аккаунта (см. выше). Полное управление Compute/VPC/Storage в одну строку.
2. **MCP Toolkit** (`@yandex-cloud/mcp -s toolkit`, stdio, OAuth) — когда authorized key нет; OAuth обходит скоупы API-ключа.
3. REST с AQVN API-ключом — только Translate/Vision/S3; для Compute не годится.
4. Cloud Functions + API Gateway — не нужны ни для start/stop VM, ни для оркестрации: заменяются каналом через S3 (ниже).
## Pitfall: SSH с зарубежного IP не работает — нужен канал через S3 ⚠️
Гео-фильтр YC режет порт 22 для зарубежных адресов. Проверено: с российского узла TCP 22 отвечает ~35 мс, из Германии и США — timeout. При этом **порт 443 (управление, API) и S3 работают отовсюду**. Диагностика «блокировка на моей стороне или у сервиса» — `check-host.net`: `curl -s "https://check-host.net/check-tcp?host=HOST:PORT&node=ru3.node.check-host.net"`, затем GET `check-result/<request_id>`. RU-узел OK + foreign-узлы timeout = гео-блок, а не падение сервиса.
**Рабочий канал управления ВМ без SSH — S3-агент.** systemd-сервис на ВМ опрашивает бакет, забирает команду по хешу, выполняет, выгружает вывод. Команда: `put-object` ключа `_cmd/command.sh`; результат читается из `_cmd/output.txt`. Схема: `references/vm-s3-command-channel.md`.
Три питфолла, стоившие итераций:
- **HEAD-запрос к S3 с IAM-токеном не работает** (`head-object` отдаёт пусто) — опрашивать наличие команды через **GET** и проверять HTTP-код ответа.
- **`yc compute instance update --metadata user-data=...` НЕ запускает cloud-init на существующей ВМ** — user-data исполняется один раз при создании. Чтобы прогнать bootstrap, ВМ надо **пересоздать** с `--metadata-from-file user-data=...`.
- **Long-running команду запускать через `systemd` Type=simple + Restart=always**, а не timer/oneshot: oneshot с внешним таймером не переживает ошибку и не логирует причину. Логи писать в файл (`/var/log/...`) И в `/dev/console` — консоль читается через `yc compute instance get-serial-port-output`, это единственный доступный канал, когда SSH закрыт.
**IAM-токен изнутри ВМ** (для S3 без статических ключей): `curl -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token`. Далее запросы к S3 с заголовком `X-YaCloud-SubjectToken: <token>` — работают и PUT, и GET, и list.
**Готовые реквизиты аккаунта** (проверено): зона `ru-central1-b`, подсеть `e2lihlksrvl26ukhrcef`, группа безопасности `enpeaib2jcgjfab3hg63` (`ssh-access-sg`), образ `fd8nj6iro13qffg31not` (ubuntu-24-04-lts). **Группе безопасности нужен EGRESS-rule**, иначе ответные пакеты блокируются и SSH висит по таймауту: `yc vpc security-group update-rules enpeaib2jcgjfab3hg63 --add-rule "direction=egress,protocol=any,from-port=0,to-port=65535,v4-cidrs=0.0.0.0/0"`. Параметр называется `v4-cidrs`, не `cidr`.
**Образы искать с `--folder-id standard-images`** — без него `--create-boot-disk image-family=...` падает с NotFound. Надёжнее явный `image-id`.
**Размер ВМ под PostgreSQL + сборщик + cron**: 4×20% vCPU / 8 ГБ RAM / 60 ГБ network-SSD ≈ 4 300 ₽/мес, постоянная. 20% vCPU достаточно (агент ждёт API, не считает). 8 ГБ (не 4) — pandas при разборе Росстата пиково съедает ~2 ГБ. Managed PostgreSQL дороже самой ВМ (~7 200 ₽/мес) → самогестед на той же машине.
## Сервисы YC, полезные в пайплайне (проверено)
- **Векторный поиск** — `pgvector` в существующем PostgreSQL (0 ₽ сверху) вместо Managed OpenSearch (~7 800 ₽/мес минимум — неоправданно для 689 страниц).
- **Визуализация** — DataLens: **одно рабочее место НЕ тарифицируется** (второе+ 990 ₽/мес). Убирает `data-summary.json` как промежуточный слой и проблему кэша при просмотре с телефона.
- **Search API** — брать **отложенный режим**: 30,5 ₽/1000 запросов против 488 ₽ синхронных (в 16 раз дешевле). Включает Wordstat `GetTop`/`GetDynamics` (20 ₽) и `GetRegionsDistribution` (50 ₽) — путь к региональному nowcast спроса.
- **Векторизация AI Studio** — 0,0101 ₽/1000 токенов.
- **AI Studio модели** (от 0,1 ₽/1000 ток.) доступны из YC, в отличие от OpenAI/Anthropic (гео-блок) — важно, если агент переедет в YC.
- `references/vm-s3-command-channel.md` — рабочая реализация канала управления ВМ через S3 (bootstrap + агент + диагностика).
- `references/datalens-connection.md` — подключение Yandex DataLens к PostgreSQL на собственной ВМ:
  4 шага (listen_addresses → роль read-only с ALTER DEFAULT PRIVILEGES → pg_hba по диапазонам
  DataLens → свой УЦ с IP SAN вместо snakeoil), параметры формы подключения,
  питфоллы (дефис в имени БД, SSL verify failed), тарификация рабочих мест,
  разница между ролью в БД и рабочим местом DataLens.
1. **yc CLI** — основной инструмент, когда он авторизован сервисным аккаунтом (`yc config list` показывает `service-account-key` + cloud-id/folder-id). Бинарь ставится в `~/yandex-cloud/bin/yc` и **не попадает в PATH** неинтерактивных сессий Hermes (shell не читает `.bashrc`): сделать симлинк `ln -sf ~/yandex-cloud/bin/yc ~/.local/bin/yc` — `~/.local/bin` уже в PATH. Проверять `yc --version` без export.
2. **MCP Toolkit** (`@yandex-cloud/mcp -s toolkit`, stdio, OAuth) — покрывает Compute/VPC/IAM/Storage, OAuth обходит скоупы API-ключа.
3. REST с API-ключом (AQVN…) — только Translate/Vision/S3; для Compute не годится без расширения скоупа.
## Доступ к ВМ: что проверено ⚠️
- **SSH на порт 22 с зарубежного IP (VPS во Франкфурте) не проходит** — таймаут. Проверка через `check-host.net` показала: узлы в РФ (СПб) подключаются за ~18 мс, узлы DE/US получают timeout. То есть порт открыт и доступен из России, но блокируется для зарубежных адресов. Не тратить время на «починить SSH» с VPS — либо работать из РФ-IP, либо использовать serial console / probe-VM (см. reference).
- **Serial console читается через API без SSH**: `yc compute instance get-serial-port-output <id>` — рабочий канал для диагностики и для запуска скриптов на ВМ, когда SSH недоступен.
- **OS Login на сервисный аккаунт не работает**: `yc compute ssh --login <user>` падает с «OS login info not found», `oslogin get-settings` — PermissionDenied (нет роли на организацию). Переключать ВМ на обычные SSH-ключи: `--serial-port-settings ssh-authorization=instance_metadata` + ключ в metadata.
## Pitfall: флаги yc CLI, на которых легко застрять ⚠️
- **`--image-family ubuntu-2404-lts` → NotFound.** Нужен либо явный `--create-boot-disk image-id=<id>`, либо `--folder-id standard-images` рядом с family. Явный image-id надёжнее: `yc compute image list --folder-id standard-images | grep ubuntu-2404`.
- **`--add-rule cidr=...` → «unknown property 'cidr'».** Правильный параметр — `v4-cidrs=0.0.0.0/0`.
- **`--metadata ssh-keys=user:ssh-ed25519 AAAA…` не записывается** — пробел внутри значения ломает разбор списка key=value. Использовать `--metadata-from-file ssh-keys=/tmp/key.txt` (содержимое `user:<pubkey одной строкой>`). Проверять результат через `yc compute instance get <id> --full` — `--format json` может показывать `metadata: null` при фактически записанных метаданных.
- **`--async` без ожидания возвращает пусто** — ВМ может не создаться. При отладке создавать без `--async`, чтобы увидеть ошибку.
## Зондирование сети и цензуры: только из целевой сети
TCP/HTTPS-доступность, замеренная с чужих узлов (`check-host.net`), НЕ переносится на датацентр-IP YC. Проверено в этой сессии: с бытовых российских нод Telegram доступен, с YC-IP — блокируется по SNI на уровне DPI (`api.telegram.org` → errno 101 / TLS timeout, при этом другие DC Telegram по IP отвечают TCP). Зарубежные LLM API из YC: OpenAI/OpenRouter/Anthropic/Google — 403 (геополитика), Ollama Cloud и Moonshot — 200. Российские источники из YC открыты все (fedstat, rosstat, cbr, bo.nalog, clearspending, zakupki, roschart).
Правило: **сначала зонд из самой сети**, потом выводы. Рецепт зонда без SSH — `references/vm-probe-and-access.md`.
## Выбор конфигурации ВМ (цены РФ с НДС)
Постоянная ВМ под PostgreSQL + сборщик + cron: **4×20% vCPU / 8 ГБ RAM / 60 ГБ SSD ≈ 4 300 ₽/мес** (100% vCPU в тех же параметрах ≈ 6 300 ₽; с CVoS на год ≈ 5 500 ₽). 20% vCPU хватает: агент и gateway большую часть времени ждут сети, а не считают. **Managed PostgreSQL невыгоден**: минимальный кластер (1 хост 2/8 + 100 ГБ SSD) ≈ 7 200 ₽/мес — дороже самой ВМ, поэтому СУБД ставить самогестедом. Диск только SSD (`0,0199 ₽/ГБ·ч`): скрипты работают с SQLite-базами на сотни МБ, network-HDD тормозит. Исходящий трафик: первые 100 ГБ/мес бесплатно, далее 1,42 ₽/ГБ.
## Разделение нагрузок: gateway отдельно от сборщика
Gateway (Telegram-канал, LLM-вызовы, cron) должен оставаться на зарубежном VPS, где Telegram отвечает за ~60 мс. В YC ехать должны те нагрузки, ради которых облако и нужно — сбор российских данных с резидентного IP (ЕМИСС, Росреестр, zakupki, clearspending, БФО). Попытка собрать всё на одной ВМ в YC требует SSH-туннеля к VPS ради Telegram и не даёт ничего, кроме сложности: VPS всё равно остаётся точкой выхода.
- `references/vm-probe-and-access.md` — рецепт зонда сети/цензуры с YC-IP без SSH (cloud-init + base64 + serial console) и всё про доступ к ВМ.
- `references/datalens-connection-and-api.md` — DataLens: роли на организацию через Identity Hub (не на каталог), три состояния API (`Auth denied` / `LICENSE_IS_REQUIRED` / `ENDPOINT_NOT_FOUND`) как диагностический признак, Public API `api.datalens.tech` (спецификация `GET /json/`, заголовки, методы датасетов и лицензий, схема `createDataset`), тарификация рабочих мест, подключение к PostgreSQL (read-only роль, диапазоны `pg_hba`, TLS с IP-SAN).