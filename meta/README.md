# Tier 4 — Meta: Skills That Create Skills

**Unlocks after contributing 2+ skills used by someone else.**

| Skill | What it does | Novel? |
|-------|-------------|--------|
| `writing-skills` v3 | Design and write effective skills with testing | Evolved |
| **`skill-porter`** | **Convert skills between Claude/Gemini/Codex formats** | **✨ Original** |
| `skill-creator` | Scaffold new skills with proper structure | Adapted |
| `skill-development` | Iterate and improve existing skills | Adapted |

## skill-porter (original)

The only known tool that converts AI agent skills between platforms. Takes a Claude Code
skill and ports it to Gemini, or a Cursor skill to Codex. Handles:
- Frontmatter conversion (YAML → JSON → TOML)
- Tool reference translation
- Path normalization per platform
- Reference file restructuring

Born from managing 77 skills across 6 agent ecosystems where the same skill needed to
exist in 3-5 different formats simultaneously.

## writing-skills v3

What v3 adds:
- Testing skills with subagents (verify a skill works before publishing)
- Persuasion principles (how to write skills agents actually follow)
- Anthropic best practices integration
- Graphviz conventions for visual skill documentation
