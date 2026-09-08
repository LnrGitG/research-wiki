# Obsidian: research-wiki как vault

Репозиторий `~/research-wiki` открывается в Obsidian как vault (Open folder as vault → ~/research-wiki). Вики-ссылки `[[...]]` уже совместимы с Obsidian — навигация работает из коробки.

## Рекомендуемые настройки (Settings)

1. **Files & Links**
   - Default location for new notes: `queries/` (или отключить автосоздание)
   - New link format: **Shortest path when possible** (совместимо с конвенцией вики)
   - Detect all file extensions: ON (чтобы открывался `hypotheses.yaml`, `catalog.md`)

2. **Core plugins**: включить Backlinks, Outgoing Links, Graph view, Page preview.
3. **Graph view**: фильтр `path:-papers` (423 статьи-источники заглушают граф; смотреть по concepts/queries/models).
4. **Daily notes**: template `templates/` (если понадобится).

## Community plugins (рекомендуемые)
- **Dataview** — таблицы из frontmatter (реестр гипотез по статусу, карточки моделей)
- **Kanban** — трек задач (status: backlog/in-progress/review/done в frontmatter)
- **Obsidian Git** — pull/push с локального ПК без терминала

## Что не синхронизировать
`.obsidian/workspace*.json`, cache и тяжёлые plugin-байнари — в `.gitignore` уже добавлены.
Плагины настраиваются локально (на телефоне — только чтение через GitHub Pages или Obsidian mobile + git-плагин).

## Конвенции совместимости
- Имена файлов латиницей (lowercase, hyphens) — безопасно для sync и мобильных ОС
- Кириллица в [[wikilinks]] встречается в legacy-страницах — Obsidian их резолвит, но при правке страниц нормализуем к транслиту
- [[сноски]] вида [[1]] в papers/ — это маркеры источников, не ссылки; в Obsidian отображаются как пустые ссылки (не чинить)

## MOC
Точка входа: [[MOC]] — тематическая навигация. Граф строить от него.