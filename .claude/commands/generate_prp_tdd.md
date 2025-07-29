# Create TDD-Optimized PRP

## Feature file: $ARGUMENTS

Generate a complete PRP optimized for Test-Driven Development (TDD) workflow. The PRP will enable AI agents to first write comprehensive tests, then implement code to pass those tests through iterative refinement.

Read the feature file first to understand requirements, then conduct thorough research to provide all context needed for successful TDD implementation.

## Research Process

1. **Codebase Analysis**
   - Search for similar features/patterns in the codebase
   - **CRITICAL**: Identify existing test patterns and conventions
   - Find test fixtures, helpers, and testing utilities
   - Note TDD-friendly patterns to follow
   - Check integration test approaches

2. **External Research**
   - Search for TDD examples and best practices for similar features
   - Library documentation focusing on testable APIs
   - Testing patterns specific to the technologies used
   - Common testing pitfalls and how to avoid them

3. **Test Strategy Planning**
   - Identify all testable behaviors and edge cases
   - Plan unit tests, integration tests, and validation tests
   - Consider test data needs and fixture requirements
   - Plan mocking strategy for external dependencies

## TDD-Optimized PRP Generation

Using `dev/PRPs/templates/prp_base.md` as template, but enhanced for TDD:

### Critical TDD Context to Include
- **Existing Test Patterns**: Real examples from the codebase showing how to structure tests
- **Test Data Requirements**: What fixtures, factories, or test data will be needed
- **Mocking Strategy**: Which external dependencies to mock and how
- **Test Coverage Plan**: Specific test cases that must be written
- **Validation Commands**: Exact commands to run tests and verify they fail appropriately

### TDD Implementation Blueprint
- **Test-First Task Breakdown**: Tests written before any implementation
- **Expected Test Structure**: Detailed examples of what tests should look like
- **Implementation Guidance**: Minimal code patterns to make tests pass
- **Refactoring Notes**: How to improve code quality once tests pass

### Two-Phase Validation Gates

#### Phase 1: Test Validation (Red State)
```bash
# Tests written but failing appropriately
uv run pytest tests/test_new_feature.py -v  # Should fail
uv run pytest tests/test_new_feature.py --collect-only  # Should succeed
```

#### Phase 2: Implementation Validation (Green State)  
```bash
# Tests passing after implementation
uv run pytest tests/test_new_feature.py -v  # Should pass
uv run ruff check src/ --fix && mypy src/
uv run pytest tests/ -v  # Full suite should pass
```

## Enhanced Context Requirements

### Test Pattern Examples
Include real examples from the codebase:
```python
# From tests/test_existing_feature.py (actual pattern to follow):
def test_function_name_happy_path():
    """Describe expected behavior in docstring."""
    # Arrange
    input_data = setup_test_data()
    
    # Act  
    result = function_under_test(input_data)
    
    # Assert
    assert result.success is True
    assert result.data == expected_output
```

### Testability Requirements
Ensure the PRP includes:
- Input/output specifications for every function
- Error conditions that must be tested
- Integration points that need test coverage
- Performance or behavior constraints to verify

### Implementation Constraints
- Code must be written to satisfy tests, not the other way around
- Tests should not be modified during implementation phase
- Implementation should be minimal to pass tests initially
- Refactoring happens only after tests pass

## Output Structure

Save as: `dev/PRPs/{phase_num}_{feature_name}_tdd.md`

Include these TDD-specific sections:
1. **Test Strategy First** - What tests will drive implementation
2. **Test-Driven Task Breakdown** - Tests before implementation in each task
3. **Expected Test Structure** - Detailed examples of required tests
4. **Two-Phase Validation** - Separate test and implementation validation
5. **TDD Anti-Patterns** - Common mistakes to avoid in TDD workflow

## Quality Checklist
- [ ] All testable behaviors identified and planned
- [ ] Existing test patterns documented and referenced
- [ ] Test data and fixture requirements specified
- [ ] Two-phase validation gates are executable
- [ ] Implementation guidance focuses on making tests pass
- [ ] TDD workflow clearly separated into test-first, then implementation
- [ ] Anti-patterns specifically call out test modification during implementation

## TDD Success Criteria

The PRP should enable:
1. **Tests written first** that fail for the right reasons
2. **Minimal implementation** that makes tests pass
3. **Iterative development** guided by test feedback
4. **Separate commits** for tests and implementation
5. **Refactoring confidence** with comprehensive test coverage

Score the PRP on TDD readiness (1-10): Confidence that AI can successfully write tests first, then implement code to pass them in separate phases.

Remember: The goal is true Test-Driven Development where tests genuinely drive the design and implementation, not just verify pre-written code.