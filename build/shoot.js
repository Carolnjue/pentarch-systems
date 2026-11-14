// Playwright screenshots + checks. usage: node shoot.js [slug,slug] [tag]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const PV = process.env.PSS_PREVIEW || path.join(__dirname, '.preview'), OUT = process.env.PSS_SHOTS || path.join(__dirname, '.shots');
const STUB = path.join(__dirname, 'stub');
const only = (process.argv[2] || '').split(',').filter(Boolean);
const tag = process.argv[3] || 'p';
const VPS = [['d', 1366, 768], ['t', 1024, 768], ['m', 390, 844]];
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch();
  const pages = fs.readdirSync(PV).filter(f => f.endsWith('.html')).map(f => f.slice(0, -5)).filter(s => !only.length || only.includes(s));
  const report = [];
  for (const [vk, W, H] of VPS) {
    const ctx = await b.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
    await ctx.route(/^https?:/, r => {
      const u = r.request().url();
      if (u.includes('LOGOwhitetrans')) return r.fulfill({ path: path.join(STUB, 'logo-white.svg'), contentType: 'image/svg+xml' });
      if (u.includes('LOGO-LOGO-TRANSPARENT')) return r.fulfill({ path: path.join(STUB, 'logo-dark.svg'), contentType: 'image/svg+xml' });
      if (u.includes('LOGO-SYMBOL')) return r.fulfill({ path: path.join(STUB, 'mark.svg'), contentType: 'image/svg+xml' });
      if (u.includes('fonts.googleapis')) return r.fulfill({ body: '', contentType: 'text/css' });
      return r.abort();
    });
    for (const s of pages) {
      const p = await ctx.newPage();
      const errs = [];
      p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
      p.on('pageerror', e => errs.push('PAGEERROR ' + e.message));
      await p.goto('file://' + path.join(PV, s + '.html'));
      await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 30)); } window.scrollTo(0, 0); });
      await p.evaluate(() => Promise.all([...document.images].map(i => i.decode().catch(() => 0))));
      await p.waitForTimeout(1200);
      const info = await p.evaluate(() => {
        const de = document.documentElement, over = [];
        if (de.scrollWidth > window.innerWidth + 1) {
          document.querySelectorAll('body *').forEach(el => { const r = el.getBoundingClientRect(); if (r.right > window.innerWidth + 1 && r.width > 0 && getComputedStyle(el).position !== 'fixed') { let p = el.parentElement, clipped = false; while (p) { const o = getComputedStyle(p).overflowX; if (o !== 'visible') { clipped = true; break; } p = p.parentElement; } if (!clipped) over.push(el.tagName + '.' + el.className.toString().slice(0, 40) + ' ' + Math.round(r.right)); } });
        }
        // content pushed past the right edge but hidden by overflow clipping (not inside a scroller)
        document.querySelectorAll('.pss h1,.pss h2,.pss h3,.pss p,.pss .btn,.pss img').forEach(el => {
          const r = el.getBoundingClientRect(); if (!r.width || r.right <= window.innerWidth + 1 || r.left >= window.innerWidth) return;
          if (el.closest('[aria-hidden=true],.mm,.drawer,[data-off],[hidden],.emb-poster')) return;
          let p = el.parentElement; while (p) { const o = getComputedStyle(p).overflowX; if (o === 'auto' || o === 'scroll') return; p = p.parentElement; }
          over.push('CLIP ' + el.tagName + '.' + el.className.toString().slice(0, 30) + ' ' + Math.round(r.right));
        });
        return { sw: de.scrollWidth, h: de.scrollHeight, over: over.slice(0, 8) };
      });
      const f = path.join(OUT, `${tag}-${s}-${vk}.png`);
      await p.screenshot({ path: f, fullPage: true });
      report.push({ s, vk, sw: info.sw, W, h: info.h, over: info.over, errs: errs.filter(e => !/ERR_FAILED|ERR_BLOCKED|net::/.test(e)) });
      await p.close();
    }
    await ctx.close();
  }
  await b.close();
  for (const r of report) {
    const bad = r.sw > r.W || r.errs.length || r.over.length;
    console.log(`${bad ? 'XX' : 'ok'} ${r.s.padEnd(13)} ${r.vk} h=${r.h} sw=${r.sw}${r.over.length ? ' OVER ' + r.over.join(' | ') : ''}${r.errs.length ? ' ERR ' + r.errs.join(' | ') : ''}`);
  }
})();
