# Blocked-source recovery for literature sessions
Companion to the web `blocked-page-recovery` ladder (Wayback → archive.today →
Jina → API-first → browser). That ladder is generic; this file adds the
routes that matter when scanning literature while blocked.
## Platform-wide JSON blocks (Reddit class)
When a platform blocks every route at once — the scrape service answers
"Website Not Supported", the public JSON API (`reddit.com/...json`,
`api.reddit.com`) returns an HTML block shell instead of JSON, and the
alternate frontend (old.reddit) serves the same shell — do NOT spend
calls enumerating redlib/Libreddit mirrors: most are dead or bot-gated.
Once the JSON endpoint returns HTML you are blocked at the CDN/IP level;
rotating User-Agents or hosts of the same platform will not get through.
Pivot to derived copies instead:
1. `web_search` the exact post title in quotes → republications surface:
   X article versions, community digests, newsletter summaries of the
   subreddit (the post and its top comments are usually quoted with links).
2. Extract the digest as the source of quotes.
3. Cite with provenance: "via <digest>" and state explicitly that the
   original thread was not directly accessible.
## Validate every fetched body
Check content type or first bytes, not just size: an API endpoint whose
body starts with `<!DOCTYPE` or `<body` is a block page, not JSON. Rate-
limit bodies (archive.today 429 pages) ship multi-KB HTML that reads as a
success to a size check. Verify the target's actual strings (title words)
before treating a body as the page.
## When the block survives everything
Report the blocker to the user and cite secondary copies — never dress a
dead-end chain up as a completed fetch. Provenance honesty beats
completeness: a digest with the post quoted verbatim is a legitimate copy;
an unverifiable one is not.
- `references/blocked-source-recovery.md` — platform-wide JSON blocks (Reddit class) and derived-copy pivots when every direct route is gated; body-validation rules.