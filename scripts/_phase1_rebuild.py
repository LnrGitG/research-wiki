# -*- coding: utf-8 -*-
"""Фаза 1, шаг 3: пересборка graph (kg_build_dkp.py) + шок-аннотации.

kg_build_dkp идемпотентен (upsert ON CONFLICT) — деструктива нет;
uncertainty-узлы не затрагивает (не входят в его циклы).
Шок-аннотации: _shock_annotations в kg_dkp_context.py — per-meeting,
обновляет props существующих узлов.
"""
import subprocess
import sys

VENV = "/home/lnr/.hermes/hermes-agent/venv/bin/python3"
BASE = "/home/lnr/research-wiki-private/scripts"

r = subprocess.run([VENV, BASE + "/kg_build_dkp.py"], capture_output=True, text=True, timeout=420)
print("kg_build_dkp rc=%d" % r.returncode)
print(r.stdout[-3000:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    sys.exit(1)