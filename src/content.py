# -*- coding: utf-8 -*-
"""All words on the site live here. Edit text, then run build.py."""

SITE = {
    "name": "Grace Dental Suite",
    # CONFIRM: the domain she buys. Used for canonical links, sitemap and Google.
    "domain": "https://www.gracedentalsuite.co.za",
    # From her Instagram and TikTok bios (Oct 2026). The BP network list still shows 061 325 0776.
    "phone": "073 366 1421", "phone_tel": "+27733661421",
    "phone2": "021 023 3250", "phone2_tel": "+27210233250",
    "whatsapp": "27733661421",  # CONFIRM this number is on WhatsApp
    "email": "drgracemwizerwa@gmail.com",  # as published on her Instagram bio
    "tiktok_followers": "13K+", "instagram_followers": "8,900+",
    "street": "11 Kitchener Street", "area": "Fairfield Estate", "city": "Parow, Cape Town",
    "postcode": "7500", "region": "Western Cape", "country": "ZA",
    "maps_query": "11 Kitchener Street, Fairfield Estate, Parow, 7500",
    "maps_link": "https://www.google.com/maps/search/?api=1&query=Grace+Dental+Suite+11+Kitchener+Street+Parow",
    # CONFIRM opening hours. Leave empty until Dr Grace confirms; the site then asks people to call or WhatsApp.
    # Format: (day label, display, schema days, opens, closes), e.g.
    # ("Monday to Friday", "08:00 to 17:00", ["Monday","Tuesday","Wednesday","Thursday","Friday"], "08:00", "17:00"),
    "hours": [],
    "instagram": "https://www.instagram.com/grace_dental_suite/",
    "facebook": "https://www.facebook.com/p/Grace-Dental-Suite-61552113605504/",
    "tiktok": "https://www.tiktok.com/@grace.dental.suit",
    "ig_post": "https://www.instagram.com/p/Dax7MRqigpk/",
    "tiktok_video": "https://www.tiktok.com/@grace.dental.suit/video/7655656063072570645",
    "google_reviews": "https://www.google.com/search?q=Grace+Dental+Suite+Parow+reviews",
    "review_count": 88,
    "credit": "",  # e.g. "Website by Your Agency" with link below
    "credit_url": "",
}

# Real patient quotes go here once Dr Grace picks them from Google (first name + initial only).
REVIEWS = [
    # {"quote": "…", "name": "Thandi M."},
]

TREATMENT_GROUPS = [
    ("Everyday care", ["check-ups-and-cleaning", "fillings", "childrens-dentistry"]),
    ("Saving and replacing teeth", ["root-canal-treatment", "bridges", "extractions", "dentures"]),
    ("Cosmetic", ["composite-bonding", "teeth-whitening"]),
    ("Urgent care", ["emergency-dentist"]),
]

TREATMENTS = {
"check-ups-and-cleaning": dict(
    name="Check-ups and cleaning",
    short="A thorough exam, scale and polish, and honest advice.",
    title="Dental Check-up and Cleaning in Parow | Grace Dental Suite",
    desc="Unhurried dental check-ups and professional cleaning in Parow, Cape Town. Dr Grace explains what she finds before any treatment.",
    h1="Dental check-ups and cleaning in Parow",
    intro=["A check-up is a short, unhurried visit where Dr Grace looks at your teeth, gums and mouth, and a professional clean removes the hard build-up your toothbrush can’t reach.",
           "Catching small problems early is the easiest way to avoid toothache, bigger treatment and bigger bills later. Most adults do well with a check-up every six months. If you have gum problems or a history of decay, we may suggest coming more often."],
    signs_title="Time to book if",
    signs=["It’s been more than six months since your last visit",
           "Your gums bleed when you brush or floss",
           "You have bad breath that doesn’t go away",
           "A tooth feels sensitive to hot, cold or sweet things",
           "You’re pregnant or planning to be, when healthy gums matter even more"],
    steps=[("We chat first", "About your health, any medicines you take and anything that’s been bothering you."),
           ("A careful exam", "Dr Grace checks every tooth, your gums, your bite and the soft tissues of your mouth, with X-rays if they’re needed."),
           ("Scale and polish", "Hard build-up is gently removed above and below the gum line, then your teeth are polished smooth."),
           ("Your plan", "You leave knowing what’s healthy, what to watch and what, if anything, needs treatment.")],
    aftercare=["Your gums may feel a little tender for a day after a scale. Keep brushing twice a day with fluoride toothpaste and clean between your teeth once a day."],
    faqs=[("Does a scale and polish hurt?", "Most people feel some scraping and vibration but no pain. If your gums are sensitive, tell us and we can go slower or numb the area first."),
          ("Will my medical aid cover a check-up?", "Most medical aid plans cover routine check-ups and cleaning from day-to-day benefits, often twice a year. Benefits differ from plan to plan, so send us your medical aid details and we’ll help you check."),
          ("How long does a check-up take?", "Plan for about 30 to 45 minutes, a little longer if X-rays are needed.")],
    related=["fillings", "teeth-whitening", "childrens-dentistry"],
),
"fillings": dict(
    name="Tooth-coloured fillings",
    short="Repair decay with fillings that match your natural teeth.",
    title="Tooth-Coloured Fillings in Parow | Grace Dental Suite",
    desc="White, tooth-coloured fillings in Parow, Cape Town. Comfortable treatment for cavities, chips and old fillings, explained step by step.",
    h1="Tooth-coloured fillings",
    intro=["When decay or a small break leaves a hole in a tooth, a filling seals it and restores its shape so you can chew comfortably again. We use tooth-coloured composite, matched to your natural shade so the repair blends in.",
           "Treating a cavity while it’s small usually means a quicker, simpler visit than waiting until it hurts."],
    signs_title="Signs you may need a filling",
    signs=["A tooth is sensitive to sweet, hot or cold food",
           "Food keeps catching between two teeth",
           "You can feel a rough edge, chip or hole",
           "A dark spot has appeared on a tooth",
           "An old filling has cracked or come loose"],
    steps=[("Numbing", "The tooth is numbed so you feel pressure but not pain."),
           ("Removing decay", "The damaged part is cleaned out, keeping as much healthy tooth as possible."),
           ("Shaping", "Composite is placed in thin layers, shaped and hardened with a blue light."),
           ("Bite check", "We check your bite and polish the filling smooth.")],
    aftercare=["The numbness wears off in two to three hours, so wait before eating to avoid biting your cheek or lip.",
               "Some sensitivity for a few days is normal. If your bite feels high or uneven, call us and we’ll adjust it."],
    faqs=[("Can I eat straight after a white filling?", "Yes. Composite sets hard straight away, but wait until the numbness wears off."),
          ("How long does a filling last?", "With good care many fillings last for years. Grinding, new decay around the edges and very large fillings shorten their life, which is why regular check-ups matter."),
          ("Can you replace my old silver fillings?", "If an amalgam filling is cracked, leaking or has decay under it, it can be replaced with a tooth-coloured one. If it’s sound, Dr Grace will talk you through the pros and cons before you decide.")],
    related=["check-ups-and-cleaning", "root-canal-treatment", "composite-bonding"],
),
"root-canal-treatment": dict(
    name="Root canal treatment",
    short="Precise, comfortable care that saves your natural tooth.",
    title="Root Canal Treatment in Parow, Cape Town | Grace Dental Suite",
    desc="Gentle root canal treatment in Parow with the cordless FKG Rooter for precise, smooth care. Save your tooth and get out of pain.",
    h1="Root canal treatment, done gently",
    intro=["Root canal treatment saves a tooth whose inner nerve and blood supply (the pulp) has become infected or badly inflamed. The infected tissue is removed, the canals are cleaned and sealed, and the tooth is protected so you can keep it.",
           "Its reputation is far worse than the reality. With modern anaesthetic and equipment, many patients say it feels much like having a filling."],
    callout="Dr Grace uses the cordless FKG Rooter, an endodontic motor that gives precise, steady control of the instruments inside the canals. That means smoother cleaning and shaping, and a more comfortable visit for you.",
    signs_title="Signs you may need a root canal",
    signs=["Pain from hot or cold that lingers after the food is gone",
           "A throbbing toothache that wakes you at night",
           "Pain when you bite down",
           "Swelling, or a small pimple on the gum near a tooth",
           "A tooth that has darkened after a knock"],
    steps=[("Diagnosis", "X-rays and simple tests show what’s happening. Dr Grace explains your options, including extraction."),
           ("Numbing", "The tooth is numbed and isolated with a thin rubber sheet to keep it clean and dry."),
           ("Cleaning and shaping", "The infected pulp is removed and the canals are cleaned and shaped with the Rooter."),
           ("Sealing", "The canals are filled and sealed and the tooth is closed. Back teeth usually need a crown afterwards to protect them.")],
    aftercare=["Some tenderness when biting is normal for a few days and usually settles with over-the-counter pain relief.",
               "Avoid chewing hard food on the tooth until it has its final filling or crown."],
    faqs=[("Does a root canal hurt?", "The treatment is done under local anaesthetic, so it should feel similar to having a filling. The pain people dread is usually the infection beforehand, which the treatment relieves."),
          ("How many visits will I need?", "Many root canals are finished in one or two visits, depending on the tooth and how much infection there is."),
          ("Why not just take the tooth out?", "Keeping your own tooth is usually best for chewing and for the teeth around it. Extraction is an option, and Dr Grace will explain both honestly so you can choose."),
          ("Will I need a crown afterwards?", "Back teeth usually do, because a root-treated tooth is more likely to crack. Front teeth sometimes only need a filling.")],
    related=["extractions", "emergency-dentist", "fillings"],
),
"extractions": dict(
    name="Tooth extractions",
    short="Gentle removal when a tooth can’t be saved, with clear aftercare.",
    title="Gentle Tooth Extractions in Parow | Grace Dental Suite",
    desc="Careful tooth extractions in Parow, Cape Town, with your options explained first and clear aftercare to help you heal quickly.",
    h1="Gentle tooth extractions",
    intro=["Sometimes a tooth is too broken, loose or infected to save. A careful extraction removes it gently and lets the area heal. Dr Grace will always talk you through other options first.",
           "We’ll also talk about what comes next, whether that’s leaving the space, a denture, or a referral for an implant or bridge."],
    signs_title="When an extraction may be needed",
    signs=["A tooth is broken below the gum line",
           "Decay or infection is too severe to repair",
           "A tooth is very loose because of gum disease",
           "A baby tooth is stuck and blocking the adult tooth",
           "Your orthodontist has asked for space to be made"],
    steps=[("Assessment", "An exam and X-ray, then your options explained."),
           ("Numbing", "The area is fully numbed. You’ll feel pressure, but you shouldn’t feel pain."),
           ("Removal", "The tooth is gently loosened and removed."),
           ("Recovery", "You bite on gauze to stop the bleeding and go home with clear aftercare instructions.")],
    aftercare_list=["Keep biting on the gauze for 30 to 45 minutes",
                    "For the first 24 hours, don’t rinse, spit hard or drink through a straw",
                    "Avoid smoking and alcohol while the socket heals",
                    "Eat soft, cool food and chew on the other side",
                    "From the next day, rinse gently with warm salt water after meals",
                    "Call us if pain gets worse after two or three days, or if you have swelling or a fever"],
    faqs=[("Will it hurt?", "The area is numbed first, so you’ll feel pressure but not sharp pain. Some soreness afterwards is normal and usually eases within a few days."),
          ("How long does it take to heal?", "The gum usually closes over within one to two weeks. The bone underneath takes a few months to heal completely."),
          ("What is a dry socket?", "A painful condition that can happen when the blood clot in the socket is lost, usually a few days after an extraction. Smoking and using straws raise the risk. If pain gets worse instead of better after two or three days, call us."),
          ("Can you remove wisdom teeth?", "Dr Grace will assess your wisdom teeth with an X-ray. Straightforward cases can often be treated in the practice, and complex ones are referred to a specialist oral surgeon.")],
    related=["root-canal-treatment", "dentures", "emergency-dentist"],
),
"teeth-whitening": dict(
    name="Teeth whitening",
    short="Professional, safe whitening after a proper check-up.",
    title="Professional Teeth Whitening in Parow, Cape Town | Grace Dental Suite",
    desc="Safe, professional teeth whitening in Parow, supervised by a dentist after a check-up. Brighter teeth without guesswork.",
    h1="Professional teeth whitening",
    intro=["Professional whitening lightens the natural colour of your teeth safely, under a dentist’s supervision. It’s the simplest way to brighten your smile without changing the shape of your teeth.",
           "Before whitening, Dr Grace checks that your teeth and gums are healthy, because whitening over untreated decay or gum problems can be painful."],
    signs_title="Whitening suits you if",
    signs=["Coffee, tea, red wine or smoking have stained your teeth",
           "Your teeth have yellowed over time",
           "You want a brighter smile before a wedding, graduation or photoshoot"],
    not_for="Whitening isn’t recommended during pregnancy or breastfeeding, or while you have untreated decay. It also won’t change the colour of existing fillings or crowns.",
    steps=[("Check-up", "We make sure your teeth and gums are healthy and record your starting shade."),
           ("Your plan", "Dr Grace recommends the whitening option that suits your teeth, budget and timeline."),
           ("Whitening", "Your gums are protected and the whitening gel is applied under supervision."),
           ("Keeping it bright", "We show you how to keep your new shade for as long as possible.")],
    aftercare=["A day or two of sensitivity is common and fades on its own; a sensitive toothpaste helps.",
               "For 48 hours, go easy on strongly coloured food and drinks such as coffee, tea, red wine and curry."],
    faqs=[("Is professional whitening safe?", "Yes, when it’s done under a dentist’s supervision after a check-up. Your gums are protected and the strength is chosen for your teeth."),
          ("Why not use shop kits or charcoal?", "Shop kits are weaker, and one-size trays can let gel irritate your gums. Charcoal is abrasive and can wear enamel, which can make teeth look more yellow over time."),
          ("Will my fillings or crowns whiten too?", "No. Whitening only works on natural enamel, so fillings or crowns on front teeth may need replacing afterwards to match."),
          ("How long do results last?", "Usually from several months to a couple of years. Coffee, tea, red wine and smoking bring stains back faster.")],
    related=["composite-bonding", "check-ups-and-cleaning", "fillings"],
),
"composite-bonding": dict(
    name="Composite bonding",
    short="Hand-sculpted, tooth-coloured bonding to fix chips, gaps and old gold.",
    title="Composite Bonding in Parow, Cape Town | Grace Dental Suite",
    desc="Composite bonding in Parow, Cape Town: chips, gaps, worn teeth and old gold restorations rebuilt by hand in tooth-coloured resin, often in one visit.",
    h1="Composite bonding, sculpted by hand",
    intro=["Composite bonding is the treatment Grace Dental Suite is best known for. A tooth-coloured resin is layered, sculpted and polished directly onto your natural teeth to repair chips, close gaps, rebuild worn or decayed edges, cover stains and even out uneven shapes.",
           "Because the resin is added to your tooth, very little or none of your natural tooth usually needs to be removed. Many smiles are finished in a single visit, with no lab and no waiting."],
    callout="We don’t rush bonding. Each tooth is shade-matched and shaped by hand, and we typically spend 2 to 3 hours on each tooth, paying attention to shape, colour, function and how it suits your face and bite. More complex cases may need two appointments.",
    signs_title="Bonding can help with",
    signs=["Chipped, cracked or worn front teeth",
           "Gaps between teeth, including a natural gap you’d like closed",
           "Teeth of uneven length or shape",
           "Stains or discolouration that cleaning won’t lift",
           "Old gold or silver restorations you’d like replaced with a natural look",
           "Adult teeth with enamel defects left by decayed baby teeth"],
    steps=[("Consultation", "Tell us what you’d like to change. Dr Grace checks your bite and gum health and explains your options."),
           ("Shade matching", "The resin colour is matched to your natural teeth. Any whitening is done first, because bonding won’t whiten later."),
           ("Sculpting", "Decay or old restorations are removed where needed, then the resin is layered and shaped tooth by tooth."),
           ("Polish and check", "Each tooth is polished to a natural shine and your bite is checked and refined.")],
    aftercare=["Results are immediate. Avoid biting hard objects such as ice, nails, pens and bottle tops, and don’t use your teeth as tools.",
               "Composite is softer than porcelain, so over time it can stain or chip. Regular check-ups and a professional polish keep it looking its best, and small repairs are simple."],
    faqs=[("Does bonding damage my teeth?", "In suitable cases very little or no natural tooth needs to be removed, which is one of the biggest advantages of bonding over veneers and crowns."),
          ("How long does bonding last?", "With good care, bonding lasts for years. How long depends on your bite, habits such as grinding, and keeping up with check-ups."),
          ("Can you remove the gold on my front teeth?", "In many cases, yes. Old gold or silver restorations can be removed and replaced with tooth-coloured bonding. A consultation shows what’s possible for your teeth."),
          ("Bonding, composite veneers or porcelain veneers?", "Composite is quicker, more conservative and easier to repair, but it isn’t permanent and can stain or chip over time. Dr Grace will be honest about which option suits your goals.")],
    related=["bridges", "teeth-whitening", "fillings"],
),
"bridges": dict(
    name="Fibre and traditional bridges",
    short="Replace a missing tooth, often in one visit with a fibre bridge.",
    title="Fibre Bridges and Dental Bridges in Parow | Grace Dental Suite",
    desc="Replace a missing tooth in Parow, Cape Town. Fibre bridges are usually done in one visit without surgery; traditional bridges are made in a lab for strength.",
    h1="Fibre and traditional bridges",
    intro=["A bridge replaces a missing tooth by attaching a new tooth to the teeth on either side of the gap. Grace Dental Suite offers two kinds.",
           "A fibre bridge uses a strong fibre framework and tooth-coloured composite bonded to the neighbouring teeth. It’s conservative, needs no surgery, and is usually completed in one visit. A traditional bridge is made in a dental laboratory and cemented over prepared teeth for long-term strength."],
    signs_title="A bridge may suit you if",
    signs=["You have one missing tooth and healthy teeth on either side",
           "You’d like to avoid implant surgery",
           "You want a natural-looking result quickly",
           "An old bridge feels uncomfortable or looks unnatural and needs redoing"],
    callout="Sometimes the right space has to be created first. If neighbouring teeth have drifted into a gap over the years, a short course of braces can move them back before the missing tooth is replaced.",
    steps=[("Assessment", "Dr Grace checks the gap, the neighbouring teeth and your bite, and explains which bridge suits you."),
           ("Preparation", "For a fibre bridge, the neighbouring teeth are gently prepared for bonding. For a traditional bridge, they are shaped and impressions are taken."),
           ("Building the bridge", "A fibre bridge is built and bonded in the chair. A traditional bridge is made in the lab while you wear a temporary one."),
           ("Final fit", "The bridge is fitted, shaped and polished, and your bite is checked.")],
    aftercare=["A fibre bridge is strong, but not as strong as your natural teeth. Be mindful when biting into hard foods.",
               "Brush twice a day, clean carefully under and around the bridge, and keep up with six-monthly check-ups and cleaning."],
    faqs=[("Is a fibre bridge done in one day?", "Usually, yes. A fibre bridge is typically completed in a single visit, with an immediate result."),
          ("Fibre bridge or traditional bridge?", "A fibre bridge is quicker and more conservative. A traditional bridge is stronger for heavy chewing but needs more tooth preparation and a lab. Dr Grace will recommend what suits your mouth."),
          ("Can a bridge that was done badly be fixed?", "Often, yes. A poorly fitting bridge can be redone to correct its fit, shape and balance so it feels comfortable and looks natural."),
          ("Is a bridge better than an implant?", "Neither is better for everyone. A bridge avoids surgery and is quicker; an implant doesn’t rely on the neighbouring teeth. If an implant would suit you better, Dr Grace will explain why and refer you.")],
    related=["composite-bonding", "dentures", "extractions"],
),
"dentures": dict(
    name="Dentures",
    short="Comfortable, natural-looking replacements for missing teeth.",
    title="Dentures in Parow, Cape Town | Grace Dental Suite",
    desc="Partial and full dentures in Parow, made to fit your mouth and adjusted until they’re comfortable. Medical aid patients welcome.",
    h1="Dentures that fit and feel right",
    intro=["Dentures replace missing teeth so you can eat, speak and smile with confidence. A partial denture fills gaps between your natural teeth, and a full denture replaces all the teeth in an arch.",
           "Each denture is made by a dental laboratory to fit your mouth and adjusted until it feels comfortable."],
    signs_title="Dentures may suit you if",
    signs=["You’re missing several teeth", "You’ve lost all the teeth in your upper or lower jaw", "Your old denture is loose, worn or broken", "You want an affordable way to replace teeth"],
    steps=[("Assessment", "We check your gums and remaining teeth and talk about partial or full options."),
           ("Impressions", "Moulds and bite records are taken so the lab can build your denture."),
           ("Try-in", "You see and feel the denture before it’s finished, so changes can still be made."),
           ("Fitting", "Your denture is fitted and adjusted, with follow-up visits for any sore spots.")],
    aftercare=["Sore spots in the first weeks are common. Come back and we’ll adjust the denture rather than putting up with it.",
               "Clean your denture daily with a soft brush and denture cleaner or mild soap (regular toothpaste is too abrasive), and keep it in water when it’s out. You’ll usually be advised to take it out at night to rest your gums."],
    faqs=[("How long until I get used to them?", "Most people adjust within a few weeks. Start with soft food cut into small pieces; speaking and eating get easier with practice."),
          ("Does medical aid cover dentures?", "Many plans offer some cover, often with limits on how often dentures can be replaced. Send us your plan details and we’ll help you check."),
          ("My denture is loose. Can it be fixed?", "Gums and bone change shape over time. An old denture can often be relined to fit better, or replaced if it’s worn.")],
    related=["extractions", "check-ups-and-cleaning", "emergency-dentist"],
),
"childrens-dentistry": dict(
    name="Children’s dentistry",
    short="Relaxed first visits that help kids grow up unafraid.",
    title="Children’s Dentist in Parow, Cape Town | Grace Dental Suite",
    desc="Friendly, patient dental visits for children in Parow. First check-ups, cleaning and advice for parents, at your child’s pace.",
    h1="A friendly dentist for your child",
    intro=["A good first visit can shape how a child feels about the dentist for life. We keep children’s appointments relaxed and friendly, explain things in words they understand and never rush.",
           "Bring your child for their first check-up when their first tooth appears, or by their first birthday."],
    signs_title="Book a visit when",
    signs=["Your child’s first tooth appears, or by age one", "It’s been six months since their last check-up", "They complain of toothache or you see dark spots", "A tooth has been knocked or chipped", "You have questions about thumb-sucking or teething"],
    steps=[("Meet and greet", "A ride in the chair and a look at the tools, so nothing is a surprise."),
           ("A gentle check", "Dr Grace counts and checks teeth, gums and how the bite is developing."),
           ("Clean and protect", "A gentle clean, with fluoride where it’s helpful."),
           ("Parent chat", "Practical tips on brushing, snacks and what to expect next.")],
    aftercare_title="Healthy habits at home",
    aftercare_list=["Brush twice a day with fluoride toothpaste: a smear for under-threes, a pea-sized amount from three to six",
                    "Help with brushing until your child can do it well, usually around seven or eight",
                    "Keep sweet drinks and snacks to mealtimes",
                    "Don’t put your child to bed with a bottle of milk or juice"],
    faqs=[("Do baby teeth really matter?", "Yes. They help children eat and speak, and they hold space for adult teeth. Decay in baby teeth can cause pain and infection."),
          ("My child is scared. What should I do?", "Keep the visit low-key, avoid words like ‘hurt’ or ‘needle’, and tell us beforehand. We’ll go at your child’s pace."),
          ("Can I stay with my child?", "Of course. Parents are welcome in the room.")],
    related=["check-ups-and-cleaning", "fillings", "emergency-dentist"],
),
"emergency-dentist": dict(
    name="Emergency dental care",
    short="Toothache, swelling or a broken tooth? Call us first.",
    title="Emergency Dentist in Parow, Cape Town | Grace Dental Suite",
    desc="Toothache, swelling, a broken or knocked-out tooth? Call or WhatsApp Grace Dental Suite in Parow and we’ll see you as soon as we can.",
    h1="Emergency dental care in Parow",
    intro=["Dental pain doesn’t wait for a convenient time. If you have a toothache, swelling, a broken tooth or a knocked-out tooth, call or WhatsApp us straight away and we’ll see you as soon as we can."],
    warning="If swelling is spreading towards your eye or neck, or you have difficulty breathing or swallowing, or a high fever, go to your nearest hospital emergency unit immediately.",
    signs_title="Call us for",
    signs=["Severe or throbbing toothache", "Swelling of the face or gum", "A broken or cracked tooth", "A knocked-out tooth", "A lost filling or crown", "Bleeding that won’t stop after an extraction"],
    first_aid=[("Knocked-out adult tooth", "Pick it up by the crown, not the root. If it’s dirty, rinse it briefly in milk. Try to put it back in the socket, or keep it in milk, and get to a dentist as soon as possible, ideally within an hour."),
               ("Broken tooth", "Rinse your mouth with warm water, keep any pieces, and hold a cold compress on your cheek to reduce swelling."),
               ("Toothache", "Rinse with warm salt water and floss gently to remove trapped food. Take over-the-counter pain relief as directed on the pack. Don’t put aspirin on the gum, as it can burn."),
               ("Swelling", "Hold a cold compress on the outside of your cheek and call us. If the swelling is spreading or you feel very unwell, go to a hospital emergency unit.")],
    faqs=[("Can you see me today?", "We do our best to see urgent cases as soon as possible. Call or WhatsApp us and tell us what’s happening."),
          ("What if it’s after hours?", "Send us a WhatsApp and we’ll reply when the practice opens. For severe swelling, trouble breathing or swallowing, or heavy bleeding, go to your nearest hospital emergency unit."),
          ("Should I take antibiotics for a toothache?", "Only if a dentist or doctor prescribes them. Antibiotics don’t fix the cause of a toothache; treatment does.")],
    related=["root-canal-treatment", "extractions", "fillings"],
),
}

NEW_PATIENT_FAQS = [
    ("Do I need to be on BP Medical Aid?", "No. We’re on the BP Medical Aid Dental Network. If you’re on another medical aid or paying cash, contact us before your visit and we’ll explain how payment works."),
    ("Can I get a quote before treatment?", "Yes. Ask for a quote at your consultation, before any treatment is done."),
    ("What if I’m nervous about the dentist?", "You’re not alone. Tell us when you book. Dr Grace explains each step before she starts, and you can ask to pause at any time."),
    ("How do I book?", "Send us a WhatsApp, call the practice, or use the booking form on our contact page."),
]

POSTS = [
dict(
    slug="what-happens-during-a-root-canal",
    title="What really happens during a root canal",
    seo_title="What Happens During a Root Canal? Step by Step | Grace Dental Suite",
    desc="Root canals have a scary reputation. Here’s what actually happens at each step, how it feels, and how to recover well.",
    date="2026-10-16", category="Treatments", mark="RC",
    excerpt="It’s not the horror story you’ve heard. Here’s each step, explained.",
    body="""
<p>Say “root canal” and most people wince. The truth is that the treatment itself is usually no more uncomfortable than a filling. What hurts is the infection that leads to it, and a root canal is what takes that pain away.</p>
<h2>Why a tooth needs a root canal</h2>
<p>Inside every tooth is the pulp: soft tissue with nerves and blood vessels. Deep decay, a crack or a hard knock can let bacteria in. Once the pulp is infected or badly inflamed, it can’t heal by itself. Left alone, the infection can spread into the bone and cause an abscess.</p>
<p>A root canal removes that infected tissue and seals the tooth, so you keep your natural tooth instead of losing it.</p>
<h2>The signs to look out for</h2>
<ul>
<li>Pain from hot or cold that lingers after the food or drink is gone</li>
<li>A throbbing toothache, especially one that wakes you at night</li>
<li>Pain when you bite</li>
<li>A swollen gum, or a small pimple on the gum near the tooth</li>
<li>A tooth that has turned darker after an injury</li>
</ul>
<h2>What happens, step by step</h2>
<h3>1. Finding the cause</h3>
<p>An X-ray and a few simple tests show which tooth is the problem and how far the infection has gone. Before anything starts, Dr Grace explains your options, including taking the tooth out.</p>
<h3>2. Numbing</h3>
<p>The tooth is numbed with local anaesthetic. A thin rubber sheet is placed around it to keep it clean and dry. You’ll feel pressure but not pain.</p>
<h3>3. Cleaning the canals</h3>
<p>A small opening is made in the top of the tooth, and the infected pulp is removed. The narrow canals are then cleaned and shaped. At Grace Dental Suite this is done with the cordless FKG Rooter, an endodontic motor that gives precise, steady control. That precision makes the process smoother.</p>
<h3>4. Sealing</h3>
<p>The clean canals are filled and sealed so bacteria can’t get back in, and the opening is closed with a filling.</p>
<h3>5. Protecting the tooth</h3>
<p>A root-treated back tooth is more likely to crack, so it usually needs a crown afterwards. Front teeth sometimes only need a filling.</p>
<h2>How long does it take?</h2>
<p>Many root canals are finished in one or two visits, depending on the tooth and how much infection there is.</p>
<h2>Recovering well</h2>
<ul>
<li>Expect some tenderness when biting for a few days. Over-the-counter pain relief usually helps.</li>
<li>Avoid chewing hard food on the tooth until it has its final filling or crown.</li>
<li>Call us if you have swelling, or if pain gets worse instead of better.</li>
</ul>
<div class="callout"><p><strong>The bottom line:</strong> a root canal is a way to get out of pain and keep your tooth. If you’re nervous, tell us. We’ll explain every step before we do it and go at your pace.</p></div>
"""),
dict(
    slug="how-often-should-you-see-the-dentist",
    title="How often should you see the dentist?",
    seo_title="How Often Should You See the Dentist? | Grace Dental Suite, Parow",
    desc="Why a six-monthly check-up saves you pain and money later, and when you might need to come more often.",
    date="2026-10-16", category="Everyday care", mark="6m",
    excerpt="Why six-monthly check-ups save you money and pain later.",
    body="""
<p>Most adults do well with a check-up and professional clean every six months. Some people need to come more often, and a few can come less. Here’s why it matters, and how to tell which group you’re in.</p>
<h2>Why regular check-ups are worth it</h2>
<p>Tooth decay and gum disease are quiet at first. A small cavity rarely hurts, and early gum disease often only shows as a little bleeding when you brush. By the time something aches, the problem is usually bigger, and so is the treatment.</p>
<p>At a check-up, small problems are found while they’re still quick and affordable to fix. A filling today can save a root canal next year.</p>
<h2>What a check-up includes</h2>
<ul>
<li>A look at every tooth, your gums and the soft tissues of your mouth</li>
<li>X-rays when they’re needed, to see between teeth and below the gum</li>
<li>A scale and polish to remove hard build-up (tartar) that brushing can’t shift</li>
<li>Honest advice on what’s healthy and what to watch</li>
</ul>
<h2>When you might need to come more often</h2>
<ul>
<li>You have gum disease, or your gums bleed often</li>
<li>You’ve had a lot of fillings or new decay recently</li>
<li>You smoke, or you have diabetes</li>
<li>You’re pregnant, when hormones make gums more prone to inflammation</li>
<li>You wear braces or have a dry mouth from medication</li>
</ul>
<h2>What about medical aid?</h2>
<p>Many medical aid plans cover routine check-ups and cleaning from day-to-day benefits, often twice a year. Plans differ, so it’s worth checking yours. We’re happy to help.</p>
<h2>Between visits</h2>
<ul>
<li>Brush twice a day for two minutes with fluoride toothpaste</li>
<li>Spit, don’t rinse, so the fluoride keeps working</li>
<li>Clean between your teeth once a day with floss or interdental brushes</li>
<li>Keep sugary drinks and snacks to mealtimes</li>
</ul>
<div class="callout"><p><strong>Not sure when you were last seen?</strong> If it’s been more than a year, book a check-up. It’s the easiest way to stay out of pain.</p></div>
"""),
dict(
    slug="teeth-whitening-whats-safe",
    title="Teeth whitening: what’s safe and what isn’t",
    seo_title="Teeth Whitening: What’s Safe and What Isn’t | Grace Dental Suite",
    desc="Shop kits, charcoal, social media hacks and professional whitening, compared honestly by a dental practice.",
    date="2026-10-16", category="Cosmetic", mark="W",
    excerpt="Shop kits, charcoal and professional whitening, compared honestly.",
    body="""
<p>A brighter smile is one of the most common things people ask us about. There are plenty of options out there, and not all of them are kind to your teeth. Here’s an honest guide.</p>
<h2>Why teeth change colour</h2>
<p>Teeth stain from the outside (coffee, tea, red wine, curry, smoking) and darken from the inside with age, as enamel thins and the yellower layer underneath shows through. Some medicines and injuries can also change a tooth’s colour.</p>
<h2>Professional whitening</h2>
<p>Professional whitening lightens the natural colour of your teeth using a gel applied under a dentist’s supervision. Before whitening, your teeth and gums are checked, because whitening over decay or gum problems can be painful. Your gums are protected, and the strength is chosen for your teeth.</p>
<h2>Shop kits</h2>
<p>Over-the-counter strips and kits are weaker, so results are usually slower and milder. One-size trays can let gel leak onto your gums and irritate them. If you have sensitive teeth or any untreated decay, it’s best to get a check-up first.</p>
<h2>Charcoal and “natural” hacks</h2>
<p>Charcoal powders and toothpastes are abrasive. They can scrub off surface stains, but they can also wear away enamel. Thinner enamel lets more of the yellower layer show through, so teeth can look <em>more</em> yellow over time. Lemon juice and bicarbonate scrubs carry similar risks.</p>
<h2>Whitening toothpaste</h2>
<p>Whitening toothpastes mainly remove surface stains. They can help keep your teeth bright after whitening, but they won’t change your teeth’s natural shade.</p>
<h2>Things whitening can’t do</h2>
<ul>
<li>It won’t change the colour of fillings, crowns or veneers</li>
<li>It isn’t recommended during pregnancy or breastfeeding</li>
<li>Some deep stains respond poorly, and bonding may be a better option</li>
</ul>
<h2>Keeping your results</h2>
<ul>
<li>Go easy on strongly coloured food and drinks for 48 hours after whitening</li>
<li>Rinse with water after coffee or tea</li>
<li>Keep up your six-monthly check-ups and cleaning</li>
</ul>
<div class="callout"><p><strong>Thinking about whitening?</strong> Start with a check-up. Dr Grace will tell you honestly what result to expect and which option suits your teeth.</p></div>
"""),
]


# ---------------------------------------------------------------- SOCIAL MEDIA & GALLERY
# Instagram posts to embed on the Smile gallery page (paste the post link, e.g. https://www.instagram.com/p/XXXX/).
# The first one also appears on the home page. A carousel post shows all its slides.
INSTAGRAM_POSTS = [
    {"url": "https://www.instagram.com/p/Dax7MRqigpk/", "title": "Before and after: gold and silver to a natural smile"},
    {"url": "https://www.instagram.com/p/DZcs7L-ihmE/", "title": "Before and after"},
    {"url": "https://www.instagram.com/reel/DbYM7R-KUDz/", "title": "Worn front teeth, restored in one day"},
    {"url": "https://www.instagram.com/reel/DbvnfYsKBXw/", "title": "Fibre bridge or bonding? Can you tell?"},
    {"url": "https://www.instagram.com/reel/DaDGlD9Kc7k/", "title": "Composite bonding, explained"},
    {"url": "https://www.instagram.com/reel/DbdnAFYKqmZ/", "title": "Handcrafted, tooth by tooth"},
    {"url": "https://www.instagram.com/reel/DdgVFKgq6R7/", "title": "Bonding, veneers or crowns?"},
    {"url": "https://www.instagram.com/p/DdoD6nPqfJ9/", "title": "When baby teeth affect adult teeth"},
    {"url": "https://www.instagram.com/p/DWDXPbQCpXw/", "title": "Composite veneers: the honest truth"},
]

# TikTok videos (Share > Copy link). The first one also appears on the home page.
TIKTOK_VIDEOS = [
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7655656063072570645", "title": "Goodbye gold, hello confidence", "badge": "Most viewed"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7644602721005522196", "title": "Composite bonding in one visit"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7448908141590334725", "title": "Thank you God for my talent"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7631959615382588693", "title": "From pain to confidence: root canal and bonding"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7695014310463950100", "title": "From decayed teeth to a new smile"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7621197540892986644", "title": "Fibre bridges, explained"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7680610415277116693", "title": "Braces first, then a fibre bridge"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7610453603345616149", "title": "Traditional bridge: the final reveal"},
    {"url": "https://www.tiktok.com/@grace.dental.suit/video/7617839700300008725", "title": "Proudly Black woman-owned"},
]

# Before-and-after pairs shown as drag-to-compare sliders. Only add photos the patient agreed to share.
# Prepare images with:  python3 tools/prepare_photos.py <slug> <before.jpg> <after.jpg>
# then add an entry like:
# {"slug": "bonding-1", "title": "Composite bonding", "note": "Small gap closed in one visit"},
BEFORE_AFTER = [
    {"slug": "badly-decayed-front-teeth", "title": "Badly decayed front teeth"},
    {"slug": "broken-decayed-front-teeth", "title": "Broken and decayed front teeth"},
    {"slug": "stained-worn-teeth", "title": "Heavily stained teeth"},
    {"slug": "missing-front-tooth", "title": "Missing front tooth"},
    {"slug": "chipped-discoloured-front-tooth", "title": "Chipped, discoloured front tooth"},
    {"slug": "decay-between-front-teeth", "title": "Decay between the front teeth"},
    {"slug": "gaps-and-decay", "title": "Gaps and decay on the upper teeth"},
    {"slug": "short-lower-front-tooth", "title": "Short lower front tooth"},
]
