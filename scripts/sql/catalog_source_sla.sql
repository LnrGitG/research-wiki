-- catalog.source_sla — норматив публикации по источнику (SLA свежести).
--
-- Зачем: сторож свежести сравнивал ряд с произвольным допуском в днях, из-за
-- чего реальное опоздание источника не отличалось от нормы. Норматив теперь
-- лежит данными и обновляется из фактических наблюдений: p90 лага публикации
-- по derived.v_publication_lag_trusted (там только релизы с настоящей датой
-- публикации; даты, скопированные из времени приёма, в этот слой не попадают).
--
-- basis = 'measured' — посчитано по n_obs наблюдениям (>= 20),
-- basis = 'assumed'  — запасное значение из scripts/source_sla_assumed.json,
--                       до накопления настоящих дат публикации.
--
-- Обратимость: drop table catalog.source_sla; приложение читает таблицу
-- терпимо к её отсутствию (падает на значения по умолчанию).

create table if not exists catalog.source_sla (
    source_id      integer primary key references catalog.source(source_id),
    lag_p90_days   integer not null check (lag_p90_days >= 0),
    lag_median_days integer,
    basis          text not null check (basis in ('measured', 'assumed')),
    n_obs          integer not null default 0,
    measured_at    timestamptz,
    note           text,
    updated_at     timestamptz not null default now()
);

comment on table catalog.source_sla is
    'Норматив публикации (дни) по источнику: p90 наблюдённого лага или запасное значение. Читается сторожем fresh-ness_digest.py.';
