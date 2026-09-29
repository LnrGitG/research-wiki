Слои: SOUL → AGENTS (~/shared-context) → memory → skills → session_search; сокращения расшифровывать при первом употреблении (ИФО, ИКВ, cost-push).
§
Работа с ТЗ: пользователь пишет спеку сам, присылает на критику; артефакт → queries/*.md + commit.
§
Реестр гипотез: ~/research-wiki/hypotheses.yaml; skill hypothesis-tracker.
§
Wiki: 319 карточек, 633 вектора, CI green; вектора — Яндекс-эмбеддинги 256 dim. Детали → AGENTS.md.
§
Параметры инжеста источников (ЕМИСС, ФНС, Wordstat, iminfin, ККТ, ЦБ, правила v2) → queries/ingest-source-params.md — там все детали парсеров/релизов/КТ; память держит только этот якорь.
§
Wordstat СМР: композит S2–S5 lead-1m r=0.644 (n=18); уровневая OLS непригодна — MIDAS/алмон; scripts/wordstat_api.py.
§
ФНС: фильтр filed=1 AND line_2110>0; RFSD-детали → queries/ingest-source-params.md.
§
Библиотека навыков: инжест — 2 зонтика (research-wiki-data-ingestion 87 ref, research-document-ingestion 30); источники в references/. Обслуживание: skill hermes-skill-library-maintenance.
§
Репо: research-wiki-private — ГЛАВНЫЙ (всё, рабочий каталог, remotes private+public); research-wiki — публичный (только знания). Публикация: APPLY=1 scripts/publish_wiki.py. queries/ публикуется выборочно (20 из 93).
§
Корпус публикаций: 314 статей + 161 перевод в papers/; склейка по имени файла (у перевода source_pdf с префиксом raw/papers/); 188 уникальных sha256 (8 дублей). core.paper_card в БД YC (314 карточек + v_paper_card); core.document/file_registry пусты.
§
S3-канал agent-vm-exchange работает (put/get-object с IAM-токеном из metadata). psql под ubuntu не работает — только sudo -u postgres. OOM на ВМ: 4× OOM-kill python3 (5.2 ГБ) при чтении целого parquet — итератор обязателен.
§
Роль monitor (ВМ YC, hermes peer 18642→8642, ollama-cloud gpt-oss:120b) — общий исполнитель для ВСЕХ главных профилей: default И macroeconomist. Один экземпляр: сбор/обработка данных, БД v2, расчёты, fedstat/JupyterLab через peer yc. Профиль-агностична; доменные границы главных профилей (СМР/жильё — default; макроагрегаты/ДКП — macroeconomist) на её роль не влияют. Telegram на ВМ недоступен.
§
Стек ВМ: R 4.6 (user-lib: midasr/midasml — mkdir lib-каталога обязателен), Python 3.12 + venv sandbox, TeX Live/pandoc/Quarto, gretl 2023c, pg_cron+pg_stat_statements (cron.database_name=research_wiki), code-server :8443, xrdp :3389, Tailscale research-db=100.89.141.127, vps=100.121.130.59.
§
Спеки: specs/ + spec_cli.py; ИКВ = kep1_63 (56187); freq_id v2: 2=мес, 3=кв; шаг 2 разметки не начата.
§
Инжест ЦБ в PG v2 завершён (релизы 91/95/96/101/102/108/110); КТ PASS; блоки API исчерпаны; очередь — шаг 2 разметка после «наполнение источников завершено» (решение владельца). Детали релизов и пайплайнов → queries/ingest-source-params.md.
§
Каталог v1 завершён (2440, карантин 180, unit 71%); проект → БД v2. Детали queries/db-v2-*.md.
§
Маршрутизация (AGENTS.md 51cc69c): БД/скрипты/парсеры → delegate_task (leaf, gpt-oss:120b); fedstat/JupyterLab → peer yc. Дорогие модели (Astra, выше Medium) — только вручную. delegation.model=gpt-oss:120b.
§
CBR ИБК: пересбор 23.09 из API www.cbr.ru/dataservice/data; сдвиги датировки НЕ единые — правило по dt↔date блока (таблица в queries/cbr-monitoring-api-rebuild.md); dataNew мёртв (501).
§
irz = канонический ряд ставок ИЖК; izhk_rate_fx 66/91 точек = 0 (нет валютных выдач с ~2025-03) — нули не трактовать как ставку.
§
Оперативные индикаторы (Wordstat-композит, чеки/ККТ, trudvsem, геолокация) — блок источников, а не отдельные ряды-факты в памяти: состав и параметры держать в queries/ingest-source-params.md; поиск недостающих рядов блока — отдельная задача «в целях определения» (какие ряды, частота, лаг). Владелец предпочитает разгружать память профиля переносом технических деталей в репо-справочники.
§
Модели (26.09): VPS-профили (default/macroeconomist) — nous/deepseek-v4.1-flash (вход $0,035, кэш $0,001, выход $0,290 за млн; дешевле ollama в 8,6 раза); ВМ monitor — ollama-cloud (nous с ВМ 403); делегаты — nous/openai/gpt-oss-120b; vision-aux — gemini-3.1-flash-lite; 12 cron-джобов перепинено на nous. Бэкап конфигов — config.yaml.bak-pre-nous-20260926; разбор цен → queries/model-config-20260926.md.
§
vmd = канонический код ИЖК (дефектные строки release 7 в карантине, observation_status=rejected); zyi/zyli_2 = корпдолг итого, zyli = валютная часть; нулевые virtr = нет выдач, а не ставка.
§
YouTube: Data API v3 недоступен (GCP_API_KEY — OAuth-токен AQ.Ab8…, нужен ключ AIza… в проекте); обход каналов — через RSS-фиды scripts/youtube_monitor.py + data/yt_channels.csv (11 каналов). Профильные институты (Минстрой, НОСТРОЙ, Росстат, Гайдар) на YouTube мертвы с 2021-2024 — живут на VK Видео/Rutube.
§
База v2 адресуема (27.09): derived.metric_card — 3530 карточек с векторами 256 (Яндекс), темы, свежесть; поиск scripts/metric_search.py, пересборка scripts/build_metric_cards.py (кэш по хешу).