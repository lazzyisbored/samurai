"""Build the offline HTML from the editable game and its bundled Three.js copy."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = (root / "index.html").read_text(encoding="utf-8")
library = (root / "vendor" / "three.min.js").read_text(encoding="utf-8")
license_text = (root / "vendor" / "THREE-LICENSE.txt").read_text(encoding="utf-8")
tag = '<script src="vendor/three.min.js"></script>'
if source.count(tag) != 1:
    raise SystemExit("Expected exactly one bundled Three.js script tag")
if "</script" in library.lower():
    raise SystemExit("Library contains an HTML script terminator")
embedded = f"<script>\n/*\n{license_text}\n*/\n{library}\n</script>"
target = root / "samurai.html"
target.write_text(source.replace(tag, embedded), encoding="utf-8")
print(f"Built {target.name} ({target.stat().st_size:,} bytes)")
