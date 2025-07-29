# Execute PRP - Implementation Only (Lean)

Implement code to make existing tests pass. Optimized for fresh context.

## PRP File: $ARGUMENTS

## Process

1. **Load Context**
   - Read PRP file for requirements
   - Examine test files to understand expected behavior
   - **Never modify test files**

2. **Implement Iteratively**
   - Write minimal code to make tests pass
   - Run tests frequently: code → test → adjust → repeat
   - Follow patterns from existing similar code
   - Stop if tests seem wrong - ask before changing them

3. **Validate & Commit**
   - All tests pass: `uv run pytest tests/test_[feature].py -v`
   - Code quality: `uv run ruff check --fix && mypy`
   - Commit: "Implement [feature]"

## Rules
- ✅ Make tests pass with minimal code
- ✅ Follow existing codebase patterns
- ✅ Iterate based on test feedback
- ❌ Never modify test files
- ❌ Don't write more code than needed to pass tests
- ❌ Don't ignore failing tests

## Success: All tests green, code committed.