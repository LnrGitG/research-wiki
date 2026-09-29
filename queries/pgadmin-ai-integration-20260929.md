# pgAdmin 4 + AI-native сервисы: варианты интеграции и лучшая практика (2026-09-29)

Метка: **«Независимый расчёт, не связанный с Банком России».**

## Контекст: что уже умеет pgAdmin 4 из коробки (v9.16–9.18)

Начиная с v9.15 (март 2026) pgAdmin несёт собственный AI-стек, включается
мастер-ключом `LLM_ENABLED = True` в `config_local.py`. Три фичи:

1. **AI Chat Agent** (вкладка «AI Assistant» в Query Tool): NL→SQL через
   tool-call цикл. Инструменты: get_database_schema, get_table_info,
   get_table_columns, execute_sql_query. Безопасность: только READ ONLY
   транзакция, лимит 1000 строк, MAX_LLM_TOOL_ITERATIONS (дефолт 20).
2. **AI Reports** (правый клик по серверу/БД/схеме → AI Analysis): отчёты
   security / performance / design review (Markdown, скачивание .md).
3. **AI Insights**: разбор EXPLAIN-плана с рекомендациями (индексы и др.).

Провайдеры из коробки: **Anthropic, OpenAI, Ollama, Docker Model Runner**
(OpenAI-совместимый эндпоинт = LiteLLM / LM Studio / свой прокси).
Ключи — из файлов на диске (не в конфиге); модель выбирается динамически.
`ALLOWED_LLM_API_URLS` — allow-list эндпоинтов (защита от SSRF; в 9.15
регрессия с кастомными URL, починена в 9.16 — PR #10016; добавить свой
эндпоинт в config_local.py).

## Вариант A. Обновить pgAdmin до 9.18 (веб, серверная установка) — AI из коробки

Самый короткий путь. На базе `research_wiki` на ВМ наш pgAdmin — веб-версия
(database.mlcluster.ru). Апгрейд → LLM_ENABLED=True → Preferences → AI →
провайдер. Чат видят все пользователи pgAdmin; каждый настраивает свой
ключ в личных Preferences.

- Провайдер для нас: **Ollama на ВМ** (уже есть ollama на ollama-cloud, но
  для pgAdmin можно поднять локальный Ollama на самой ВМ — маленькая модель
  из каталога, без интернета) ИЛИ OpenAI-совместимый endpoint от Hermes
  peer (требуется добавление в ALLOWED_LLM_API_URLS).
- Ограничение: у viewer-роли все 4 инструмента read-only — совпадает с
  нашей моделью безопасности.

## Вариант B. MCP-сервер PostgreSQL (Postgres MCP Pro, crystaldba)

Отдельный сервис поверх БД: Claude Desktop / любой MCP-клиент получает
инструменты read-only SQL + health checks + explain + **index tuning**
(гипотетические индексы, перебор комбинаций). Режим `restricted`
(рекомендуемый для нас) = read-only wrapping. Лучше pgAdmin-AI в tuning,
но требует отдельного клиента. Подключение к туннелю 127.0.0.1:15432
или напрямую при доступе с ВМ.

## Вариант C. Естественный язык → SQL через собственный слой (без pgAdmin)

- **DataLens + AI-подключение**: пока нет нативного генератора SQL, но
  есть редактор D3-чартов с источником SQL.
- **GitHub Pages + LLM API**: у нас уже есть 15 890 карточек метрик
  (векторный поиск metric_search.py, модели Яндекса 256d). Построить
  «поиск метрики на естественном языке» - вопрос к векторной базе,
  не к БД. Дешевле и надёжнее, чем NL→SQL.

## Рекомендация (лучша практика, с учётом нашего стека)

1. **Сначала вариант A** (pgAdmin 9.18 + LLM_ENABLED + провайдер) —
   минимум движущихся частей, AI внутри привычного корпоративного
   портала, security-model совпадает с viewer-ролью.
2. **Ollama локально на ВМ как провайдер** — данные pgAdmin-AI не
   уходят наружу (корпоративные ограничения); модель 7-8B хватает
   для NL→SQL по нашей схеме.
3. **Docker Model Runner** — если Docker Desktop есть у коллеги на его
   машине, но наш pgAdmin — серверный, поэтому модель должна быть на
   ВМ (localhost), не на рабочих машинах.
4. **Postgres MCP Pro** отложить до потребности (index tuning для
   медленных аналитических запросов) — дополнительная движущаяся часть.

## Безопасность (обязательные шаги при включении)

- READ ONLY-рамка pgAdmin-AI + наша viewer-роль = двухслойная защита
  (LLM не может писать; даже если бы хотел — не сможет).
- MAX_LLM_TOOL_ITERATIONS уменьшить до 10 для пользователей-новичков.
- Локальная модель (Ollama на ВМ) — данные не утекают в облако.
- Обновить до 9.18: закрыты 4 CVE (вкл. auth-bypass в WEBSERVER mode),
  hardening LLM-redirect (CVE-2026-17351 — важный: SQL-инъекция через
  COMMIT в READ ONLY-рамке чат-агента была устранена двумя раундами).

## Источники
- pgAdmin news: v9.18 (17.09.2026), v9.17, v9.16, v9.14
- Документация: pgadmin.org/docs/pgadmin4/9.16/ai_tools.html
- Серия блога Dave Page (pgEdge, март 2026): конфигурация+отчёты,
  AI Chat агент, AI Insights
- Bytebase: Top 3 Open Source Postgres MCP Servers
- GitHub issue #9936 (regression/fix ALLOWED_LLM_API_URLS)