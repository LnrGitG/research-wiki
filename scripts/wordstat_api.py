#!/usr/bin/env python3
"""Yandex Wordstat Search API v2 client — verified against live API 25.08.2026.

Verified facts:
- Auth: Api-Key works; folderId can be OMITTED (SA's own folder used)
- History: monthly & weekly from 2018-01 (matches Karpenko 2026 data start!)
- Daily: only ~last 60 days
- weekly: toDate must be a Sunday; monthly: last day of month
- One call returns full range: monthly ALL = 1 call, weekly ALL = 1 call
- count is a string, share is float (share of all Yandex queries)
"""
import os, json, time, urllib.request

API = "https://searchapi.api.cloud.yandex.net/v2/wordstat"


def _key():
    for line in open(os.path.expanduser('~/.hermes/.env')):
        if line.startswith('YANDEX_CLOUD_API_KEY='):
            return line.split('=', 1)[1].strip()
    raise RuntimeError("YANDEX_CLOUD_API_KEY not found in ~/.hermes/.env")


def dynamics(phrase, period='PERIOD_MONTHLY', date_from=None, date_to=None,
             regions=None, devices=None):
    """period: PERIOD_DAILY|PERIOD_WEEKLY|PERIOD_MONTHLY.
    date_from/date_to: 'YYYY-MM-DD'. Weekly: date_to must be Sunday; monthly: last day of month."""
    body = {"phrase": phrase, "period": period}
    if date_from: body["fromDate"] = f"{date_from}T00:00:00Z"
    if date_to:   body["toDate"] = f"{date_to}T00:00:00Z"
    if regions:   body["regions"] = [str(r) for r in regions]
    if devices:   body["devices"] = devices
    req = urllib.request.Request(f"{API}/dynamics",
                                 data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Api-Key {_key()}",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        d = json.load(r)
    out = pd_like(d.get('results', []))
    return out


def pd_like(results):
    """-> list of dicts {date, count:int, share:float}"""
    return [{"date": r["date"][:10], "count": int(r["count"]), "share": r["share"]}
            for r in results]


def top_requests(phrase, num_phrases=20, regions=None):
    body = {"phrase": phrase, "numPhrases": num_phrases}
    if regions: body["regions"] = [str(r) for r in regions]
    req = urllib.request.Request(f"{API}/topRequests",
                                 data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Api-Key {_key()}",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    return {"total_count": int(d.get("totalCount", 0)),
            "results": [(x["phrase"], int(x["count"])) for x in d.get("results", [])],
            "associations": [(x["phrase"], int(x["count"])) for x in d.get("associations", [])]}


if __name__ == "__main__":
    t0 = time.time()
    m = dynamics("ипотека", "PERIOD_MONTHLY", "2018-01-01", "2026-08-31")
    print(f"monthly ипотека: {len(m)} pts ({m[0]['date']} -> {m[-1]['date']}) in {time.time()-t0:.1f}s")
    print("first:", m[0], "\nlast: ", m[-1])
