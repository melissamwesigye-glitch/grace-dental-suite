# -*- coding: utf-8 -*-
"""Builds the static Grace Dental Suite site into ../site. Run: python3 build.py"""
import json, os, html, datetime
from urllib.parse import quote
from content import SITE, REVIEWS, TREATMENTS, TREATMENT_GROUPS, NEW_PATIENT_FAQS, POSTS, INSTAGRAM_POSTS, TIKTOK_VIDEOS, BEFORE_AFTER

OUT = os.environ.get("BUILD_OUT") or os.path.join(os.path.dirname(__file__), "..", "site")
# PREVIEW=1 builds a copy for a temporary preview address (e.g. GitHub Pages) that search engines must not index.
PREVIEW = os.environ.get("PREVIEW") == "1"
D = SITE["domain"].rstrip("/")
TODAY = datetime.date.today().isoformat()
WA_TEXT = quote("Hi Grace Dental Suite, I’d like to book an appointment.")
WA = f"https://wa.me/{SITE['whatsapp']}?text={WA_TEXT}"
e = html.escape
PAGES = []  # for sitemap
import hashlib
def _ver(rel):
    """Short content hash so browsers fetch a fresh copy whenever the file changes."""
    p = os.path.join(os.path.dirname(__file__), "..", "site", rel)
    return hashlib.md5(open(p, "rb").read()).hexdigest()[:8]
CSS_V, JS_V = _ver("assets/css/style.css"), _ver("assets/js/main.js")

ICON_WA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2Zm5.8 14.16c-.24.69-1.42 1.32-1.96 1.36-.5.05-1.13.07-1.82-.11a16.6 16.6 0 0 1-1.65-.61c-2.9-1.25-4.79-4.17-4.94-4.36-.14-.19-1.18-1.57-1.18-3s.75-2.13 1.02-2.42c.26-.29.57-.36.76-.36h.55c.18 0 .42-.07.65.5.24.58.82 2 .89 2.15.07.14.12.31.02.5-.1.19-.14.31-.29.48-.14.17-.3.38-.43.5-.14.14-.29.3-.13.59.17.29.74 1.22 1.58 1.97 1.09.97 2.01 1.27 2.3 1.42.29.14.46.12.62-.07.17-.19.72-.84.91-1.13.19-.29.38-.24.65-.14.26.1 1.68.79 1.97.94.29.14.48.21.55.33.07.12.07.69-.17 1.37Z"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/></svg>'
ICON_GO = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

NAV = [("about.html","Dr Grace"),("treatments.html","Treatments"),("gallery.html","Smile gallery"),("new-patients.html","New patients"),("blog.html","Blog"),("contact.html","Contact")]

def practice_schema():
    days=[]
    for label,disp,dlist,o,c in SITE["hours"]:
        if dlist: days.append({"@type":"OpeningHoursSpecification","dayOfWeek":dlist,"opens":o,"closes":c})
    s={"@context":"https://schema.org","@type":"Dentist","@id":D+"/#practice","name":SITE["name"],
       "url":D+"/","image":D+"/assets/img/og-image.jpg","logo":D+"/assets/img/logo.svg",
       "telephone":SITE["phone_tel"],
       "address":{"@type":"PostalAddress","streetAddress":SITE["street"]+", "+SITE["area"],"addressLocality":"Parow","addressRegion":SITE["region"],"postalCode":SITE["postcode"],"addressCountry":SITE["country"]},
       "areaServed":["Parow","Bellville","Goodwood","Tygerberg","Elsies River","Cape Town"],
       "sameAs":[SITE["instagram"],SITE["facebook"],SITE["tiktok"]],
       "employee":{"@id":D+"/about.html#dr-grace"},
       "paymentAccepted":"Cash, Card, Medical aid"}
    if days: s["openingHoursSpecification"]=days
    if SITE["email"]: s["email"]=SITE["email"]
    return s

def person_schema():
    return {"@context":"https://schema.org","@type":"Person","@id":D+"/about.html#dr-grace","name":"Dr Grace Mwizerwa",
            "jobTitle":"General dental practitioner","worksFor":{"@id":D+"/#practice"},
            "alumniOf":{"@type":"CollegeOrUniversity","name":"University of the Western Cape"},
            "hasCredential":{"@type":"EducationalOccupationalCredential","credentialCategory":"degree","name":"Bachelor of Dental Surgery (BChD)"},
            "image":D+"/assets/img/dr-grace-800.jpg","url":D+"/about.html"}

def faq_schema(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

def crumbs_schema(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":D+"/"+u} for i,(n,u) in enumerate(items)]}

def jsonld(objs):
    return "".join(f'<script type="application/ld+json">{json.dumps(o,ensure_ascii=False)}</script>' for o in objs)

def page(path, title, desc, body, current=None, schema=(), crumbs=None, og_type="website", noindex=False, priority="0.7"):
    depth = path.count("/")
    r = "../"*depth
    url = D+"/"+("" if path=="index.html" else path)
    sch = [practice_schema()] + list(schema)
    if crumbs: sch.append(crumbs_schema(crumbs))
    nav = "".join(f'<li><a href="{r}{u}"{" aria-current=\"page\"" if current==u else ""}>{t}</a></li>' for u,t in NAV)
    crumb_html = ""
    if crumbs:
        parts=[]
        for i,(n,u) in enumerate(crumbs):
            if i==len(crumbs)-1: parts.append(f'<li aria-current="page">{e(n)}</li>')
            else: parts.append(f'<li><a href="{r}{u}">{e(n)}</a></li>')
        crumb_html=f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{"".join(parts)}</ol></nav>'
    hours_rows="".join(f"<li>{e(l)}: {e(d)}</li>" for l,d,*_ in SITE["hours"])
    credit = f'<a href="{SITE["credit_url"]}" rel="noopener">{e(SITE["credit"])}</a>' if SITE["credit"] else ""
    email_li = f'<li><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>' if SITE["email"] else ""
    doc = f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex">' if (noindex or PREVIEW) else ''}
<meta name="theme-color" content="#2A2224">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{D}/assets/img/og-image.jpg">
<meta property="og:locale" content="en_ZA">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}favicon.ico" sizes="32x32">
<link rel="icon" href="{r}assets/img/heart.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preload" href="{r}assets/fonts/antic-didone-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}assets/fonts/jost-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/style.css?v={CSS_V}">
{jsonld(sch)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{r}index.html" aria-label="Grace Dental Suite, home">
      <img class="on-light" src="{r}assets/img/logo.svg" alt="Grace Dental Suite" width="118" height="62">
      <img class="on-dark" src="{r}assets/img/logo-on-dark.svg" alt="" width="118" height="62">
    </a>
    <ul class="menu" id="menu">{nav}</ul>
    <div class="nav-cta">
      <a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">{ICON_WA}Book on WhatsApp</a>
      <button class="menu-toggle" aria-expanded="false" aria-controls="menu">Menu</button>
    </div>
  </div>
</header>
{crumb_html}
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="foot-logo" src="{r}assets/img/logo-on-dark.svg" alt="Grace Dental Suite" width="200" height="105">
        <p>Gentle general dentistry in Parow, Cape Town, with Dr Grace Mwizerwa, BChD (UWC).</p>
      </div>
      <div>
        <h2>Visit</h2>
        <ul><li>{SITE['street']}<br>{SITE['area']}, {SITE['city']}, {SITE['postcode']}</li><li><a href="{SITE['maps_link']}" target="_blank" rel="noopener">Get directions</a></li></ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul><li><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></li><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp us</a></li>{email_li}{hours_rows}</ul>
      </div>
      <div>
        <h2>Follow</h2>
        <ul><li><a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{SITE['tiktok']}" target="_blank" rel="noopener">TikTok</a></li><li><a href="{SITE['facebook']}" target="_blank" rel="noopener">Facebook</a></li></ul>
      </div>
    </div>
    <div class="legal"><span>© <span id="yr">{datetime.date.today().year}</span> Grace Dental Suite. All rights reserved.</span><span class="legal-links"><a href="{r}privacy.html">Privacy policy</a><a href="{r}terms.html">Terms and conditions</a>{credit}</span></div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Book on WhatsApp">{ICON_WA}</a>
<script>window.GDS={{whatsapp:"{SITE['whatsapp']}"}};</script>
<script src="{r}assets/js/main.js?v={JS_V}" defer></script>
</body>
</html>
"""
    doc = fix_display(doc)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(doc)
    if not noindex: PAGES.append((url, priority))

import re as _re
_DISP = _re.compile(r'(<(h1|h2|h3|summary|b|blockquote)(?:\s[^>]*)?>)(.*?)(</\2>)|(<span class="name">)(.*?)(</span>)', _re.S)
def _glyphs(inner):
    def txt(m):
        t = m.group(1)
        t = t.replace("’", '<span class="g">’</span>').replace("‘", '<span class="g">‘</span>')
        t = _re.sub(r'(?<=\w)-(?=\w)', '<span class="g">-</span>', t)
        return ">" + t + "<"
    return _re.sub(r'>([^<]*)<', txt, ">" + inner + "<")[1:-1]
def fix_display(doc):
    head, sep, rest = doc.partition("<body>")
    def rep(m):
        if m.group(1): return m.group(1) + _glyphs(m.group(3)) + m.group(4)
        return m.group(5) + _glyphs(m.group(6)) + m.group(7)
    return head + sep + _DISP.sub(rep, rest)

def cta_buttons(r, ghost=True):
    g = f'<a class="btn btn-ghost" href="tel:{SITE["phone_tel"]}">{ICON_PHONE}Call {SITE["phone"]}</a>' if ghost else ""
    return f'<div class="btn-row"><a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">{ICON_WA}Book on WhatsApp</a>{g}</div>'

def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in faqs) + "</div>"

def t_index(slugs, r):
    return '<ul class="t-index">' + "".join(
        f'<li><a href="{r}treatments/{s}.html"><span class="name">{e(TREATMENTS[s]["name"])}</span><span class="desc">{e(TREATMENTS[s]["short"])}</span><span class="go">{ICON_GO}</span></a></li>' for s in slugs) + "</ul>"

def heart(cls="heart"):
    return f'<span class="{cls}" aria-hidden="true"></span>'

def post_cards(r, posts):
    out=[]
    for p in posts:
        d = datetime.date.fromisoformat(p["date"]).strftime("%-d %B %Y")
        out.append(f'<a class="post-card" href="{r}blog/{p["slug"]}.html"><div class="cover"><span>{e(p["category"])}</span><img src="{r}assets/img/heart-soft.svg" alt="" class="cover-heart"></div><time datetime="{p["date"]}">{d}</time><h3>{e(p["title"])}</h3><p>{e(p["excerpt"])}</p></a>')
    return '<div class="posts">' + "".join(out) + "</div>"

def ig_block(post):
    return f'''<div class="embed" data-instagram="{post['url']}"><a class="embed-fallback" href="{post['url']}" target="_blank" rel="noopener"><b>{e(post.get('title','View on Instagram'))}</b><span>View on Instagram</span></a></div>'''

def tt_block(video):
    """TikTok's own player: shows the video cover and plays in place. Loaded one at a time as it scrolls into
    view (loading many TikTok embeds at once makes TikTok refuse them). The link is the fallback."""
    vid = video["url"].rstrip("/").split("/")[-1]
    badge = f'<span class="badge">{e(video["badge"])}</span>' if video.get("badge") else ""
    return f'''<figure class="tt"><div class="embed tt-frame" data-tiktok-player="{vid}"><a class="embed-fallback tall" href="{video['url']}" target="_blank" rel="noopener">{badge}<span class="play" aria-hidden="true"></span><b>{e(video.get('title','Watch on TikTok'))}</b><span>Watch on TikTok</span></a></div><figcaption>{e(video.get('title',''))}</figcaption></figure>'''

def ba_pair(r, item):
    base = f"{r}assets/img/gallery/{item['slug']}"
    t = e(item["title"])
    return f'''<figure class="ba"><div class="ba-pair">
<div class="ba-side"><img src="{base}-before.webp" alt="Before treatment: {t.lower()}" width="1200" height="800" loading="lazy"><span class="ba-tag">Before</span></div>
<div class="ba-side"><img src="{base}-after.webp" alt="After treatment at Grace Dental Suite" width="1200" height="800" loading="lazy"><span class="ba-tag">After</span></div>
</div><figcaption>{t}</figcaption></figure>'''

def hours_html():
    if not SITE["hours"]:
        return "<p class=\"mb-0\">Call or WhatsApp us for appointment times.</p>"
    return '<table class="hours"><tbody>' + "".join(f"<tr><td>{e(l)}</td><td>{e(d)}</td></tr>" for l,d,*_ in SITE["hours"]) + "</tbody></table>"

def visit_block(r, heading="Visit the practice"):
    email = f'<div><dt>Email</dt><dd><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></dd></div>' if SITE["email"] else ""
    return f'''<section class="section" id="visit"><div class="wrap split even">
<div><h2>{heading}</h2>
<dl class="info">
<div><dt>Address</dt><dd>{SITE['street']}, {SITE['area']}<br>{SITE['city']}, {SITE['postcode']}<br><a href="{SITE['maps_link']}" target="_blank" rel="noopener">Get directions</a></dd></div>
<div><dt>Phone</dt><dd><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a><br><a href="tel:{SITE['phone2_tel']}">{SITE['phone2']}</a></dd></div>
<div><dt>WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">Message us to book</a></dd></div>
{email}
<div><dt>Hours</dt><dd>{hours_html()}</dd></div>
</dl></div>
<div class="map" data-map="{e(SITE['maps_query'])}"><a class="btn btn-ghost" href="{SITE['maps_link']}" target="_blank" rel="noopener">Open in Google Maps</a></div>
</div></section>'''

# ------------------------------------------------------------------ HOME
def build_home():
    r=""
    quotes = ""
    if REVIEWS:
        quotes = '<div class="quotes">' + "".join(f'<figure><blockquote>{e(q["quote"])}</blockquote><figcaption>{e(q["name"])}, Google review</figcaption></figure>' for q in REVIEWS[:3]) + "</div>"
    body = f'''
<section class="hero"><div class="wrap hero-grid">
  <div>
    <h1>Gentle, clearly explained dentistry in Parow</h1>
    <p class="lede">Dr Grace Mwizerwa (BChD, UWC) offers check-ups, fillings, root canal treatment, composite bonding and fibre bridges at 11 Kitchener Street, Fairfield Estate. Before each step, she tells you what she’s doing and why.</p>
    {cta_buttons(r)}
    <ul class="facts">
      <li><strong>{SITE['review_count']}</strong> reviews on Google</li>
      <li><strong>BP Medical Aid</strong> Dental Network</li>
      <li><strong>Open since</strong> 2023</li>
    </ul>
  </div>
  <div class="portrait">
    {heart()}
    <div class="arch"><picture><source type="image/webp" srcset="assets/img/dr-grace-480.webp 480w, assets/img/dr-grace-800.webp 800w, assets/img/dr-grace-1100.webp 1100w" sizes="(max-width:860px) 84vw, 460px"><img src="assets/img/dr-grace-800.jpg" srcset="assets/img/dr-grace-480.jpg 480w, assets/img/dr-grace-800.jpg 800w, assets/img/dr-grace-1100.jpg 1100w" sizes="(max-width:860px) 84vw, 460px" width="800" height="800" alt="Dr Grace Mwizerwa" fetchpriority="high"></picture></div>
    <div class="tag"><b>Dr Grace Mwizerwa</b><span>General dental practitioner</span></div>
  </div>
</div></section>

<section class="section tint"><div class="wrap">
  <div class="section-head"><h2>Before and after</h2><a class="btn btn-ghost" href="gallery.html">See all results</a></div>
  <div class="ba-grid">{"".join(ba_pair(r, i) for i in BEFORE_AFTER[:4])}</div>
  <p class="small muted" style="margin-top:28px">Photos of Grace Dental Suite patients, shared with their permission. Every mouth is different, so results vary.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Treatments</h2><a class="btn btn-ghost" href="treatments.html">All treatments</a></div>
  {t_index(["composite-bonding","root-canal-treatment","bridges","check-ups-and-cleaning","fillings","emergency-dentist"], r)}
</div></section>

<section class="section tint"><div class="wrap split">
  <div><h2>If you’re nervous about the dentist</h2><p class="lede" style="margin-top:18px">Tell us when you book. Here is what to expect in the chair.</p></div>
  <ul class="promises">
    <li><b>Explained first</b><p>Dr Grace tells you what she’s about to do, and why, before she starts.</p></li>
    <li><b>Your pace</b><p>Ask for a break at any time.</p></li>
    <li><b>Your options</b><p>You hear the options for your teeth before any treatment is done.</p></li>
    <li><b>No rushing</b><p>Bonding is shaped by hand, typically 2 to 3 hours per tooth.</p></li>
  </ul>
</div></section>

<section class="section panel"><div class="wrap split even" style="align-items:center">
  <div>
    <h2>Meet Dr Grace</h2>
    <p class="lede" style="margin-top:18px">Dr Grace Mwizerwa trained at the University of the Western Cape and opened Grace Dental Suite in 2023. It is a proudly Black woman-owned practice. She shares her work, and honest dental advice, on TikTok and Instagram.</p>
    <div class="btn-row" style="margin-top:28px"><a class="btn btn-primary" href="about.html">About Dr Grace</a></div>
  </div>
  <div class="tt-single">{tt_block(TIKTOK_VIDEOS[0])}</div>
</div></section>

<section class="section" id="reviews"><div class="wrap split">
  <div><h2>What patients say</h2></div>
  <div class="prose">
    <p>Grace Dental Suite has {SITE['review_count']} reviews on Google. Patients often describe their appointments as smooth and painless, and mention that Dr Grace explains each step of their treatment.</p>
    {quotes}
    <div class="btn-row" style="margin-top:24px"><a class="btn btn-ghost" href="{SITE['google_reviews']}" target="_blank" rel="noopener">Read the reviews on Google</a></div>
  </div>
</div></section>

<section class="section tight"><div class="wrap"><div class="band">
  <div><h2>On the BP Medical Aid Dental Network</h2><p>BP Medical Aid members can be seen as network patients. On another medical aid or paying cash? Contact us and we’ll explain how payment works.</p></div>
  <a class="btn btn-primary" href="new-patients.html#medical-aid">Medical aid and payment</a>
</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Dental advice</h2><a class="btn btn-ghost" href="blog.html">All articles</a></div>
  {post_cards(r, POSTS[:3])}
</div></section>

{visit_block(r)}
'''
    page("index.html", "Grace Dental Suite | Dentist in Parow, Cape Town", "Dr Grace Mwizerwa (BChD, UWC): check-ups, fillings, root canals, composite bonding and fibre bridges in Fairfield Estate, Parow. BP Medical Aid network. Book on WhatsApp.", body, current=None, priority="1.0")

# ------------------------------------------------------------------ ABOUT
def build_about():
    r=""
    body = f'''
<section class="page-hero"><div class="wrap split even" style="align-items:center">
  <div>
    <h1>Dr Grace Mwizerwa</h1>
    <p class="lede">General dental practitioner and owner of Grace Dental Suite in Fairfield Estate, Parow.</p>
    {cta_buttons(r)}
  </div>
  <div class="portrait">{heart()}<div class="arch"><picture><source type="image/webp" srcset="assets/img/dr-grace-480.webp 480w, assets/img/dr-grace-800.webp 800w" sizes="(max-width:860px) 84vw, 400px"><img src="assets/img/dr-grace-800.jpg" width="800" height="800" alt="Dr Grace Mwizerwa" loading="lazy"></picture></div></div>
</div></section>

<section class="section tint" id="dr-grace"><div class="wrap split">
  <div><h2>Qualifications</h2></div>
  <ul class="creds">
    <li><b>Bachelor of Dental Surgery (BChD)</b><span>University of the Western Cape</span></li>
    <li><b>General dental practitioner</b><span>On the BP Medical Aid Dental Network</span></li>
    <li><b>Root canal equipment</b><span>Uses the cordless FKG Rooter endodontic motor</span></li>
  </ul>
</div></section>

<section class="section"><div class="wrap split">
  <div><h2>How Dr Grace works</h2></div>
  <div class="prose">
    <p>Dr Grace opened Grace Dental Suite in Fairfield Estate, Parow, in 2023. It is a proudly Black woman-owned practice, built, in her words, with passion, faith, hard work and the trust of the patients who walk through the door.</p>
    <p>Before any treatment, she talks you through what will happen. Nothing starts until you’re ready, and you can ask to pause at any time. Patients often describe their visits as smooth and painless.</p>
    <p>Much of her work is composite bonding: rebuilding chipped, worn, decayed or gapped teeth, and replacing old gold restorations, by hand in tooth-coloured resin. She typically spends 2 to 3 hours per tooth and aims to save natural teeth wherever possible.</p>
    <p>She also shares her cases and everyday dental advice on <a href="{SITE['tiktok']}" target="_blank" rel="noopener">TikTok</a> and <a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram</a>.</p>
  </div>
</div></section>

<section class="section tint"><div class="wrap split even" style="align-items:center">
  <div><h2>Dr Grace’s story</h2><p class="lede" style="margin-top:18px">A short video from Dr Grace about starting and growing the practice.</p></div>
  <div class="tt-single">{tt_block(next(v for v in TIKTOK_VIDEOS if "woman-owned" in v["title"]))}</div>
</div></section>
{visit_block(r, "Book with Dr Grace")}
'''
    page("about.html", "Dr Grace Mwizerwa, Dentist in Parow | Grace Dental Suite", "Dr Grace Mwizerwa, BChD (University of the Western Cape), general dental practitioner on the BP Medical Aid Dental Network in Fairfield Estate, Parow, Cape Town.", body, current="about.html", schema=[person_schema()], crumbs=[("Home","index.html"),("Dr Grace","about.html")], og_type="profile", priority="0.9")

# ------------------------------------------------------------------ TREATMENTS
def build_treatments():
    r=""
    groups = "".join(f'<div class="t-group"><h2>{e(g)}</h2>{t_index(sl, r)}</div>' for g,sl in TREATMENT_GROUPS)
    body = f'''
<section class="page-hero"><div class="wrap">
  <h1>Treatments</h1>
  <p class="lede">Everything from your six-monthly check-up to a smile makeover, under one roof in Parow. Not sure what you need? Book a check-up and Dr Grace will explain your options.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">{groups}</div></section>
<section class="section tight"><div class="wrap"><div class="band"><div><h2>Not sure where to start?</h2><p>Send us a WhatsApp with what’s bothering you and we’ll suggest the right appointment.</p></div>{cta_buttons(r, ghost=False)}</div></div></section>
'''
    page("treatments.html", "Dental Treatments in Parow, Cape Town | Grace Dental Suite", "Check-ups, fillings, root canals, extractions, whitening, bonding, dentures, children’s dentistry and emergency care in Parow, Cape Town.", body, current="treatments.html", crumbs=[("Home","index.html"),("Treatments","treatments.html")], priority="0.9")

    for slug,t in TREATMENTS.items():
        r="../"
        path=f"treatments/{slug}.html"
        intro="".join(f"<p>{e(p)}</p>" for p in t["intro"])
        parts=[]
        if t.get("warning"): parts.append(f'<div class="callout"><p><strong>Important:</strong> {e(t["warning"])}</p></div>')
        if t.get("callout"): parts.append(f'<div class="callout"><p>{e(t["callout"])}</p></div>')
        parts.append(f'<h2>{e(t["signs_title"])}</h2><ul>' + "".join(f"<li>{e(s)}</li>" for s in t["signs"]) + "</ul>")
        if t.get("not_for"): parts.append(f"<p>{e(t['not_for'])}</p>")
        if t.get("first_aid"):
            parts.append("<h2>What to do right now</h2>" + "".join(f"<h3>{e(a)}</h3><p>{e(b)}</p>" for a,b in t["first_aid"]))
        steps_html=""
        if t.get("steps"):
            steps_html = f'<section class="section tint"><div class="wrap"><h2 style="margin-bottom:36px">What happens at your appointment</h2><ol class="steps">' + "".join(f"<li><b>{e(a)}</b><p>{e(b)}</p></li>" for a,b in t["steps"]) + "</ol></div></section>"
        after=""
        if t.get("aftercare") or t.get("aftercare_list"):
            after = f'<h2>{e(t.get("aftercare_title","Aftercare"))}</h2>' + "".join(f"<p>{e(p)}</p>" for p in t.get("aftercare",[]))
            if t.get("aftercare_list"): after += "<ul>" + "".join(f"<li>{e(x)}</li>" for x in t["aftercare_list"]) + "</ul>"
        rel = t_index(t["related"], r)
        body=f'''
<section class="page-hero"><div class="wrap with-aside">
  <div>
    <h1>{e(t["h1"])}</h1>
    <div class="prose lede-prose">{intro}</div>
  </div>
  <aside class="side-card" aria-label="Book this treatment">
    <h3>Book a visit</h3>
    <p class="muted small">Tell us what’s going on and we’ll find a time that suits you.</p>
    <a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">{ICON_WA}Book on WhatsApp</a>
    <a class="btn btn-ghost" href="tel:{SITE['phone_tel']}">{ICON_PHONE}Call {SITE['phone']}</a>
  </aside>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">{"".join(parts)}</div></div></section>
{steps_html}
<section class="section"><div class="wrap split">
  <div class="prose">{after}</div>
  <div><h2 style="margin-bottom:20px">Questions</h2>{faq_html(t["faqs"])}</div>
</div></section>
<section class="section tint"><div class="wrap"><h2 style="margin-bottom:28px">Related treatments</h2>{rel}</div></section>
'''
        page(path, t["title"], t["desc"], body, current="treatments.html", schema=[faq_schema(t["faqs"])], crumbs=[("Home","index.html"),("Treatments","treatments.html"),(t["name"],path)], priority="0.8")

# ------------------------------------------------------------------ NEW PATIENTS
def build_new_patients():
    r=""
    body=f'''
<section class="page-hero"><div class="wrap">
  <h1>Your first visit</h1>
  <p class="lede">New to Grace Dental Suite? Here’s what to expect, what to bring and how medical aid and payment work.</p>
  {cta_buttons(r)}
</div></section>
<section class="section tint"><div class="wrap"><h2 style="margin-bottom:36px">How your first visit works</h2>
<ol class="steps">
  <li><b>Book</b><p>Send a WhatsApp, call us, or use the form on our contact page. Tell us if you’re nervous or in pain.</p></li>
  <li><b>Arrive a few minutes early</b><p>We’ll take your details, medical history and medical aid information.</p></li>
  <li><b>Exam and chat</b><p>Dr Grace examines your teeth and gums, with X-rays if needed, and explains what she finds.</p></li>
  <li><b>Your options</b><p>You hear your treatment options before anything is done, and choose what happens next.</p></li>
</ol></div></section>
<section class="section"><div class="wrap split">
  <div><h2>What to bring</h2></div>
  <div class="prose"><ul>
    <li>Your ID or passport</li>
    <li>Your medical aid card, if you have one</li>
    <li>A list of any medicines you take, and any allergies</li>
    <li>Recent dental X-rays or records, if you have them</li>
  </ul></div>
</div></section>
<section class="section tint" id="medical-aid"><div class="wrap split">
  <div><h2>Medical aid and payment</h2></div>
  <div class="prose">
    <p>We’re on the <strong>BP Medical Aid Dental Network</strong>, so BP Medical Aid members can be treated as network patients.</p>
    <p>On another medical aid or paying cash? Contact us before your visit and we’ll explain how payment works. Benefits differ from plan to plan, so have your medical aid details ready.</p>
    <p>You can ask for a quote at your consultation, before any treatment is done.</p>
  </div>
</div></section>
<section class="section"><div class="wrap split">
  <div><h2>Nervous about the dentist?</h2></div>
  <div class="prose">
    <p>Tell us when you book. Dr Grace will explain each step before she starts, and you can ask her to pause at any time.</p>
    <p>If something worries you, whether it’s needles, the sound of the drill or a bad experience in the past, just say so. Knowing helps us make the visit easier for you.</p>
  </div>
</div></section>
<section class="section tint"><div class="wrap split"><div><h2>Questions</h2></div>{faq_html(NEW_PATIENT_FAQS)}</div></section>
'''
    page("new-patients.html", "New Patients, Medical Aid and Payment | Grace Dental Suite, Parow", "What to expect at your first visit to Grace Dental Suite in Parow, what to bring, and how medical aid (including BP Medical Aid) and payment work.", body, current="new-patients.html", schema=[faq_schema(NEW_PATIENT_FAQS)], crumbs=[("Home","index.html"),("New patients","new-patients.html")], priority="0.8")

# ------------------------------------------------------------------ BLOG
def build_blog():
    r=""
    body=f'''
<section class="page-hero"><div class="wrap">
  <h1>Blog</h1>
  <p class="lede">Honest, practical dental advice from Grace Dental Suite in Parow.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">{post_cards(r, POSTS)}</div></section>
'''
    page("blog.html", "Dental Advice Blog | Grace Dental Suite, Parow", "Practical, honest dental advice: root canals, check-ups, whitening and more, from Grace Dental Suite in Parow, Cape Town.", body, current="blog.html", crumbs=[("Home","index.html"),("Blog","blog.html")], priority="0.7")
    for p in POSTS:
        r="../"; path=f"blog/{p['slug']}.html"
        d = datetime.date.fromisoformat(p["date"]).strftime("%-d %B %Y")
        others=[o for o in POSTS if o["slug"]!=p["slug"]][:2]
        art={"@context":"https://schema.org","@type":"BlogPosting","headline":p["title"],"description":p["desc"],"datePublished":p["date"],"dateModified":p["date"],
             "author":{"@type":"Organization","name":SITE["name"],"url":D+"/"},"publisher":{"@id":D+"/#practice"},"mainEntityOfPage":D+"/"+path,"image":D+"/assets/img/og-image.jpg"}
        body=f'''
<article>
<section class="page-hero"><div class="wrap narrow">
  <p class="post-meta">{e(p["category"])}, <time datetime="{p["date"]}">{d}</time></p>
  <h1>{e(p["title"])}</h1>
  <p class="lede">{e(p["desc"])}</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap narrow"><div class="prose">{p["body"]}</div>
<p class="muted small" style="margin-top:40px">This article is general information, not a diagnosis. For advice about your own teeth, book a check-up.</p>
</div></section>
</article>
<section class="section tint"><div class="wrap"><div class="band" style="background:transparent;padding:0;margin-bottom:56px"><div><h2>Have a question about your teeth?</h2><p>Send us a WhatsApp. We’re happy to help.</p></div>{cta_buttons(r, ghost=False)}</div>
<h2 style="margin-bottom:28px">More articles</h2>{post_cards(r, others)}</div></section>
'''
        page(path, p["seo_title"], p["desc"], body, current="blog.html", schema=[art], crumbs=[("Home","index.html"),("Blog","blog.html"),(p["title"],path)], og_type="article", priority="0.6")

# ------------------------------------------------------------------ CONTACT
def build_contact():
    r=""
    opts="".join(f"<option>{e(t['name'])}</option>" for t in TREATMENTS.values())
    body=f'''
<section class="page-hero"><div class="wrap">
  <h1>Book your visit</h1>
  <p class="lede">The quickest way to book is WhatsApp. Fill in the form and it opens WhatsApp with your request already written, ready to send.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap split even">
  <div>
    <dl class="info" style="margin-top:0">
      <div><dt>WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">{SITE['phone']}</a></dd></div>
      <div><dt>Phone</dt><dd><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a><br><a href="tel:{SITE['phone2_tel']}">{SITE['phone2']}</a></dd></div>
      {f'<div><dt>Email</dt><dd><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></dd></div>' if SITE['email'] else ''}
      <div><dt>Address</dt><dd>{SITE['street']}, {SITE['area']}<br>{SITE['city']}, {SITE['postcode']}<br><a href="{SITE['maps_link']}" target="_blank" rel="noopener">Get directions</a></dd></div>
      <div><dt>Hours</dt><dd>{hours_html()}</dd></div>
    </dl>
    <div class="callout" style="margin-top:32px;border-left:3px solid var(--rose);background:var(--bg-2);padding:18px 22px;border-radius:0 6px 6px 0"><p style="margin:0"><strong>In severe pain or swelling?</strong> Call us straight away. If swelling spreads towards your eye or neck, or you struggle to breathe or swallow, go to your nearest hospital emergency unit.</p></div>
  </div>
  <form class="form" id="book-form" novalidate>
    <h2>Request an appointment</h2>
    <div class="row2">
      <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-phone">Phone number</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
    </div>
    <div class="row2">
      <div class="field"><label for="f-treatment">Treatment</label><select id="f-treatment" name="treatment"><option>Not sure yet</option>{opts}</select></div>
      <div class="field"><label for="f-aid">Medical aid</label><select id="f-aid" name="aid"><option>BP Medical Aid</option><option>Other medical aid</option><option>Paying cash</option></select></div>
    </div>
    <div class="field"><label for="f-when">Preferred day or time (optional)</label><input id="f-when" name="when" placeholder="e.g. Tuesday morning"></div>
    <div class="field"><label for="f-msg">Anything we should know? (optional)</label><textarea id="f-msg" name="message" placeholder="Nervous, in pain, or have a question? Tell us here."></textarea></div>
    <label class="check"><input type="checkbox" name="consent" required><span>I agree that Grace Dental Suite may contact me about my appointment. See our <a href="privacy.html">privacy policy</a>.</span></label>
    <p class="form-error" role="alert"></p>
    <button class="btn btn-primary" type="submit">{ICON_WA}Continue in WhatsApp</button>
    <p class="form-note">Nothing is stored on this website. Your request is sent only when you press send in WhatsApp.</p>
  </form>
</div></section>
<section class="section tint"><div class="wrap"><div class="map" data-map="{e(SITE['maps_query'])}" style="margin-top:0;aspect-ratio:21/9"><a class="btn btn-ghost" href="{SITE['maps_link']}" target="_blank" rel="noopener">Open in Google Maps</a></div></div></section>
'''
    page("contact.html", "Book an Appointment | Grace Dental Suite, Parow, Cape Town", "Book at Grace Dental Suite, 11 Kitchener Street, Fairfield Estate, Parow. WhatsApp or call " + SITE["phone"] + ". Hours, directions and map.", body, current="contact.html", crumbs=[("Home","index.html"),("Contact","contact.html")], priority="0.9")


# ------------------------------------------------------------------ GALLERY
def build_gallery():
    r=""
    parts=[]
    if BEFORE_AFTER:
        parts.append(f'''<section class="section" style="padding-top:0"><div class="wrap"><h2 style="margin-bottom:36px">Before and after</h2><div class="ba-grid">{"".join(ba_pair(r,i) for i in BEFORE_AFTER)}</div></div></section>''')
    if INSTAGRAM_POSTS:
        parts.append(f'''<section class="section{' tint' if BEFORE_AFTER else ''}"{' style="padding-top:0"' if not BEFORE_AFTER else ''}><div class="wrap"><div class="section-head"><h2>From Instagram</h2><a class="btn btn-ghost" href="{SITE['instagram']}" target="_blank" rel="noopener">Follow @grace_dental_suite</a></div><div class="media-grid">{"".join(ig_block(p) for p in INSTAGRAM_POSTS)}</div></div></section>''')
    if TIKTOK_VIDEOS:
        parts.append(f'''<section class="section"><div class="wrap"><div class="section-head"><h2>Videos</h2><a class="btn btn-ghost" href="{SITE['tiktok']}" target="_blank" rel="noopener">Follow on TikTok</a></div><div class="media-grid">{"".join(tt_block(v) for v in TIKTOK_VIDEOS)}</div></div></section>''')
    body=f'''
<section class="page-hero"><div class="wrap">
  <h1>Smile gallery</h1>
  <p class="lede">Before-and-after photos of Grace Dental Suite patients, shared with their permission, plus Dr Grace’s posts and videos. Every mouth is different, so results vary.</p>
</div></section>
{"".join(parts)}
<section class="section tight"><div class="wrap"><div class="band"><div><h2>Book a consultation</h2><p>Dr Grace will look at your teeth and explain which options could work for you.</p></div>{cta_buttons(r, ghost=False)}</div></div></section>
'''
    page("gallery.html", "Smile Gallery: Before and After | Grace Dental Suite, Parow", "Real before-and-after results and videos from Grace Dental Suite in Parow, Cape Town: whitening, bonding, fillings and more.", body, current="gallery.html", crumbs=[("Home","index.html"),("Smile gallery","gallery.html")], priority="0.8")

# ------------------------------------------------------------------ PRIVACY / 404
def _contact_line():
    mail = f', or email <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>' if SITE["email"] else ""
    return f'Call <a href="tel:{SITE["phone_tel"]}">{SITE["phone"]}</a> or <a href="tel:{SITE["phone2_tel"]}">{SITE["phone2"]}</a>{mail}.'

def build_privacy():
    body=f'''
<section class="page-hero"><div class="wrap narrow"><h1>Privacy policy</h1><p class="lede">How Grace Dental Suite handles your personal information, in line with the Protection of Personal Information Act (POPIA).</p></div></section>
<section class="section" style="padding-top:0"><div class="wrap narrow"><div class="prose">
<h2>Who we are</h2><p>Grace Dental Suite, {SITE['street']}, {SITE['area']}, {SITE['city']}, {SITE['postcode']}. Our Information Officer is Dr Grace Mwizerwa. {_contact_line()}</p>
<h2>What this website collects</h2><p>This website does not store personal information and does not use analytics or advertising cookies. The booking form prepares a WhatsApp message on your own device. Nothing is sent until you press send in WhatsApp, and the message is then handled under WhatsApp’s own privacy terms.</p>
<h2>Embedded content</h2><p>Some pages show content from Instagram, TikTok and Google Maps. These load only when you scroll to them, and those services may set their own cookies under their own privacy policies.</p>
<h2>Patient information</h2><p>Information you share with us as a patient, such as contact details, medical history and medical aid details, is used to provide your dental care, communicate with you and process medical aid claims. It is kept confidential and shared only where needed for your care, with your medical aid, or where the law requires.</p>
<h2>Photos</h2><p>Before-and-after photos on this website are of Grace Dental Suite patients and are shown with their permission. To ask for a photo to be removed, contact us.</p>
<h2>Your rights</h2><p>You may ask to see, correct or delete the personal information we hold about you, or object to how it is used, by contacting us. You may also lodge a complaint with the Information Regulator of South Africa.</p>
<p class="muted small">Last updated {datetime.date.today().strftime("%-d %B %Y")}.</p>
</div></div></section>
'''
    page("privacy.html", "Privacy Policy (POPIA) | Grace Dental Suite", "How Grace Dental Suite in Parow handles personal information under POPIA.", body, crumbs=[("Home","index.html"),("Privacy policy","privacy.html")], priority="0.3")

def build_terms():
    body=f'''
<section class="page-hero"><div class="wrap narrow"><h1>Terms and conditions</h1><p class="lede">These terms apply to your use of the Grace Dental Suite website.</p></div></section>
<section class="section" style="padding-top:0"><div class="wrap narrow"><div class="prose">
<h2>Using this website</h2><p>By using this website you agree to these terms. If you don’t agree, please don’t use the website.</p>
<h2>Health information</h2><p>The information on this website is general and is not a diagnosis or a substitute for an examination. Advice for your own teeth is given only at a consultation. If you have swelling spreading towards your eye or neck, or trouble breathing or swallowing, go to your nearest hospital emergency unit.</p>
<h2>Appointments</h2><p>Sending a booking request through the website or WhatsApp does not confirm an appointment. Your appointment is confirmed only when the practice confirms it with you.</p>
<h2>Fees and medical aid</h2><p>Fees and what your medical aid may cover are discussed with you at the practice. Medical aid benefits depend on your plan.</p>
<h2>Before-and-after photos</h2><p>Photos show real results for individual patients. Every mouth is different, so they are not a promise of the same result for you.</p>
<h2>Other websites</h2><p>This website links to and shows content from WhatsApp, Instagram, TikTok and Google Maps. Those services are run by other companies under their own terms, and we are not responsible for their content.</p>
<h2>Copyright</h2><p>The text, logo and photos on this website belong to Grace Dental Suite. Please don’t copy or reuse them without our written permission.</p>
<h2>Liability</h2><p>We take care to keep this website accurate and up to date, but we can’t guarantee it is free of errors. As far as the law allows, Grace Dental Suite is not liable for any loss arising from your use of this website.</p>
<h2>Privacy</h2><p>How we handle personal information is explained in our <a href="privacy.html">privacy policy</a>.</p>
<h2>Changes and governing law</h2><p>We may update these terms from time to time; the date below shows the latest version. These terms are governed by the laws of the Republic of South Africa.</p>
<h2>Contact</h2><p>{_contact_line()}</p>
<p class="muted small">Last updated {datetime.date.today().strftime("%-d %B %Y")}.</p>
</div></div></section>
'''
    page("terms.html", "Terms and Conditions | Grace Dental Suite", "Terms for using the Grace Dental Suite website: health information, appointments, photos, copyright and liability.", body, crumbs=[("Home","index.html"),("Terms and conditions","terms.html")], priority="0.3")

def build_404():
    body=f'''<section class="section"><div class="wrap narrow center"><h1>Page not found</h1><p class="lede" style="margin:20px auto 32px">The page you’re looking for has moved or doesn’t exist.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="index.html">Go to the home page</a><a class="btn btn-ghost" href="treatments.html">See treatments</a></div></div></section>'''
    page("404.html", "Page not found | Grace Dental Suite", "This page could not be found.", body, noindex=True)

def build_meta():
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>\n" for u,p in PAGES) + "</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write("User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\n\nSitemap: {D}/sitemap.xml\n")
    mf={"name":SITE["name"],"short_name":"Grace Dental","start_url":"/","display":"browser","background_color":"#FFFAFB","theme_color":"#2A2224",
        "icons":[{"src":"/assets/img/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/assets/img/icon-512.png","sizes":"512x512","type":"image/png"}]}
    open(os.path.join(OUT,"site.webmanifest"),"w").write(json.dumps(mf,indent=2))
    # Apache hosts (cPanel): custom 404, HTTPS + www redirect, caching, compression
    open(os.path.join(OUT,".htaccess"),"w").write("""# Grace Dental Suite — for Apache/cPanel hosting
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
RewriteEngine On
# Always use HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
# Always use www (change if you prefer the bare domain)
RewriteCond %{HTTP_HOST} !^www\\. [NC]
RewriteRule ^ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 1 month"
ExpiresByType application/javascript "access plus 1 month"
ExpiresByType image/webp "access plus 6 months"
ExpiresByType image/jpeg "access plus 6 months"
ExpiresByType image/png "access plus 6 months"
ExpiresByType image/svg+xml "access plus 6 months"
ExpiresByType font/woff2 "access plus 1 year"
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/xml text/plain
</IfModule>
""")

if __name__ == "__main__":
    build_home(); build_about(); build_treatments(); build_new_patients(); build_blog(); build_contact(); build_gallery(); build_privacy(); build_terms(); build_404(); build_meta()
    print(len(PAGES), "pages indexed")
