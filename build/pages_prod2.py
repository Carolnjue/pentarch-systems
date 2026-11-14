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
    also = section(f'''<div class="split">{head("Pair it with SimLab", "Pentarch SimLab adds more than 50 interactive simulations that students open in any browser.")}<div>{shot("sim-home", "Pentarch SimLab simulation library", "shot-n")}<div class="btns">{btn("/simlab/", "Explore SimLab", "p", "arrow")}</div></div></div>''', tone="ink2")
    cta = lead_section("learning", "Book a demo", "Put your courses online", "Tell us how many courses and intakes you run. We will show you the platform with your catalogue.", ["Your schools and courses", "Registration and M-Pesa", "No obligation"])
    return page("learning", hero + live + feats + also + cta)


# ============================================================== NGO PORTAL
def ngo():
    """No longer showcased: old address sends visitors to Products."""
    body = section(f'''<div class="moved" data-redirect="/products/"><meta http-equiv="refresh" content="0; url=/products/">
<p class="hs-k">{ic("layers")}Products</p><h1>This page has moved to Products</h1>
<div class="btns">{btn("/products/", "Go to Products", "p", "arrow")}</div></div>''', tone="ink", cls="sec-moved")
    return page("ngo-portal", body)


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
    feats = section(head("From print to proof", "Every printed code reports back, so you know which placement worked.") + f'<ul class="caps caps-compact">{fs}</ul>', sid="features")
    how = section(head("How it works") + steps([("Create a code", "Name the campaign and set the address it should open."), ("Print it", "Put the code on posters, flyers, packaging or slides."),
                                              ("People scan", "Each scan is counted and sent on to the address you set."), ("Read the report", "Share the dashboard or export a report for the client.")]), tone="white")
    built = section(f'''<div class="split">{head("Built with Zingira Pesa", "QR Analytics was built with Zingira Pesa, a natural capital advisory, and runs at zingirapesa.com/qr on our own server.")}
{terminal("qr analytics · sample data", [("cmd", "campaign: market poster"), ("row", '<b>scans</b><span>2,418</span>'), ("row", '<b>unique devices</b><span>1,932</span>'), ("row", '<b>countries</b><span>6</span>'), ("ok", "report ready: CSV, Excel, PDF")])}</div>''', tone="ink2")
    cta = lead_section("qr", "Book a demo", "Track your next campaign", "Tell us about the campaign and how many codes you need.", ["Codes for each placement", "Reports for your clients", "No obligation"])
    return page("qr-analytics", hero + feats + how + built + cta)


# ============================================================== COMPLYSCOPE
CS = "https://complyscope.pentarchsystemssolutions.co.ke"


def complyscope():
    hero = f'''<section class="hero hero-cs t-paper"><div class="wrap hero-2">
<div>{crumb(("Products", "/products/"), "ComplyScope Kenya")}<p class="hs-k">{ic("shield")}ComplyScope Kenya · business compliance</p>
<h1>Never miss a filing, permit or renewal in Kenya.</h1>
<p class="hero-p">ComplyScope maps the registrations, permits, payroll remittances and tax filings that apply to a Kenyan business, national and county, works out every due date and keeps a dossier ready for inspectors, lenders and auditors.</p>
<div class="btns">{btn(CS + "/#dashboard", "Try the live dashboard", "p", "ne", True)}{btn(CS + "/signup", "Add your business, free", "g", "ne", True)}</div>
<ul class="hero-facts"><li>{ic("map")}All 47 counties</li><li>{ic("shield")}KRA, SHA, NSSF, NITA, BRS, ODPC and DOSH</li><li>{ic("star")}Free during the pilot</li></ul></div>
{duo("cs-overview", "ComplyScope workspace overview with compliance score", "cs-obligation", "ComplyScope obligation detail for the VAT return")}</div></section>'''
    mods = [("users", "Business profiler", "A ten-minute intake maps legal form, branches and counties, staff, turnover, sector and data use to the obligations that apply."),
            ("layers", "Obligation mapping", "National, county and sector obligations, each showing why it applies, the authority and the official source."),
            ("chart", "Gap analysis and score", "Every obligation marked in place, due soon, overdue or not recorded, with the next step and a score out of 100."),
            ("cal", "Deadline tracking", "Due dates worked out from the rules and moved off weekends and public holidays, with calendar links and CSV."),
            ("check", "Filing log", "Each filing, payment and renewal recorded with its iTax acknowledgement or M-Pesa reference and evidence."),
            ("print", "Dossier on demand", "A dated report of the profile, obligations, filings and documents, printed or saved as PDF.")]
    m = "".join(f'<li>{ic(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in mods)
    mods_s = section(head("Six modules, one compliance view", "From KRA iTax to the county permit office, every layer for every branch in one place.") + f'<ul class="caps caps-3">{m}</ul>', sid="features", tone="white")
    tour_s = section(head("Inside ComplyScope", "Shown as it runs for Zingira Pesa Ltd, a Nairobi company. Every screen below is the real system.", "real screens") + tour("cs", [
        ("cs-intake", "Add your business", "Answer what you can; \"not sure\" is always allowed and everything can change later.", ""),
        ("cs-overview", "Score and what to do next", "The share of obligations in order, what is overdue or due in 14 days, and the next 30 days.", ""),
        ("cs-obligation", "Why each item applies", "Authority, frequency, what to do, the penalty if late, the official source, and a form to mark it filed.", ""),
        ("cs-obligations", "Every obligation, filtered", "All obligations by status, for the whole business or one location.", ""),
        ("cs-deadlines", "The next 120 days", "Every date in order, with Mark filed, Google Calendar links and CSV.", ""),
        ("cs-filing-log", "Filing log", "Each filing and payment with its date, period and reference.", ""),
        ("cs-dossier", "Compliance dossier", "A dated report ready to print or save as PDF for an inspection or a loan application.", "")], "tour-d"), sid="screens", tone="ink2")
    guard = [("lock", "Never files for you", "Nothing is submitted to KRA, BRS, SHA, NSSF or a county portal. You file, then record the reference."),
             ("search", "Every item cites its source", "Each obligation shows why it applies, the authority and a link to the law or official portal."),
             ("shield", "Nothing assumed compliant", "Anything without a record or a date is flagged and lowers the score until you confirm it."),
             ("users", "Roles for the team", "Owners manage the business and team, editors record filings and documents, viewers can only look.")]
    gd = "".join(f'<li>{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in guard)
    guard_s = section(f'''<div class="split">{head("It tracks and reminds. You decide and file.", "ComplyScope is advisory tracking, not legal or tax advice. Rules and dates come from official sources and are being reviewed by a professional during the pilot.")}
<ul class="roles">{gd}</ul></div>''', tone="ink")
    counties = section(f'''<div class="split">{head("Permits in all 47 counties", "Add each branch with its county and ComplyScope tracks its permit and renewal. The county guide shows the permit name, where to apply and pay, and how long it lasts.")}
<div>{shot("cs-counties", "ComplyScope county permit guide", "shot-n", "complyscope.pentarchsystemssolutions.co.ke/counties")}<div class="btns">{btn(CS + "/counties", "Open the county guide", "d", "ne", True)}</div></div></div>''', tone="white")
    how = section(head("From sign-up to audit-ready") + steps([("Profile the business", "Legal form, branches and counties, staff, turnover, sector and data use."),
                                                              ("Get the gap report", "Every obligation scored, with its status, due date and next step."),
                                                              ("Stay ahead of dates", "Mark filings with references, add dates to your calendar and invite your accountant."),
                                                              ("Be audit-ready", "Export the dossier whenever KRA, BRS or a county inspector asks.")]))
    faqs = section(f'''<div class="split">{head("Questions about ComplyScope")}{faq([
        ("Does ComplyScope file returns for us?", "No. It tells you what is due and when, and keeps the record. You or your accountant file on iTax or the county portal, then record the reference."),
        ("Which obligations does it cover?", "Business registration and annual returns, KRA taxes including VAT, PAYE and instalment tax, SHA, NSSF, NITA and the Housing Levy, ODPC registration, DOSH workplace rules, county permits and sector licences."),
        ("We have branches in several counties. Does that work?", "Yes. Add each location with its county; each one gets its own permit and renewal dates."),
        ("Can our accountant use it with us?", "Yes. Invite them as an editor to record filings, or as a viewer to see everything without changing it."),
        ("Is our data private?", "Each business is visible only to the people its owner invites. Documents stay private to the team and are listed in the dossier.")])}</div>''', tone="paper")
    cta = lead_section("complyscope", "Book a demo", "See your own compliance score", "Tell us about your business and its branches. We will walk you through ComplyScope with your obligations.", ["National and county obligations", "Free during the pilot", "No obligation"])
    return page("complyscope", hero + mods_s + tour_s + guard_s + counties + how + faqs + cta)
