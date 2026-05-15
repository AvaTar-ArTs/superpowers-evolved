# verification-before-completion v3 — Battle-Hardened

## What changed from v1

### 1. The Iron Law (v2 addition)

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

The vanilla skill had a checklist. v2 formalized it as law. v3 added enforcement: "If you
haven't run the verification command in this message, you cannot claim it passes."

### 2. The Gate Function (v3 addition)

A 5-step algorithmic gate that must be executed before any success claim:

```
1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim
```

### 3. Common Failures Table (v3 addition)

v1 said "verify before claiming done." v3 specifies exactly what verification each claim
type requires — and what is NOT sufficient:

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test command output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check, extrapolation |
| Build succeeds | Build command: exit 0 | Linter passing, logs look good |
| Bug fixed | Test original symptom: passes | Code changed, assumed fixed |
| Agent completed | VCS diff shows changes | Agent reports "success" |

### 4. Rationalization Prevention Table (v3 addition)

Every excuse the agent has been observed using, mapped to reality:

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Linter passed" | Linter ≠ compiler |
| "Agent said success" | Verify independently |
| "I'm tired" | Exhaustion ≠ excuse |
| "Different words so rule doesn't apply" | Spirit over letter |

### 5. Red Flag Detection (v3 addition)

Specific agent behaviors that trigger STOP:
- Using "should", "probably", "seems to"
- Expressing satisfaction before verification ("Great!", "Perfect!", "Done!")
- About to commit/push/PR without verification
- Trusting agent success reports
- **ANY wording implying success without having run verification**

### 6. Pattern Examples (v3 addition)

Concrete ✅/❌ examples for tests, regression tests (red-green cycle), builds, requirements
checklists, and agent delegation — showing exactly what verification looks like vs what
pretending looks like.

## Source evidence

- 24 failure memories collected across sessions where incomplete verification caused:
  - Undefined functions shipped (would crash)
  - Missing requirements shipped (incomplete features)
  - Trust broken ("I don't believe you")
  - Time wasted on false completion → redirect → rework

## Cross-links

- `systematic-debugging` v3 — Phase 4 Step 3 uses this as the verification gate
- `test-driven-development` — red-green cycle verification pattern
