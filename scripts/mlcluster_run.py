#!/usr/bin/env python3
"""Выполнить произвольный Python-код ВНУТРИ пода пользователя на mlcluster JupyterHub.

Зачем: программно гонять разведку и расчёты в контуре mlcluster (шаг 6 переезда),
не заходя в веб-интерфейс. Работает через Jupyter Server API пода
(/user/<name>/api/kernels + WebSocket), токен берётся из JUPYTERHUB_TOKEN
(переменная окружения или ~/.hermes/.env) и никогда не печатается.

Примеры:
  ... mlcluster_run.py --file probe_deep.py
  echo 'import sys; print(sys.version)' | ... mlcluster_run.py -
  ... mlcluster_run.py -c 'import pandas; print(pandas.__version__)'

Код печатает stdout/stderr/результаты ячеек; маркер @@RUN@@ отделяет служебный JSON.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

import requests

HUB = "https://jupyterhub.mlcluster.ru"
USER = os.environ.get("JUPYTERHUB_USER_NAME", "gabdullinln")
SERVER = f"{HUB}/user/{USER}"


def load_token() -> str | None:
    tok = os.environ.get("JUPYTERHUB_TOKEN")
    if tok:
        return tok.strip()
    for f in (Path.home() / ".hermes" / ".env", Path.home() / ".env"):
        if not f.exists():
            continue
        for line in f.read_text(errors="ignore").splitlines():
            if line.strip().startswith("JUPYTERHUB_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


async def run(code: str, tok: str, timeout: int = 600, keep: bool = False) -> dict:
    import websockets

    out: dict = {}
    r = requests.post(f"{SERVER}/api/kernels", headers={"Authorization": f"token {tok}"},
                      json={"name": "python3"}, timeout=60)
    if r.status_code not in (200, 201):
        return {"error": f"create kernel HTTP {r.status_code}: {r.text[:400]}"}
    kid = r.json()["id"]
    out["kernel_id"] = kid
    ws_url = (SERVER + f"/api/kernels/{kid}/channels").replace("https://", "wss://")
    chunks: list[str] = []
    try:
        async with websockets.connect(ws_url, additional_headers={"Authorization": f"token {tok}"},
                                      max_size=2 ** 24, open_timeout=45) as ws:
            await ws.send(json.dumps({
                "header": {"msg_id": f"run-{int(time.time())}", "username": USER,
                           "session": "mlcluster-run", "msg_type": "execute_request",
                           "version": "5.3"},
                "parent_header": {}, "metadata": {},
                "content": {"code": code, "silent": False, "store_history": False,
                            "user_expressions": {}, "allow_stdin": False, "stop_on_error": True},
                "buffers": [], "channel": "shell"}))
            deadline = time.time() + timeout
            while time.time() < deadline:
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=45)
                except asyncio.TimeoutError:
                    continue
                msg = json.loads(raw)
                mt = msg.get("header", {}).get("msg_type")
                c = msg.get("content", {})
                if mt == "stream":
                    chunks.append(c.get("text", ""))
                elif mt == "execute_result":
                    chunks.append(c.get("data", {}).get("text/plain", ""))
                elif mt == "display_data":
                    chunks.append("[display_data]")
                elif mt == "error":
                    out["error"] = c.get("evalue")
                    chunks.append("\n".join(c.get("traceback", [])))
                elif mt == "execute_reply":
                    out["status"] = c.get("status")
                    break
    except Exception as e:  # noqa: BLE001
        out["ws_error"] = f"{type(e).__name__}: {e}"
    out["text"] = "".join(chunks)
    if not keep:
        try:
            requests.delete(f"{SERVER}/api/kernels/{kid}",
                            headers={"Authorization": f"token {tok}"}, timeout=30)
        except Exception:  # noqa: BLE001
            pass
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="файл с кодом")
    ap.add_argument("-c", "--code", help="код строкой")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--keep", action="store_true", help="не удалять ядро после прогона")
    args = ap.parse_args()

    if args.file == "-":
        code = sys.stdin.read()
    elif args.file:
        code = Path(args.file).read_text()
    elif args.code:
        code = args.code
    else:
        ap.error("нужен --file, --file - или -c")

    tok = load_token()
    if not tok:
        print("JUPYTERHUB_TOKEN не найден (переменная окружения или ~/.hermes/.env)")
        return 2
    res = asyncio.run(run(code, tok, timeout=args.timeout, keep=args.keep))
    print("@@RUN@@" + json.dumps({k: v for k, v in res.items() if k != "text"},
                                 ensure_ascii=False))
    print(res.get("text", ""))
    return 0 if res.get("status") == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
