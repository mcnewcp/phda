# Placeholder Dockerfile for Phoenix monitoring service
# This will be replaced with actual Arize Phoenix container configuration
# when we implement monitoring in a future feature

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
RUN uv sync --frozen --no-group dev --group phoenix-monitor

# Copy application code
COPY shared/ ./shared/
COPY services/phoenix-monitor/ ./services/phoenix-monitor/

# Set Python path
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app/services/phoenix-monitor

EXPOSE 8000

# Placeholder command - will be replaced with actual Phoenix startup
CMD ["python", "-c", "print('Phoenix monitor placeholder'); import time; time.sleep(3600)"]