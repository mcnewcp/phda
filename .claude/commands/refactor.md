# Refactor & Simplify Project

We are in the middle of developing this project and the codebase is starting to feel over-engineered.  Your job is to review the project from a holistic perspective and suggest areas for simplification, combination, and condensation, following the process below and the task given.

## Refactor Process

1. **Read and understand** documentation for necessary context:
    - `CLAUDE.md` for global rules and guidelines
    - `.dev/REQUIREMENTS.md` for project requirements
    - `.dev/PLANNING.md` for project development plan
    - `README.md` for current project status
    - Any existing source files you see fit

2. **Research** if necessary:
    - Use web search for best practices and/or libraries related to the task
    - Use the LangGraph MCP if the task involves LangGraph components

3. **Plan** a refactoring strategy that:
    - Reduces complexity
    - Improves human readability
    - Reduces total lines of code
    - Reduces total number of files
    - Condenses testing strategy
    - Removes unnecessary tests

4. **Explain** your plan to the user:
    - Display details of which files you'll modify or create
    - Justify your suggested changes.  What do they accomplish?
    - Validation strategy

5. **Wait** for user feedback:
    - Do not continue until the user agrees to the plan
    - If the user provides suggestions or edits, critically evaluate those suggestions.  Don't just assume the user is correct.

6. **Implement** your plan once the user has agreed.

7. **Test** the refactored code

8. **Iterate** if any tests fail until all tests pass

## Output Expected

1. Simplified codebase
2. Implementation validated
3. Brief summary, including justification or measurement of impact

## Task

{task}

Begin the process now.