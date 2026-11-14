const { chromium } = require('playwright');
const path = require('path');
const PV = process.env.PSS_PREVIEW || path.join(__dirname, '.preview'), OUT = process.env.PSS_SHOTS || path.join(__dirname, '.shots');
async function ctx(b, w, h) {
  const c = await b.newContext({ viewport: { width: w, height: h } });
  await c.route(/^https?:/, r => {
    const u = r.request().url();
    if (u.includes('fonts.googleapis')) return r.fulfill({ body: '', contentType: 'text/css' });
    return r.fulfill({ body: '<html><body style="margin:0;display:grid;place-items:center;height:100vh;font:20px sans-serif;background:#eef">Embedded: ' + u + '</body></html>', contentType: 'text/html' });
  });
  return c;
}
const res = [];
async function step(name, fn) { try { const r = await fn(); res.push('PASS ' + name + (r !== undefined ? ' -> ' + r : '')); } catch (e) { res.push('FAIL ' + name + ': ' + e.message.split('\n')[0]); } }
(async () => {
  const b = await chromium.launch(); const errs = [];
  let c = await ctx(b, 1366, 768); let p = await c.newPage(); p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + PV + '/home.html'); await p.waitForTimeout(500);
  await step('mega menu opens', async () => { await p.hover('.has-mm >> nth=1'); await p.waitForTimeout(400); return await p.locator('.has-mm >> nth=1 >> .mm-list li').count() + ' items'; });
  await step('carousel tabs', async () => { await p.mouse.move(10, 700); await p.click('.hc-tab >> nth=2'); await p.waitForTimeout(900); return await p.locator('.hc-tab[aria-pressed=true]').innerText(); });
  await step('viewer opens and closes', async () => { const a = p.locator('.case h3 a[href^="http"], .pc h3 a').first(); await p.goto('file://' + PV + '/websites.html'); await p.click('.site h3 a >> nth=1'); await p.waitForTimeout(500); const v = await p.locator('.pss-vw').isVisible(); await p.keyboard.press('Escape'); return 'visible ' + v + ', closed ' + !(await p.locator('.pss-vw').isVisible()); });
  await step('back to top', async () => { await p.mouse.wheel(0, 3000); await p.waitForTimeout(500); await p.click('.pss-top'); await p.waitForTimeout(1200); return 'scrollY ' + await p.evaluate(() => scrollY); });
  await step('embed loads on click', async () => { await p.goto('file://' + PV + '/labs.html'); await p.click('#showroom .emb-go'); await p.waitForTimeout(400); return await p.locator('#showroom iframe').count() + ' iframe'; });
  await step('medicore tabs', async () => { await p.goto('file://' + PV + '/medicore.html'); const t = p.locator('[role=tab]:visible').nth(2); await t.click(); await p.waitForTimeout(300); return await t.getAttribute('aria-selected'); });
  await step('live edit try box', async () => { await p.goto('file://' + PV + '/live-edit.html'); await p.click('[data-lt-edit] >> nth=0'); await p.keyboard.press('End'); await p.keyboard.type(' and evening'); await p.click('[data-lt-save]'); return 'saved'; });
  await step('simlab filter', async () => { await p.goto('file://' + PV + '/simlab.html'); const f = p.locator('[data-f]').nth(2); await f.click(); return await p.locator('#sg li:not([hidden])').count() + ' sims'; });
  await step('pos demo switch', async () => { await p.goto('file://' + PV + '/pos.html'); await p.click('.sw button >> nth=3'); await p.waitForTimeout(600); return (await p.locator('.sw button[aria-pressed=true], .sw button.on').count()) + ' active'; });
  await c.close();
  c = await ctx(b, 390, 844); p = await c.newPage(); p.on('pageerror', e => errs.push(e.message));
  await step('phone drawer', async () => { await p.goto('file://' + PV + '/home.html'); await p.click('.hd-burger'); await p.waitForTimeout(300); const open = await p.locator('.drawer').isVisible(); await p.screenshot({ path: OUT + '/i-drawer.png' }); return 'open ' + open; });
  await c.close(); await b.close();
  console.log(res.join('\n')); console.log('page errors:', errs);
})();
