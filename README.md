# Personal Health Data Assistant (PHDA)

AI-powered personal health data logging and analytics platform built with Python, LangGraph, and modern observability tools.

## Overview

The Personal Health Data Assistant is a Python-first, containerized micro-services stack that enables users to:

1. **Log health events** in natural language via an AI Data Logger agent
2. **Ingest daily data** from Apple Health exports and other sources via automated workflows
3. **View interactive dashboards** of near-real-time stats and trends  
4. **Ask free-form questions** to an AI Analytics Assistant
5. **Receive insights** from model-based predictions and personalized analytics (future phases)

## Architecture

The system is built as a monorepo with service-specific dependency groups:

- **ai_data_logger/** - LangGraph ReAct agent for natural language health logging
- **data_workflows/** - Scheduled ETL jobs and data import workflows
- **analytics_workflows/** - Statistics, analytics, and ML workflow processing
- **ai_analytics_assistant/** - LangGraph analyst agent for Q&A (Phase 4+)
- **ui/** - Streamlit web interface (later React SPA)
- **shared/** - Common utilities, database models, and configuration helpers
- **docker/** - Docker Compose and containerization configuration
- **tests/** - Integration tests and shared testing infrastructure

## Prerequisites

- **Python 3.11+** - Primary runtime environment
- **uv** - Fast Python package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- **Docker & Docker Compose** - For containerized services and PostgreSQL
- **Git** - Version control

## Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd personal-health-data-assistant

# Copy environment variables template
cp .env.example .env
# Edit .env with your actual API keys and configuration

# Install development dependencies
uv sync --group dev

# Verify setup by running service placeholders
uv run python -m ai_data_logger.main
uv run python -m data_workflows.main
uv run python -m ui.main

# Start PostgreSQL database (optional)
docker compose -f docker/compose.yaml up postgres -d
```

## Development Setup

### Environment Configuration

1. Copy `.env.example` to `.env`
2. Update the following variables:
   - `OPENAI_API_KEY` - Your OpenAI API key for LangGraph agents
   - `BING_SEARCH_API_KEY` - Bing Search API key for web search tool
   - `ARIZE_API_KEY` - Arize API key for Phoenix observability
   - Database credentials (if using custom PostgreSQL setup)

### Service-Specific Dependencies

Install dependencies for specific services:

```bash
# AI services (LangChain, LangGraph, OpenAI)
uv sync --group ai_data_logger

# Data processing (pandas, scheduling)
uv sync --group data_workflows

# Analytics and ML (pandas, plotly, scikit-learn)
uv sync --group analytics_workflows

# UI development (Streamlit, plotly)
uv sync --group ui

# All development tools (pytest, ruff, mypy, etc.)
uv sync --group dev
```

### Code Quality

```bash
# Format code
uv run ruff format .

# Lint and fix issues
uv run ruff check . --fix

# Type checking  
uv run mypy shared/

# Run tests
uv run pytest tests/ -v
```

## Service Architecture

### Phase 1 (Current) - Logging MVP
- Manual LangGraph ReAct agent (GPT-4o)
- PostgreSQL container with single user (`user_id='mcnewcp'`)
- Minimal Streamlit chat interface
- Phoenix cloud tracing integration

### Phase 2 - Local ETL & Self-Hosted Phoenix
- Health Auto Export endpoint and parser
- Scheduled ETL container operations  
- Self-hosted Phoenix Docker service
- Dashboard skeleton implementation

### Phase 3 - Descriptive Analytics
- Analytics Workflows container computing aggregates
- Interactive dashboard plots with Plotly
- Daily/weekly health summaries

### Future Phases
- AI Analytics Assistant with read-only DB access
- Personalized ML models and predictions
- React SPA with REST API gateways

## Contributing

### Code Standards
- Follow PEP 8 via ruff and black (88-character lines)
- Use type hints with `from __future__ import annotations`
- Write unit tests for all new functionality
- Keep source files under 500 lines
- Follow Test-Driven Development (TDD) workflow

### Development Workflow
1. Create feature branch from main
2. Write failing tests first
3. Implement code to pass tests
4. Run full validation suite
5. Submit pull request

### File Structure
```
├── .gitignore              # Comprehensive Python + Docker patterns
├── .env.example            # Environment variables template
├── pyproject.toml          # uv dependency groups + tool config
├── ai_data_logger/         # LangGraph agent service
├── data_workflows/         # ETL and scheduling service
├── analytics_workflows/    # Analytics and ML service
├── ai_analytics_assistant/ # Q&A agent service (Phase 4+)
├── ui/                     # Streamlit web interface
├── shared/                 # Common utilities and models
├── docker/                 # Docker Compose configuration
├── tests/                  # Integration tests
└── dev/                    # Planning, PRPs, and feature specs
```

## License

[Add your license information here]

## Support

For questions, issues, or contributions, please [create an issue](../../issues) in this repository.