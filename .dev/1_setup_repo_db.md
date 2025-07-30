# PHDA Repository Structure and Docker Setup Requirements

## Overview

The Personal Health Data Assistant (PHDA) project requires a robust monorepo architecture supporting four microservices (ai-data-logger, analytics-workflows, ai-analytics-assistant, phoenix-monitor) with shared database models, containerized deployment, and modern Python tooling. This setup enables atomic changes across services, simplified dependency management, and scalable development workflows while maintaining service autonomy through proper isolation patterns.

The architecture leverages uv for fast dependency management, Docker Compose for local development and deployment orchestration, PostgreSQL for shared data persistence, and Alembic for coordinated database migrations. This configuration supports both rapid development iteration and production deployment while following established patterns from companies like Opendoor and Netflix.

## Examples

### Recommended Directory Structure

```
phda/
├── pyproject.toml              # Single root configuration
├── uv.lock                     # Unified dependency lockfile
├── docker-compose.yml          # Development environment
├── alembic.ini                 # Migration configuration
├── migrations/
│   ├── env.py                  # Shared migration environment
│   └── versions/               # Migration files
├── shared/
│   ├── models/                 # SQLAlchemy database models
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── health_logs.py
│   └── utils/                  # Common utilities
└── services/
    ├── ai-data-logger/
    │   ├── Dockerfile
    │   └── app/
    ├── analytics-workflows/
    │   ├── Dockerfile
    │   └── app/
    ├── ai-analytics-assistant/
    │   ├── Dockerfile
    │   └── app/
    └── phoenix-monitor/
        ├── Dockerfile
        └── app/
```

### Root pyproject.toml Configuration

```toml
[project]
name = "phda"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "sqlalchemy>=2.0.0",
    "alembic>=1.12.0",
    "psycopg2-binary>=2.9.0",
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0"
]

[dependency-groups]
ai-data-logger = [
    "fastapi>=0.100.0",
    "uvicorn>=0.23.0",
    "langgraph>=0.1.0",
    "openai>=1.0.0",
    "httpx>=0.24.0"
]

analytics-workflows = [
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "scikit-learn>=1.3.0",
    "langgraph>=0.1.0",
    "scipy>=1.11.0"
]

ai-analytics-assistant = [
    "fastapi>=0.100.0",
    "uvicorn>=0.23.0",
    "langgraph>=0.1.0",
    "openai>=1.0.0",
    "httpx>=0.24.0"
]

phoenix-monitor = [
    "arize-phoenix>=4.0.0",
    "fastapi>=0.100.0",
    "uvicorn>=0.23.0"
]

dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "black>=23.0.0",
    "ruff>=0.1.0"
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 88
target-version = ["py312"]

[tool.ruff]
target-version = "py312"
line-length = 88
select = ["E", "W", "F", "I"]
```

### Docker Compose Configuration

```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: phda_dev
      POSTGRES_USER: phda_user
      POSTGRES_PASSWORD: phda_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U phda_user -d phda_dev"]
      interval: 10s
      timeout: 3s
      retries: 3

  ai-data-logger:
    build: 
      context: .
      dockerfile: services/ai-data-logger/Dockerfile
    ports:
      - "8001:8000"
    environment:
      DATABASE_URL: postgresql://phda_user:phda_password@db:5432/phda_dev
    volumes:
      - ./services/ai-data-logger:/app/services/ai-data-logger
      - ./shared:/app/shared
    depends_on:
      db:
        condition: service_healthy

volumes:
  postgres_data:
```

### Shared Database Models

**shared/models/base.py:**
```python
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)
```

**shared/models/health_logs.py:**
```python
from sqlalchemy import Column, Integer, String, DateTime, Float
from .base import Base

class HeartLog(Base):
    __tablename__ = 'heart_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    systolic_mmhg = Column(Integer, nullable=False)
    diastolic_mmhg = Column(Integer, nullable=False)
    rate_bpm = Column(Integer, nullable=False)

class BodyLog(Base):
    __tablename__ = 'body_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    weight_lb = Column(Float, nullable=False)
    smm_lb = Column(Float, nullable=False)
    pbf = Column(Float, nullable=False)
    ecw_tcw = Column(Float, nullable=False)

class NutritionLog(Base):
    __tablename__ = 'nutrition_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    short_description = Column(String(255), nullable=False)
    protein_g = Column(Float, nullable=False)
    sodium_mg = Column(Float, nullable=False)
    potassium_mg = Column(Float, nullable=False)
    long_description = Column(String, nullable=False)

class CaffeineLog(Base):
    __tablename__ = 'caffeine_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    item_description = Column(String(255), nullable=False)
    caffeine_mg = Column(Float, nullable=False)

class AlcoholLog(Base):
    __tablename__ = 'alcohol_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    item_description = Column(String(255), nullable=False)
    alcohol_oz = Column(Float, nullable=False)

class SaunaLog(Base):
    __tablename__ = 'sauna_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    duration_min = Column(Integer, nullable=False)
```

### Alembic Configuration

**alembic.ini:**
```ini
[alembic]
script_location = migrations
sqlalchemy.url = postgresql://phda_user:phda_password@localhost:5432/phda_dev

[loggers]
keys = root,sqlalchemy,alembic

[logger_root]
level = WARN
handlers = console

[logger_alembic]
level = INFO
handlers = console

[handlers]
keys = console

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatters]
keys = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
```

**migrations/env.py:**
```python
from alembic import context
from sqlalchemy import engine_from_config, pool
import os

# Import all models
from shared.models.base import Base
from shared.models import health_logs

config = context.config

# Override database URL from environment
database_url = os.getenv('DATABASE_URL')
if database_url:
    config.set_main_option('sqlalchemy.url', database_url)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
```

### Service Dockerfile Template

**services/ai-data-logger/Dockerfile:**
```dockerfile
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Copy dependency files
COPY uv.lock pyproject.toml ./

# Install dependencies for this service
RUN uv sync --frozen --no-group dev --group ai-data-logger

# Copy application code
COPY shared/ ./shared/
COPY services/ai-data-logger/ ./services/ai-data-logger/

# Set Python path
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app/services/ai-data-logger

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Documentation

### Official Documentation Links

**uv Documentation:**
- [Dependency Groups](https://docs.astral.sh/uv/concepts/dependency-groups/)
- [Docker Integration](https://docs.astral.sh/uv/guides/integration/docker/)

**Docker Documentation:**
- [Docker Compose Specification](https://docs.docker.com/compose/compose-file/)
- [PostgreSQL Docker Hub](https://hub.docker.com/_/postgres)

**SQLAlchemy and Alembic:**
- [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## Other Considerations

### Essential Development Setup

**Dependency Management:**
- Install all dependencies: `uv sync`
- Install service-specific: `uv sync --group ai-data-logger --group dev`
- Add new dependencies: `uv add fastapi --group ai-data-logger`

**Database Setup:**
- Run migrations: `uv run alembic upgrade head`
- Create new migration: `uv run alembic revision --autogenerate -m "description"`

**Docker Development:**
- Start all services: `docker-compose up`
- Rebuild after changes: `docker-compose up --build`
- View logs: `docker-compose logs ai-data-logger`

### Common Gotchas

**Import Paths:**
- Use direct imports: `from shared.models.health_logs import HeartLog, BodyLog`
- All shared code is accessible from project root

**Docker Issues:**
- Services communicate using container names (not localhost)
- Set `PYTHONUNBUFFERED=1` to see real-time logs
- Wait for database health check before starting services

**Database Connections:**
- Use environment variables for DATABASE_URL
- Run migrations before starting services
- Services should retry database connections on startup

This setup provides everything needed to get PHDA development started while keeping complexity minimal.

## Validation

Complete these checks to confirm the feature is working:

- [ ] Repository structure matches the documented layout
- [ ] `uv sync` installs all dependencies without errors
- [ ] `uv sync --group ai-data-logger --group dev` installs service-specific dependencies
- [ ] `docker-compose up` starts PostgreSQL container successfully
- [ ] Database health check passes (visible in docker logs)
- [ ] Can connect to database at `localhost:5432` with credentials from docker-compose.yml
- [ ] `uv run alembic upgrade head` creates all 6 health tracking tables
- [ ] Database contains tables: `heart_log`, `body_log`, `nutrition_log`, `caffeine_log`, `alcohol_log`, `sauna_log`
- [ ] All tables have expected columns matching the schema specifications
- [ ] `uv run alembic revision --autogenerate -m "test"` generates migration file
- [ ] Sample service Dockerfile builds successfully: `docker build -f services/ai-data-logger/Dockerfile .`
- [ ] `.env.example` contains all required environment variables
- [ ] Shared models can be imported: `from shared.models.health_logs import HeartLog`