"""Generate the shared header, footer, order form and Instagram blocks for each language.

Edit contact details, Instagram posts or wording HERE, then run (from D:/passion_gourmande_website):
    python tools/build_partials.py
    quarto render
Outputs in _partials/: header-<lang>.html, footer-<lang>.html, _form-<lang>.md,
                       _ig-latest-<lang>.md (home page strip), _ig-gallery-<lang>.md (gallery page)
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_partials"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- business details
# Leave "email" / "whatsapp" empty until Lilya confirms them: the matching buttons are
# simply not shown. Instagram always works (DM).
CO = {
    "instagram": "passion_gourmande_by_l",
    "facebook": "https://www.facebook.com/lilya.jas",
    "email": "",            # e.g. "hello@passiongourmande.ca"
    "whatsapp": "",         # international digits only, e.g. "16135551234"
    "phone": None,          # e.g. ("613 555 1234", "+16135551234"); None = hidden
    "year": "2026",
}
IG_URL = f"https://www.instagram.com/{CO['instagram']}/"
IG_DM = f"https://ig.me/m/{CO['instagram']}"

# Instagram posts shown on the site (her own posts only). Newest first.
# Format: (type, shortcode) where type is "p" (photo/carousel) or "reel".
# To add a post: open it on Instagram, copy the code from the URL (instagram.com/p/<CODE>/).
POSTS = [
    ("reel", "DfxH_gng-F8"),   # wedding cake, Nov 2026
    ("p",    "DfsE8QuGdC-"),
    ("reel", "DepMTtYAHMG"),   # cake in progress
    ("p",    "DeXDlC3FJ83"),
    ("reel", "DdPyULegM9I"),   # wedding cake
    ("reel", "DcwMyQNAZz9"),   # strawberry chiffon cake
    ("p",    "DLKzwMOuJfx"),
    ("reel", "DKzZXhvOMM5"),
]
LATEST = 3   # how many posts on the home page

PAGES = ["index", "creations", "gallery", "order"]

ICON = {
    "ig": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>',
    "fb": '<path d="M15 3h-2.5A4.5 4.5 0 0 0 8 7.5V10H5.5v3.5H8V21h3.5v-7.5H14l.5-3.5h-3V7.8c0-.6.4-1.3 1.3-1.3H15z"/>',
    "wa": '<path d="M20.5 11.6a8.5 8.5 0 0 1-12.6 7.4L3.5 20.5l1.5-4.3a8.5 8.5 0 1 1 15.5-4.6z"/><path d="M9 8.6c.2 2.6 3.3 5.7 6 6l1.2-1.4-2-1-1 .8a5 5 0 0 1-2.4-2.4l.8-1-1-2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "cake": '<path d="M4 21V13a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8M2 21h20M4 16c1.3 1 2.7 1 4 0s2.7-1 4 0 2.7 1 4 0 2.7-1 4 0M12 11V7"/><path d="M12 7c-1 0-1.6-.8-1.6-1.7C10.4 4.2 12 3 12 3s1.6 1.2 1.6 2.3c0 .9-.6 1.7-1.6 1.7z"/>',
    "copy": '<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>',
}
def icon(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')

T = {
 "en": {
  "root": "", "lang_label": "Language", "menu": "Menu",
  "nav": ["Home", "Creations", "Gallery", "Order"],
  "cta": "Order a cake", "dm": "Message", "by": "by Lilya",
  "city": "Ottawa, Ontario",
  "cl": {"ig": "Instagram · send a message", "wa": "WhatsApp", "phone": "Phone", "mail": "Email", "fb": "Facebook", "area": "Based in"},
  "about": "Custom cakes, French pastries and sweet tables for weddings, birthdays and special events. "
           "Every creation is designed one of a kind.",
  "h_pages": "Pages", "h_contact": "Get in touch", "rights": "All rights reserved",
  "follow": "Follow on Instagram", "ig_more": "See all creations on Instagram",
  "ig_note": "Posts load from Instagram.",
  "form": {
   "title": "Order request", "s1": "Step 1/2 · Your event", "s2": "Step 2/2 · Your details",
   "occasion": ("Occasion", ["Wedding", "Birthday", "Engagement / henna", "Baby shower / gender reveal",
                              "Corporate event", "Other"]),
   "items": ("What would you like?", ["Custom cake", "Wedding cake", "3D / sculpted cake", "Cheesecake",
                                      "French pastries & bites", "Savoury bites", "Traditional sweets",
                                      "Sweet table / buffet"]),
   "date": "Event date", "servings": ("Number of guests", "e.g. 40"),
   "details": ("Theme, colours, flavours", "Theme, colours, flavours you love, any allergies or dietary needs…"),
   "nom": "Your name", "tel": "Phone", "email": "Email",
   "reception": ("Pickup or delivery?", ["Pickup", "Delivery (to be confirmed)"]),
   "pref": ("Best way to reach you", ["Instagram", "WhatsApp", "Phone call", "Email"]),
   "next": "Next", "back": "Back", "submit": "Prepare my request",
   "err1": "Please choose the occasion, at least one item and the event date.",
   "err2": "Please enter your name and a phone number or email.",
   "done_t": "Your request is ready",
   "done_p": "Send it in one click. You can attach inspiration photos in the same conversation.",
   "by_mail": "Send by email", "by_wa": "Send on WhatsApp", "by_ig": "Copy & open Instagram",
   "copied": "Copied! Paste it in the Instagram chat.", "edit": "Edit",
   "note": "Nothing is stored on this website: your request is sent from your own app.",
   "subject": "Cake order request – website",
   "intro": "Hello Lilya, I would like to order for the following event:",
  },
 },
 "fr": {
  "root": "../", "lang_label": "Langue", "menu": "Menu",
  "nav": ["Accueil", "Créations", "Galerie", "Commander"],
  "cta": "Commander un gâteau", "dm": "Message", "by": "by Lilya",
  "city": "Ottawa, Ontario",
  "cl": {"ig": "Instagram · envoyer un message", "wa": "WhatsApp", "phone": "Téléphone", "mail": "E-mail", "fb": "Facebook", "area": "Basée à"},
  "about": "Gâteaux personnalisés, pâtisseries françaises et tables sucrées pour mariages, anniversaires "
           "et événements. Chaque création est unique.",
  "h_pages": "Pages", "h_contact": "Contact", "rights": "Tous droits réservés",
  "follow": "Suivre sur Instagram", "ig_more": "Voir toutes les créations sur Instagram",
  "ig_note": "Publications chargées depuis Instagram.",
  "form": {
   "title": "Demande de commande", "s1": "Étape 1/2 · Votre événement", "s2": "Étape 2/2 · Vos coordonnées",
   "occasion": ("Occasion", ["Mariage", "Anniversaire", "Fiançailles / henné", "Baby shower / gender reveal",
                              "Événement d'entreprise", "Autre"]),
   "items": ("Que souhaitez-vous ?", ["Gâteau personnalisé", "Pièce montée / gâteau de mariage", "Gâteau 3D",
                                      "Cheesecake", "Pâtisseries & bouchées", "Bouchées salées",
                                      "Gâteaux traditionnels", "Table sucrée / buffet"]),
   "date": "Date de l'événement", "servings": ("Nombre d'invités", "ex. 40"),
   "details": ("Thème, couleurs, saveurs", "Thème, couleurs, saveurs préférées, allergies ou régime particulier…"),
   "nom": "Votre nom", "tel": "Téléphone", "email": "E-mail",
   "reception": ("Retrait ou livraison ?", ["Retrait", "Livraison (à confirmer)"]),
   "pref": ("Comment vous joindre ?", ["Instagram", "WhatsApp", "Appel", "E-mail"]),
   "next": "Suivant", "back": "Précédent", "submit": "Préparer ma demande",
   "err1": "Merci d'indiquer l'occasion, au moins un article et la date de l'événement.",
   "err2": "Merci d'indiquer votre nom et un téléphone ou un e-mail.",
   "done_t": "Votre demande est prête",
   "done_p": "Envoyez-la en un clic. Vous pourrez joindre vos photos d'inspiration dans la même conversation.",
   "by_mail": "Envoyer par e-mail", "by_wa": "Envoyer sur WhatsApp", "by_ig": "Copier & ouvrir Instagram",
   "copied": "Copié ! Collez-le dans la conversation Instagram.", "edit": "Modifier",
   "note": "Aucune donnée n'est enregistrée sur ce site : la demande part depuis votre propre application.",
   "subject": "Demande de commande – site web",
   "intro": "Bonjour Lilya, je souhaite passer commande pour l'événement suivant :",
  },
 },
 "ar": {
  "root": "../", "lang_label": "اللغة", "menu": "القائمة",
  "nav": ["الرئيسية", "إبداعاتنا", "معرض الصور", "اطلب الآن"],
  "cta": "اطلب كعكتك", "dm": "راسلنا", "by": "by Lilya",
  "city": "أوتاوا، أونتاريو",
  "cl": {"ig": "إنستغرام · أرسلوا رسالة", "wa": "واتساب", "phone": "الهاتف", "mail": "البريد الإلكتروني", "fb": "فيسبوك", "area": "المقر"},
  "about": "كعكات حسب الطلب، حلويات فرنسية وموائد حلويات للأعراس وأعياد الميلاد والمناسبات الخاصة. "
           "كل إبداع فريد من نوعه.",
  "h_pages": "الصفحات", "h_contact": "تواصل معنا", "rights": "جميع الحقوق محفوظة",
  "follow": "تابعونا على إنستغرام", "ig_more": "شاهدوا كل الإبداعات على إنستغرام",
  "ig_note": "المنشورات معروضة من إنستغرام.",
  "form": {
   "title": "طلب كعكة", "s1": "الخطوة 1/2 · مناسبتكم", "s2": "الخطوة 2/2 · معلوماتكم",
   "occasion": ("المناسبة", ["عرس", "عيد ميلاد", "خطوبة / حنّة", "استقبال مولود",
                             "مناسبة مهنية", "أخرى"]),
   "items": ("ماذا تريدون؟", ["كعكة حسب الطلب", "كعكة عرس", "كعكة ثلاثية الأبعاد", "تشيز كيك",
                              "حلويات فرنسية صغيرة", "مملحات", "حلويات تقليدية", "مائدة حلويات / بوفيه"]),
   "date": "تاريخ المناسبة", "servings": ("عدد الضيوف", "مثال: 40"),
   "details": ("الموضوع، الألوان، النكهات", "الموضوع، الألوان، النكهات المفضلة، أي حساسية أو نظام غذائي خاص…"),
   "nom": "الاسم", "tel": "الهاتف", "email": "البريد الإلكتروني",
   "reception": ("الاستلام أو التوصيل؟", ["استلام", "توصيل (يُؤكَّد لاحقًا)"]),
   "pref": ("أفضل وسيلة للتواصل معكم", ["إنستغرام", "واتساب", "مكالمة", "بريد إلكتروني"]),
   "next": "التالي", "back": "السابق", "submit": "تحضير الطلب",
   "err1": "يرجى اختيار المناسبة وصنف واحد على الأقل وتاريخ المناسبة.",
   "err2": "يرجى إدخال الاسم ورقم الهاتف أو البريد الإلكتروني.",
   "done_t": "طلبكم جاهز",
   "done_p": "أرسلوه بنقرة واحدة، ويمكنكم إرفاق صور للإلهام في نفس المحادثة.",
   "by_mail": "إرسال عبر البريد", "by_wa": "إرسال عبر واتساب", "by_ig": "نسخ وفتح إنستغرام",
   "copied": "تم النسخ! الصقوه في محادثة إنستغرام.", "edit": "تعديل",
   "note": "لا يتم حفظ أي بيانات على هذا الموقع: يُرسل الطلب من تطبيقكم الخاص.",
   "subject": "طلب كعكة – الموقع الإلكتروني",
   "intro": "السلام عليكم ليليا، أود الطلب للمناسبة التالية:",
  },
 },
}

def brand(r, by):
    return (f'<a class="brand" href="index.html"><img src="{r}assets/logo-mark.svg" alt="" width="46" height="46">'
            f'<span lang="fr"><strong>Passion Gourmande</strong><em>{escape(by)}</em></span></a>')

def header(lang):
    t, r = T[lang], T[lang]["root"]
    nav = "".join(f'<a href="{p}.html" data-page="{p}">{escape(n)}</a>' for p, n in zip(PAGES, t["nav"]))
    cur = lambda l: ' aria-current="true"' if l == lang else ""
    langs = (f'<a data-lang="en" href="#" hreflang="en"{cur("en")}>EN</a>'
             f'<a data-lang="fr" href="#" hreflang="fr"{cur("fr")}>FR</a>'
             f'<a data-lang="ar" href="#" hreflang="ar" lang="ar"{cur("ar")}>عربي</a>')
    return f"""<header class="site-header" data-root="{r}" data-lang="{lang}">
  <div class="wrap header-inner">
    {brand(r, t['by'])}
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">{escape(t['menu'])}</button>
    <nav id="site-nav" class="site-nav" aria-label="Navigation">
      {nav}
      <div class="lang-switch" role="group" aria-label="{escape(t['lang_label'])}">{langs}</div>
      <a class="icon-link" href="{IG_URL}" target="_blank" rel="noopener" aria-label="Instagram">{icon('ig')}</a>
      <a class="btn btn-rose" href="order.html">{escape(t['cta'])}</a>
    </nav>
  </div>
</header>
"""

def contact_items(t):
    items = [f'<li><a href="{IG_URL}" target="_blank" rel="noopener">{icon("ig")}<span class="ltr">@{CO["instagram"]}</span></a></li>']
    if CO["whatsapp"]:
        items.append(f'<li><a href="https://wa.me/{CO["whatsapp"]}" target="_blank" rel="noopener">{icon("wa")}WhatsApp</a></li>')
    if CO["phone"]:
        items.append(f'<li><a href="tel:{CO["phone"][1]}">{icon("phone")}<span class="ltr">{CO["phone"][0]}</span></a></li>')
    if CO["email"]:
        items.append(f'<li><a href="mailto:{CO["email"]}">{icon("mail")}{CO["email"]}</a></li>')
    items.append(f'<li><a href="{CO["facebook"]}" target="_blank" rel="noopener">{icon("fb")}Facebook</a></li>')
    items.append(f'<li><span>{icon("pin")}{escape(t["city"])}</span></li>')
    return "".join(items)

def footer(lang):
    t, r = T[lang], T[lang]["root"]
    links = "".join(f'<li><a href="{p}.html">{escape(n)}</a></li>' for p, n in zip(PAGES, t["nav"]))
    return f"""<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div>
      {brand(r, t['by'])}
      <p>{escape(t['about'])}</p>
    </div>
    <div><h4>{escape(t['h_pages'])}</h4><ul>{links}</ul></div>
    <div><h4>{escape(t['h_contact'])}</h4><ul class="foot-contact">{contact_items(t)}</ul></div>
  </div>
  <div class="legal"><span>© {CO['year']} Passion Gourmande by Lilya · {escape(t['rights'])}</span><span>{escape(t['city'])}</span></div>
</div></footer>
<div class="mobile-bar">
  <a href="{IG_DM}" target="_blank" rel="noopener">{icon('ig')}{escape(t['dm'])}</a>
  <a href="order.html#order">{icon('cake')}{escape(t['cta'])}</a>
</div>
<script src="{r}assets/site.js" defer></script>
"""

def form(lang):
    f = T[lang]["form"]
    def opts(name, spec, kind="radio", req=True):
        legend, items = spec
        star = ' <span class="req">*</span>' if req else ""
        lab = "".join(f'<label><input type="{kind}" name="{name}" value="{escape(i)}"><span>{escape(i)}</span></label>' for i in items)
        return f'<fieldset><legend>{escape(legend)}{star}</legend><div class="opts">{lab}</div></fieldset>'
    def field(name, label, kind="text", req=False, ph="", extra=""):
        star = ' <span class="req">*</span>' if req else ""
        return (f'<div class="field"><label class="lbl" for="q-{name}">{escape(label)}{star}</label>'
                f'<input id="q-{name}" name="{name}" type="{kind}" placeholder="{escape(ph)}"{extra}></div>')
    send = []
    if CO["whatsapp"]:
        send.append(f'<a class="btn btn-rose" data-send="wa" href="#" target="_blank" rel="noopener">{icon("wa")}{escape(f["by_wa"])}</a>')
    if CO["email"]:
        send.append(f'<a class="btn btn-dark" data-send="mail" href="#">{icon("mail")}{escape(f["by_mail"])}</a>')
    ig_cls = "btn-line" if send else "btn-rose"
    send.append(f'<a class="btn {ig_cls}" data-send="ig" href="{IG_DM}" target="_blank" rel="noopener">{icon("ig")}{escape(f["by_ig"])}</a>')
    html = f"""<div class="quote" id="order">
  <div class="quote-head"><h3>{escape(f['title'])}</h3><span class="stepno" data-s1="{escape(f['s1'])}" data-s2="{escape(f['s2'])}">{escape(f['s1'])}</span></div>
  <div class="progress"><i></i></div>
  <form novalidate data-email="{CO['email']}" data-wa="{CO['whatsapp']}"
        data-subject="{escape(f['subject'])}" data-intro="{escape(f['intro'])}">
    <div class="step" data-step="1">
      {opts('occasion', f['occasion'])}
      {opts('items', f['items'], 'checkbox')}
      <div class="row2">
        {field('date', f['date'], 'date', req=True)}
        {field('servings', f['servings'][0], 'number', ph=f['servings'][1], extra=' min="1" inputmode="numeric"')}
      </div>
      <div class="field"><label class="lbl" for="q-details">{escape(f['details'][0])}</label>
        <textarea id="q-details" name="details" rows="4" placeholder="{escape(f['details'][1])}"></textarea></div>
      <p class="error" role="alert">{escape(f['err1'])}</p>
      <div class="nav"><span></span><button type="button" class="btn btn-dark" data-next>{escape(f['next'])}</button></div>
    </div>
    <div class="step" data-step="2" hidden>
      {field('nom', f['nom'], req=True, extra=' autocomplete="name"')}
      <div class="row2">
        {field('tel', f['tel'], 'tel', extra=' autocomplete="tel" inputmode="tel" dir="ltr"')}
        {field('email', f['email'], 'email', extra=' autocomplete="email" dir="ltr"')}
      </div>
      {opts('reception', f['reception'], req=False)}
      {opts('pref', f['pref'], req=False)}
      <p class="error" role="alert">{escape(f['err2'])}</p>
      <div class="nav"><button type="button" class="btn btn-line" data-back>{escape(f['back'])}</button>
        <button type="submit" class="btn btn-rose">{escape(f['submit'])}</button></div>
    </div>
    <div class="step done" data-step="3" hidden>
      <h3>{escape(f['done_t'])}</h3>
      <p>{escape(f['done_p'])}</p>
      <textarea class="summary" readonly rows="7" aria-label="{escape(f['title'])}"></textarea>
      <div class="actions">{''.join(send)}</div>
      <p class="copied" role="status" hidden>{escape(f['copied'])}</p>
      <p style="margin-top:16px"><button type="button" class="btn btn-line" data-back>{escape(f['edit'])}</button></p>
    </div>
    <p class="note">{escape(f['note'])}</p>
  </form>
</div>"""
    return "```{=html}\n" + html + "\n```\n"

def contact_list(lang):
    t = T[lang]; c = t["cl"]
    def li(ic, lab, inner):
        return f'<li>{icon(ic)}<div><b>{escape(lab)}</b>{inner}</div></li>'
    rows = [li("ig", c["ig"], f'<a href="{IG_DM}" target="_blank" rel="noopener"><span class="ltr">@{CO["instagram"]}</span></a>')]
    if CO["whatsapp"]:
        rows.append(li("wa", c["wa"], f'<a href="https://wa.me/{CO["whatsapp"]}" target="_blank" rel="noopener"><span class="ltr">+{CO["whatsapp"]}</span></a>'))
    if CO["phone"]:
        rows.append(li("phone", c["phone"], f'<a href="tel:{CO["phone"][1]}"><span class="ltr">{CO["phone"][0]}</span></a>'))
    if CO["email"]:
        rows.append(li("mail", c["mail"], f'<a href="mailto:{CO["email"]}">{CO["email"]}</a>'))
    rows.append(li("fb", c["fb"], f'<a href="{CO["facebook"]}" target="_blank" rel="noopener">Lilya Jas</a>'))
    rows.append(li("pin", c["area"], f'<span>{escape(t["city"])}</span>'))
    return '```{=html}\n<ul class="contact-list">' + "".join(rows) + "</ul>\n```\n"

def ig_block(lang, posts):
    t = T[lang]
    cards = "".join(
        f'<div class="ig-card"><blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/{k}/{c}/" '
        f'data-instgrm-version="14"><a href="https://www.instagram.com/{k}/{c}/" target="_blank" rel="noopener">'
        f'{icon("ig")}<span>Instagram</span></a></blockquote></div>' for k, c in posts)
    html = f"""<div class="ig-grid">{cards}</div>
<p class="ig-more"><a class="btn btn-rose" href="{IG_URL}" target="_blank" rel="noopener">{icon('ig')}{escape(t['ig_more'])}</a></p>
<p class="ig-note">{escape(t['ig_note'])}</p>
<script async src="https://www.instagram.com/embed.js"></script>"""
    return "```{=html}\n" + html + "\n```\n"

for lang in T:
    (OUT / f"header-{lang}.html").write_text(header(lang), encoding="utf-8")
    (OUT / f"footer-{lang}.html").write_text(footer(lang), encoding="utf-8")
    (OUT / f"_form-{lang}.md").write_text(form(lang), encoding="utf-8")
    (OUT / f"_contact-{lang}.md").write_text(contact_list(lang), encoding="utf-8")
    (OUT / f"_ig-latest-{lang}.md").write_text(ig_block(lang, POSTS[:LATEST]), encoding="utf-8")
    (OUT / f"_ig-gallery-{lang}.md").write_text(ig_block(lang, POSTS), encoding="utf-8")
    print("wrote", lang)
