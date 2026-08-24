# Tree Ring Memory Skill Privacy Notice

Effective August 23, 2026

This repository contains agent instructions only. It does not operate a hosted
service, collect analytics, send telemetry, or include a remote MCP server.

When an agent runs the separately installed Tree Ring Memory CLI, the CLI stores
the memory content the user chooses in a local SQLite database under the
configured Tree Ring root. The project does not receive that database or its
contents. Data leaves the local environment only when the user or another tool
explicitly exports, syncs, publishes, or otherwise transmits it.

The skill instructs agents to avoid transcripts, credentials, secrets, private
keys, raw chain-of-thought, and unnecessary sensitive personal data. These
safeguards do not replace the privacy and data-use terms of the AI host,
operating system, source-control provider, or another tool the user invokes.
