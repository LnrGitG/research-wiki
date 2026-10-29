-- derived.metric_progress — прогресс рядов одним снимком.
--
-- Зачем: сторожу свежести нужны «последний период и объём» по каждому ряду, а
-- считать это по data.observation (7,9 млн строк) дважды в день — 25 с на запрос
-- и лишняя нагрузка. Здесь агрегат материализован и обновляется перед прогоном
-- сторожа.
--
-- Почему по data.observation, а не по derived.v_observation_latest: последний
-- период и объём ряда инвариантны к выбору ревизии (max(period_end) и count не
-- зависят от того, взяли raw или validated), поэтому DISTINCT ON по 7,7 млн
-- строк дал бы ту же цифру за минуты вместо секунд. Правило релиза применяется
-- на витрине (v_bi_observation), а не в прогрессе.
--
-- rejected исключён: сентинелы и мусор не должны выглядеть как свежие данные.
-- regional_share — доля регионов, у которых есть последний период: позволяет
-- отличить «ряд обновился целиком» от «обновился один регион».

create materialized view if not exists derived.metric_progress as
with base as (
    select o.metric_id,
           count(*) as n_obs,
           max(o.period_start) as last_period_start,
           max(o.period_end) as last_period_end,
           mode() within group (order by o.frequency_id) as frequency_id,
           mode() within group (order by o.source_id) as source_id,
           max(o.created_at) as last_ingest_at
    from data.observation o
    where o.observation_status not in ('rejected', 'superseded')
    group by o.metric_id
),
latest as (
    select metric_id, max(period_start) as lp
    from data.observation
    where observation_status not in ('rejected', 'superseded')
    group by metric_id
),
per_region as (
    -- доля регионов на последнем периоде: без коррелированного подзапроса,
    -- иначе 7,9 млн строк превращаются в квадратичный план на десятки минут
    select o.metric_id,
           count(distinct o.region_id) as n_regions_total,
           count(distinct o.region_id) filter (where o.period_start = l.lp)
               as n_regions_latest
    from data.observation o
    join latest l on l.metric_id = o.metric_id
    where o.observation_status not in ('rejected', 'superseded')
    group by o.metric_id
)
select b.metric_id,
       b.n_obs,
       b.last_period_start,
       b.last_period_end,
       b.frequency_id,
       b.source_id,
       b.last_ingest_at,
       pr.n_regions_total,
       pr.n_regions_latest,
       m.metric_code,
       m.name_ru,
       m.status,
       now() as built_at
from base b
join catalog.metric m on m.metric_id = b.metric_id
left join per_region pr on pr.metric_id = b.metric_id
with no data;

create unique index if not exists metric_progress_metric_uq
    on derived.metric_progress (metric_id);
create index if not exists metric_progress_last_period_idx
    on derived.metric_progress (last_period_end);
