#!/usr/bin/env python3
"""
CREST Team — Club Variant Generator
Takes the CSA master HTML and produces per-club variants by swapping CLUB_CONFIG.
To add a new club later: append to CLUBS, drop the logo in the repo at logo-{id}.png, re-run.
"""

import re
import pathlib

MASTER = pathlib.Path("/home/claude/work/crest_team_csa.html").read_text()

CLUBS = [
    {
        "id":"skyline",
        "name":"Skyline Soccer Club",
        "short":"Skyline SC",
        "established":"1965",
        "location":"Denver, CO",
        "primary":"#0050B4",
        "primaryD":"#081E40",
        "primaryL":"#0066D9",
        "accent":"#F5C842",
        "accentL":"#FFE08A",
        "textOnPrimary":"#FFFFFF",
        "logo":"logo-skyline.png",
        "tagline":"Powered by the CSA / CREST Education Program",
        "isCSA":False,
    },
    {
        "id":"pride",
        "name":"Pride Soccer Club",
        "short":"Pride SC",
        "established":"1994",
        "location":"Colorado",
        "primary":"#A00028",
        "primaryD":"#380010",
        "primaryL":"#C0143C",
        "accent":"#F0B400",
        "accentL":"#F5CE3D",
        "textOnPrimary":"#FFFFFF",
        "logo":"logo-pride.png",
        "tagline":"Powered by the CSA / CREST Education Program",
        "isCSA":False,
    },
    {
        "id":"united",
        "name":"Colorado United Soccer",
        "short":"Colorado United",
        "established":"1960",
        "location":"Littleton, CO",
        "primary":"#000078",
        "primaryD":"#000038",
        "primaryL":"#1414A0",
        "accent":"#F0C83C",
        "accentL":"#FFE070",
        "textOnPrimary":"#FFFFFF",
        "logo":"logo-united.png",
        "tagline":"Powered by the CSA / CREST Education Program",
        "isCSA":False,
    },
]

CONFIG_RE = re.compile(r"const CLUB_CONFIG = \{.*?\};", re.DOTALL)

def js_literal(d):
    lines = ["const CLUB_CONFIG = {"]
    keys = ["id","name","short","established","location","primary","primaryD","primaryL",
            "accent","accentL","textOnPrimary","logo","tagline","isCSA"]
    for k in keys:
        v = d[k]
        if isinstance(v, bool):
            jv = "true" if v else "false"
        else:
            jv = '"' + str(v).replace('"','\\"') + '"'
        lines.append(f"  {k+',':16} {jv},")
    # remove trailing comma from last entry by rebuilding
    return "const CLUB_CONFIG = {\n" + "".join(
        f'  {k}: {("true" if v else "false") if isinstance(v,bool) else chr(34)+str(v).replace(chr(34),chr(92)+chr(34))+chr(34)},\n'
        for k,v in [(k, d[k]) for k in keys]
    ) + "};"

# Also swap title/meta
def transform(html, club):
    out = CONFIG_RE.sub(js_literal(club), html, count=1)
    # update <title>
    out = re.sub(
        r"<title>.*?</title>",
        f"<title>CREST Team — {club['name']}</title>",
        out, count=1
    )
    # update meta description
    out = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="CREST Team — {club["name"]}. Referee education and respect, powered by Colorado Soccer Association.">',
        out, count=1
    )
    return out

outdir = pathlib.Path("/home/claude/work")
for club in CLUBS:
    transformed = transform(MASTER, club)
    out = outdir / f"crest_team_{club['id']}.html"
    out.write_text(transformed)
    print(f"  ✓ {out.name}  ({club['name']}, primary={club['primary']})")

print("\nDone. Master file unchanged.")
