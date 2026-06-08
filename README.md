# CREST — Colorado Referee Education & Supplemental Training

The Colorado Soccer Association's referee development program hub.

**Live site:** https://coloradoreferee.github.io
**Developed by:** JAReferee LLC
**Licensed to:** Colorado Soccer Association

---

## What this is

This repository hosts the source for **coloradoreferee.github.io** — the central hub for the C.R.E.S.T. (Colorado Referee Education and Supplemental Training) program operated by the Colorado Soccer Association.

The Hub serves the main landing page and houses the CREST Game Day toolkit, the CREST Ref Coach experience, and the per-club CREST Team apps. As CREST consolidates ahead of the program's full handoff to CSA in January 2027, additional CREST tools currently in standalone repositories will migrate into this hub.

---

## What's in this repo

| File | Purpose |
|---|---|
| `index.html` | CREST Hub landing page — entry point to every tool in the suite |
| `crest_gameday.html` | CREST Game Day toolkit — gameday command center, QR check-in, ref coach feedback loop |
| `crest_refcoach.html` | CREST Ref Coach experience — entry point to the ref coach suite |
| `crest_team_csa.html` | CREST Team — CSA flagship instance |
| `crest_team_albion.html` | CREST Team — Albion SC |
| `crest_team_broomfield.html` | CREST Team — Broomfield SC |
| `crest_team_pride.html` | CREST Team — Pride Soccer Club |
| `crest_team_skyline.html` | CREST Team — Skyline SC |
| `crest_team_united.html` | CREST Team — Colorado United |
| `build_clubs.py` | Per-club page generator. Edit club config, run script, ship. |
| `assets/` | Logos, branding marks, illustrations |

---

## The CREST Team pattern

CREST Team is the branded education app delivered to every Colorado club. Each club gets its own per-club HTML file at `/crest_team_[club].html`, generated from a shared template with a `CLUB_CONFIG` block at the top of the file. To add a new club: copy an existing team file, swap the config block (id, name, colors, logo), drop the logo PNG into the repo root, commit.

Each Team app serves three audiences from one page — **Coach tools**, **Player development**, and **Parent education** — plus a built-in Referee Abuse Prevention pathway.

---

## The broader CREST suite

| Tool | Current location | Status |
|---|---|---|
| CREST Hub | this repo (root `index.html`) | Live |
| CREST Game Day | this repo (`crest_gameday.html`) | Live |
| CREST Ref Coach | this repo (`crest_refcoach.html`) | Live |
| CREST Team | this repo (`crest_team_*.html`) | Live — 6 clubs |
| CREST Evaluator | `coloradoreferee/CREST_Evaluator` (separate repo) | Live — to migrate into hub |
| CREST Academy | `coloradoreferee/CREST_Academy` (separate repo) | Live — to migrate into hub |
| CREST Reference Library | `coloradoreferee/CREST_Reference` (separate repo) | Live — to migrate into hub |

---

## Architecture

Each tool is a single HTML file with no server, no backend, and no build process at runtime.

- Vanilla HTML, CSS, and JavaScript — no frameworks
- Embedded fonts (Bebas Neue, DM Sans) where offline operation is required
- Client-side everything — localStorage for persistence, client-side PDF for exports
- Hosted via GitHub Pages from `main`

The `build_clubs.py` script is the only build step in the repo — and it only runs when a new club is added.

---

## About C.R.E.S.T.

C.R.E.S.T. (Colorado Referee Education and Supplemental Training) is the Colorado Soccer Association's referee development program. It exists to elevate the quality of officiating across the state, integrate U.S. Soccer's Green Badge certification, support the Referee Abuse Prevention initiative, and keep more young Colorado players involved in officiating.

The program was developed by **Deanna Duncan-Allen** (Director of Referee Operations, CSA), **Jeff Arthurholtz** (Referee Coach and Program Facilitator), with advisory support from **Esse Baharmast** (Head of Refereeing, CSA).

---

## Status

This software is under active development as part of the CREST program. Releases deploy automatically to GitHub Pages from the `main` branch. Ahead of the January 2027 program handoff to CSA, the three standalone CREST repos will be merged into this hub.

---

## License & Use

This software is the proprietary property of **JAReferee LLC** and is licensed to the **Colorado Soccer Association** for use within the CREST program. See `LICENSE` and `NOTICE.md` for the full terms.

Use by parties other than CSA (acting within the scope of the CREST program) requires a separate written license agreement from JAReferee LLC.

**Public visibility of source does not imply public license.**

---

## Contact

**For CREST program questions:**
- Director of Referee Operations: **Deanna Duncan-Allen** — refeducation@coloradoreferees.com — 303.888.6863
- Head of Refereeing: **Esse Baharmast**
- Media: **Krissia Vasquez** — kvasquez@coloradosoccer.org
- Colorado Soccer Association — https://coloradosoccer.org

**For software licensing or development questions:**
- JAReferee LLC — https://jareferee.com — licensing@jareferee.com
- Principal: **Jeff Arthurholtz**

---

© 2026 JAReferee LLC. All rights reserved.
Licensed to the Colorado Soccer Association for use within the CREST program.
