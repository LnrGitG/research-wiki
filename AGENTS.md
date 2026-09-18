# AGENTS.md — research-wiki

Инструкции для ИИ-агентов, работающих в этом репозитории (Hermes, Codex, Claude Code, opencode).

## Что это
Персональная исследовательская вики по экономике жилищного рынка России:
трансмиссия ДКП, ипотека, СМР, nowcasting, региональный анализ.
Владелец: Ленар (см. README.md). Схема вики: SCHEMA.md — прочитать перед правками.

## Структура
```
papers/            # научные статьи (EN, .md после конверсии из PDF)
papers/ru_papers/  # переводы: topic_author1_author2_year.RU.md
raw/               # → symlink на ~/gcs-wiki/raw/ (GCS бакет, gcsfuse)
concepts/          # концепты-синтезы
entities/          # сущности (девелоперы, регионы, банки)
comparisons/       # сравнительные таблицы
queries/           # аналитические записки и списки источников
data/              # обработанные данные (CSV) + локальный кэш DB
scripts/           # пайплайны сбора и обработки
catalog.yaml       # реестр работ с метаданными и тегами
hypotheses.yaml    # реестр гипотез (skill: hypothesis-tracker)
index.md, log.md   # оглавление и журнал действий
```

## Конвенции
- Страницы вики — на русском; имена файлов — латиницей (lowercase, hyphens).
- Frontmatter по схеме SCHEMA.md; при правке страницы — bump `updated`.
- Минимум 2 outbound `[[wikilinks]]` на страницу; новые страницы → index.md.
- Кросс-референсы к существующим работам обязательны (Baum-Snow & Han 2024, Saiz 2010 …).
- Точные количественные значения — только с источником; inline [[N]] + список в конце.
- Каждое действие — запись в журнал: **содержательное** (новые публикации,
  источники, обновления данных, аналитические записки) → `log.md`;
  **техническое** (инфраструктура, базы данных, скрипты, CI, настройка
  сервисов) → `log-tech.md`. Коммиты — с подробным сообщением.

## Ключевые скрипты (scripts/)
- `lint_wiki.py` — проверка вики; `rebuild_embeddings.py` — векторный слой
- `query.py`, `vector_search_cli.py` — поиск по вики
- `collect_panel.py` (1429 зап, 14 комп), `collect_smartlab.py`, `collect_rsbu.py`
- `wordstat_api.py` (100 зап/час), `wordstat_construction_collect.py`
- `translate_papers.py` — EN→RU переводы
- `gcs_sync.py` — синхронизация с GCS: `ensure_db()`, `raw_path()`, CLI sync/pull/status/verify
- Python: `~/.hermes/hermes-agent/venv/bin/python3` (PEP 668 на системном 3.12)

## Хранилище тяжёлых данных (YC Object Storage)
- **Бакет:** `wiki-research` (Yandex Object Storage, rclone-remote `yc-s3`)
- **raw/** → symlink на `~/yc-wiki/raw/` (монтирование rclone, PDF/XLSX/JSON — 2.1 ГБ)
- **data/db/** → источник для SQLite DB (1.45 ГБ); `ensure_db()` скачивает по требованию
- **data/archive/** → JSONL-архивы (110 МБ)
- **Скрипты** используют `from yc_sync import ensure_db` для DB и симлинк `raw/` для исходников
- CLI: `python3 scripts/yc_sync.py sync|pull|status|verify`
- **Монтирование:** systemd-юнит `yc-wiki-mount.service` (user), автозапуск включён
- **НЕ удалять локальные DB** (rosstat_construction.db и др.) — это горячий кэш

Google Cloud выведен из эксплуатации 17.09.2026: 3.5 ГБ перенесены в YC, `gcs_sync.py`
удалён, `gcsfuse` отключён. Исторические детали — `queries/database-deployment-plan.md`.

## Что не трогать
- `raw/` — symlink на GCS; исходники только добавлять (через `gcs_sync.py sync`)
- `.env` — секреты; никогда не коммитить
- `latest.zip`, `_archive/` — архивы
- Локальные `data/*.db` — кэш; не коммитить (в .gitignore)

## Перед коммитом
- catalog.yaml обновлён, если добавлялись/менялись работы
- журнал дополнен: `log.md` (содержательное) либо `log-tech.md` (техническое)
- страницы из изменений внесены в index.md
- git commit с детальным сообщением (без '&' в message)