"""Turn Dr Grace's combined before/after images into separate 3:2 slider images.

Usage: python3 tools/split_pairs.py <folder with the original images>
Writes site/assets/img/gallery/<slug>-before.webp and <slug>-after.webp (1200x800).

Each box is (left, top, right, bottom) in the original image's pixels. Boxes on the
labelled images start below the burned-in "Before"/"After" stickers so they are cropped out.
Only use photos the patient agreed to share publicly.
"""
import os, sys
from PIL import Image, ImageOps

LABELLED_BEFORE = (116, 160, 963, 720)    # top half of a 1080x1440 image, below the sticker
LABELLED_AFTER = (116, 880, 963, 1440)    # bottom half, below the sticker

PAIRS = {
    # slug: (file, before box, after box)
    "decay-between-front-teeth": ("36aa2ad3-image.jpg", (0, 0, 1152, 768), (0, 1110, 1152, 1878)),
    "chipped-discoloured-front-tooth": ("e02adcce-image.png", (0, 720, 1080, 1440), (0, 0, 1080, 720)),
    "badly-decayed-front-teeth": ("5c643277-image.jpg", (0, 0, 1440, 960), (0, 960, 1440, 1920)),
    "missing-front-tooth": ("580b2200-image.jpg", LABELLED_BEFORE, LABELLED_AFTER),
    "short-lower-front-tooth": ("6df983fd-image.jpg", LABELLED_BEFORE, LABELLED_AFTER),
    "broken-decayed-front-teeth": ("92d84736-image.jpg", LABELLED_BEFORE, LABELLED_AFTER),
    "gaps-and-decay": ("d622749b-image.jpg", LABELLED_BEFORE, LABELLED_AFTER),
    "stained-worn-teeth": ("42904f73-image.jpg", LABELLED_BEFORE, LABELLED_AFTER),
}

def main(src):
    out = os.path.join(os.path.dirname(__file__), "..", "site", "assets", "img", "gallery")
    os.makedirs(out, exist_ok=True)
    for slug, (name, before, after) in PAIRS.items():
        im = ImageOps.exif_transpose(Image.open(os.path.join(src, name))).convert("RGB")
        for kind, box in (("before", before), ("after", after)):
            part = ImageOps.fit(im.crop(box), (1200, 800), Image.LANCZOS, centering=(0.5, 0.5))
            part.save(os.path.join(out, f"{slug}-{kind}.webp"), "WEBP", quality=82, method=6)
        print("wrote", slug)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
