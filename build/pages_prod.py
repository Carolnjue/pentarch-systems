from lib import *
from mocks import *


def integ(items):
    return '<ul class="integ">' + "".join(f'<li>{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in items) + "</ul>"


def gallery(items, cls=""):
    """items: (shot name, caption) or (shot name, title, description)."""
    out = ""
    for it in items:
        n, t = it[0], it[1]
        d = it[2] if len(it) > 2 else ""
        cap = f"<b>{t}</b> {d}" if d else t
        out += (f'<figure class="gal-i"><div class="shot-bar" aria-hidden="true"><i></i><i></i><i></i></div>'
                f'{img(n, t + (": " + d if d else ""))}<figcaption>{cap}</figcaption></figure>')
    return f'<div class="gal {cls}" data-gal>{out}</div>'


def counter_mock():
    rows = [("Amoxicillin 500 mg caps", "B-2291 · exp 03/2027", "30"), ("Paracetamol 500 mg", "B-1180 · exp 11/2026", "20"), ("ORS sachet", "B-0457 · exp 08/2027", "4")]
    r = "".join(f'<div class="ml-r"><span>{n}<small>{b}</small></span><b>{q}</b></div>' for n, b, q in rows)
    return f'<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Counter sale</b><span>Earliest expiry first</span></div>{r}<div class="ml-f">Paracetamol batch B-1180 expires in 30 days</div></div>'


def beds_mock():
    beds = "".join(f'<i class="{c}"></i>' for c in "ooxoxooo-xoooxo-oxoooxoo".replace("-", "f"))
    return f'<div class="mk mk-beds" aria-hidden="true"><div class="ml-h"><b>Maternity ward</b><span>24 beds</span></div><div class="bedg">{beds}</div><div class="bed-k"><span class="o">Occupied</span><span class="x">Free</span><span class="f">Cleaning</span></div></div>'


# ============================================================== MEDICORE
def mc_try():
    """In-page 30-day demo: pss.js posts to the MediCore server, which creates a private demo and returns the sign-in."""
    return f'''<form class="tf mcx" id="mcx-try" novalidate>
<div id="mcx-fields" class="mcx-f">
<div class="seg" role="group" aria-label="Facility type"><button type="button" class="on" aria-pressed="true" data-t="pharmacy">Pharmacy</button><button type="button" aria-pressed="false" data-t="clinic">Clinic</button><button type="button" aria-pressed="false" data-t="hospital">Hospital</button></div>
<label>Facility name<input name="facility" required placeholder="e.g. Afya Bora Chemist"></label>
<div class="r2"><label>Your name<input name="contact" required autocomplete="name"></label><label>Phone<input name="phone" required inputmode="tel" placeholder="07…" autocomplete="tel"></label></div>
<div class="r2"><label>Email (optional)<input name="email" type="email" autocomplete="email"></label><label>Town<input name="town" placeholder="e.g. Thika"></label></div>
<label class="ck"><input type="checkbox" name="agree" required><span>Pentarch may call or WhatsApp me about this demo.</span></label>
<div class="err" id="mcx-err" role="alert"></div>
<button class="go" type="submit">Create my free demo</button>
<p>No card, no devices, no commitment. Or <a href="{MEDICORE}/try" target="_blank" rel="noopener">start the demo on the MediCore site</a>.</p>
</div>
<div id="mcx-done" class="mcx-done" hidden><h3>Your MediCore is ready</h3><p>Save these details. You need them to sign in.</p>
<div class="creds"><div><small>Web address</small><b>medicore.pentarchsystemssolutions.co.ke</b></div><div><small>Username</small><b id="mcx-u"></b></div><div><small>PIN</small><b id="mcx-p"></b></div><div><small>Free until</small><b id="mcx-e"></b></div></div>
<a class="go" href="{MEDICORE}/" target="_blank" rel="noopener">Open my MediCore</a></div>
</form>'''


def lis(items):
    return "".join(f'<li>{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in items)


def medicore():
    hero = f'''<section class="hero hero-mc t-ink"><div class="hero-grid" aria-hidden="true"></div>
<div class="mc-trace" aria-hidden="true">{ecg()}</div>
<div class="wrap hero-2"><div>{crumb(("Systems", "/products/"), "MediCore")}<p class="hs-k">{ic("health")}Pentarch MediCore · health facility system</p>
<h1>The whole facility on one system, with or without internet.</h1>
<p class="hero-p">Counter sales, stock, patients, lab, wards and money in one system for pharmacies, clinics and hospitals in Kenya. It runs on a computer inside your facility and records every sale and every stock movement.</p>
<div class="btns">{btn("#try", "Try it free for 30 days", "p", "arrow")}{btn("#demo", "Book a demo at your facility", "g")}</div>
<ul class="hero-facts"><li>{ic("offline")}Works offline on the local network</li><li>{ic("cash")}Cash, M-Pesa, insurance and SHA billing</li><li>{ic("clock")}One day to install and train</li></ul></div>
<div class="mc-stack">{shot("mc-queue", "MediCore patient queue screen", "shot-a")}{medicore_queue()}</div></div></section>'''

    types = [("pill", "Pharmacies and chemists", "A fast scan-and-sell counter", ["Barcode and 2D medicine-pack scanning", "Expiry alerts and a reorder list from real sales", "Shifts and cash-up per cashier", "Customer accounts, loyalty points and returns"]),
             ("health", "Clinics and medical centres", "The whole patient journey", ["Registration, queue, triage and consultation", "Lab requests, results and referrals", "Prescriptions dispensed from the visit", "Bills for SHA, insurance, M-Pesa and cash"]),
             ("bed", "Hospitals and nursing homes", "Everything, plus wards", ["Admissions, wards and bed occupancy", "Maternity and inpatient charges", "Stores, purchase orders and branch transfers", "Several branches on one owner dashboard"])]
    ty = "".join(f'<li>{ic(i)}<p class="mono">{k}</p><h3>{t}</h3>{ticks(p)}</li>' for i, k, t, p in types)
    who = section(f'''{head("One system, set up for the way you work", "Choose your facility type when we install it. MediCore switches on the screens you need and keeps the rest out of the way. Add branches of any type later.")}
<ul class="types types-3">{ty}</ul>{gallery([("mc-setup-type", "Choose the facility type"), ("mc-setup-services", "Choose services and departments"), ("mc-setup-start", "Start with sample data or your own")], "gal-3")}''', sid="who")

    T = [
        ("counter", "Counter and pharmacy", "pill", feat_panel("A fast counter that knows your stock",
            "Scan, take M-Pesa, cash, card or account. The receipt prints and stock drops from the right batch, earliest expiry first.",
            ["Barcode scanning, keyboard shortcuts and credit sales", "Discounts that need a supervisor PIN", "Packs and loose units, shelf stock takes", "A witnessed register for expired stock"],
            counter_mock())),
        ("patients", "Patients and queue", "users", feat_panel("Every patient, every visit, one timeline",
            "Register a patient once. Each visit moves through the queue, from triage to consultation, lab, pharmacy and the cashier, and stays on the patient's timeline.",
            ["Patient register and search", "Queue and triage with waiting times", "Vitals, notes, diagnoses and appointments", "Referrals out, with results recorded on return"],
            shot("mc-patients", "MediCore patient register", "shot-n"))),
        ("lab", "Laboratory", "lab", feat_panel("Lab requests and results in the same record",
            "Clinicians request tests from the consultation. The lab works through its own list and enters results with normal ranges on the patient record.",
            ["Lab requests from consultation", "Results with normal ranges", "Printable lab reports", "Tests sent out and results taken back in"],
            shot("mc-timeline", "MediCore visit timeline", "shot-n"))),
        ("wards", "Wards and maternity", "bed", feat_panel("Wards, beds and maternity",
            "See which beds are free, admit and discharge, and follow mothers and babies through maternity care.",
            ["Wards and bed occupancy", "Admissions, transfers and discharge bills", "Maternity records", "Inpatient charges"],
            beds_mock())),
        ("billing", "Billing and cash-up", "cash", feat_panel("Billing, payments and cash-up",
            "M-Pesa, cash, card, SHA and insurance on one bill, with claims follow-up. Each shift closes with a count of the drawer by note and coin.",
            ["Cash, M-Pesa, card, insurance and SHA", "Unpaid bills list and follow-up", "Shifts, cash-up and expenses", "Receipts and statements"],
            shot("mc-unpaid", "MediCore unpaid bills list", "shot-n"))),
        ("stock", "Purchasing and branches", "box", feat_panel("Stock in, and stock between branches",
            "Suggested orders go to suppliers on WhatsApp. Partial deliveries are received against the order, and stock moves between branches in send and receive steps.",
            ["Suggested orders on WhatsApp", "Partial deliveries and what you owe each supplier", "Branch transfers with send and receive steps", "Batch and expiry from the pack's 2D code"],
            '<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Branch transfer</b><span>Main to Branch 2</span></div><div class="ml-r"><span>Amoxicillin 500 mg caps<small>B-2291 · exp 03/2027</small></span><b>10 packs</b></div><div class="ml-r"><span>ORS sachet<small>B-0457 · exp 08/2027</small></span><b>50</b></div><div class="ml-r"><span>Sent from main store<small>Supervisor PIN</small></span><b>09:40</b></div><div class="ml-f">Waiting for Branch 2 to receive</div></div>')),
        ("reports", "Reports", "chart", feat_panel("The owner's view, across branches",
            "Profit on the real cost of goods, prices below your markup, best and slowest sellers, and each cashier's takings, for any day or month. A daily summary goes to WhatsApp.",
            ["Branches dashboard", "Profit, dead stock and price checks", "MOH reports", "Daily summary on WhatsApp"],
            shot("mc-dashboard", "MediCore dashboard", "shot-n"))),
    ]
    feats = section(head("Every action has a name and a time", "Owners see who sold what, who changed a price and who opened the drawer, even from another branch. Screens are shown with sample data.") + tabs("mc", T), sid="features", tone="white")

    day = section(head("From the delivery van to the evening report", "A day on MediCore at a pharmacy counter.", "a day on medicore") + steps([
        ("Receive stock", "Scan the delivery. Batch and expiry fill in from the pack's 2D code and the order is ticked off."),
        ("Sell or dispense", "Scan, take M-Pesa, cash, card or account. The receipt prints and stock drops from the right batch."),
        ("Handle returns", "Refunds go back to the original batch, need a supervisor PIN and keep a reason on record."),
        ("Close the shift", "Count the drawer by note and coin. MediCore shows what should be there and asks about any gap."),
        ("Read the numbers", "Profit, best and slowest sellers, dead stock and each cashier's takings, for any day or month."),
    ], "steps steps-5"), sid="day")

    screens = section(head("This is MediCore, not a mock-up", "Screens from the demonstration edition with sample patients and staff. Pick a screen to see it.", "real screens") + tour("mcs", [
        ("mc-dashboard", "Dashboard", "Collections, patients waiting, lab tests pending and unpaid bills, with the live queue.", ""),
        ("mc-queue", "Service queue", "Patients move across the board from triage to clinician, lab, pharmacy and cashier.", ""),
        ("mc-register", "Register a patient", "Search first, then register and send straight to the queue.", ""),
        ("mc-patients", "Patients", "Every patient with number, SHA status, flags and last visit.", ""),
        ("mc-patient", "Health overview", "Vitals and lab values against normal ranges, allergies and chronic conditions.", ""),
        ("mc-timeline", "Patient timeline", "Every visit, result and diagnosis in order.", ""),
        ("mc-waiting", "Patients waiting", "Who is waiting where, and for how long.", ""),
        ("mc-collections", "Collections today", "Takings by payment method and by type, with every payment listed.", ""),
        ("mc-unpaid", "Unpaid bills", "Open bills and balances, one click to billing.", ""),
        ("mc-who", "Who is working?", "Staff pick their name and sign in with their own PIN.", ""),
        ("mc-devices", "Other devices", "Other computers, tablets and phones open MediCore on the facility Wi-Fi.", "")], "tour-d"), sid="screens", tone="ink2")

    dep = section(f'''<div class="dep">{head("Your facility keeps working when the line or the power goes", "MediCore is a Node.js application installed on a computer inside your facility. Other computers, tablets and phones on your Wi-Fi connect to it. The internet is only needed for M-Pesa prompts, backups and checking the business from outside.", "offline first")}
<div class="lan" aria-hidden="true"><div class="lan-srv">{ic("server")}<b>Facility computer</b><small>MediCore server</small></div>
<div class="lan-ring"><span>{ic("monitor")}Reception</span><span>{ic("health")}Consultation</span><span>{ic("lab")}Lab</span><span>{ic("pill")}Pharmacy</span><span>{ic("cash")}Cashier</span><span>{ic("bed")}Ward</span></div>
<div class="lan-cloud">{ic("cloud")}<small>Backups and WhatsApp summary when online</small></div></div></div>
<ul class="integ integ-d">{lis([
    ("monitor", "Main computer at the counter", "Holds every record. Scanner, printer and cash drawer plug in here."),
    ("wifi", "Facility Wi-Fi", "Consultation room, lab and store use tablets or phones. No internet needed."),
    ("cloud", "Internet, when available", "Backups, M-Pesa prompts and the owner checking sales from anywhere."),
    ("lock", "PINs and roles", "A cashier never sees the profit report. Every user signs in with their own PIN.")])}</ul>''', tone="ink", cls="sec-dep")

    kit_s = section(f'''<div class="split">{head("The MediCore Counter Kit", "Tested devices that work together, delivered and installed. Buy MediCore with the complete kit, or let us set it up on the computers you already have. Every item is stocked in Kenya, so a replacement is a day away.", "devices")}
<ul class="kit">{lis([
    ("monitor", "Computer", "Renewed business mini PC, Core i5, 8 GB, SSD, 19-inch monitor, keyboard and mouse."),
    ("scan", "2D barcode scanner", "Reads box barcodes and the square codes on medicine packs. Plugs into USB."),
    ("print", "Receipt printer", "80 mm thermal printer with automatic cutter, USB and network."),
    ("cash", "Cash drawer", "Opens automatically when a cash sale prints."),
    ("battery", "Power backup", "About 15 minutes to finish sales and close safely during a power cut."),
    ("wifi", "Wi-Fi router and paper", "For tablets and phones in other rooms, plus receipt rolls to start.")])}</ul></div>''', sid="kit", tone="white")

    how = section(head("From demo to daily use") + steps([
        ("Try the online demo", "Create your own 30-day demo on this page and set it up as your facility type."),
        ("Demo at your facility", "We show MediCore with your services, prices and departments."),
        ("Install and connect", "One day on site for most pharmacies and clinics: we install, import your items and prices, and connect your devices."),
        ("Train and go live", "Staff get their own PINs and are trained by role. Larger hospitals go live department by department."),
    ]))
    tryit = section(f'''<div class="lead-grid"><div class="lead-txt">{head("See your own MediCore in one minute", "You get a private copy already filled with sample medicines, patients and a month of sales, so every report has something to show. Use it on a phone or computer.", "free for 30 days")}
{ticks(["Make a sale, receive stock, close a shift, read the profit report.", "A Pentarch advisor calls to take you through it.", "If you buy, your demo becomes your live system."])}</div>
<div class="lead-form">{mc_try()}</div></div>''', sid="try", tone="ink2", cls="sec-lead sec-try")
    pilots = section(f'''<div class="split">{head("Piloted in two real facilities", "MediCore was built with the people who use it, and shaped by their daily work.")}
<ul class="pilots">{lis([("pill", "A community pharmacy with its own lab", "Counter sales, lab tests, minor procedures and referrals out for tests and scans, with results taken back in."),
    ("bed", "A maternity-focused clinic", "A general clinic with inpatient beds, where most admissions are for maternity care.")])}</ul></div>''', tone="ink")

    ints = section(head("Works with what you already use") + integ([
        ("cash", "M-Pesa", "Record M-Pesa payments against bills, alongside cash, card and insurance."),
        ("shield", "SHA and insurance", "SHA and insurance numbers on patients and bills, with claim lists to follow up."),
        ("wa", "WhatsApp", "A daily summary for the owner, and suggested orders sent to suppliers."),
        ("print", "Printers and scanners", "Receipts, prescriptions, lab results and reports; 2D medicine-pack codes."),
        ("cloud", "Backups", "Backups you can restore, kept locally and online."),
        ("users", "Sales agents", f'Agents record clients from their phone and start their demos. Sign in at the <a href="{MEDICORE}/portal" target="_blank" rel="noopener">MediCore agent portal</a>.')]), tone="white")

    faqs = section(f'''<div class="split">{head("What facilities ask before they switch")}{faq([
        ("Do we need internet for MediCore to work?", "No. The installed system runs on your own computer and keeps working with no internet. When there is a connection it sends M-Pesa payment prompts, backs up and lets the owner check sales from elsewhere. The free online demo does need internet."),
        ("What does the 30-day demo include?", "A private online copy of MediCore, set up for your facility type and filled with sample data. If you buy, your demo becomes your live system and we install it at your facility."),
        ("Can we use the computers we already have?", "Yes. Any Windows computer with 4 GB of RAM or more will run it. We install it on your machines and connect your printer and scanner."),
        ("How long does it take to start?", "One day on site for most pharmacies and clinics: we install, import your item list and prices, set up staff PINs and train the team. Larger hospitals are planned department by department."),
        ("Is our data ours?", "Yes. It is stored on your facility computer, with backups you can restore. If a plan lapses, after a 7-day grace period the system becomes read-only: you can view and print everything, but new entries pause until the plan is renewed."),
        ("Does it handle SHA and insurance?", "MediCore records SHA and insurance numbers on patients and bills and produces claim lists. Direct electronic submission depends on certification and integration approvals; ask us for the current status before you buy."),
        ("Can the owner see several branches?", "Yes. Add branches of any type under one account. The owner sees all of them together or one at a time, and can move stock between them."),
    ])}</div>''')
    cta = lead_section("medicore", "Book a MediCore demo", "See MediCore with your own services", "Tell us about your facility and a time that suits you. We will show you MediCore at your premises or online.", ["Set up for your facility type", "Your services, departments and prices", "No obligation"])
    return page("medicore", hero + who + feats + day + screens + kit_s + dep + how + tryit + ints + pilots + faqs + cta)


# ============================================================== POS
POS_TYPES = [("duka", "Shop", "box"), ("minimart", "Supermarket", "cart"), ("hardware", "Hardware", "cog"), ("agrovet", "Agrovet", "spark"),
             ("pharmacy", "Chemist", "pill"), ("boutique", "Boutique", "star"), ("electronics", "Phones & electronics", "phone"), ("butchery", "Butchery", "scan"),
             ("bakery", "Bakery", "clock"), ("restaurant", "Restaurant", "users"), ("bar", "Bar", "cal"), ("salon", "Salon", "scissor"),
             ("wholesale", "Wholesale", "layers"), ("autospares", "Auto spares", "cog"), ("stationery", "Stationery & cyber", "print"), ("gas_water", "Gas & water", "battery")]


def pos():
    sw = "".join(f'<button type="button" data-type="{k}" aria-pressed="{"true" if n == 0 else "false"}">{ic(i)}{l}</button>' for n, (k, l, i) in enumerate(POS_TYPES))
    hero = f'''<section class="hero hero-pos t-paper" data-pos="{POS}"><div class="pos-dots" aria-hidden="true"></div><div class="wrap">
<div class="pos-head">{crumb(("Systems", "/products/"), "Pentarch POS")}<p class="hs-k">{ic("cart")}Pentarch POS · point of sale</p>
<h1>Sell, count stock and track credit, even when the internet is down.</h1>
<p class="hero-p">One till system for Kenyan shops, chemists, hardware stores, restaurants, bars and salons. M-Pesa, KRA tax codes and Kiswahili are built in. Try the real system below.</p>
<div class="btns"><a class="btn btn-p" href="#live-demo" data-act="start">{ic("play")}Try the live demo</a><a class="btn btn-d" href="{POS}?trial=1" data-link="trial" target="_blank" rel="noopener">Start the one-month free trial{ic("ne")}</a><a class="btn btn-g" href="#demo">Book a demo</a></div></div>
<div class="pos-demo" id="live-demo"><div class="pd-top"><p>Choose your type of business, then use the system as you would at the counter.</p><a href="{POS}?demo=1&amp;type=duka" data-link="full" target="_blank" rel="noopener">Open full-screen demo{ic("ne")}</a></div>
<div class="sw" role="group" aria-label="Business type">{sw}</div>
<div class="monitor"><div class="scr" id="pp-scr"><div class="pst">{pos_till()}</div>
<button type="button" class="pp-go" id="pp-go"><span class="pp-play">{ic("play")}</span><b>Start the live demo</b><small>The full system with a sample business. Everything stays in your browser.</small></button></div><div class="stand" aria-hidden="true"></div></div>
<ul class="pd-notes"><li>{ic("lock")}Sample data only, nothing is sent to us</li><li>{ic("users")}If the screen locks, use PIN Owner 1234 or Cashier 1111</li><li>{ic("layers")}Switch business type at any time</li></ul></div>
<ul class="pos-badges"><li>{ic("offline")}Works offline</li><li>{ic("cash")}M-Pesa</li><li>{ic("shield")}KRA tax codes</li><li>{ic("globe")}English and Kiswahili</li><li>{ic("pin")}Made in Nairobi</li></ul></div></section>'''

    biz = [("box", "Shop and duka", "duka", ["Quick keys for your fastest sellers", "Sell by piece or by carton", "Credit book for regular customers"]),
           ("cart", "Minimart and supermarket", "minimart", ["Scale barcodes for weighed items", "Loyalty points for customers", "Several tills and branches"]),
           ("cog", "Hardware and building", "hardware", ["Quotes and invoices for contractors", "Wholesale prices by quantity", "Units: piece, box, bundle, metre"]),
           ("spark", "Agrovet", "agrovet", ["Batch numbers and expiry dates", "Sell by sack, kg or packet", "Credit for farmers, with statements"]),
           ("pill", "Pharmacy and chemist", "pharmacy", ["First-expiry-first-out selling by batch", "Expiry tracker: 30, 60 and 90 days", "Loyalty points for regular patients"]),
           ("star", "Boutique, fashion and shoes", "boutique", ["Sizes and colours, each with its own barcode", "Print price labels for new stock", "Stock per size, so you know what to reorder"]),
           ("phone", "Phones and electronics", "electronics", ["Serial and IMEI captured at sale", "Quotes for corporate buyers", "Look up any serial to see when it was sold"]),
           ("scan", "Butchery", "butchery", ["Sell by kg, with decimals", "Reads barcodes from weighing scales", "Credit for hotels and regular buyers"]),
           ("users", "Restaurant, café and hotel", "restaurant", ["Tables, waiters and kitchen tickets", "Extras and notes on each dish", "Split bills, takeaway and delivery"]),
           ("cal", "Bar and liquor store", "bar", ["Open tabs per table, bar tickets", "Sell by bottle or by crate", "Every void and drawer opening recorded"]),
           ("scissor", "Salon, barber and spa", "salon", ["Services and products on one bill", "Stylist per service, commission report", "Loyalty points for regular clients"]),
           ("layers", "Wholesale and distribution", "wholesale", ["Wholesale and retail price tiers", "Cartons, bales and dozens", "Credit, statements and quotes"])]
    bz = "".join(f'<article class="bz">{ic(i)}<h3>{t}</h3>{ticks(pts)}<button type="button" class="bz-try" data-try="{k}">Try the {t.split(",")[0].split(" and ")[0].lower()} demo{ic("arrow")}</button></article>' for i, t, k, pts in biz)
    biz_s = section(head("Set up for the way your business sells", "Choose your business type and Pentarch POS switches on the right tools, categories and typical products. You can change any of it later.") +
                    f'<div class="bzg">{bz}</div><p class="small center">Also set up for bakeries, cosmetics shops, auto spares, stationery and cyber cafés, LPG gas and water refill, and service businesses.</p>', sid="types", tone="white")

    def till():
        return '''<div class="mk mk-rc" aria-hidden="true"><div class="rc-h"><b>NRB1-000214</b><span>Shift open</span></div><div class="rc-l"><span>Maize flour 2 kg</span><span>2 × 210</span><b>420</b></div><div class="rc-l"><span>Cooking oil 1 L</span><span>1 × 395</span><b>395</b></div><div class="rc-l"><span>Fresh milk 500 ml</span><span>3 × 65</span><b>195</b></div><div class="rc-t"><span>Total</span><b>KES 1,010</b></div><div class="rc-c"><small>M-Pesa code</small><b>TKB4R7QX2M</b><em>Checked</em></div></div>'''

    def stock():
        return '''<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Stock on hand</b><span>Main branch</span></div><div class="ml-r warn"><span>Sugar 1 kg</span><b>8 left</b></div><div class="ml-r"><span>Rice 5 kg</span><b>34</b></div><div class="ml-r"><span>Bar soap 800 g</span><b>120</b></div><div class="ml-r exp"><span>Yoghurt 500 ml</span><b>Expires in 9 days</b></div><div class="ml-f">3 items below reorder level</div></div>'''

    def credit():
        return '''<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Wanjiru M.</b><span>0712 ··· 456</span></div><div class="ml-r"><span>Balance owed</span><b>4,850</b></div><div class="ml-r"><span>Credit limit</span><b>10,000</b></div><div class="age"><i style="--w:55%">0–30</i><i style="--w:25%">31–60</i><i style="--w:15%">61–90</i><i style="--w:5%">90+</i></div><div class="ml-f">WhatsApp reminder ready</div></div>'''

    def log():
        return '''<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Activity log</b><span>Today</span></div><div class="ml-r"><span>10:42 Sale voided, approved with manager PIN</span></div><div class="ml-r"><span>11:05 Price changed · Sugar 1 kg · 160 to 150</span></div><div class="ml-r warn"><span>11:20 Drawer opened, no sale</span></div><div class="ml-f">Shift close · variance −150</div></div>'''

    def rep():
        bars = "".join(f'<i style="--h:{h}%"></i>' for h in [22, 35, 48, 62, 55, 40, 58, 74, 90, 68, 44, 30])
        return f'<div class="mk mk-rep" aria-hidden="true"><div class="ml-h"><b>Sales today</b><span>+12% on last week</span></div><div class="rp-k"><div><small>Sales</small><b>48,620</b></div><div><small>Gross profit</small><b>9,870</b></div></div><div class="qd-chart">{bars}</div></div>'

    def branches():
        return '''<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Branches · today</b><span>All synced</span></div><div class="ml-r"><span>Thika Road · 2 tills</span><b>62,300</b></div><div class="ml-r"><span>CBD · 1 till</span><b>48,950</b></div><div class="ml-r"><span>Ruiru · 1 till</span><b>21,400</b></div><div class="ml-f">Transfer: 20 × Cooking oil 1 L, CBD to Ruiru · Sent</div></div>'''

    def sync():
        return f'''<div class="mk mk-sync" aria-hidden="true"><div class="sy s1">{ic("offline")}<b>Internet down</b><small>Selling continues · 6 waiting</small></div><div class="sy s2">{ic("wifi")}<b>Connection back</b><small>6 sales uploaded</small></div><div class="sy s3">{ic("phone")}<b>Owner's phone</b><small>Same figures, up to date</small></div></div>'''

    def labels():
        return '''<div class="mk mk-lab" aria-hidden="true"><div class="lbl"><b>Ankara dress · Size M</b><span>KES 2,450</span><i class="bars"></i><small>2000012345675</small></div><div class="lbl-sz"><span>38 × 25 mm</span><span class="on">40 × 30 mm</span><span>50 × 25 mm</span><span>A4 sheet</span></div></div>'''

    T = [("sell", "Selling", "cart", feat_panel("Fast selling at the counter", "Scan, search or tap a quick key. A sale is saved in a fraction of a second, with or without internet.",
          ["Cash, M-Pesa, card, bank and credit, or a mix of them", "M-Pesa codes checked for format and flagged if used before", "Hold a sale, serve the next customer, recall it later", "Receipts printed, or sent on WhatsApp", "Returns and refunds with the original receipt"], till())),
         ("stock", "Stock", "box", feat_panel("Stock you can trust", "Every item in and out is recorded with who did it and why, so stock on hand is always explained.",
          ["Receive goods from suppliers, with or without an order", "Low-stock list and reorder suggestions", "Stock take by scanning, with a variance report", "Batches and expiry dates, damaged and expired write-offs", "Repack bulk items, for example a 50 kg sack into 1 kg packets"], stock())),
         ("credit", "Customers and credit", "users", feat_panel("Customers and credit, without the lost book", "Sell on account with a credit limit, then see exactly who owes what and for how long.",
          ["Find a customer by phone number in seconds", "Payments applied to the oldest debt first", "Statements and polite reminders by WhatsApp", "Debt age: 0–30, 31–60, 61–90 and over 90 days", "Loyalty points and wholesale customer groups"], credit())),
         ("staff", "Staff and theft control", "lock", feat_panel("Staff accounts and theft control", "Each person signs in with their own PIN and sees only what their role allows. Sensitive actions need a manager's PIN.",
          ["Roles: owner, manager, cashier, waiter, stock clerk, accountant", "Voids, discounts, price changes and drawer openings logged", "Discount limit per staff member", "Shift close: expected against counted cash, by note and coin", "Screen locks itself when the till is left alone"], log())),
         ("reports", "Reports", "chart", feat_panel("Reports that answer real questions", "See today against yesterday and last week, which items make money, and where the cash went.",
          ["Sales by item, category, staff, hour and payment method", "Profit and margin, expenses, profit and loss", "VAT report by KRA tax code", "Slow and dead stock, debtors and supplier balances", "Print or export any report to Excel (CSV)"], rep())),
         ("branches", "Branches", "layers", feat_panel("More than one branch", "Run every branch from one account. Each branch sells on its own, and the owner sees them all together.",
          ["Branch comparison on the dashboard", "Stock transfers, sent and received with checks", "Different prices per branch where needed", "Staff limited to the branches they work in"], branches())),
         ("offline", "Offline and sync", "offline", feat_panel("Works offline, syncs when it can", "The system runs on the computer itself, so a dropped connection or a finished bundle does not stop sales.",
          ["Sell, print receipts and check stock with no internet", "Sales wait safely on the till and upload on reconnect", "Cloud backup of all your records", "Download a full backup or export to CSV at any time"], sync())),
         ("labels", "Barcodes and labels", "scan", feat_panel("Barcodes and price labels", "Use the barcodes already on your goods, or create your own for loose items and print labels.",
          ["Scan from anywhere on the screen, no clicking first", "Generate barcodes for items that have none", "Labels for label printers or A4 sticker sheets", "Carton barcodes sell the full pack at the carton price"], labels()))]
    feats = section(head("Everything the counter needs, in one place", "From the first sale of the morning to the cash count at night.") + tabs("pos", T), sid="features")

    how = section(head("From first look to first sale") + steps([
        ("Try the demo", "Use the live demo above with a sample business like yours. No sign-up needed."),
        ("One month free", "Start the full system on your own computer with your own products. No payment needed."),
        ("We install and train", "We set up the devices, load your products and train your staff at your business."),
        ("Start selling", "Sell from day one, with WhatsApp support from our Nairobi team when you need it."),
    ]), tone="white")

    hw = [("monitor", "Computer", "HP EliteDesk 800 G2 Mini", "Refurbished. Core i5, 8 GB RAM, 256 GB SSD, Windows Pro. Small, quiet, low power."),
          ("monitor", "Screen", "HP 19-inch monitor", "Refurbished, P19b or EliteDisplay class."),
          ("scan", "Scanner", "Syble XB-6221 2D", "Reads barcodes, QR codes and codes on phone screens."),
          ("print", "Receipt printer", "Xprinter XP-Q80A", "80 mm thermal printer with auto-cutter, USB and network."),
          ("cash", "Cash drawer", "OCOM ECD-420X", "Metal, 5 note and 8 coin slots. Opens on cash sales."),
          ("battery", "Backup power", "Mercury Elite 650 Pro UPS", "Keeps the till running about 15 to 20 minutes in a blackout and protects against surges.")]
    h = "".join(f'<li>{ic(i)}<p class="mono">{k}</p><h3>{t}</h3><p>{d}</p></li>' for i, k, t, d in hw)
    hw_s = section(f'''<div class="split">{head("The Complete Till", "Buy the whole counter from us, installed and tested, or use your own Windows computer with Google Chrome. Spare parts and paper are easy to find in Nairobi.")}
<div class="iso" aria-hidden="true"><div class="iso-desk"><span class="iso-mon"></span><span class="iso-pc"></span><span class="iso-prn"></span><span class="iso-drw"></span><span class="iso-scn"></span></div></div></div>
<ul class="hw">{h}</ul><p class="small">Devices tested before delivery. 6 to 12 month warranty, claims handled by Pentarch. Installed at your business in Nairobi. You receive a written quote after the demo.</p>''', tone="ink", cls="sec-hw")

    rows = [("Today's sales and profit", "Added up at night, if at all", "Sales totals", "Live sales and profit, compared with last week"),
            ("Stock on hand", "Only after a manual count", "Yes", "Yes, with expiry dates and reorder suggestions"),
            ("Who owes you money", "Credit book, easy to lose", "Often limited", "Limits, statements, debt age, WhatsApp reminders"),
            ("Voids, discounts and drawer openings", "Not recorded", "Varies", "Every action logged with the staff name"),
            ("Works without internet", "Yes", "Often needs a connection", "Yes, fully, and syncs later"),
            ("M-Pesa payments", "Written by hand", "Varies", "Code checked, repeated codes flagged"),
            ("Language", "Any", "Usually English only", "English and Kiswahili"),
            ("Try before you pay", "Not applicable", "Sometimes", "Live demo and one month free"),
            ("Setup and support", "None", "Varies", "Installed, trained and supported from Nairobi")]
    tb = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td class="hl">{d}</td></tr>' for a, b, c, d in rows)
    cmp_s = section(head("Paper book, a typical POS, or Pentarch POS") + f'<div class="tbl-wrap" tabindex="0" role="region" aria-label="Comparison"><table class="tbl tbl-cmp"><thead><tr><td></td><th scope="col">Paper book</th><th scope="col">Typical POS</th><th scope="col">Pentarch POS</th></tr></thead><tbody>{tb}</tbody></table></div>', tone="white")

    ints = section(head("Built for how Kenya pays and reports") + integ([
        ("cash", "M-Pesa", "Codes recorded with each sale, checked for format and flagged if repeated. A payment request to the customer's phone can be set up on request."),
        ("shield", "KRA tax codes", "Your KRA PIN and the tax code for every item (A to E) on receipts, and a VAT report by code. eTIMS integration is on the way."),
        ("wa", "WhatsApp", "Receipts, statements and debt reminders sent to the customer's WhatsApp."),
        ("globe", "English and Kiswahili", "Every screen in both languages, switchable per user."),
        ("cloud", "Cloud backup", "Records backed up to the Pentarch cloud, separate from every other business."),
        ("users", "Sales agents", f'Agents register and follow their clients in the <a href="{POS}agents/" target="_blank" rel="noopener">POS agent portal</a>.')]))

    faqs = section(f'''<div class="split">{head("Frequently asked questions")}{faq([
        ("Does it really work without internet?", "Yes. Selling, receipts, stock and reports all work offline because the system runs on your computer. Sales are kept safely on the till and upload to your cloud backup as soon as the connection returns."),
        ("How much internet does it use?", "Very little. Syncing sends small text records, not pictures or video, so an ordinary data bundle or home Wi-Fi is enough. Internet is only needed for backup, sync between devices and branches, and updates."),
        ("Is my data safe, and who owns it?", "Your data belongs to you. It is stored on your till and backed up to the Pentarch cloud, separated from every other business. You can download a full backup or export everything to CSV at any time."),
        ("Is it KRA eTIMS compliant?", "Receipts already carry your KRA PIN and the KRA tax code for every item (A to E), and the VAT report groups sales by tax code. eTIMS integration is on the way. We will tell every client when it is available and switch it on for you."),
        ("What happens when the free month ends?", "Choose a plan and pay by M-Pesa Paybill. Nothing is charged automatically and everything you entered stays. If you do not continue, you can still view and export your records."),
        ("Can I run more than one branch?", "Yes. You get branch comparison, stock transfers between branches and per-branch prices, all under one account."),
        ("Can I use my own computer?", "Yes. You need a Windows PC or laptop with a Core i3 processor or better, 4 GB RAM and Google Chrome. USB barcode scanners and 58 mm or 80 mm thermal receipt printers work with it."),
        ("What support do I get?", f"WhatsApp and phone support from our Nairobi team, Monday to Saturday, 8am to 6pm, on {PHONE}. Updates are included."),
    ])}</div>''')
    cta = lead_section("pos", "Book my demo", "See it working in your business", "Tell us about your business and a convenient time. We will call to confirm, then show you the system at your premises or online.", ["A demo set up for your type of business", "Honest advice on the right devices", "A written quote after the demo"])
    return page("pos", hero + biz_s + feats + how + hw_s + cmp_s + ints + faqs + cta)
