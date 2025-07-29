# Base PRP Template v3 - TDD-Optimized Context-Rich Implementation

## Purpose
Template optimized for Test-Driven Development (TDD) workflow where AI agents first write comprehensive tests, then implement code to pass those tests through iterative refinement.

## Core Principles
1. **Tests Drive Implementation**: Write failing tests first, then minimal code to pass
2. **Context is King**: Include ALL necessary documentation, examples, and caveats
3. **Separate Commits**: Tests committed first, implementation committed separately
4. **Validation Loops**: Executable tests guide iterative development
5. **Information Dense**: Use keywords and patterns from the codebase
6. **Global Rules**: Follow all rules in CLAUDE.md

---

## Goal
[What needs to be built - be specific about the end state and desires]

## Why
- [Business value and user impact]
- [Integration with existing features]
- [Problems this solves and for whom]

## What
[User-visible behavior and technical requirements]

### Success Criteria
- [ ] [Specific measurable outcomes that tests will verify]

## All Needed Context

### Documentation & References (list all context needed to implement the feature)
```yaml
# MUST READ - Include these in your context window
- url: [Official API docs URL]
  why: [Specific sections/methods you'll need]
  
- file: [path/to/example.py]
  why: [Pattern to follow, gotchas to avoid]
  
- doc: [Library documentation URL] 
  section: [Specific section about common pitfalls]
  critical: [Key insight that prevents common errors]

- docfile: [PRPs/ai_docs/file.md]
  why: [docs that the user has pasted in to the project]
```

### Current Codebase Tree
```bash
# Run `tree` in the root of the project to get an overview
[Include current directory structure]
```

### Desired Codebase Tree with Files to be Added
```bash
# Show exactly what files will be created and their responsibilities
[Include target directory structure with new files]
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: [Library name] requires [specific setup]
# Example: FastAPI requires async functions for endpoints
# Example: This ORM doesn't support batch inserts over 1000 records
# Example: We use pydantic v2 and certain patterns changed
```

### Existing Test Patterns
```python
# CRITICAL: Follow these exact patterns from the codebase
# Example from tests/test_existing_feature.py:
def test_happy_path():
    """Test description following project conventions"""
    # Setup
    input_data = SomeModel(field="value")
    
    # Execute
    result = function_under_test(input_data)
    
    # Assert
    assert result.status == "success"
    assert result.data.field == "expected_value"

# Example fixture pattern:
@pytest.fixture
def sample_data():
    """Provide test data following project patterns"""
    return create_test_data()
```

## TDD Implementation Blueprint

### Test Strategy First
Define comprehensive test cases that will drive the implementation:

```python
# Unit Tests Required (write these FIRST):
# 1. test_[function_name]_happy_path()
# 2. test_[function_name]_validation_error()  
# 3. test_[function_name]_edge_cases()
# 4. test_[class_name]_initialization()
# 5. test_[class_name]_state_changes()

# Integration Tests Required:
# 1. test_[feature]_end_to_end()
# 2. test_[feature]_database_integration()
# 3. test_[feature]_external_api_integration()

# Error Condition Tests:
# 1. test_[function]_handles_network_timeout()
# 2. test_[function]_handles_invalid_input()
# 3. test_[function]_handles_database_error()
```

### Data Models and Structure
Create the core data models that tests will expect:

```python
# Examples of what tests will expect to exist:
# - ORM models with specific fields and methods
# - Pydantic models with validation rules
# - Pydantic schemas for API requests/responses
# - Custom validators and type definitions

# Tests will verify:
# - Model field types and constraints
# - Validation behavior for invalid data
# - Serialization/deserialization
# - Database schema compliance
```

### Test-Driven Task Breakdown

```yaml
TDD Phase 1 - Write Tests:
Task 1: Create Unit Tests
  CREATE tests/test_new_feature.py:
    - FOLLOW pattern from tests/test_similar_feature.py
    - WRITE tests for each function/method before implementation exists
    - INCLUDE positive, negative, and edge case tests
    - USE descriptive test names that explain expected behavior
    - DO NOT create any implementation code

Task 2: Create Integration Tests
  CREATE tests/integration/test_new_feature_integration.py:
    - TEST end-to-end workflows
    - TEST database interactions
    - TEST external API integrations
    - MOCK external dependencies appropriately

Task 3: Validate Test Suite
  RUN tests and confirm they fail appropriately:
    - Verify failures indicate missing implementation
    - Fix any test syntax errors
    - Ensure tests cover all requirements
  COMMIT failing tests with message: "Add tests for [feature]"

TDD Phase 2 - Implement Code:
Task 4: Implement Core Models
  CREATE src/new_feature.py:
    - IMPLEMENT minimal code to pass model tests
    - FOLLOW patterns from existing similar modules
    - DO NOT modify test files

Task 5: Implement Business Logic  
  MODIFY src/new_feature.py:
    - ADD functions/methods to pass logic tests
    - ITERATE: run tests → fix code → repeat
    - STOP if tests seem wrong - ask for clarification

Task 6: Implement Integration Points
  MODIFY relevant integration modules:
    - ADD database models/migrations
    - ADD API endpoints/routes
    - ADD configuration/environment handling
    - ENSURE all integration tests pass

Task 7: Final Implementation Polish
  REFACTOR code once tests pass:
    - OPTIMIZE performance if needed
    - IMPROVE code organization
    - ADD comprehensive docstrings
    - ENSURE follows all project standards
  COMMIT implementation with message: "Implement [feature]"
```

### Expected Test Structure

```python
# tests/test_new_feature.py structure:
"""
Test module for new feature functionality.

Tests drive the implementation by defining expected behavior
before any implementation code is written.
"""

import pytest
from unittest.mock import Mock, patch

from src.new_feature import NewFeature, process_data  # Will not exist initially
from shared.db.models import SomeModel  # Existing model
from shared.utils.exceptions import ValidationError  # Existing exception


class TestNewFeature:
    """Test cases for NewFeature class."""
    
    def test_initialization_with_valid_data(self):
        """NewFeature should initialize correctly with valid parameters."""
        # This test defines what the constructor should accept
        feature = NewFeature(param1="value1", param2=42)
        assert feature.param1 == "value1"
        assert feature.param2 == 42
        assert feature.status == "initialized"
    
    def test_initialization_raises_validation_error_for_invalid_data(self):
        """NewFeature should raise ValidationError for invalid parameters."""
        with pytest.raises(ValidationError, match="param1 cannot be empty"):
            NewFeature(param1="", param2=42)
    
    def test_process_method_returns_expected_result(self):
        """process() method should return correctly formatted result."""
        feature = NewFeature(param1="test", param2=10)
        result = feature.process()
        
        assert result.success is True
        assert result.data["processed_value"] == "test_processed"
        assert result.data["multiplied_value"] == 100  # 10 * 10


def test_process_data_function_happy_path():
    """process_data() should handle standard input correctly."""
    input_data = {"key": "value", "number": 5}
    result = process_data(input_data)
    
    assert result["status"] == "success"
    assert result["processed_key"] == "VALUE"  # uppercase transformation
    assert result["calculated_number"] == 25   # squared


def test_process_data_function_handles_missing_keys():
    """process_data() should handle missing required keys gracefully."""
    input_data = {"key": "value"}  # missing 'number'
    
    with pytest.raises(KeyError, match="Required key 'number' not found"):
        process_data(input_data)


@pytest.fixture
def sample_feature():
    """Provide a configured NewFeature instance for testing."""
    return NewFeature(param1="test_data", param2=100)
```

## TDD Validation Loops

### Phase 1: Test Validation (Red State)
```bash
# Run these to validate tests are written correctly:
uv run pytest tests/test_new_feature.py -v
# Expected: All tests FAIL due to missing implementation

# Verify test syntax is correct:
uv run pytest tests/test_new_feature.py --collect-only
# Expected: Tests are discovered without syntax errors

# Check test coverage planning:
uv run pytest tests/test_new_feature.py --co -q | wc -l
# Expected: Sufficient number of test cases for complete coverage
```

### Phase 2: Implementation Validation (Green State)
```bash
# Run during implementation iterations:
uv run pytest tests/test_new_feature.py -v
# Goal: Make tests pass one by one

# Verify code quality during implementation:
uv run ruff check src/new_feature.py --fix
uv run mypy src/new_feature.py

# Run full test suite to check for regressions:
uv run pytest tests/ -v
# Expected: All tests pass, no existing functionality broken
```

### Phase 3: Integration Validation
```bash
# Test the complete feature end-to-end:
uv run pytest tests/integration/test_new_feature_integration.py -v

# Run any manual validation steps from requirements:
# [Include specific curl commands, database queries, or other verification steps]
```

## Final Validation Checklist

### Test Phase Completion
- [ ] All unit tests written and failing appropriately: `uv run pytest tests/test_new_feature.py -v`
- [ ] Integration tests written and failing appropriately
- [ ] Tests cover all success criteria from PRP
- [ ] Test syntax validated: `uv run pytest --collect-only`
- [ ] Tests committed with clear message

### Implementation Phase Completion  
- [ ] All tests pass: `uv run pytest tests/test_new_feature.py -v`
- [ ] No linting errors: `uv run ruff check src/`
- [ ] No type errors: `uv run mypy src/`
- [ ] Integration tests pass: `uv run pytest tests/integration/ -v`
- [ ] No regressions: `uv run pytest tests/ -v`
- [ ] Manual validation successful: [specific commands from PRP]
- [ ] Implementation committed with clear message

---

## TDD Anti-Patterns to Avoid

### During Test Writing Phase
- ❌ Don't write any implementation code, even "harmless" stubs
- ❌ Don't create mock implementations that make tests pass
- ❌ Don't write tests that will always pass regardless of implementation
- ❌ Don't skip edge cases or error condition tests
- ❌ Don't write overly specific tests that constrain implementation unnecessarily

### During Implementation Phase
- ❌ Don't modify test files to make implementation easier
- ❌ Don't write more code than needed to pass tests
- ❌ Don't skip failing tests or hack them to pass
- ❌ Don't ignore linting/type checking errors
- ❌ Don't break existing functionality

### Process Anti-Patterns
- ❌ Don't commit tests and implementation together
- ❌ Don't skip the "tests fail first" validation step
- ❌ Don't implement before writing tests
- ❌ Don't modify tests during implementation without explicit approval