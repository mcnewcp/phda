# CLAUDE.md - Global Rules and Guidance for Claude Code

## Project Context
You are working on `phda`, a health tracking application using AI to help users log, analyze, and understand health data through natural language interactions.

## Global Development Rules

### Language and Framework Requirements
- Python 3.11+ for all backend code
- FastAPI for API endpoints
- LangGraph for agent orchestration
- LangChain for LLM integration
- pytest and pytest-asyncio for testing
- No unnecessary dependencies - keep it minimal but functional

### Code Style and Quality
- Follow PEP 8 for Python code
- Use type hints for all function signatures
- Docstrings for all public functions and classes
- Keep functions small and focused (< 30 lines preferred)
- Meaningful variable names - no single letters except for indices

### File Organization
- Source code in `src/` directory
- Tests in `tests/` directory
- All imports should be absolute from `src` package

### Documentation
- Keep comments concise and relevant
- Document "why" not "what" in code comments

### Simplicity Principle
**SIMPLICITY IS KING** - Always choose the simpler solution when multiple approaches exist. This is not production software. Make it work, make it clear, keep it simple. However, it should be a **real working implementation** - not mocked or faked. 

## Important Reminders
- Clarity over cleverness
- Do not optimize prematurely
- Ask for clarification if requirements are ambiguous
- Validate assumptions with tests
- **activate .venv** prior to running any commands
- The user does not need a sycophant.  The user needs an equal who will openly discuss and correct them when they're wrong.  You should be critical of the user's decisions and suggestions. 
