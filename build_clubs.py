#!/usr/bin/env python3
"""
CREST Team — Club Variant Generator
============================================================================
WHAT IT DOES
  Reads crest_team_csa.html (the master) and produces per-club HTML files
  by swapping the CLUB_CONFIG block at the top of the master.

WHERE TO PUT IT
  In the same folder as crest_team_csa.html. That's it.
  Recommended: keep this folder as your local clone of the GitHub repo.

WHEN TO RUN IT
  - After you edit crest_team_csa.html (the master) to update content
  - When you add a new club to the CLUBS list below
  - Then commit and push the regenerated files

HOW TO RUN IT
  Windows:  open Command Prompt or PowerShell in this folder, run:
              python build_clubs.py
  Mac:      open Terminal in this folder, run:
              python3 build_clubs.py

REQUIREMENTS
  Python 3.7+. Nothing else. No pip install needed.
  Don't have Python? Install from python.org, check "Add to PATH" on Windows.

============================================================================
TO ADD A NEW CLUB
  1) Drop logo-{id}.png into this folder (and into the GitHub repo root)
  2) Add a new dict to CLUBS below with that club's colors
  3) Run the script. New file appears as crest_team_{id}.html
============================================================================
"""

import re
import pathlib
import sys

# Script lives in the same folder as the HTML files
HERE = pathlib.Path(__file__).parent.resolve()
MASTER_FILE = HERE / "crest_team_csa.html"

CLUBS = [
    {
        "id":            "skyline",
        "name":          "Skyline Soccer Club",
        "short":         "Skyline SC",
        "established":   "1965",
        "location":      "Denver, CO",
        "primary":       "#0050B4",
        "primaryD":      "#081E40",
        "primaryL":      "#0066D9",
        "accent":        "#F5C842",
        "accentL":       "#FFE08A",
        "textOnPrimary": "#FFFFFF",
        "logo":          "logo-skyline.png",
        "tagline":       "Powered by the CSA / CREST Education Program",
        "isCSA":         False,
    },
    {
        "id":            "pride",
        "name":          "Pride Soccer Club",
        "short":         "Pride SC",
        "established":   "1994",
        "location":      "Colorado",
        "primary":       "#A00028",
        "primaryD":      "#380010",
        "primaryL":      "#C0143C",
        "accent":        "#F0B400",
        "accentL":       "#F5CE3D",
        "textOnPrimary": "#FFFFFF",
        "logo":          "logo-pride.png",
        "tagline":       "Powered by the CSA / CREST Education Program",
        "isCSA":         False,
    },
    {
        "id":            "united",
        "name":          "Colorado United Soccer",
        "short":         "Colorado United",
        "established":   "1960",
        "location":      "Littleton, CO",
        "primary":       "#000078",
        "primaryD":      "#000038",
        "primaryL":      "#1414A0",
        "accent":        "#F0C83C",
        "accentL":       "#FFE070",
        "textOnPrimary": "#FFFFFF",
        "logo":          "logo-united.png",
        "tagline":       "Powered by the CSA / CREST Education Program",
        "isCSA":         False,
    },
    {
        "id":            "albion",
        "name":          "Albion Soccer Club",
        "short":         "Albion SC",
        "established":   "",
        "location":      "Boulder County, CO",
        "primary":       "#4A4A4A",   # slate gray — matches shield base
        "primaryD":      "#1A1A1A",   # near-black background
        "primaryL":      "#6A6A6A",   # hover gray
        "accent":        "#C81E1E",   # Albion red from the banner
        "accentL":       "#E84444",   # lighter red for highlights
        "textOnPrimary": "#FFFFFF",
        "logo":          "logo-albion.png",
        "tagline":       "Powered by the CSA / CREST Education Program",
        "isCSA":         False,
    },
]

CONFIG_RE = re.compile(r"const CLUB_CONFIG = \{.*?\};", re.DOTALL)

def build_config_js(club):
    keys = ["id","name","short","established","location",
            "primary","primaryD","primaryL","accent","accentL",
            "textOnPrimary","logo","tagline","isCSA"]
    out = "const CLUB_CONFIG = {\n"
    for k in keys:
        v = club[k]
        if isinstance(v, bool):
            jv = "true" if v else "false"
        else:
            jv = '"' + str(v).replace('"', '\\"') + '"'
        out += f"  {k}: {jv},\n"
    out += "};"
    return out

def transform(html, club):
    out = CONFIG_RE.sub(build_config_js(club), html, count=1)
    out = re.sub(
        r"<title>.*?</title>",
        f"<title>CREST Team \u00b7 {club['name']}</title>",
        out, count=1
    )
    out = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="CREST Team. {club["name"]}. Referee education and respect, powered by Colorado Soccer Association.">',
        out, count=1
    )
    # Swap the static favicon to this club's logo
    out = re.sub(
        r'<link rel="icon"[^>]*>',
        f'<link rel="icon" type="image/png" href="{club["logo"]}">',
        out, count=1
    )
    return out

def main():
    if not MASTER_FILE.exists():
        print(f"ERROR: cannot find {MASTER_FILE.name} in this folder.")
        print(f"       Make sure build_clubs.py sits next to crest_team_csa.html.")
        sys.exit(1)

    master = MASTER_FILE.read_text(encoding="utf-8")
    print(f"Master: {MASTER_FILE.name}  ({len(master):,} chars)\n")

    for club in CLUBS:
        out_file = HERE / f"crest_team_{club['id']}.html"
        out_file.write_text(transform(master, club), encoding="utf-8")
        print(f"  built  {out_file.name:32}  ({club['name']}, primary={club['primary']})")

    print(f"\nDone. {len(CLUBS)} club file(s) written to: {HERE}")
    print("Next step: commit and push to GitHub.")

if __name__ == "__main__":
    main()
