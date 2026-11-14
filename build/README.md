# Page generator

The page designs in `../blocks/*.html` are generated from these Python modules. Edit the modules, not the blocks.

- `lib.py` – shared parts: header, footer, sections, tabs, journeys (`journey_tour`), screen tours (`tour`), real screenshots (`shot`, with address-bar text in `URLS`).
- `pages_core.py` (home, products, Live Edit), `pages_prod.py` (MediCore, POS), `pages_prod2.py` (Portal, BeautySuite, Learning, NGO Portal, QR Analytics), `pages_more.py` (solutions, labs, SimLab, data and maps, websites, work, about, contact, the old /dashboards/ address), `mocks.py` (HTML/CSS illustrations with sample data).
- `../assets/pss.css` and `../assets/pss.js` are written by hand.

Build and check:

```
python3 build.py      # writes ../blocks/*.html, plus setup-pages.php.txt and products.txt (copy into includes/ if pages or products change)
python3 preview.py    # wraps each block in a test page in .preview/, using the real images in ../assets/img
node shoot.js         # Playwright: 1366, 1024 and 390 px screenshots in .shots/, flags horizontal scroll, clipped content and console errors
python3 dsheet.py .shots/<file>.png   # contact sheets for reading long screenshots
```

After pushing to GitHub, use "Update from GitHub" in wp-admin → Pentarch Systems (with "restore the page designs" ticked) to import the new blocks into Live Edit.
