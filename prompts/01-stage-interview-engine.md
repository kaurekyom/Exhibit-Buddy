# Stage 1: Interview Engine and Exhibit Idea Library

Paste the master prompt (00-master-prompt.md) first, then this stage prompt. Run Stage 1 completely before moving on.

```
Stage 1 of 4. Build ONLY the interview engine and the exhibit idea library.
Do not build the guide renderer, animation or hosting steps yet.

DELIVER
1. A single index.html with:
   - A friendly start screen ("Exhibit Buddy: plan your science exhibit").
   - The adaptive interview (max 5 questions, one at a time, big buttons
     plus an optional text box) and an optional "class or age" field.
   - A "Here is what I understood" summary screen with Confirm / Change.
   - A safety screen that refuses unsafe ideas (no way to continue) and
     shows cautions for risky ones (lasers, nuclear, mains, advanced topics).
   - A screen for ideas that are not in the library: say so plainly and
     offer Claude-assisted mode first.
2. A JavaScript exhibit idea library (a JS object inside index.html) with at
   least 24 ideas across school science: motion and force, gravity and
   buoyancy, work and energy, sound, light and mirrors, electricity with
   batteries only, matter and mixtures, chemical reactions, atoms, cells and
   tissues, the human body (for example the digestive system and breathing),
   plants, animals and health, earth and space, natural resources and food.
   For each idea store: id, title, topic area, the science concept, working
   or static model, difficulty (easy/medium/hard), time in hours, main
   materials, safety level, and keywords for matching my answers.
   Do NOT claim an idea matches a particular syllabus or textbook chapter.
3. The decision logic: how my answers are matched to ideas, how the engine
   decides it has enough information, and what it does when nothing matches
   or only related ideas match (offer Claude-assisted mode first and show the
   student's own words).
4. Claude-assisted mode: the app writes a ready-made prompt (idea, class or
   age, cautions, instructions). A button opens https://claude.ai/new?q=<the
   prompt, URL-encoded> in a new tab and ALSO copies the prompt. Show a
   readable copy of the prompt, a "Copy again" button, and plain instructions
   for when Claude opens with an empty box. If the prompt is too long for a
   link, open a blank chat instead.

RULES
- No API key, no server, no external libraries. The only link the app may
  open is claude.ai/new.
- Every science statement in the library must be correct. Flag any you are
  unsure about instead of guessing.
- Show typed text as plain text, never as HTML.
- Explain every part of the code to me in simple English after the code.

AT THE END
Give me: (a) how to test this stage by opening the file in my browser,
(b) test answers to try, including one unsafe idea, one idea that is not
in the library, and one body-organ idea (for example "digestive system"),
and (c) a short verification note for this stage.
```
