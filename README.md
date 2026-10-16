# NyayaSetu — Indian Legal Information

Plain-language browser for Indian central laws, with a CORS-proof proxy.

## Files

- `index.html` — the app (search box, result cards, disclaimer)
- `worker.js` — Cloudflare Worker that serves the page **and** proxies `/api/search` to IndiaCode server-side, so the browser never hits CORS
- `wrangler.toml` — deploy config

## Why the proxy

IndiaCode's API sends no `Access-Control-Allow-Origin` header. A plain `fetch()` from the browser gets blocked. The Worker forwards the request from its own origin, which is allowed, and returns the JSON with CORS headers attached.

## Deploy (free)

```bash
npm i -g wrangler
wrangler login
wrangler deploy
```

That gives you `https://nyayasetu.<your-subdomain>.workers.dev` — page and API on one origin, zero cost, no card.

## Run locally without Cloudflare

```bash
python -m http.server 8000
```

Direct mode will fail on search due to CORS — that's expected. The Worker is what makes search work in production.

## Data source

IndiaCode public API — no key, no quota. https://indiacode.ecourtsindia.com

## Disclaimer

General information only, not legal advice. Consult a licensed advocate for anything affecting rights or obligations.
