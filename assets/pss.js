(function () {
	window.PC_OK = true;
	var d = document, hdr = d.getElementById('pc-hdr');
	var y = d.getElementById('pc-yr'); if (y) y.textContent = new Date().getFullYear();
	var tt = d.getElementById('pc-totop');
	function onS() { var s = window.scrollY > 20; if (hdr) hdr.classList.toggle('sc', s); if (tt) tt.classList.toggle('show', window.scrollY > 900); }
	window.addEventListener('scroll', onS, { passive: true }); onS();
	if (tt) tt.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

	/* current menu item */
	var p = location.pathname.replace(/\/+$/, '/') || '/';
	d.querySelectorAll('#pc-nav>li[data-p]').forEach(function (li) {
		li.getAttribute('data-p').split('|').forEach(function (q) { if (q === p || (q !== '/' && p.indexOf(q) === 0)) li.classList.add('cur'); });
	});

	/* mega menus */
	var dds = d.querySelectorAll('#pc-nav>li.dd'), tm;
	function closeAll(ex) { dds.forEach(function (li) { if (li !== ex) { li.classList.remove('on'); li.querySelector('button').setAttribute('aria-expanded', 'false'); } }); if (!ex && hdr) hdr.classList.remove('open'); }
	function open(li) { closeAll(li); li.classList.add('on'); li.querySelector('button').setAttribute('aria-expanded', 'true'); if (hdr) hdr.classList.add('open'); }
	dds.forEach(function (li) {
		li.addEventListener('mouseenter', function () { if (window.matchMedia('(hover:hover)').matches) { clearTimeout(tm); open(li); } });
		li.addEventListener('mouseleave', function () { if (window.matchMedia('(hover:hover)').matches) { tm = setTimeout(function () { closeAll(); }, 160); } });
		li.querySelector('button').addEventListener('click', function () {
			var q = li.getAttribute('data-go');
			if (q && window.matchMedia('(hover:hover)').matches) { location.href = q; return; }
			if (li.classList.contains('on')) closeAll(); else open(li);
		});
		li.querySelector('button').addEventListener('keydown', function (e) { if (e.key === 'ArrowDown') { e.preventDefault(); open(li); var a = li.querySelector('.pc-mega a'); if (a) a.focus(); } });
	});
	d.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeAll(); closeDr(); } });
	d.addEventListener('click', function (e) { if (hdr && !hdr.contains(e.target)) closeAll(); });

	/* mobile drawer */
	var dr = d.getElementById('pc-drawer'), bg = d.getElementById('pc-burger');
	function closeDr() { if (!dr) return; dr.classList.remove('open'); dr.setAttribute('aria-hidden', 'true'); if (bg) bg.setAttribute('aria-expanded', 'false'); d.documentElement.style.overflow = ''; }
	if (bg && dr) {
		bg.addEventListener('click', function () { dr.classList.add('open'); dr.setAttribute('aria-hidden', 'false'); bg.setAttribute('aria-expanded', 'true'); d.documentElement.style.overflow = 'hidden'; });
		dr.querySelector('.x').addEventListener('click', closeDr);
		dr.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeDr); });
	}

	/* reveal + counters */
	var els = d.querySelectorAll('.pc .rv,.pc .stg');
	if ('IntersectionObserver' in window) {
		var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0, rootMargin: '0px 0px -60px 0px' });
		els.forEach(function (el) { io.observe(el); });
	} else els.forEach(function (el) { el.classList.add('in'); });
	var reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
	function count(el) {
		var t = +el.getAttribute('data-n'), s = null; if (reduce) { el.textContent = t; return; }
		function st(ts) { if (!s) s = ts; var k = Math.min((ts - s) / 1600, 1); el.textContent = Math.round(t * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(st); }
		requestAnimationFrame(st);
	}
	var cs = d.querySelectorAll('.pc [data-n]');
	if ('IntersectionObserver' in window) {
		var co = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { count(e.target); co.unobserve(e.target); } }); }, { threshold: .5 });
		cs.forEach(function (c) { co.observe(c); });
	} else cs.forEach(function (c) { c.textContent = c.getAttribute('data-n'); });
	d.querySelectorAll('.pc .mq-t').forEach(function (t) { t.innerHTML += t.innerHTML; });

	/* smooth in-page links */
	d.addEventListener('click', function (e) {
		var a = e.target.closest && e.target.closest('a[href*="#"]'); if (!a) return;
		var u = new URL(a.href, location.href); if (u.pathname !== location.pathname || !u.hash) return;
		var t = d.getElementById(u.hash.slice(1)); if (!t) return;
		e.preventDefault(); var off = (hdr ? hdr.offsetHeight : 0) + 16;
		window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - off, behavior: 'smooth' }); history.replaceState(null, '', u.hash);
	});

	/* home hero carousel */
	d.querySelectorAll('.pc .hc').forEach(function (hc) {
		var sl = hc.querySelectorAll('.sl'), tb = hc.querySelectorAll('.tabs button'), i = 0, timer, dur = 7000;
		hc.style.setProperty('--dur', dur / 1000 + 's');
		function go(n) {
			i = (n + sl.length) % sl.length;
			sl.forEach(function (s, k) { s.classList.toggle('on', k === i); s.setAttribute('aria-hidden', k === i ? 'false' : 'true'); });
			tb.forEach(function (b, k) { b.classList.toggle('on', k === i); var bar = b.querySelector('i'); if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; } });
			hc.setAttribute('data-i', i);
			clearTimeout(timer); if (!reduce) timer = setTimeout(function () { if (!hc.classList.contains('paused')) go(i + 1); else wait(); }, dur);
		}
		function wait() { clearTimeout(timer); timer = setTimeout(function () { if (!hc.classList.contains('paused')) go(i + 1); else wait(); }, 800); }
		tb.forEach(function (b, k) { b.addEventListener('click', function () { go(k); }); });
		var pv = hc.querySelector('.arr .pv'), nx = hc.querySelector('.arr .nx');
		if (pv) pv.addEventListener('click', function () { go(i - 1); });
		if (nx) nx.addEventListener('click', function () { go(i + 1); });
		hc.addEventListener('mouseenter', function () { hc.classList.add('paused'); });
		hc.addEventListener('mouseleave', function () { hc.classList.remove('paused'); });
		var x0 = null;
		hc.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
		hc.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) go(i + (dx < 0 ? 1 : -1)); x0 = null; });
		go(0);
	});

	/* sector tabs */
	d.querySelectorAll('.pc .sx').forEach(function (sx) {
		var bs = sx.querySelectorAll('.sx-nav button'), ps = sx.querySelectorAll('.sx-pane');
		bs.forEach(function (b, k) { b.addEventListener('click', function () { bs.forEach(function (x, j) { x.classList.toggle('on', j === k); x.setAttribute('aria-selected', j === k); }); ps.forEach(function (x, j) { x.classList.toggle('on', j === k); }); }); });
	});

	/* sub-nav highlight */
	var sl2 = d.querySelectorAll('.pc .ssn a'), secs = [];
	sl2.forEach(function (a) { var t = d.getElementById((a.getAttribute('href') || '').replace('#', '')); if (t) secs.push([a, t]); });
	if (secs.length) {
		window.addEventListener('scroll', function () {
			var cur = null; secs.forEach(function (s) { if (s[1].getBoundingClientRect().top < 220) cur = s[0]; });
			sl2.forEach(function (a) { a.classList.toggle('on', a === cur); });
		}, { passive: true });
	}

	/* MediCore free demo (creates a private demo on the MediCore server) */
	var f = d.getElementById('mcx-try');
	if (f) {
		var type = 'pharmacy', API = 'https://medicore.pentarchcommunications.com';
		f.querySelectorAll('.seg button').forEach(function (b) { b.addEventListener('click', function () { type = b.getAttribute('data-t'); f.querySelectorAll('.seg button').forEach(function (x) { x.classList.toggle('on', x === b); }); }); });
		var err = d.getElementById('mcx-err');
		function show(m) { err.textContent = m; err.style.display = 'block'; }
		f.addEventListener('submit', function (e) {
			e.preventDefault(); err.style.display = 'none';
			var v = { type: type, facility: f.facility.value.trim(), contact: f.contact.value.trim(), phone: f.phone.value.trim(), email: f.email.value.trim(), town: f.town.value.trim(), agent: new URLSearchParams(location.search).get('agent') || '' };
			if (!v.facility || !v.contact || !v.phone) return show('Please fill in the facility name, your name and phone.');
			if (!f.agree.checked) return show('Please tick the box so we can contact you about the demo.');
			var btn = f.querySelector('.go'); btn.disabled = true; btn.textContent = 'Setting up your MediCore…';
			fetch(API + '/api/public/demo', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(v) })
				.then(function (r) { return r.json().then(function (j) { if (!r.ok) throw new Error(j.error || 'Something went wrong.'); return j; }); })
				.then(function (j) {
					d.getElementById('mcx-u').textContent = j.username; d.getElementById('mcx-p').textContent = j.pin;
					d.getElementById('mcx-e').textContent = new Date(j.ends + 'T00:00:00').toLocaleDateString('en-KE', { day: 'numeric', month: 'long' });
					d.getElementById('mcx-fields').style.display = 'none'; d.getElementById('mcx-done').style.display = 'grid';
				})
				.catch(function (x) { show(x.message === 'Failed to fetch' ? 'We could not reach the demo server. Please try again in a minute, or WhatsApp +254 729 455 912.' : x.message); })
				.then(function () { btn.disabled = false; btn.textContent = 'Create my free demo'; });
		});
	}
})();

/* Real-screen tours */
document.querySelectorAll('.pc .tour').forEach(function (t) {
	var bs = t.querySelectorAll('.tour-nav button'), ps = t.querySelectorAll('.tour-pane');
	bs.forEach(function (b, i) {
		b.addEventListener('click', function () {
			bs.forEach(function (x, j) { x.classList.toggle('on', j === i); x.setAttribute('aria-selected', j === i ? 'true' : 'false'); });
			ps.forEach(function (p, j) { p.classList.toggle('on', j === i); p.hidden = j !== i; });
			if (window.innerWidth <= 1000) { b.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' }); }
		});
	});
});
/* Journey stepper */
(function(){
 document.querySelectorAll('.pc .jr').forEach(function(jr){
  var btns=[].slice.call(jr.querySelectorAll('.jr-steps button')),panes=[].slice.call(jr.querySelectorAll('.jr-pane')),bar=jr.querySelector('.jr-bar i'),cnt=jr.querySelector('.jr-count'),play=jr.querySelector('.jr-play'),n=btns.length,cur=0,timer=null,auto=+jr.dataset.auto||0,stopped=false,seen=false;
  function pad(x){return (x<10?'0':'')+x}
  function go(i,user){
   cur=(i+n)%n;
   btns.forEach(function(b,k){b.classList.toggle('on',k===cur);b.classList.toggle('done',k<cur);b.setAttribute('aria-selected',k===cur?'true':'false')});
   panes.forEach(function(p,k){p.classList.toggle('on',k===cur);p.hidden=k!==cur});
   if(bar)bar.style.width=(n>1?cur/(n-1)*100:100)+'%';
   if(cnt)cnt.textContent=pad(cur+1)+' / '+pad(n);
   if(user&&window.innerWidth<=1000){btns[cur].scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'})}
   if(user)stop();
  }
  function tick(){if(!stopped&&seen&&!document.hidden)go(cur+1)}
  function start(){if(auto&&!timer)timer=setInterval(tick,auto)}
  function stop(){stopped=true;clearInterval(timer);timer=null;if(play){play.querySelector('span').textContent='Play';play.setAttribute('aria-label','Play the journey')}}
  btns.forEach(function(b,k){b.addEventListener('click',function(){go(k,true)})});
  var pv=jr.querySelector('.jr-prev'),nx=jr.querySelector('.jr-next');
  if(pv)pv.addEventListener('click',function(){go(cur-1,true)});
  if(nx)nx.addEventListener('click',function(){go(cur+1,true)});
  if(play)play.addEventListener('click',function(){if(stopped){stopped=false;play.querySelector('span').textContent='Pause';play.setAttribute('aria-label','Pause the journey');go(cur+1);start()}else stop()});
  jr.addEventListener('mouseenter',function(){clearInterval(timer);timer=null});
  jr.addEventListener('mouseleave',function(){if(!stopped)start()});
  if('IntersectionObserver' in window){new IntersectionObserver(function(e){seen=e[0].isIntersecting},{threshold:.35}).observe(jr)}else seen=true;
  go(0);
  if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches){stop()}else start();
 });
})();
