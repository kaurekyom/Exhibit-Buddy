# Stage 2: Verification Note

| Check | Method | Result |
|---|---|---|
| Both built-in guides pass the validator with no errors or warnings | jsdom tests | Pass |
| Pieces stay inside the page margins and never overlap | Layout tests | Pass |
| Box net outline does not cross itself; area equals the formula (60x60x60 = 20280 mm2; 5 other sizes) | Geometry tests | Pass |
| Sheet is 210mm x 297mm, viewBox 210x297, scale bar is 50 units | UI tests | Pass |
| 28 kinds of bad guide are rejected (bad ids, sizes, unknown parts, missing adult labels, unsafe text, URLs, HTML, long text) | Mutation tests | Pass |
| Pasted-reply import: fenced, plain, with chatter, broken, empty, huge, wrong types, prototype pollution, HTML | Import tests | Pass |
| Rendered in real Chromium; sheets looked at; template-only print gives 1 page | Screenshots and PDF | Pass |
| Stage 1 regression | 692 earlier checks | Pass |

Total: 132 new checks and 692 earlier checks, 0 failed, no page script errors.

Fixed after the first user trial: the two-prompt flow was confusing, so it is now one prompt and one paste. A real Claude reply for the digestive system failed on a 280 mm part; oversize parts now become loose items and the guide builds (tested with that exact reply).

Fixed during testing: scale-bar text ran off the page; template-only print also printed the guide header.

## NOT verified
1. **Physical builds.** Nobody has built either model from these templates. Sizes are checked by code only. Build both once and note any problems.
2. **Science and numbers.** Statements (air resistance, inverted image, 250 mm threads, 15 g clay, 15 mm pinhole window) have not been checked by a teacher or textbook. The pinhole model is a simple design; a very small hole makes a dim picture.
3. **Printers.** True scale depends on the student choosing Actual size. Tested only with Chromium's PDF output, not real printers or other browsers.
4. **Claude-written guides.** The app checks structure, sizes and safety words only. Claude's science and measurements can still be wrong; a teacher must review.
5. **Safety words are a short list**; a dangerous step worded unusually could pass.
6. **Accessibility** not tested with a screen reader; part drawings have text labels only.
