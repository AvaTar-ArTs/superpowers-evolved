# Superpowers Evolved

**Skills that level up.** Tiered AI agent skills with documented evolution history.

Built from the [obra/superpowers](https://github.com/obra/superpowers) foundation and hardened
through multi-ecosystem battle testing across Cline, Qwen, Gemini, Cursor, and Codex.

## Install

```bash
npx skills add steven/superpowers-evolved
```

## Quick start — the Iron Foundation

Install these two first. Everything else depends on them.

| Skill | What it does | Installs |
|-------|-------------|----------|
| `systematic-debugging` | Four-phase root cause before fixes | — |
| `verification-before-completion` | Evidence before claims, always | — |

```bash
npx skills add steven/superpowers-evolved/core/systematic-debugging
npx skills add steven/superpowers-evolved/core/verification-before-completion
```

## The full tree

```
core/           Tier 1 — The Iron Foundation (install first)
workflow/       Tier 2 — Idea to shipped feature (unlocks after core)
advanced/       Tier 3 — Multi-agent & ecosystem intelligence
meta/           Tier 4 — Skills that create/modify skills
evolution-log/  The archive — see how each skill got better
```

Read [SKILL_TREE.md](SKILL_TREE.md) for the visual progression map.

## What's different from vanilla superpowers

| Vanilla (obra/superpowers) | Evolved (steven/superpowers-evolved) |
|---------------------------|--------------------------------------|
| Flat list of 14 skills | Tiered progression system |
| Single version per skill | v1 → v2 → v3 evolution history |
| Generic agent language | Cross-platform (Claude/Cursor/Codex/Gemini/Cline tool refs) |
| No failure-mode hardening | Iron Laws + Rationalization Prevention tables |
| No multi-component debugging | Instrumentation at every boundary before fixes |
| No architecture-questioning rule | 3+ failed fixes → question architecture |

## License

Based on obra/superpowers (MIT). Evolution additions MIT.
# superpowers-evolved
