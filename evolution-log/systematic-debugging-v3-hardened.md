# systematic-debugging v3 — Battle-Hardened

## What changed from v1

### 1. The Iron Law (v2 addition, strengthened in v3)

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

Placed at the top of the skill as a non-negotiable gate. If Phase 1 isn't complete, no fixes
can be proposed. This prevents the most common failure mode: jumping to solutions.

### 2. Multi-Component Evidence Gathering (v3 addition)

From real debugging sessions on CI→build→signing pipelines. The v1 approach of "gather
evidence" was too vague for multi-layer systems. v3 adds explicit instrumentation:

```
For EACH component boundary:
  - Log what data enters component
  - Log what data exits component
  - Verify environment/config propagation
  - Check state at each layer

Run once to gather evidence showing WHERE it breaks
THEN analyze evidence to identify failing component
THEN investigate that specific component
```

Includes a concrete bash example showing secrets→workflow→build script→signing script→codesign
instrumentation across 4 layers.

### 3. Architecture-Questioning Rule (v3 addition)

From sessions where 3+ fixes were attempted on the wrong architecture:

```
If 3+ Fixes Failed: Question Architecture

Pattern indicating architectural problem:
  - Each fix reveals new shared state/coupling/problem in different place
  - Fixes require "massive refactoring" to implement
  - Each fix creates new symptoms elsewhere

STOP and question fundamentals:
  - Is this pattern fundamentally sound?
  - Are we "sticking with it through sheer inertia"?
  - Should we refactor architecture vs. continue fixing symptoms?
```

### 4. Expanded Red Flag Table (v2→v3)

v1 had 7 red flags. v3 has 12, including:
- "One more fix attempt" (when already tried 2+)
- "Each fix reveals new problem in different place"
- Proposing solutions before tracing data flow

### 5. User Signal Detection (v3 addition)

Specific phrases from real human responses that indicate the agent is doing it wrong:
- "Is that not happening?" → You assumed without verifying
- "Will it show us...?" → You should have added evidence gathering
- "Stop guessing" → You're proposing fixes without understanding
- "Ultrathink this" → Question fundamentals, not just symptoms

### 6. Rationalization Prevention Table (v3 addition)

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from start |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem |

## Source evidence

- Qwen session `EVOLUTION_AND_ITEM_HISTORY.md` — hardening passes dated 2026-04-16
- Multi-component debugging derived from `macBaks` CI pipeline debugging sessions
- Architecture-questioning rule from `~/iterm2` debugging sessions with 4+ failed fix attempts

## Cross-links

- `verification-before-completion` v3 — used at Phase 4 Step 3
- `test-driven-development` — for creating the failing test in Phase 4 Step 1
- `root-cause-tracing.md` — supporting technique referenced inline
- `defense-in-depth.md` — supporting technique for multi-layer validation
