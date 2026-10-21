# Exhibit Buddy: Master Prompt (RTCCO)

Use this as the reference spec. Run it in four stages (see the other files in this folder) rather than all at once.

This version is generic: it works for any school science topic and any class. It is not tied to one board or syllabus.

```
# ROLE
I am a school student. I am building this project myself. The only tools I
know are Claude AI (chat) and github.com in my web browser. I do not know
coding, the terminal, Git commands, or any other software or accounts.

You are my patient mentor and developer. You do all the coding. You explain
everything in simple English, one step at a time, and never assume I know a
technical term without explaining it.

# TASK
Help me create an AI-guided web app called "Exhibit Buddy" and host it for
free on GitHub Pages, using only Claude and github.com.

The app helps students plan a science exhibition on ANY science topic. It
interviews the student, decides when it understands the idea, and then
produces a complete HTML build guide with an animated assembly demo.

Also give me beginner step-by-step instructions to create the app and host it:
1. Create a GitHub account (if needed) and a new public repository.
2. Add the files using only the browser ("Add file > Create new file" or
   "Upload files"), with exact file names and copy-paste code.
3. Turn on GitHub Pages (Settings > Pages), wait for it to publish, and
   open the live link.
4. Update the app later, and fix common mistakes (blank page, 404, old
   version showing).
Describe what I should see on screen after each step so I can confirm it worked.

# CONTEXT
## A. Technical limits (because of what I know)
- Keep the app as ONE self-contained index.html, or as few files as
  possible. No build tools, no installs, no terminal.
- GitHub Pages cannot keep secrets, so do not put an API key in the code.
  The app must work with no API key and no extra accounts.
- Make the interview "smart" without a server: build an adaptive decision
  engine in JavaScript, with a built-in library of ready-made exhibit ideas
  across school science (motion and force, gravity, energy, sound, light,
  electricity with batteries only, matter, chemical reactions, atoms,
  cells, the human body, plants and health, earth and space, natural
  resources) and branching questions.
- Claude-assisted mode, for ANY idea that is not in the library (for example
  a body organ that is not in the list):
  * The app writes a ready-made prompt that includes the student's idea,
    class or age (optional), safety cautions, and clear instructions.
  * A button opens Claude (claude.ai/new?q=...) in a new tab with the
    prompt filled in, and the app also copies the prompt as a fallback.
    The student must be told what to do if Claude opens with an empty box.
  * Later (Stage 2), the student pastes Claude's reply back into the app so
    it renders the same guide and animation.

## B. Adaptive interview
- Start with one open question about what exhibit I have in mind, plus an
  optional "class or age" field.
- Ask only follow-ups that change the outcome (topic, working model or
  static, time, budget, materials at home).
- Maximum 5 questions. Do not ask what can be inferred. If I'm unsure,
  suggest 3 easy ideas to choose from.
- If my idea is not in the library, say so plainly and offer Claude-assisted
  mode first. Never show unrelated ideas as if they were what I asked for.
- Show a short "Here is what I understood" summary and ask me to confirm
  before generating the guide.

## C. Reference model for the guide
- Visit the Canon Creative Park paper-craft site and study how a finished
  model is broken down into parts, printable templates, fold/cut/glue marks,
  numbered assembly steps, and difficulty/time estimates.
- This is for your reference only. Do NOT mention Canon anywhere in the app,
  code, or output, and do not copy its templates. Create original ones.
- If you cannot access the site, tell me and ask me to paste example pages.

## D. The generated guide must contain
1. Exhibit title, the science concept it shows, and a simple "Why it works".
2. Materials list with quantity, size and where to get each item locally
   (home, stationery shop, hardware shop, scrap). Use paper first; use
   other materials only when paper cannot do the job, and say why.
3. Each component as a numbered card with a drawing, dimensions in cm/mm,
   and cut/fold/glue steps.
4. Printable A4 templates (true scale): solid cut lines, dashed fold lines,
   numbered glue tabs.
5. A numbered assembly sequence (Step 1..N) linked to part numbers.
6. An ANIMATED assembly demo (HTML/CSS/SVG/JS only): numbered parts move
   into place step by step, with play, pause, next, previous and speed
   controls, and a caption per step matching the written instructions.
7. Safety notes, a testing checklist, troubleshooting tips, 3 viva
   questions with model answers, and a short glossary.
- Mobile-friendly and printable.

# CONSTRAINTS
- Facts, formulas, dimensions, quantities and circuits must be correct.
  Check that template sizes match the assembly steps and that part counts
  match the materials list. If something cannot be verified, say so
  instead of guessing.
- Fit the student's level. If the idea is too advanced for the class or age
  given, say so, explain the main idea with a simpler model the student can
  build, and ask whether to continue. If it is too easy, suggest ways to
  extend it. Do not claim an idea matches a particular syllabus or textbook
  chapter unless you have verified it from an official source.
- Safety for a minor comes first. Refuse outright: explosives, fireworks,
  weapons, mains electricity or high voltage, strong acids or other
  dangerous chemicals, growing germs, dangerous fuels. Add an "Ask an adult"
  label to anything with heat, flame, electricity (batteries only), glass,
  or sharp tools.
- Every instruction must be doable by someone who has never coded.
- Readable fonts, good contrast, no reliance on color alone.

# OUTPUT
1. Complete file(s) ready to paste into GitHub, with exact file names.
2. Beginner hosting guide (steps above) with what to expect at each stage.
3. One sample generated guide (a simple paper working model) showing the
   full instructions and the animated numbered assembly.
4. A short verification report: facts checked, assumptions, open risks.
```
