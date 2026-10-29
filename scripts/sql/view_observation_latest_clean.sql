-- derived.v_observation_latest — последняя ревизия каждого периода, без отклонённых.
--
-- Правка 29.10.2026. Что было не так: в DISTINCT ON участвовали все статусы, и
-- строка rejected (например, сентинел -999 или разобранная ошибка парсера) могла
-- оказаться «самой свежей» по дате релиза и вытеснить корректную ревизию. Замер
-- перед правкой: 35 819 отклонённых строк попадали в представление.
--
-- Что изменилось: отклонённые строки исключены из выбора. Если у периода есть
-- и отклонённая, и годная ревизия — побеждает годная; если годных нет вовсе, период
-- из представления исчезает, что и требуется: показывать нечего.
--
-- Обратимость: scripts/sql/view_observation_latest_ORIGINAL_20261029.sql.
-- Зависимые объекты: derived.v_observation_latest_recent (пересоздаётся автоматически
-- через CREATE OR REPLACE), витрины и вопросы Metabase читают по имени.
--
-- ВНИМАНИЕ: DROP VIEW ... CASCADE уносит зависимые представления. Применять этой
-- формой нельзя без пересоздания зависимых; в скрипте cleanup_apply.py используется
-- CREATE OR REPLACE с предварительной проверкой списка зависимостей.
CREATE OR REPLACE VIEW derived.v_observation_latest AS
 SELECT DISTINCT ON (o.metric_id, o.region_id, o.period_start, o.frequency_id, o.assessment_type, o.sub_dimension) o.observation_id,
    o.metric_id,
    o.region_id,
    o.period_start,
    o.period_end,
    o.value,
    o.value_str,
    o.observation_status,
    o.assessment_type,
    o.sub_dimension,
    o.quality_flags,
    o.frequency_id,
    o.source_id,
    o.release_id,
    o.event_id,
    o.created_at
   FROM (data.observation o
     LEFT JOIN catalog.release r ON ((r.release_id = o.release_id)))
  WHERE o.observation_status <> 'rejected'
  ORDER BY o.metric_id, o.region_id, o.period_start, o.frequency_id, o.assessment_type, o.sub_dimension, COALESCE(r.published_at, r.ingested_at, o.created_at) DESC NULLS LAST, o.release_id DESC, o.observation_id DESC;
