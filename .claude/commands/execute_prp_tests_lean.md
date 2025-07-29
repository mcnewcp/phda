# Execute PRP - Tests Only (Lean)

Write comprehensive tests for a feature based on the PRP file. Optimized for context efficiency.

## PRP File: $ARGUMENTS

## Process

1. **Load & Analyze PRP**
   - Read PRP file and identify all testable requirements
   - Find existing test patterns in codebase to follow

2. **Write Tests First**
   - **CRITICAL**: Write ONLY tests - no implementation code
   - Follow existing test patterns from similar features
   - Cover all PRP success criteria with tests
   - Use clear test names describing expected behavior

3. **Validate & Commit**
   - Run tests to confirm they fail appropriately 
   - Fix syntax errors but don't implement functionality
   - Commit with message: "Add tests for [feature]"

## Rules
- ✅ Write comprehensive test cases for all requirements
- ✅ Follow existing project test patterns
- ✅ Test happy path, errors, and edge cases
- ❌ No implementation code whatsoever
- ❌ No mock implementations or stubs
- ❌ Don't import non-existent modules in tests

## Validation
```bash
# Tests should fail for missing implementation
uv run pytest tests/test_[feature].py -v

# But syntax should be correct
uv run pytest tests/test_[feature].py --collect-only
```

Ready for `execute-prp-impl` after commit.