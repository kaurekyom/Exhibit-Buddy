# Stage 3: Student Steps, Code and Verification

## What the demo does
Every guide page (built-in or from Claude) now has a section called **Watch it go together**. Parts start in a tray. For each written step, the parts used in that step are highlighted, and a part moves into the assembly area at the first real step that uses it. A blue number on a part is that step number. The caption is the written step, word for word.

It shows **order and which parts are used**. It does NOT show exact positions or a 3D model, and it says so on the page. Follow the written step for how to fit things.

A step that starts with "Print" only gets the parts ready, so parts do not join the model there.

## Student steps (about 15 minutes)
1. Get the new code from Claude (paste `00-master-prompt.md` then `03-stage-animated-demo.md`), save it as `index.html`, refresh.
2. Open the Paper Parachute guide. Find **Watch it go together**.
3. Test each control:
   | Control | What should happen |
   |---|---|
   | Next / Previous | Step number and caption change; parts move |
   | Play | Steps advance by themselves; button says Pause |
   | Pause | It stops where it is |
   | Speed 0.5x / 1x / 2x | Slower or faster (press Play after changing if it was stopped) |
   | Restart | All parts return to the tray |
   | Reduce motion | Parts jump instead of sliding |
   | Left / Right arrow keys | Click the demo box first, then they change the step |
4. Compare: is every animation caption the same as the written step below it? Is the part letter the same as on the part card and the template?
5. Open the Pinhole Camera guide and check the **Ask an adult** tag shows in the caption at steps 4 and 7.
6. Make a guide with Claude for your own idea and run the demo on it.

## How the code works
- **Demo.buildSteps** copies each written step and works out when each part first joins the model.
- **Demo.layout** gives every part a place in the tray and in the assembly area.
- **Demo.stateAt(k)** says, after step k, which parts are placed and which are highlighted.
- **demoSection** draws it with SVG and CSS. The parts slide because CSS animates their position. The controls change the step number `k`.
- **Adding a new exhibit** needs no demo code. Any guide data (built-in or pasted) gets a demo from its `steps` and `parts` lists, so write each step's `parts` carefully.

## Step mapping (animation step = written step)
### Paper Parachute

| Animation step | Written step | Parts highlighted | Parts that join the model here |
|---|---|---|---|
| 1 | 1 | A | none |
| 2 | 2 | A | A |
| 3 | 3 | B | B |
| 4 | 4 | A, B | none |
| 5 | 5 | B | none |
| 6 | 6 | B, C | C |
| 7 | 7 | A, B | none |

### Pinhole Camera

| Animation step | Written step | Parts highlighted | Parts that join the model here |
|---|---|---|---|
| 1 | 1 | A, B, C, D | none |
| 2 | 2 | A, B, C, D | A, B, C, D |
| 3 | 3 | A, B, C, D | none |
| 4 | 4 | A, C | none |
| 5 | 5 | A, C | none |
| 6 | 6 | A, B | none |
| 7 | 7 | A, B, E | E |
| 8 | 8 | A | none |
| 9 | 9 | A | none |
| 10 | 10 | C, D | none |
| 11 | 11 | A, C | none |

## Verification
- 119 automated checks: same step count, order, wording and Ask-an-adult flags as the written steps; every part joins once, at a step that lists it; no two parts share a spot and all spots are inside the picture; start state, end state and highlighted parts at every step; Next, Previous, Restart, Play, Pause, speed (2x faster than 0.5x), run-to-end, restart-after-end, timer cleared on leaving the page, Reduce motion, arrow keys. Tested on both built-in guides and on the 17-part digestive-system guide Claude produced.
- Real Chromium screenshots at desktop and phone width: no script errors, controls usable, caption readable.
- Earlier checks: 692 (Stage 1) and 132 (Stage 2) still pass.

Bugs found and fixed: the caption showed the word "null" after step 1; the tray was too short for 17 parts; "Print the templates" made every part appear at step 1.

## NOT verified
1. The animation shows order only. It cannot show that a part fits where the step says.
2. On a phone the picture is small, so part names are tiny; the caption carries the real information.
3. "Reduce motion" follows the device setting at the start and the checkbox afterwards. Tested with the checkbox only.
4. No screen reader test. The picture has a text description, and the live caption is announced when it changes in browsers that support this, but this was not heard on a real screen reader.
5. Which parts a step lists comes from the guide data. If Claude lists the wrong parts in a step, the demo repeats that mistake.
