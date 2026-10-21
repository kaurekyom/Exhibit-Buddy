# Stage 1: Verification Note (generic version)

## What was checked and how

| Check | Method | Result |
|---|---|---|
| App opens and shows the start screen | Ran the real `index.html` in a simulated browser (jsdom), including the real page-load event | Pass |
| Never more than 5 questions | Drove the app with 60 different inputs (single words, blanks, symbols, 250-character text, mixed topics, body organs, space, advanced topics) | Pass, no crashes |
| Summary shown before the plan is saved | Flow tests | Pass |
| Unsafe idea refused with no way to continue | Tests with 5 unsafe phrases, plus liquid mercury | Pass |
| Risky ideas show a caution but are not refused | Tests with laser and electromagnet | Pass |
| "Digestive system" works (the case that failed before) | Test | Pass: Human Digestive System Model |
| An idea outside the library offers Claude first | Tests with "origami frog" and "human heart model" | Pass |
| The Open Claude link carries the whole prompt, opens a new tab, and copies as a fallback | Tests on the link's address, target and click behaviour | Pass |
| Very long idea does not break the link | Test with a 300-character idea | Pass |
| Typed text (idea and class) cannot run as code | Typed HTML tags into both boxes | Pass: shown as plain text |
| Library data is consistent | 26 ideas: valid fields, unique IDs, every topic has an idea, every idea found by its own title, no idea or topic word wrongly refused | Pass |
| No "Canon", no API key, no Class 9 / NCERT / CBSE wording, no web address except claude.ai/new | Searched the file | Pass |

Total: 692 automated checks, 0 failed, no page script errors.

Bugs found by the tests and fixed: (1) the word "model" matched many idea titles; (2) the safety rule refused the planet Mercury along with the metal. Also changed: the simple-circuit bulb is now "rated about 3 V" so that it matches two AA cells.

## NOT verified (please read)

1. **The Open Claude link on the live Claude website.** I could not test it against claude.ai. Anthropic's support page documents a prefilled-prompt link for Claude Desktop (`claude://claude.ai/new?q=...`), which fills in the prompt for the user to review and send, with long prompts cut at about 14,000 characters. The web form (`https://claude.ai/new?q=...`) is described only by a third-party tool. It may fill the box and send automatically, or only fill it, or need you to sign in first. This is why the app always copies the prompt too and tells the student to press Ctrl+V. **Please test it on your own browser.**
2. **Science statements.** Each idea's concept line is a short, standard statement. I reviewed the 8 new ones (digestive system, breathing, solar system, pinhole camera, periscope, circuit, baking soda volcano, seed germination), but nothing was checked against a printed textbook. A science teacher should read all 26.
3. **Level and syllabus.** The app no longer claims any syllabus. Whether an idea suits a student's class is for the student and teacher to decide.
4. **Real devices.** Tested in a simulated browser only. Not yet tested on a real phone, a screen reader, or with printing.
5. **Keyword matching is simple.** It can miss unusual wording (the app then offers Claude, which is safe) or, rarely, match the wrong idea. The student always sees the matched idea and must confirm it.
6. **Safety word lists are not complete.** They cover common cases only. A new unsafe idea could pass through to Claude-assisted mode. The prompt asks Claude to refuse unsafe steps, but a teacher or adult should review any plan before building.
7. **Simple-circuit materials.** A 3 V bulb with two AA cells is a standard match, but an adult should check the actual bulb and cell ratings when building.

## Assumptions

- The student uses a modern browser on a computer or phone.
- Materials marked `home` or `cheap` are common household or stationery-shop items. Prices are not stated in the app.
- Build times (1 to 6 hours) are estimates for a first-time builder and will be refined in Stage 2.

## Sources for the Open Claude link

- Anthropic support: [Open Claude Desktop with a link](https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link)
- Third-party description of the web link: [Claude prompt link generator](https://u2l.ai/tools/claude-prompt-link-generator)

## Open risks

- The web link behaviour may change or differ between browsers.
- A teacher has not yet reviewed the library.
