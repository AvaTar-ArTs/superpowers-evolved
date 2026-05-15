# VERSIONING.md — The Design Philosophy of Skill Evolution

## Why skills need to evolve

Most AI agent skills are published once and frozen. A `SKILL.md` from March works exactly the same in May —
even if the agents it targets have changed, even if new failure modes were discovered, even if the
ecosystem around it shifted.

**Superpowers Evolved rejects this.** Skills are code. Code has versions. Code improves.

## The three-version model

Every skill ships with three versions in `evolution-log/`:

| Version | Name | Purpose |
|---------|------|---------|
| `v1.strict-original.md` | Vanilla | The canonical `obra/superpowers` source. Unmodified. |
| `v2.simplified-current.md` | Adaptation | First pass at making it work in a specific agent (Qwen, Cline, etc.) |
| `v3.hybrid-recommended.md` | Battle-hardened | Merges upstream improvements with field-tested fixes |

## What gets better between versions

Based on actual session evidence from the Qwen ecosystem (see `EVOLUTION_AND_ITEM_HISTORY.md`):

### v1 → v2 (Adaptation pass)
- Paths changed from generic to ecosystem-specific
- Agent-idiomatic language (e.g., "use the Skill tool" vs "invoke the skill")
- Tool references mapped to host platform capabilities
- Redundant sections trimmed for the target agent's context window

### v2 → v3 (Hardening pass)
- **Pressure testing:** Ran under time-pressure scenarios. Identified where agents rationalize
  skipping skills ("just this once," "this is an emergency"). Added explicit counters.
- **Iron Law addition:** A non-negotiable rule at the top of the skill that gates all action.
- **Rationalization Prevention table:** Maps every common excuse to its reality. Agents
  have been observed using these exact excuses; the table short-circuits them.
- **Architecture-questioning rule:** For systematic-debugging, the rule that 3+ failed fixes
  means "question the architecture, not the symptom." This emerged from real debugging sessions
  where agents kept applying fixes without stepping back.
- **Multi-component evidence gathering:** For debugging in CI→build→signing pipelines,
  the v3 adds instrumentation at every component boundary before proposing fixes.

## Why version history matters to users

1. **Trust through transparency.** You can see exactly what changed and why.
2. **Progressive adoption.** Start with v1 (safe, proven). Move to v3 when you hit the
   failure modes v3 was designed to handle.
3. **Contribution surface.** The evolution log shows where the skill has room to grow.
   Found a new rationalization the agent uses? PR it into v4.
4. **Degradation resistance.** When a new agent platform emerges, you don't start from
   scratch — you fork from the closest version and adapt.

## The 1% rule (from `contributor-guidelines.md`)

> If a proposed change improves the skill's compliance rate by less than 1%, it stays in
> `evolution-log/` as a note but does not become the active version. Version bumps require
> evidence.

## Session evidence format

Every evolution entry should answer:
- **What was observed** (specific agent behavior, session log reference)
- **What changed** (diff against previous version)
- **Why it matters** (compliance improvement, failure mode eliminated)
- **Cross-links** (related skills, upstream sources, test cases)
