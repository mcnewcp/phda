# Feature 1: Project Structure Setup

## Overview
Establish the foundational monorepo structure and Python environment management for the Personal Health Data Assistant (PHDA) project. This feature creates the complete directory structure, dependency management system, and basic configuration files that all subsequent features will build upon.

## Purpose
- Create a standardized, maintainable monorepo structure
- Establish uv-based dependency management with service-specific groups
- Set up environment variable templates and configuration
- Provide the foundation for containerized micro-services architecture

## Key Requirements

### Directory Structure
Must create the exact repository layout as specified in `dev/PLANNING.md`:

```
/ (repo root)
  ├─ .gitignore               # master ignore list for all services
  ├─ .env.example             # consolidated env-var template for the whole stack
  ├─ ai_data_logger/          # service 1 – LangGraph agent & tools
  ├─ data_workflows/          # service 2 – scheduled ETL jobs
  ├─ analytics_workflows/     # service 3 – stats + ML jobs (later)
  ├─ ai_analytics_assistant/  # service 4 – LangGraph analyst agent (later)
  ├─ ui/                      # service 5 – Streamlit app (later React)
  ├─ shared/                  # common utils, DB models, config helpers
  ├─ docker/                  # Dockerfiles & compose.yaml
  ├─ tests/                   # integration tests; each service holds its own unit tests
  └─ dev/
       ├─ PLANNING.md         # existing
       ├─ PRPs/               # Product Requirement Prompts reside here
       ├─ features/           # each numbered feature spec lives here
       └─ ...
```

### Python Environment Management
- **Primary Tool**: uv for virtual environment and dependency management
- **Python Version**: 3.11+
- **Architecture**: Single repo-wide virtual environment with dependency groups
- **Service Isolation**: Each service uses only its required dependency group

### Configuration Management
- Centralized `.env.example` with all environment variables needed across services
- python-dotenv integration for environment loading
- No secrets committed to repository

## Detailed Requirements

### 1. Root-Level Files

#### .gitignore
Must include comprehensive ignore patterns for:
- Python artifacts (`__pycache__/`, `*.pyc`, `.pytest_cache/`)
- Virtual environments (`.venv/`, `venv/`, `.uv/`)
- IDE files (`.vscode/`, `.idea/`, `*.swp`)
- Environment files (`.env`, `.env.local`)
- Docker artifacts (`docker-compose.override.yml`)
- Database files (`*.db`, `*.sqlite`)
- Logs (`logs/`, `*.log`)
- Build artifacts (`dist/`, `build/`, `*.egg-info/`)

#### .env.example
Must define all environment variables used across the stack:

```bash
# Database Configuration
POSTGRES_URL=postgresql://phda_user:phda_pass@localhost:5432/phda_db
POSTGRES_USER=phda_user
POSTGRES_PASSWORD=phda_pass
POSTGRES_DB=phda_db

# AI/ML APIs
OPENAI_API_KEY=your_openai_api_key_here
BING_SEARCH_API_KEY=your_bing_search_api_key_here

# Observability
ARIZE_API_KEY=your_arize_api_key_here
PHOENIX_COLLECTOR_URL=https://app.arize.com/v1/traces

# Application Configuration
USER_ID=mcnewcp
TIMEZONE=America/Chicago
LOG_LEVEL=INFO

# Service Ports
UI_PORT=8501
AI_LOGGER_PORT=8000
```

#### pyproject.toml
Must configure uv dependency management with service-specific groups:

```toml
[project]
name = "personal-health-data-assistant"
version = "0.1.0"
description = "AI-powered personal health data logging and analytics platform"
authors = [{name = "Your Name", email = "your.email@example.com"}]
readme = "README.md"
requires-python = ">=3.11"

dependencies = [
    # Core shared dependencies
    "python-dotenv>=1.0.0",
    "pydantic>=2.0.0",
    "sqlalchemy>=2.0.0",
    "alembic>=1.12.0",
    "psycopg2-binary>=2.9.0",
    "asyncpg>=0.29.0",
]

[dependency-groups]
ai_data_logger = [
    "langchain>=0.1.0",
    "langgraph>=0.0.40",
    "openai>=1.0.0",
    "arize-phoenix>=3.0.0",
    "requests>=2.31.0",
]

data_workflows = [
    "pandas>=2.0.0",
    "schedule>=1.2.0",
    "httpx>=0.24.0",
]

analytics_workflows = [
    "pandas>=2.0.0",
    "plotly>=5.15.0",
    "scikit-learn>=1.3.0",
]

ai_analytics_assistant = [
    "langchain>=0.1.0",
    "langgraph>=0.0.40",
    "pandas>=2.0.0",
    "matplotlib>=3.7.0",
]

ui = [
    "streamlit>=1.28.0",
    "plotly>=5.15.0",
]

dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.1.0",
    "black>=23.0.0",
    "mypy>=1.5.0",
    "pre-commit>=3.4.0",
]

[tool.ruff]
line-length = 88
target-version = "py311"
select = ["E", "F", "W", "C90", "I", "N", "UP", "B", "A", "S", "T20", "Q"]
ignore = ["E501"]  # Line too long (handled by black)

[tool.black]
line-length = 88
target-version = ['py311']

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
addopts = "-v --tb=short --strict-markers"
markers = [
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]
```

### 2. Service Directory Structure

Each service directory must contain:
- `__init__.py` (empty, makes it a Python package)
- `tests/` subdirectory with `__init__.py`
- Service-specific directories as needed

#### ai_data_logger/
```
ai_data_logger/
├─ __init__.py
├─ agent/
│  └─ __init__.py
├─ tools/
│  └─ __init__.py
├─ tests/
│  └─ __init__.py
└─ main.py (placeholder)
```

#### data_workflows/
```
data_workflows/
├─ __init__.py
├─ etl/
│  └─ __init__.py
├─ schedulers/
│  └─ __init__.py
├─ tests/
│  └─ __init__.py
└─ main.py (placeholder)
```

#### shared/
```
shared/
├─ __init__.py
├─ db/
│  ├─ __init__.py
│  └─ models.py (placeholder)
├─ utils/
│  ├─ __init__.py
│  ├─ config.py (placeholder)
│  └─ dates.py (placeholder)
├─ monitoring/
│  ├─ __init__.py
│  └─ phoenix.py (placeholder)
└─ tests/
   └─ __init__.py
```

#### docker/
```
docker/
├─ compose.yaml (placeholder)
├─ postgres/
│  └─ init.sql (placeholder)
└─ dockerfiles/
   └─ .keep
```

#### tests/
```
tests/
├─ __init__.py
├─ integration/
│  ├─ __init__.py
│  └─ test_placeholder.py
├─ fixtures/
│  ├─ __init__.py
│  └─ database.py (placeholder)
└─ conftest.py (placeholder)
```

#### dev/PRPs/
```
dev/PRPs/
├─ templates/
│  └─ prp_base.md (existing)
└─ .keep
```

### 3. Initial Documentation

#### README.md
Must include:
- Project overview and purpose
- Prerequisites (Python 3.11+, uv, Docker)
- Quick start instructions
- Development setup
- Service architecture overview
- Contributing guidelines

#### Basic Service Placeholders
Each service's `main.py` should contain a minimal placeholder:

```python
"""
[Service Name] - Part of Personal Health Data Assistant

This service handles [brief description].
Currently a placeholder for Phase 1 development.
"""

from __future__ import annotations

import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

def main() -> None:
    """Main entry point for [service name]."""
    logger.info("[Service Name] starting...")
    # Placeholder implementation
    logger.info("[Service Name] ready")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
```

## Key Deliverables

1. **Complete Directory Structure**: All directories and subdirectories created with proper `__init__.py` files
2. **Dependency Management**: `pyproject.toml` with all dependency groups defined
3. **Environment Configuration**: `.env.example` with all required variables
4. **Git Configuration**: Comprehensive `.gitignore` file
5. **Documentation**: Basic README.md with setup instructions
6. **Service Placeholders**: Basic `main.py` files for each service
7. **Test Structure**: Initial test directory structure with pytest configuration

## Acceptance Criteria

- [ ] All directories from PLANNING.md structure exist
- [ ] `pyproject.toml` defines all required dependency groups
- [ ] `.env.example` contains all environment variables needed for Phase 1
- [ ] `.gitignore` prevents committing sensitive files and build artifacts
- [ ] `uv sync --group dev` installs development dependencies without errors
- [ ] Each service directory is a valid Python package
- [ ] README.md provides clear setup instructions
- [ ] Test directory structure supports both unit and integration tests
- [ ] All placeholder files contain valid Python code with proper imports

## Dependencies
- None (this is the foundation feature)

## Estimated Effort
- **Complexity**: Low
- **Time**: 2-3 hours
- **Risk**: Low

## Notes
- This feature establishes conventions that all subsequent features must follow
- The dependency groups will be extended as features are added in later phases
- Service placeholders should be minimal but functional
- Focus on creating a solid foundation rather than implementing functionality