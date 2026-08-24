#!/usr/bin/env python3
"""Validate the portable Tree Ring Memory skill package."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def require_markers(relative: str, markers: list[str]) -> None:
    text = " ".join(read(relative).split())
    missing = [marker for marker in markers if " ".join(marker.split()) not in text]
    if missing:
        raise SystemExit(f"{relative} is missing: {', '.join(missing)}")


def main() -> None:
    skill = read("SKILL.md")
    if not skill.startswith("---\n"):
        raise SystemExit("SKILL.md must start with YAML frontmatter")

    _, frontmatter, body = skill.split("---", 2)
    for field in (
        "name:",
        "description:",
        "version:",
        "license:",
        "tags:",
        "triggers:",
    ):
        if field not in frontmatter:
            raise SystemExit(f"missing frontmatter field: {field}")
    if not re.search(r"^version:\s*0\.14\.0\s*$", frontmatter, re.MULTILINE):
        raise SystemExit("SKILL.md must declare version 0.14.0")
    if "Claude Code" in frontmatter or "Codex" in frontmatter:
        raise SystemExit("portable skill frontmatter must remain provider-neutral")

    required_guidance = [
        "Runtime Preflight",
        "DOX Contract Flow",
        "tree-ring dox sync --source-root <path> --dry-run",
        "Certification Boundary",
        "tree-ring integrations certify --source-root .",
        "tree-ring recall-quality --source-root .",
        "full framework release suite",
        "0.14.0 or newer",
        "tree-ring integrations status",
        "configured-awaiting-proof",
        "active-isolated",
        "needs-plugin",
        "needs-user-review",
        "--operation-id",
        "TREE_RING_COORDINATOR_TOKEN",
        "same-host local-filesystem processes",
        "schema v3 fences",
        "operation is unsupported",
    ]
    normalized_body = " ".join(body.split())
    missing = [
        marker
        for marker in required_guidance
        if " ".join(marker.split()) not in normalized_body
    ]
    if missing:
        raise SystemExit("missing v0.14 guidance: " + ", ".join(missing))

    require_markers(
        "README.md",
        [
            "0.14.0 or newer",
            "configured-awaiting-proof",
            "needs-project-mount",
            "observed command output",
        ],
    )
    require_markers("PRIVACY.md", ["local SQLite database", "does not receive"])
    require_markers("TERMS.md", ["MIT License", "provided without warranty"])

    blocked = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "BEGIN PRIVATE KEY"]
    text_suffixes = {".json", ".md", ".py", ".sh", ".toml", ".txt", ".yaml", ".yml"}
    public_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.resolve() != Path(__file__).resolve()
        and path.suffix.lower() in text_suffixes
    )
    for marker in blocked:
        if marker in public_text:
            raise SystemExit(f"potential secret marker found: {marker}")
    if "[TODO:" in public_text:
        raise SystemExit("placeholder text remains in the package")

    print("Tree Ring Memory portable skill validation passed")


if __name__ == "__main__":
    main()
