# Служебная записка для администратора mlcluster: подключение AI-ассистента pgAdmin к внутренней LLM

Метки: pgAdmin 4 v9.15+ AI features; наш PostgreSQL: research_wiki на
host 89.169.168.214:5432 (схемы core, derived, v2, staging и др.).

---

## 1. Что нужно (одной фразой)

Включить AI-фичи pgAdmin 4 и указать pgAdmin на внутренний OpenAI-
совместимый LLM-эндпоинт (наш сервис уже работает на соседней ВМ,
эндпоинт жив — проверен). Требуется pgAdmin ≥ 9.17 (рекомендуем 9.18,
см. CVE) и четыре настройки в `config_local.py` + Preferences.

## 2. Почему pgAdmin 4, а не свой сервис

pgAdmin с v9.15 (апрель 2026) несёт нативный AI-стек:
- вкладка «AI Assistant» в Query Tool (NL→SQL, агент сам изучает схему и
  тестирует запросы; READ ONLY транзакция, лимит 1000 строк, итерации
  по умолчанию 20);
- AI Reports: security / performance / design review для сервера/БД/схемы;
- AI Insights: разбор EXPLAIN-плана.

Это бесплатное встроенное ПО — не новый сервис, а апгрейд того же pgAdmin.

## 3. Список требований для админа (пошагово, 30 минут)

### Шаг 1. Обновление / версии

```bash
pgadmin4 --version  # нужно ≥ 9.16, рекомендуем 9.18 (2026-09-17)
```
9.18 закрывает 4 CVE (вкл. CVE-2026-86863 auth-bypass в WEBSERVER-mode,
CVE-2026-17351 — обход READ ONLY-обёртки AI-агента через SQL-lexer).

### Шаг 2. Включить AI

В `config_local.py` (или `web/config_local.py` для пакета-инсталляции):
```python
LLM_ENABLED = True
DEFAULT_LLM_PROVIDER = 'openai'  # используем OpenAI-совместимый эндпоинт
ALLOWED_LLM_API_URLS = [ ...existing..., '<URL нашего LLM>' ]
```
(Если pgAdmin < 9.15 — обновить; AI-стек появился в 9.15.)

### Шаг 3. LLM-эндпоинт

Наш OpenAI-совместимый сервис:
```
URL: http://<IP-ВМ>:<PORT>/v1
API Key: (файл из 1 строки, передать защищённым каналом)
Модель: «monitor» (Hermes-профиль gpt-oss:120b через ollama-cloud)
```
(Значения URL/ключ — в личной передаче, не в чате.)

### Шаг 4. Настройка в веб-интерфейсе

Preferences → AI:
- Default Provider: OpenAI
- OpenAI → API URL, API Key File, Model (набрать «monitor» вручную или
  Refresh — pgAdmin получит список моделей).

Per-user ключ можно настроить индивидуально в личных Preferences, если
никак не в config_local.py — глобально.

### Шаг 5. Безопасность (пункты для подтверждения админа)

- pgAdmin сам ограничивает AI read-only рамкой (READ ONLY транзакция,
  1000 строк, MAX_LLM_TOOL_ITERATIONS — рекомендуем 10).
- Наш PostgreSQL-роль `viewer` — только SELECT на 11 схем; даже при
  обходе READ ONLY-рамки в БД писать нечем. Двухуровневая защита.
- API ключ LLM хранить в файле на диске (не в конфиге; pgAdmin так
  устроен) — не в переменных окружения и не в git.
- Дополнительная сеть: LLM-эндпоинт должен быть доступен с pgAdmin-машины.
  Рекомендуем security group «только с IP pgAdmin-сервера», не 0.0.0.0/0.

## 4. Что pgAdmin получит после включения

- Правый клик по серверу/БД → AI Analysis → Security/Performance/Design
  Review (отчёты Markdown).
- Правый клик → AI Insights для EXPLAIN-планов (рекомендации по индексам).
- В Query Tool вкладка AI Assistant: NL-вопрос → SQL, с «Copy/Insert/-
  Replace» кнопками.
- AI работает поверх уже известного нашим pgAdmin-пользователям UI.

## 5. Ссылки

- Релизы pgAdmin: v9.18 (17.09.2026), v9.17, v9.16, v9.15.
- Документация AI Reports: pgadmin.org/docs/pgadmin4/9.16/ai_tools.html
- Блог Dave Page (pgEdge, 3 части, март 2026): LLM конфигурация,
  AI Chat агент, AI Insights.
- GitHub issue #9936: регрессия кастомных LLM-URL (9.15) → фикс в
  9.16 (PR #10016): добавить эндпоинт в ALLOWED_LLM_API_URLS в
  `config_local.py`.