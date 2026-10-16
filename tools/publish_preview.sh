#!/usr/bin/env bash
# Publishes a no-index preview of the site to the gh-pages branch (GitHub Pages).
# Usage: bash tools/publish_preview.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
cp -r "$ROOT/site/." "$TMP/"
rm -f "$TMP/README.txt" "$TMP/.htaccess"
(cd "$ROOT/src" && BUILD_OUT="$TMP" PREVIEW=1 python3 build.py)
touch "$TMP/.nojekyll"
cd "$TMP"
git init -q -b gh-pages
git add -A
git -c user.name="$(git -C "$ROOT" config user.name)" -c user.email="$(git -C "$ROOT" config user.email)" commit -q -m "Preview build $(date +%F)"
git push -q -f "$(git -C "$ROOT" remote get-url origin)" gh-pages
echo "Pushed preview to gh-pages"
