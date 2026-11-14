"""Assemble every Live Edit block, plus setup-pages.php.txt and products.txt."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import header, footer
import pages_core as A, pages_prod as B, pages_prod2 as C, pages_more as D

HERE = os.path.dirname(os.path.abspath(__file__))
# Inside the plugin repository (build/ next to pentarch-systems.php) the output is the plugin itself;
# otherwise a pentarch-systems/ folder beside this one.
OUT = os.environ.get("PSS_OUT") or (os.path.dirname(HERE) if os.path.exists(os.path.join(HERE, "..", "pentarch-systems.php")) else os.path.join(HERE, "..", "pentarch-systems"))
PAGES = [
    ("home", "Home", A.home), ("products", "Products", A.products), ("medicore", "Pentarch MediCore", B.medicore),
    ("pos", "Pentarch POS", B.pos), ("portal", "Pentarch Portal", C.portal), ("beautysuite", "Pentarch BeautySuite", C.beautysuite),
    ("learning", "Courses and Learning", C.learning), ("ngo-portal", "Pentarch EduSponsor", C.ngo), ("qr-analytics", "Pentarch QR Analytics", C.qr),
    ("live-edit", "Pentarch Live Edit", A.live_edit), ("services", "Services", D.services), ("solutions", "Solutions", D.solutions), ("labs", "Interactive and 3D", D.labs),
    ("simlab", "Pentarch SimLab", D.simlab), ("data-maps", "Dashboards and StoryMaps", D.data_maps), ("websites", "Websites", D.websites),
    ("work", "Our Work", D.work), ("about", "About Us", D.about), ("contact", "Contact Us", D.contact),
    ("dashboards", "Dashboards and StoryMaps", D.dashboards),  # old address, sends visitors to /data-maps/
]
PRODUCTS = [("medicore", "Pentarch MediCore (pharmacy, clinic or hospital)"), ("pos", "Pentarch POS (shops and businesses)"),
            ("portal", "Pentarch Portal (school or college)"), ("beautysuite", "Pentarch BeautySuite (salon or spa)"),
            ("learning", "Courses and learning system"), ("simlab", "Pentarch SimLab for my students"), ("ngo", "Pentarch EduSponsor (education sponsorship)"),
            ("qr", "QR Analytics for a campaign"), ("website", "A new website or a website revamp"), ("data", "Dashboards and StoryMaps"),
            ("custom", "A custom system"), ("agent", "I want to become a sales agent"), ("other", "Something else")]


def main():
    bd = os.path.join(OUT, "blocks"); os.makedirs(bd, exist_ok=True)
    for f in os.listdir(bd):
        if f.endswith(".html"): os.remove(os.path.join(bd, f))
    open(os.path.join(bd, "global-header.html"), "w").write(header() + "\n")
    open(os.path.join(bd, "global-footer.html"), "w").write(footer() + "\n")
    for slug, title, fn in PAGES:
        html = fn()
        assert "{{icon:" in html or True
        open(os.path.join(bd, slug + ".html"), "w").write(html)
    php = "<?php\n/* Pentarch Systems Solutions: replace pss_pages() in includes/setup.php with this function. */\nfunction pss_pages() {\n\treturn array(\n"
    php += "".join(f"\t\t'{s}' => '{t.replace(chr(39), chr(92) + chr(39))}',\n" for s, t, _ in PAGES) + "\t);\n}\n"
    open(os.path.join(HERE, "setup-pages.php.txt"), "w").write(php)
    pr = "<?php\n/* Product keys for the lead form. New keys: ngo, qr. Kept: medicore pos portal beautysuite learning website data custom agent other. */\nfunction pss_products() {\n\treturn array(\n"
    pr += "".join(f"\t\t'{k}' => '{v}',\n" for k, v in PRODUCTS) + "\t);\n}\n"
    open(os.path.join(HERE, "products.txt"), "w").write(pr)
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    main()
