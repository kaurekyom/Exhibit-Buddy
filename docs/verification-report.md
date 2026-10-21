# Verification report (Exhibit Buddy)

Date of report: 21 October 2026. Status: **not yet reviewed by a teacher or built by a student.**
Legend: ✅ checked by running code or by eye · 🔶 checked by the author only (needs a teacher) · ❌ not verified.

## 1. What was tested by code
| Area | Result |
|---|---|
| Interview engine, routing, unsafe-idea refusal (`test_v2.js`, 692 checks) | ✅ pass |
| Guide import from Claude, validation, A4 fit, true-scale templates (`test_v3.js`, 132) | ✅ pass |
| Tray demo order equals written step order (`test_v4.js`, 119) | ✅ pass |
| 3D models, pictures, labelled figures, hostile input (`test_v5.js`, 256) | ✅ pass |
| No outside files or scripts are loaded; the only web addresses in the file are the SVG standard and the two claude.ai links | ✅ |
`test_stage1.js` is an old script that was replaced by `test_v2.js`; ignore it.

## 2. Facts in the built-in material (all 🔶: need a teacher)
These were written from general science knowledge. They were **not** compared line by line with a textbook in this project.
- **Pinhole camera**: light travels in straight lines; the image is upside down and left-right reversed; a smaller hole gives a sharper but dimmer image; black inside reduces stray light.
- **Paper parachute**: gravity pulls down; air resistance pushes up and grows with canopy area; a larger canopy falls more slowly.
- **Animal cell**: membrane, cytoplasm, nucleus (DNA, nucleolus), mitochondria (respiration, ATP), endoplasmic reticulum (rough and smooth), Golgi apparatus, ribosomes, lysosomes.
- **Carbon atom**: 6 protons, 6 neutrons (carbon-12), 6 electrons, K shell 2 and L shell 4 (electron arrangement 2, 4); the nucleus is about 100,000 times smaller than the atom.
- **Solar system**: eight planets in order; Mercury about 88 days and Neptune about 165 years per orbit; Sun holds about 99.8% of the mass; Venus is the hottest planet; Mars is red from iron oxide; Uranus found in 1781.
Teacher action: tick each bullet in `docs/teacher-review-checklist.md`.

## 3. Dimension cross-check
- ✅ Every part has a template or is a loose item; templates fit A4; every part in the steps exists; every part is used (code-checked).
- ✅ Templates are drawn at 1 unit = 1 mm with a 50 mm scale bar on each sheet.
- ❌ Nobody has printed on a real printer and measured the scale bar.
- ❌ Nobody has built a model from the guide.

## 4. Safety review (🔶)
- Steps with pins, craft knives, scissors, hot glue and similar are labelled "Ask an adult" by a word list; unsafe ideas (fire, chemicals, electricity at mains level, weapons and similar) are refused by a keyword screen.
- A keyword screen is **not** a complete safety check. Words it does not know will pass. A teacher must read every Claude-made guide before the student starts.

## 5. Accessibility
- ✅ Keyboard use: all buttons work; figure parts are focusable and respond to Enter; the 3D demo responds to arrow keys.
- ✅ Reduce motion: toggle in the 3D demo; figures start paused if the device asks for reduced motion.
- ✅ Phone width (390 px): no sideways scrolling in the pages tested.
- 🔶 Font size and colour contrast chosen for readability but not measured with a contrast tool.
- ❌ Not tested with a screen reader. Pictures have text labels, but the 3D model itself is not described in detail.

## 6. Assumptions and open risks
1. Claude's replies can contain wrong science. The app checks structure, not truth.
2. The "Open Claude with this prompt" link is **not tested on live claude.ai**. Fallback: the prompt is copied; paste it.
3. In pinhole step 10 the 3D lid shows small dark gaps at two top corners (drawing issue only).
4. Figures drawn by Claude are checked for shape and safety of text only.
5. Planets are not to scale and speeds are for show (stated in the figure).
6. Only two built-in build guides exist; all other build topics rely on Claude.
