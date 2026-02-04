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
