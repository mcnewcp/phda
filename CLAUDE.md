# PHDA Development Context

## Project Overview

**Personal Health Data Assistant (PHDA)** is a Python monorepo containing four microservices:

1. **AI Data Logger** - Parses natural language input ("I ate oatmeal") into structured health logs
2. **Analytics Workflows** - Automated data import, stats calculation, and predictive modeling  
3. **AI Analytics Assistant** - On-demand health data analysis ("How's my sleep vs last month?")
4. **Phoenix Monitor** - Containerized Arize Phoenix for agent monitoring

All services share database models and communicate via a unified web app interface.

## Architecture

- **Monorepo** with shared database models in `shared/models/`
- **Single PostgreSQL database** with health tracking tables
- **Docker Compose** for local development
- **LangGraph agents** for all AI functionality
- **Arize Phoenix tracing** for all agent interactions

## Database Schema

Core health tracking tables:
- `heart_log` - Blood pressure and heart rate measurements
- `body_log` - Weight, muscle mass, body fat, hydration metrics
- `nutrition_log` - Food intake with protein/sodium/potassium tracking
- `caffeine_log` - Caffeine consumption tracking
- `alcohol_log` - Alcohol consumption tracking  
- `sauna_log` - Sauna session duration tracking

All tables use `datetime` (timezone-aware) and auto-incrementing `id` primary keys.

## Technology Stack

- **Python 3.12+** with uv for dependency management
- **FastAPI** for service APIs
- **SQLAlchemy 2.0** with Alembic migrations
- **PostgreSQL 15** via Docker
- **LangGraph** for all AI agents
- **Arize Phoenix** for agent monitoring and tracing
- **Docker Compose** for development environment

## Development Standards

### Dependency Management
- **Single repo-wide uv environment** at project root
- **Dependency groups** per service (keep minimal)
- All Python commands executed via `uv`: `uv run pytest`, `uv run alembic upgrade head`
- Add dependencies: `uv add package-name --group service-name`

### Environment Variables
- Maintain `.env.example` with all required dev environment variables
- Never commit actual `.env` files
- Load via `python-dotenv` in application code

### Agent Development
- **All agents use LangGraph** - no direct OpenAI API calls
- **Instrument with Phoenix tracing** following [LangGraph integration guide](https://arize.com/docs/phoenix/integrations/frameworks/langchain/langchain-tracing)
- Configure tracing in agent initialization, not per-call

### Code Quality Standards

#### File Size Limits
- **Maximum 500 lines per source file**
- Refactor into modules/helpers when approaching limit
- Prefer composition over large monolithic files

#### Test-Driven Development (TDD)
When implementing new features:
1. **Write tests first** - describe expected input/output pairs
2. **Do NOT create mock implementations** - write real test cases
3. **Run tests** and confirm they fail (red state)
4. **Commit failing tests**
5. **Implement code** to pass tests without modifying test files
6. **Iterate**: run tests → adjust code → re-run until green
7. **Commit passing code**

After logic updates:
- **Review and update existing tests** as necessary
- **Maintain ≥80% test coverage**
- Run: `uv run pytest --cov=shared --cov=services --cov-fail-under=80`

#### Documentation Requirements
- **Google-style docstrings** on all public methods
- **Comment non-obvious code** for mid-level developer comprehension
- **Include `# Reason:` comments** explaining complex logic decisions
- **Update README.md** when features, dependencies, or setup change

#### Development Principles
- **Simplicity is king** - avoid over-engineering
- **Never assume missing context** - ask clarifying questions
- **Never hallucinate** libraries or functions - only use verified packages
- **Confirm file paths** and module names exist before referencing
- **Microservices approach** - each service self-contained and containerized

## Project Structure

```
phda/
├── pyproject.toml              # Single root configuration
├── uv.lock                     # Unified dependency lockfile  
├── docker-compose.yml          # Development environment
├── alembic.ini                 # Migration configuration
├── .env.example                # Required environment variables
├── migrations/
│   ├── env.py                  # Shared migration environment
│   └── versions/               # Migration files
├── shared/
│   ├── models/
│   │   ├── base.py
│   │   └── health_logs.py      # All health tracking tables
│   └── utils/                  # Common utilities
└── services/
    ├── ai-data-logger/
    ├── analytics-workflows/
    ├── ai-analytics-assistant/
    └── phoenix-monitor/
```

## Common Commands

**Setup:**
```bash
uv sync                                    # Install all dependencies
docker-compose up                          # Start all services
uv run alembic upgrade head                # Run migrations
```

**Development:**
```bash
uv sync --group ai-data-logger --group dev # Install service deps
uv run pytest                             # Run tests
uv run pytest --cov=shared --cov=services # Run with coverage
uv add package-name --group service-name  # Add dependency
```

**Database:**
```bash
uv run alembic revision --autogenerate -m "description"  # Create migration
uv run alembic upgrade head                               # Apply migrations
```

## Import Patterns

- Shared models: `from shared.models.health_logs import HeartLog, BodyLog`
- Shared utilities: `from shared.utils.database import get_session`
- Service communication via environment variables and HTTP

## Key Constraints

- **No workspace packages** - single pyproject.toml with dependency groups
- **Phoenix tracing required** for all agent interactions
- **TDD workflow** for new feature development
- **80% test coverage minimum**
- **500 line file size limit**
- **Google docstring standard**