-- снимок 20.10.2026: FK derived.catalog_facets смотрел на снимок core.metric_legacy
ALTER TABLE derived.catalog_facets DROP CONSTRAINT IF EXISTS catalog_facets_metric_id_fkey;
ALTER TABLE derived.catalog_facets ADD CONSTRAINT catalog_facets_metric_id_fkey FOREIGN KEY (metric_id) REFERENCES core.metric_legacy(metric_id);
