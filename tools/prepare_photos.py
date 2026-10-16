"""Prepare a before/after pair for the Smile gallery.
Usage: python3 tools/prepare_photos.py <slug> <before-image> <after-image>
Writes site/assets/img/gallery/<slug>-before.webp and -after.webp (1000x1000, centre-cropped),
then add {"slug": "<slug>", "title": "...", "note": "..."} to BEFORE_AFTER in src/content.py.
Only use photos the patient has agreed to share publicly."""
import sys, os
from PIL import Image, ImageOps
if len(sys.argv) != 4:
    sys.exit(__doc__)
slug, before, after = sys.argv[1:]
out = os.path.join(os.path.dirname(__file__), "..", "site", "assets", "img", "gallery")
os.makedirs(out, exist_ok=True)
for kind, path in (("before", before), ("after", after)):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    im = ImageOps.fit(im, (1000, 1000), Image.LANCZOS, centering=(0.5, 0.5))
    dest = os.path.join(out, f"{slug}-{kind}.webp")
    im.save(dest, "WEBP", quality=80, method=6)
    print("wrote", os.path.relpath(dest))
