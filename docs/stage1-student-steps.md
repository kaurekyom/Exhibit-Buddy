# Stage 1: Student Steps

You will create the Exhibit Buddy interview app yourself. You do not need to know coding. You will copy code from Claude, save it as a file, open it in your browser, and test it.

Time needed: about 30 minutes.

---

## Part A: Create the file

**Step 1. Get the code from Claude.**
In your Exhibit Buddy project chat, paste `00-master-prompt.md` and then `01-stage-interview-engine.md`. Claude will reply with one big block of code that starts with `<!DOCTYPE html>`.
Click the **Copy** button on that code block.

**Step 2. Open a plain text editor.**
- Windows: press the Start button, type **Notepad**, press Enter.
- Mac: open **TextEdit**, then choose **Format > Make Plain Text** (menu names can be slightly different on your computer).

**Step 3. Paste the code.**
Click inside the empty page and press **Ctrl+V** (Windows) or **Cmd+V** (Mac).
You should see many lines of text. This is normal. It is your app.

**Step 4. Save it as `index.html`.**
- Windows Notepad: **File > Save As**. In **Save as type**, choose **All files**. Name the file `index.html`. Set **Encoding** to **UTF-8**. Save it in a new folder called `exhibit-buddy`.
- Mac TextEdit: **File > Save**. Name it `index.html`. If it asks about `.html` or `.txt`, choose **.html**.

**Check it worked:** the file's icon should look like a web page (a browser logo), not a notepad.
If the name shows `index.html.txt`, the extension is wrong. Rename it and remove `.txt`. On Windows, turn on **View > Show > File name extensions** in File Explorer to see this.

---

## Part B: Open it

**Step 5.** Double-click `index.html`. It opens in your browser.

**Check it worked:** you see a blue bar with **Exhibit Buddy** at the top, the word **Welcome!**, and a **Start** button.

If you see a lot of code instead of a web page, the file was saved as text. Go back to Step 4.

---

## Part C: Test it (do all five)

Press **Start**, then type the idea in the box and press **Next**. You can also type your class (for example `Class 7`) in the optional box. After each test, press **Start over** (or refresh the page with F5).

| # | Type this | What you should see |
|---|---|---|
| 1 | `balloon rocket` | Straight to **Here is what I understood** with Balloon Rocket. Only 1 question asked. |
| 2 | Press **I am not sure yet**, then choose **Sound** | Three sound ideas to choose from. Pick one and see the summary. |
| 3 | `digestive system` | The summary for **Human Digestive System Model**. Any science topic is allowed. |
| 4 | `bomb` | A **Stop** message. There is no Continue button. This is correct. |
| 5 | `origami frog` | **I do not have a ready-made plan for that.** Press **Plan it with Claude**. |

**Test 5 in detail (the Open Claude button):**
1. On the next screen, you see a blue button: **Open Claude with this prompt**.
2. Press it. Claude opens in a **new tab** with your prompt already written in the box. The app also copies the prompt for you.
3. If the box in Claude is empty, click in it and press **Ctrl+V** (Cmd+V on a Mac).
4. If the prompt is there but not sent, press **Send**. If Claude asks you to sign in, sign in first.

Also try these two:
- `human heart model`: you see "I do not have an exact plan" and a button to plan it with Claude first, because the heart is not in the library.
- `laser light show`: you see an **Extra care** box about lasers. It does not stop you, but it tells you to ask an adult.

**Write down:** did everything behave as expected? If not, copy what you typed and what you saw, and tell Claude.

---

## Part D: Try changing something (this is how you learn)

1. Open `index.html` in Notepad again (right-click the file, choose **Open with > Notepad**).
2. Press **Ctrl+F** and search for `Balloon Rocket`.
3. Change `Balloon Rocket` to `Super Balloon Rocket`. Save.
4. Go to your browser and press **F5** to refresh. Run test 1 again.

**Check it worked:** the summary now says Super Balloon Rocket.

Now you know how every idea in the app is stored. In Stage 2 you will use the same idea data to build the full guide.

---

## Part E: Check your plan before you build

The app does not know your school, your class or your syllabus. Before you build anything:
- Ask your science teacher whether the idea suits your class.
- Ask an adult to check any step with heat, batteries, glass or sharp tools.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| Blank white page | Make sure you copied ALL the code, from `<!DOCTYPE html>` to the last `</html>`. |
| Page shows code, not the app | The file is `.txt`. Rename it to `index.html`. |
| Buttons do nothing | Some of the code was missed when pasting. Copy it again from Claude. |
| Strange symbols like `â€”` | Save again with Encoding set to UTF-8. |
| Open Claude button opens an empty chat | Press Ctrl+V (Cmd+V on a Mac) to paste. The app copied the prompt for you. |
| Nothing opens when I press Open Claude | Your browser may block new tabs. Allow pop-ups for this page, or press **Copy the prompt again**, go to claude.ai yourself, and paste. |
| Copy button says to copy yourself | Normal on some browsers. Click in the prompt box and press Ctrl+C. |

When all five tests pass, tick the Stage 1 items in `verification-checklist.md`.
