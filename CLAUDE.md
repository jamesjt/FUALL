# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

"Foundational Understanding" is a static single-page application that aggregates educational content (articles, books, breakdowns) from Google Sheets and Google Docs, displaying them with an interactive reference tooltip system and a network graph visualization ("Wisdom Map").

## Development

This is a zero-build static web project — no package.json, no bundler, no framework. To develop:

- Open `index.html` directly in a browser, or serve with any static server (e.g., `npx serve`, VS Code Live Server, `python -m http.server`)
- No install, build, lint, or test commands exist

There are three files: `index.html`, `script.js`, `styles.css`.

## Architecture

### Data Flow

1. On page load, two Google Sheets CSV feeds are fetched via PapaParse
2. The **unified content sheet** (gid=464648636) provides all content entries with columns: Title, Link, Type, Tag, Parent, Chapter, and `D:` prefixed data columns
3. The **references sheet** (gid=1749170252) provides term→definition pairs for the tooltip system
4. Content is categorized by Type into Articles, Books, and Breakdowns
5. All content is preloaded into DOM elements stored in the global `contentElements` object (keyed by title)
6. Google Docs content is fetched as HTML, parsed, and stripped of Google UI chrome
7. Google Sheets content (spreadsheet links) is parsed into tabbed row layouts using `D:` columns

### Key Global State

- `contentElements` — cache of preloaded DOM elements keyed by title
- `tooltips` — reference term→definition map from the refs sheet
- `network` — vis.js Network instance (created lazily on first Map button click)
- `unifiedData`, `articlesData`, `booksData`, `breakdownsData` — parsed row arrays

### Content Rendering

- **Google Docs links** (`link.includes('document')`): fetched as HTML, Google UI elements stripped, injected into `.doc-content`
- **Google Sheets links** (`link.includes('spreadsheets')`): converted to CSV, parsed. Columns prefixed with `D:` become content columns. Multiple non-empty `D:` columns in a row render as a tabbed interface; single columns render as plain paragraphs. The `Chapter` column creates heading dividers.

### Reference/Tooltip System

`highlightReferences()` walks text nodes via TreeWalker, matches terms from the tooltips map using word-boundary regex (longest-first), and wraps matches in `<span class="ref">`. `initializeTippy()` then attaches Tippy.js tooltips. A MutationObserver on `.content-body` re-applies highlighting when DOM changes.

### Deep Linking

URL parameters: `?type=article&content=Title&row=1&tab=2` — navigates directly to a specific content item, row (1-based), and tab (1-based).

### Wisdom Map

Lazy-initialized vis.js hierarchical network graph of articles. Nodes are grouped by Tag (Wisdom, Reality, Reason, Right, Musings). Edges connect nodes to their Parent. Musings are auto-clustered. Layout direction toggleable (UD/DU/LR). Node hover shows content preview; click opens popover.

## CDN Dependencies

- **PapaParse 5.3.2** — CSV parsing
- **Popper.js @2** + **Tippy.js @6** — tooltip positioning and rendering
- **vis-network** (standalone UMD) — network graph visualization

## Styling Conventions

- Dark theme: background `#121212`, text `#c1c1c1`/`#e0e0e0`, surface `#1e1e1e`
- Gold accent via CSS custom properties: `--gold-accent: #d29a38`, `--gold-hover: #b8862f`
- Primary font: Source Serif 4 (serif) with optical sizing
- Fixed navbar (top, z-index 1000) and fixed sidebar (left, 250px wide, z-index 999)

## Workflow Orchestration

### 1. Plan First Default

- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy

- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop

- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done

- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)

- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing

- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plans**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

---

# Modern Editions Project

## Overview
This project transforms older texts into multiple versions for a modern audience. Each work is organized in a CSV with passages indexed by chapter/section and thought number. Each passage gets four rewritten versions alongside the original.

## CSV Structure
| Column | Purpose |
|---|---|
| Index | Passage ID (e.g., 1.1, 2.F1). "F" entries are footnotes. |
| Chapter | Chapter or section number |
| Thought | Thought number within chapter |
| D: Original | The original text |
| D: Refashioned | Editorial reconstruction for a 2026 audience |
| D: Elegant | Polished literary compression |
| D: Summary | 2–3 sentence plain language summary |
| D: Distilled | Single sentence core insight |
| Notes | Editorial notes, historical context, references |

## Version Definitions

### Refashioned
Rewrite the author's argument as a modern author would make it today. This is editorial reconstruction, not translation.

- **Modernize examples and references** for a 2026 audience. Replace dated cultural specifics with contemporary equivalents that serve the same argumentative function.
- **Cut redundancy.** If the previous passage already established a point, do not restate it. Read the preceding passage before writing.
- **Restructure freely** for clarity and directional flow between passages. The original sentence structure does not need to be preserved.
- **Add brief interpretive bridges** where they help a modern reader follow the argument across passages.
- **Preserve the author's core argument faithfully.** Editorial reconstruction means rebuilding for clarity, not changing the ideas. Do not soften, strengthen, or editorialize the author's positions.
- **Voice:** Direct, confident, non-academic. Front-load the point. Avoid sentences that delay the payoff with subordinate clauses.
- **Length:** Target 40–60% of the original.
- **Do not** include editorial notes in this column. Those go in Notes.

### Elegant
Capture the spirit, weight, and persuasive force of the original argument in polished, compressed prose.

- Prioritize **rhythm, punch, and quotability**.
- A reader should find this compelling without having read the original.
- This is **not a summary** — it should *move* the reader, not just inform them.
- Take creative liberty with expression while remaining faithful to the core argument.
- **Length:** Shorter than Refashioned. No fixed ratio — use what the passage needs.

### Summary
The core argument in plain language.

- **2–3 sentences maximum.**
- Essential ideas only — no rhetoric, examples, or historical references.
- A reader should understand what the author is arguing and why, nothing more.

### Distilled
A single sentence capturing the central insight.

- Should stand alone as a **shareable, self-contained idea**.
- No dependent context needed — someone encountering this sentence alone should grasp the point.
- Think: what you'd post, quote in a slide, or use as a section epigraph.

## Processing Rules

### Passage ordering matters
Passages are sequential arguments. Each Refashioned version should read as a natural continuation of the previous one. Before writing any passage, read the preceding 1–2 passages to avoid redundancy and ensure flow.

### Adapt to the source author's mode
Different works make different demands. An argumentative text (Mill, Locke, Machiavelli) should be reconstructed as argument. A narrative or reflective text (Marcus Aurelius, Montaigne) should be reconstructed with voice and texture, not just logical structure. Match the mode of the original — don't flatten everything into essay form.

### Footnotes
- Rows with "F" in the Index (e.g., 2.F1) are footnotes.
- **Citation-only footnotes** — short references to names, dates, sources. These generally do not need rewriting. Skip or copy as-is.
- **Substantive footnotes** — contain real arguments or context. Rewrite these using the same four-version approach.

### HTML in cells
Some passages may contain HTML tags (`<b>`, `<a href>`). Strip these from rewritten versions unless the user adds them back intentionally.

### Batch processing
- Process **one chapter or section at a time**.
- Within a chapter, process passages in order (sequential context matters).
- After each batch, save and verify before continuing.
- Preserve all existing content — do not overwrite filled cells.

### Skipping rows
- Skip rows where D: Original is empty (e.g., chapter headers).
- Skip rows where all four rewritten columns are already filled, unless explicitly asked to redo them.

## Style Rules

### Openings
Front-load the point. Do not open passages with abstract constructions that delay the payoff (e.g., "It is generally acknowledged that..." → state the claim directly).

### Modern equivalents
When replacing dated examples, choose equivalents that are specific enough to land but general enough to age well. Prefer references to enduring categories (political identity, social media, public health) over references to specific 2024–2026 events that will themselves become dated.

### Tone
Write for a thoughtful general reader, not an academic audience. Assume intelligence but not specialized knowledge. Avoid jargon from any discipline unless the original author's argument depends on a technical term, in which case define it briefly on first use.

## Notes Agent

### Purpose
A sub-agent that reads each passage and identifies everything the author alludes to, assumes, or builds upon without explicitly naming or justifying. The goal is to surface the implicit knowledge the original audience was expected to have so that it can be referenced, linked, or incorporated into the modernized versions.

### What to look for

**Historical events and documents** — When the author references "the struggle in Greece, Rome, and England" or "recognition of certain immunities," identify the specific events, treaties, charters, revolutions, or legal milestones being invoked (e.g., Magna Carta, English Bill of Rights, French Revolution).

**People and their ideas** — When the author alludes to a philosophical position, rhetorical tradition, or intellectual lineage without naming its originator, identify them (e.g., Mill says the question "has divided mankind from the remotest ages" → Plato's Republic, philosopher kings, the noble lie).

**Unstated premises and logical dependencies** — When the author's argument depends on a claim they treat as self-evident but which actually requires justification, flag it. These are assumptions the original audience may have shared but a modern reader may not (e.g., "the tyranny of the majority" assumes the reader already accepts that democratic rule can be oppressive).

**Legal cases, trials, and precedents** — When the author references judicial events, sentencing, or legal principles without full citation, identify the specific case, date, jurisdiction, and outcome where possible.

**Literary and philosophical references** — Quotations, paraphrases, or allusions to other works, even when unmarked (e.g., Mill quotes Dante in Italian without attribution in 2.12 — identify the source as *Inferno*, Canto IV).

**Concepts borrowed from other disciplines** — When the author uses a term or framework from another field (economics, theology, natural philosophy) as if it needs no explanation, note the origin and brief definition.

### Notes format
Keep notes concise and reference-oriented. Use this pattern:

```
[Specific reference] (date if applicable) — brief explanation of relevance to the passage
```

Examples from existing notes:
- `Magna Carta (1215), Model Parliament (1295), Hungary's Golden Bull (1222)`
- `Plato suggesting philosopher kings and noble lies to maintain a Just City`
- `English Bill of Rights (1689)`

Multiple references in a single note should be comma-separated or line-broken. Prioritize specificity — a name, date, and document title is more useful than a general description.

### Processing approach
- Run through passages **in order**, since later allusions may depend on context established earlier.
- Check the original text, not the rewritten versions — allusions live in Mill's (or the author's) language and may be lost in modernization.
- If an allusion is ambiguous or could refer to multiple sources, note the most likely candidate and flag the uncertainty.
- Do not duplicate notes that already exist — read the existing Notes column first.

## Current Works

### On Liberty — John Stuart Mill (1859)
- **Source:** [econlib.org/library/Mill/mlLbty.html](https://www.econlib.org/library/Mill/mlLbty.html)
- **CSV:** On_Liberty_-_On_Liberty__Data.csv
- **Chapters:** 5 (143 passages total)
- **Status:** Chapter 1 Refashioned complete. Chapter 2 partially complete (2.1–2.18 all four versions filled).
- **Quality benchmarks:** Use filled passages as style references. Specifically:
  - Refashioned 2.14 (Marcus Aurelius) — interpretive compression with a modern editorial voice.
  - Elegant 2.12 (Socrates) — literary compression with emotional weight.
  - Distilled 2.6 ("Confidence in a belief is earned by surviving challenge, not by forbidding it.") — standalone, quotable single sentence.
- **Notes:** Mill's arguments are densely layered and heavily recursive. Cutting redundancy between adjacent passages is especially important. Many of his examples (religious sects, 1850s court cases) need full replacement, not just modernization.
