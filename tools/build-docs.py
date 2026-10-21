#!/usr/bin/env python3
"""Turn every .md file into a .html page (needs pandoc). Run from the repo root:  python3 tools/build-docs.py"""
import re, subprocess, pathlib, html
root = pathlib.Path(__file__).resolve().parent.parent
CSS = """<style>
:root{--bg:#fff;--fg:#1a1a1a;--line:#c9d1dc;--p:#0b4f9c;--code:#f1f4f8}
@media (prefers-color-scheme:dark){:root{--bg:#14181d;--fg:#e8ecf1;--line:#3a4452;--p:#8ab8f0;--code:#1d242c}}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
header{background:#0b4f9c;color:#fff;padding:14px 16px}header a{color:#fff;font-weight:700;text-decoration:none}
main{max-width:46rem;margin:0 auto;padding:16px}
a{color:var(--p)}h1,h2,h3{line-height:1.25}h2{border-bottom:1px solid var(--line);padding-bottom:4px;margin-top:2em}
pre{background:var(--code);padding:12px;border-radius:8px;overflow:auto;white-space:pre-wrap;word-break:break-word;font-size:15px}
code{background:var(--code);padding:1px 4px;border-radius:4px;font-size:.92em}pre code{padding:0;background:none}
table{border-collapse:collapse;display:block;overflow-x:auto}td,th{border:1px solid var(--line);padding:6px 10px;text-align:left}
img{max-width:100%}li{margin:.2em 0}input[type=checkbox]{width:1.1em;height:1.1em;margin-right:.4em}
footer{max-width:46rem;margin:0 auto;padding:16px;font-size:15px;opacity:.8}
@media print{header,footer{display:none}body{font-size:12pt}pre{white-space:pre-wrap}}
</style>"""
def page(title, body, up):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} - Exhibit Buddy</title>{CSS}</head><body>
<header><a href="{up}index.html">Exhibit Buddy: documentation</a> &nbsp; <a href="{up}../index.html" style="font-weight:400">Open the app</a></header>
<main>{body}</main><footer>Part of the Exhibit Buddy project. Not reviewed by a teacher unless the verification report says so.</footer></body></html>"""
def conv(md_path, out_path, up):
    text = md_path.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.+)$", text, re.M); title = m.group(1).strip() if m else md_path.stem
    body = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"], input=text, capture_output=True, text=True, check=True).stdout
    body = re.sub(r'href="([^":#]+)\.md(#[^"]*)?"', lambda k: 'href="%s.html%s"' % (k.group(1), k.group(2) or ""), body)
    body = body.replace('disabled=""', "")
    out_path.write_text(page(title, body, up), encoding="utf-8"); return title
groups = [
 ("Start here", [("docs/about.html", root/"README.md", "About Exhibit Buddy, how to use it, how to publish it"), ("docs/claude-project-instructions.html", None, None)]),
 ("How this project was created (the prompts, in order)", [(f"prompts/{p.stem}.html", p, None) for p in sorted((root/"prompts").glob("*.md"))]),
 ("How it works (the code explained in simple English)", [(f"docs/{n}.html", None, None) for n in ["stage1-code-explained","stage2-code-explained","stage3-demo","stage3b-3d-and-figures"]]),
 ("What the student does", [(f"docs/{n}.html", None, None) for n in ["stage1-student-steps","stage2-student-steps"]]),
 ("Checks, tests and honest limits", [(f"docs/{n}.html", None, None) for n in ["verification-report","stage1-verification-note","stage2-verification-note","verification-checklist","teacher-review-checklist"]]),
]
titles = {}
for p in sorted((root/"docs").glob("*.md")): titles["docs/"+p.stem+".html"] = conv(p, p.with_suffix(".html"), "")
for p in sorted((root/"prompts").glob("*.md")): titles["prompts/"+p.stem+".html"] = conv(p, p.with_suffix(".html"), "../docs/")
titles["docs/about.html"] = conv(root/"README.md", root/"docs/about.html", "")
# the README is linked from prompts and docs pages as README.md -> README.html; point that to about.html
for f in list((root/"docs").glob("*.html")) + list((root/"prompts").glob("*.html")):
    t = f.read_text(encoding="utf-8").replace("README.html", "about.html"); f.write_text(t, encoding="utf-8")
items = []
for g, rows in groups:
    li = []
    for path, _, desc in rows:
        li.append(f'<li><a href="{path.replace("docs/","",1) if path.startswith("docs/") else "../"+path}">{html.escape(titles.get(path, path))}</a></li>')
    items.append(f"<h2>{html.escape(g)}</h2><ul>{''.join(li)}</ul>")
intro = "<h1>Exhibit Buddy: documentation</h1><p>Everything about the project in one place: how it was created, how it works, how to use it, and how well it has been checked.</p><p><a href='../index.html'><strong>Open the app</strong></a></p>"
(root/"docs/index.html").write_text(page("Documentation", intro + "".join(items), ""), encoding="utf-8")
print("built", len(titles), "pages")
