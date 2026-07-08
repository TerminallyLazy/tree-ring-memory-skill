# Tree Ring Memory Skill

Root-level Claude Code skill package for
[Tree Ring Memory](https://github.com/TerminallyLazy/Tree-Ring-Memory).

Tree Ring Memory is a framework-agnostic, local-first memory lifecycle for AI
agents. It helps agents decide when to recall, capture, audit, consolidate, and
forget project memory without turning memory into an unbounded transcript dump.

## Install

For Claude Code's personal skills directory:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/TerminallyLazy/tree-ring-memory-skill \
  ~/.claude/skills/tree-ring-memory
```

For a project-local skill:

```bash
mkdir -p .claude/skills
git clone https://github.com/TerminallyLazy/tree-ring-memory-skill \
  .claude/skills/tree-ring-memory
```

The skill is useful on its own as memory lifecycle guidance. To use the full
local store, install the Tree Ring Memory CLI:

```bash
brew tap TerminallyLazy/tree-ring
brew install tree-ring
```

Or use the canonical project install guide:
<https://github.com/TerminallyLazy/Tree-Ring-Memory#install>

## What It Teaches

- Recall before project restarts, architecture changes, repeated workflows, and
  user corrections.
- Capture only durable, useful, privacy-safe decisions, warnings, lessons, and
  future seeds.
- Use rings deliberately: cambium, outer, inner, heartwood, scar, and seed.
- Prefer evidence records for evaluated outcomes.
- Treat source documents as authoritative when memory and source files disagree.
- Redact, delete, or supersede stale or unsafe memory.

## Source Project

- Framework: <https://github.com/TerminallyLazy/Tree-Ring-Memory>
- Claude plugin wrapper:
  <https://github.com/TerminallyLazy/tree-ring-memory-claude-plugin>
- Skill file: [`SKILL.md`](SKILL.md)

## License

MIT. See [`LICENSE`](LICENSE).
