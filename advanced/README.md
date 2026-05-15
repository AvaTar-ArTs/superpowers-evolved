# Tier 3 — Advanced: Multi-Agent & Ecosystem Intelligence

**Unlocks after completing one full Tier 2 workflow cycle.**

| Skill | What it does | Novel? |
|-------|-------------|--------|
| `dispatching-parallel-agents` | Orchestrate multiple AI agents on subtasks | Adapted |
| `subagent-driven-development` v3 | Spec → implement → review via agents | Evolved with custom prompts |
| `requesting-code-review` | Structured review requests with code-reviewer agent | Adapted |
| `receiving-code-review` | Process and apply review feedback | Adapted |
| **`capability-atlas`** | **Cross-platform capability matrix** | **✨ Original** |
| **`ecosystem-navigation`** | **Navigate multi-agent tool ecosystems** | **✨ Original** |
| `managing-ecosystem-cleanup` | Dedup, audit, and clean AI tool directories | Adapted |
| `workspace-ecosystem-audit` | Full filesystem audit with CSV output | Adapted |

## Original skills unique to this collection

### capability-atlas
Maps capabilities across agent platforms (Claude Code, Cursor, Gemini, Codex, Cline).
Includes:
- Capability matrix template
- Host translation rules (Claude→Gemini, Gemini→Codex, etc.)
- Parity tests to verify translations work

### ecosystem-navigation
Helps agents and users navigate sprawling multi-tool home directories.
Answers: "Where is the canonical copy of this skill? Which agent owns this config?
What's safe to edit vs read-only?"

Both born from managing a real 6-agent ecosystem across `~/.cline`, `~/.qwen`, `~/.gemini`,
`~/.cursor`, `~/.codex`, and `~/my-supremepowers`.
