"""Product UI mock-ups built in HTML and CSS (illustrations of real screens, sample data only)."""
from lib import ic, circuit


def browser(url, inner, cls=""):
    return (f'<div class="bw {cls}"><div class="bw-bar" aria-hidden="true"><i></i><i></i><i></i><span class="bw-url">{url}</span></div>'
            f'<div class="bw-body">{inner}</div></div>')


def terminal(title, lines, cls=""):
    body = "".join(f'<p class="tl {c}">{t}</p>' for c, t in lines)
    return (f'<div class="term {cls}"><div class="term-bar" aria-hidden="true"><i></i><i></i><i></i><span>{title}</span></div>'
            f'<div class="term-body">{body}</div></div>')


def pos_till():
    items = [("Maize flour 2 kg", "210", "c1"), ("Sugar 1 kg", "160", "c2"), ("Cooking oil 1 L", "395", "c3"),
             ("Bread 400 g", "65", "c4"), ("Fresh milk 500 ml", "65", "c5"), ("Bar soap 800 g", "230", "c6")]
    tiles = "".join(f'<div class="mt {c}"><i></i><b>{n}</b><span>{p}</span></div>' for n, p, c in items)
    return f'''<div class="mk mk-pos" aria-hidden="true">
<div class="mk-side"><i class="on"></i><i></i><i></i><i></i><i></i></div>
<div class="mk-main"><div class="mk-search">{ic("search")}<span>Search or scan a barcode</span></div>
<div class="mk-chips"><span class="on">All</span><span>Food</span><span>Drinks</span><span>Household</span></div>
<div class="mk-tiles">{tiles}</div></div>
<div class="mk-cart"><p class="mk-h">Current sale</p>
<div class="mk-line"><span>2 × Maize flour 2 kg</span><b>420</b></div><div class="mk-line"><span>1 × Cooking oil 1 L</span><b>395</b></div><div class="mk-line"><span>3 × Fresh milk 500 ml</span><b>195</b></div>
<div class="mk-tot"><span>Total</span><b>KES 1,010</b></div><div class="mk-pay"><span>Cash</span><span class="on">M-Pesa</span><span>Credit</span></div>
<div class="mk-code"><span>TKB4R7QX2M</span><em>{ic("check")}Checked</em></div></div></div>'''


def medicore_queue():
    rows = [("Amina W.", "Triage", "Vitals taken", "s-ok", "08:42"), ("John K.", "Consultation", "Waiting 6 min", "s-w", "08:51"),
            ("Grace N.", "Lab", "Malaria RDT, result due", "s-lab", "09:03"), ("Peter O.", "Pharmacy", "Prescription ready", "s-ok", "09:10"),
            ("Mary A.", "Cashier", "SHA claim, M-Pesa top-up", "s-c", "09:14")]
    r = "".join(f'<div class="q-row"><span class="q-av">{n[0]}</span><span class="q-n">{n}</span><span class="q-st">{s}</span>'
                f'<span class="q-chip {c}">{d}</span><span class="q-t">{t}</span></div>' for n, s, d, c, t in rows)
    return f'''<div class="mk mk-mc" aria-hidden="true"><div class="mc-top"><span class="mc-dot"></span><b>Patient queue</b><span class="mc-lan">{ic("offline")}Local network · 4 devices</span></div>
<div class="mc-kpis"><div><small>Waiting</small><b>7</b></div><div><small>In lab</small><b>3</b></div><div><small>Admitted</small><b>12</b></div><div><small>Beds free</small><b>9</b></div></div>
<div class="q-list">{r}</div></div>'''


def ecg():
    d = "M0 60 L120 60 L135 60 L145 40 L155 60 L170 60 L178 70 L188 10 L198 100 L206 60 L240 60 L255 48 L270 60 L400 60"
    return (f'<svg class="ecg" viewBox="0 0 400 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
            f'<path class="ecg-b" d="{d}"/><path class="ecg-p" d="{d}"/></svg>')


def portal_cert():
    qr = "".join(f'<i class="{"on" if (x * 7 + y * 3 + x * y) % 3 == 0 or x in (0, 6) and y in (0, 1, 5, 6) or y in (0, 6) and x in (0, 1, 5, 6) else ""}"></i>'
                 for y in range(7) for x in range(7))
    return f'''<div class="mk mk-cert" aria-hidden="true"><div class="cert">
<p class="cert-k">Certificate of completion</p><p class="cert-n">Diploma in Cosmetology</p><p class="cert-s">Awarded to a graduate of the college</p>
<div class="cert-f"><div class="cert-qr">{qr}</div><div><small>Certificate no.</small><b>GV-2026-0418</b><small>Scan to verify</small></div></div></div>
<div class="verify"><span class="v-ic">{ic("shield")}</span><div><b>This certificate is genuine</b><small>Issued by the college and recorded in the Portal</small></div></div></div>'''


def journey():
    st = [("Apply", "users"), ("Activate", "check"), ("Fees", "cash"), ("Learn", "book"), ("Assess", "pen"), ("Graduate", "star"), ("Verify", "shield"), ("Alumni", "handshake")]
    return '<ol class="journey">' + "".join(f'<li><span class="j-n">{ic(i)}</span><span class="j-l">{t}</span></li>' for t, i in st) + "</ol>"


def salon_cal():
    staff = ["Wanjiku", "Achieng", "Mumbi", "Halima"]
    blocks = [(0, 1, 2, "Braids", "b1"), (0, 4, 1, "Wash and set", "b2"), (1, 0, 3, "Bridal party", "b3"), (1, 4, 2, "Manicure", "b4"),
              (2, 0, 1, "Walk-in", "b5"), (2, 2, 2, "Bridal party", "b3"), (3, 1, 1, "Lashes", "b2"), (3, 3, 2, "Make-up", "b1")]
    cols = "".join(f'<span class="sc-h">{s}</span>' for s in staff)
    b = "".join(f'<div class="sc-b {c}" style="--c:{col + 2};--r:{row + 2};--s:{span}"><b>{t}</b></div>' for col, row, span, t, c in blocks)
    times = "".join(f'<span class="sc-t" style="--r:{i + 2}">{h}</span>' for i, h in enumerate(["9:00", "10:00", "11:00", "12:00", "13:00", "14:00"]))
    return f'<div class="mk mk-salon" aria-hidden="true"><div class="sc-top"><b>Saturday bookings</b><span>4 stylists · 2 walk-ins waiting</span></div><div class="sc-grid"><span></span>{cols}{times}{b}</div></div>'


def seats_board():
    rows = [("Graphic Design", "Next intake", "8 of 12"), ("Web Design and Coding", "Next intake", "5 of 12"),
            ("Data Analysis", "Next intake", "11 of 15"), ("Public Relations and Corporate Communications", "Next intake", "12 of 15")]
    r = "".join(f'<div class="sb-r"><span class="sb-c">{c}</span><span class="sb-d">{d}</span><span class="sb-s">{s}</span></div>' for c, d, s in rows)
    return f'<div class="mk mk-board" aria-hidden="true"><div class="sb-h"><span>Course</span><span>Class</span><span>Seats left</span></div>{r}<p class="sb-f">Sample data · seats update as people register</p></div>'


def ngo_flow():
    n = [("Sponsor", "handshake"), ("Donation", "cash"), ("Student", "school"), ("Fees paid", "check"), ("Letters", "mail"), ("Impact", "chart")]
    return '<div class="flow" aria-hidden="true">' + "".join(f'<div class="fl-n"><span>{ic(i)}</span><b>{t}</b></div>' for t, i in n) + "</div>"


def qr_art(seed=5, n=21):
    import random
    r = random.Random(seed)
    cells = []
    for y in range(n):
        for x in range(n):
            finder = any(x in range(a, a + 7) and y in range(b, b + 7) for a, b in ((0, 0), (n - 7, 0), (0, n - 7)))
            if finder:
                fx = min(x % (n - 7) if x >= n - 7 else x, 6); fy = min(y % (n - 7) if y >= n - 7 else y, 6)
                on = fx in (0, 6) or fy in (0, 6) or (2 <= fx <= 4 and 2 <= fy <= 4)
            else:
                on = r.random() < .45
            if on:
                cells.append(f'<rect x="{x}" y="{y}" width="1" height="1"/>')
    return f'<svg class="qr" viewBox="-1 -1 {n + 2} {n + 2}" aria-hidden="true" focusable="false"><rect x="-1" y="-1" width="{n + 2}" height="{n + 2}" class="qr-bg"/>{"".join(cells)}</svg>'


def qr_dash():
    bars = "".join(f'<i style="--h:{h}%"></i>' for h in [30, 42, 38, 55, 61, 48, 70, 82, 76, 64, 88, 72, 58, 66])
    return f'''<div class="mk mk-qr" aria-hidden="true"><div class="qd-top"><b>Campaign: market poster</b><span>Last 14 days</span></div>
<div class="qd-k"><div><small>Scans</small><b>2,418</b></div><div><small>Unique devices</small><b>1,932</b></div><div><small>Countries</small><b>6</b></div></div>
<div class="qd-chart">{bars}</div><div class="qd-split"><div><small>Android</small><span style="--w:68%"></span></div><div><small>iPhone</small><span style="--w:27%"></span></div><div><small>Other</small><span style="--w:5%"></span></div></div>
<div class="qd-ex"><span>CSV</span><span>Excel</span><span>PDF</span></div></div>'''


def liveedit_mock():
    return f'''<div class="le-mock" aria-hidden="true">
<div class="le-bar"><span class="le-badge">{ic("pen")}Live Edit</span><span class="le-saved">Saved · revision 14</span></div>
<div class="le-page"><div class="le-h"><span class="le-sel">Storage designed around the way you live<i class="le-caret"></i></span></div>
<p class="le-p">Kitchens, wardrobes and vanities, made in our own workshop.</p>
<div class="le-row"><div class="le-card"><span class="le-img"></span><b>Kitchens</b></div><div class="le-card le-hov"><span class="le-img i2"></span><b>Wardrobes</b><span class="le-tools"><i>{ic("layers")}</i><i>{ic("x")}</i></span></div><div class="le-card"><span class="le-img i3"></span><b>Vanities</b></div></div>
<span class="le-link">{ic("web")}/design-your-storage/</span></div>
<span class="le-cursor"></span></div>'''


def sim_mock():
    import math
    teeth = lambda cx, cy, r, n, cls: f'<g class="{cls}" style="transform-origin:{cx}px {cy}px">' + "".join(
        f'<rect x="{cx - 5}" y="{cy - r - 9}" width="10" height="14" rx="2" transform="rotate({i * 360 / n} {cx} {cy})"/>' for i in range(n)) + f'<circle cx="{cx}" cy="{cy}" r="{r}"/><circle class="hub" cx="{cx}" cy="{cy}" r="{r * .3}"/></g>'
    return (f'<div class="mk mk-sim" aria-hidden="true"><svg viewBox="0 0 400 260" focusable="false">'
            f'<g class="grid">' + "".join(f'<path d="M{x} 0V260"/>' for x in range(0, 401, 20)) + "".join(f'<path d="M0 {y}H400"/>' for y in range(0, 261, 20)) + '</g>'
            + teeth(140, 130, 62, 16, "g1") + teeth(244, 130, 31, 8, "g2") +
            '</svg><div class="sim-read"><span>Ratio 2 : 1</span><span>Driver 60 rpm</span><span>Driven 120 rpm</span></div></div>')


def engine_mock():
    pist = "".join(f'<g class="pi" style="--i:{i}"><rect x="{40 + i * 70}" y="40" width="44" height="40" rx="4"/><path d="M{62 + i * 70} 80 L{62 + i * 70} 150"/></g>' for i in range(4))
    return f'<div class="mk mk-eng" aria-hidden="true"><svg viewBox="0 0 340 200" focusable="false"><g class="bores">' + "".join(
        f'<rect x="{34 + i * 70}" y="20" width="56" height="110" rx="6"/>' for i in range(4)) + f'</g>{pist}<path class="crank" d="M30 160 H310"/></svg><div class="sim-read"><span>Inline-4</span><span>Firing order 1-3-4-2</span></div></div>'


def wiira_mock():
    cols = [("Found", ["Regional ESG study", "County data tender"]), ("Preparing", ["Expression of interest"]), ("Submitted", ["Concept note", "Proposal"]), ("Won", ["Field validation"])]
    c = "".join(f'<div class="kb-c"><p>{t}</p>' + "".join(f'<span>{x}</span>' for x in xs) + "</div>" for t, xs in cols)
    return f'<div class="mk mk-kb" aria-hidden="true">{c}</div>'


def stack_svg():
    return circuit(77, 600, 400, 12, 20, 4)
