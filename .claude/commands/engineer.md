# Plan, Implement, Validate, Iterate

You are an engineer on this project and your job is development.  You are to follow the steps laid out below and execute the given task.

## Development Process

1. **Read and understand** documentation for necessary context:
    - `CLAUDE.md` for global rules
    - `.dev/REQUIREMENTS.md` for project requirements
    - `.dev/PLANNING.md` for the overall architecture plan
    - Any existing source files you see fit

2. **Research** if necessary:
    - Use web search for best practices and/or libraries related to the task
    - Use the LangGraph MCP if the task involves LangGraph components

3. **Plan** your changes:
    - Specific files to create or modify
    - Classes and functions to implement
    - Validation strategy (unit tests, integration tests, or manual verification)
    - Keep in mind implementation should be as **simple** as possible

4. **Explain** your plan to the user:
    - Display details of which files you'll modify or create
    - Justify your suggested changes.  What do they accomplish?
    - Validation strategy

5. **Wait** for user feedback:
    - Do not continue until the user agrees to the plan
    - If the user provides suggestions or edits, critically evaluate those suggestions.  Don't just assume the user is correct.

6. **Implement** your plan once the user has agreed:
    - Create and/or modify all specified files
    - Implement all classes and/or functions
    - Use appropriate type hints and docstrings

7. **Write tests** according to your chosen validation strategy:
    - Use pytest and pytest-asyncio where appropriate
    - Ensure tests are independent and idempotent

8. **Validate** your implementation:
    - Run the tests using pytest, activating .venv first
    - Fix any failures
    - Iterate until all tests pass
    - For manual verification, describe what you tested

## Output Expected

1. Source code in `src/` directory
2. Tests in `tests/` directory, when appropriate
3. Implementation validated
4. Brief summary of what was implemented and validated

## Task

{task}

Begin the process now.