# Hermes Agent: справка по сервисным командам

> Справочник CLI-команд и slash-команд Hermes Agent.
> Версия на момент составления: **v0.21.2 (2026.9.11)**, upstream 205645ee.
> Дата: 2026-09-14. Всегда авторитетный источник: `hermes --help`, `hermes <cmd> --help`, `/help` в сессии.
> Составлено из реальных выводов `--help` по всем командам установленной версии.

---

## 1. Глобальные флаги (до команды)

| Флаг | Действие |
|---|---|
| `-z PROMPT` | One-shot: один промпт → только финальный текст в stdout. Для скриптов/пайпов; approvals bypass. С `--usage-file PATH` пишет JSON-отчёт о токенах/стоимости даже при падении |
| `-m MODEL` / `--provider` | Переопределение модели/провайдера на этот вызов (только -z и --tui; постоянный дефолт — в config.yaml) |
| `--resume SESSION` / `--continue [NAME]` | Продолжить сессию по ID / последнюю или именованную |
| `--worktree` | Режим git worktree (изолированный checkout для агентских правок) |
| `--tui` / `--cli` | Ink TUI вместо классического REPL / наоборот |
| `--yolo` | Отключить approval-промпты (осторожно в gateway-сессиях) |
| `--safe-mode` | Читательный режим без опасных инструментов |
| `-t TOOLSETS` | Список toolsets на этот вызов |
| `--skills SKILLS` | Ограничить загружаемые скиллы |
| `--ignore-user-config` / `--ignore-rules` | Игнорировать config.yaml / AGENTS.md |
| `--in DIR` | Рабочая директория сессии |
| `--version` | Версия билда |

## 2. Сессии и чат

**CLI:** `chat` (интерактив; `-q` одиночный запрос), `sessions`:
- `list` — последние сессии; `export` — выгрузка JSONL/Markdown/QMD
- `delete` / `prune` (фильтры по времени/источнику) / `archive` (мягкое скрытие без удаления)
- `optimize` — слияние FTS5-сегментов + VACUUM (диск, без потери данных); `optimize-storage` — компактный v23-лейаут индекса
- `repair` / `repair-routing` / `recover` — починка state.db и роутинга
- `rename`, `pin/unpin/pinned`, `browse`, `import`, `stats`

**Slash (в сессии):** `/new`, `/clear`, `/retry`, `/undo [N]`, `/title`, `/compress` (+`here [N]`, `--preview`), `/branch`, `/resume`, `/sessions`, `/status`, `/redraw`, `/prompt` ($EDITOR), `/rollback [N]` (чекпоинты ФС), `/diff` (git), `/snapshot`, `/bg <prompt>` (фоновая сессия), `/btw <question>` (боковой вопрос без прерывания), `/queue <prompt>` (очередь на следующий ход), `/steer <prompt>` (инъекция после ближайшего tool call), `/goal [text]` + `/subgoal` (стоящая цель), `/handoff <platform>` (передать сессию в мессенджер).

## 3. Модели и провайдеры

| Команда | Назначение |
|---|---|
| `model` | Пикер модели+провайдера (дефолт) |
| `moa` | Mixture-of-Agents слоты (list/configure/delete) |
| `fallback` | Цепочка fallback-провайдеров (list/add/remove/clear) — срабатывает при rate-limit/overload/сети |
| `portal` | Nous Portal: login (one-shot онбординг), info, open, tools |
| `auth` | Пул кредов: add/list/remove/reset/priority/refresh/status/logout |
| `login` / `logout` | Авторизация провайдера / сброс |
| `migrate` | Миграция конфига при retirement моделей/настроек (сейчас: `xai`) |
| `setup` | Мастер первичной настройки |
| Slash: | `/model [name] [--global]` (смена для сессии по умолчанию), `/personality`, `/reasoning`, `/fast` |

## 4. Gateway и платформы

| Команда | Подкоманды |
|---|---|
| `gateway` | run (foreground; для WSL/Docker/Termux), start/stop/restart, status, install/uninstall (systemd/launchd), list (все профили), setup (платформы), migrate (мультиплекс на один gateway), enroll (relay) |
| `send` | Отправка в любой сконфигурированный платформенный канал без LLM/агента: `hermes send -t telegram "текст"`; target-форматы `platform`, `platform:chat_id`, `platform:#channel` |
| `pairing` | Пары-коды доступа пользователей: list/approve/revoke/clear-pending |
| `peer` | Бот-к-боту DM между машинами: add/list/remove/dm/run/status |
| `whatsapp`, `whatsapp-cloud`, `slack` | Сетапы конкретных платформ |
| `browser` | Хелперы реального браузера (закрыть браузер, залочивший профиль) |
| Slash (GW): | `/approve`, `/deny`, `/restart`, `/sethome`, `/topic`, `/platform pause/resume/list`, `/commands` |

## 5. Автоматизация

**`cron`**: list, create/add, edit, pause/resume, run (на следующий тик), remove, status (жив ли планировщик), runs/history (попытки исполнения), incidents (список/ack сбоев), **notepad** (durable KV джобы между запусками), doctor (health-check джобов), tick (исполнить due-джобы и выйти).

**`webhook`**: subscribe/add, list, remove, test (тестовый POST).

**`kanban`** (SQLite-борда поверх профилей; ~40 подкоманд): init, boards, create, **swarm** (граф: параллельные воркеры → verifier → synthesizer), list/show, assign/reassign/reclaim, set-model (оверрайд модели задачи), link/unlink (зависимости), claim, comment, attach, complete, block/unblock/schedule, request-review/request-changes, promote/archive, tail, dispatch/daemon/watch, stats, log/runs/heartbeat, context/specify/decompose, gc/repair.

**Slash:** `/cron`, `/kanban`, `/suggestions` (предложенные автоматизации), `/blueprint [name]` (готовый сценарий из каталога), `/heartbeat every 10m <prompt>` (ре-энтри в idle-сессию), `/moa <prompt>`.

## 6. Навыки (skills)

**`skills`**: trust/untrust (проектные скиллы из ./.hermes/skills), browse/search (реестры skills.sh/GitHub/ClawHub), install/inspect (превью без установки), list, check/update (обновления hub-скиллов), audit (рескан), uninstall, **reset** (сброс bundled-скилла к стоку), list-modified, **diff** (что изменено vs stock), opt-out/opt-in, repair-official, publish (--to github/clawhub), **snapshot** export/import (перенос набора скиллов), **tap** (list/add/remove — GitHub-репо как источник), config.

**`bundles`** — алиасы-наборы скиллов (загрузка пачкой по /<name>).

**`curator`** (фоновая поддержка агентных скиллов; bundled/hub не трогает): status, **usage** (телеметрия ВСЕХ скиллов с provenance), run (сейчас; `--dry-run`, `--consolidate`, `--sync/--background`), pause/resume, pin/unpin (защита от авто-переходов), list-unmanaged, adopt, restore/list-archived, archive, prune, backup, rollback, ledger (audit-журнал), purge (TTL архива).

**Slash:** `/skills` (+ review: `pending`, `diff <id>`, `approve|reject <id>`, `approval on|off`), `/learn <source>` (скилл из директории/URL/текущего чата), `/bundles`, `/journey` (таймлайн обучения).

**Наша конфигурация:** `skills.write_approval=true` — любая мутация skill_manage (и от агента, и от куратора) staged → подтверждение через `/skills approve`. Отключение: `hermes config set skills.write_approval false`.

## 7. Память

**`memory`** (внешние провайдеры; встроенный MEMORY.md/USER.md активен всегда): setup (интерактивный выбор: honcho, openviking, mem0, hindsight, holographic, retaindb, byterover), status, off, **reset** (стереть встроенную память).

**Slash:** `/memory [pending|approve|reject]` (ревью отложенных записей), `/journey` — таймлайн навыков+памятей; `journey` CLI: list/delete/edit нод.

## 8. Инструменты

| Команда | Назначение |
|---|---|
| `tools` | Включение/отключение инструментов per-platform (interactive UI без аргументов; list/disable/enable, MCP в нотации `server:tool`, post-setup) |
| `mcp` | serve (Hermes как MCP-сервер), add/rm/list/test/configure, login/reauth (OAuth), picker, catalog (одноклик-инсталлы), install; slash `/reload-mcp` |
| `lsp` | Языковые серверы для post-write диагностик: status/list/install/install-all/restart/which |
| `computer-use` | Backend cua-driver (macOS/Win/Linux): install/doctor |
| `plugins` | install/search/validate/update/remove/list/enable/disable/doctor/pack/show (нативные + portable Agent Plugins v1) |
| Slash: | `/tools`, `/toolsets`, `/plugins`, `/reload` (подтянуть .env), `/reload-skills` |

## 9. Безопасность и секреты

| Команда | Назначение |
|---|---|
| `security` | Supply-chain аудит по OSV.dev: venv, plugin-зависимости, pinned MCP-серверы (`security audit`) |
| `approvals` | suggest (мининг истории аппрувов → proposals для command_allowlist), test (dry-run вердикта) |
| `vault` | Локальный шифрованный autofill-vault: add/list/rm/sources (агент видит только handle'ы) |
| `secrets` | Внешние секрет-менеджеры при старте: bitwarden/bw, onepassword/op |
| `egress` | iron-proxy — TLS-перехватывающий egress-фаервол (install/setup/start/stop/status/disable/config) |
| `pairing` | Авторизация пользователей мессенджера (см. §4) |
| `console` | Безопасная командная консоль |
| `checkpoints` | Store shadow-git чекпоинтов: status/prune/clear/clear-legacy (rollback через `/rollback`) |
| `pause` / `resume` | **Emergency stop**: halt новых cron/kanban dispatch и gateway-ходов (in-flight не убивается); resume снимает |
| `hooks` | Shell-хуки из config.yaml: list/test/revoke/doctor |
| Slash: | `/yolo`, `/approvals`, `/busy [queue|steer|interrupt]` |

## 10. Обслуживание и диагностика

| Команда | Назначение |
|---|---|
| `doctor` | Диагностика сетапа; `--fix` автофикс, `--live` реальные probe-вызовы бэкендов, `--ack ID` закрыть advisory |
| `status` | Статус компонентов (`--all` с красакцией, `--deep`) |
| `verify` | Детект рецепта проекта (bootstrap→build→test→start→poll→teardown) |
| `logs` | agent/errors/gateway/gui/desktop.log: `-n`, `-f` (follow), `--level`, `--session`, `--since`, `--component` |
| `dump` | Компактный текстовый summary сетапа для саппорта (`--show-keys` — маскированные префиксы ключей) |
| `debug` | `share` — выгрузка логов+системы на paste-сервис с URL; `delete` |
| `insights` | Токены/стоимости/паттерны инструментов за `--days N`, фильтр `--source` |
| `monitoring` | Health-метрики gateway, экспорт OTLP, контент-фри по построению |
| `prompt-size` | Бюджет системного промпта: skills index, память, tool-схемы (`--platform`, `--json`) |
| `backup` | Zip всего ~/.hermes (без кодовой базы); `-q` быстрый снапшот критических файлов; `-k N` ретеншн |
| `import` | Восстановление из бэкап-zip |
| `update` | Pull + переустановка зависимостей; `--check` (только проверка), `--plan` (план без действий), `--gateway` |
| `uninstall` | Полное удаление |
| `worktree` | Ревизия .worktrees/: list (классификация age/size/verdict) / prune (только безопасные) |
| Slash: | `/update`, `/version`, `/usage` (токены/лимиты), `/insights`, `/debug` |

## 11. Инфраструктура и поверхности

| Команда | Назначение |
|---|---|
| `dashboard` | Web-UI админка (конфиг, ключи, сессии, embedded TUI); `register` — привязка к Nous Portal |
| `serve` | Headless JSON-RPC/WebSocket backend (для desktop/remote), порт 9119 |
| `desktop` (gui) | Нативное Electron-приложение |
| `acp` | ACP-сервер для IDE (VS Code/Zed/JetBrains); `--check`, `--setup` |
| `proxy` | Локальный OpenAI-совместимый прокси поверх OAuth-провайдера |
| `profile` | Изолированные инстансы: list/use/create/delete/describe/show/alias/rename/export/import/install/update/info |
| `project` | Именованные мульти-папочные воркспейсы: create/list/show/add-folder/bind-board |
| `config` | show/edit/get/set/unset/path/env-path/check/migrate — **правка настроек только через `config set`, не руками** |
| `skin` | Темы: list/switch/tweak (активная правится `hermes skin set <key> <hex>`) |
| `sync` | Skill Sync между устройствами/организацией: status/pull/push/now/enable/disable/device/propose |
| `pets` | Petdex-маскоты: list/install/select/show/off/scale |
| `completion` | Shell completion (bash/zsh/fish) |
| Slash: | `/config`, `/skin`, `/profile`, `/footer`, `/voice`, `/verbose`, `/indicator`, `/statusbar`, `/timestamps`, `/battery`, `/codex-runtime` |

## 12. Типовые операции нашего сетапа

```bash
# Проверка перед важными изменениями
hermes doctor && hermes status

# Skills: гейт включён — все записи через подтверждение
hermes skills pending            # (в CLI-сессии: /skills pending)
hermes curator status            # телеметрия скиллов
hermes curator run --dry-run     # предпросмотр прогона

# Cron
hermes cron list && hermes cron doctor
hermes cron runs <job>           # история попыток
hermes cron incidents            # сбои с ack

# Бэкап
hermes backup -q -l pre-update   # быстрый снапшот перед update

# Модель
hermes model                     # пикер; /model в сессии — на текущую
hermes fallback add              # резервный провайдер

# Обновление
hermes update --check && hermes update
```

**Ключевые инварианты:** секреты только в `.env` (настройки — config.yaml через `hermes config set`); конфиг руками не править; `/model` меняет модель только текущей сессии; Telegram-токен = один слушатель; bundled/hub-скиллы куратором не трогаются никогда.