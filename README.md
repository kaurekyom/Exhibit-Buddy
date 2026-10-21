# Exhibit Buddy

A web app that helps a school student plan a science exhibit on any topic. It asks up to 5 short questions, then gives a build guide with true-size printable templates, numbered steps, safety notes, viva questions and a 3D "watch it go together" model. It also has labelled figures (animal cell, carbon atom, solar system) where you tap a part to learn about it. Topics that are not built in are planned with Claude.

*Created by Ekyom Kaur, Class 9, PMS Alwal, Secunderabad.*

**Live app:** https://kaurekyom.github.io/Exhibit-Buddy/

**Documentation (web pages):** https://kaurekyom.github.io/Exhibit-Buddy/docs/ : how it was created, how it works, how to use it, and the verification report.

The app is one file, `index.html`. It needs no server, no account and no API key.

## How to use it (for students)
1. Open the live link. Press **Start** and answer the questions.
2. If there is a ready-made guide, press **Build my guide**.
3. If there is not: press **Plan it with Claude**. Claude opens in a new tab with the prompt filled in (if the box is empty, press Ctrl+V; the prompt is already copied). Wait for Claude's code block, press its Copy button, paste it into the app, and press **Build my guide**.
4. Print the templates (A4, scale 100%, turn off "Fit to page"). Measure the 50 mm scale bar.
5. Do every step yourself. Steps marked **Ask an adult** need an adult.
6. For biology, atoms and space: press **Explore a labelled figure**.

The app checks sizes, parts, steps and safety words. **It cannot check the science.** Ask a teacher to read your guide (see `docs/teacher-review-checklist.md`).

## Publish your own copy on GitHub Pages (using only a browser)
1. Sign in at github.com. Click **+** (top right) > **New repository**. Name it, choose **Public**, tick **Add a README file**, click **Create repository**. *You see your new repository page.*
2. Click **Add file > Upload files**, drag `index.html` in, and click **Commit changes**. *The file appears in the list.* The name must be exactly `index.html`, all lower case.
3. Click **Settings > Pages**. Under **Build and deployment** choose **Deploy from a branch**. Branch: **main**, folder: **/ (root)**. Click **Save**. *A blue box says your site is being published.*
4. Wait 1 to 2 minutes and refresh. The box shows **Your site is live at** `https://USERNAME.github.io/REPOSITORY/`. Open it. *You see "Welcome!".*
5. To update: open `index.html` in the repository, click the pencil, change it, **Commit changes**, wait a minute and refresh (Ctrl+F5).

**Problems.** Blank page or 404: check the file is called `index.html` and is in the top folder, and that Pages is set to main and /(root). Old version showing: wait 2 minutes and press Ctrl+F5. Pages option missing: the repository must be public.

## What is in this repository
- `index.html` the app
- `prompts/` the prompts used to build it, in stages
- `docs/` explanations, test notes, `verification-report.md`, `teacher-review-checklist.md`

## Honest limits
Not tested on real phones, printers or screen readers. Nobody has built the models yet. The link that opens Claude with the prompt has not been tested on live claude.ai. See `docs/verification-report.md`.
