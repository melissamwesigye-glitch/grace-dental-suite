# Grace Dental Suite website

Static website for Grace Dental Suite, a general dental practice in Parow, Cape Town (Dr Grace Mwizerwa, BChD UWC).
Dr Grace owns her domain and hosting; this repo produces plain files she uploads there. No frameworks, no build server.

## Layout

- `src/content.py`: every word on the site, plus the site settings (`SITE`), treatments, FAQs, blog posts,
  `INSTAGRAM_POSTS`, `TIKTOK_VIDEOS` and `BEFORE_AFTER`. Edit content here, never in `site/*.html`.
- `src/build.py`: templates. Writes all HTML pages, `sitemap.xml`, `robots.txt`, `site.webmanifest` and `.htaccess` into `site/`.
- `site/`: the deployable website. HTML files are generated; `site/assets/` (css, js, fonts, images) is hand-maintained.
- `tools/`: `prepare_photos.py` (before/after pairs), `make_logo.py` (rebuilds the vector logo), `shoot.py` (screenshots).

## Commands

```bash
cd src && python3 build.py            # rebuild every page after editing content.py or build.py
cd site && python3 -m http.server 8000 # preview at http://localhost:8000
python3 tools/prepare_photos.py <slug> before.jpg after.jpg   # then add {"slug", "title", "note"} to BEFORE_AFTER
python3 tools/shoot.py index.html,gallery.html mobile          # screenshots (needs the preview server on port 8765)
```

## Rules

- Never invent facts about the practice: prices, reviews, quotes from Dr Grace, hours, staff or services.
  Unknowns are marked `CONFIRM` in `content.py`.
- Patient photos only with the patient's permission. Review quotes only real ones, first name and initial.
- Medical content stays general and accurate; emergencies always point to hospital for spreading swelling or breathing trouble.
- Plain, warm, South African English (colour, centre). Typographic apostrophes (’).
- Headings use Antic Didone, whose apostrophe and hyphen glyphs are poor; `fix_display()` in build.py swaps them to the body font automatically.
- Links between pages are relative so the site works from any folder; canonical URLs use `SITE["domain"]`.
- Keep it fast: no new third-party scripts. Instagram, TikTok and Maps load only when scrolled into view.
- After changes, rebuild and check pages at 390px wide (no horizontal scroll) and in dark mode.

## Before launch (open items)

Domain, opening hours, WhatsApp number, practice email, treatment list, medical aids accepted,
approval of the three blog articles, real review quotes, real practice photos.
