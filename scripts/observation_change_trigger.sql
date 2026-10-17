-- Уведомление слушателя витрины свежести: одно сообщение на команду, а не на строку.
-- Нужно потому, что pg_notify не переживает разрыв связи, а периодическое
-- обновление в pg_cron поставить не удалось (расширения на сервере нет) —
-- обязанность поднимать канал лежит на триггере, страховка — в самом слушателе.
--
-- Statement-level (FOR EACH STATEMENT): ингест вставляет наблюдения пачками,
-- построчный триггер дал бы десятки тысяч pg_notify на один прогон.
--
-- Откат: scripts/observation_change_trigger_rollback.sql

CREATE OR REPLACE FUNCTION data.notify_observation_change()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
BEGIN
    PERFORM pg_notify(
        'observation_changed',
        format('%s:%s', TG_TABLE_NAME, TG_OP)
    );
    RETURN NULL;
END
$function$;

DROP TRIGGER IF EXISTS trg_observation_change ON data.observation;

CREATE TRIGGER trg_observation_change
    AFTER INSERT OR UPDATE OR DELETE ON data.observation
    FOR EACH STATEMENT
    EXECUTE FUNCTION data.notify_observation_change();
