# Claude handoff

This is a deliberately small static Twine project. There is no framework, database, build service, or paid dependency.

## Canonical source

- Edit passages in `build/build.py`.
- Edit presentation in `build/css.txt`.
- Edit the copy helper in `build/js.txt`.
- `source/original.html` supplies the embedded Harlowe runtime.

## Rebuild and verify

Run `python3 build/build.py` from the repository root. The script validates passage links, reachability, empty passages, forbidden names, and bracket balance before regenerating `She Survived - Now Name Her.html`.

Vercel serves the generated Twine export directly as `index.html`; do not reintroduce the old blob-URL launcher.

## Product guardrails

- Keep it mobile-first and easy for five children to use independently.
- Preserve pronunciation guides for first names.
- Current preferred name ingredients include Marlowe, Rae, Quinn, Winter, and Wilde.
- Romy and Sabine are excluded.
- Keep the humour warm, chaotic, and candid rather than solemn.
