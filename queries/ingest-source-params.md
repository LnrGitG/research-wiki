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
- Релиз 110 `iminfin_snapshot_2026-09-25`: 294 точки (исполнение/план/доля расходов, 98 регионов, частота день, period = дата снапшота); алиасы имён в `scripts/ingest_iminfin.py` (Татарстан, Кузбасс, Югра, Тюмень (без ХМАО и ЯНАО) и др.).
- КТ: РФ 972 602,8 / 2 604 580,6 млн / 37,34 %; Башкортостан 52,58 %.
- Не инжесты: трансферты (3 столбца без легенды), госдолг (доля только по ФО), помесячная история (клик-интерфейс), нацпроекты.

## ККТ ФНС (geochecki)
- API только с ВМ YC; `/api/api/v1/kkt/{summary,count-by-regions}/ГГГГ-М` (месяц без нуля), `count-dynamics/ГГГГ`; карта `/api/Metrics/bounds` — web-mercator метры, только последняя полная неделя.
- Релиз 108; cron job 356c0298e19e («0 6 8 * *»), пайплайн scripts/kkt_monthly_job.sh.
- Инжест scripts/ingest_kkt.py (FNS_TO_CODE; unmapped «99-Иные территории»).

## ЦБ РФ
- Релиз 91 `cbr_api_monitoring_v2` (307 332 строки, 739 метрик cbrmon_*/pb_ds*), КТ PASS; блоки API в v2 исчерпаны (ds25-40, 57, 140 — rows=0).
- CBR ИБК пересбор из API www.cbr.ru/dataservice/data (118=RAW, 119=SA); сдвиги датировки не единые — правило по dt↔date блока, таблица в queries/cbr-monitoring-api-rebuild.md.
- Скрипты cbr_monitoring_{api,facts,all}_collect.py (коммиты 0c3b7c4/d0ffa3e/dd5e192); dataNew мёртв (501); каталог scripts/cbr_api_catalog.py → data/cbr_api_catalog.txt.
- Ожидания: релизы 101 (inFOM 224 точки) + 102 (макроопрос 455 точек), scripts/ingest_expectations.py; канал Infl_exp_YY-MM.xlsx.
- irz = канонический ряд ставок ИЖК (VFS); izhk_rate_rub/fx (58082/83) derived; в izhk_rate_fx 66/91 точек = 0 (нет валютных выдач с ~2025-03) — нули не трактовать как ставку.

## Инфраструктура / правила v2
- freq_id v2: 2=мес, 3=кв (4=день); unit 12=pct, 13=pct_pts; ИКВ = kep1_63 (metric 56187).
- observation_v2 INSERT: period_end NOT NULL (для дневных = period_start); CHECK (assessment_type, observation_status) → ('final','validated').
- Батч-вставка через SSH-тоннель обязательна (построчный → timeout); db_tunnel.connect() → psycopg.Connection.
- Спеки: specs/ + spec_cli.py + derived.spec_runs/spec_diagnostics (diag.py авто); шаг 2 LLM-разметки не начата.