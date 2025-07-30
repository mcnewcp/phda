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
RUN uv sync --frozen --no-group dev --group ai-analytics-assistant

# Copy application code
COPY shared/ ./shared/
COPY services/analytics-workflows/ ./services/ai-analytics-assistant/

# Set Python path
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app/services/ai-analytics-assistant

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]