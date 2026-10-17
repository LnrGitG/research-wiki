-- Откат триггера уведомлений (см. scripts/observation_change_trigger.sql).

DROP TRIGGER IF EXISTS trg_observation_change ON data.observation;
DROP FUNCTION IF EXISTS data.notify_observation_change();
