from lib import *
from mocks import *
from pages_prod import gallery

ZP = "https://zingirapesa.com/insights/tools/"
LQ = "https://laqimautoworld.com"

SIMS = {
    "physics": ["projectile", "orbits", "oscillations", "waves-optics", "wind-tunnel", "plane-builder", "helicopter", "gas-laws"],
    "engineering": ["gears", "robot-arm", "truss-bridge", "beams", "engine", "circuits", "logic-gates", "networking", "power-grid", "plant-operator"],
    "biology": ["cell", "chromosomes", "dna-lab", "gene-mixer", "ear", "eye", "neuron", "skeleton", "ecosystem"],
    "health": ["vitals", "heart", "pharmacology", "epidemic"],
    "chemistry": ["molecule-builder", "periodic-table", "reaction-kinetics", "titration"],
    "maths": ["calculus", "matrices", "fourier", "algorithms"],
    "media": ["camera", "lighting", "mixer", "piano", "radio-studio", "tv-studio", "newsroom"],
    "operations": ["air-traffic", "dispatch", "business-finance", "market", "farm"],
    "earth": ["climate", "earthquake"],
}
SUBJ = {"physics": ("Physics and aerospace", "globe"), "engineering": ("Engineering and computing", "cog"), "biology": ("Life sciences", "lab"),
        "health": ("Health", "health"), "chemistry": ("Chemistry", "spark"), "maths": ("Mathematics", "code"), "media": ("Media and broadcast", "play"),
        "operations": ("Operations and business", "chart"), "earth": ("Earth sciences", "map")}
NAMES = {"air-traffic": "Air traffic control", "dna-lab": "DNA splicing lab", "gas-laws": "Gas laws", "gene-mixer": "Sickle cell, G6PD and blood groups",
         "logic-gates": "Logic gates", "molecule-builder": "Molecule builder", "periodic-table": "Periodic table", "plane-builder": "Build a plane",
         "plant-operator": "Treatment plant operator", "power-grid": "National power grid", "radio-studio": "Radio studio", "reaction-kinetics": "Reaction kinetics",
         "robot-arm": "Robot arm kinematics", "truss-bridge": "Truss bridge", "tv-studio": "Direct a match", "waves-optics": "Waves and optics",
         "wind-tunnel": "Wind tunnel", "business-finance": "Business finance", "vitals": "Vitals, NEWS2 and ETAT+ triage", "heart": "Heart, ECG and auscultation",
         "pharmacology": "Drug and drip-rate calculations", "epidemic": "Outbreaks, cholera and KEPI", "mixer": "Mixing desk", "dispatch": "Dispatch centre",
         "gears": "Gear trains", "ear": "The human ear", "eye": "Eye: visual acuity and trachoma", "skeleton": "Fractures and X-ray reading",
         "cell": "Cells, osmosis and IV fluids", "chromosomes": "Karyotypes", "neuron": "Nerves and electrolytes", "newsroom": "Newsroom"}
DESC = {"robot-arm": "Pose a six-axis robot arm.", "gears": "Mesh gears and see the maths move.", "plane-builder": "Design a wing, attach it to an airframe and take off.",
        "wind-tunnel": "Test a wing design in a wind tunnel.", "dna-lab": "Splice introns out of a gene and cross organisms.", "ear": "Walk through the ear's anatomy.",
        "heart": "Watch a heart beat and its ECG trace.", "tv-studio": "Cut cameras on a live football match.", "mixer": "Ride the faders and time the jingle.",
        "plant-operator": "Run a treatment plant and recover from faults.", "air-traffic": "Manage an approach radar sector.", "power-grid": "Control a national power grid.",
        "dispatch": "Handle emergency calls as a dispatcher.", "radio-studio": "Work as a radio presenter.", "newsroom": "Work as a PR and news editor.",
        "vitals": "Vital signs and triage.", "epidemic": "Outbreak and vaccination scenarios.", "pharmacology": "Drug and drip-rate calculations.",
        "helicopter": "Hover a helicopter.", "cell": "Osmosis and IV fluid choice.", "gene-mixer": "Inherited blood conditions and blood groups.",
        "chromosomes": "Karyotypes and Down syndrome.", "skeleton": "Fracture recognition and X-ray reading.", "eye": "Visual acuity and trachoma."}


def sim_name(k):
    return NAMES.get(k, k.replace("-", " ").capitalize())


HALL = '<div class="emb-art hall-art"><div class="hall"></div><i class="pav p1"></i><i class="pav p2"></i><i class="pav p3"></i></div>'


# ============================================================== SOLUTIONS
def solutions_old():
    S = [("health", "health", "Health", "Pharmacies, clinics and hospitals that cannot stop when the internet does.",
          ["Counter and dispensing with batches and expiry", "Queue, triage, lab and referrals", "Wards, beds and maternity", "Billing by cash, M-Pesa, insurance and SHA"],
          [("Pentarch MediCore", "/medicore/"), ("Pentarch POS, chemist type", "/pos/")]),
         ("retail", "cart", "Retail and hospitality", "Dukas, minimarts, hardware stores, agrovets, boutiques, restaurants and bars.",
          ["Selling with M-Pesa and KRA tax codes", "Stock, expiry and reorder", "Credit book and WhatsApp reminders", "Tables, kitchen tickets and bar tabs"],
          [("Pentarch POS", "/pos/")]),
         ("education", "school", "Colleges and training", "Colleges, training institutes and university departments.",
          ["Admissions, fees and online learning", "Certificates with online verification", "Course catalogues with seats left", "Simulations students open in a browser"],
          [("Pentarch Portal", "/portal/"), ("Courses & Learning", "/learning/"), ("Pentarch SimLab", "/simlab/")]),
         ("beauty", "scissor", "Salons and spas", "Salons, barbers, spas and beauty colleges with a training floor.",
          ["Desk, calendar and walk-ins", "Bridal packages with mixed teams", "Commission per stylist", "Product sales at the counter"],
          [("Pentarch BeautySuite", "/beautysuite/"), ("Pentarch POS, salon type", "/pos/")]),
         ("ngo", "handshake", "NGOs and charities", "Sponsorship programmes, conservation and development projects.",
          ["Students, sponsors and donations", "Fees paid to schools and letters", "StoryMaps of field work", "Dashboards for programme results"],
          [("Pentarch EduSponsor", "/ngo-portal/"), ("Data & maps", "/data-maps/")]),
         ("campaigns", "chart", "Campaigns and media", "Publishers, communication teams and event organisers.",
          ["Trackable QR codes on print", "Scans by place, device and time", "Interactive dashboards", "Event and conference microsites"],
          [("QR Analytics", "/qr-analytics/"), ("Dashboards", "/data-maps/#dashboards")]),
         ("web", "web", "Any organisation with a website", "Companies, firms and institutions that want a site of their own.",
          ["Designed and coded for you", "Edited by you with Live Edit", "Interactive tools: planners, checklists, calculators", "Hosted and supported by us"],
          [("Websites we built", "/websites/"), ("Pentarch Live Edit", "/live-edit/")])]
    tiles = "".join(f'<a class="sx" href="#{k}">{ic(i)}<span>{t}</span></a>' for k, i, t, *_ in S)
    hero = f'''<section class="hero hero-sol t-ink"><div class="hero-grid" aria-hidden="true"></div>{circuit(21)}<div class="wrap">
{crumb("Solutions")}<h1>Start from the work you do.</h1><p class="hero-p">Pick your sector to see which systems fit, what they handle and how other organisations like yours use them.</p>
<nav class="sx-grid" aria-label="Sectors">{tiles}</nav></div></section>'''
    body = ""
    for n, (k, i, t, d, pts, prods) in enumerate(S):
        p = "".join(f'<li><a href="{h}">{x}{ic("arrow")}</a></li>' for x, h in prods)
        vis = {"health": medicore_queue(), "retail": f'<div class="mon">{pos_till()}</div>', "education": portal_cert(), "beauty": salon_cal(),
               "ngo": f'<div class="sol-flow">{ngo_flow()}</div>', "campaigns": qr_dash(), "web": browser("your-site.co.ke", liveedit_mock())}[k]
        body += section(f'<div class="sol{" sol-r" if n % 2 else ""}"><div class="sol-t"><div class="sol-h"><span class="sol-ic">{ic(i)}</span><h2>{t}</h2><p>{d}</p></div>{ticks(pts)}<div class="sol-p"><p class="mono">Systems</p><ul>{p}</ul></div></div><div class="sol-v">{vis}</div></div>',
                        sid=k, tone="white" if n % 2 else "paper", cls="sec-sol")
    cta = lead_section("other", "Book my demo", "Not on the list?", "We also build custom systems. Tell us what you need to run and we will tell you honestly whether we can help.", ["One call, no obligation", "A written quote after the demo", "Built and supported in Nairobi"])
    return page("solutions", hero + body + cta)


# ============================================================== LABS
def labs():
    hero = f'''<section class="hero hero-labs t-ink">{waves()}<div class="wrap hero-2"><div>
{crumb(("Services", "/services/"), "Interactive and 3D")}<h1>Websites people stay on.</h1>
<p class="hero-p">A walk-through 3D showroom, animated engine cutaways, a race simulator, calculators and planners, built into client websites. All of them run in an ordinary browser.</p>
<ul class="lab-jump">{"".join(f'<li><a href="#{a}">{ic(i)}{t}</a></li>' for a, i, t in [("showroom", "monitor", "3D showroom"), ("engine", "cog", "Engine cutaways"), ("play", "play", "Games"), ("parts", "search", "Parts finder"), ("tools", "spark", "Nature-finance tools"), ("planners", "layers", "Planners")])}</ul></div>
{duo("site-laqim", "Laqim Autoworld home page", "sim-wind-tunnel", "Pentarch SimLab wind tunnel simulation")}</div></section>'''

    simlab = section(f'''<div class="split">{head("Pentarch SimLab", "More than 50 interactive labs across ten departments, from engineering to health, free for every student and run entirely in the browser.")}
<div>{sim_mock()}<div class="btns">{btn("/simlab/", "Explore all simulations", "p", "arrow")}{btn(SIMLAB + "/", "Open SimLab", "g", "ne", True)}</div></div></div>''', sid="simlab", tone="paper")

    showroom = section(f'''{head("Laqim Autoworld: the 3D showroom", "A private viewing hall for a Nairobi car showcase. Visitors walk between brand pavilions with life-size cars and open any car for its full story.")}
<div class="lab-row"><div class="lab-vis">{embed(LQ + "/showroom/", "Laqim Autoworld 3D showroom", "3D needs a modern browser. On a phone, open it full screen.", "16/10", f'<div class="emb-art emb-shot">{img("laqim-showroom", "Laqim Autoworld 3D showroom")}</div>', label="Enter the showroom")}</div>
<ul class="ctl"><li><kbd>Drag</kbd><span>Look around</span></li><li><kbd>W A S D</kbd><span>Walk, or use the arrow keys or the on-screen pad</span></li><li><kbd>Click</kbd><span>Open a car's card</span></li><li><kbd>Scroll</kbd><span>Zoom</span></li><li><kbd>Tour</kbd><span>Start a guided tour</span></li><li><kbd>Heart</kbd><span>Save a car to My Garage, or add it to a Spec Duel</span></li></ul></div>''', sid="showroom", tone="ink")

    eng = [("Engine room", "Inline-4, V6, flat-6, V8 and V12 cutaways with real crankshaft geometry and firing order, slow-motion X-ray and exploded view."),
           ("Boost Lab", "Feel turbo lag across five set-ups, from naturally aspirated to electric turbo, and record a 0–100 km/h time for each."),
           ("Engine builder", "Choose cylinders, bore, stroke, redline and induction. See displacement, a live dyno chart and piston speed."),
           ("Ear test", "Hear an engine idle, blip and rev to redline, view its waveform and guess the car."),
           ("Stopping distance", "Pick a car, speed, surface and driver state, then see whether it stops before the crossing."),
           ("Performance map", "Plot any two metrics for every car, with bubble size for weight and colour for body style.")]
    e = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in eng)
    engine = section(f'''<div class="split">{head("Under the Hood: engine cutaways", "How cars work, shown with animated 3D models you can orbit, slow down and take apart.")}<div>{engine_mock()}<div class="btns">{btn(LQ + "/lab/", "Open the lab", "d", "ne", True)}</div></div></div><ul class="cards6">{e}</ul>''', sid="engine", tone="white")

    games = [("Race simulator", "Any two cars, any conditions. Power, weight, grip, gearbox, drag and the thin air at Nairobi's altitude decide the result, over 0–100 km/h, a quarter mile, 1 km or an 80–120 overtake."),
             ("Hot lap", "Drive any showcase car round the Laqim circuit in 3D and beat your best lap."),
             ("Launch control", "React to five red lights and launch on green. Reaction time and 0–100 time recorded."),
             ("Paint Studio", "Repaint a 3D car in factory colours, change the finish and the light, then save a photo."),
             ("3D Silhouette", "Name a spinning, blacked-out car from its shadow."),
             ("Size Up", "Compare two cars at true scale against a 1.75 m person.")]
    g = "".join(f'<li><h3>{ic("play")}{t}</h3><p>{d}</p></li>' for t, d in games)
    play = section(head("Play: games built from real specifications", "Thirteen games and tools on one page, all driven by the published figures for each car.") + f'<ul class="cards6 cards-d">{g}</ul><div class="center">{btn(LQ + "/play/", "Play on Laqim Autoworld", "p", "ne", True)}</div>', sid="play", tone="ink2")

    parts = section(f'''<div class="split">{head("Rare parts finder", "Pick a car and a part. The finder gives a rarity score out of ten, the likely wait, the original part name, alternatives and where to look, in order.")}
<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Carbon-ceramic brake discs</b><span>Rarity 8 / 10</span></div><div class="rarity"><i style="--w:80%"></i></div><div class="ml-r"><span>Likely wait</span><b>Factory order</b></div><div class="ml-r"><span>Where to look first</span><b>Franchise dealer</b></div><div class="ml-f">An estimate for orientation. Confirm the part number from the VIN.</div></div></div>
<p class="small">Illustration. The finder's score is a simple model of brand volume, part type and model age, and the site says so.</p>{btn(LQ + "/parts/", "Try the parts finder", "d", "ne", True)}''', sid="parts", tone="paper")

    tools = [("Carbon project revenue estimator", "Credits, revenue, benefit-sharing and payback for a nature-based carbon project, with a cash-flow chart by year.", ZP + "carbon-project-revenue-estimator/", "chart"),
             ("Natural capital balance sheet sketcher", "An order-of-magnitude value for forests, rangelands, wetlands and reefs, from hectares by ecosystem.", ZP + "natural-capital-balance-sheet/", "layers"),
             ("One Health landscape screener", "Ten questions across five dimensions give a readiness profile for a programme or landscape. Answers stay in the browser.", ZP + "one-health-landscape-screener/", "health")]
    t = "".join(f'<article class="tool">{ic(i)}<h3>{n}</h3><p>{d}</p><a href="{u}" target="_blank" rel="noopener">Open the tool{ic("ne")}</a></article>' for n, d, u, i in tools)
    tools_s = section(head("Nature-finance tools, built with Zingira Pesa", "Free calculators on zingirapesa.com. Each one explains its method and its limits on the page.") + f'<div class="tools">{t}</div>', sid="tools", tone="ink")

    plan = [("Design your storage", "Johms Interiors", "Visitors choose a space, style, finish and size, add room photos and send the design for a tailored quote.", "https://johms.pentarchcommunications.com/", "layers"),
            ("Compliance self-assessment", "Charles and Barker", "Two checklists, environmental due diligence (21 questions) and occupational safety and health (30), with an instant score and recommendations.", "https://cnb.pentarchcommunications.com/checklist/", "shield"),
            ("Course planner", "Glamourvine College", "Matches a visitor to a course and shows what it involves.", "https://glamourvinecollege.com/", "school")]
    p = "".join(f'<article class="tool tool-l">{ic(i)}<p class="mono">{c}</p><h3>{n}</h3><p>{d}</p><a href="{u}" target="_blank" rel="noopener">Open it{ic("ne")}</a></article>' for n, c, d, u, i in plan)
    plan_s = section(head("Planners and checklists on client sites", "Small tools that turn a visitor into an enquiry.") + f'<div class="tools">{p}</div>', sid="planners", tone="white")
    cta = lead_section("interactive", "Talk about my idea", "Want something interactive?", "Simulations, 3D, calculators or games: tell us what you want people to understand or do.", ["Runs in an ordinary browser", "Light enough for phones", "Built and hosted by us"])
    return page("labs", hero + showroom + engine + play + parts + tools_s + plan_s + cta)


# ============================================================== SIMLAB
def simlab():
    allk = [(s, k) for s, ks in SIMS.items() for k in ks]
    fan = "".join(f'<div class="fan-i fan-{n}">{shot(k, "", "shot-n")}</div>' for n, k in enumerate(["sim-tv-studio", "sim-heart", "sim-robot-arm"], 1))
    hero = f'''<section class="hero hero-sim t-ink"><div class="sim-orbits" aria-hidden="true"><i></i><i></i><i></i><b></b></div><div class="wrap hero-2">
<div>{crumb(("Our Work", "/work/"), "SimLab")}<p class="hs-k">{ic("lab")}Pentarch SimLab · interactive learning</p><h1>See the maths move.</h1>
<p class="hero-p">A library of {len(allk)} interactive simulations for college and university students, from engineering and physics to anatomy, pharmacology and broadcast media. Every lab runs in the browser with nothing to install, and it is free for every student.</p>
<div class="btns">{btn("#sims", "Browse the simulations", "p", "arrow")}{btn(SIMLAB + "/", "Open SimLab", "g", "ne", True)}</div>
<ul class="hero-facts"><li>{ic("lab")}{len(allk)} interactive labs</li><li>{ic("users")}Free for every student</li><li>{ic("phone")}Laptops, tablets and phones</li></ul></div>
<div class="sim-fan" aria-hidden="true">{fan}</div></div></section>'''
    f = [("play", "Live simulation", "Drag, switch and adjust, and every number on screen comes from the same equations as the lecture notes."),
         ("book", "Theory and worked examples", "The real equations, explained step by step, with worked examples beside the model."),
         ("star", "Challenges and quizzes", "Hands-on scenarios to solve and a quiz at the end, so students can check their own understanding."),
         ("spark", "Demos and guided tours", "A short demo and a guided tour show first-time users what to try."),
         ("monitor", "Present mode", "Lecturers project any lab in class and run it live while they teach."),
         ("phone", "Any device, no install", "Runs in the browser on laptops, tablets and phones, with nothing to download or set up.")]
    feats = section(head("More than an animation. A complete lesson.", "Each lab pairs a live simulation with the theory behind it, so students can test what they read and read about what they see.", "every lab") +
                    f'<ul class="caps caps-3">{"".join(f"<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>" for i, t, d in f)}</ul>', tone="white")
    tour_s = section(head("The labs, on real screens", f"A few of the {len(allk)} labs, as students see them at simlab.pentarchcommunications.com.", "inside simlab") + tour("sl", [
        ("sim-home", "The catalogue", "Every lab a click from the home page, grouped by department.", ""),
        ("sim-robot-arm", "Robot arm kinematics", "Move a joint and watch the tool position and the Denavit–Hartenberg maths update.", ""),
        ("sim-wind-tunnel", "Wind tunnel and airfoils", "Change the angle of attack and see streamlines, lift and drag, right up to the stall.", ""),
        ("sim-heart", "Heart and circulation", "A beating heart with valves, conduction and the ECG it produces, plus clinical cases.", ""),
        ("sim-pharmacology", "Pharmacokinetics", "Dose a teaching drug and follow its concentration through the body over time.", ""),
        ("sim-molecule", "Molecule builder", "Bond atoms, check valence and see the 3D shape of the molecule.", ""),
        ("sim-tv-studio", "TV match director", "Direct a live football broadcast: cut cameras, run replays, graphics and sound.", "")]), sid="inside")
    picks = [("gears", "Gear trains"), ("projectile", "Projectile"), ("orbits", "Orbits"), ("heart", "Heart and ECG"), ("circuits", "Circuits"), ("titration", "Titration")]
    pk = "".join(f'<button type="button" data-sim="{SIMLAB}/{k}.html" aria-pressed="{"true" if n == 0 else "false"}">{t}</button>' for n, (k, t) in enumerate(picks))
    live = section(f'''{head("Run one now", "Choose a simulation and press play. It loads from simlab.pentarchcommunications.com.")}
<div class="simpick" role="group" aria-label="Choose a simulation">{pk}</div>
{embed(SIMLAB + "/gears.html", "Pentarch SimLab simulation", "", "16/9", f'<div class="emb-art">{sim_mock()}</div>', "emb-sim", "Run the simulation")}''', sid="live", tone="ink2")
    flt = '<button type="button" data-f="all" aria-pressed="true">All <span>' + str(len(allk)) + "</span></button>" + "".join(
        f'<button type="button" data-f="{s}" aria-pressed="false">{SUBJ[s][0]} <span>{len(ks)}</span></button>' for s, ks in SIMS.items())
    cards = "".join(f'<li data-s="{s}"><a href="{SIMLAB}/{k}.html" target="_blank" rel="noopener"><span class="sg-ic">{ic(SUBJ[s][1])}</span><b>{sim_name(k)}</b>'
                    f'<small>{DESC.get(k, SUBJ[s][0])}</small><em class="mono">{k}.html</em></a></li>' for s, k in allk)
    grid = section(head("Every simulation", f"{len(allk)} labs, grouped by subject, from gear trains to the newsroom. Each one opens in a new tab.") +
                   f'<div class="filters" role="group" aria-label="Filter by subject" data-filter="#sg">{flt}</div><ul class="simgrid" id="sg">{cards}</ul>', sid="sims", tone="white")
    health = section(f'''<div class="split">{head("Built for Kenyan health students", "Twelve health labs for nursing, clinical medicine and other health courses: clinical cases, timed OSCE stations with mark sheets, drug and fluid calculations with worked steps, and exam-style questions.", "health sciences")}
<div>{shot("sim-pharmacology", "The Pharmacokinetics lab in Pentarch SimLab, with a dosing regimen and plasma concentration chart", "shot-n")}
{ticks(["Follows Kenyan national guidance, including ETAT+, and WHO recommendations", "Vitals, NEWS2 and triage practice", "Cholera outbreaks and KEPI, trachoma, sickle cell, G6PD and GeneXpert", "Works offline once the labs are saved"])}
<p class="small">For learning only. Students always follow current national and facility protocols and their supervisors.</p></div></div>''', tone="ink", cls="sec-health")
    cta = lead_section("simlab", "Talk about SimLab", "Bring SimLab into your courses", "Link labs from your course pages, your LMS or the Pentarch Portal, and use Present mode in lectures. Tell us your courses and we will point your students to the right labs.", ["Free for every student", "Runs in the browser", "Ask us about new labs for your syllabus"], tone="ink2")
    return page("simlab", hero + feats + tour_s + live + grid + health + cta)


AGILE = "https://pentarchcommunications.com/AGILE-digital-media-and-advocacy-dashboard/"


def agile_section(sid, tone="ink", compact=False):
    pipe = (f'<ol class="pipe" aria-label="How the dashboard is built"><li>{ic("server")}<b>Database</b><small>Its own database of results</small></li>'
            f'<li>{ic("cog")}<b>Build and configuration</b><small>Indicators and views set in configuration</small></li>'
            f'<li>{ic("chart")}<b>Interactive dashboard</b><small>One page that filters and charts the data</small></li>'
            f'<li>{ic("users")}<b>Readers</b><small>Teams and partners, on screen or phone</small></li></ol>')
    bars = "".join(f'<i style="--h:{h}%"></i>' for h in [34, 48, 41, 63, 57, 71, 80, 66, 74, 88, 69, 77])
    poster = (f'<div class="emb-art ag-art"><div class="ag-k"><i></i><i></i><i></i><i></i></div><div class="qd-chart">{bars}</div>'
              f'<div class="ag-ring"><svg viewBox="0 0 42 42" aria-hidden="true" focusable="false"><circle cx="21" cy="21" r="15.9" class="r0"/><circle cx="21" cy="21" r="15.9" class="r1"/><circle cx="21" cy="21" r="15.9" class="r2"/></svg></div></div>')
    txt = (f'<p class="hs-k">{ic("chart")}Flagship dashboard</p><h2>AGILE Digital Media &amp; Advocacy Dashboard</h2>'
           f'<p class="lead">Built for ALMANA SS in South Sudan: a data-backed dashboard system for digital media and advocacy results. The page reads from its own database, and a build and configuration layer sets what it shows, so the dashboard grows as the data does.</p>'
           + ticks(["Interactive single-page dashboard, open in any browser", "Backed by its own database, not a static spreadsheet", "Build and configuration kept separate from the data", "Hosted and maintained by Pentarch"])
           + f'<div class="btns">{btn(AGILE, "Open the dashboard", "p", "ne", True)}{"" if compact else btn("/contact/?product=data", "Talk about a dashboard", "g")}</div>')
    poster = f'<div class="emb-art emb-shot">{img("agile", "AGILE Digital Media and Advocacy Dashboard")}</div>'
    return section(f'<div class="agile"><div class="ag-txt">{txt}</div><div class="ag-vis">{embed(AGILE, "AGILE Digital Media and Advocacy Dashboard", "Loads the live dashboard inside this page.", "16/10", poster, "emb-ag", "Load the live dashboard")}{pipe}</div></div>',
                   sid=sid, tone=tone, cls="sec-agile")


# ============================================================== DATA & MAPS
def data_maps():
    SM = "https://storymaps.arcgis.com/stories/"
    stories = [("2f52bd444ef048fb8109f8ca95b92870", "Kenya Rangeland Validation Project", "A dry-season field campaign across selected grassland-savanna landscapes in Kenya.", "March 2026", "Kenya"),
               ("624490cfe6624659808cd615e8eb7258", "Field visits reports", "Field visits in Gaza, Maputo and Sofala provinces.", "September 2024", "Mozambique"),
               ("55e1e6378de442a9b2f6e9f165e0c6d2", "Sofala Province field visit and market research", "Data quality assessment in Gorongosa and market research for programme design.", "June 2024", "Mozambique"),
               ("25f6a0cf24f24086b161c6565f8a7f72", "KHETA field review", "Verification visits in the Limpopo–Kruger area.", "August 2023", "Mozambique")]
    hero = f'''<section class="hero hero-data t-ink">{topo(3)}<div class="wrap hero-2"><div>
{crumb(("Services", "/services/"), "Dashboards and StoryMaps")}<h1>From field data to a story people can follow.</h1>
<p class="hero-p">ArcGIS StoryMaps, interactive dashboards and campaign analytics. We turn survey points, programme results and scans into pages decision-makers actually read.</p>
<div class="btns">{btn("#dashboards", "See the AGILE dashboard", "p", "arrow")}{btn("#storymaps", "See the StoryMaps", "g")}</div></div>
{solo("sm-map", "Kenya Rangeland Validation Project StoryMap: field sites from Kajiado to Kilifi")}</div></section>'''
    first = stories[0]
    feat = section(f'''{head("StoryMaps, built with Zingira Pesa", "Field campaigns and programme reviews in Kenya and Mozambique, published as ArcGIS StoryMaps.")}
<div class="sm-feat">{embed(SM + first[0], first[1] + " StoryMap", "Opens the StoryMap inside this page.", "16/10", f'<div class="emb-art emb-shot">{img("sm-cover", "Kenya Rangeland Validation Project StoryMap cover")}</div>', label="Open the StoryMap here")}
<div class="sm-txt"><p class="mono">{first[3]} · {first[4]}</p><h3>{first[1]}</h3><p>{first[2]} Co-authored by the field team; 155 ground-truth points and 360 paired observations.</p></div></div>
<ul class="sm-list">''' + "".join(f'<li><a href="{SM}{i}" target="_blank" rel="noopener">{ic("map")}<span><b>{t}</b><small>{d}</small></span><em class="mono">{dt} · {pl}</em></a></li>' for i, t, d, dt, pl in stories[1:]) +
        f'''</ul><p class="small">Zingira Pesa's founder was interviewed for an Esri ArcGIS blog feature on StoryMaps and USAID partnerships (August 2024). <a href="https://www.esri.com/arcgis-blog/products/story-maps/sharing-collaboration/a-growing-success-story-usaid-partnerships-deliver-results-for-people-and-the-planet" target="_blank" rel="noopener">Read the Esri article</a>.</p>''',
        sid="storymaps", tone="ink")
    agile = agile_section("dashboards", "ink2")
    dash = section(head("More dashboards and microsites", "Interactive single-page builds hosted on our server.") + f'''<div class="dash2">
<article class="dash-c">{browser("pentarchcommunications.com/8th_ADFC_2026_Conference", img("adfc", "8th ADFC 2026 programme dashboard"))}
<h3>8th ADFC 2026 Conference</h3><p>Programme dashboard for the University of Nairobi conference: speakers, papers, itinerary and fees on one page.</p><a href="https://pentarchcommunications.com/8th_ADFC_2026_Conference/" target="_blank" rel="noopener">Open the microsite{ic("ne")}</a></article>
<article class="dash-c">{browser("zingirapesa.com/qr", img("qr-dashboard", "Pentarch QR Analytics dashboard"))}<h3>QR Analytics</h3><p>Scans of printed campaigns by date, device and country, with client reports.</p><a href="/qr-analytics/">See QR Analytics{ic("arrow")}</a></article></div>''', sid="more-dash", tone="white")
    deliver = section(head("From the field form to the board meeting", "We connect the way you collect data to the way people read it, then automate the reporting so it arrives on time every month.", "what we deliver") + '<ul class="caps caps-3">' + "".join(f"<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>" for i, t, d in [
        ("chart", "Programme and M&amp;E dashboards", "Indicators against targets, by site, month and partner, for managers and funders."),
        ("phone", "KoboToolbox and ODK pipelines", "Field forms flowing straight into clean tables and dashboards, with checks along the way."),
        ("map", "StoryMaps and web maps", "Maps, photos and findings combined into stories that people scroll through and share."),
        ("web", "Interactive reports", "Microsites and online annual reports instead of PDFs nobody opens."),
        ("clock", "Automated reporting", "Monthly summaries generated and sent without anyone rebuilding a spreadsheet."),
        ("users", "Training your team", "Your staff learn to update and extend the dashboards themselves.")]) + "</ul>", sid="deliver")
    method = section(head("How we work with data") + steps([
        ("Collect", "Field forms, survey points, programme records or scans, cleaned and checked."),
        ("Analyse", "Maps, indicators and charts that answer the questions the programme is asked."),
        ("Publish", "A StoryMap, a dashboard or a page on your website, readable on a phone."),
        ("Keep it current", "Updated as new data arrives, with the method written down."),
    ]), sid="method", tone="white")
    cta = lead_section("data", "Talk about my data", "Have data that needs an audience?", "Tell us what you collect and who needs to see it.", ["StoryMaps and dashboards", "Built for phones as well as screens", "A written quote after the call"])
    return page("data-maps", hero + agile + feat + dash + deliver + method + cta)


# ============================================================== WEBSITES
SITES = [
    ("Glamourvine Hair & Beauty College", "glamourvinecollege.com", "https://glamourvinecollege.com/", "College", "Course planner, online application, student Portal and certificate verification.", ["Portal", "BeautySuite"]),
    ("Laqim Autoworld", "laqimautoworld.com", "https://laqimautoworld.com/", "Car showcase", "3D showroom, Under the Hood engine cutaways, games and a rare-parts finder.", ["Three.js", "Custom plugin"]),
    ("Pentarch Training Institute", "pentarchtraininginstitute.co.ke", "https://pentarchtraininginstitute.co.ke/", "Training", "33 courses in five schools, intakes with seats left and online registration.", ["Courses plugin", "M-Pesa"]),
    ("Zingira Pesa", "zingirapesa.com", "https://zingirapesa.com/", "Advisory", "Nature-finance advisory site with free calculators, insights, a glossary and an interactive network globe.", ["Tools", "QR Analytics"]),
    ("Pentarch Communications", "pentarchcommunications.com", "https://pentarchcommunications.com/", "Studio", "Communication, design and digital studio with hover mega menus and a portfolio of work.", ["Mega menu"]),
    ("LFE Solutions", "lfesolutions.co.ke", "https://lfesolutions.co.ke/", "Company", "Company website with a carousel home hero.", ["Carousel"]),
    ("RARC Consulting", "rarcconsulting.com", "https://rarcconsulting.com/", "Advisory", "Advisory firm for non-profits: six practice areas, team and an assess-build-grow approach.", ["Team pages"]),
    ("SAM Elimu Charity", "samelimu.pentarchcommunications.com", "https://samelimu.pentarchcommunications.com/", "Charity", "Charity site with sponsor, alumni and staff sign-in and online donations by card, PayPal or M-Pesa.", ["NGO Portal", "Donations"]),
    ("Johms Interiors", "johms.pentarchcommunications.com", "https://johms.pentarchcommunications.com/", "Interiors", "Design-and-build joinery studio with a design-your-storage planner, packages and guides.", ["Planner", "Custom plugin"]),
    ("Charles and Barker", "cnb.pentarchcommunications.com", "https://cnb.pentarchcommunications.com/", "Consultancy", "Environmental and OSH consultancy with a free compliance self-assessment.", ["Checklist tool"]),
    ("Sasa Media", "sasamedia.pentarchcommunications.com", "https://sasamedia.pentarchcommunications.com/", "Media agency", "Corporate publishing and development communication agency, with a sample media-monitoring dashboard.", ["Sample dashboard"]),
    ("PentarchNet", "net.pentarchcommunications.com", "https://net.pentarchcommunications.com/", "Internet", "Home and business internet, pay-as-you-go hotspot by M-Pesa, CCTV and networking.", ["Hotspot"]),
    ("Natural State", "nsnew.pentarchcommunications.com", "https://nsnew.pentarchcommunications.com/", "Redesign concept", "A redesign concept for a restoration NGO, explaining how a data point becomes funding.", ["Concept"]),
]


SITE_SHOT = {"glamourvinecollege.com": "glamourvine", "laqimautoworld.com": "laqim", "pentarchtraininginstitute.co.ke": "pti", "zingirapesa.com": "zingira",
             "pentarchcommunications.com": "comms", "lfesolutions.co.ke": "lfe", "rarcconsulting.com": "rarc", "samelimu.pentarchcommunications.com": "samelimu",
             "johms.pentarchcommunications.com": "johms", "cnb.pentarchcommunications.com": "cnb", "sasamedia.pentarchcommunications.com": "sasamedia",
             "net.pentarchcommunications.com": "net", "nsnew.pentarchcommunications.com": "ns"}


def site_shot(d, n):
    """Real home-page screenshot of a client website."""
    return img("site-" + SITE_SHOT[d], n + " home page")


def websites():
    stack = "".join(f'<div class="bwst" style="--i:{i}">{browser(d, site_shot(d, n))}</div>' for i, (n, d, *_r) in enumerate(SITES[:4]))
    hero = f'''<section class="hero hero-web t-paper"><div class="wrap hero-2"><div>{crumb(("Services", "/services/"), "Websites")}
<h1>Thirteen websites, each one edited by its owner.</h1>
<p class="hero-p">Colleges, consultancies, charities, a car showcase and an internet provider. Every one is coded by hand, hosted on our server and editable by its owner.</p>
<div class="btns">{btn("#sites", "See the websites", "p", "arrow")}{btn("/live-edit/", "How Live Edit works", "g")}</div></div><div class="bw-stack">{stack}</div></div></section>'''
    cards = "".join(f'''<article class="site"><a class="site-vis" href="{u}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">{browser(d, site_shot(d, n))}</a>
<p class="site-k mono">{k}</p><h3><a href="{u}" target="_blank" rel="noopener">{n}{ic("ne")}</a></h3><p>{t}</p>{tags(["Live Edit"] + tg)}</article>''' for i, (n, d, u, k, t, tg) in enumerate(SITES))
    grid = section(head("The websites", "Open any of them here. Most include a tool or system of their own.") + f'<div class="sites" id="sites">{cards}</div>', tone="white")
    opts = "".join(f'<option value="{u}">{n}</option>' for n, d, u, *_ in SITES)
    pv = section(f'''<div class="split">{head("Preview one here", "Choose a site and load it in the frame. Some sites do not allow being shown inside another page; open those in a new tab.")}
<div class="sitepv" data-sitepv><label class="sp-l"><span>Website</span><select data-sp-sel>{opts}</select></label>
{embed(SITES[0][2], "Website preview", "", "16/10", label="Load the preview")}</div></div>''', tone="ink")
    what = section(head("What comes with a Pentarch website") + f'''<ul class="caps">{"".join(f"<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>" for i, t, d in [
        ("code", "Designed and coded for you", "A layout, animation and visuals of its own, not a theme with your logo on it."),
        ("pen", "Live Edit inside", "Change words, pictures and links yourself, with a revision for every save."),
        ("layers", "Mega menus and carousels", "Hover menus with icons, and a carousel home hero, where they help visitors find their way."),
        ("spark", "Tools that bring enquiries", "Planners, checklists, calculators and course finders built for your visitors."),
        ("server", "Hosting and email", "Hosted on our server, with domain and email set up for you."),
        ("handshake", "Support after launch", "Changes, new pages and help by phone and WhatsApp.")])}</ul>''')
    cta = lead_section("website", "Talk about my website", "Want a website like these?", "Tell us about your organisation and what the site must do.", ["A design of its own", "Live Edit inside", "A written quote after the call"])
    return page("websites", hero + grid + what + cta)


# ============================================================== WORK
def work():
    cases = [
        ("glamourvine", "Glamourvine Hair & Beauty College", "Machakos", "A college website, a student portal and a salon system that work together.",
         ["College website with a course planner and online application", "Pentarch Portal: admissions, fees, LMS, gradebook, hostel, graduation and certificates", "Certificate verification by QR code", "BeautySuite for Glamour by Beth, the owner salon"],
         [("Portal", "/portal/"), ("BeautySuite", "/beautysuite/"), ("Visit the site", "https://glamourvinecollege.com/")], "portal-verify"),
        ("laqim", "Laqim Autoworld", "Nairobi", "A car showcase where visitors explore, learn how cars work and play.",
         ["3D virtual showroom with brand pavilions and a guided tour", "Under the Hood: engine cutaways and an engine builder", "Race simulator, hot lap, launch control and more games", "Rare parts finder"],
         [("Interactive websites", "/labs/#showroom"), ("Visit the site", "https://laqimautoworld.com/")], "laqim-showroom"),
        ("samelimu", "SAM Elimu Charity", "Kenya and Philadelphia", "A charity that has supported children in rural Kenya through school since 2002.",
         ["New charity website", "Portal for students, schools, sponsors, donations, fees, letters and alumni", "Online donations by card, PayPal or M-Pesa", "Sponsor progress tracking"],
         [("Pentarch EduSponsor", "/ngo-portal/"), ("Visit the site", "https://samelimu.pentarchcommunications.com/")], "se-sponsor"),
        ("pti", "Pentarch Training Institute", "Nairobi", "A professional training institute with 33 certificate courses in five schools.",
         ["Course catalogue by school", "Class dates with live seats left", "Registration with M-Pesa", "Group and organisation requests"],
         [("Courses & Learning", "/learning/"), ("Visit the site", "https://pentarchtraininginstitute.co.ke/")], "pti-intake"),
        ("zingira", "Zingira Pesa", "Nairobi and Maputo", "A natural capital and nature-finance advisory registered in Kenya and Mozambique.",
         ["Website with free nature-finance calculators", "QR Analytics for printed and event material", "WiIRA, an internal opportunities and task planner with Gmail integration", "ArcGIS StoryMaps of field campaigns"],
         [("Data & maps", "/data-maps/"), ("Visit the site", "https://zingirapesa.com/")], None),
        ("agile", "AGILE dashboard", "South Sudan", "A digital media and advocacy dashboard for ALMANA SS, a South Sudanese company, that brings its programme's online results into one place.",
         ["Campaign and media results in one view", "Filters by channel, period and theme", "Built on a private database", "Shared with partners by link"],
         [("Open the dashboard", AGILE), ("Dashboards and maps", "/data-maps/#dashboards")], "agile"),
        ("medicore", "MediCore pilots", "Kenya", "A community pharmacy with its own lab, and a maternity-focused clinic.",
         ["Counter, lab and referrals for the pharmacy", "Inpatient beds and maternity for the clinic", "Runs on the local network", "Sample data removed before real use"],
         [("MediCore", "/medicore/")], "mc-queue"),
        ("cnb", "Charles and Barker", "Nairobi", "An environmental and OSH consultancy working across sub-Saharan Africa.",
         ["Website with nine practice areas", "Free compliance self-assessment: 21 and 30 questions", "Instant score with recommendations"],
         [("Visit the checklist", "https://cnb.pentarchcommunications.com/checklist/")], None),
    ]
    idx = "".join(f'<li><a href="#{k}"><span class="mono">{i + 1:02d}</span>{t}</a></li>' for i, (k, t, *_r) in enumerate(cases))
    hero = f'''<section class="hero hero-work t-white"><div class="wrap hero-2"><div>{crumb("Our work")}<h1>Our work, in use.</h1>
<p class="hero-p">Systems and sites that organisations run every day. Each entry lists what we built and where you can see it.</p></div>
<ol class="w-idx">{idx}</ol></div></section>'''
    body = ""
    for n, (k, t, pl, d, pts, links, sh) in enumerate(cases):
        vis = shot(sh, t) if sh else (wiira_mock() if k == "zingira" else (engine_mock() if k == "laqim" else '<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Compliance score</b><span>OSH checklist</span></div><div class="rarity"><i style="--w:72%"></i></div><div class="ml-r"><span>Questions</span><b>30</b></div><div class="ml-f">Recommendations shown instantly</div></div>'))
        lk = "".join(btn(h, l, "d" if j == 0 else "g", "ne" if h.startswith("http") else "arrow", h.startswith("http")) for j, (l, h) in enumerate(links))
        body += section(f'<article class="wcase{" wcase-r" if n % 2 else ""}"><div class="wc-txt"><p class="case-p">{ic("pin")}{pl}</p><h2>{t}</h2><p class="lead">{d}</p><h3 class="mono">What we built</h3>{ticks(pts)}<div class="btns">{lk}</div></div><div class="wc-vis">{vis}</div></article>',
                        sid=k, tone="paper" if n % 2 == 0 else "white")
    cta = lead_section("other", "Book my demo", "Your organisation next?", "Tell us what you run. We will show you what we have built for others like you.", ["Real systems, not mock-ups", "Walk-throughs on request", "No obligation"])
    return page("work", hero + body + cta)


# ============================================================== ABOUT
def about():
    hero = f'''<section class="hero hero-about t-ink"><canvas class="net" data-net aria-hidden="true"></canvas><div class="wrap hero-2"><div>{crumb("About")}
<h1>The systems company of the Pentarch family.</h1>
<p class="hero-p">Pentarch Systems Solutions builds, installs and supports the software behind Pentarch websites and the systems our clients run: health, retail, education, salons, charities and campaigns. We work from Nairobi.</p></div>
<div class="ab-mark"><img src="{MARK}" alt="" width="260" height="260" loading="lazy"><span class="ab-ring" aria-hidden="true"></span></div></div></section>'''
    prin = [("offline", "Offline first", "Our systems keep working when the connection drops, because in many places it does."),
            ("cash", "Built for local payment and tax", "M-Pesa, KRA tax codes and SHA billing where the system needs them."),
            ("globe", "In the language people work in", "English and Kiswahili across Pentarch POS."),
            ("play", "Try before you commit", "Live demos and free trials, then a written quote after the demo."),
            ("pen", "You stay in control", "Your data is yours to export, and your website is yours to edit."),
            ("handshake", "Support from people you can call", f"Phone and WhatsApp on {PHONE}. The people who built your system answer."),
            ("check", "Honest advice", "If an existing tool would serve you better than ours, we will say so before you spend anything."),
            ("shield", "Privacy by design", "Set up around the principles of Kenya's Data Protection Act, with backups and a tested restore plan."),
            ("users", "Trained before handover", "Hands-on training and a short guide for every role, before we call a system live.")]
    p = "".join(f'<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in prin)
    who = section(f'''<div class="split">{head("Software built and supported in Nairobi", "", "who we are")}<div class="prose"><p>Pentarch Systems Solutions is the systems and software company of the Pentarch family, alongside Pentarch Communications, the Nairobi studio known for communication strategy, design and campaigns. We grew out of building websites and portals for Pentarch clients, and now build and support our own products.</p>
<p>Clients get one team that understands both the message and the machinery: what an organisation needs to say, and the systems it needs to run its day.</p></div></div>''', tone="white")
    pr = section(head("What you can expect from us") + f'<ul class="caps caps-3">{p}</ul>', tone="paper")
    fam = section(f'''{head("Part of the Pentarch family")}<div class="fam">
<a class="fam-c" href="https://pentarchcommunications.com/" target="_blank" rel="noopener"><img src="{LOGO}" alt="Pentarch Communications" width="168" height="56" loading="lazy"><p>Strategic communication, design and digital studio.</p><span>pentarchcommunications.com{ic("ne")}</span></a>
<div class="fam-c fam-me"><span class="fam-ic">{ic("server")}</span><h3>Pentarch Systems Solutions</h3><p>Systems, plugins and websites.</p><span class="mono">pentarchsystemssolutions.co.ke</span></div>
<a class="fam-c" href="https://pentarchtraininginstitute.co.ke/" target="_blank" rel="noopener"><span class="fam-ic">{ic("book")}</span><h3>Pentarch Training Institute</h3><p>Professional certificate courses, taught by practitioners.</p><span>pentarchtraininginstitute.co.ke{ic("ne")}</span></a>
</div>''', tone="white", sid="family")

    team = section(f'''<div class="split">{head("The team behind the systems", "A Nairobi team of developers, designers and trainers.")}
<div class="people"><div class="person"><span class="pp-av" aria-hidden="true">CN</span><div><h3>Caroline Mukami Njue</h3><p class="mono">Director</p><p>Communications Director of Pentarch Communications. Leads client relationships, product direction and the training that comes with every system.</p><a href="mailto:{MAIL}">{ic("mail")}{MAIL}</a></div></div>
<div class="person"><span class="pp-av" aria-hidden="true">SM</span><div><h3>Stevedenzel Mungai Mukami</h3><p class="mono">Systems and web development</p><p>Builds Pentarch's websites, portals and plugins, including the Pentarch Portal, BeautySuite, Live Edit and the courses system.</p></div></div></div></div>''', tone="ink", sid="team")
    clients = section(head("Our clients", "Organisations running Pentarch systems and websites today.", "clients") + '<ul class="cl-list">' + "".join(f'<li><a href="{h}">{ic(ii)}<span><b>{n}</b><small>{w}</small></span></a></li>' for ii, n, w, h in [
        ("school", "Glamourvine Hair & Beauty College", "Website and Pentarch Portal", "/work/#glamourvine"),
        ("scissor", "Glamour by Beth", "Pentarch BeautySuite", "/beautysuite/"),
        ("handshake", "SAM Elimu Charity", "Website and Pentarch EduSponsor", "/work/#samelimu"),
        ("monitor", "Laqim Autoworld", "3D showroom and website", "/work/#laqim"),
        ("map", "Zingira Pesa", "Website, StoryMaps, tools and QR Analytics", "/work/#zingira"),
        ("chart", "ALMANA SS, South Sudan", "AGILE media and advocacy dashboard", "/work/#agile"),
        ("book", "Pentarch Training Institute", "Website and course registration", "/work/#pti"),
        ("shield", "Charles and Barker", "Website and compliance checklist", "/work/#cnb"),
        ("web", "LFE Solutions", "Website", "/websites/"),
        ("web", "RARC Consulting", "Website", "/websites/"),
        ("layers", "Johms Interiors", "Website and storage planner", "/websites/"),
    ]) + "</ul>", sid="clients", tone="paper")

    nums = section('<div class="readout">' + "".join(f'<div class="ro"><b>{v}</b><span>{l}</span></div>' for v, l in [("10", "systems built and in use"), ("13", "websites running Live Edit"), ("50+", "interactive simulations"), ("2", "MediCore pilot facilities")]) + "</div>", tone="ink2", cls="sec-ro")
    cta = lead_section("other", "Get in touch", "Talk to us", "Tell us about your organisation and what you need to run.", ["Nairobi-based team", "Phone and WhatsApp support", "Written quote after the demo"])
    return page("about", hero + who + pr + fam + team + clients + nums + cta)


# ============================================================== CONTACT
def contact():
    hero = f'''<section class="hero hero-contact t-ink"><div class="hero-grid" aria-hidden="true"></div>{circuit(64)}<div class="wrap ct-grid">
<div class="ct-txt">{crumb("Contact us")}<h1>Contact us</h1><p class="hero-p">Tell us what you run and when suits you. We call to confirm, then show you the system at your premises or online. You receive a written quote after the demo.</p>
<ul class="ct-ways"><li><a href="{TEL}">{ic("call")}<span><b>Call</b>{PHONE}</span></a></li><li><a href="{WA}" target="_blank" rel="noopener">{ic("wa")}<span><b>WhatsApp</b>{PHONE}</span></a></li>
<li class="ct-wide"><a href="mailto:{MAIL}">{ic("mail")}<span><b>Email</b>{MAIL}</span></a></li><li class="ct-wide"><span class="ct-n">{ic("pin")}<span><b>Office</b>Nairobi, Kenya · P.O. Box 1087-00241</span></span></li></ul>
<ul class="ct-try"><li><a href="{MEDICORE}/try" target="_blank" rel="noopener">{ic("health")}MediCore 30-day online demo{ic("ne")}</a></li><li><a href="/pos/#live-demo">{ic("cart")}Pentarch POS live demo{ic("arrow")}</a></li><li><a href="{POS}?trial=1" target="_blank" rel="noopener">{ic("spark")}POS one month free{ic("ne")}</a></li></ul></div>
<div class="lead-form ct-form">\n[pss_lead_form button="Book my demo"]\n</div></div></section>'''
    hours = section(f'''<div class="split">{head("Support hours", "WhatsApp and phone support from our Nairobi team, Monday to Saturday, 8am to 6pm.")}
<div class="hrs mono" aria-label="Support hours"><p><span>Monday to Saturday</span><b>8:00 to 18:00</b></p><p><span>Phone and WhatsApp</span><b>{PHONE}</b></p></div></div>''')
    nxt = section(head("What happens after you send the form") + steps([
        ("We call you", "We call or WhatsApp to confirm what you would like to see and when."),
        ("The demo", "At your premises or online, set up for your kind of organisation."),
        ("A written quote", "You receive a written quote after the demo, with what is included."),
        ("Set-up and training", "If you go ahead, we install, load your records and train your team."),
    ]), tone="white")
    agents = section(f'''<div class="split">{head("Sell Pentarch systems", "Sales agents can register and follow their clients online.")}<div class="btns">{btn(POS + "agents/", "POS agent portal", "d", "ne", True)}{btn(MEDICORE + "/portal", "MediCore agent portal", "g", "ne", True)}</div></div>''', tone="white")
    return page("contact", hero + nxt + hours + agents)


# ============================================================== DASHBOARDS (old address)
def dashboards():
    """The v1 site had /dashboards/. Its content now lives on /data-maps/; this page sends visitors there."""
    body = section(f'''<div class="moved" data-redirect="/data-maps/"><meta http-equiv="refresh" content="0; url=/data-maps/">
<p class="hs-k">{ic("chart")}Dashboards and StoryMaps</p><h1>This page has moved to Data and maps</h1>
<p class="lead">Our dashboards, the AGILE dashboard and the StoryMaps built with Zingira Pesa are now on one page.</p>
<div class="btns">{btn("/data-maps/", "Go to Data and maps", "p", "arrow")}{btn("/data-maps/#storymaps", "StoryMaps", "g")}</div></div>''', tone="ink", cls="sec-moved")
    return page("dashboards", body)


# ============================================================== SERVICES
def services():
    hero = f'''<section class="hero hero-svc t-ink"><div class="hero-grid" aria-hidden="true"></div>{circuit(17)}<div class="wrap hero-2"><div>{crumb("Services")}
<p class="hs-k">{ic("layers")}Built to order</p><h1>When a ready-made product does not fit, we build it.</h1>
<p class="hero-p">Websites, portals, dashboards, interactive experiences and integrations, designed around how your organisation works. Every Pentarch product started this way, for one client, and is still in use.</p>
<div class="btns">{btn("/contact/", "Tell us what you need", "p", "arrow")}{btn("/work/", "See what we have built", "g")}</div></div>
<div class="svc-shots">{shot("portal-dashboard", "A college portal built for Glamourvine Hair & Beauty College", "shot-a")}{shot("se-dashboard", "A sponsorship portal built for SAM Elimu Charity", "shot-b")}</div></div></section>'''
    S = [("websites", "web", "Websites", "Designed and coded by hand for each client, then handed over with Pentarch Live Edit so your team changes any word, picture or link by clicking on it.",
          ["Custom design, no templates", "Fast on phones and slow connections", "Live Edit included on every site", "Hosting, domains and email set up for you"],
          [("See the websites we built", "/websites/"), ("How Live Edit works", "/live-edit/")], "live-edit"),
         ("systems", "layers", "Custom systems and portals", "Management systems built around your own process: who does what, who approves, and what each person sees. We start from a working demo and grow it with you.",
          ["Student, member and client portals", "Fees, payments and M-Pesa", "Approvals with a full audit trail", "Reports your board and funders ask for"],
          [("Glamourvine college portal", "/work/#glamourvine"), ("SAM Elimu sponsorship portal", "/work/#samelimu")], "portal-students"),
         ("interactive", "monitor", "Interactive and 3D", "Experiences people stay on: 3D showrooms, simulations, games, planners and calculators that run in an ordinary browser.",
          ["3D showrooms and product tours", "Simulations for teaching", "Games built from real data", "Planners and calculators that bring enquiries"],
          [("Interactive and 3D work", "/labs/"), ("Pentarch SimLab", "/simlab/")], "sim-home"),
         ("data", "map", "Dashboards and StoryMaps", "Programme and campaign data turned into dashboards, maps and reports that people can explore and act on.",
          ["ArcGIS StoryMaps of field work", "Media and advocacy dashboards", "QR tracking for printed material", "Training so your team keeps them up to date"],
          [("Dashboards and maps we built", "/data-maps/"), ("Zingira Pesa StoryMaps", "/data-maps/#storymaps")], "agile")]
    body = ""
    for n, (k, i, t, d, pts, links, sh) in enumerate(S):
        lk = "".join(btn(h, l, "d" if j == 0 else "g", "arrow") for j, (l, h) in enumerate(links))
        body += section(f'<article class="wcase{" wcase-r" if n % 2 else ""}"><div class="wc-txt"><p class="case-p">{ic(i)}Service {n + 1:02d}</p><h2>{t}</h2><p class="lead">{d}</p>{ticks(pts)}<div class="btns">{lk}</div></div><div class="wc-vis">{shot(sh, t)}</div></article>',
                        sid=k, tone="paper" if n % 2 == 0 else "white")
    ig = [("cash", "M-Pesa payments", "STK Push prompts on the customer's phone, Paybill and Till confirmations matched to the right bill, B2C payouts and a daily reconciliation."),
          ("shield", "KRA eTIMS invoicing", "Invoices and receipts from your own system signed through eTIMS, with the control unit details printed on every receipt."),
          ("wa", "WhatsApp Business", "Receipts, reminders, appointment confirmations and order updates sent on WhatsApp, with replies routed to your team."),
          ("phone", "Bulk SMS and USSD", "Reminders, alerts and short menus that reach customers on any phone, including those without data."),
          ("globe", "Online card and mobile checkout", "Pesapal, Flutterwave, Paystack or Stripe on your website, with payments landing in your system automatically."),
          ("spark", "AI assistants", "An assistant on your website or WhatsApp that answers from your own documents and prices, and hands over to staff when it should."),
          ("cal", "Google Workspace and Microsoft 365", "Forms, calendars, sheets and email connected to your system, so records stop being copied by hand."),
          ("layers", "Data migration", "Records moved from Excel, QuickBooks or an old system, checked line by line before you go live.")]
    igs = "".join(f'<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in ig)
    integ = section(head("Integrations and automation", "Connect the tools you already use to your system, website or each other. We build these into Pentarch products and into what we build for you.", f"service {len(S) + 1:02d}") +
                    f'<ul class="caps">{igs}</ul><p class="ig-note">Already in use: M-Pesa code checks and WhatsApp receipts in Pentarch POS, WhatsApp summaries in MediCore, calendar links in ComplyScope and Gmail in the WiIRA planner.</p>'
                    f'<div class="btns">{btn("/contact/?product=custom", "Talk about an integration", "d", "arrow")}</div>', sid="integrations", tone="paper" if len(S) % 2 == 0 else "white")
    how = section(head("How a build runs", "You approve each stage, and your team is trained before we hand over.") + steps([
        ("Listen", "We meet your team and see how the work is done today."),
        ("Demo", "A working demo with your own names and sample data, usually within two weeks."),
        ("Build", "We build in short rounds and you test each one."),
        ("Train", "Hands-on training for every role, with a short guide."),
        ("Support", "Phone and WhatsApp support from the people who built it.")]), tone="ink2")
    cta = lead_section("custom", "Send my request", "Tell us what you need built", "A short description is enough. We will call you back and arrange a meeting.", ["One call, no obligation", "A written quote after the demo", "Built and supported in Nairobi"])
    return page("services", hero + body + integ + how + cta)


def solutions():
    """Old address: sector content now lives on the product pages; send visitors to /products/."""
    body = section(f'''<div class="moved" data-redirect="/products/"><meta http-equiv="refresh" content="0; url=/products/">
<p class="hs-k">{ic("layers")}Products</p><h1>This page has moved to Products</h1>
<div class="btns">{btn("/products/", "Go to Products", "p", "arrow")}</div></div>''', tone="ink", cls="sec-moved")
    return page("solutions", body)
