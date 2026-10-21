# Stage 1: The Code, Explained in Simple English

`index.html` is one file with three parts inside the `<script>` section. Think of it like a person: Part 1 is the **memory**, Part 2 is the **thinking**, Part 3 is the **face and voice**.

---

## Part 1: DATA (the memory)

**TOPICS** is a list of 14 science topic areas, such as Sound, Light and mirrors, or The human body. Each topic has a list of `words`. If you type a word from that list, the app guesses your topic.

**IDEAS** is the library of 26 exhibit ideas. Every idea is a small block with these facts:

| Field | Meaning |
|---|---|
| `title` | The name of the exhibit |
| `topic` | Which topic area it belongs to |
| `concept` | The science idea it shows |
| `type` | `working` (something moves or happens) or `static` (shows and explains) |
| `difficulty`, `hours` | How hard it is and how long it takes |
| `cost` | `home` (things at home) or `cheap` (a few cheap shop items) |
| `materials` | Main things you need |
| `safety`, `safetyNote` | `low` or `adult`, plus a safety tip |
| `keywords` | Words that make the app pick this idea |

**The app does not claim any school syllabus.** It is generic. Your teacher decides whether an idea suits your class.

**The safety rules:**
- `UNSAFE_RULES`: ideas the app refuses (explosives, mains electricity, strong chemicals, weapons, growing germs). There is no way to continue.
- `NOTE_RULES`: cautions for risky or advanced ideas (lasers, nuclear, robots, batteries). The app shows an "Extra care", "Model only", "Advanced topic" or "Batteries only" box, but lets you continue.
- `ADULT_WORDS`: words like candle or boiling. The app adds an **Ask an adult** label.

**To add a new idea:** copy one block in `IDEAS`, change the words, and add a comma between blocks. Every fact must be correct, so check it with a reliable source.

---

## Part 2: ENGINE (the thinking)

The engine only makes decisions. It never draws anything, so it is easy to test.

**`normalize`** turns what you type into simple lowercase words. "Newton's Cradle!" becomes "newton s cradle".

**`hasWord`** checks if a word is in your text. "balloons" counts as "balloon", but "working" does not count as "work". This stops silly matches. (This is also why the planet Mercury is allowed but liquid mercury is refused.)

**`screen`** checks your idea against the safety lists *first*, before anything else.

**`scoreIdeas`** gives every idea points:
- 2 points for each keyword you typed.
- 1 point for a special word from the title. Common words such as "model" and "paper" are ignored, because they appear in many titles.

**`first`** decides what to do after your first answer:
1. If you are unsure, go to the topic question.
2. If an idea scores 2 or more, use it (`idea`).
3. Otherwise, if your words match a topic, offer the related ideas (`topic`). The app says clearly that it has no exact plan and puts the Claude button first.
4. Otherwise, say "I do not have a ready-made plan" and offer Claude (`none`).

**`nextQuestion`** asks a follow-up question **only if the answer can change the result**. It tries each question (type, time, materials) and checks how many ideas the answer would remove. If no answer would remove any idea, it does not ask. It also stops when 3 or fewer ideas are left, or when 5 questions have been asked.

**`shortlist`** picks the best 3 ideas: the easiest first, then the quickest.

---

## Part 3: SCREENS (the face and voice)

**`el()`** builds a piece of the page (a heading, a button). We use it instead of pasting text into the page as HTML. This means anything a student types is shown as plain text and can never run as code.

**`show()`** clears the page and puts new content in. It also moves the keyboard focus to the heading so screen readers read it.

**`notice()`** makes the coloured boxes. Every box begins with a **word** (Warning, Stop, Ask an adult, Safety tip), so the meaning never depends on colour alone.

**The screens** are functions: `showStart`, `showQ1`, `showQuestion`, `showPick`, `showSummary`, `showConfirmed`, `showRefuse`, `showNoMatch`, `showAssisted`. Each button calls the next one.

**`state`** is a notebook the app writes in: how many questions were asked, which ideas are still possible, your class (optional), and which idea you picked.

### The Open Claude button

**`buildAssistedPrompt`** writes the prompt for ideas outside the library. It includes your idea, your class or age (if you gave it), any safety cautions, and instructions: check the level, ask at most 3 questions, avoid unsafe steps, and be honest when unsure.

**`claudeUrl`** turns the prompt into a web address: `https://claude.ai/new?q=` followed by the prompt with special characters encoded. If the prompt is too long for a web address, it opens a blank chat instead.

**The blue button is a link** (an `<a>` tag), not a script. Links open in a new tab without being blocked by the browser. When you click, the app also **copies the prompt**, so if Claude opens with an empty box you can paste it with Ctrl+V.

**`copyText`** copies using the browser's clipboard. If that is not allowed, it selects the text in the box so you can press Ctrl+C.

**The last line** (`DOMContentLoaded`) starts the app when the page finishes loading.

---

## Why no API key?

GitHub Pages cannot keep a secret. Anything in `index.html` can be read by anyone. So the app does its own thinking with the rules above, and opens Claude, where **you** are signed in, when it needs more help.
