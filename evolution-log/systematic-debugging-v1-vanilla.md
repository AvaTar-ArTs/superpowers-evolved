# systematic-debugging v1 — Vanilla (obra/superpowers)

> This is the canonical `obra/superpowers` version preserved as reference.
> See v3 for the active evolved version.

## Four Phases

### Phase 1: Root Cause Investigation
1. Read error messages completely — don't skip
2. Reproduce consistently
3. Check recent changes
4. Gather evidence

### Phase 2: Pattern Analysis
1. Find working examples
2. Compare against references
3. Identify differences
4. Understand dependencies

### Phase 3: Hypothesis and Testing
1. Form single hypothesis
2. Test minimally
3. Verify before continuing

### Phase 4: Implementation
1. Create failing test case
2. Implement single fix
3. Verify fix

## Red Flags
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "Pattern says X but I'll adapt it differently"
