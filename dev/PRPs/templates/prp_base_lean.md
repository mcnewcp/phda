# Lean PRP Template - TDD Optimized

## Goal
[Specific, measurable outcome - what needs to be built]

## Context
```yaml
# Essential reading only
- file: [path/to/key_pattern.py]
  why: [Follow this exact pattern]
  
- url: [critical_docs_url]  
  section: [specific section needed]
  
- gotcha: [Critical library quirk that will break implementation]
```

## Requirements
- [Testable requirement 1]
- [Testable requirement 2] 
- [Error condition that must be handled]

## Test Strategy
```python
# Required test cases (write these FIRST):
def test_happy_path():
    # Test core functionality works
    
def test_validation_errors():
    # Test input validation and error handling
    
def test_edge_cases():
    # Test boundary conditions
```

## Implementation Notes
```python
# Key patterns to follow:
class NewFeature:
    def __init__(self, param: str):
        # Follow pattern from similar_feature.py
        
    def process(self) -> Result:
        # Return format: {"status": "success", "data": {...}}
```

## Files to Create/Modify
- `tests/test_[feature].py` - Test cases
- `src/[feature].py` - Main implementation  
- `src/[existing].py` - Integration points

## Validation
```bash
# Phase 1: Tests fail appropriately
uv run pytest tests/test_[feature].py -v

# Phase 2: Tests pass, no regressions
uv run pytest tests/ -v && ruff check --fix
```

## Success Criteria
- [ ] All requirements have passing tests
- [ ] Integration works with existing code
- [ ] Error handling works correctly