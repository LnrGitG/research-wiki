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
raw/               # исходники (PDF, выгрузки) — НЕ редактировать
concepts/          # концепты-синтезы
entities/          # сущности (девелоперы, регионы, банки)
comparisons/       # сравнительные таблицы
queries/           # аналитические записки и списки источников
data/              # обработанные данные (CSV)
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
- Каждое действие — запись в log.md; коммиты — с подробным сообщением.

## Ключевые скрипты (scripts/)
- `lint_wiki.py` — проверка вики; `rebuild_embeddings.py` — векторный слой
- `query.py`, `vector_search_cli.py` — поиск по вики
- `collect_panel.py` (1429 зап, 14 комп), `collect_smartlab.py`, `collect_rsbu.py`
- `wordstat_api.py` (100 зап/час), `wordstat_construction_collect.py`
- `translate_papers.py` — EN→RU переводы
- Python: `~/.hermes/hermes-agent/venv/bin/python3` (PEP 668 на системном 3.12)

## Что не трогать
- `raw/` — исходники, только добавление
- `.env` — секреты; никогда не коммитить
- `latest.zip`, `_archive/` — архивы

## Перед коммитом
- catalog.yaml обновлён, если добавлялись/менялись работы
- log.md дополнен
- страницы из изменений внесены в index.md
- git commit с детальным сообщением (без '&' в message)