# -*- coding: utf-8 -*-
"""kg_uncertainty.py — графовая оболочка слоя неопределённости.

Рёбра (универсальный словарь, queries/dkp-uncertainty-layer-design.md):
- has_uncertainty (cbr_meeting → cbr_uncertainty_item) — НОВЫЙ тип;
- uses_metric (cbr_uncertainty_item → metric) — СУЩЕСТВУЮЩИЙ тип
  (переменные, у которых есть прогнозная серия: fuel→oil_price_tax,
  demand→cons_total, credit→claims_total, inflation_now→inflation_dec);
- wikilinks (cbr_uncertainty_item → cbr_concept) — для переменных без
  метрик (budget, labour, fx, inflation_expect, external, transmission,
  power_capacity).
Идемпотентно; provenance содержит item_id — FK-эквивалент.
"""
import json
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query, execute

ITEM_METRIC = {"fuel": "oil_price_tax",
               "demand": "cons_total",
               "credit": "claims_total",
               "inflation_now": "inflation_dec"}

CONCEPT_VARS = {"power_capacity": "Выбытие/восстановление производственных мощностей",
                "budget": "Бюджетный импульс (первичный дефицит, налоги)",
                "demand": "Внутренний спрос",
                "credit": "Кредитная активность",
                "labour": "Рынок труда (напряжённость, дефицит кадров)",
                "fx": "Валютный курс и перенос",
                "inflation_expect": "Инфляционные ожидания",
                "transmission": "Трансмиссия ДКП",
                "inflation_now": "Текущая устойчивая инфляция",
                "external": "Внешние условия (мировая экономика, цены)",
                "other": "Прочее"}


def esc(s):
    return s.replace("'", "''")


def jdump(d):
    return json.dumps(d, ensure_ascii=False).replace("'", "''")


def ensure_concept(ref_key, title):
    sql = ("INSERT INTO graph.node (ref_key, node_type, title, props) "
           "VALUES ('%s', 'cbr_concept', '%s', '{}'::jsonb) "
           "ON CONFLICT (node_type, ref_key) DO NOTHING"
           ) % (esc(ref_key), esc(title))
    execute(sql)


def link(src_ref, dst_ref, edge_type, prov):
    sql = ("INSERT INTO graph.edge (src_id, dst_id, edge_type, provenance) "
           "SELECT s.node_id, d.node_id, '%s', '%s'::jsonb "
           "FROM graph.node s, graph.node d "
           "WHERE s.ref_key='%s' AND d.ref_key='%s' "
           "ON CONFLICT (src_id, dst_id, edge_type) DO UPDATE "
           "SET provenance = EXCLUDED.provenance"
           ) % (edge_type, jdump(prov), esc(src_ref), esc(dst_ref))
    execute(sql)


def main():
    n_items = n_edges = 0
    items = query("""
        SELECT item_id, meeting_id, kind, variable, direction,
               COALESCE(text_short, text_raw)
        FROM dkp.uncertainty_item ORDER BY item_id""")
    for iid, mid, kind, var, direction, title in items:
        ref = "uncertainty:%d" % iid
        props = {"kind": kind, "variable": var, "direction": direction,
                 "meeting_id": mid}
        sql = ("INSERT INTO graph.node (ref_key, node_type, title, props) "
               "VALUES ('%s', 'cbr_uncertainty_item', '%s', '%s'::jsonb) "
               "ON CONFLICT (node_type, ref_key) DO UPDATE "
               "SET title = EXCLUDED.title, props = EXCLUDED.props"
               ) % (esc(ref), esc(title[:160] if title else ref), jdump(props))
        execute(sql)
        n_items += 1

        # has_uncertainty: meeting → item
        link("meeting:%d" % mid, ref, "has_uncertainty",
             {"item_id": iid, "source": "dkp.uncertainty_item"})
        n_edges += 1

        # привязка к переменной: метрика или concept
        met = ITEM_METRIC.get(var)
        if met:
            link(ref, "metric:%s" % met, "uses_metric",
                 {"item_id": iid, "variable": var})
            n_edges += 1
        elif var in CONCEPT_VARS:
            cref = "concept:%s" % var
            ensure_concept(cref, CONCEPT_VARS[var])
            link(ref, cref, "wikilinks",
                 {"item_id": iid, "variable": var})
            n_edges += 1
    print(f"узлов items: {n_items}, рёбер создано/обновлено: {n_edges}")


if __name__ == "__main__":
    main()