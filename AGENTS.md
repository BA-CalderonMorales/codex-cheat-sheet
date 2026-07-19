# AGENTS.md - Codex Cheat Sheet

## Quick Reference

- **Purpose**: Quick reference guide for OpenAI Codex CLI
- **Structure**: Progressive difficulty (Level 1 → Level 5)
- **Style**: Command reference tables, collapsible sections

## Core Principles

1. **Learn from proven examples** - Structure inspired by claude-code-cheat-sheet (800+ stars)
2. **Prioritize official documentation** - Verify against [OpenAI Codex repo](https://github.com/openai/codex)
3. **Guide to official sources** - Include links, "See official docs" notes

## Content Guidelines

### Include

- Frequently used commands
- Quick reference tables
- Practical real-world examples
- Configuration patterns for common problems

### Avoid

- Long explanatory prose
- Redundant information
- Speculative features without documentation
- Overly complex examples
- Excessive emojis

## Documentation Style

- Use `<details>` tags for scannable content
- Minimize emojis - use sparingly for structure, not decoration
- Clear descriptive headers over clever titles
- Generous code blocks with clear comments
- Focused, single-purpose sections

## Contributing

1. Verify accuracy against official Codex docs
2. Test commands ensure examples work
3. Keep concise - link to official docs for depth
4. Match existing organization and style
5. Cite sources

## Working Rules

- Stop and explain before major architectural changes
- One change per commit, commit before starting next
- Do not bundle unrelated work into the same commit
- **Branch flow (canonical):** All changes go through `develop`. Branch a topic branch off `develop`, make the change, merge the topic branch into `develop`, then merge `develop` into `main`. Never open a PR directly from a topic branch to `main`. This keeps `develop` as the integration branch and makes contribution easy to demonstrate and follow.

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **codex-cheat-sheet** (175 symbols, 172 relationships, 0 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> Index stale? Run `node .gitnexus/run.cjs analyze` from the project root — it auto-selects an available runner. No `.gitnexus/run.cjs` yet? `npx gitnexus analyze` (npm 11 crash → `npm i -g gitnexus`; #1939).

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows. For regression review, compare against the default branch: `detect_changes({scope: "compare", base_ref: "main"})`.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `query({search_query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `context({name: "symbolName"})`.
- For security review, `explain({target: "fileOrSymbol"})` lists taint findings (source→sink flows; needs `analyze --pdg`).

## Never Do

- NEVER edit a function, class, or method without first running `impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `rename` which understands the call graph.
- NEVER commit changes without running `detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/codex-cheat-sheet/context` | Codebase overview, check index freshness |
| `gitnexus://repo/codex-cheat-sheet/clusters` | All functional areas |
| `gitnexus://repo/codex-cheat-sheet/processes` | All execution flows |
| `gitnexus://repo/codex-cheat-sheet/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
- One change per commit, commit before starting next
- Do not bundle unrelated work into the same commit
