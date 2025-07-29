# Phase 1: Project Structure Setup - PRP

## Goal
Establish the foundational monorepo structure and Python environment management for the Personal Health Data Assistant (PHDA) project. Create the complete directory structure, dependency management system with uv, environment configuration, and basic service placeholders that all subsequent features will build upon.

## Why
- **Foundation for Development**: Provides the standardized structure needed for all Phase 1-6 features
- **Developer Velocity**: Single repo-wide virtual environment with service-specific dependency groups enables fast development cycles
- **Containerization Ready**: Directory structure aligns with micro-services architecture for Docker containerization
- **Consistency**: Establishes patterns and conventions that prevent architectural drift as the project grows

## What
Create the exact repository layout specified in `dev/PLANNING.md` with:
- Complete directory structure with proper Python packages (`__init__.py` files)
- uv-based dependency management with service-specific groups
- Comprehensive environment variable configuration
- Git ignore patterns for Python monorepo
- Basic service placeholders with proper imports and structure
- Test framework configuration supporting both unit and integration tests

### Success Criteria
- [ ] All directories from PLANNING.md structure exist with proper `__init__.py` files
- [ ] `uv sync --group dev` installs development dependencies without errors
- [ ] Each service directory is a valid Python package importable by Python
- [ ] `.env.example` contains all environment variables needed for Phase 1
- [ ] All placeholder `main.py` files execute without import errors
- [ ] Test structure supports both unit tests (per service) and integration tests (root level)

## All Needed Context

### Documentation & References
```yaml
# MUST READ - Include these in your context window
- url: https://docs.astral.sh/uv/concepts/projects/dependencies/
  why: uv dependency groups (PEP 735) configuration and management
  critical: Use [dependency-groups] table, not [tool.uv.groups] - this follows PEP 735 standard

- url: https://docs.astral.sh/uv/guides/projects/
  why: uv project structure and workspace management for monorepos
  critical: Single virtual environment at repo root with dependency groups for service isolation

- url: https://docs.pytest.org/en/stable/explanation/goodpractices.html
  why: pytest configuration in pyproject.toml and monorepo testing patterns
  critical: Use [tool.pytest.ini_options] table, enable --import-mode=importlib for better isolation

- url: https://github.com/github/gitignore/blob/main/Python.gitignore
  why: Comprehensive Python gitignore template maintained by GitHub
  critical: Include modern tools like .pixi/, __pypackages__/, and uv cache directories

- file: dev/PLANNING.md
  why: Exact directory structure requirements and service definitions
  critical: Must match the repository layout exactly - this is the canonical source

- file: CLAUDE.md
  why: Global project rules including TDD workflow, file size limits, and coding standards
  critical: Follow all rules - never create files >500 lines, use TDD, follow PEP 8 with ruff/black
```

### Current Codebase Structure
```bash
/Users/coymcnew/code/personal-health-data-assistant/
├── .git/
├── .claude/
├── CLAUDE.md
├── README.md
└── dev/
    ├── PLANNING.md
    ├── PRPs/
    │   └── templates/
    │       └── prp_base.md
    └── features/
        └── phase_1_project_structure.md
```

### Desired Codebase Structure with Files to be Added
```bash
/Users/coymcnew/code/personal-health-data-assistant/
├── .gitignore                    # Comprehensive Python patterns + monorepo specific
├── .env.example                  # All environment variables for Phase 1
├── pyproject.toml               # uv dependency groups + tool configuration
├── README.md                    # Updated with setup instructions
├── CLAUDE.md                    # Existing - keep as-is
├── ai_data_logger/              # Service 1 - LangGraph agent
│   ├── __init__.py
│   ├── agent/
│   │   └── __init__.py
│   ├── tools/
│   │   └── __init__.py
│   ├── tests/
│   │   └── __init__.py
│   └── main.py                  # Placeholder implementation
├── data_workflows/              # Service 2 - ETL jobs
│   ├── __init__.py
│   ├── etl/
│   │   └── __init__.py
│   ├── schedulers/
│   │   └── __init__.py
│   ├── tests/
│   │   └── __init__.py
│   └── main.py                  # Placeholder implementation
├── analytics_workflows/         # Service 3 - Stats + ML (later)
│   ├── __init__.py
│   ├── tests/
│   │   └── __init__.py
│   └── main.py                  # Placeholder implementation
├── ai_analytics_assistant/      # Service 4 - Analyst agent (later)
│   ├── __init__.py
│   ├── tests/
│   │   └── __init__.py
│   └── main.py                  # Placeholder implementation
├── ui/                          # Service 5 - Streamlit app
│   ├── __init__.py
│   ├── tests/
│   │   └── __init__.py
│   └── main.py                  # Placeholder implementation
├── shared/                      # Common utilities and models
│   ├── __init__.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── models.py            # SQLAlchemy models placeholder
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py            # Environment loading helper
│   │   └── dates.py             # Date utilities for America/Chicago
│   ├── monitoring/
│   │   ├── __init__.py
│   │   └── phoenix.py           # Phoenix tracing setup
│   └── tests/
│       └── __init__.py
├── docker/                      # Docker configuration
│   ├── compose.yaml             # Docker Compose placeholder
│   ├── postgres/
│   │   └── init.sql             # Database initialization
│   └── dockerfiles/
│       └── .keep                # Placeholder for future Dockerfiles
├── tests/                       # Integration tests
│   ├── __init__.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_placeholder.py  # Sample integration test
│   ├── fixtures/
│   │   ├── __init__.py
│   │   └── database.py          # Test database fixtures
│   └── conftest.py              # pytest configuration
└── dev/                         # Existing - keep as-is
    ├── PLANNING.md
    ├── PRPs/
    │   ├── templates/
    │   │   └── prp_base.md
    │   └── phase_1_project_structure.md  # This file
    └── features/
        └── phase_1_project_structure.md
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: uv dependency groups follow PEP 735 standard
# Use [dependency-groups] table in pyproject.toml, not [tool.uv.groups]
# Groups are resolved together - ensure compatibility across all groups

# CRITICAL: pytest configuration in pyproject.toml
# Use [tool.pytest.ini_options] table, not [tool.pytest]
# Enable --import-mode=importlib for better isolation in monorepo

# CRITICAL: Service isolation with uv
# Each service uses: uv sync --group <service_name>
# Dev dependencies: uv sync --group dev (includes base dependencies)
# Never mix direct pip installs with uv in same project

# CRITICAL: Python imports in monorepo
# Use absolute imports from repo root: from shared.db.models import Model
# Each service directory must have __init__.py to be importable
# Shared code should be in shared/ directory, not duplicated

# CRITICAL: Environment variable loading
# Call load_dotenv() early in each service's main.py
# Use os.getenv() with defaults, never os.environ[] directly
# Timezone handling requires specific America/Chicago setup
```

## Implementation Blueprint

### Data Models and Structure
Create the foundational file structure that supports the micro-services architecture:

```python
# pyproject.toml structure follows uv dependency groups pattern
[project]
dependencies = [
    # Core shared dependencies used by all services
    "python-dotenv>=1.0.0",
    "pydantic>=2.0.0", 
    "sqlalchemy>=2.0.0",
    # ... other shared deps
]

[dependency-groups]
ai_data_logger = [
    "langchain>=0.1.0",
    "langgraph>=0.0.40",
    # ... AI-specific deps
]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.1.0",
    # ... dev tools
]

# Each service main.py follows this pattern:
"""
Service Name - Part of Personal Health Data Assistant

This service handles [specific responsibility].
Currently a placeholder for Phase 1 development.
"""

from __future__ import annotations

import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

def main() -> None:
    """Main entry point for service."""
    logger.info("Service starting...")
    # Placeholder implementation
    logger.info("Service ready")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
```

### List of Tasks to be Completed in Order

```yaml
Task 1: Create Root Configuration Files
CREATE .gitignore:
  - USE GitHub's official Python.gitignore as base
  - ADD uv-specific patterns: .uv/, uv.lock
  - ADD Docker patterns: docker-compose.override.yml
  - ADD IDE patterns: .vscode/, .idea/
  - ADD logs/ and *.log patterns

CREATE pyproject.toml:
  - FOLLOW exact dependency groups from feature file
  - CONFIGURE ruff, black, mypy, pytest tools
  - USE [tool.pytest.ini_options] with --import-mode=importlib
  - SET line-length = 88, python >=3.11

CREATE .env.example:
  - INCLUDE all environment variables from feature file
  - USE descriptive comments for each variable
  - NEVER include actual secrets, only placeholders

Task 2: Create Service Directory Structure
CREATE ai_data_logger/ directory:
  - ADD __init__.py (empty)
  - CREATE agent/ subdirectory with __init__.py
  - CREATE tools/ subdirectory with __init__.py
  - CREATE tests/ subdirectory with __init__.py
  - ADD main.py with service placeholder template

CREATE data_workflows/ directory:
  - ADD __init__.py (empty)
  - CREATE etl/ subdirectory with __init__.py
  - CREATE schedulers/ subdirectory with __init__.py
  - CREATE tests/ subdirectory with __init__.py
  - ADD main.py with service placeholder template

CREATE analytics_workflows/ directory:
  - ADD __init__.py (empty)
  - CREATE tests/ subdirectory with __init__.py
  - ADD main.py with service placeholder template

CREATE ai_analytics_assistant/ directory:
  - ADD __init__.py (empty)
  - CREATE tests/ subdirectory with __init__.py
  - ADD main.py with service placeholder template

CREATE ui/ directory:
  - ADD __init__.py (empty)
  - CREATE tests/ subdirectory with __init__.py
  - ADD main.py with service placeholder template

Task 3: Create Shared Library Structure
CREATE shared/ directory:
  - ADD __init__.py (empty)
  - CREATE db/ subdirectory with __init__.py and models.py placeholder
  - CREATE utils/ subdirectory with __init__.py, config.py, dates.py placeholders
  - CREATE monitoring/ subdirectory with __init__.py and phoenix.py placeholder
  - CREATE tests/ subdirectory with __init__.py

Task 4: Create Docker and Testing Infrastructure
CREATE docker/ directory:
  - ADD compose.yaml placeholder with basic structure
  - CREATE postgres/ subdirectory with init.sql placeholder
  - CREATE dockerfiles/ subdirectory with .keep file

CREATE tests/ directory:
  - ADD __init__.py (empty)
  - CREATE integration/ subdirectory with __init__.py and test_placeholder.py
  - CREATE fixtures/ subdirectory with __init__.py and database.py placeholder
  - ADD conftest.py with basic pytest configuration

Task 5: Update Documentation
MODIFY README.md:
  - ADD project overview and purpose
  - ADD prerequisites (Python 3.11+, uv, Docker)
  - ADD quick start instructions using uv
  - ADD development setup workflow
  - ADD service architecture overview
```

### Per Task Pseudocode

```python
# Task 1: pyproject.toml creation
[project]
name = "personal-health-data-assistant"
requires-python = ">=3.11"
dependencies = ["python-dotenv>=1.0.0", "pydantic>=2.0.0", ...]

[dependency-groups]
ai_data_logger = ["langchain>=0.1.0", ...]
dev = ["pytest>=7.4.0", "ruff>=0.1.0", ...]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["-v", "--tb=short", "--import-mode=importlib"]

# Task 2: Service main.py template
"""
{Service Name} - Part of Personal Health Data Assistant

This service handles {brief description}.
Currently a placeholder for Phase 1 development.
"""

from __future__ import annotations
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def main() -> None:
    logger.info("{Service Name} starting...")
    logger.info("{Service Name} ready")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

# Task 3: shared/utils/config.py pattern
from __future__ import annotations
import os
from dotenv import load_dotenv

load_dotenv()

def get_database_url() -> str:
    return os.getenv("POSTGRES_URL", "postgresql://phda_user:phda_pass@localhost:5432/phda_db")

# Task 5: README.md structure
# Personal Health Data Assistant

## Overview
AI-powered personal health data logging and analytics platform...

## Prerequisites
- Python 3.11+
- uv (Python package manager)
- Docker & Docker Compose

## Quick Start
```bash
# Clone and setup
git clone <repo>
cd personal-health-data-assistant

# Install dependencies
uv sync --group dev

# Verify setup
uv run python -m ai_data_logger.main
```
```

### Integration Points
```yaml
UV_ENVIRONMENT:
  - virtual_env: Single .venv at repo root
  - command: "uv sync --group dev" installs development dependencies
  - command: "uv sync --group ai_data_logger" installs only AI service deps

IMPORT_STRUCTURE:
  - pattern: "from shared.db.models import Model"
  - pattern: "from ai_data_logger.agent import Agent"
  - requirement: All directories need __init__.py files

ENVIRONMENT_LOADING:
  - pattern: "load_dotenv()" at top of each main.py
  - pattern: "os.getenv('VAR_NAME', 'default')" for all env access
  - location: ".env.example" documents all required variables
```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Run these FIRST - fix any errors before proceeding
uv sync --group dev                    # Install dev dependencies
uv run ruff check . --fix             # Auto-fix style issues
uv run ruff format .                   # Format code with ruff
uv run mypy shared/ ai_data_logger/    # Type checking on created modules

# Expected: No errors. If errors exist, read and fix before proceeding.
```

### Level 2: Structure Validation
```bash
# Verify Python package structure
uv run python -c "import ai_data_logger; print('✓ ai_data_logger')"
uv run python -c "import data_workflows; print('✓ data_workflows')"
uv run python -c "import shared; print('✓ shared')"
uv run python -c "import shared.utils.config; print('✓ shared.utils.config')"

# Verify service main modules execute
uv run python -m ai_data_logger.main
uv run python -m data_workflows.main
uv run python -m ui.main

# Expected: All imports succeed, all main modules print startup messages
```

### Level 3: Dependency Group Validation
```bash
# Test service-specific dependency installations
uv sync --group ai_data_logger         # Should install AI/LangChain deps
uv sync --group data_workflows         # Should install pandas/schedule deps
uv sync --group dev                    # Should install testing/linting deps

# Verify no dependency conflicts
uv pip list | grep -E "(langchain|pandas|pytest|ruff)"

# Expected: All groups install without conflicts, expected packages present
```

### Level 4: Environment and Configuration
```bash
# Test environment variable loading
echo 'POSTGRES_URL=test://localhost/test' > .env
uv run python -c "from shared.utils.config import get_database_url; print(get_database_url())"

# Verify pytest configuration
uv run pytest --collect-only          # Should discover tests without errors
uv run pytest tests/integration/test_placeholder.py -v

# Expected: Environment loading works, pytest finds and runs tests
```

## Final Validation Checklist
- [ ] All services import successfully: `uv run python -c "import ai_data_logger, data_workflows, shared"`
- [ ] No linting errors: `uv run ruff check .`
- [ ] No type errors: `uv run mypy shared/`
- [ ] All service main modules execute: `uv run python -m ai_data_logger.main`
- [ ] Development dependencies install: `uv sync --group dev`
- [ ] Service-specific deps install: `uv sync --group ai_data_logger`
- [ ] Environment variables load correctly
- [ ] Git ignores build artifacts and sensitive files
- [ ] README provides clear setup instructions

---

## Anti-Patterns to Avoid
- ❌ Don't create directories without `__init__.py` files - they won't be importable
- ❌ Don't use `[tool.uv.groups]` - use `[dependency-groups]` following PEP 735
- ❌ Don't put real secrets in `.env.example` - only use placeholder values
- ❌ Don't create files over 500 lines (CLAUDE.md rule) - keep placeholders minimal
- ❌ Don't skip the import validation step - broken imports will cascade to all features
- ❌ Don't hardcode paths or values that should come from environment variables

## PRP Confidence Score: 9/10

This PRP provides comprehensive context, executable validation steps, and follows established patterns from the research. The high confidence comes from:
- Detailed research on uv dependency groups and monorepo best practices
- Clear validation gates that can be executed programmatically  
- Specific gotchas and patterns identified from external sources
- Step-by-step task breakdown with pseudocode
- Alignment with existing CLAUDE.md and PLANNING.md requirements

The 1-point deduction accounts for potential edge cases in environment setup that may require minor adjustments during implementation.