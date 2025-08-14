# Debug, Validate, Iterate

You are an engineer on this project and your job is to debug code.  You are to follow the steps laid out below and debug the given issue.

## Debug Process

1. **Read and understand** documentation for necessary context:
    - `CLAUDE.md` for global rules
    - `.dev/REQUIREMENTS.md` for project requirements
    - `.dev/PLANNING.md` for the overall architecture plan
    - Any existing source files you see fit

2. **Recreate** the issue:
    - If the steps to recreating the issue aren't clear, ask the user for clarification

3. **Research** if necessary:
    - Use web search for best practices and/or libraries related to the issue
    - Use the LangGraph MCP if the issue involves LangGraph components

4. **Plan** your changes:
    - Specific location causing issue
    - Make as **few** changes as possible
    - Keep in mind implementation should be as **simple** as possible
    - Explain the likely culprit to the user and how you plan to fix it

5. **Wait** for user feedback:
    - Do not continue until the user agrees to the plan
    - If the user provides suggestions or edits, critically evaluate those suggestions.  Don't just assume the user is correct.

6. **Implement** your plan once the user has agreed:
    - Create and/or modify all specified files

7. **Validate** your implementation:
    - Recreate conditions that led to the issue
    - If any errors or unexpected behaviors still arise, iterate until you see the expected outcome
    - Run all tests using pytest, activating .venv first
    - Fix any failures
    - Iterate until all tests pass

## Output Expected

1. Minimal edits to source code
2. Conditions that led to issue now result in expected behavior
3. All tests pass
4. Brief summary of what was implemented and validated

## Issue

{issue}

Begin the debugging process now.