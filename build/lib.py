"""Shared helpers and templates for the Pentarch Systems Solutions blocks.

Every block is plain semantic HTML so Pentarch Live Edit can edit text, images
and links in place. Decorative art is inline SVG without text, marked
aria-hidden. Placeholders {{icon:x}} and {{media:x}} are resolved by the
plugin at import time.
"""
import html, random

SITE = "https://pentarchsystemssolutions.co.ke"
POS = "https://pos.pentarchsystemssolutions.co.ke/pos/"
MEDICORE = "https://medicore.pentarchsystemssolutions.co.ke"
SIMLAB = "https://simlab.pentarchcommunications.com"
PHONE = "+254 729 455 912"
TEL = "tel:+254729455912"
WA = "https://wa.me/254729455912"
MAIL = "info@pentarchsystemssolutions.co.ke"
LOGO = "{{media:https://pentarchcommunications.com/wp-content/uploads/2026/01/cropped-LOGO-LOGO-TRANSPARENT-200x66.png}}"
LOGO_W = "{{media:pss-logo-white.png}}"
MARK = "{{media:pss-mark.png}}"

ICONS = set("arrow ne chev menu x up check call mail pin wa health school scissor cart pen book web map chart wifi offline phone shield lock users server cloud cash box scan print monitor battery lab bed pill cal star layers code search globe cog spark handshake clock play".split())


def e(s):
    return html.escape(s, quote=True)


def ic(name, cls=""):
    assert name in ICONS, name
    c = "ic" + (" " + cls if cls else "")
    return f'<span class="{c}" aria-hidden="true">{{{{icon:{name}}}}}</span>'


URLS = {  # address bar text for each real screenshot (from the screens themselves)
    "agile": "pentarchcommunications.com/AGILE-digital-media-and-advocacy-dashboard",
    "laqim-showroom": "laqimautoworld.com/showroom",
    "pos-home": "pos.pentarchsystemssolutions.co.ke/pos · home",
    "pos-sell": "pos.pentarchsystemssolutions.co.ke/pos · sell",
    "qr-dashboard": "zingirapesa.com/qr/dashboard",
    "glamour-salon": "glamourvinecollege.com/salon",
    "live-edit": "pentarchtraininginstitute.co.ke · Live Edit on",
    "mc-collections": "192.0.2.2:4100/dashboard · collections",
    "mc-dashboard": "192.0.2.2:4100/dashboard",
    "mc-devices": "192.0.2.2:4100/settings",
    "mc-patient": "192.0.2.2:4100/patients/MC100001",
    "mc-patients": "192.0.2.2:4100/patients",
    "mc-queue": "192.0.2.2:4100/queue",
    "mc-register": "192.0.2.2:4100/patients/new",
    "mc-setup-type": "192.0.2.2:4100/setup",
    "mc-timeline": "192.0.2.2:4100/patients/MC100001/timeline",
    "mc-unpaid": "192.0.2.2:4100/dashboard · unpaid",
    "mc-waiting": "192.0.2.2:4100/dashboard · waiting",
    "mc-who": "192.0.2.2:4100/sign-in",
    "portal-admissions": "glamourvinecollege.com/portal/admissions",
    "portal-alumni": "glamourvinecollege.com/portal/graduation/alumni",
    "portal-ceremony": "glamourvinecollege.com/portal/graduation/3",
    "portal-certificates": "glamourvinecollege.com/portal/certificates",
    "portal-classes": "glamourvinecollege.com/portal/academics/cohorts",
    "portal-courses": "glamourvinecollege.com/portal/academics/programmes",
    "portal-dashboard": "glamourvinecollege.com/portal/dashboard",
    "portal-fees": "glamourvinecollege.com/portal/finance",
    "portal-gk-certificates": "glamourvinecollege.com/portal/my-certificates",
    "portal-gk-grades": "glamourvinecollege.com/portal/grades",
    "portal-gk-logbook": "glamourvinecollege.com/portal/logbook",
    "portal-gk-verify": "glamourvinecollege.com/portal/verify",
    "portal-gradebook": "glamourvinecollege.com/portal/lms/gradebook",
    "portal-hostel": "glamourvinecollege.com/portal/hostel",
    "portal-lms-assessments": "glamourvinecollege.com/portal/learn/21/assessments",
    "portal-lms-modules": "glamourvinecollege.com/portal/learn/21/modules",
    "portal-notices": "glamourvinecollege.com/portal/notices",
    "portal-question-bank": "glamourvinecollege.com/portal/question-bank",
    "portal-reports": "glamourvinecollege.com/portal/reports",
    "portal-store": "glamourvinecollege.com/portal/stock",
    "portal-stu-courses": "glamourvinecollege.com/portal/learn",
    "portal-stu-dashboard": "glamourvinecollege.com/portal/dashboard",
    "portal-stu-fees": "glamourvinecollege.com/portal/fees",
    "portal-stu-grades": "glamourvinecollege.com/portal/grades",
    "portal-stu-lesson": "glamourvinecollege.com/portal/learn/1/lesson/237",
    "portal-stu-logbook": "glamourvinecollege.com/portal/logbook",
    "portal-students": "glamourvinecollege.com/portal/students",
    "portal-tr-dashboard": "glamourvinecollege.com/portal/dashboard",
    "portal-tr-logbook": "glamourvinecollege.com/portal/logbook/review",
    "portal-tr-teaching": "glamourvinecollege.com/portal/lms",
    "pti-intake": "pentarchtraininginstitute.co.ke/classes",
    "salon-artist-page": "glamourvinecollege.com/salon/artists/achieng",
    "salon-bookings": "glamourvinecollege.com/portal/desk/bookings",
    "salon-calendar": "glamourvinecollege.com/portal/desk/calendar",
    "salon-checkout": "glamourvinecollege.com/portal/desk/sales/new",
    "salon-clients": "glamourvinecollege.com/portal/desk/clients",
    "salon-commissions": "glamourvinecollege.com/portal/desk/staff",
    "salon-day-close": "glamourvinecollege.com/portal/desk/close",
    "salon-desk": "glamourvinecollege.com/portal/desk",
    "salon-my-portfolio": "glamourvinecollege.com/portal/desk/portfolio",
    "salon-my-work": "glamourvinecollege.com/portal/desk/work",
    "salon-new-booking": "glamourvinecollege.com/portal/desk/bookings/new",
    "salon-reports": "glamourvinecollege.com/portal/desk/reports",
    "salon-stock": "glamourvinecollege.com/portal/desk/products",
    "se-alumni": "samelimu.pentarchcommunications.com/portal/alumni",
    "se-dashboard": "samelimu.pentarchcommunications.com/portal",
    "se-fees": "samelimu.pentarchcommunications.com/portal/fees",
    "se-impact": "samelimu.pentarchcommunications.com/portal/reports",
    "se-letters": "samelimu.pentarchcommunications.com/portal/letters",
    "se-public": "samelimu.pentarchcommunications.com/sponsor",
    "se-sponsor": "samelimu.pentarchcommunications.com/portal",
    "se-student": "samelimu.pentarchcommunications.com/portal/students",
    "sim-heart": "simlab.pentarchcommunications.com/heart.html",
    "sim-home": "simlab.pentarchcommunications.com/",
    "sim-molecule": "simlab.pentarchcommunications.com/molecule-builder.html",
    "sim-pharmacology": "simlab.pentarchcommunications.com/pharmacology.html",
    "sim-robot-arm": "simlab.pentarchcommunications.com/robot-arm.html",
    "sim-tv-studio": "simlab.pentarchcommunications.com/tv-studio.html",
    "sim-wind-tunnel": "simlab.pentarchcommunications.com/wind-tunnel.html",
}


_DIMS = {}


def dims(name):
    """Pixel size of assets/img/pss-shot-<name>.jpg, for width/height attributes (stops layout shift)."""
    if name not in _DIMS:
        import os
        try:
            from PIL import Image
            here = os.path.dirname(os.path.abspath(__file__))
            for root in (os.path.join(here, "..", "assets", "img"), os.path.join(here, "..", "pentarch-systems", "assets", "img")):
                p = os.path.join(root, f"pss-shot-{name}.jpg")
                if os.path.exists(p):
                    _DIMS[name] = Image.open(p).size
                    break
        except ImportError:
            pass
        _DIMS.setdefault(name, None)
    return _DIMS[name]


def img(name, alt, cls="", lazy=True):
    wh = dims(name)
    a = f' width="{wh[0]}" height="{wh[1]}"' if wh else ""
    c = f' class="{cls}"' if cls else ""
    lz = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img src="{{{{media:pss-shot-{name}.jpg}}}}" alt="{e(alt)}"{a}{c}{lz}>'


def shot(name, alt, cls="", url=""):
    """A real screenshot in a browser frame. Add "shot-n" to cls to show the whole image (no crop)."""
    url = URLS.get(name) or url
    u = f'<span class="shot-url">{e(url)}</span>' if url else ""
    return (f'<figure class="shot {cls}"><div class="shot-bar" aria-hidden="true"><i></i><i></i><i></i>{u}</div>'
            f'{img(name, alt)}</figure>')


def duo(a, alt_a, b, alt_b, cls=""):
    """Two real screens: a main one and a smaller one overlapping it (hero visual)."""
    return f'<div class="duo {cls}">{shot(a, alt_a, "shot-a")}{shot(b, alt_b, "shot-b")}</div>'


def solo(a, alt, cls=""):
    return f'<div class="solo {cls}">{shot(a, alt, "shot-a")}</div>'


def journey_tour(jid, steps_, auto=7000):
    """Step-by-step journey through real screens. steps_: (icon, title, roles[list], text, main(name, alt, url), inset(name, alt, url) or None).
    Built on the tabs pattern (works as tabs without the auto-play)."""
    n = len(steps_)
    lst, pan = "", ""
    for k, (icon, title, roles, text, main, inset) in enumerate(steps_):
        on = k == 0
        lst += (f'<button type="button" role="tab" class="jr-t" id="{jid}-t{k}" aria-controls="{jid}-p{k}" aria-selected="{"true" if on else "false"}" tabindex="{0 if on else -1}">'
                f'<span class="jr-n">{ic(icon)}</span><span class="jr-l"><b class="mono">{k + 1:02d}</b>{title}</span><span class="jr-r">{roles[0]}</span></button>')
        vis = (f'<figure class="paper jr-main">{img(main[0], main[1])}</figure>' if main[2] is None
               else shot(main[0], main[1], "shot-n jr-main", main[2]))
        if inset:
            vis += shot(inset[0], inset[1], "shot-n jr-inset", inset[2])
        rl = "".join(f"<li>{r}</li>" for r in roles)
        pan += (f'<div class="tab-panel jr-pane" role="tabpanel" id="{jid}-p{k}" aria-labelledby="{jid}-t{k}"{"" if on else " data-off"}>'
                f'<div class="jr-copy"><p class="jr-k mono">Step {k + 1:02d} of {n:02d}</p><h3>{title}</h3><ul class="jr-roles">{rl}</ul><p>{text}</p></div>'
                f'<div class="jr-vis{" has-inset" if inset else ""}">{vis}</div></div>')
    return (f'<div class="jr" data-tabs data-journey="{auto}"><div class="jr-list" role="tablist" aria-label="Steps" aria-orientation="vertical">{lst}</div>'
            f'<div class="jr-stage">{pan}<div class="jr-ctl"><button type="button" class="jr-prev" aria-label="Previous step">{ic("arrow")}</button>'
            f'<span class="jr-count mono" aria-hidden="true">01 / {n:02d}</span><span class="jr-bar" aria-hidden="true"><i></i></span>'
            f'<button type="button" class="jr-next" aria-label="Next step">{ic("arrow")}</button>'
            f'<button type="button" class="jr-play" aria-label="Pause the journey"><span class="jr-pi" aria-hidden="true"></span><span class="jr-pt">Pause</span></button></div></div></div>')


def tour(tid, items, tone=""):
    """Vertical tabs over real screens. items: (shot name, title, description, url or "")."""
    lst, pan = "", ""
    for k, (name, title, desc, url) in enumerate(items):
        on = k == 0
        lst += (f'<button type="button" role="tab" class="to-t" id="{tid}-t{k}" aria-controls="{tid}-p{k}" aria-selected="{"true" if on else "false"}" tabindex="{0 if on else -1}">'
                f'<b class="mono">{k + 1:02d}</b><span>{title}<small>{desc}</small></span></button>')
        pan += (f'<figure class="tab-panel to-p" role="tabpanel" id="{tid}-p{k}" aria-labelledby="{tid}-t{k}"{"" if on else " data-off"}>'
                f'{shot(name, title + ": " + desc, "shot-n", url)}<figcaption><b>{title}</b> {desc}</figcaption></figure>')
    return f'<div class="tour {tone}" data-tabs><div class="to-list" role="tablist" aria-label="Screens" aria-orientation="vertical">{lst}</div><div class="to-view">{pan}</div></div>'


def btn(href, label, kind="p", icon=None, ext=False, attrs=""):
    t = ' target="_blank" rel="noopener"' if ext else ""
    i = ic(icon) if icon else ""
    return f'<a class="btn btn-{kind}" href="{e(href)}"{t}{attrs}>{label}{i}</a>'


def tags(items, cls="tags"):
    return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def ticks(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{ic('check')}<span>{x}</span></li>" for x in items) + "</ul>"


def head(title, lead="", label="", tag="h2", cls="sh"):
    lab = f'<p class="lab">{label}</p>' if label else ""
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="{cls}">{lab}<{tag}>{title}</{tag}>{ld}</div>'


def section(inner, cls="", sid="", tone="paper"):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="sec t-{tone} {cls}"{i}><div class="wrap">{inner}</div></section>'


def faq(items):
    out = '<div class="faq">'
    for q, a in items:
        out += f'<details><summary><span>{q}</span>{ic("chev")}</summary><div class="faq-a"><p>{a}</p></div></details>'
    return out + "</div>"


def steps(items, cls="steps"):
    if cls == "steps" and len(items) in (3, 5):
        cls = f"steps steps-{len(items)}"
    out = f'<ol class="{cls}">'
    for i, (t, d) in enumerate(items, 1):
        out += f'<li><span class="st-n" aria-hidden="true">{i:02d}</span><h3>{t}</h3><p>{d}</p></li>'
    return out + "</ol>"


def tabs(tid, items):
    """items: list of (key, label, icon, html). Accessible tabs, panels visible without JS."""
    bar = f'<div class="tabs" data-tabs><div class="tab-list" role="tablist" aria-label="Features">'
    pan = ""
    for n, (k, label, icon, body) in enumerate(items):
        on = n == 0
        bar += (f'<button type="button" role="tab" class="tab" id="{tid}-t-{k}" aria-controls="{tid}-p-{k}" '
                f'aria-selected="{"true" if on else "false"}" tabindex="{0 if on else -1}">{ic(icon)}<span>{label}</span></button>')
        pan += f'<div class="tab-panel" role="tabpanel" id="{tid}-p-{k}" aria-labelledby="{tid}-t-{k}"{"" if on else " data-off"}>{body}</div>'
    return bar + "</div>" + pan + "</div>"


def feat_panel(title, text, points, visual):
    return (f'<div class="fp"><div class="fp-txt"><h3>{title}</h3><p>{text}</p>{ticks(points)}</div>'
            f'<div class="fp-vis">{visual}</div></div>')


def embed(src, title, note="", ratio="16/10", poster="", cls="", label="Load live demo"):
    """Click-to-load iframe. Nothing loads until the visitor asks."""
    p = poster or f'<div class="emb-art" aria-hidden="true">{circuit(7, w=800, h=500, n=10)}</div>'
    n = f'<p class="emb-note">{note}</p>' if note else ""
    return (f'<div class="emb {cls}" data-embed="{e(src)}" data-title="{e(title)}" style="--r:{ratio}">'
            f'<div class="emb-poster">{p}<div class="emb-cta"><button type="button" class="btn btn-p emb-go">{ic("play")}{label}</button>{n}</div></div>'
            f'<a class="emb-open" href="{e(src)}" target="_blank" rel="noopener">Open in a new tab{ic("ne")}</a></div>')


def lead_section(product, button, title, text, points, sid="demo", tone="ink"):
    return section(
        f'<div class="lead-grid"><div class="lead-txt">{head(title, text)}{ticks(points)}'
        f'<div class="lead-alt"><a class="btn btn-g" href="{WA}" target="_blank" rel="noopener">{ic("wa")}Chat on WhatsApp</a>'
        f'<a class="btn btn-g" href="{TEL}">{ic("call")}{PHONE}</a></div>'
        f'<p class="small">Or email <a href="mailto:{MAIL}">{MAIL}</a>. You receive a written quote after the demo.</p></div>'
        f'<div class="lead-form">\n[pss_lead_form product="{product}" button="{button}"]\n</div></div>',
        cls="sec-lead", sid=sid, tone=tone)


def crumb(*parts):
    out = '<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a>'
    for p in parts:
        if isinstance(p, tuple):
            out += f'<span aria-hidden="true">/</span><a href="{p[1]}">{p[0]}</a>'
        else:
            out += f'<span aria-hidden="true">/</span><span aria-current="page">{p}</span>'
    return out + "</nav>"


# ---------------------------------------------------------------- decorative art
def circuit(seed=1, w=1200, h=600, n=18, grid=40, pulses=5, cls="circuit"):
    """Deterministic circuit-trace SVG: orthogonal traces with vias, a few carry a travelling pulse."""
    r = random.Random(seed)
    paths, nodes = [], []
    for i in range(n):
        x = r.randrange(0, w // grid + 1) * grid
        y = r.randrange(0, h // grid + 1) * grid
        d = f"M{x} {y}"
        horiz = r.random() < .5
        for _ in range(r.randint(2, 4)):
            L = r.randint(2, 7) * grid
            if horiz:
                x = max(0, min(w, x + (L if r.random() < .6 else -L)))
            else:
                y = max(0, min(h, y + (L if r.random() < .5 else -L)))
            d += f"L{x} {y}"
            horiz = not horiz
        paths.append(d)
        nodes.append((x, y))
    out = f'<svg class="{cls}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
    out += '<g class="tr">' + "".join(f'<path d="{p}"/>' for p in paths) + "</g>"
    out += '<g class="tp">' + "".join(
        f'<path d="{paths[i]}" style="--d:{r.uniform(0, 6):.1f}s;--t:{r.uniform(5, 9):.1f}s"/>' for i in range(min(pulses, n))) + "</g>"
    out += '<g class="vi">' + "".join(f'<circle cx="{x}" cy="{y}" r="4"/>' for x, y in nodes) + "</g></svg>"
    return out


def topo(seed=3, w=1200, h=600, rings=9):
    """Contour-line art for the data and maps pages."""
    r = random.Random(seed)
    out = f'<svg class="topo" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
    import math
    for cx, cy in ((w * .72, h * .45), (w * .2, h * .8)):
        for k in range(1, rings + 1):
            pts = []
            for a in range(0, 360, 12):
                t = math.radians(a)
                rad = k * 34 * (1 + .18 * math.sin(3 * t + k * .7) + .08 * math.cos(5 * t + seed))
                pts.append((cx + rad * math.cos(t) * 1.4, cy + rad * math.sin(t)))
            d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts) + "Z"
            out += f'<path d="{d}"{" class=hi" if k in (3, 7) else ""}/>'
    return out + "</svg>"


def waves():
    """Oscilloscope traces for the labs pages (animated by CSS transform only)."""
    import math
    def path(f, a, ph, w=1600, h=300):
        return "M" + " L".join(f"{x} {h/2 + a*math.sin(x/w*math.pi*2*f + ph):.1f}" for x in range(0, w + 1, 16))
    return ('<svg class="waves" viewBox="0 0 800 300" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
            f'<g class="wv wv1"><path d="{path(3, 70, 0)}"/></g><g class="wv wv2"><path d="{path(5, 40, 1)}"/></g>'
            f'<g class="wv wv3"><path d="{path(2, 100, 2)}"/></g></svg>')


def signal(cls=""):
    return f'<div class="signal {cls}" aria-hidden="true"><i></i></div>'


# ---------------------------------------------------------------- navigation data
PRODUCTS = [
    ("medicore", "Pentarch MediCore", "health", "Hospital and pharmacy system that works offline", "/medicore/"),
    ("pos", "Pentarch POS", "cart", "Point of sale for shops, restaurants and bars", "/pos/"),
    ("complyscope", "ComplyScope Kenya", "shield", "Every filing, permit and renewal for a Kenyan business", "/complyscope/"),
    ("portal", "Pentarch Portal", "school", "College management from admission to alumni", "/portal/"),
    ("beautysuite", "Pentarch BeautySuite", "scissor", "Bookings, desk and commissions for salons", "/beautysuite/"),
    ("qr", "Pentarch QR Analytics", "scan", "Track every scan of a printed campaign", "/qr-analytics/"),
    ("liveedit", "Pentarch Live Edit", "pen", "Edit your website by clicking on it", "/live-edit/"),
]

MENU = [
    ("About", "/about/", "about"),
    ("Products", "/products/", "products"),
    ("Services", "/services/", "services"),
    ("Our Work", "/work/", "work"),
]
SERVICES = [
    ("web", "Websites", "Custom-designed websites you edit yourself with Live Edit", "/websites/"),
    ("layers", "Custom systems and portals", "Software built around how your organisation works", "/services/#systems"),
    ("monitor", "Interactive and 3D", "Showrooms, simulations, games and planners in the browser", "/labs/"),
    ("map", "Dashboards and StoryMaps", "Data, maps and reports people can explore", "/data-maps/"),
    ("cog", "Integrations and automation", "M-Pesa, KRA eTIMS, WhatsApp, SMS and AI assistants", "/services/#integrations"),
]
WORK = [
    ("layers", "All projects", "Every system and site we have built", "/work/"),
    ("lab", "Pentarch SimLab", "50+ simulations for college students", "/simlab/"),
    ("monitor", "Laqim Autoworld", "3D showroom, engine cutaways and games", "/work/#laqim"),
    ("map", "Zingira Pesa", "StoryMaps, nature-finance tools and QR tracking", "/work/#zingira"),
    ("chart", "AGILE dashboard", "Media and advocacy dashboard for ALMANA SS", "/data-maps/#dashboards"),
]
ABOUT = [("/about/", "About us"), ("/about/#team", "Our team"), ("/about/#clients", "Our clients")]
ABOUT_M = [
    ("users", "About us", "Who we are and how we work", "/about/"),
    ("pen", "Our team", "The people who build and support your systems", "/about/#team"),
    ("handshake", "Our clients", "Organisations running Pentarch systems", "/about/#clients"),
    ("globe", "The Pentarch family", "Pentarch Communications and Training Institute", "/about/#family"),
]
LOGO_C = "{{media:pss-logo.png}}"


def mega_item(href, icon, title, desc, ext=False, tag=""):
    t = ' target="_blank" rel="noopener"' if ext else ""
    tg = f' <em class="mm-tag">{tag}</em>' if tag else ""
    return f'<li><a href="{href}"{t}><span class="mm-ic">{ic(icon)}</span><span><b>{title}{tg}</b><small>{desc}</small></span></a></li>'


def header():
    prod = "".join(mega_item(h, i, t, d) for k, t, i, d, h in PRODUCTS)
    serv = "".join(mega_item(h, i, t, d) for i, t, d, h in SERVICES)
    work = "".join(mega_item(h, i, t, d) for i, t, d, h in WORK)
    abt = "".join(mega_item(h, i, t, d) for i, t, d, h in ABOUT_M)
    feats = {
        "about": ("pss-shot-pti-intake.jpg", "About us", "The systems company of the Pentarch family", "Built and supported by a team in Nairobi.", "/about/", "Meet us"),
        "products": ("pss-shot-mc-dashboard.jpg", "Products", "Systems Kenyan organisations run on", "Ready to install, with a demo before you commit.", "/products/", "Compare all products"),
        "services": ("pss-shot-live-edit.jpg", "Services", "Built to order for your organisation", "Websites, portals, dashboards, 3D and integrations.", "/services/", "See our services"),
        "work": ("pss-shot-sim-heart.jpg", "Our work", "Systems and sites in use today", "Visit them live, or ask us for a walk-through.", "/work/", "See all projects"),
    }
    panels = {"about": abt, "products": prod, "services": serv, "work": work}

    def feat(k):
        img, kick, t, d, h, l = feats[k]
        return (f'<a class="mm-feat" href="{h}" style="background-image:url({{{{media:{img}}}}})">'
                f'<span class="mm-k">{kick}</span><span class="mm-ft">{t}</span><span class="mm-fd">{d}</span>'
                f'<span class="mm-fl">{l}{ic("arrow")}</span></a>')

    nav = ""
    for label, href, key in MENU:
        if key in panels:
            nav += (f'<li class="has-mm"><a class="nl" href="{href}" aria-haspopup="true" aria-expanded="false">{label}{ic("chev", "nl-c")}</a>'
                    f'<div class="mm"><div class="mm-in">{feat(key)}<ul class="mm-list">{panels[key]}</ul></div></div></li>')
        else:
            sub = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in ABOUT)
            nav += (f'<li class="has-mm has-dd"><a class="nl" href="{href}" aria-haspopup="true" aria-expanded="false">{label}{ic("chev", "nl-c")}</a>'
                    f'<div class="mm dd"><ul>{sub}</ul></div></li>')

    drawer = ""
    for label, href, key in MENU:
        if key in panels:
            sub = panels[key].replace('<small>', '<small hidden>')
        else:
            sub = "".join(f'<li><a href="{h}"><b>{t}</b></a></li>' for h, t in ABOUT)
        drawer += f'<details><summary>{label}{ic("chev")}</summary><ul>{sub}</ul></details>'

    return f'''<header class="pss pss-hd" data-pss-header>
<a class="skip" href="#pss-main">Skip to content</a>
<div class="hd-top"><div class="hd-top-in">
<span class="hd-tl"><a href="{TEL}">{ic("call")}{PHONE}</a><a href="mailto:{MAIL}">{ic("mail")}{MAIL}</a><a href="{WA}" target="_blank" rel="noopener">{ic("wa")}WhatsApp</a></span>
<span class="hd-tr"><a href="https://pentarchcommunications.com/" target="_blank" rel="noopener">Pentarch Communications</a><a href="https://pentarchtraininginstitute.co.ke/" target="_blank" rel="noopener">Pentarch Training Institute</a></span>
</div></div>
<div class="hd-in">
<a class="hd-logo" href="/" aria-label="Pentarch Systems Solutions home"><img src="{LOGO_C}" alt="Pentarch Systems Solutions" width="434" height="144"></a>
<nav class="hd-nav" aria-label="Main"><ul>{nav}</ul></nav>
<div class="hd-act">{btn("/contact/", "Contact us", "p", "arrow", attrs=' data-cta')}
<button type="button" class="hd-burger" aria-expanded="false" aria-controls="pss-drawer" aria-label="Open menu">{ic("menu", "i-open")}{ic("x", "i-close")}</button></div>
</div>
<div class="drawer" id="pss-drawer" hidden><div class="dr-in">{drawer}
<div class="dr-cta">{btn("/contact/", "Contact us", "p", "arrow")}<a class="btn btn-g" href="{WA}" target="_blank" rel="noopener">{ic("wa")}WhatsApp {PHONE}</a></div></div></div>
</header>'''


def footer():
    cols = [
        ("Products", [(t, h) for k, t, i, d, h in PRODUCTS]),
        ("Services", [(t, h) for i, t, d, h in SERVICES]),
        ("Our work", [(t, h) for i, t, d, h in WORK]),
        ("Company", [(t, h) for h, t in ABOUT] + [("Contact us", "/contact/"), ("Pentarch Communications", "https://pentarchcommunications.com/"), ("Pentarch Training Institute", "https://pentarchtraininginstitute.co.ke/")]),
    ]
    c = ""
    for t, links in cols:
        c += f'<div class="ft-col"><h2>{t}</h2><ul>' + "".join(
            f'<li><a href="{h}"{" target=_blank rel=noopener" if h.startswith("http") else ""}>{l}</a></li>' for l, h in links) + "</ul></div>"
    return f'''<footer class="pss pss-ft">
{signal()}
<div class="ft-art" aria-hidden="true">{circuit(42, 1400, 500, 16, 40, 4)}</div>
<div class="wrap">
<div class="ft-top">
<div class="ft-brand"><a href="/" class="ft-logo"><img src="{LOGO_W}" alt="Pentarch Systems Solutions" width="434" height="144" loading="lazy"></a>
<p>Pentarch Systems Solutions builds the software behind Pentarch websites and the systems our clients run every day. Part of the Pentarch family with <a href="https://pentarchcommunications.com/" target="_blank" rel="noopener">Pentarch Communications</a>, Nairobi.</p>
<ul class="ft-contact"><li><a href="{TEL}">{ic("call")}{PHONE}</a></li><li><a href="{WA}" target="_blank" rel="noopener">{ic("wa")}WhatsApp</a></li><li><a href="mailto:{MAIL}">{ic("mail")}{MAIL}</a></li><li>{ic("pin")}<span>Nairobi, Kenya</span></li></ul></div>
{c}
</div>
<div class="ft-bot"><p>&copy; 2026 Pentarch Systems Solutions. Part of the Pentarch family.</p><p class="mono">Built and edited with Pentarch Live Edit</p></div>
</div>
</footer>'''


def _nowrap_headings(html):
    """Keep hyphenated names such as M-Pesa on one line inside headings."""
    import re as _re
    def fix(m):
        parts = _re.split(r'(<[^>]+>)', m.group(0))
        return "".join(p if p.startswith("<") else _re.sub(r'(?<![\w-])([A-Za-z0-9]+(?:-[A-Za-z0-9]+)+)(?![\w-])', r'<span class="nw">\1</span>', p) for p in parts)
    return _re.sub(r'<h[1-3][^>]*>.*?</h[1-3]>', fix, html, flags=_re.S)


def page(slug, body):
    return f'<div class="pss pss-page pg-{slug}" id="pss-main">\n{_nowrap_headings(body)}\n</div>\n'
