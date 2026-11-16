/* Pentarch Systems Solutions — site behaviour. No dependencies. Every feature degrades to plain HTML without JS. */
(function () {
  'use strict';
  var d = document, w = window;
  d.documentElement.classList.add('js');
  var reduce = w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $$(s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); }
  function once(el, k) { if (!el || el.getAttribute('data-pss-' + k)) return false; el.setAttribute('data-pss-' + k, '1'); return true; }
  var IO = 'IntersectionObserver' in w;

  /* ---------- header: current item, mega menus, drawer */
  function header() {
    var hd = d.querySelector('[data-pss-header]');
    if (!once(hd, 'hd')) return;
    var path = location.pathname.replace(/\/+$/, '/') || '/';
    $$('.hd-nav .nl', hd).forEach(function (a) {
      var h = a.getAttribute('href');
      if (h && h !== '/' && path.indexOf(h) === 0) a.setAttribute('aria-current', 'page');
    });
    var items = $$('.has-mm', hd);
    /* menu pictures load on first use, or once the page is idle, not with the page */
    function bg(scope) { $$('[data-bg]', scope).forEach(function (el) { el.style.backgroundImage = 'url(' + el.getAttribute('data-bg') + ')'; el.removeAttribute('data-bg'); }); }
    items.forEach(function (li) { ['mouseenter', 'focusin', 'touchstart'].forEach(function (ev) { li.addEventListener(ev, function () { bg(li); }, { once: true, passive: true }); }); });
    w.addEventListener('load', function () { setTimeout(function () { (w.requestIdleCallback || setTimeout)(function () { bg(hd); }); }, 2500); });
    function closeAll(except) {
      items.forEach(function (li) { if (li !== except) { li.classList.remove('open'); var a = li.querySelector('.nl'); if (a) a.setAttribute('aria-expanded', 'false'); } });
    }
    items.forEach(function (li) {
      var a = li.querySelector('.nl');
      li.addEventListener('mouseenter', function () { a.setAttribute('aria-expanded', 'true'); });
      li.addEventListener('mouseleave', function () { if (!li.classList.contains('open')) a.setAttribute('aria-expanded', 'false'); });
      /* touch: first tap opens the panel, second tap follows the link */
      a.addEventListener('pointerup', function (ev) { a._pt = ev.pointerType; });
      a.addEventListener('click', function (ev) {
        if (a._pt === 'touch' && !li.classList.contains('open')) { ev.preventDefault(); closeAll(li); li.classList.add('open'); a.setAttribute('aria-expanded', 'true'); }
      });
      a.addEventListener('keydown', function (ev) {
        if (ev.key === 'ArrowDown' || ev.key === ' ') {
          ev.preventDefault(); closeAll(li); li.classList.add('open'); a.setAttribute('aria-expanded', 'true');
          var f = li.querySelector('.mm a'); if (f) f.focus();
        }
      });
      li.addEventListener('focusout', function (ev) { if (!li.contains(ev.relatedTarget)) { li.classList.remove('open'); a.setAttribute('aria-expanded', 'false'); } });
    });
    d.addEventListener('keydown', function (ev) {
      if (ev.key !== 'Escape') return;
      var open = hd.querySelector('.has-mm.open'); closeAll();
      if (open) open.querySelector('.nl').focus();
      if (!drawer.hidden) toggle(false);
    });
    d.addEventListener('click', function (ev) { if (!hd.contains(ev.target)) closeAll(); });
    var onScroll = function () { hd.classList.toggle('is-scrolled', w.scrollY > 60); };
    w.addEventListener('scroll', onScroll, { passive: true }); onScroll();
    var burger = hd.querySelector('.hd-burger'), drawer = d.getElementById('pss-drawer');
    function toggle(on) {
      if (!drawer) return;
      drawer.hidden = !on; burger.setAttribute('aria-expanded', on ? 'true' : 'false');
      burger.setAttribute('aria-label', on ? 'Close menu' : 'Open menu');
      d.body.classList.toggle('pss-lock', on);
      if (on) { var f = drawer.querySelector('summary, a'); if (f) f.focus(); }
    }
    if (burger && drawer) {
      burger.addEventListener('click', function () { toggle(drawer.hidden); });
      $$('a', drawer).forEach(function (a) { a.addEventListener('click', function () { toggle(false); }); });
      w.addEventListener('resize', function () { if (w.innerWidth >= 1100 && !drawer.hidden) toggle(false); });
    }
  }

  /* ---------- pause animations off-screen */
  function offscreen() {
    if (!IO) return;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { e.target.classList.toggle('is-off', !e.isIntersecting); });
    }, { rootMargin: '80px' });
    $$('.pss .sec, .pss .hero, .pss-ft').forEach(function (s) { if (once(s, 'off')) io.observe(s); });
  }

  /* ---------- home carousel */
  function carousel(root) {
    if (!once(root, 'car')) return;
    var slides = $$('.hs', root), tabs = $$('.hc-tab', root), i = 0, timer = null, DUR = 7000;
    var paused = reduce, hover = false, visible = true;
    root.style.setProperty('--dur', DUR / 1000 + 's');
    if (reduce) root.classList.add('paused');
    function show(n, focus) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) { if (k === i) s.removeAttribute('data-off'); else s.setAttribute('data-off', ''); s.setAttribute('aria-hidden', k === i ? 'false' : 'true'); s.inert = k !== i; });
      tabs.forEach(function (t, k) {
        t.setAttribute('aria-pressed', k === i ? 'true' : 'false');
        var b = t.querySelector('.hc-bar'); if (b) { b.style.animation = 'none'; void b.offsetWidth; b.style.animation = ''; }
      });
      if (focus) tabs[i].focus();
      schedule();
    }
    function schedule() {
      clearTimeout(timer);
      if (paused || hover || !visible) return;
      timer = setTimeout(function () { show(i + 1); }, DUR);
    }
    function setPaused(p) {
      paused = p; root.classList.toggle('paused', p);
      var b = root.querySelector('.hc-pause'); if (b) b.setAttribute('aria-label', p ? 'Play slides' : 'Pause slides');
      schedule();
    }
    tabs.forEach(function (t, k) {
      t.addEventListener('click', function () { show(k); });
      t.addEventListener('keydown', function (ev) {
        if (ev.key === 'ArrowRight') { ev.preventDefault(); show(i + 1, true); }
        if (ev.key === 'ArrowLeft') { ev.preventDefault(); show(i - 1, true); }
      });
    });
    var pv = root.querySelector('.hc-prev'), nx = root.querySelector('.hc-next'), pa = root.querySelector('.hc-pause');
    if (pv) pv.addEventListener('click', function () { show(i - 1); });
    if (nx) nx.addEventListener('click', function () { show(i + 1); });
    if (pa) pa.addEventListener('click', function () { setPaused(!paused); });
    root.addEventListener('mouseenter', function () { hover = true; root.classList.add('paused'); schedule(); });
    root.addEventListener('mouseleave', function () { hover = false; root.classList.toggle('paused', paused); schedule(); });
    root.addEventListener('focusin', function () { hover = true; schedule(); });
    root.addEventListener('focusout', function (ev) { if (!root.contains(ev.relatedTarget)) { hover = false; schedule(); } });
    /* swipe */
    var x0 = null;
    root.addEventListener('touchstart', function (ev) { x0 = ev.touches[0].clientX; }, { passive: true });
    root.addEventListener('touchend', function (ev) {
      if (x0 === null) return; var dx = ev.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) show(dx < 0 ? i + 1 : i - 1);
    });
    if (IO) new IntersectionObserver(function (es) { visible = es[0].isIntersecting; schedule(); }).observe(root);
    d.addEventListener('visibilitychange', function () { visible = !d.hidden; schedule(); });
    show(0);
  }

  /* ---------- tabs */
  function tabsInit(root) {
    if (!once(root, 'tabs')) return;
    var tabs = $$('[role=tab]', root);
    function sel(t, focus) {
      tabs.forEach(function (x) {
        var on = x === t, p = d.getElementById(x.getAttribute('aria-controls'));
        x.setAttribute('aria-selected', on ? 'true' : 'false'); x.tabIndex = on ? 0 : -1;
        if (p) { if (on) { p.removeAttribute('data-off'); p.classList.remove('in'); void p.offsetWidth; p.classList.add('in'); } else p.setAttribute('data-off', ''); }
      });
      if (focus) t.focus();
      var list = t.parentElement;
      if (list.scrollWidth > list.clientWidth + 2) list.scrollTo({ left: Math.max(0, t.offsetLeft - 16), behavior: reduce ? 'auto' : 'smooth' });
      if (root._onsel) root._onsel(tabs.indexOf(t));
    }
    root._sel = function (i) { sel(tabs[(i + tabs.length) % tabs.length]); };
    tabs.forEach(function (t, k) {
      t.addEventListener('click', function (ev) { sel(t); if (ev.isTrusted && root._user) root._user(); });
      t.addEventListener('keydown', function (ev) {
        var n = null;
        if (ev.key === 'ArrowRight' || ev.key === 'ArrowDown') n = tabs[(k + 1) % tabs.length];
        if (ev.key === 'ArrowLeft' || ev.key === 'ArrowUp') n = tabs[(k - 1 + tabs.length) % tabs.length];
        if (ev.key === 'Home') n = tabs[0];
        if (ev.key === 'End') n = tabs[tabs.length - 1];
        if (n) { ev.preventDefault(); sel(n, true); if (root._user) root._user(); }
      });
    });
  }


  /* ---------- journeys: tabs that step through on their own until the visitor takes over */
  function journeyInit(root) {
    if (!once(root, 'jr')) return;
    var tabs = $$('[role=tab]', root), n = tabs.length, cur = 0, timer = null, stopped = false, seen = false, hover = false;
    var every = +root.getAttribute('data-journey') || 7000;
    var cnt = root.querySelector('.jr-count'), bar = root.querySelector('.jr-bar i'), play = root.querySelector('.jr-play');
    function pad(x) { return (x < 10 ? '0' : '') + x; }
    root._onsel = function (i) {
      cur = i;
      tabs.forEach(function (t, k) { t.classList.toggle('done', k < i); });
      if (cnt) cnt.textContent = pad(i + 1) + ' / ' + pad(n);
      if (bar) bar.style.width = (n > 1 ? i / (n - 1) * 100 : 100) + '%';
    };
    function label() {
      root.classList.toggle('paused', stopped);
      if (!play) return;
      play.querySelector('.jr-pt').textContent = stopped ? 'Play' : 'Pause';
      play.setAttribute('aria-label', stopped ? 'Play the journey' : 'Pause the journey');
    }
    function tick() { if (!stopped && seen && !hover && !d.hidden) root._sel(cur + 1); }
    function stop() { stopped = true; label(); }
    root._user = stop;
    var pv = root.querySelector('.jr-prev'), nx = root.querySelector('.jr-next');
    if (pv) pv.addEventListener('click', function () { root._sel(cur - 1); stop(); });
    if (nx) nx.addEventListener('click', function () { root._sel(cur + 1); stop(); });
    if (play) play.addEventListener('click', function () { if (stopped) { stopped = false; root._sel(cur + 1); } else stopped = true; label(); });
    root.addEventListener('mouseenter', function () { hover = true; });
    root.addEventListener('mouseleave', function () { hover = false; });
    root.addEventListener('focusin', function () { hover = true; });
    root.addEventListener('focusout', function () { hover = false; });
    if (IO) new IntersectionObserver(function (es) { seen = es[0].isIntersecting; }, { threshold: 0.3 }).observe(root); else seen = true;
    root._onsel(0);
    if (reduce) stop(); else { label(); timer = setInterval(tick, every); }
  }


  /* ---------- MediCore: create a private 30-day demo on the MediCore server */
  function mcTry() {
    var f = d.getElementById('mcx-try');
    if (!f || !once(f, 'mcx')) return;
    var type = 'pharmacy', API = 'https://medicore.pss.africa', err = d.getElementById('mcx-err');
    $$('.seg button', f).forEach(function (b) {
      b.addEventListener('click', function () {
        type = b.getAttribute('data-t');
        $$('.seg button', f).forEach(function (x) { x.classList.toggle('on', x === b); x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      });
    });
    function show(m) { err.textContent = m; }
    f.addEventListener('submit', function (ev) {
      ev.preventDefault(); show('');
      var agent = ''; try { agent = new URLSearchParams(w.location.search).get('agent') || ''; } catch (x) {}
      var v = { type: type, facility: f.facility.value.trim(), contact: f.contact.value.trim(), phone: f.phone.value.trim(), email: f.email.value.trim(), town: f.town.value.trim(), agent: agent };
      if (!v.facility || !v.contact || !v.phone) return show('Please fill in the facility name, your name and phone.');
      if (!f.agree.checked) return show('Please tick the box so we can contact you about the demo.');
      var btn = f.querySelector('button.go'); btn.disabled = true; btn.textContent = 'Setting up your MediCore…';
      fetch(API + '/api/public/demo', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(v) })
        .then(function (r) { return r.json().then(function (j) { if (!r.ok) throw new Error(j.error || 'Something went wrong.'); return j; }); })
        .then(function (j) {
          d.getElementById('mcx-u').textContent = j.username; d.getElementById('mcx-p').textContent = j.pin;
          d.getElementById('mcx-e').textContent = new Date(j.ends + 'T00:00:00').toLocaleDateString('en-KE', { day: 'numeric', month: 'long' });
          d.getElementById('mcx-fields').hidden = true; d.getElementById('mcx-done').hidden = false;
        })
        .catch(function (x) { show(x.message === 'Failed to fetch' ? 'We could not reach the demo server. Please try again in a minute, or WhatsApp +254 729 455 912.' : x.message); })
        .then(function () { btn.disabled = false; btn.textContent = 'Create my free demo'; });
    });
  }

  /* ---------- click-to-load embeds */
  function loadEmbed(box) {
    var src = box.getAttribute('data-embed'), f = box.querySelector('iframe');
    if (!f) {
      f = d.createElement('iframe');
      f.title = box.getAttribute('data-title') || 'Live demo';
      f.setAttribute('allow', 'fullscreen; clipboard-write; autoplay');
      f.setAttribute('allowfullscreen', '');
      f.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
      f.style.aspectRatio = getComputedStyle(box).getPropertyValue('--r') || '16/10';
      box.classList.add('loading');
      f.addEventListener('load', function () { box.classList.remove('loading'); });
      box.insertBefore(f, box.querySelector('.emb-open'));
    }
    box.classList.add('is-on');
    if (f.getAttribute('src') !== src) { box.classList.add('loading'); f.src = src; }
  }
  function setEmbed(box, src) {
    if (!box) return;
    box.setAttribute('data-embed', src);
    var o = box.querySelector('.emb-open'); if (o) o.href = src;
    if (box.classList.contains('is-on')) loadEmbed(box);
  }
  function embeds() {
    $$('.pss [data-embed]').forEach(function (box) {
      if (!once(box, 'emb')) return;
      $$('iframe', box).forEach(function (f) { f.remove(); });
      box.classList.remove('is-on', 'loading');
      var b = box.querySelector('.emb-go');
      if (b) b.addEventListener('click', function () { loadEmbed(box); });
    });
    $$('.pss .simpick').forEach(function (g) {
      if (!once(g, 'pick')) return;
      var box = g.parentElement.querySelector('[data-embed]');
      $$('button', g).forEach(function (b) {
        b.addEventListener('click', function () {
          $$('button', g).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
          setEmbed(box, b.getAttribute('data-sim')); loadEmbed(box);
        });
      });
    });
    $$('.pss [data-sitepv]').forEach(function (p) {
      if (!once(p, 'spv')) return;
      var s = p.querySelector('[data-sp-sel]'), box = p.querySelector('[data-embed]');
      if (s) s.addEventListener('change', function () { setEmbed(box, s.value); });
    });
  }

  /* ---------- filters (SimLab grid) */
  function filters() {
    $$('.pss [data-filter]').forEach(function (g) {
      if (!once(g, 'flt')) return;
      var list = d.querySelector(g.getAttribute('data-filter')); if (!list) return;
      $$('button', g).forEach(function (b) {
        b.addEventListener('click', function () {
          var f = b.getAttribute('data-f');
          $$('button', g).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
          $$('li', list).forEach(function (li) { li.hidden = !(f === 'all' || li.getAttribute('data-s') === f); });
        });
      });
    });
  }

  /* ---------- POS live demo with business-type switcher */
  function posDemo() {
    var root = d.querySelector('.pss .hero-pos');
    if (!once(root, 'pos')) return;
    var page = root.closest('.pss-page') || d;
    var BASE = root.getAttribute('data-pos') || '/pos/';
    var ref = '';
    try { ref = (new URLSearchParams(location.search).get('ref') || '').trim().toUpperCase(); } catch (e) {}
    if (!/^AG-[A-Z0-9]{3,8}$/.test(ref)) ref = '';
    var type = 'duka';
    function posUrl(t) {
      var p = t ? ['demo=1', 'type=' + encodeURIComponent(t)] : ['trial=1'];
      if (ref) p.push('ref=' + encodeURIComponent(ref));
      return BASE + '?' + p.join('&');
    }
    function links() {
      $$('[data-link]', page).forEach(function (a) { var k = a.getAttribute('data-link'); a.href = k === 'trial' ? posUrl('') : posUrl(type); });
    }
    var scr = d.getElementById('pp-scr'), frame = null;
    function fit() {
      if (!scr || !frame) return;
      var wd = scr.clientWidth;
      if (wd >= 600) { var k = wd / 1366; frame.style.width = '1366px'; frame.style.height = '768px'; frame.style.transform = 'scale(' + k + ')'; }
      else { frame.style.width = wd + 'px'; frame.style.height = scr.clientHeight + 'px'; frame.style.transform = 'none'; }
    }
    function load() {
      if (!scr) return;
      scr.classList.add('loading');
      if (!frame) {
        frame = d.createElement('iframe'); frame.title = 'Pentarch POS live demo'; frame.setAttribute('allow', 'clipboard-write');
        frame.addEventListener('load', function () { scr.classList.remove('loading'); });
        var go = d.getElementById('pp-go'); if (go) go.remove();
        var pst = scr.querySelector('.pst'); if (pst) pst.remove();
        scr.appendChild(frame);
      }
      fit(); frame.src = posUrl(type);
    }
    function setType(t, start) {
      type = t;
      $$('.sw button', page).forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-type') === t ? 'true' : 'false'); });
      links();
      if (frame || start) load();
    }
    $$('.sw button', page).forEach(function (b) { b.addEventListener('click', function () { setType(b.getAttribute('data-type'), true); }); });
    var go = d.getElementById('pp-go'); if (go) go.addEventListener('click', load);
    function toDemo() { var el = d.getElementById('live-demo'); if (el) el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); }
    $$('[data-try]', page).forEach(function (b) {
      b.addEventListener('click', function () {
        var t = b.getAttribute('data-try'); toDemo(); setType(t, true);
        var s = page.querySelector('.sw button[data-type="' + t + '"]'); if (s) s.scrollIntoView({ block: 'nearest', inline: 'center' });
      });
    });
    $$('[data-act=start]', page).forEach(function (a) { a.addEventListener('click', function (ev) { ev.preventDefault(); toDemo(); if (!frame) load(); }); });
    if (w.ResizeObserver && scr) new ResizeObserver(fit).observe(scr); else w.addEventListener('resize', fit);
    links();
  }

  /* ---------- Live Edit "try it" box */
  function leTry() {
    $$('.pss [data-le-try]').forEach(function (box) {
      if (!once(box, 'le')) return;
      var page = box.querySelector('.lt-page'), revs = box.querySelector('[data-lt-revs]'), st = box.querySelector('[data-lt-status]');
      var list = box.querySelector('[data-lt-list]'), hist = [], n = 0, imgs = ['', 'i2', 'i3', 'i4'];
      if (revs) revs.innerHTML = '';
      function status(t) { if (st) st.textContent = t; }
      function snap() { var c = list.cloneNode(true); $$('.lt-tools', c).forEach(function (x) { x.remove(); }); return { h: page.querySelector('h3').innerHTML, p: page.querySelector('p').innerHTML, l: c.innerHTML }; }
      function tools(card) {
        $$('.lt-tools', card).forEach(function (x) { x.remove(); });
        var t = d.createElement('span'); t.className = 'lt-tools';
        t.innerHTML = '<button type="button" data-a="dup" aria-label="Duplicate card" title="Duplicate">+</button><button type="button" data-a="del" aria-label="Delete card" title="Delete">&times;</button>';
        card.appendChild(t);
      }
      function wire() { $$('.lt-card', list).forEach(tools); }
      wire();
      hist.push(snap());
      box.addEventListener('click', function (ev) {
        var ed = ev.target.closest('[data-lt-edit]');
        if (ed && !ed.isContentEditable) { ed.contentEditable = 'true'; ed.spellcheck = false; ed.focus(); }
        var im = ev.target.closest('[data-lt-img]');
        if (im) { var c = imgs.indexOf((im.className.match(/i\d/) || [''])[0]); im.classList.remove('i2', 'i3', 'i4'); var nx = imgs[(c + 1) % imgs.length]; if (nx) im.classList.add(nx); status('Picture changed, not saved'); }
        var b = ev.target.closest('.lt-tools button');
        if (b) {
          var card = b.closest('.lt-card');
          if (b.getAttribute('data-a') === 'dup') { var cp = card.cloneNode(true); $$('[contenteditable]', cp).forEach(function (x) { x.removeAttribute('contenteditable'); }); card.after(cp); tools(cp); status('Card duplicated, not saved'); }
          else if ($$('.lt-card', list).length > 1) { card.remove(); status('Card deleted, not saved'); }
        }
      });
      box.addEventListener('input', function () { status('Edited, not saved'); });
      box.addEventListener('focusout', function (ev) { var ed = ev.target.closest && ev.target.closest('[data-lt-edit]'); if (ed) ed.removeAttribute('contenteditable'); });
      var save = box.querySelector('[data-lt-save]'), undo = box.querySelector('[data-lt-undo]');
      save.addEventListener('click', function () {
        hist.push(snap()); n++;
        var li = d.createElement('li'), t = new Date();
        li.textContent = 'Revision ' + n + ' saved at ' + ('0' + t.getHours()).slice(-2) + ':' + ('0' + t.getMinutes()).slice(-2);
        revs.prepend(li); status('Saved, revision ' + n);
      });
      undo.addEventListener('click', function () {
        var cur = JSON.stringify(snap()), last = hist[hist.length - 1];
        if (JSON.stringify(last) === cur && hist.length > 1) { hist.pop(); last = hist[hist.length - 1]; if (revs.firstChild) revs.firstChild.remove(); n = Math.max(0, n - 1); }
        page.querySelector('h3').innerHTML = last.h; page.querySelector('p').innerHTML = last.p; list.innerHTML = last.l; wire();
        status(n ? 'Restored revision ' + n : 'Restored the original');
      });
    });
  }

  /* ---------- node network canvas (hero backgrounds) */
  function net(cv) {
    if (!once(cv, 'net') || !cv.getContext) return;
    var ctx = cv.getContext('2d'), dpr = Math.min(w.devicePixelRatio || 1, 1.5), W = 0, H = 0, pts = [], raf = null, on = true;
    function size() {
      var r = cv.getBoundingClientRect(); W = r.width; H = r.height;
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.min(64, Math.round(W * H / 22000));
      while (pts.length < n) pts.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .25, vy: (Math.random() - .5) * .25, h: Math.random() < .12 });
      pts.length = n;
    }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      var L = 150;
      for (var a = 0; a < pts.length; a++) {
        var p = pts[a];
        for (var b = a + 1; b < pts.length; b++) {
          var q = pts[b], dx = p.x - q.x, dy = p.y - q.y, dd = dx * dx + dy * dy;
          if (dd < L * L) { ctx.strokeStyle = 'rgba(127,227,223,' + (0.16 * (1 - Math.sqrt(dd) / L)).toFixed(3) + ')'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke(); }
        }
      }
      pts.forEach(function (p) { ctx.fillStyle = p.h ? 'rgba(246,178,44,.9)' : 'rgba(127,227,223,.55)'; ctx.beginPath(); ctx.arc(p.x, p.y, p.h ? 2.4 : 1.6, 0, 6.283); ctx.fill(); });
    }
    function step() {
      pts.forEach(function (p) { p.x += p.vx; p.y += p.vy; if (p.x < 0 || p.x > W) p.vx *= -1; if (p.y < 0 || p.y > H) p.vy *= -1; });
      draw(); raf = on ? requestAnimationFrame(step) : null;
    }
    size(); draw();
    w.addEventListener('resize', function () { size(); draw(); });
    if (reduce) return;
    function run(v) { on = v && !d.hidden; if (on && !raf) raf = requestAnimationFrame(step); }
    if (IO) new IntersectionObserver(function (es) { run(es[0].isIntersecting); }).observe(cv); else run(true);
    d.addEventListener('visibilitychange', function () { run(!d.hidden); });
  }

  /* ---------- viewer: open client sites and tools inside this site */
  var VIEW_HOSTS = /(^|\.)(laqimautoworld\.com|glamourvinecollege\.com|pentarchtraininginstitute\.co\.ke|zingirapesa\.com|lfesolutions\.co\.ke|rarcconsulting\.com|pentarchcommunications\.com|storymaps\.arcgis\.com)$|^(pos|medicore|complyscope)\.(pss\.africa|pentarchsystemssolutions\.co\.ke)$/i;
  var VIEW_SKIP = /\/(signup|login|account|portal\/?$|agents|try|wp-admin|wp-login)/i;
  var vw = null;
  function viewerEl() {
    if (vw) return vw;
    vw = d.createElement('div');
    vw.className = 'pss-vw';
    vw.setAttribute('role', 'dialog'); vw.setAttribute('aria-modal', 'true'); vw.setAttribute('aria-label', 'Site viewer'); vw.hidden = true;
    vw.innerHTML = '<div class="vw-box"><div class="vw-bar"><span class="vw-dots" aria-hidden="true"><i></i><i></i><i></i></span><b class="vw-t"></b><span class="vw-u"></span>' +
      '<a class="vw-open" target="_blank" rel="noopener">Open in a new tab</a><button type="button" class="vw-x" aria-label="Close">&times;</button></div>' +
      '<div class="vw-body"><div class="vw-load" aria-hidden="true"></div><iframe title="" loading="eager" allow="fullscreen; clipboard-write" referrerpolicy="strict-origin-when-cross-origin"></iframe></div></div>';
    d.body.appendChild(vw);
    function close() { vw.hidden = true; vw.querySelector('iframe').src = 'about:blank'; d.documentElement.classList.remove('vw-on'); if (vw._from) vw._from.focus(); }
    vw.querySelector('.vw-x').addEventListener('click', close);
    vw.addEventListener('click', function (ev) { if (ev.target === vw) close(); });
    d.addEventListener('keydown', function (ev) { if (ev.key === 'Escape' && !vw.hidden) close(); });
    vw.querySelector('iframe').addEventListener('load', function () { vw.classList.add('vw-ready'); });
    return vw;
  }
  function viewer() {
    if (!once(d.body, 'vw')) return;
    d.addEventListener('click', function (ev) {
      if (ev.defaultPrevented || ev.button !== 0 || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
      var a = ev.target.closest && ev.target.closest('a[href]');
      if (!a || !a.closest('.pss') || a.closest('[data-pss-header], .ft, .pss-vw, .emb, [data-noview]')) return;
      var u; try { u = new URL(a.href, location.href); } catch (e) { return; }
      if (!/^https?:$/.test(u.protocol) || u.host === location.host || !VIEW_HOSTS.test(u.hostname) || VIEW_SKIP.test(u.pathname)) return;
      ev.preventDefault();
      var v = viewerEl(), fr = v.querySelector('iframe');
      var t = (a.getAttribute('aria-label') || a.textContent || '').replace(/\s+/g, ' ').trim();
      if (!t || t.length > 60 || /^(visit|open|see|explore|try|play|enter|load)/i.test(t)) { var box = a.closest('article, li, .case, section'); var hh = box && box.querySelector('h2, h3'); t = hh ? hh.textContent.replace(/\s+/g, ' ').trim() : u.hostname.replace(/^www\./, ''); }
      v.querySelector('.vw-t').textContent = t;
      v.querySelector('.vw-u').textContent = u.hostname.replace(/^www\./, '') + (u.pathname.length > 1 ? u.pathname : '');
      v.querySelector('.vw-open').href = u.href;
      fr.title = t; v.classList.remove('vw-ready'); fr.src = u.href;
      v._from = a; v.hidden = false; d.documentElement.classList.add('vw-on');
      v.querySelector('.vw-x').focus();
    });
  }

  /* ---------- back to top */
  function toTop() {
    if (!once(d.body, 'top')) return;
    var b = d.createElement('button');
    b.type = 'button'; b.className = 'pss-top'; b.setAttribute('aria-label', 'Back to top');
    b.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m18 15-6-6-6 6"/></svg>';
    d.body.appendChild(b);
    b.addEventListener('click', function () { w.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });
    var tick = false;
    function upd() { tick = false; b.classList.toggle('on', w.scrollY > 700); }
    w.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(upd); } }, { passive: true });
    upd();
  }

  function init() {
    var mv = d.querySelector('.pss [data-redirect]');
    if (mv && !d.body.classList.contains('logged-in')) { w.location.replace(mv.getAttribute('data-redirect')); return; }
    header(); offscreen(); embeds(); viewer(); toTop(); filters(); posDemo(); leTry(); mcTry();
    $$('.pss [data-carousel]').forEach(carousel);
    $$('.pss [data-tabs]').forEach(tabsInit);
    $$('.pss [data-journey]').forEach(journeyInit);
    $$('.pss [data-net]').forEach(net);
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', init); else init();
})();
