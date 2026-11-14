from lib import *
from mocks import *
from pages_more import agile_section, HALL

LE_SITES = [
    ("Glamourvine Hair & Beauty College", "glamourvinecollege.com", "https://glamourvinecollege.com/"),
    ("Laqim Autoworld", "laqimautoworld.com", "https://laqimautoworld.com/"),
    ("Pentarch Training Institute", "pentarchtraininginstitute.co.ke", "https://pentarchtraininginstitute.co.ke/"),
    ("Johms Interiors", "johms.pentarchcommunications.com", "https://johms.pentarchcommunications.com/"),
    ("Pentarch Systems Solutions", "pentarchsystemssolutions.co.ke", "/"),
]


# ============================================================== HOME
def home():
    slides = [
        ("products", "layers", "Products",
         "Systems Kenyan organisations run on, even when the internet is down.",
         "Pharmacies, shops, salons and colleges run on Pentarch systems every day, with M-Pesa and KRA tax codes built in and a demo before you commit.",
         [btn("/products/", "See our products", "p", "arrow"), btn("/pos/#live-demo", "Try the POS now", "g", "play")],
         duo("mc-dashboard", "Pentarch MediCore dashboard at a pharmacy", "pos-sell", "Pentarch POS sell screen")),
        ("services", "web", "Services",
         "Websites and portals built around you, that your team edits itself.",
         "We design and build each website, portal and dashboard by hand, then hand it over with Pentarch Live Edit so you change any word or picture by clicking on it.",
         [btn("/services/", "See our services", "p", "arrow"), btn("/live-edit/", "How Live Edit works", "g")],
         duo("live-edit", "Pentarch Live Edit open on a client website", "portal-dashboard", "A college portal built for Glamourvine")),
        ("work", "monitor", "Our Work",
         "Experiences people stay on, built for real clients.",
         "A walk-through 3D car showroom, more than 50 science simulations and a media and advocacy dashboard, all running in an ordinary browser.",
         [btn("/work/", "See our work", "p", "arrow"), btn("https://laqimautoworld.com/showroom/", "Enter the 3D showroom", "g", "ne", True)],
         duo("laqim-showroom", "Laqim Autoworld 3D showroom", "sim-heart", "Pentarch SimLab heart simulation")),
    ]
    sl, tb = "", ""
    for n, (k, i, name, h, p, b, vis) in enumerate(slides):
        tag = "h1" if n == 0 else "h2"
        sl += (f'<div class="hs" id="hs-{k}" role="group" aria-roledescription="slide" aria-label="{n + 1} of {len(slides)}"{"" if n == 0 else " data-off"}>'
               f'<div class="hs-txt"><p class="hs-k">{ic(i)}{name}</p><{tag}>{h}</{tag}><p class="hs-p">{p}</p><div class="btns">{"".join(b)}</div></div>'
               f'<div class="hs-vis">{vis}</div></div>')
        tb += f'<button type="button" class="hc-tab" aria-controls="hs-{k}" aria-pressed="{"true" if n == 0 else "false"}">{ic(i)}<span>{name.replace("Pentarch ", "")}</span><i class="hc-bar"></i></button>'
    hero = f'''<section class="hero hero-car t-ink" aria-roledescription="carousel" aria-label="Pentarch systems" data-carousel>
<canvas class="net" data-net aria-hidden="true"></canvas><div class="hero-grid" aria-hidden="true"></div>
<div class="wrap"><div class="hc-slides">{sl}</div>
<div class="hc-ctl"><div class="hc-tabs">{tb}</div><div class="hc-arrows"><button type="button" class="hc-prev" aria-label="Previous slide">{ic("chev")}</button><button type="button" class="hc-pause" aria-label="Pause slides"><i></i></button><button type="button" class="hc-next" aria-label="Next slide">{ic("chev")}</button></div></div></div></section>'''

    readout = section(
        '<div class="readout">' + "".join(
            f'<div class="ro"><b>{v}</b><span>{l}</span></div>' for v, l in [
                ("10", "systems built and in use"), ("10", "websites running Live Edit"), ("50+", "interactive simulations"),
                ("19", "business types in Pentarch POS"), ("47", "counties covered by ComplyScope")]) +
        '</div><p class="ro-note">Counted from the systems and sites listed on this website.</p>', cls="sec-ro", tone="ink2")

    big = [p for p in PRODUCTS if p[0] in ("medicore", "pos", "portal")]
    rest = [p for p in PRODUCTS if p[0] not in ("medicore", "pos", "portal")]
    meta = {
        "medicore": ("Offline-first · local network", ["Pharmacy counter", "Queue and triage", "Lab", "Wards and maternity", "Billing and cash-up"], "30-day free online demo"),
        "pos": ("Offline PWA · cloud sync", ["Selling and receipts", "Stock and expiry", "Credit book", "Shifts and staff PINs", "Branches"], "Live demo, one month free"),
        "complyscope": ("Web app · all 47 counties", ["Obligations", "Deadlines", "Dossier"]),
        "portal": ("WordPress plugin · on your website", ["Admissions and fees", "LMS and exams", "Gradebook", "Certificates", "Alumni"], "Live at a college in Machakos"),
        "beautysuite": ("Web app", ["Bookings", "Walk-ins", "Commissions"]),
        "simlab": ("Browser · free for students", ["Engineering", "Health", "ICT and media"]),
        "qr": ("Web app · API", ["Scans", "Devices", "Reports"]),
        "liveedit": ("WordPress plugin", ["Click to edit", "Revisions", "Blocks"]),
    }
    cards = ""
    for k, t, i, d, h in big:
        m = meta[k]
        cards += (f'<article class="pc pc-big pc-{k}"><div class="pc-art" aria-hidden="true">{circuit(len(k) * 7, 600, 300, 9, 30, 3)}</div>'
                  f'<span class="pc-ic">{ic(i)}</span><p class="pc-m mono">{m[0]}</p><h3><a href="{h}">{t}</a></h3><p>{d}.</p>'
                  f'{tags(m[1])}<p class="pc-free">{ic("spark")}{m[2]}</p></article>')
    for k, t, i, d, h in rest:
        m = meta[k]
        cards += (f'<article class="pc pc-{k}"><span class="pc-ic">{ic(i)}</span><p class="pc-m mono">{m[0]}</p>'
                  f'<h3><a href="{h}">{t}</a></h3><p>{d}.</p>{tags(m[1])}</article>')
    products = section(head("Systems we build, run and support", "Each one started with a real client and is in use today. We install it, train your team and stay on WhatsApp when you need us.") +
                       f'<div class="pgrid">{cards}<a class="pc pc-more" href="/products/#compare"><span class="pc-ic">{ic("layers")}</span><h3>Not sure which one fits?</h3><p>Compare all {len(PRODUCTS)} products side by side: where each runs, what it needs and how to try it.</p><span class="pc-go">Compare products{ic("arrow")}</span></a></div>', sid="products")

    le_sites = "".join(f'<li><a href="{u}"{" target=_blank rel=noopener" if u.startswith("http") else ""}>{ic("web")}{d}</a></li>' for n, d, u in LE_SITES)
    engine = section(f'''<div class="eng"><div class="eng-txt">{head("The engine behind every site we build", "Pentarch Live Edit is our WordPress plugin. We design and code each site by hand, then Live Edit turns every page into something you can change by clicking on it.", "pentarch-live-edit")}
{ticks(["Click any text and type. Click a picture to replace it from the Media Library.", "Change where a link or button goes without touching code.", "Duplicate, move or delete repeated items such as cards and FAQs.", "Every save is kept as a revision, so any change can be undone."])}
<div class="btns">{btn("/live-edit/", "See Live Edit in action", "p", "arrow")}</div>
<p class="small">Running on:</p><ul class="le-sites">{le_sites}</ul></div>
<div class="eng-vis">{browser("your-site.co.ke", liveedit_mock(), "bw-glow")}<ol class="eng-flow"><li>{ic("code")}<span>We code the design</span></li><li>{ic("layers")}<span>Live Edit imports it as blocks</span></li><li>{ic("pen")}<span>You edit on the page</span></li><li>{ic("clock")}<span>Every save kept</span></li></ol></div></div>''',
                     cls="sec-eng", sid="live-edit", tone="ink")

    labs = section(head("Try them here", "Every lab below is live. Nothing loads until you press play, so the page stays light.") + f'''<div class="labs3">
<article class="lab-c">{embed(SIMLAB + "/gears.html", "Pentarch SimLab: gear trains", "SimLab · gear trains", "4/3", f'<div class="emb-art">{sim_mock()}</div>', label="Run the simulation")}<h3><a href="/simlab/">Pentarch SimLab</a></h3><p>Mesh gears and watch the ratio change. One of more than 50 labs.</p></article>
<article class="lab-c">{embed("https://laqimautoworld.com/showroom/", "Laqim Autoworld 3D showroom", "Laqim Autoworld · 3D showroom", "4/3", HALL, label="Enter the showroom")}<h3><a href="/labs/#showroom">3D virtual showroom</a></h3><p>Walk a hall of cars with the keyboard or the arrow pad, then click a car to open it.</p></article>
<article class="lab-c">{embed("https://storymaps.arcgis.com/stories/2f52bd444ef048fb8109f8ca95b92870", "Kenya Rangeland Validation Project StoryMap", "ArcGIS StoryMap · 2026", "4/3", f'<div class="emb-art">{topo(5, 800, 600, 7)}</div>', label="Open the StoryMap")}<h3><a href="/data-maps/#storymaps">Kenya Rangeland Validation</a></h3><p>A dry-season field campaign told with maps. Built with Zingira Pesa.</p></article>
</div>''', cls="sec-labs", tone="ink2")


    why = section(head("Made for power cuts, M-Pesa and busy people", "", "why pentarch") + '<ul class="caps">' + "".join(f"<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>" for i, t, d in [
        ("offline", "Works offline", "MediCore and POS run on a computer at your premises, so a dropped line or a power cut does not stop a sale."),
        ("cash", "M-Pesa built in", "M-Pesa, cash, card or account on one record, with a daily cash-up and over or short per cashier."),
        ("lock", "Your data is yours", "Every user has a role and a PIN. Export or back up your records at any time; we only open your system to support it, with your permission."),
        ("shield", "Kenyan rules built in", "KRA tax codes on receipts, SHA and insurance billing in MediCore, and ComplyScope to keep every filing and permit on time.")]) + "</ul>", cls="sec-why", tone="white")

    how = section(head("From first call to a system your team uses", "The same five steps on every website, portal and system. You approve each stage, and your team is trained before we hand over.") + steps([
        ("Discover", "Your goals, users, workflows and the records you already keep."),
        ("Try and see a demo", "Use a live demo or free trial, then see the system set up for your organisation, at your premises or online."),
        ("Set up", "We configure it, import your items, prices or students, and test."),
        ("Train", "Hands-on training and a short guide for every role."),
        ("Support", "Updates, backups and help by phone and WhatsApp from our Nairobi team, on a monthly or annual plan."),
    ], "steps steps-5"), tone="paper", cls="sec-how")

    stack = [("Node.js", "MediCore server on the facility computer"), ("PHP and WordPress", "Plugins: Portal, Courses, Live Edit, showroom"),
             ("Offline PWA", "POS installs from the browser and runs without internet"), ("IndexedDB sync", "Sales queue on the device and upload on reconnect"),
             ("Three.js and WebGL", "3D showroom, engine cutaways, hot lap"), ("ArcGIS StoryMaps", "Maps and field stories"),
             ("Power BI and custom charts", "Dashboards for programmes and campaigns"), ("M-Pesa Daraja", "Payments confirmed against M-Pesa"),
             ("Preact and Vite", "Fast interfaces on modest hardware"), ("English and Kiswahili", "Every POS screen in both languages")]
    st = "".join(f'<li><b class="mono">{a}</b><span>{b}</span></li>' for a, b in stack)
    stack_s = section(f'{head("What it runs on", "We pick tools that work on the computers and connections our clients already have.")}<ul class="stack">{st}</ul>',
                      tone="ink", cls="sec-stack")

    cases = [("MediCore pilots", "Kenya", "A community pharmacy with its own lab, and a maternity-focused clinic, run their counter, patients and stock on MediCore on their own premises.", "/work/#medicore", ["Pharmacy", "Clinic", "Two facilities"]),
             ("Pentarch POS", "Nairobi", "Tills set up for dukas, chemists, hardware stores, butcheries, restaurants and bars, each with its own tools, and a live demo anyone can open.", "/pos/#live", ["Retail", "Hospitality", "Live demo"]),
             ("Pentarch Training Institute", "Nairobi", "A course catalogue in five schools, class dates that show seats left, and registration with M-Pesa.", "/work/#pti", ["Courses", "M-Pesa"]),
             ("Glamourvine Hair & Beauty College", "Machakos", "College website, student Portal with certificate verification, and BeautySuite for the owner salon.", "/work/#glamourvine", ["Portal", "BeautySuite", "Live Edit"])]
    cs = "".join(f'<article class="case"><p class="case-p">{ic("pin")}{p}</p><h3><a href="{h}">{t}</a></h3><p>{d}</p>{tags(tg)}</article>' for t, p, d, h, tg in cases)
    cases_s = section(head("Recent work", "Real systems for real organisations. Visit them, or ask us for a walk-through.") + f'<div class="cases">{cs}</div><div class="center">{btn("/work/", "See all our work", "d", "arrow")}</div>')

    agents = section(f'''<div class="agent-band"><div>{head("Know businesses and facilities? Become a Pentarch agent.", "Medical reps, pharmacists, IT technicians and students across Kenya introduce Pentarch MediCore and Pentarch POS in their area. Sign up free, record your clients from your phone and start their demos yourself. Pentarch installs, trains and supports.", "earn with pentarch")}</div>
<div class="btns">{btn(MEDICORE + "/portal", "MediCore agents", "p", "ne", True)}{btn(POS + "agents/", "POS agents", "g", "ne", True)}</div></div>''', tone="ink2", cls="sec-agents")
    faqs = section(f'''<div class="split">{head("Before you book a demo")}{faq([
        ("Can you set a system up for the way we work?", "Yes. Each product is configured to your workflows, roles and branding, and we build extra features where you need them. If an existing tool would serve you better, we will tell you."),
        ("How does pricing work?", "A one-off set-up covers configuration, data import and training. After that, a monthly or annual plan covers hosting, support and updates. You receive a written quote after your demo. MediCore has a 30-day online demo and Pentarch POS a free month."),
        ("How long does it take to start?", "Most pharmacies, shops and clinics are running in one day on site. Larger hospitals, schools and colleges are set up in planned stages, department by department."),
        ("Can you take over our existing website or system?", "Usually, yes. We review it first, tell you whether it is worth keeping, and then improve it, move it to secure hosting or rebuild it."),
        ("How does this relate to Pentarch Communications?", "Pentarch Systems Solutions is the systems and software company of the Pentarch family, alongside Pentarch Communications and Pentarch Training Institute. Clients can come to one family for communication, training, websites and the systems that run their work."),
    ])}</div>''', tone="white")
    cta = lead_section("other", "Book my demo", "See it working for your organisation",
                       "Tell us what you run and when suits you. We call to confirm, then show you the system at your premises or online.",
                       ["A demo set up for your type of organisation", "Honest advice on the right system and devices", "No obligation to buy"])
    sv = "".join(f'<li><a href="{h}">{ic(i)}<h3>{t}</h3><p>{d}</p><span class="sv-go">Learn more{ic("arrow")}</span></a></li>' for i, t, d, h in SERVICES)
    services_s = section(head("Built to order", "When a ready-made product does not fit, we build what you need.", "services") + f'<ul class="caps caps-5 sv-cards">{sv}</ul>', tone="white")
    return page("home", hero + readout + products + services_s + why + cases_s + how + agents + faqs + cta)


# ============================================================== PRODUCTS
def products():
    lines = [("cmd", "$ pentarch ls systems/"), ("", "")]
    for k, t, i, d, h in PRODUCTS:
        lines.append(("row", f'<a href="{h}">{t.replace("Pentarch ", "").lower().replace(" & ", "-").replace(" ", "-")}/</a><span>{d}</span>'))
    lines += [("", ""), ("ok", f"{len(PRODUCTS)} products · all in use · demos available"), ("cmd", '$ <i class="cur"></i>')]
    hero = f'''<section class="hero hero-term t-ink"><div class="hero-grid" aria-hidden="true"></div>{circuit(9)}
<div class="wrap hero-2"><div>{crumb("Products")}<h1>Software we build, install and support</h1><p class="hero-p">Seven products, each first built for a client who uses it every day. Choose one to see what it does, how it is deployed and how to try it.</p>
<div class="btns">{btn("/contact/", "Book a demo", "p", "arrow")}{btn("#compare", "Compare products", "g")}</div></div>
{duo("pos-home", "Pentarch POS home screen", "salon-calendar", "Pentarch BeautySuite bookings calendar")}</div></section>'''

    detail = {
        "medicore": ("For pharmacies, clinics and hospitals", "Counter with batches and expiry, patients, queue and triage, lab, wards and beds, maternity, billing, shifts and cash-up, stock, branches and MOH reports.", "Runs on the facility computer and local network; works offline", "30-day online demo", "mc-dashboard"),
        "pos": ("For shops, chemists, restaurants, bars and salons", "Selling with M-Pesa and KRA tax codes, stock and expiry, credit book, staff PINs, shifts, reports and branches.", "Offline web app on your computer, with cloud backup", "Live demo and one month free", "pos-sell"),
        "complyscope": ("For every Kenyan business", "National and county obligations mapped from a short intake, a compliance score, deadlines worked out from the rules, a filing log and a dossier for inspectors and lenders.", "Web app, any browser", "Live dashboard demo, free pilot", "cs-overview"),
        "portal": ("For colleges and training schools", "Admissions, fees, classes, LMS with quizzes, CATs and exams, gradebook, hostel, store, graduation, certificates and alumni.", "WordPress plugin on your college website", "Live at glamourvinecollege.com/portal", "portal-dashboard"),
        "beautysuite": ("For salons, barbers and spas", "Reception desk, bookings calendar, walk-ins, bridal packages with mixed teams, payments, staff commissions and reports.", "Web app for the desk, tablets and phones", "Live for Glamour by Beth", "salon-desk"),
        "learning": ("For training institutes", "Course catalogue in schools, class dates with seats left, online registration with M-Pesa, group rates, trainers and student showcase. Moodle set-up and support.", "WordPress plugin, plus Moodle where needed", "Live at pentarchtraininginstitute.co.ke", "pti-intake"),
        "simlab": ("For colleges, universities and TVETs", "More than 50 interactive simulations across ten departments, from engineering and ICT to health, media and hospitality. Free for students, nothing to install.", "Website, works in any browser", "Free, open it now", "sim-home"),
        "qr": ("For campaigns, publishers and events", "Trackable QR codes with a dashboard of scans by date, device and country, client reports and exports to CSV, Excel and PDF.", "Web app with an API", "Demo on request", "qr-dashboard"),
        "liveedit": ("For every website we build", "Click to edit text, pictures and links, repeat or remove items, site-wide header and footer, and a revision for every save.", "WordPress plugin", "Installed on every Pentarch site", "live-edit"),
    }
    rows = ""
    for n, (k, t, i, d, h) in enumerate(PRODUCTS):
        who, what, dep, tr, sh = detail[k]
        vis = shot(sh, f"{t} screen") if sh else (f'<div class="mon mon-sm">{pos_till()}</div>' if k == "pos" else qr_dash())
        rows += (f'<article class="prow{" prow-r" if n % 2 else ""}" id="p-{k}"><div class="prow-txt"><span class="pc-ic">{ic(i)}</span><p class="mono pc-m">{who}</p>'
                 f'<h2><a href="{h}">{t}</a></h2><p>{what}</p><dl class="kv"><div><dt>Deployment</dt><dd>{dep}</dd></div><div><dt>Try it</dt><dd>{tr}</dd></div></dl>'
                 f'<div class="btns">{btn(h, "Explore " + t.replace("Pentarch ", ""), "d", "arrow")}</div></div><div class="prow-vis">{vis}</div></article>')
    lineup = section(rows, cls="sec-prows")

    cmp_rows = [("Works without internet", ["Yes, on the local network", "Yes, syncs later", "Needs internet", "Needs internet", "Needs internet", "Needs internet", "Needs internet"]),
                ("Runs on", ["Facility computer + LAN", "Your PC or our till", "Browser", "Your website", "Desk, tablet, phone", "Browser", "WordPress"]),
                ("Way to try", ["30-day online demo", "Live demo, one month free", "Live dashboard, free pilot", "Live college site", "Demo on request", "Demo on request", "This website"])]
    th = "".join(f'<th scope="col">{t.replace("Pentarch ", "")}</th>' for k, t, *_ in PRODUCTS)
    tb = "".join(f'<tr><th scope="row">{r}</th>' + "".join(f"<td>{v}</td>" for v in vals) + "</tr>" for r, vals in cmp_rows)
    compare = section(head("Compare at a glance") + f'<div class="tbl-wrap" tabindex="0" role="region" aria-label="Product comparison"><table class="tbl"><thead><tr><td></td>{th}</tr></thead><tbody>{tb}</tbody></table></div>', sid="compare", tone="white")

    also = [("wifi", "WiIRA work planner", "Opportunities pipeline, tasks, notes and categories with Gmail integration. Built for Zingira Pesa's own team.", "Private tool"),
            ("monitor", "Pentarch Showroom plugin", "3D showroom, engine cutaways, games and a parts finder for Laqim Autoworld.", "/labs/#showroom"),
            ("layers", "Johms storage planner", "Visitors design a kitchen or wardrobe and send it for a quote.", "/labs/#planners"),
            ("server", "Pentarch NetDesk", "Billing for internet service providers, building on PentarchNet.", "Planned")]
    al = "".join(f'<li>{ic(i)}<div><h3>{t}</h3><p>{d}</p>' + (f'<a href="{l}">Learn more</a>' if l.startswith("/") else f'<span class="mono">{l}</span>') + "</div></li>" for i, t, d, l in also)
    also_s = section(head("Also built by our team", "Plugins and tools made for one client, which we can adapt for yours.") + f'<ul class="also">{al}</ul>', tone="ink2")
    cta = lead_section("other", "Book my demo", "Not sure which one fits?", "Tell us how your organisation works today. We will suggest the smallest set-up that solves it.", ["One call, no obligation", "A demo using your kind of data", "A written quote after the demo"])
    return page("products", hero + lineup + compare + also_s + cta)


# ============================================================== LIVE EDIT
def live_edit():
    hero = f'''<section class="hero hero-le t-paper"><div class="le-dots" aria-hidden="true"></div><div class="wrap hero-2">
<div class="le-hero-txt">{crumb(("Products", "/products/"), "Live Edit")}<p class="hs-k">{ic("pen")}Pentarch Live Edit · WordPress plugin</p>
<h1>We build it custom. You edit it yourself.</h1><p class="hero-p">Live Edit is the engine inside every website Pentarch builds. Your site is designed and coded by hand, and you still change any word, picture or link by clicking on it.</p>
<div class="btns">{btn("#try", "Try it on this page", "p", "pen")}{btn("/websites/", "Sites running Live Edit", "g")}</div></div>
<div class="le-stage">{solo("live-edit", "Pentarch Live Edit open on a client website")}<span class="le-tip t1">{ic("pen")}Click text to type</span><span class="le-tip t2">{ic("layers")}Duplicate or delete</span><span class="le-tip t3">{ic("clock")}Every save kept</span></div>
</div></section>'''

    caps = [("pen", "Click any text to type", "Headings, paragraphs, lists and buttons. What you see is what visitors get, with the site's own fonts and spacing."),
            ("monitor", "Click a picture to replace it", "Choose a new image from the WordPress Media Library or upload one. Alt text is edited in the same place."),
            ("web", "Change where links go", "Click a link or button to change its address. Links to pages that move are repaired automatically."),
            ("layers", "Duplicate, move or delete", "Hover a repeated item, such as a service card or a question, to copy it, move it or remove it."),
            ("clock", "A revision for every save", "Every save is kept. Compare and restore an earlier version if something goes wrong."),
            ("layers", "Site-wide header and footer", "Edit the header or footer once and it changes on every page."),
            ("code", "Hand-coded designs, imported", "We write each page in HTML, CSS and JavaScript. Live Edit imports it as an editable block, so design freedom stays."),
            ("cog", "Shortcodes inside designs", "Forms, course lists and other dynamic parts sit inside the design and keep working while you edit around them.")]
    cg = "".join(f'<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in caps)
    caps_s = section(head("What you can do on the page", "Live Edit works on ordinary HTML, so it adapts to each design instead of forcing a template.") + f'<ul class="caps">{cg}</ul>', sid="features")

    tryit = section(f'''<div class="split">{head("Try it here", "This box behaves the way Live Edit does on a real site. Click the heading or the text and type. Hover a card to copy or delete it. Your changes stay on your screen only.")}
<div class="le-try" data-le-try><div class="lt-bar"><span class="le-badge">{ic("pen")}Live Edit</span><span class="lt-st" data-lt-status>Not edited</span><button type="button" class="btn btn-s btn-d" data-lt-save>Save</button><button type="button" class="btn btn-s btn-g" data-lt-undo>Undo</button></div>
<div class="lt-page"><h3 data-lt-edit>Fresh bread every morning</h3><p data-lt-edit>Baked in Kahawa West from 5 am. Order before 8 pm for next-day delivery.</p>
<div class="lt-cards" data-lt-list><div class="lt-card"><span class="lt-img" data-lt-img></span><b data-lt-edit>Brown loaf</b></div><div class="lt-card"><span class="lt-img i2" data-lt-img></span><b data-lt-edit>Queen cakes</b></div></div>
<ol class="lt-revs" data-lt-revs aria-label="Revisions"></ol></div></div></div>''', sid="try", tone="ink", cls="sec-try")

    how = section(head("From our code to your hands") + steps([
        ("We design and code", "Each site starts from your brief and is written by hand, with animations, interactive tools and a layout of its own."),
        ("Live Edit imports it", "Every page becomes a block that Live Edit understands. Shortcodes for forms and lists keep working inside it."),
        ("You edit on the page", "Sign in and click. Text, pictures, links and repeated items are all editable in place."),
        ("Every save is kept", "Revisions let you go back. We keep supporting the site after handover."),
    ]))

    sites = "".join(f'<li><a href="{u}"{" target=_blank rel=noopener" if u.startswith("http") else ""}><span class="ls-dot"></span><b>{n}</b><small class="mono">{d}</small>{ic("ne")}</a></li>' for n, d, u in LE_SITES)
    sites_s = section(f'<div class="split">{head("Installed on every Pentarch site", "Ten websites run Live Edit today, from a college with a student portal to a car showcase with a 3D showroom.")}<div><ul class="le-list">{sites}</ul>{btn("/websites/", "See all ten sites", "d", "arrow")}</div></div>', tone="white")

    faqs = faq([
        ("Do I need to know code?", "No. You edit by clicking on the page. Code stays with us, for when you want a new section or a redesign."),
        ("Can I break the design?", "Live Edit only changes words, pictures, links and repeated items, so the layout stays as designed. If something looks wrong, restore an earlier revision."),
        ("Can several people edit?", "Yes. Anyone with an editor account on your WordPress site can use Live Edit. Each save records who made it."),
        ("Is Live Edit sold separately?", "Live Edit comes with every website we build. Ask us if you would like it on an existing WordPress site."),
        ("What happens to forms and dynamic parts?", "They are placed as shortcodes inside the design and keep working while you edit the text around them."),
    ])
    faq_s = section(f'<div class="split">{head("Questions about Live Edit")}{faqs}</div>')
    cta = lead_section("liveedit", "Talk about my website", "Want a site you can edit yourself?", "Tell us about your organisation. We design and build it, then hand you the keys with Live Edit inside.", ["A design of its own, not a template", "Training for the people who will edit it", "Support after handover"])
    return page("live-edit", hero + caps_s + tryit + how + sites_s + faq_s + cta)
