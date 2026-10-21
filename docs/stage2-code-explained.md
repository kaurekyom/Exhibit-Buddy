# Stage 2: The Code, Explained

New parts inside `index.html`:

- **GUIDES** (data): two complete hand-written guides, Paper Parachute and Pinhole Camera. Sizes are in millimetres.
- **Part types**: `rect`, `disc` (circle, optional numbered thread points), `frame` (a window in the middle), `box` (open-top box net with 4 glue tabs), `item` (loose thing, no template).
- **Guide.shape**: works out the flat outline, fold lines, tabs and holes of a part. For the box, the net is `(2h + w)` wide and `(2h + d)` tall.
- **Guide.layout**: places all pieces on A4 pages (210 x 297 mm) in rows ("shelf packing") with 10 mm margins, at true scale. The SVG uses 1 unit = 1 mm and the page is 210mm x 297mm, so 100% print is exact.
- **Guide.validate**: checks counts, sizes, part ids, that every part is used in a step, that steps with knife/pin/heat are marked "Ask an adult", that nothing unsafe is described, that text has no web addresses or code, and that each cut outline does not cross itself and has the expected area.
- **Guide.parse**: reads Claude's pasted reply. Finds the code block, reads the JSON, copies only known fields (so nothing extra can sneak in), then validates. All text is shown with text nodes, never as HTML.
- **Guide.rulesText**: the data shape and rules. It is added to the one prompt the student sends, so there is only one prompt to send and one reply to paste.
- **Guide.autoFix**: a part too big for A4 becomes a loose item with its size written out, and the app says so.
- **showGuide**: draws the page: materials, parts, templates, steps, safety, tests, troubleshooting, viva, glossary and a cross-check table.
