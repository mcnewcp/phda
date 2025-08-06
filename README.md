# Personal Health Data Assistant (PHDA)

> A comprehensive AI-powered health tracking platform built with Python, LangGraph agents, and modern observability tools.

## Overview

The Personal Health Data Assistant (PHDA) is a monorepo containing four microservices designed to provide intelligent health data logging, analysis, and insights. The system uses LangGraph agents to parse natural language inputs into structured health data, performs automated analytics, and provides on-demand health insights—all with comprehensive monitoring via Arize Phoenix.

### Core Services

1. **AI Data Logger** - Converts natural language health inputs into structured database entries
   - *"I spent 25 minutes in the sauna this morning"* → Structured sauna log with timestamp
   - Supports heart rate, blood pressure, body composition, and sauna session logging
   
2. **Analytics Workflows** - Automated data processing and predictive modeling
   - Batch imports from health devices and apps
   - Statistical analysis and trend detection
   - Predictive health modeling
   
3. **AI Analytics Assistant** - Interactive health data analysis
   - *"How's my blood pressure trending compared to last month?"*
   - Natural language queries with intelligent responses
   
4. **Phoenix Monitor** - Comprehensive AI agent observability
   - Real-time tracing of all LLM interactions
   - Performance monitoring and debugging tools

## Architecture

### Technology Stack

- **Python 3.12+** with `uv` for fast dependency management
- **FastAPI** for service APIs with automatic OpenAPI documentation
- **SQLAlchemy 2.0** with Alembic migrations for robust database management
- **PostgreSQL 15** for reliable data persistence
- **LangGraph** for building sophisticated AI agent workflows
- **OpenAI GPT-4o-mini** and **Ollama** support for flexible LLM deployment
- **Arize Phoenix** for comprehensive agent monitoring and tracing
- **Docker Compose** for streamlined development and deployment

### Monorepo Structure

```
phda/
├── pyproject.toml              # Single root configuration with dependency groups
├── uv.lock                     # Unified dependency lockfile
├── docker-compose.yml          # Development environment orchestration
├── alembic.ini                 # Database migration configuration
├── .env.example                # Environment variable template
├── migrations/                 # Shared database migrations
│   ├── env.py                  # Migration environment setup
│   └── versions/               # Version-controlled schema changes
├── shared/
│   ├── models/                 # SQLAlchemy database models
│   │   ├── base.py            # Base model configuration
│   │   └── health_logs.py     # Health tracking table definitions
│   └── utils/
│       └── database.py        # Database session management utilities
└── services/
    ├── ai-data-logger/        # Natural language health data parser
    ├── analytics-workflows/   # Automated data processing pipeline
    ├── ai-analytics-assistant/# Interactive health analysis agent
    └── phoenix-monitor/       # AI observability dashboard
```

## Database Schema

The system tracks six core health metrics with timezone-aware timestamps:

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `heart_log` | Blood pressure & heart rate | `systolic_mmhg`, `diastolic_mmhg`, `rate_bpm` |
| `body_log` | Body composition metrics | `weight_lb`, `smm_lb`, `pbf`, `ecw_tcw` |
| `nutrition_log` | Food intake tracking | `protein_g`, `sodium_mg`, `potassium_mg` |
| `caffeine_log` | Caffeine consumption | `item_description`, `caffeine_mg` |
| `alcohol_log` | Alcohol consumption | `item_description`, `alcohol_oz` |
| `sauna_log` | Sauna session tracking | `duration_min`, `temperature_f` |

All tables include auto-incrementing `id` primary keys and timezone-aware `datetime` fields (US/Central timezone).

## Quick Start

### Prerequisites

- Python 3.12+
- Docker and Docker Compose
- OpenAI API key (optional - defaults to Ollama)

### Installation

1. **Clone and setup dependencies:**
   ```bash
   git clone <repository-url>
   cd phda
   uv sync                    # Install all dependencies
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration:
   # - Set LLM_PROVIDER=openai (or ollama)
   # - Add your OPENAI_API_KEY if using OpenAI
   ```

3. **Start services:**
   ```bash
   docker-compose up          # Start all services
   uv run alembic upgrade head # Apply database migrations
   ```

4. **Verify installation:**
   ```bash
   curl http://localhost:8001/health  # AI Data Logger health check
   open http://localhost:6006         # Phoenix monitoring dashboard
   ```

## Usage Examples

### Natural Language Health Logging

The AI Data Logger accepts conversational inputs and intelligently parses them:

```bash
# Simple sauna session
curl -X POST http://localhost:8001/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "I spent 25 minutes in a 180F sauna this morning"}]}'

# Blood pressure with context
curl -X POST http://localhost:8001/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "My blood pressure was 120/80 with heart rate 65 after my workout yesterday at 3pm"}]}'

# Body composition data
curl -X POST http://localhost:8001/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "This morning I weighed 185 lbs with 22% body fat, 85 lbs muscle mass, and 0.38 water ratio"}]}'
```

### Conversation History Support

The system maintains conversation context for follow-up questions:

```bash
curl -X POST http://localhost:8001/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "I had a sauna session this morning"},
      {"role": "assistant", "content": "How long was your sauna session?"},
      {"role": "user", "content": "Actually it was 25 minutes at 174F"}
    ]
  }'
```

## Development

### Local Development Setup

```bash
# Install service-specific dependencies
uv sync --group ai-data-logger --group dev

# Run individual services locally
cd services/ai-data-logger
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8001

# Run tests with coverage
uv run pytest --cov=shared --cov=services --cov-fail-under=80

# Code formatting and linting
uv run black .
uv run ruff check --fix
```

### Database Management

```bash
# Create new migration
uv run alembic revision --autogenerate -m "Add new health metric"

# Apply migrations
uv run alembic upgrade head

# View migration history
uv run alembic history
```

### Testing Agent Functionality

```bash
# Test with shell script
./services/ai-data-logger/scripts/test_agent.sh "I did a 30 minute sauna session at 9am"

# Direct API testing
curl -X POST http://localhost:8001/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Test prompt here"}]}'
```

## Development Standards

### Code Quality Requirements

- **File Size Limit:** Maximum 500 lines per source file
- **Test Coverage:** Minimum 80% coverage required
- **Documentation:** Google-style docstrings on all public methods
- **Code Style:** Black formatting with 88-character line length
- **Type Safety:** Full type hints using Python 3.12+ syntax

### Test-Driven Development (TDD)

The project follows strict TDD practices:

1. **Write tests first** describing expected behavior
2. **Run tests** to confirm they fail (red state)
3. **Implement minimal code** to pass tests
4. **Iterate** until all tests pass (green state)
5. **Refactor** while maintaining green tests

### Environment Configuration

Essential environment variables:

```bash
# LLM Provider Selection
LLM_PROVIDER=openai              # Options: openai, ollama
OPENAI_API_KEY=your_key_here     # Required if using OpenAI

# Database Configuration
DATABASE_URL=postgresql://phda_user:phda_password@db:5432/phda_dev

# Monitoring
PHOENIX_COLLECTOR_ENDPOINT=http://phoenix-monitor:4317
```

## AI Agent Architecture

### LangGraph Implementation

All AI functionality uses LangGraph with manual graph construction for maximum control and learning:

```python
# Example agent structure
def create_health_logger_agent():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", tool_node)
    
    # Define routing logic
    workflow.add_conditional_edges("agent", should_continue, {...})
    workflow.add_edge("tools", "agent")
    
    return workflow.compile()
```

### Phoenix Monitoring Integration

All agent interactions are traced through Arize Phoenix:

- **Real-time tracing** of LLM calls and tool executions
- **Performance metrics** and latency monitoring
- **Debug capabilities** with full conversation history
- **Project isolation** for different agent types

Access the Phoenix dashboard at `http://localhost:6006` after starting services.

## Deployment

### Docker Compose Deployment

The system is designed for easy deployment via Docker Compose:

```bash
# Production deployment
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# View service logs
docker-compose logs -f ai-data-logger

# Scale specific services
docker-compose up -d --scale ai-data-logger=3
```

### Service Dependencies

Services have health checks and proper dependency ordering:

1. **PostgreSQL** starts first with health checks
2. **Phoenix Monitor** starts with telemetry collection
3. **Application services** start after dependencies are healthy
4. **Automatic restart** on failure

## Current Status

### ✅ Completed Features

- **Core Infrastructure:** Monorepo setup with uv dependency management
- **Database Layer:** PostgreSQL with SQLAlchemy 2.0 and Alembic migrations
- **AI Data Logger Service:** Natural language parsing with LangGraph agents
- **Multi-LLM Support:** OpenAI GPT-4o-mini and Ollama integration
- **Health Logging:** Heart rate, blood pressure, body composition, and sauna tracking
- **API Layer:** FastAPI with conversation history support
- **Monitoring:** Arize Phoenix integration for agent observability
- **Containerization:** Docker Compose development environment
- **Testing:** Comprehensive test scripts and API validation

### 🚧 In Development

- **Analytics Workflows Service:** Automated data processing and statistical analysis
- **AI Analytics Assistant Service:** Interactive health data querying
- **Advanced Time Parsing:** Enhanced natural language datetime processing
- **Data Visualization:** Health metrics dashboards and trend analysis
- **Mobile Integration:** API endpoints for mobile app development

### 🔮 Planned Features

- **Predictive Modeling:** Machine learning for health trend prediction
- **Integration APIs:** Connect with popular health apps and devices
- **Advanced Analytics:** Correlation analysis and personalized insights
- **Multi-user Support:** User management and data isolation
- **Export Capabilities:** PDF reports and data export functionality

## Contributing

### Development Workflow

1. **Create feature branch** from `main`
2. **Write tests first** following TDD principles
3. **Implement feature** with proper error handling
4. **Ensure test coverage** meets 80% minimum
5. **Update documentation** including docstrings and README
6. **Submit pull request** with detailed description

### Code Review Requirements

- All tests must pass with minimum 80% coverage
- Code must follow Black formatting standards
- Type hints required on all function signatures
- Google-style docstrings on all public methods
- Phoenix tracing properly implemented for AI features

## Support

### Common Commands

```bash
# Development setup
uv sync                                     # Install all dependencies
docker-compose up                           # Start development environment
uv run alembic upgrade head                 # Apply database migrations

# Testing
uv run pytest --cov=shared --cov=services  # Run tests with coverage
./services/ai-data-logger/scripts/test_agent.sh  # Test AI agent

# Service management
docker-compose logs ai-data-logger          # View service logs
docker-compose restart ai-data-logger       # Restart specific service
```

### Troubleshooting

- **Database connection issues:** Check PostgreSQL container health and credentials
- **Agent not responding:** Verify LLM provider configuration and API keys
- **Phoenix not collecting traces:** Confirm collector endpoint and container networking
- **Import errors:** Ensure `PYTHONPATH` includes project root directory

### Resources

- **LangGraph Documentation:** [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)
- **Arize Phoenix Guide:** [docs.arize.com/phoenix](https://docs.arize.com/phoenix/)
- **SQLAlchemy 2.0 Tutorial:** [docs.sqlalchemy.org](https://docs.sqlalchemy.org/en/20/tutorial/)
- **uv Package Manager:** [docs.astral.sh/uv](https://docs.astral.sh/uv/)

---

**License:** MIT | **Python Version:** 3.12+ | **Last Updated:** August 2025