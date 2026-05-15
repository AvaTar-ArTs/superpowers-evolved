# Superpowers Evolved — Skill Tree

*A progression system for AI agent skills. Not a flat list. Not a one-shot install. Skills that level up.*

```
                    ┌──────────────────────────┐
                    │     META (Tier 4)        │
                    │  Skills that create or   │
                    │  modify other skills     │
                    │                          │
                    │  writing-skills v3       │
                    │  skill-porter            │
                    │  skill-creator           │
                    │  skill-development       │
                    └────────────┬─────────────┘
                                 │ unlocks after
                                 │ mastering 2+ Tier 3
              ┌──────────────────┼──────────────────┐
              │                                     │
    ┌─────────┴──────────┐              ┌───────────┴─────────┐
    │  ADVANCED (Tier 3) │              │  ADVANCED (Tier 3)  │
    │  Multi-agent &     │              │  Ecosystem          │
    │  parallel execution│              │  intelligence       │
    │                    │              │                     │
    │  dispatching-      │              │  capability-atlas   │
    │    parallel-agents │              │  ecosystem-         │
    │  subagent-driven-  │              │    navigation       │
    │    development v3  │              │  managing-ecosystem │
    │  requesting-code-  │              │    -cleanup         │
    │    review          │              │  workspace-ecosystem│
    │  receiving-code-   │              │    -audit           │
    │    review          │              │                     │
    └─────────┬──────────┘              └───────────┬─────────┘
              │                                     │
              └──────────────┬──────────────────────┘
                             │ unlocks after
                             │ completing Tier 1
              ┌──────────────┴──────────────────────┐
              │        WORKFLOW (Tier 2)            │
              │    From idea to shipped feature     │
              │                                     │
              │    brainstorming v3                 │
              │    writing-plans                    │
              │    executing-plans                  │
              │    finishing-a-development-branch   │
              │    using-git-worktrees              │
              │    test-driven-development          │
              └──────────────┬──────────────────────┘
                             │ unlocks after
                             │ internalizing core
              ┌──────────────┴──────────────────────┐
              │           CORE (Tier 1)             │
              │    The Iron Foundation              │
              │                                     │
              │    systematic-debugging v3          │
              │    verification-before-completion v3│
              └─────────────────────────────────────┘
```

## The Tiers

| Tier | Name | Install first | Gates |
|------|------|---------------|-------|
| **1** | Core | Always | No gate — install immediately |
| **2** | Workflow | After Tier 1 internalized | Must complete one real debugging cycle with Tier 1 skills |
| **3** | Advanced | After one full workflow cycle | Must ship one feature using Tier 2 chain |
| **4** | Meta | After contributing 2+ skills | Must have a skill used by someone else |

## What makes this "evolved"

Every skill includes `evolution-log/` entries showing **how** it got better across versions. The vanilla `obra/superpowers` skills are v1. These are v3 — hardened through:

- Multi-ecosystem battle testing (Cline, Qwen, Gemini, Cursor, Codex)
- Pressure testing under time constraints
- Cross-platform tool mapping
- Iron Law enforcement with rationalization prevention tables
