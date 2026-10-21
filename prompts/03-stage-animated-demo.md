# Stage 3: Animated Assembly Demo

Run this after Stage 2 works. Paste your current index.html along with this prompt.

```
Stage 3 of 4. Here is my current index.html from Stage 2 (pasted below).
Add the animated assembly demo. Do not remove anything that already works.

DELIVER
An animated assembly demo for each of the two sample exhibits, using only
HTML, CSS, SVG and JavaScript (no libraries):
1. Numbered parts appear in an exploded layout, each labelled with the same
   part number used in the component cards and templates.
2. Parts move into position one assembly step at a time, in the same order
   as the written assembly sequence.
3. A caption under the animation for each step, with the same wording as
   the written step.
4. Controls: Play, Pause, Previous step, Next step, Restart, and a speed
   selector (0.5x, 1x, 2x). Controls must work with keyboard and touch.
5. A step counter ("Step 3 of 8") and highlighted part numbers.
6. An option to reduce motion for accessibility (respect the
   prefers-reduced-motion setting and offer a manual toggle).
7. The demo data must be a simple JS array of steps (part, from, to,
   caption) so any new exhibit can reuse the same animation engine.

RULES
- The animation must not contradict the written instructions: same step
  order, same part numbers, same final shape.
- No reliance on color alone to identify parts.
- Works on a phone screen.

AT THE END
Give me: (a) a table mapping each animation step to its written step and
part numbers, (b) how to test play, pause, next, previous and speed, and
(c) how to add a new exhibit to the animation engine.
```
