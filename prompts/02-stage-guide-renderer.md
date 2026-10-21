# Stage 2: Guide Renderer (Materials, Components, Printable Templates)

Run this after Stage 1 works. Paste your current index.html into the chat along with this prompt so Claude builds on it.

```
Stage 2 of 4. Here is my current index.html from Stage 1 (pasted below).
Extend it. Do not remove anything that already works.

FIRST (research, if you can browse)
Visit the Canon Creative Park paper-craft site and study how a finished
model is broken into parts, templates, fold/cut/glue marks and numbered
steps. This is for your reference only. Do NOT mention Canon anywhere and
do not copy templates. If you cannot access it, tell me and I will paste
example pages.

DELIVER
Build the guide renderer that turns a confirmed idea into a full HTML guide:
1. Header: title, the science concept, difficulty, time, "Why it works".
2. Materials list: item, quantity, size, local source, and a note when a
   non-paper material is used and why paper would not work.
3. Component cards: one numbered card per part with a drawing, dimensions
   in cm/mm, and cut/fold/glue steps.
4. Printable A4 templates as inline SVG at true scale (1 SVG unit = 1 mm),
   with solid cut lines, dashed fold lines, numbered glue tabs, and a
   scale-check ruler (e.g. a 5 cm bar) so I can confirm my printer did not
   resize the page. Add print CSS so each template prints on its own page.
5. Numbered assembly sequence (Step 1..N) linked to part numbers.
6. Safety notes with "Ask an adult" labels, a testing checklist,
   troubleshooting tips, 3 viva questions with model answers, a glossary.
7. Write full guide content for TWO ideas from the library so I can test:
   one very simple paper model and one working model.

RULES
- Dimensions in the templates must match the dimensions in the component
  cards and the assembly steps. Part counts must match the materials list.
- If any number, formula or fact cannot be verified, say so.
- Mobile-friendly, readable fonts, good contrast.

AT THE END
Give me: (a) a cross-check table (part number, template size, card size,
step number, material count) proving everything matches, and (b) how to
test printing at 100 percent scale.
```
