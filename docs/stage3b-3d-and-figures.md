# Stage 3b: 3D assembly models, pictures and labelled figures

This stage answers the feedback "show me drawings and clear visuals of how the parts fit together" and "there should be something similar for biology, cells and atoms".

## What the student sees

### 1. Build-it exhibits (pinhole camera and paper parachute are built in)
- **How the parts fit together**: shaded 3D pictures (parts laid out, exploded view) plus a flat "How it works" diagram (light rays, or forces).
- **Watch it go together**: a 3D model that folds, flips and joins the parts step by step. Controls: Play, Previous, Next, Restart, speed, Turn left/right, Tilt, Reset view, Reduce motion. Drag the model to turn it. Arrow keys change step; Shift + arrow keys turn the model. A readout shows live numbers (for example "Foil moved onto the base: 100%").
- **A picture under every written step**. These also print.
- Part letters in the pictures match the letters on the part cards and templates.

### 2. Guides written by Claude (any topic)
These still use the tray animation. A box "Add pictures that show how the parts fit together" gives the student one prompt for Claude and one paste box. The app checks every picture before showing it.

### 3. Labelled figures (cells, atoms, animals, planets, any topic)
Start screen → "Explore a labelled figure".
- Built in: **animal cell**, **carbon atom (Bohr model)**, **solar system**.
- Tap a part, or press its button, to read what it is and what it does. Parts have keyboard focus; Enter selects.
- Parts can move in orbits (electrons, planets). "Pause the moving parts" stops them; the app starts paused if the device asks for reduced motion.
- "Test me": asks "Which part is the …?", says Yes/Not quite, and scores first-try answers.
- "Plan it with Claude": the same one-prompt, one-paste flow as the guides, for any topic.

## How it is built (for the student to read)
Everything is in `index.html`.
- `Studio` (section 2E) is a small 3D engine: faces in millimetres, a turn-and-tilt camera, four-tone shading, far-to-near drawing order. Each model lists its parts and says where they are after each step.
- `Scenes` (section 2D) checks flat pictures from Claude. `Figures` (section 2F) checks labelled figures. They only accept known shapes, known colours, numbers in range and plain text (no `<`, `>` or web addresses), and they build the page with text nodes only, never `innerHTML`.
- Built-in figures pass through the same checker as Claude's figures. During development the checker rejected one of our own colour names.

## Tests (run with Node + jsdom)
`test_v5.js` (256 checks): model step counts, every coordinate a number at every step and animation time, tab strips inside the box, demo controls and keyboard, a picture under every step, the add-pictures flow, malformed and hostile input (markup, web addresses, out-of-range numbers, unknown shapes, prototype pollution), figure selection by click, button and Enter, orbit movement, quiz scoring, the carbon atom (2 + 4 electrons, 6 protons, 6 neutrons), the solar system (Sun + 8 planets in distance order), unsafe-topic refusal.
`test_v2` to `test_v4` still pass (692, 132, 119). `test_stage1` is an early script that was replaced by `test_v2` and is no longer used.
Screenshots from Chromium were checked by eye on desktop and a 390 px phone width.

## Honest limits
- Not tried on real phones, printers or screen readers.
- Nobody has built the models from the guides yet. The 3D model shows the intended result; the student must still follow the written steps.
- The pinhole 3D lid has small dark gaps at two top corners in step 10 (the lid is drawn slightly smaller than the box opening). It does not affect the instructions.
- Figures are simplified (see each figure's note). A teacher must check the science. The app cannot verify facts in figures drawn by Claude.
- The "Open Claude with this prompt" link has not been tested on live claude.ai. If the box opens empty, the prompt is already copied; paste it.
- Planets are not to scale and their speeds are for show; the figure says so.
