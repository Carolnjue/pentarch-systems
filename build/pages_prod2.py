from lib import *
from mocks import *
from pages_prod import gallery, integ

GV = "https://glamourvinecollege.com"


# ============================================================== PORTAL
GVU = "glamourvinecollege.com/portal"

PORTAL_JOURNEY = [
    ("school", "Applies online", ["Applicant", "Office"], "She applies from the college website and uploads her documents. The application lands in the admissions queue for the office to review and send an offer.",
     ("portal-admissions", "Admissions queue in the Pentarch Portal", GVU + "/admissions"), None),
    ("users", "Is admitted", ["Office"], "Accepting the offer turns the applicant into a student, with an admission number, a class and her own sign-in.",
     ("portal-students", "Student list in the Pentarch Portal", GVU + "/students"), ("portal-stu-dashboard", "The new student's own dashboard", GVU + "/dashboard")),
    ("cash", "Pays fees", ["Student", "Office"], "She sees her balance, invoices and the M-Pesa Pay Bill details. The office sees every payment against her record.",
     ("portal-stu-fees", "The student's fees page with M-Pesa details", GVU + "/fees"), ("portal-fees", "Fees and payments for the office", GVU + "/finance")),
    ("cal", "Joins a class", ["Office", "Student"], "Classes run by intake. Orientation opens first, then the units of her course unlock in order.",
     ("portal-classes", "Classes by intake", GVU + "/academics/cohorts"), ("portal-stu-courses", "The student's courses, starting with orientation", GVU + "/learn")),
    ("book", "Learns online", ["Trainer", "Student"], "Trainers publish modules and lessons. She reads, watches and checks her understanding, with her progress shown as she goes.",
     ("portal-stu-lesson", "A lesson from the student view", GVU + "/learn/lesson"), ("portal-lms-modules", "Modules from the trainer view", GVU + "/learn/modules")),
    ("pen", "Sits CATs and exams", ["Student", "Trainer"], "Quizzes, CATs and exams open in the portal, drawing questions from the unit question bank.",
     ("portal-lms-assessments", "Assessments for a unit", GVU + "/learn/assessments"), ("portal-question-bank", "The question bank", GVU + "/question-bank")),
    ("chart", "Gets her marks", ["Trainer", "Student"], "CAT and exam marks are weighted into a final result. Results stay provisional until the school approves them.",
     ("portal-gradebook", "The trainer gradebook", GVU + "/lms/gradebook"), ("portal-gk-grades", "A graduating student's approved results", GVU + "/grades")),
    ("check", "Proves her practical skills", ["Student", "Trainer"], "She logs each practical with a photo. Her trainer checks the evidence and signs it competent or sends it back.",
     ("portal-tr-logbook", "Logbook sign-off for trainers", GVU + "/logbook/review"), ("portal-gk-logbook", "The student's logbook", GVU + "/logbook")),
    ("star", "Graduates", ["Director"], "The school approves graduands, prints the list and holds the ceremony.",
     ("portal-ceremony", "A graduation ceremony in the portal", GVU + "/graduation"), None),
    ("school", "Receives her certificate", ["Graduate"], "Printed or saved as a PDF, with the official seal, both signatures, a serial number and a QR verification code, plus a full academic transcript.",
     ("portal-gk-cert-full", "A certificate of completion issued from the Pentarch Portal", None), ("portal-gk-certificates", "The graduate's certificates page with her verification link", GVU + "/my-certificates")),
    ("shield", "Is verified by an employer", ["Employer"], "Anyone can scan the QR code or open the link to confirm the certificate is genuine.",
     ("portal-gk-verify", "A genuine certificate on the public verification page", GVU + "/verify"), None),
    ("handshake", "Joins the alumni", ["Graduate", "Office"], "Graduates stay on the alumni list for job referrals, salon placements and events.",
     ("portal-alumni", "The alumni list", GVU + "/graduation/alumni"), None),
]


def roles_grid(items):
    return '<div class="rgrid">' + "".join(f'<div class="rg">{ic(i)}<h3>{t}</h3>{ticks(pts)}</div>' for i, t, pts in items) + "</div>"


def portal():
    hero = f'''<section class="hero hero-portal t-ink"><div class="hero-grid" aria-hidden="true"></div><div class="wrap hero-2">
<div class="hp-txt">{crumb(("Products", "/products/"), "Portal")}<p class="hs-k">{ic("school")}Pentarch Portal · college management</p>
<h1>One record for each student, from the first application to the alumni list.</h1>
<p class="hero-p">A complete management portal for schools, colleges and training centres, running inside your own website. Applicants become students the moment their admission fee is confirmed, and everyone gets a dashboard that fits their role.</p>
<div class="btns">{btn("#demo", "Book a Portal demo", "p", "arrow")}{btn("#journey", "Follow a student through it", "g")}</div>
<ul class="hero-facts"><li>{ic("pin")}Live at a college in Machakos</li><li>{ic("users")}A dashboard for every role</li><li>{ic("web")}Runs inside your WordPress website</li></ul></div>
<div class="hp-shots">{shot("portal-dashboard", "The Pentarch Portal admin dashboard at Glamourvine Hair & Beauty College", "shot-a", GVU + "/dashboard")}{shot("portal-cert-full", "A Pentarch Portal certificate with its verification code", "shot-b")}</div></div></section>'''

    T = [("adm", "Admissions and fees", "users", feat_panel("Applications that become students",
            "Applications come in from your website with documents attached. Admission numbers and sign-ins are issued once the admission fee is confirmed against M-Pesa.",
            ["Online application with documents", "Review, offer and activation by the college", "Admission numbers for sign-in", "Fees, receipts and statements, confirmed by M-Pesa"],
            shot("portal-admissions", "Portal admissions screen", "shot-n"))),
         ("lms", "Teaching and LMS", "book", feat_panel("Online learning inside the same portal",
            "Modules and lessons for each unit, with quizzes, CATs and exams drawn from a shared question bank.",
            ["Courses, classes by intake and modules", "Quizzes, CATs and exams", "Question bank for trainers", "Timetables, attendance and printable ID cards"],
            shot("portal-lms-modules", "Portal LMS modules", "shot-n"))),
         ("grades", "Marking and gradebook", "chart", feat_panel("Marks in one gradebook",
            "Online work is marked automatically, essays queue for the trainer, and the gradebook weights CATs and exams into a final result.",
            ["Automatic marking of online work", "Essays queued for the trainer", "Weighted CAT and exam results", "Results approved by the school before release"],
            shot("portal-gradebook", "Portal gradebook", "shot-n"))),
         ("log", "Practical logbook", "check", feat_panel("Practical skills, with evidence",
            "Students record practicals with photo evidence, and trainers sign each one as competent or send it back.",
            ["Photo evidence for each practical", "Sign-off by the trainer", "Competent or sent back, with a note", "A complete logbook at graduation"],
            shot("portal-logbook", "Portal practical logbook", "shot-n"))),
         ("life", "Hostel, store and notices", "bed", feat_panel("The rest of college life",
            "Hostel rooms and beds, a store for class materials, and notices to students and staff.",
            ["Hostel rooms, beds and requests", "One store for the school and the salon", "Low-stock alerts", "Notices to everyone, students or staff"],
            shot("portal-hostel", "Portal hostel board", "shot-n"))),
         ("grad", "Graduation and certificates", "star", feat_panel("Certificates anyone can check",
            "Approve graduands, print the list, hold the ceremony and print certificates with serial numbers and an online verification code.",
            ["Graduation list and ceremony", "Certificate printing with a QR code", "Certificate register: issued, collected or revoked", "Online check: is this certificate genuine?"],
            shot("portal-verify-genuine", "Portal certificate verification result", "shot-n"))),
         ("alumni", "Alumni", "handshake", feat_panel("Graduates stay connected",
            "Graduates move to an alumni list you can use for job referrals, placements and events.",
            ["Alumni records", "Course and year of graduation", "Job referrals and placements", "Kept in the same portal"],
            shot("portal-alumni", "Portal alumni screen", "shot-n")))]
    feats = section(head("Every office in the college, on one record", "Admissions, finance, teaching, the hostel and the students themselves work from the same information, so nobody re-types a name or chases a receipt.") + tabs("pt", T), sid="features", tone="white")

    jr = section(head("From application to alumni", "A student's path through the Portal at Glamourvine Hair & Beauty College, with the screens each person sees along the way.", "the journey") +
                 journey_tour("pj", PORTAL_JOURNEY), sid="journey", cls="sec-jr")

    pins = [(31, 44, "Graduate's name and award, with the classification"), (24, 76, "Signed by the Principal and the Director"), (55, 70, "Official college seal"),
            (13, 92, "Unique serial and admission numbers"), (88, 84, "QR code and link to the verification page")]
    pn = "".join(f'<span class="pin" style="left:{x}%;top:{y}%" aria-hidden="true"><b>{k}</b><em>{t}</em></span>' for k, (x, y, t) in enumerate(pins, 1))
    keys = "".join(f"<li><b>{k}</b><span>{t}</span></li>" for k, t in enumerate(["Name, award and classification", "Principal's and Director's signatures", "Official college seal", "Serial and admission numbers", "QR code for instant verification"], 1))
    cert = section(f'''{head("A certificate employers can check in seconds", "Every certificate the Portal issues carries its own proof. Here is a real one, as the graduate prints it.", "the certificate")}
<div class="cert-show"><figure class="cert-main">{img("portal-cert-full", "A Diploma in Beauty Therapy certificate issued by Glamourvine Hair & Beauty College from the Pentarch Portal")}{pn}</figure>
<div class="cert-side"><ol class="cert-keys">{keys}</ol>
<figure class="paper">{img("portal-transcript", "The academic transcript with CAT, exam and final marks for every unit")}<figcaption>The transcript lists every unit with CAT, exam and final marks.</figcaption></figure></div></div>
<div class="cert-verify"><h3>Is this certificate genuine?</h3>{steps([("Scan the QR code", "Every certificate printed from the Portal carries its own QR code."), ("Open the verification page", "The code opens the college's verification page for that certificate."), ("See the record", "The page confirms the graduate, course and date as recorded by the college.")], "steps steps-3")}
<div class="btns">{btn(GV + "/portal/verify", "Try the verification page", "p", "ne", True)}</div></div>''', sid="certificate", tone="ink", cls="sec-cert")

    student = section(head("What a new student sees when she signs in", "A Diploma in Beauty Therapy student in her first month, on her own account.", "the student's view") + tour("ps", [
        ("portal-stu-dashboard", "Her own dashboard", "Admission number, course and class, and the next lesson waiting for her.", GVU + "/dashboard"),
        ("portal-stu-courses", "My courses", "Orientation first, then the units of her diploma open in order.", GVU + "/learn"),
        ("portal-stu-lesson", "Lessons", "Readings, videos and quick checks, with an outline showing her progress.", GVU + "/learn/lesson"),
        ("portal-stu-grades", "Grades", "CATs, exams and final results for every unit, provisional until the school approves them.", GVU + "/grades"),
        ("portal-stu-fees", "Fees", "Balance, invoices, M-Pesa Pay Bill details and a printable statement.", GVU + "/fees"),
        ("portal-stu-logbook", "Practical logbook", "She logs each practical with a photo and her trainer signs it off.", GVU + "/logbook")]), sid="student", tone="white")
    trainer = section(head("Teaching, signing off, and the certificate at the end", "The same portal from a trainer's sign-in, and from a student who has finished her course.", "trainers and graduates") + tour("pt2", [
        ("portal-tr-dashboard", "A trainer's dashboard", "Work to mark, her units, assessments coming up and her salon portfolio, in one place.", GVU + "/dashboard"),
        ("portal-tr-teaching", "Teaching", "Each unit with its modules, question bank and classes, with marks and registers a click away.", GVU + "/teaching"),
        ("portal-tr-logbook", "Logbook sign-off", "She checks each student's practical evidence and signs it competent or sends it back.", GVU + "/logbook/review"),
        ("portal-gk-grades", "A graduate's results", "Every unit competent and approved, with her overall average and classification.", GVU + "/grades"),
        ("portal-gk-logbook", "A graduate's logbook", "Every practical task signed competent, with the trainer and date on each one.", GVU + "/logbook"),
        ("portal-gk-certificates", "A graduate's certificates", "Her certificate, transcript and a verification link she can share with employers.", GVU + "/my-certificates")], "tour-d"), sid="trainer", tone="ink2")

    office = section(head("The rest of the office, too", "Screens from the college office, shown as they run at Glamourvine.") + gallery([
        ("portal-reports", "Reports", "How admissions, fees, attendance and results are going."), ("portal-certificates", "Certificate register", "Every certificate issued, collected or revoked."),
        ("portal-courses", "Courses and units", "Programmes, units and fees set up by the college."), ("portal-store", "Store", "One stock for the school and the salon, with low-stock alerts."),
        ("portal-notices", "Notices", "Announcements to everyone, students or staff."), ("portal-teaching", "Teaching schedule", "Who teaches which unit, and when."),
        ("portal-graduation", "Graduation", "Graduands approved and the list printed."), ("portal-cert-print", "Certificate printing", "Certificates printed with serial numbers and QR codes."),
        ("portal-cert-record", "Certificate record", "One certificate, with its history and verification link.")]), cls="sec-gal")

    roles = section(head("Each person sees exactly what they need", "Four kinds of dashboard, one record underneath.", "dashboards by role") + roles_grid([
        ("cog", "Principal and admin", ["Dashboard of the whole college", "Admissions and student records", "Graduation and certificates", "Reports and an audit log"]),
        ("cash", "Finance and office", ["Fees, M-Pesa and receipts", "Balances by class", "Hostel and store", "Notices"]),
        ("book", "Trainers", ["Modules, lessons and quizzes", "Marking and the gradebook", "Attendance registers", "Logbook sign-off"]),
        ("users", "Students", ["Lessons and assessments", "Results and fee statements", "Practical logbook with photos", "Certificate and alumni record"])]), tone="white")

    story = section(f'''<div class="split">{head("In use at Glamourvine Hair & Beauty College, Machakos", "The Pentarch Portal replaced a generic learning system at Glamourvine. Applications, admissions, fees and practical work now run inside the college website, and the college salon runs on Pentarch BeautySuite alongside it.", "in use")}
<div class="also-po"><div class="ap">{ic("scissor")}<div><h3>The college salon</h3><p>Glamour by Beth runs on Pentarch BeautySuite, sharing one store with the college.</p><a href="/beautysuite/">See BeautySuite</a></div></div>
<div class="ap">{ic("handshake")}<div><h3>Scholarship programmes</h3><p>Charities that sponsor students use Pentarch EduSponsor, in use at SAM Elimu Charity.</p><a href="/ngo-portal/">See Pentarch EduSponsor</a></div></div>
<div class="btns">{btn(GV + "/", "Visit glamourvinecollege.com", "d", "ne", True)}</div></div></div>''', tone="ink", cls="sec-story")

    how = section(head("Setting up your college") + steps([
        ("Demo", "We show the Portal set up with your courses and fee structure."),
        ("Install", "The plugin goes on your college website. We can build the website too."),
        ("Load your college", "Courses, classes, trainers and current students are imported from your spreadsheets."),
        ("Train and run", "Staff are trained by role; students sign in with their admission number."),
    ]))
    faqs = section(f'''<div class="split">{head("What schools ask")}{faq([
        ("Do we need a new website?", "No. The Portal runs inside a WordPress website. If your current site is WordPress we add it there; if not, we can build or move your site at the same time, with Live Edit inside."),
        ("Can it fit a school, not only a college?", "Yes. Terms, classes, units and fees are configured for your institution, whether a school, college, TVET or training centre."),
        ("How do students sign in?", "With the admission number the college issues on activation. New applicants register online."),
        ("Can parents or sponsors pay fees?", "Yes. Fees can be paid by M-Pesa by anyone, and the payment is matched to the student's record and statement."),
        ("Can we bring our existing student records?", "Yes. We import students, classes and balances from spreadsheets so you start with a complete record."),
        ("Can we use our own certificate design?", "Yes. The certificate is designed for your college, with the verification QR code added."),
    ])}</div>''', tone="white")
    cta = lead_section("portal", "Book a Portal demo", "See the Portal with your courses", "Tell us about your college. We will show you the Portal with your own courses and fees.", ["Set up for your courses and intakes", "Works on your college website", "No obligation"])
    return page("portal", hero + jr + cert + roles + office + story + how + faqs + cta)


# ============================================================== BEAUTYSUITE
GBU = "glamourvinecollege.com"
SALON_JOURNEY = [
    ("globe", "Books online", ["Client"], "Clients browse services and stylists on the salon website and send a booking request, or book a stylist by name from her own page.",
     ("glamour-salon", "The salon website with online booking", GBU + "/salon"), ("salon-artist-page", "A stylist's page on the salon website", GBU + "/salon/artist")),
    ("cal", "Reception books it in", ["Receptionist"], "Walk-ins, calls, WhatsApp and website requests land in one bookings list, bridal parties included. Existing clients pop up as she types, and the quote and deposit fill in from the price list.",
     ("salon-bookings", "Bookings, including bridal parties with deposits", GBU + "/salon-desk/bookings"), ("salon-new-booking", "The new booking form", GBU + "/salon-desk/bookings/new")),
    ("clock", "The day on one calendar", ["Receptionist", "Stylists"], "Every stylist's bookings sit side by side, so reception can see who is free at a glance.",
     ("salon-calendar", "The salon calendar", GBU + "/salon-desk/calendar"), ("salon-desk", "The front desk today", GBU + "/salon-desk")),
    ("scissor", "The stylist logs the work", ["Stylist"], "Each stylist logs her session with photos from her own sign-in. Her portfolio builds itself as she goes.",
     ("salon-my-work", "A stylist's work log", GBU + "/salon-desk/my-work"), ("salon-my-portfolio", "A stylist's portfolio", GBU + "/salon-desk/portfolio")),
    ("cash", "Checkout", ["Receptionist", "Client"], "Services and products go on one bill, paid by cash, M-Pesa, card or voucher, or left as a balance for later.",
     ("salon-checkout", "Checkout at reception", GBU + "/salon-desk/checkout"), None),
    ("star", "Clients come back", ["Receptionist", "Client"], "Every visit builds the client record: visits, spending, loyalty points and birthdays, with one tap to WhatsApp or book her again.",
     ("salon-clients", "Client records with visits, spending and loyalty points", GBU + "/salon-desk/clients"), None),
    ("box", "Stock looks after itself", ["Storekeeper"], "Retail and back-bar products are tracked with stock value and reorder levels, so low stock shows up before it runs out.",
     ("salon-stock", "Products and stock", GBU + "/salon-desk/stock"), None),
    ("users", "Commissions add up", ["Manager", "Stylists"], "Each stylist's share is calculated from the jobs she did, even on shared bridal bookings.",
     ("salon-commissions", "Staff and commissions", GBU + "/salon-desk/staff"), None),
    ("check", "The day is closed", ["Receptionist"], "At closing, takings are counted by cash, M-Pesa, card and other payments against the cash drawer.",
     ("salon-day-close", "Day close", GBU + "/salon-desk/day-close"), None),
    ("chart", "The owner sees the numbers", ["Owner"], "Revenue, expenses, clients served and the no-show rate for any period.",
     ("salon-reports", "Salon reports", GBU + "/salon-desk/reports"), None),
]


def bridal_mock():
    rows = [("Bride: hair and veil", "Lead stylist"), ("Bride: make-up", "Make-up artist"), ("Bridesmaids × 3: braids", "Two stylists"), ("Nails for the party", "Nail technician")]
    r = "".join(f'<div class="ml-r"><span>{a}</span><b>{b}</b></div>' for a, b in rows)
    return (f'<div class="mk mk-list mk-bridal" aria-hidden="true"><div class="ml-h"><b>Bridal package</b><span>07:00 · on location · 4 staff</span></div>{r}'
            f'<div class="ml-f">Each stylist&#8217;s share is recorded at checkout</div></div>')


def beautysuite():
    hero = f'''<section class="hero hero-salon t-white"><div class="sal-art" aria-hidden="true">{circuit(31, 1200, 600, 14, 40, 0)}</div><div class="wrap hero-2">
<div>{crumb(("Products", "/products/"), "BeautySuite")}<p class="hs-k">{ic("scissor")}Pentarch BeautySuite · salons and spas</p>
<h1>The front desk, the bookings and fair commissions, on one screen.</h1>
<p class="hero-p">Front desk, online booking, payments and staff commissions in one system for salons, spas and barbershops. Built with a busy bridal salon, so it handles real days like a four-stylist wedding package before breakfast.</p>
<div class="btns">{btn("#demo", "Book a BeautySuite demo", "p", "arrow")}{btn("#journey", "Follow a client's visit", "g")}</div>
<p class="small hero-note">Live for Glamour by Beth, the salon that owns Glamourvine Hair &amp; Beauty College.</p></div>
<div class="sal-vis">{duo("salon-desk", "BeautySuite front desk at Glamour by Beth", "salon-calendar", "BeautySuite bookings calendar")}</div></div></section>'''

    f = [("cal", "Bookings and walk-ins", "Online booking from your website and a front-desk diary for walk-ins, calls and WhatsApp."),
         ("star", "Services and packages", "Services, prices and packages, including bridal teams with several stylists on one booking."),
         ("cash", "Payments and takings", "Cash, M-Pesa, card or voucher on each bill, with a day close against the cash drawer."),
         ("users", "Fair commissions", "Each stylist's share calculated from the jobs she did, even on shared bookings."),
         ("layers", "Photos and portfolios", "Session photos saved to the client record and to each stylist's portfolio."),
         ("handshake", "Clients who come back", "Visits, spending, loyalty points and birthdays, with one tap to WhatsApp."),
         ("box", "Stock and back bar", "Retail and back-bar products with stock value and reorder levels."),
         ("school", "Salon and college together", "Runs alongside the Pentarch Portal, so a beauty college and its training salon share one system.")]
    fs = "".join(f'<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in f)
    feats = section(head("Run the salon floor without the notebook", "Reception logs every job as it happens, so takings, stock and each stylist's pay add up at the end of the day.") + f'<ul class="caps">{fs}</ul>', sid="features")

    jr = section(head("A client's visit, from booking to day close", "Real screens from Glamour by Beth, as the client, the receptionist, the stylist and the owner see them.", "the journey") +
                 journey_tour("bj", SALON_JOURNEY), sid="journey", tone="white", cls="sec-jr")

    comm = section(f'''<div class="split">{head("No more end-of-month arguments", "Every job is logged by reception with who did what. BeautySuite applies your commission rules and shows each stylist her own total, so pay day is quick and fair.", "commissions")}
<div>{ticks(["A team of stylists on one bridal booking, each on the right part of the job", "Commission per service or per stylist, as your salon pays", "Each stylist sees her own work and earnings", "Clear figures for the period at pay time"])}
{bridal_mock()}</div></div>''', tone="ink", cls="sec-comm")

    live = section(f'''<div class="split">{head("Built with a salon: Glamour by Beth", "BeautySuite was built with Glamour by Beth Salon &amp; Spa, the salon behind Glamourvine Hair &amp; Beauty College in Machakos, where students also practise on real clients in supervised sessions. It is now available to other salons, spas and barbershops.", "in use")}
<figure class="live-fig">{shot("salon-services", "BeautySuite services and price list at Glamour by Beth", "shot-n")}<figcaption>Services and prices, set up by the salon.</figcaption></figure></div>''', tone="paper")
    pair = section(f'''<div class="split">{head("BeautySuite or Pentarch POS?", "Both handle salons. Choose by how your business earns.")}
<div class="vs"><div><h3>{ic("scissor")}BeautySuite</h3>{ticks(["Most income comes from bookings and services", "Bridal and event packages", "Teams of stylists per client"])}</div><div><h3>{ic("cart")}Pentarch POS, salon type</h3>{ticks(["Many product sales as well as services", "Stylist per service and commission report", "Needs to sell offline at the counter"])}{btn("/pos/", "See Pentarch POS", "d", "arrow")}</div></div></div>''', tone="white")
    faqs = section(f'''<div class="split">{head("Questions about BeautySuite")}{faq([
        ("Which devices does it run on?", "The desk computer, a tablet at the stations and phones. It runs in the browser."),
        ("Can clients book themselves?", "Yes. Clients send booking requests from your salon website, or book a stylist from her own page. Reception confirms them on the desk."),
        ("Can it handle a training salon?", "Yes. It was built for a salon that is also a training floor for a beauty college, and runs alongside the Pentarch Portal."),
        ("Can we take deposits for bridal bookings?", "Yes. The quote and deposit fill in from your price list when the booking is made, and the balance is settled at checkout."),
    ])}</div>''')
    cta = lead_section("beautysuite", "Book a BeautySuite demo", "See BeautySuite on your salon floor", "Tell us how many stylists you have and how you take bookings today.", ["Set up with your services", "Your commission rules", "No obligation"])
    return page("beautysuite", hero + jr + comm + live + pair + faqs + cta)


# ============================================================== LEARNING
def learning():
    schools = [("Creative Media", 7), ("Digital and Tech", 11), ("Research, Data and Impact", 9), ("Communication and Public Relations", 5), ("Training of Trainers", 1)]
    sc = "".join(f'<li><b>{n}</b><span>{s}</span><i style="--w:{n / 11 * 100:.0f}%"></i></li>' for s, n in schools)
    hero = f'''<section class="hero hero-learn t-ink"><div class="hero-grid" aria-hidden="true"></div><div class="wrap hero-2">
<div>{crumb(("Our Work", "/work/"), "Courses & Learning")}<p class="hs-k">{ic("book")}Courses & Learning · training platforms</p>
<h1>Course catalogues that fill classes.</h1>
<p class="hero-p">A WordPress plugin for training institutes: courses grouped into schools, class dates with live seats left, online registration with M-Pesa, group rates, trainers and a student showcase. We also set up and support Moodle.</p>
<div class="btns">{btn("#demo", "Book a demo", "p", "arrow")}{btn("https://pentarchtraininginstitute.co.ke/", "See it live", "g", "ne", True)}</div></div>
{solo("pti-intake", "Pentarch Training Institute class dates with seats left")}</div></section>'''
    live = section(f'''<div class="split">{head("Running at Pentarch Training Institute", "33 certificate courses in five schools, each with its own page, intakes and registration.")}
<ul class="bars-list">{sc}</ul></div>''', tone="white")
    T = [("cat", "Catalogue", "layers", feat_panel("Courses grouped into schools", "Each course has its own page with outcomes, duration, trainers and upcoming dates.", ["Schools and course pages", "Popular courses this term", "Careers the course leads to", "Trainers on each course"], terminal("catalogue", [("cmd", "$ pentarch courses --by-school"), ("row", '<b>Creative Media</b><span>7 courses</span>'), ("row", '<b>Digital and Tech</b><span>11 courses</span>'), ("row", '<b>Research, Data and Impact</b><span>9 courses</span>'), ("row", '<b>Communication and PR</b><span>5 courses</span>'), ("row", '<b>Training of Trainers</b><span>1 course</span>'), ("ok", "33 courses in 5 schools")]))),
         ("intake", "Intakes and seats", "cal", feat_panel("Class dates with seats left", "Seats count down as people register, so visitors see which dates are filling.", ["Class dates per course", "Live seats left", "Next intake on the home page", "Upcoming intakes page"], seats_board())),
         ("reg", "Registration", "cash", feat_panel("Register and pay online", "Visitors choose a course and a date, register online and pay by M-Pesa, then receive joining details.", ["Online registration", "M-Pesa payment", "Fees and payment plans pages", "Joining details sent on registration"], journey())),
         ("org", "Organisations", "users", feat_panel("Groups and corporate training", "Group rates for ten or more, and a request form for custom courses and Training of Trainers.", ["Group rate on each course page", "Training proposals for organisations", "Custom courses", "Trainer profiles"], '<div class="mk mk-list" aria-hidden="true"><div class="ml-h"><b>Group booking</b><span>10 or more</span></div><div class="ml-r"><span>Course</span><b>Data Analysis</b></div><div class="ml-r"><span>Participants</span><b>14</b></div><div class="ml-r"><span>Rate</span><b>Group rate applied</b></div><div class="ml-f">Proposal sent to the organisation</div></div>')),
         ("moodle", "Moodle", "server", feat_panel("Moodle, set up and supported", "Where an institution needs a full learning management system, we install, configure and support Moodle alongside the catalogue.", ["Installation and configuration", "Course set-up", "Help for trainers and students", "Ongoing support"], terminal("moodle", [("cmd", "$ pentarch setup moodle"), ("ok", "installed and configured"), ("ok", "courses set up"), ("ok", "support: phone and WhatsApp")]))) ]
    feats = section(head("What the platform does") + tabs("ln", T), sid="features")
    also = section(f'''<div class="split">{head("Pair it with SimLab", "Pentarch SimLab adds more than 50 interactive simulations that students open in any browser.")}<div>{sim_mock()}{btn("/simlab/", "Explore SimLab", "p", "arrow")}</div></div>''', tone="ink2")
    cta = lead_section("learning", "Book a demo", "Put your courses online", "Tell us how many courses and intakes you run. We will show you the platform with your catalogue.", ["Your schools and courses", "Registration and M-Pesa", "No obligation"])
    return page("learning", hero + live + feats + also + cta)


# ============================================================== NGO PORTAL
def ngo():
    hero = f'''<section class="hero hero-ngo t-paper"><div class="wrap hero-2">
<div class="ngo-txt">{crumb(("Products", "/products/"), "Pentarch EduSponsor")}<p class="hs-k">{ic("handshake")}Pentarch EduSponsor</p>
<h1>Every sponsor, every student, every shilling, traced.</h1>
<p class="hero-p">For charities and education sponsorship programmes. Track students and schools, sponsors and donations, fees paid to schools, letters between sponsors and students, and the impact years later.</p>
<div class="btns">{btn("#demo", "Book a demo", "p", "arrow")}{btn("https://samelimu.pentarchcommunications.com/", "See it live for SAM Elimu", "g", "ne", True)}</div></div>
{duo("se-dashboard", "Pentarch EduSponsor programme dashboard", "se-sponsor", "Pentarch EduSponsor sponsor view")}</div></section>'''
    mods = [("school", "Students and schools", "Each student's school, class, results and needs, with a tracker across the programme."),
            ("handshake", "Sponsors and donations", "Sponsor records, gifts and online donations by card, PayPal or M-Pesa."),
            ("cash", "Fees and disbursements", "Fees owed and paid to each school, requested, approved and paid with a reference."),
            ("mail", "Letters", "Letters between sponsors and students, reviewed by staff before delivery."),
            ("chart", "Impact and alumni", "Progress over the years, an annual impact report and an alumni network for mentoring."),
            ("globe", "Public pages", "Pages that show the programme's work and the students awaiting a sponsor.")]
    m = "".join(f'<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in mods)
    mods_s = section(head("Six parts, one portal", "Shown as it runs for SAM Elimu Charity, which has supported children in rural Kenya through school since 2002.") + f'<ul class="caps caps-3">{m}</ul>', sid="features", tone="white")
    SEU = "samelimu.pentarchcommunications.com"
    tour_s = section(head("Inside the portal", "The demonstration portal, with invented sample data. Every screen below is the real system.", "real screens") + tour("se", [
        ("se-dashboard", "Programme dashboard", "Students supported, money raised and disbursed, results by level, and what needs attention today.", ""),
        ("se-student", "A student's whole journey", "Results by term, fees paid, welfare visits with photos, letters and a one-click progress report.", ""),
        ("se-fees", "Every shilling leaves a trail", "Staff request a fee, an administrator approves it, and it is paid with a bank or M-Pesa reference.", ""),
        ("se-sponsor", "Sponsor view", "Sponsors see only their own students: results, field visit notes, letters and receipts.", ""),
        ("se-letters", "Letters, reviewed first", "Letters between sponsors and students wait for staff approval before delivery.", ""),
        ("se-alumni", "Alumni and mentoring", "Graduates record their careers and mentor current students.", ""),
        ("se-impact", "Annual impact report", "Built from live records and saved as a PDF in one click.", ""),
        ("se-public", "Sponsor a student", "The public website lists students awaiting a sponsor, with first names only.", "")], "tour-d"), sid="screens", tone="ink2")
    rl = [("cog", "Administrators", "Approve fee payments and see the whole programme."), ("users", "Programme staff", "Run students, schools, welfare visits, fees and reports."),
          ("globe", "The board", "Their own sign-in to follow the programme."), ("handshake", "Sponsors", "Follow their own students' progress, receipts and letters."),
          ("school", "Students", "Their own record and letters from their sponsor."), ("star", "Alumni", "Record their careers and mentor current students.")]
    roles = section(f'''<div class="split">{head("Six ways in", "Administrators, programme staff, the board, sponsors, students and alumni each sign in to their own view of the same portal.")}
<ul class="roles roles-6">{"".join(f'<li>{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in rl)}</ul></div>''', tone="ink")
    cta = lead_section("ngo", "Book a demo", "Run your programme from one portal", "Tell us how many students and sponsors you work with. We will show you the portal with your own structure.", ["Your programmes and schools", "Online donations", "No obligation"])
    return page("ngo-portal", hero + mods_s + tour_s + roles + cta)


# ============================================================== QR ANALYTICS
def qr():
    hero = f'''<section class="hero hero-qr t-ink"><div class="qr-field" aria-hidden="true">{qr_art(9, 29)}</div><div class="wrap hero-2">
<div>{crumb(("Products", "/products/"), "QR Analytics")}<p class="hs-k">{ic("scan")}Pentarch QR Analytics · campaign tracking</p>
<h1>Know which poster was scanned, where and when.</h1>
<p class="hero-p">Create trackable QR codes for printed campaigns, events and publications. Every scan is counted by date, device and country, and clients get their own reports.</p>
<div class="btns">{btn("#demo", "Book a demo", "p", "arrow")}{btn("#features", "See the features", "g")}</div></div>
<div class="qr-vis">{solo("qr-dashboard", "Pentarch QR Analytics dashboard for Zingira Pesa")}</div></div></section>'''
    f = [("chart", "Dashboard", "Scans across all your codes and campaigns in one view."),
         ("clock", "Analytics over time", "Scans by day and hour, so you see what a launch or an event did."),
         ("phone", "Devices", "Which kinds of phones and devices scanned each code."),
         ("globe", "Countries", "Where scans came from, for campaigns that travel."),
         ("users", "Client reports", "A report per client, ready to share."),
         ("print", "Exports", "Download to CSV, Excel or PDF."),
         ("cog", "Settings", "Account, campaign and code settings in one place."),
         ("code", "API", "Connect scans to your own systems.")]
    fs = "".join(f'<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in f)
    feats = section(head("From print to proof", "Every printed code reports back, so you know which placement worked.") + f'<ul class="caps">{fs}</ul>', sid="features")
    how = section(head("How it works") + steps([("Create a code", "Name the campaign and set the address it should open."), ("Print it", "Put the code on posters, flyers, packaging or slides."),
                                              ("People scan", "Each scan is counted and sent on to the address you set."), ("Read the report", "Share the dashboard or export a report for the client.")]), tone="white")
    built = section(f'''<div class="split">{head("Built with Zingira Pesa", "QR Analytics was built with Zingira Pesa, a natural capital advisory, and runs at zingirapesa.com/qr on our own server.")}
{terminal("qr analytics · sample data", [("cmd", "campaign: market poster"), ("row", '<b>scans</b><span>2,418</span>'), ("row", '<b>unique devices</b><span>1,932</span>'), ("row", '<b>countries</b><span>6</span>'), ("ok", "report ready: CSV, Excel, PDF")])}</div>''', tone="ink2")
    cta = lead_section("qr", "Book a demo", "Track your next campaign", "Tell us about the campaign and how many codes you need.", ["Codes for each placement", "Reports for your clients", "No obligation"])
    return page("qr-analytics", hero + feats + how + built + cta)
