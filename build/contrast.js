const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const PV = process.env.PSS_PREVIEW || path.join(__dirname, '.preview');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1366, height: 768 } });
  await p.route(/^https?:/, r => r.abort());
  for (const f of fs.readdirSync(PV).filter(f => f.endsWith('.html'))) {
    await p.goto('file://' + PV + '/' + f);
    const bad = await p.evaluate(() => {
      function rgb(s) { const m = s.match(/[\d.]+/g); return m ? m.map(Number) : null; }
      function lum(c) { const a = c.slice(0, 3).map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * a[0] + .7152 * a[1] + .0722 * a[2]; }
      function blend(fg, bg) { const a = fg[3] === undefined ? 1 : fg[3]; return [0, 1, 2].map(i => fg[i] * a + bg[i] * (1 - a)); }
      function bgOf(el) { const stack = []; while (el) { const cs = getComputedStyle(el); const c = rgb(cs.backgroundColor); if (c && (c[3] === undefined || c[3] > 0)) { stack.push(c); if (c[3] === undefined || c[3] >= 1) break; } if (cs.backgroundImage !== 'none' && !cs.backgroundImage.includes('url(') && cs.backgroundImage.includes('gradient') && el.tagName !== 'SECTION') return null; el = el.parentElement; }
        let base = [255, 255, 255]; for (let i = stack.length - 1; i >= 0; i--) base = blend(stack[i], base); return base; }
      const out = []; const seen = new Set();
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      while (walker.nextNode()) { const t = walker.currentNode; if (!t.textContent.trim()) continue; const el = t.parentElement; if (seen.has(el)) continue; seen.add(el);
        const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none' || el.closest('[aria-hidden=true],[hidden],[data-off],.mm,.drawer,.emb-poster')) continue;
        const r = el.getBoundingClientRect(); if (!r.width) continue;
        const bg = bgOf(el); if (!bg) continue; const fg = blend(rgb(cs.color), bg);
        const L1 = lum(fg), L2 = lum(bg), cr = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
        const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700; const large = size >= 24 || (bold && size >= 18.66);
        if (cr < (large ? 3 : 4.5)) out.push(cr.toFixed(2) + ' ' + el.tagName + '.' + (el.className || '').toString().slice(0, 30) + ' "' + t.textContent.trim().slice(0, 30) + '"'); }
      return out; });
    if (bad.length) console.log(f, bad.length, '\n  ' + [...new Set(bad)].slice(0, 12).join('\n  '));
  }
  await b.close();
})();
