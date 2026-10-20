# Параметры инжеста источников (перенос из памяти профиля, 2026-09-25)

Справочник технических деталей инжеста. Память профиля держит только однострочные
якоря; подробности живут здесь и в соответствующих scripts/queries. Обновлять при
изменении пайплайнов.

## ЕМИСС (Росстат)
- Инжест через ВМ YC: R fedstatAPIr 1.1.0 (`emiss_collect2.R`); сырые POST-фильтры dataGrid не работают.
- Реестр владельца: 22/23 → релиз `emiss_registry_batch1_2026-09` (1 894 271 строка, 24 метрики `emiss_*`; 39233 отложен).
- sub = '<РФ|РФ-без-новых> | срезы'; флаги cumulative_jan_NN, stock_on_07.
- КТ: розница 2024 = 107,7; ЗП 06.2024 = 89 144,9.
- trudvsem API открыт (cron); api.hh.ru — нужна регистрация (решение владельца); rmsp ищется.
- Отчёт: queries/emiss-registry-batch1-ingest.md.

## ФНС / Точно-ст
- Единицы: тыс. руб; 87 % simplified; фильтр filed=1 AND line_2110>0 (~25К фирм).
- Агрегат F corr +0,96/+0,99 с ИКВ; L не работает (−0,34).
- RFSD панель: 15 parquet 2011–2025 (60,1 млн × 214/224 col) на ВМ ~/raw/rfsd/; займы заполнены с ~2016; v2_stage.rfsd_slice не создана (OOM-kill исполнителя).
- Urbanica: 52 агломерации в CSV + бакет.

## Wordstat СМР
- Композит S2–S5 lead-1m r=0,644 (n=18); уровневая OLS непригодна — MIDAS/алмон.
- scripts/wordstat_api.py.

## iminfin (iМониторинг КРИСТА, региональные бюджеты)
- Скрапер `scripts/iminfin_scrape.js` (node + playwright) — работает только с ВМ YC (BI-хосты copen-imon/wf-imon.fm.epbs.ru не отвечают с VPS); POST `/redirect/copen-imon/Data?uuid=…` отдаёт чистый JSON.
- Снапшоты: `~/yc-wiki/raw/iminfin/<date>/` + зеркало yc-s3:wiki-research/raw/iminfin.
- Релизы 110 (`iminfin_snapshot_2026-09-25`) + 171 (`iminfin_snapshot_2026-09-21`): 6 метрик × 2 снапшота × ~98 регионов = 936 наблюдений (исполнение/план/доля расходов, расходы на душу, трансферты, госдолг), частота день, period = дата снапшота; алиасы имён в `scripts/ingest_iminfin.py` (Татарстан, Кузбасс, Югра, Тюмень (без ХМАО и ЯНАО) и др.).
- Каноническая схема: `catalog.source/metric/release` + `data.observation` + `catalog.region` (переписано 06.10.2026 с core.* на catalog.*/data.*).
- КТ: РФ 972 602,8 / 2 604 580,6 млн / 37,34 %; Башкортостан 52,58 %; РФ на душу 6 656 руб/чел.
- Трансферты: raw в тыс. руб → конвертация /1e3 в млн руб; col0 (план ФЗ) при наличии, col1 (распределено) при None — 27 регионов (Москва, СПб, Татарстан и др.); РФ 1 098 923 млн, ratio transferty/exec = 1,13.
- Госдолг: доля к доходам, только по ФО (8 округов), raw в долях → as-is (unit=pct).
- Не инжесты: помесячная история (клик-интерфейс), нацпроекты, кредиты, доходы (динамика).

## hh.ru (HeadHunter API)
- OpenAPI spec: `https://api.hh.ru/openapi/specification/public` (YAML, 109 путей, OAuth2 OauthToken).
- Авторизация: OAuth2, два flow — `authorizationCode` (пользовательский) и `clientCredentials` (app-level, без браузера); token: `POST https://api.hh.ru/token` с `grant_type=client_credentials`, `client_id`, `client_secret`.
- Регистрация приложения: https://dev.hh.ru/admin → client_id + client_secret → `.env` (HH_CLIENT_ID, HH_CLIENT_SECRET).
- Без авторизации доступны только справочники: `/areas` (16 836 регионов), `/industries` (30 отраслей), `/professional_roles` (27 категорий), `/dictionaries`, `/salary_statistics/dictionaries/*`.
- С авторизацией: `/vacancies` (поиск, пагинация `page&per_page` max 100, ответ `{found, pages, page, items}`), `/resumes` (поиск), `/salary_statistics/paid/salary_evaluation/{area_id}` (оценка ЗП, платный).
- Скрипт: `scripts/hh_index_collect.py` — каноническая схема (`catalog.source/metric/release` + `data.observation`), сбор вакансий по тексту «строительство» + региональный разрез, avg/median ЗП из `only_with_salary=true`.
- Метрики: `hh_vacancies_count_m` (29/count), `hh_avg_salary_m` (38/rub), `hh_median_salary_m` (38/rub), `hh_vacancies_with_salary_m` (29/count); freq=5 (месячная), source_id=32.
- Справочники сохранены: `~/yc-wiki/raw/hh/areas_2026-10-06.json`, `industries_*.json`, `professional_roles_*.json`.
- stats.hh.ru (открытая аналитика) защищён DDoS-Guard + кастомная авторизация (hhuId/cryptedId) — не подходит для автоматического сбора.
- **Статус: ожидает регистрации приложения на dev.hh.ru/admin.**

## ККТ ФНС (geochecki)
- API только с ВМ YC; `/api/api/v1/kkt/{summary,count-by-regions}/ГГГГ-М` (месяц без нуля), `count-dynamics/ГГГГ`; карта `/api/Metrics/bounds` — web-mercator метры, только последняя полная неделя.
- **Периодичность уточнена 29.09.2026**: платформа отдаёт только МЕСЯЧНЫЕ агрегаты ККТ (summary по ГГГГ-М; count-dynamics — помесячные серии, август = последняя заполненная точка). Ежедневного месячного обновления API не существует: «ежедневное обновление» относится к карте геочек (`/geochecks`, последняя полная неделя), а не к ККТ-статистике. Проверено: `summary/2026-9` → 404 (текущий месяц не публикуется), weekly-эндпоинты не существуют (HTML SPA вместо API).
- Релиз 108; cron job 356c0298e19e («0 6 8 * *»), пайплайн scripts/kkt_monthly_job.sh.
- Инжест scripts/ingest_kkt.py (FNS_TO_CODE; unmapped «99-Иные территории»).

## ЦБ РФ
- Релиз 91 `cbr_api_monitoring_v2` (307 332 строки, 739 метрик cbrmon_*/pb_ds*), КТ PASS; блоки API в v2 исчерпаны (ds25-40, 57, 140 — rows=0).
- CBR ИБК пересбор из API www.cbr.ru/dataservice/data (118=RAW, 119=SA); сдвиги датировки не единые — правило по dt↔date блока, таблица в queries/cbr-monitoring-api-rebuild.md.
- Скрипты cbr_monitoring_{api,facts,all}_collect.py (коммиты 0c3b7c4/d0ffa3e/dd5e192); dataNew мёртв (501); каталог scripts/cbr_api_catalog.py → data/cbr_api_catalog.txt.
- Ожидания: релизы 101 (inFOM 224 точки) + 102 (макроопрос 455 точек), scripts/ingest_expectations.py; канал Infl_exp_YY-MM.xlsx.
- irz = канонический ряд ставок ИЖК (VFS); izhk_rate_rub/fx (58082/83) derived; в izhk_rate_fx 66/91 точек = 0 (нет валютных выдач с ~2025-03) — нули не трактовать как ставку.

## Казначейство (roskazna, source_id=33) — ИСКЛЮЧЕН из наблюдения
- **Решение (06.10.2026):** источник исключён из наблюдения — отчёты datamarts.roskazna.ru
  содержат данные только за 2023 год, оперативность недостаточна для nowcasting.
- БД: catalog.source source_id=33 (roskazna) → is_active=False; 0 наблюдений, 0 релизов.
- Метрики в каталоге (зомби, без наблюдений): 74618 (0501 ЖКХ), 74619 (0502 ЖКХ), 74620 (итого).
- Скрипт scripts/roskazna_collect.py — заготовка, не использовался (datamarts.roskazna.ru
  требует JS-рендеринг Krista BI, недоступен с VPS по SSL).
- Альтернатива: iminfin (iМониторинг КРИСТА) — региональные бюджеты в реальном времени,
  релиз 110, 294 точки; см. секцию iminfin выше.

## Инфраструктура / правила v2
- freq_id v2: 2=мес, 3=кв (4=день); unit 12=pct, 13=pct_pts; ИКВ = kep1_63 (metric 56187).
- observation_v2 INSERT: period_end NOT NULL (для дневных = period_start); CHECK (assessment_type, observation_status) → ('final','validated').
- Батч-вставка через SSH-тоннель обязательна (построчный → timeout); db_tunnel.connect() → psycopg.Connection.
- Спеки: specs/ + spec_cli.py + derived.spec_runs/spec_diagnostics (diag.py авто); шаг 2 LLM-разметки не начата.
## Промноменклатура Росстата (медиабанк бюллетеней)
- Источник: `https://rosstat.gov.ru/storage/mediabank/<имя>`; имена за разные годы
  пишутся по-разному: `prom_MM-2023.xlsx`, `prom_MM-2024.xlsx`, `Prom_MM-2025.xlsx`,
  `prom_MM_YYYY.xlsx` (2026, подчёркивание), разовые — `Prom_07_2024.xlsx`,
  `Prom_12_2023.xlsx`, `Prom_12-2024.xlsx`, `Prom_12_2025.xlsx`.
- `Prom_12_2025.xlsx` отдаётся только с заголовком `Referer: https://rosstat.gov.ru/enterprise_industrial`;
  без него 404 (ловушка: выглядит как снятый файл).
- Перечень актуальных ссылок — на странице `https://rosstat.gov.ru/enterprise_industrial`
  (grep по `href="/storage/mediabank/.*[Pp]rom.*xlsx"`); часть ссылок ведёт на 2021 год
  (`Prom-january.xlsx` и др.) — период всегда проверять по шапке файла, а не по имени.
- Период бюллетеня: лист «Содержание», строка вида «…за январь 2024 года».
- Сопоставление продуктов: имя в каталоге обрезано до 200 символов
  (`direct_core.ensure_metric`), поэтому ключ сравнения — `('Промпродукция, месяц: '+product)[:200]`;
  переименования ловятся картой код ОКПД2 (графа B) → имя из текущего бюллетеня.
- Загрузчики: `scripts/direct_rosstat_prom.py` (текущий месяц, cron 13-го),
  `scripts/backfill_prom_history.py` (архив, окно `--from/--to`),
  `scripts/backfill_prom_2023.py` (резерв через сводный `Proizvodstvo_mes_2023.xlsx`).
- Состояние на 20.10.2026: 36 месяцев подряд (2023-09…2026-08), 130 839 наблюдений
  варианта «месяц», 0 дублей; «накопленным итогом» — производные (is_derived).
