# she-survived-name-her
A chaotic family-built name game where five kids roast, rank and ultimately help rename their mum. Built in Twine (Harlowe 3.3.9), with personality questions, a 12-name gut-reaction gauntlet, a knockout tournament, a wildcard and a final vote.

## Files

- **`She Survived - Now Name Her.html`** — the finished, playable/importable Twine export. Open it directly in a browser, or import it into the Twine editor.
- **`source/original.html`** — the original export this build repairs and extends, kept for reference.
- **`build/build.py`** — regenerates the finished HTML from scratch. Every passage's text lives here as plain Python strings, plus a validator that checks for broken links, empty passages, unreachable passages, forbidden names and unbalanced brackets before writing the file. Run with `python3 build/build.py` from the repo root.
- **`build/css.txt`** / **`build/js.txt`** — the story stylesheet and the copy-to-clipboard helper script, injected into the Twine story's stylesheet/script passages.

To make further changes: edit the passage text inside `build.py` (or open the finished HTML directly in the Twine editor and re-export), then re-run the build script to re-validate.
