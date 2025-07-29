# Execute PRP - Implementation Only

Write implementation code to make existing tests pass, following TDD best practices.

## PRP File: $ARGUMENTS

## Implementation-Only Execution Process

1. **Load Context**
   - Read the specified PRP file for implementation guidance
   - Review existing test files to understand expected behavior
   - Identify all failing tests that need to pass
   - **DO NOT** modify any test files during this phase

2. **ULTRATHINK Implementation Strategy**
   - Analyze test expectations to understand required implementation
   - Plan minimal code needed to make tests pass
   - Identify existing patterns and utilities to reuse
   - Break down implementation into logical components
   - Use TodoWrite tool to track implementation progress

3. **Implement Minimal Code**
   - Write only enough code to make tests pass (green state)
   - Follow patterns identified in existing codebase
   - Start with simplest implementation that satisfies tests
   - **ABSOLUTE RULE**: Never modify test files
   - Focus on making tests pass, not on perfect architecture initially

4. **Iterative Development**
   - Run tests frequently during development
   - Fix failing tests one at a time
   - Iterate: code → test → adjust → test again
   - If tests seem wrong, STOP and discuss with user before changing them

5. **Code Quality Standards**
   - Follow all rules in CLAUDE.md (PEP 8, type hints, docstrings)
   - Keep functions focused and files under 500 lines
   - Use appropriate error handling and logging
   - Follow existing architectural patterns

6. **Validation Loop**
   - Run all tests and confirm they pass
   - Run linting (ruff) and type checking (mypy)
   - Verify no regressions in existing functionality
   - Test integration points manually if needed

7. **Refactor for Quality**
   - Once tests pass, improve code quality if needed
   - Extract common functionality into shared utilities
   - Optimize performance if necessary
   - Ensure code is maintainable and follows project standards

8. **Final Verification**
   - Run complete test suite to ensure no regressions
   - Verify all PRP requirements are implemented
   - Check that implementation integrates properly with existing code
   - Confirm all validation steps from PRP pass

## Key Rules for Implementation-Only Phase

### ✅ DO
- Write minimal code to make tests pass
- Follow existing code patterns and conventions
- Use appropriate error handling and logging
- Keep implementation focused and maintainable
- Run tests frequently during development
- Refactor code once tests pass

### ❌ DO NOT
- Modify test files under any circumstances
- Write more code than necessary to pass tests
- Ignore failing tests or make them pass by hacking
- Skip validation steps (linting, type checking)
- Break existing functionality
- Deviate from project architectural patterns

## When Tests Seem Wrong

If during implementation you discover tests that seem incorrect:

1. **STOP implementation work immediately**
2. **Document the specific issue with the test**
3. **Explain why the test expectation seems wrong**
4. **Ask user for clarification before proceeding**
5. **Only modify tests after explicit user approval**
6. **If tests are modified, commit them separately before continuing**

## Commit Instructions

After implementation is complete:
1. **Verify all tests pass**: Run complete test suite
2. **Run quality checks**: Linting, type checking, etc.
3. **Commit implementation only**: Use commit message format "Implement [feature]: [brief description]"
4. **Do not commit any test changes**

## Success Criteria

- [ ] All tests pass (green state)
- [ ] No linting or type checking errors
- [ ] No regressions in existing functionality
- [ ] Implementation follows project standards and patterns
- [ ] All PRP requirements are satisfied
- [ ] Code is maintainable and well-documented
- [ ] Commit contains only implementation code

## Integration Testing

After implementation:
- Run any integration tests specified in the PRP
- Test the feature manually end-to-end
- Verify the feature works as expected in the broader system
- Check that error handling works appropriately

## Next Steps

After committing implementation, the feature should be complete and ready for use. If additional changes are needed, follow the same TDD cycle: tests first, then implementation.