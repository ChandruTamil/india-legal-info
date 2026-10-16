# NyayaSetu — Indian Legal Information

Plain-language browser for Indian central laws.

- Searches the official **IndiaCode** JSON API (`indiacode.ecourtsindia.com`)
- Shows each act's title, year, number, description
- Maps every result to its official text URL
- Footer disclaimer: general information, not legal advice — consult a licensed advocate

## Run locally

Open `index.html` in a browser, or serve it:

```bash
python -m http.server 8000
```

Then visit http://localhost:8000

## Stack

Single static file. No build step, no backend. Deployable to GitHub Pages, Netlify, or any static host.

## Data source

IndiaCode public API — no key, no quota. See https://indiacode.ecourtsindia.com
