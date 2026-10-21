#!/usr/bin/env python3
"""Turn every .md file into a .html page (needs pandoc). Run from the repo root:  python3 tools/build-docs.py"""
import re, subprocess, pathlib, html
root = pathlib.Path(__file__).resolve().parent.parent
CREDIT = "Created by Ekyom Kaur, Class 9, PMS Alwal, Secunderabad"
CSS = """<style>
:root{--bg:#f5f8fc;--card:#fff;--fg:#1b2430;--muted:#55627a;--line:#d5deea;--p:#0b4f9c;--p2:#e3effc;--code:#eef2f7;--ok:#e9f7ee;--warn:#fff6e0}
@media (prefers-color-scheme:dark){:root{--bg:#0f141a;--card:#171e26;--fg:#e8ecf1;--muted:#a3b0c2;--line:#2f3b4a;--p:#8ab8f0;--p2:#1b2a3d;--code:#1d252f;--ok:#14281c;--warn:#2e2711}}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:70px}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--p)}a:focus-visible,button:focus-visible{outline:3px solid #000;outline-offset:2px}
.bar{position:sticky;top:0;z-index:5;background:#0b4f9c;color:#fff;display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center;padding:10px 16px}
.bar a{color:#fff;text-decoration:none;font-weight:600}.bar a:hover{text-decoration:underline}.bar .brand{font-size:1.1rem;margin-right:auto}
.hero{background:linear-gradient(135deg,#0b4f9c,#1a73c9);color:#fff;padding:28px 16px 24px}
.hero .in{max-width:50rem;margin:0 auto}.hero h1{margin:.1em 0 .2em;font-size:clamp(1.6rem,5vw,2.3rem);line-height:1.2}
.hero p{margin:.3em 0;opacity:.95}.crumb{font-size:.9rem;opacity:.9}.crumb a{color:#fff}
.credit{display:inline-block;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.4);border-radius:999px;padding:4px 14px;font-size:.92rem;margin-top:10px}
main{max-width:50rem;margin:0 auto;padding:20px 16px 8px}
.content{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:8px 22px 22px}
h1{font-size:1.9rem}h2{font-size:1.45rem;margin-top:1.8em;padding-top:.2em;border-top:2px solid var(--p2)}h2:first-child{border:0;margin-top:.8em}h3{font-size:1.15rem;margin-top:1.4em}
h1,h2,h3{line-height:1.3}
.content>h1:first-child{display:none}
pre{position:relative;background:var(--code);padding:14px;border-radius:10px;overflow:auto;white-space:pre-wrap;word-break:break-word;font-size:15px;border:1px solid var(--line)}
code{background:var(--code);padding:1px 5px;border-radius:5px;font-size:.9em}pre code{padding:0;background:none}
.copy{position:absolute;top:6px;right:6px;font:600 13px system-ui;background:var(--p);color:#fff;border:0;border-radius:6px;padding:5px 10px;cursor:pointer}
blockquote{margin:1em 0;padding:.4em 1em;background:var(--warn);border-left:5px solid #e0a800;border-radius:0 8px 8px 0}
table{border-collapse:collapse;display:block;overflow-x:auto;margin:1em 0;max-width:100%}th,td{border:1px solid var(--line);padding:8px 12px;text-align:left;vertical-align:top}
th{background:var(--p2)}tr:nth-child(even) td{background:rgba(120,140,170,.07)}
li{margin:.3em 0}ul.task,li:has(>input[type=checkbox]){list-style:none}input[type=checkbox]{width:1.15em;height:1.15em;margin:0 .5em 0 -1.3em;vertical-align:-.15em}
.toc{background:var(--p2);border-radius:12px;padding:12px 18px;margin:0 0 18px}.toc strong{display:block;margin-bottom:4px}
.toc ol{margin:0;padding-left:1.3em;columns:1}@media(min-width:700px){.toc ol{columns:2;column-gap:28px}}.toc li{margin:.15em 0;font-size:.97rem;break-inside:avoid}
.pn{display:flex;gap:12px;justify-content:space-between;flex-wrap:wrap;margin:22px 0 4px}.pn a{flex:1 1 220px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;text-decoration:none;font-weight:600}.pn a small{display:block;color:var(--muted);font-weight:400}.pn a:hover{border-color:var(--p)}.pn .nx{text-align:right}
footer{max-width:50rem;margin:0 auto;padding:18px 16px 36px;font-size:.92rem;color:var(--muted);text-align:center}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin:12px 0 8px}
.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;text-decoration:none;color:var(--fg);transition:transform .12s,border-color .12s}
.card:hover{border-color:var(--p);transform:translateY(-2px)}.card b{display:block;color:var(--p);font-size:1.02rem;margin-bottom:2px}.card span{font-size:.93rem;color:var(--muted)}
.card.big{background:var(--p2);border-color:var(--p)}.card.big b{font-size:1.15rem}
.sec h2{border:0;margin:1.6em 0 .2em}.sec p.sub{margin:.1em 0 .4em;color:var(--muted)}
@media print{.bar,.hero .crumb,.pn,.copy,.toc{display:none}.hero{background:none;color:#000;padding:0}.content{border:0;padding:0}body{background:#fff;color:#000;font-size:12pt}.credit{border-color:#000;background:none;color:#000}}
</style>"""
JS = """<script>document.querySelectorAll('pre').forEach(function(p){var b=document.createElement('button');b.className='copy';b.type='button';b.textContent='Copy';b.setAttribute('aria-label','Copy this block');b.onclick=function(){var t=p.innerText.replace(/Copy$/,'').trim();var done=function(){b.textContent='Copied!';setTimeout(function(){b.textContent='Copy'},1500)};if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(done,function(){})}else{var r=document.createRange();r.selectNodeContents(p);var s=getSelection();s.removeAllRanges();s.addRange(r);try{document.execCommand('copy');done()}catch(e){}}};p.appendChild(b)});</script>"""
def esc(s): return html.escape(s)
def shell(title, hero_sub, crumb, body, up, extra=""):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} - Exhibit Buddy</title><meta name="author" content="Ekyom Kaur">{CSS}</head><body>
<nav class="bar" aria-label="Site"><a class="brand" href="{up}index.html">Exhibit Buddy help</a><a href="{up}index.html">All help pages</a><a href="{up}../index.html">Open the app</a></nav>
<div class="hero"><div class="in"><div class="crumb">{crumb}</div><h1>{esc(title)}</h1>{('<p>'+esc(hero_sub)+'</p>') if hero_sub else ''}<span class="credit">{CREDIT}</span></div></div>
<main>{body}</main>
<footer>{CREDIT}.<br>Exhibit Buddy helps a student plan a science exhibit. A teacher should check the science. <a href="{up}../index.html">Open the app</a></footer>{JS}</body></html>"""
# ---- page list, in reading order ----
DOCS = "docs"; PR = "prompts"
G = [
 ("Start here", "Read these first.", [
   ("docs/about.html", "README.md", "About Exhibit Buddy", "What it is, how a student uses it, and how to put it on GitHub Pages."),
   ("docs/claude-project-instructions.html", "docs/claude-project-instructions.md", None, "Instructions to paste into a Claude Project so every chat follows the rules.")]),
 ("How this project was created", "The prompts used to build the app, in the order they were run. You can reuse them to build your own.", [
   (f"prompts/{p.stem}.html", f"prompts/{p.name}", None, None) for p in sorted((root/PR).glob("*.md"))]),
 ("How it works", "The code explained in simple English, stage by stage.", [
   ("docs/stage1-code-explained.html", "docs/stage1-code-explained.md", None, "Stage 1: the question-and-answer engine."),
   ("docs/stage2-code-explained.html", "docs/stage2-code-explained.md", None, "Stage 2: turning a plan into a guide with true-size templates."),
   ("docs/stage3-demo.html", "docs/stage3-demo.md", None, "Stage 3: the animated tray demo."),
   ("docs/stage3b-3d-and-figures.html", "docs/stage3b-3d-and-figures.md", None, "Stage 3b: 3D models, step pictures and labelled figures (cells, atoms, planets).")]),
 ("What the student does", "Step-by-step help for the student building and testing the app.", [
   ("docs/stage1-student-steps.html", "docs/stage1-student-steps.md", None, "Create, open and test Stage 1."),
   ("docs/stage2-student-steps.html", "docs/stage2-student-steps.md", None, "Build, print and test the guides.")]),
 ("Checks, tests and honest limits", "What was tested, what was not, and what a teacher should check.", [
   ("docs/verification-report.html", "docs/verification-report.md", None, "The full report: tests, facts, safety, accessibility, open risks."),
   ("docs/teacher-review-checklist.html", "docs/teacher-review-checklist.md", None, "A checklist a science teacher fills in before a guide is used."),
   ("docs/verification-checklist.html", "docs/verification-checklist.md", None, "A tick list for the student after every stage."),
   ("docs/stage1-verification-note.html", "docs/stage1-verification-note.md", None, "Stage 1 tests and limits."),
   ("docs/stage2-verification-note.html", "docs/stage2-verification-note.md", None, "Stage 2 tests and limits.")]),
]
order = [(g[0], r) for g in G for r in g[2]]
def title_of(md):
    m = re.search(r"^#\s+(.+)$", (root/md).read_text(encoding="utf-8"), re.M); return m.group(1).strip() if m else pathlib.Path(md).stem
def first_para(md):
    t = (root/md).read_text(encoding="utf-8"); t = re.sub(r"```.*?```", "", t, flags=re.S)
    for para in t.split("\n\n"):
        p = para.strip()
        if p and not p.startswith(("#", "-", "|", ">", "`", "*")) and len(p) > 30: return re.sub(r"[*_`]", "", p).replace("\n", " ")[:150].rstrip() + ("…" if len(p) > 150 else "")
    return ""
info = {}
for i, (gname, (out, md, ttl, desc)) in enumerate(order):
    t = ttl or title_of(md); info[out] = dict(title=t, desc=desc or first_para(md), group=gname, md=md, i=i)
def render(out):
    d = info[out]; up = "../docs/" if out.startswith("prompts/") else ""
    text = (root/d["md"]).read_text(encoding="utf-8")
    body = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"], input=text, capture_output=True, text=True, check=True).stdout
    body = re.sub(r'href="(?:\.\./)?(?:docs/)?README\.md(#[^"]*)?"', lambda k: 'href="%sabout.html%s"' % (up, k.group(1) or ""), body)
    body = re.sub(r'href="([^":#]+)\.md(#[^"]*)?"', lambda k: 'href="%s.html%s"' % (k.group(1), k.group(2) or ""), body)
    body = body.replace('disabled=""', "")
    body = re.sub(r"<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.S)   # the title is shown in the banner
    h2 = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, flags=re.S)
    toc = ""
    if len(h2) >= 4:
        toc = '<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>' + "".join(f'<li><a href="#{a}">{re.sub("<[^>]+>", "", b)}</a></li>' for a, b in h2) + "</ol></nav>"
    nav = ""
    i = d["i"]; prev = order[i-1][1][0] if i else None; nxt = order[i+1][1][0] if i+1 < len(order) else None
    link = lambda o, lab, cls: f'<a class="{cls}" href="{("../" if out.startswith("prompts/") and o.startswith("docs/") else "")}{o if not out.startswith("prompts/") or o.startswith("docs/") else o.split("/",1)[1]}'.replace('href="../docs/', 'href="../docs/') + f'"><small>{lab}</small>{esc(info[o]["title"])}</a>'
    def href(o):
        if out.startswith("prompts/"): return ("../" + o) if o.startswith("docs/") else o.split("/", 1)[1]
        return o.split("/", 1)[1] if o.startswith("docs/") else "../" + o
    nav = '<div class="pn">' + (f'<a href="{href(prev)}"><small>← Previous</small>{esc(info[prev]["title"])}</a>' if prev else "<span></span>") + (f'<a class="nx" href="{href(nxt)}"><small>Next →</small>{esc(info[nxt]["title"])}</a>' if nxt else "") + "</div>"
    crumb = f'<a href="{up}index.html">Help</a> › {esc(d["group"])}'
    pathlib.Path(root/out).write_text(shell(d["title"], d["desc"], crumb, f'<div class="content">{toc}{body}</div>{nav}', up), encoding="utf-8")
for out in info: render(out)
# fix any stray README links
for f in list((root/"docs").glob("*.html")) + list((root/"prompts").glob("*.html")):
    f.write_text(f.read_text(encoding="utf-8").replace("README.html", "about.html"), encoding="utf-8")
# ---- index ----
cards = lambda items: '<div class="cards">' + "".join(f'<a class="card" href="{o.split("/",1)[1]}"><b>{esc(info[o]["title"])}</b><span>{esc(info[o]["desc"])}</span></a>' for o in items) + "</div>"
start = '<div class="cards"><a class="card big" href="../index.html"><b>Open the app</b><span>Plan an exhibit, build a guide, explore labelled figures.</span></a><a class="card big" href="about.html"><b>How to use it</b><span>Short guide for students, and how to publish on GitHub Pages.</span></a><a class="card big" href="verification-report.html"><b>How well was it checked?</b><span>Tests, safety, and what is still not verified.</span></a></div>'
secs = ""
for gname, sub, rows in G:
    outs = [r[0] for r in rows]
    outs = [o if not o.startswith("prompts/") else o for o in outs]
    c = '<div class="cards">' + "".join(f'<a class="card" href="{(o if o.startswith("prompts/") else o.split("/",1)[1]).replace("prompts/","../prompts/")}"><b>{esc(info[o]["title"])}</b><span>{esc(info[o]["desc"])}</span></a>' for o in outs) + "</div>"
    secs += f'<section class="sec"><h2>{esc(gname)}</h2><p class="sub">{esc(sub)}</p>{c}</section>'
intro = f'<div class="content" style="background:none;border:0;padding:0"><p style="font-size:1.1rem">Everything about the project in one place: how it was created, how it works, how to use it, and how well it has been checked. All pages are plain web pages, so they work on a phone and print cleanly.</p>{start}{secs}</div>'
(root/"docs/index.html").write_text(shell("Exhibit Buddy help and documentation", "A science exhibit planner for school students, with step-by-step help.", "Help", intro, ""), encoding="utf-8")
print("built", len(info) + 1, "pages")
