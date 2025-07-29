# Create Lean PRP

## Feature file: $ARGUMENTS

Generate a concise, TDD-focused PRP optimized for context efficiency. Focus on essential information only.

## Research Process

1. **Find Key Patterns**
   - Identify 1-2 similar features to follow
   - Find critical test patterns 
   - Note essential gotchas only

2. **Identify Core Requirements**
   - Extract testable behaviors from feature file
   - Focus on success criteria that can be verified
   - Note integration points

## Lean PRP Generation

Using `dev/PRPs/templates/prp_base_lean.md`:

### Essential Context Only
- **One key pattern file** to follow
- **Critical gotchas** that will break implementation
- **Core test structure** needed

### Focused Implementation
- **Specific files** to create/modify
- **Key integration points** only
- **Validation commands** that must pass

## Output
Save as: `dev/PRPs/{phase_num}_{feature_name}_lean.md`

## Quality Check
- [ ] Core requirements clearly testable
- [ ] Essential patterns identified
- [ ] Critical gotchas included
- [ ] Validation commands executable
- [ ] Under 100 lines total

Focus on what's essential for successful TDD implementation, not comprehensive documentation.