# Grace Dental Suite: website

The website for [Grace Dental Suite](https://www.instagram.com/grace_dental_suite/), a gentle general dental practice in Parow, Cape Town, run by Dr Grace Mwizerwa (BChD, University of the Western Cape).

22 pages: home, about, treatments (10 treatment pages), smile gallery, new patients, blog (3 articles), contact, privacy policy, terms and conditions and 404.

## What's in it

- Plain HTML, CSS and a little JavaScript: works on any web host, no subscription.
- Built for local search: a page per treatment, structured data for Google (Dentist, FAQ, articles), sitemap, social sharing image.
- Booking by WhatsApp: the form writes the message for the patient; nothing is stored on the website.
- Smile gallery with side-by-side before-and-after photos, Instagram posts and TikTok videos.
- Light and dark mode, accessible, fast on phones.

## Editing

All text lives in `src/content.py`. After editing:

```bash
cd src && python3 build.py
```

Then upload the contents of `site/` to the hosting's `public_html` folder.

### Add a before-and-after

```bash
python3 tools/prepare_photos.py whitening-1 before.jpg after.jpg
```

Then add `{"slug": "whitening-1", "title": "Stained front teeth"}` to `BEFORE_AFTER` in `src/content.py` and rebuild.

### Add an Instagram post or TikTok video

Paste the link into `INSTAGRAM_POSTS` or `TIKTOK_VIDEOS` in `src/content.py` and rebuild.

## Preview locally

```bash
cd site && python3 -m http.server 8000
```

Open http://localhost:8000.
