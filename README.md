# Tree Ring Memory Skill

Root-level Claude Code skill package for
[Tree Ring Memory](https://github.com/TerminallyLazy/Tree-Ring-Memory).

Tree Ring Memory is a framework-agnostic, local-first memory lifecycle for AI
agents. It helps agents decide when to recall, capture, audit, consolidate, and
forget project memory without turning memory into an unbounded transcript dump.

Skill package **0.15.1** adds authorized verified bootstrap and scope-preserving
updates while keeping coordinator capabilities out of shell history. It
requires Tree Ring Memory CLI **0.15.0 or newer**.

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
local store, run the verified project-local setup from the actual project root
after the user has authorized installation:

Download the official version-pinned `v0.15.0/install.sh` to a temporary file,
verify its SHA-256 is
`ef0d5eb8f09cbe2e4c3abe80ee9a98a56759c89ad4ddd103d6c68314cd653ade`, inspect
it, then run `sh <verified-installer-path> --project --init --release latest
--no-animation` from the project root. Do not pipe a network response directly
to a shell.

Or use the canonical project install guide:
<https://github.com/TerminallyLazy/Tree-Ring-Memory#install>

The receipt-backed harness, multi-agent, Coordinated-policy, and schema-v3
guidance in this skill requires Tree Ring Memory CLI **0.15.0 or newer**. Before
a current process opens a pre-v0.13 store, stop all Tree Ring processes,
checkpoint and back up the database, and upgrade every CLI, plugin, and bundled
worker. Do not use v0.12 against an upgraded schema-v3 root; all mixed-version
operation is unsupported.

If the CLI is absent or older and the user's request already authorizes Tree
Ring setup, the skill uses the verified project-local bootstrap. Otherwise it
explains the operation and asks before downloading or changing software. Use
`tree-ring update --check` for a read-only check and, with update authorization,
`tree-ring update` to preserve the active scope. It does not edit shell
configuration, change global scope, or claim that recall or another action ran
without the required authorization and observed command output. On a host
without a local shell, it remains guidance-only.

## What It Teaches

- Recall before project restarts, architecture changes, repeated workflows, and
  user corrections.
- Capture only durable, useful, privacy-safe decisions, warnings, lessons, and
  future seeds.
- Use rings deliberately: cambium, outer, inner, heartwood, scar, and seed.
- Prefer evidence records for evaluated outcomes.
- Treat source documents as authoritative when memory and source files disagree.
- Read the applicable DOX-style `AGENTS.md` chain before editing, preview DOX
  sync output, and never let recalled summaries override or rewrite contracts.
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
- Distinguish project-local harness configuration from activation, which
  requires a fresh matching receipt from scoped recall and safe context
  injection in a new session.
- Report exact non-active states such as `configured-awaiting-proof`,
  `needs-trust`, `needs-plugin`, `needs-project-mount`, and `needs-user-review`
  without modifying trust or manufacturing receipts.
- Distinguish installed-CLI harness and recall-quality evidence from the full
  repository-only `scripts/certify-tree-ring.sh` release suite.

## Source Project

- Framework: <https://github.com/TerminallyLazy/Tree-Ring-Memory>
- Skill release: <https://github.com/TerminallyLazy/tree-ring-memory-skill/releases/tag/v0.15.1>
- v0.15 release: <https://github.com/TerminallyLazy/Tree-Ring-Memory/releases/tag/v0.15.1>
- Claude plugin wrapper:
  <https://github.com/TerminallyLazy/tree-ring-memory-claude-plugin>
- Skill file: [`SKILL.md`](SKILL.md)

## License

MIT. See [`LICENSE`](LICENSE).

See [`PRIVACY.md`](PRIVACY.md), [`TERMS.md`](TERMS.md), and
[`SECURITY.md`](SECURITY.md) for data handling, use terms, and disclosures.
