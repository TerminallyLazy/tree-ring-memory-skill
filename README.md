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

The multi-agent, Coordinated-policy, and schema-v3 guidance in this skill
requires Tree Ring Memory CLI **0.13.0 or newer**. Before a v0.13 process opens
an existing store, stop all Tree Ring processes, checkpoint and back up the
database, and upgrade every CLI, plugin, and bundled worker. Do not use v0.12
against an upgraded schema-v3 root; all mixed-version operation is unsupported.

## What It Teaches

- Recall before project restarts, architecture changes, repeated workflows, and
  user corrections.
- Capture only durable, useful, privacy-safe decisions, warnings, lessons, and
  future seeds.
- Use rings deliberately: cambium, outer, inner, heartwood, scar, and seed.
- Prefer evidence records for evaluated outcomes.
- Treat source documents as authoritative when memory and source files disagree.
- Redact, delete, or supersede stale or unsafe memory.
- Give same-host fan-out workers unique agent profiles and logical operation
  IDs while sharing workflow and attempt-level session IDs.
- Reuse the original session and operation IDs only for an exact retry; use new
  IDs for a genuinely new attempt, and fail closed on conflicting operation
  reuse.
- Fan in across worker profiles by recalling the shared workflow/session
  without an agent-profile filter, then retain source references in the
  coordinator summary.
- Keep `TREE_RING_COORDINATOR_TOKEN` out of worker environments, memory, logs,
  source refs, transcripts, and committed files.
- Require coordinator authority for shared/non-agent writes, heartwood,
  imports, persisted adapter/consolidation output, lifecycle mutations, and
  maintenance apply/repair operations in Coordinated mode.
- Keep the shared-root claim bounded to concurrent processes on one host and a
  local filesystem; use per-host stores and explicit evidence-preserving fan-in
  across hosts.

## Source Project

- Framework: <https://github.com/TerminallyLazy/Tree-Ring-Memory>
- Claude plugin wrapper:
  <https://github.com/TerminallyLazy/tree-ring-memory-claude-plugin>
- Skill file: [`SKILL.md`](SKILL.md)

## License

MIT. See [`LICENSE`](LICENSE).
