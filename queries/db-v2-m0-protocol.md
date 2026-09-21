# Протокол M0: схема v2 развёрнута

**Дата:** 2026-09-21
**Коммит спеки:** 918caea (queries/db-v2-reload-spec.md)
**Среда:** ВМ research-db (YC), PostgreSQL research_wiki, схема `v2` (core не тронут)

## Состав (15 таблиц + 2 витрины)

Справочники: source (8), dataset, region, unit (11), frequency (4)
Каталог: domain (9), metric, metric_dataset_map
Конвейер: load_run (версии/шаблоны загрузок), load_check (верификация файлов)
Данные: observation (UNIQUE по run_id → версионность, is_current, quality_flags TEXT[])
Ревизии: series_revision (автодетект пересчётов между run)
Актуальность: freshness (fresh/lagging/stale + expected_next)
Витрины: v2.v_core_panel (панель ядра), v2.v_freshness_board

## Отличия от v1
- observation хранит run_id: ревизия = новая строка, история читается по любому run
- metric содержит методологию + parent_metric_id (подчинённость) в самом каталоге
- load_check: обязательная верификация каждого файла до подъёма is_current
- allowlist: метрики заводятся из потребностей анализа, не из листов файлов

## Фиксы при развёртывании
- USING(frequency_id) в view давал «common column name appears more than once»
  → явные ON-условия
- psql через ssh: параметры %s не пробрасывать, литеральные строки в SQL

## Сиды
frequency 4, unit 11, domain 9, source 8. Все ON CONFLICT DO NOTHING (идемпотентно).

## Следующий этап (M1)
Реестр датасетов ядра (12 карточек YAML) + список ~60 метрик ядра на утверждение владельца.
