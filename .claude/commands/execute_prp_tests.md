# Execute PRP - Tests Only

Write comprehensive tests for a feature based on the PRP file, following TDD best practices.

## PRP File: $ARGUMENTS

## Tests-Only Execution Process

1. **Load PRP Context**
   - Read the specified PRP file completely
   - Understand all requirements and success criteria
   - Identify all testable behaviors and edge cases
   - Research existing test patterns in the codebase

2. **ULTRATHINK Test Strategy**
   - Plan comprehensive test coverage for all PRP requirements
   - Identify unit tests, integration tests, and validation tests needed
   - Break down complex features into testable components
   - Use TodoWrite tool to track test implementation plan
   - **CRITICAL**: Plan tests that will drive proper implementation

3. **Write Tests First**
   - **ABSOLUTE RULE**: Write ONLY test code - no implementation whatsoever
   - Create unit tests for every function, class, method, and behavior
   - Write integration tests for service interactions
   - Use clear input/output expectations to define behavior
   - **DO NOT** create mock implementations, stubs, or placeholder functions
   - **DO NOT** import modules that don't exist yet - tests should expect them
   - Focus on describing desired behavior through test assertions

4. **Test Structure Requirements**
   - Follow existing test patterns from codebase
   - Use pytest fixtures and markers appropriately
   - Include both positive and negative test cases
   - Test error conditions and edge cases
   - Write descriptive test names that explain the behavior being tested

5. **Validate Test Quality**
   - Run tests and confirm they fail for the right reasons
   - Verify test failures indicate missing implementation, not syntax errors
   - Ensure tests are isolated and don't depend on each other
   - Check test coverage addresses all PRP requirements

6. **Document Test Intentions**
   - Add docstrings to test functions explaining what behavior is being verified
   - Include comments for complex test setup or assertions
   - Document any test data or fixtures used

7. **Ready for Implementation**
   - Confirm all tests are written and failing appropriately
   - Verify tests will guide proper implementation
   - Ensure tests are comprehensive enough to catch regressions

## Key Rules for Tests-Only Phase

### ✅ DO
- Write comprehensive test cases covering all PRP requirements
- Use clear, descriptive test names and docstrings
- Test both happy path and error conditions
- Follow existing test patterns and conventions
- Use appropriate pytest fixtures and markers
- Write tests that will catch implementation bugs

### ❌ DO NOT
- Write any implementation code whatsoever
- Create placeholder functions or mock implementations  
- Import modules that don't exist yet
- Write tests that will always pass regardless of implementation
- Modify existing implementation files
- Write overly specific tests that constrain implementation unnecessarily

## Commit Instructions

After completing tests:
1. **Run test validation**: Confirm tests fail appropriately
2. **Review test completeness**: Ensure all PRP requirements are covered
3. **Commit tests only**: Use commit message format "Add tests for [feature]: [brief description]"
4. **Do not commit any implementation code**

## Success Criteria

- [ ] All PRP requirements have corresponding tests
- [ ] Tests fail when run (red state)
- [ ] Test failures indicate missing implementation, not syntax errors
- [ ] Tests follow project conventions and patterns
- [ ] Test coverage includes edge cases and error conditions
- [ ] Tests are isolated and independent
- [ ] Commit contains only test files

## Next Steps

After committing tests, use `execute-prp-impl` to write the implementation that makes these tests pass.