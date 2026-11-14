const { chromium } = require('playwright');
const path = require('path');
const PV = process.env.PSS_PREVIEW || path.join(__dirname, '.preview'), OUT = process.env.PSS_SHOTS || path.join(__dirname, '.shots'), STUB = path.join(__dirname, 'stub');
async function ctx(b, w, h) {
  const c = await b.newContext({ viewport: { width: w, height: h } });
  await c.route(/^https?:/, r => { const u = r.request().url();
    if (u.includes('LOGOwhitetrans')) return r.fulfill({ path: path.join(STUB, 'logo-white.svg'), contentType: 'image/svg+xml' });
    if (u.includes('LOGO-LOGO')) return r.fulfill({ path: path.join(STUB, 'logo-dark.svg'), contentType: 'image/svg+xml' });
    if (u.includes('LOGO-SYMBOL')) return r.fulfill({ path: path.join(STUB, 'mark.svg'), contentType: 'image/svg+xml' });
    if (u.includes('fonts.googleapis')) return r.fulfill({ body: '', contentType: 'text/css' });
    return r.fulfill({ body: '<html><body style="margin:0;display:grid;place-items:center;height:100vh;font:20px sans-serif;background:#eef">Embedded page: ' + u + '</body></html>', contentType: 'text/html' });
  });
  return c;
}
(async () => {
  const b = await chromium.launch(); const errs = [];
  let c = await ctx(b, 1366, 768); let p = await c.newPage(); p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto('file://' + PV + '/home.html'); await p.waitForTimeout(600);
  await p.hover('.has-mm >> nth=0'); await p.waitForTimeout(400); await p.screenshot({ path: OUT + '/i-mega-products.png' });
  await p.hover('.has-mm >> nth=2'); await p.waitForTimeout(400); await p.screenshot({ path: OUT + '/i-mega-labs.png', clip: { x: 0, y: 0, width: 1366, height: 520 } });
  await p.mouse.move(10, 700); await p.click('.hc-tab >> nth=1'); await p.waitForTimeout(1000); await p.screenshot({ path: OUT + '/i-car-pos.png' });
  await p.click('.hc-tab >> nth=3'); await p.waitForTimeout(1000); await p.screenshot({ path: OUT + '/i-car-le.png' });
  await p.click('.hc-tab >> nth=2'); await p.waitForTimeout(1000); await p.screenshot({ path: OUT + '/i-car-portal.png' });
  await p.click('.hc-tab >> nth=4'); await p.waitForTimeout(1000); await p.screenshot({ path: OUT + '/i-car-labs.png' });
  // embed
  await p.click('.lab-c .emb-go >> nth=0'); await p.waitForTimeout(500);
  console.log('iframes after click:', await p.locator('.lab-c iframe').count());
  // tabs on medicore
  await p.goto('file://' + PV + '/medicore.html'); await p.click('.tab >> nth=3'); await p.waitForTimeout(300);
  console.log('visible panels:', await p.locator('.tab-panel:not([data-off])').count(), await p.locator('.tab[aria-selected=true]').innerText());
  await p.locator('#features').screenshot({ path: OUT + '/i-mc-tabs.png' });
  // live edit try
  await p.goto('file://' + PV + '/live-edit.html');
  await p.click('[data-lt-edit] >> nth=0'); await p.keyboard.press('End'); await p.keyboard.type(' and evening');
  await p.click('[data-lt-save]'); await p.hover('.lt-card >> nth=0'); await p.click('.lt-card >> nth=0 >> [data-a=dup]'); await p.click('[data-lt-img] >> nth=0');
  await p.locator('#try').screenshot({ path: OUT + '/i-le-try.png' });
  // simlab filter
  await p.goto('file://' + PV + '/simlab.html'); await p.click('[data-f=chemistry]');
  console.log('visible sims chemistry:', await p.locator('#sg li:not([hidden])').count());
  // pos demo
  await p.goto('file://' + PV + '/pos.html'); await p.click('.sw button[data-type=restaurant]'); await p.waitForTimeout(800);
  console.log('pos iframe src:', await p.locator('#pp-scr iframe').getAttribute('src'));
  await p.locator('.pos-demo').screenshot({ path: OUT + '/i-pos-demo.png' });
  await c.close();
  c = await ctx(b, 390, 844); p = await c.newPage(); p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + PV + '/home.html'); await p.click('.hd-burger'); await p.waitForTimeout(300);
  await p.click('.drawer summary >> nth=0'); await p.waitForTimeout(300); await p.screenshot({ path: OUT + '/i-drawer.png' });
  await c.close(); await b.close();
  console.log('errors:', errs);
})();
