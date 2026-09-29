# AI-интеграция pgAdmin: выполнено (2026-09-29) — Hermes API как OpenAI-совместимый провайдер

Метка: **«Независимый расчёт, не связанный с Банком России».**

## Что выяснилось при «Делай»

- pgAdmin 4 крутится **не на нашем ВМ**, а на корпоративном портале
  `database.mlcluster.ru` (158.160.225.75) — обновление до 9.18 и
  `LLM_ENABLED` — вопрос администратора mlcluster, не наш.
- ВМ: RAM свободно 907 МБ — локальный Ollama 7-8B не встанет (нужен 4-5 ГБ).
- **Готовый OpenAI-совместимый LLM-эндпоинт на ВМ уже есть** — Hermes
  API-сервер профиля monitor: `127.0.0.1:8642/v1` (gateway hermes-gateway-
  monitor.service, API_SERVER_ENABLED=true, ключ 43 симв. в
  profiles/monitor/.env). Модель = профиль `monitor`.

## Проверено сквозным тестом

1. `/v1/models` отдаёт `{"id": "monitor", "owned_by": "hermes"}` — 200.
2. Chat-completions отвечает (4 с).
3. **NL→SQL работает**: вопрос «Последняя дата и значение ввода жилья для
   Республики Татарстан» → корректный SQL → в БД он вернул
   **2026-08-01, 230,328 тыс. кв. м Татарстан** — числа совпали.
4. Систем-промпт (схема core в 5 строках) достаточен для точного SQL.

## Что сделать для включения pgAdmin → Hermes API

1. Владельцу mlcluster: обновить pgAdmin до ≥9.16 (9.18 лучше; CVE-2026-17351
   fix), в `config_local.py`: `LLM_ENABLED = True` и в `ALLOWED_LLM_API_URLS`
   добавить `http://<IP-ВМ>:<PORT>` (см. ниже).
2. Настроить Preferences → AI в pgAdmin: provider = OpenAI, API URL =
   эндпоинт Hermes ВМ, API Key File = файл с API_SERVER_KEY (43 симв).
   Модель: `monitor`.
3. Сеть: API-сервер ВМ слушает 127.0.0.1:8642. Для pgAdmin с mlcluster надо
   либо (а) bind 0.0.0.0 + security group на ip mlcluster (158.160.225.75),
   либо (б) socat/франкфурт-прокси. Рекомендация: (а) с ограничением по IP.
4. MAX_LLM_TOOL_ITERATIONS = 10.
5. Альтернатива без infra: Hermes peer на VPS (18642→8642) — тоже
   OpenAI-совместим; pgAdmin может указать эндпоинт VPS.

## Риски/ограничения

- 12k токенов на системный промпт из-за накладных — Hermes-профиль несёт
  системный контекст; для pgAdmin лучше отдельный лайт-профиль без лишнего.
- Модель monitor = ollama-cloud gpt-oss:120b — расход кредитов ollama при
  использовании коллегами; оценка: ~1 вызов ≈ 3-15k токенов.
- READ ONLY-рамка pgAdmin (9.18) + наша viewer-роль = двойная защита.
- Без pgAdmin-обновления: любой OpenAI-клиент (Cherry Studio, Chatbox)
  может подключаться уже сейчас к 8642 с ключом — быстрый pilot.

## Файлы/переменные (не секреты в чате)
- Ключ API_SERVER_KEY: profiles/monitor/.env на ВМ (43 симв).
- Секрет для pgAdmin-конфигурации (файл API Key File) — положить на mlcluster.

## Статус
- LLM-провайдер: работоспособен (эндпоинт жив на ВМ, 2/2 теста прошли).
- pgAdmin-интеграция: ждёт администратора mlcluster (LLM_ENABLED + allowlist
  + соединение между mlcluster и ВМ).