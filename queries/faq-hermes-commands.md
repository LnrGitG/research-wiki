# FAQ по полезным командам Hermes на нашем сетапе

> Практический справочник для research-wiki. Составлен по установленной версии
> **Hermes Agent v0.21.2 (2026.9.11), upstream 205645ee** и нашему `docs/help.md`.
> Всегда авторитетный источник — `hermes --help`, `hermes <cmd> --help`, `/help` в сессии.

---

## 1. Диагностика: «что-то сломалось»

Перед любой крупной операцией — сначала проверка, потом действия.

```bash
hermes doctor && hermes status          # здоровье сетапа и компонентов
hermes logs -f agent                    # живой хвост (errors/gateway/gui тоже)
hermes logs --session <id> --since 1h   # по конкретной сессии
hermes insights --days 7                # токены, стоимость, паттерны инструментов
hermes prompt-size --json               # бюджет системного промпта: skills+memory+tools
```

`prompt-size` у нас особенно полезен: kanban-toolset занимает ~23.5 KB схемы
(≈5,900 токенов) при 0 строк в `kanban.db` — крупнейший единичный потребитель
статического контекста после системного промпта.

## 2. Сессии и история

```bash
hermes sessions list                    # последние, с моделью и источником
hermes sessions export <id> --format md # выгрузка в JSONL/Markdown/QMD
hermes sessions optimize                # слить FTS5-сегменты + VACUUM (диск, без потери)
hermes sessions repair                  # починить state.db / роутинг
```

В сессии: `/resume`, `/sessions`, `/undo [N]`, `/rollback [N]` (чекпоинты ФС),
`/compress` и `/compress here [N]` (сжать историю), `/status`.
Повтор прошлой задачи — `session_search` по query + `sort=newest`, затем сверка
артефактов с файлами на диске (сводки ассистента — самоотчёты, не факты).

## 3. Cron — наши джобы

У нас 8 джобов, все запинены на `glm-5.3-flash / ollama-cloud`, чтобы дрейф
модели их не «молча пропускал».

```bash
hermes cron list                        # состав и статус
hermes cron doctor                      # health-check джобов
hermes cron runs <job_id>               # история попыток
hermes cron incidents                   # сбои с ack: hermes cron incidents --ack <id>
hermes cron run <job_id>                # запустить на следующем тике
```

**Режим `--no-agent`** — важный приём: если вся работа делается скриптом (загрузка
данных), LLM не нужен, и джоб переводится в режим «скрипт сам себе джоб»:

```bash
hermes cron create "0 9 5,7 * *" --name "KEP refresh" \
  --script kep_refresh.sh --no-agent --deliver origin
```

Так устроен наш `KEP short-term indicators monthly refresh`: пустой stdout =
ничего не отправляется, тишина при отсутствии нового выпуска. Это снимает риск
дрейфа модели и не тратит токены. Скрипт лежит в `~/.hermes/scripts/kep_refresh.sh`
(cron ищет именно там), а рабочая версия — в `research-wiki/scripts/`.

## 4. Скиллы и гейт записи

У нас включён `skills.write_approval=true`: **любая** мутация `skill_manage`
(staged) ждёт подтверждения — и от агента, и от куратора.

```bash
hermes skills pending                   # в CLI; в сессии: /skills pending
hermes skills diff <id>                 # что изменено
hermes skills approve <id>              # /skills approve <id>
hermes curator status                   # телеметрия скиллов с provenance
hermes curator run --dry-run            # предпросмотр прогона
```

Правило: bundled/hub-скиллы куратор не трогает никогда. Отключить гейт —
`hermes config set skills.write_approval false`.

## 5. Память

Встроенная `MEMORY.md`/`USER.md` активна всегда; внешние провайдеры — опция.

```bash
hermes memory status
hermes memory reset                     # стереть встроенную память (осторожно)
```

В сессии `/memory pending|approve|reject` — ревью отложенных записей; `/journey` —
таймлайн навыков и памятей.

## 6. Модели и fallback

```bash
hermes model                            # пикер модель+провайдер (постоянный дефолт)
hermes fallback list | add | remove     # цепочка при rate-limit/overload
hermes auth status                      # пул кредов, приоритеты
```

В сессии `/model [name] [--global]` меняет модель **только текущей** сессии.
Наш fallback: `claude-sonnet-4 / openrouter`; делегаты — `glm-5.3-flash`;
Astra Pro — лишь короткие синтезы, не tool-call.

## 7. Бэкап, обновление, откат

```bash
hermes backup -q -l pre-update          # быстрый снапшот критических файлов
hermes backup -k 5                      # zip ~/.hermes с ретеншном
hermes update --check && hermes update  # проверка, затем обновление (--plan для плана)
```

Откат правок ФС — `/rollback [N]` в сессии; `hermes checkpoints status|prune`.
Перед разрушительными операциями делаем точку возврата (git-тег/ветка-бэкап) и
сообщаем путь восстановления.

## 8. Отправка и платформы (без LLM)

```bash
hermes send -t telegram "текст"          # в канал без агента/токенов
hermes gateway status                    # жив ли gateway
hermes pairing list                      # пары-коды доступа
```

Target-форматы: `platform`, `platform:chat_id`, `platform:#channel`.

## 9. Инварианты нашего сетапа

- Секреты — только в `.env`; настройки — `config.yaml` через `hermes config set`,
  руками конфиг не править.
- Telegram-токен = один слушатель: два gateway на один токен конфликтуют.
- `/model` действует на текущую сессию; постоянный дефолт — через `hermes model`.
- Скиллы hub/bundled куратором не трогаются; мутации — только через гейт.

## 10. Данные research-wiki (вне Hermes CLI, но на каждый день)

```bash
python3 scripts/yc_sync.py status|verify # синхронизация с YC Object Storage
python3 scripts/lint_wiki.py             # проверка вики (wikilinks, frontmatter)
python3 scripts/query.py "..."           # поиск по вики
python3 scripts/wordstat_construction_collect.py  # поисковые лиды (100 зап/час)
```

Тяжёлое — на YC: PostgreSQL `research_wiki` (46.243.210.160, ru-central1-b) с
pgvector; `raw/` — симлинк на `~/yc-wiki/raw/`.
