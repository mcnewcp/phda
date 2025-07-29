# CLAUDE.md – Global Project Instructions

Read this file **every time** before you (Claude) plan or modify code in this project. Follow these rules unless explicitly instructed otherwise **and** this file is updated.

---
## 1  Canonical Context

This project is the **Personal Health Data Assistant** (PHDA).

* High‑level roadmap lives in `dev/PLANNING.md` — **always read this file at the start of a new conversation** to understand architecture, goals, style, and constraints.
* Granular work items live in `dev/features/`.
* Product‑requirement prompts live in `dev/PRPs/`.
* The stack is Python‑first, micro‑service oriented, containerised with Docker Compose, and initially single‑user (`user_id = 'mcnewcp'`).

---
## 2  Language & Runtime

* **Python 3.11+** for all production code.
* **uv** manages the single repo‑wide virtual environment; dependency *groups* (`[dependency-groups]` in `pyproject.toml`) keep per‑service footprints minimal. **Use `uv` for all Python commands, including tests.**
* Use type hints (`from __future__ import annotations`) and adhere to **PEP 8** via **ruff** + **black** (88‑char lines).

---
## 3  Service Rules

| Service                    | Key Tech                          | Notes                                                                    |
| -------------------------- | --------------------------------- | ------------------------------------------------------------------------ |
| **ai_data_logger**         | LangGraph ReAct agent (manual)    | Must log Phoenix traces; tools: logging, web‑search, calculator.         |
| **data_workflows**         | Python sched or cron              | Initial ETL: Apple Health via Health Auto Export POST; extensible.       |
| **analytics_workflows**    | pandas + plotly (later sklearn)   | Phase 1: summaries only, ML postponed.                                   |
| **ai_analytics_assistant** | LangGraph + Python REPL tool      | Read‑only DB access; generates charts on demand.                          |
| **ui**                     | Streamlit (Phase 1–3) → React SPA | Use `st.plotly_chart` for interactive visuals.                            |
| **monitoring**             | Arize Phoenix                     | Cloud in Phase 1; self‑host container added Phase 2.                      |

Each service **must** ship:

1. `Dockerfile` based on `python:3.11-slim` (or Alpine‑compatible) installing only its dep group.
2. `entrypoint.sh` (if needed) for start‑up.
3. Unit tests in `<service>/tests/`.

---
## 4  Database Contract

* **PostgreSQL**, containerised locally or managed (Supabase) in cloud.
* All tables include `user_id TEXT NOT NULL DEFAULT 'mcnewcp'`. Primary key = `id SERIAL` unless otherwise specified.
* SQLAlchemy models live in `shared/db/models.py`.
* Schema migrations handled via **Alembic** (generate migration scripts per feature when schema changes).

---
## 5  Environment Configuration

* `.env.example` must list **all** variables a dev needs (`POSTGRES_URL`, `OPENAI_API_KEY`, `ARIZE_API_KEY`, `PHOENIX_COLLECTOR_URL`, etc.).
* Load variables with `python_dotenv.load_dotenv()` at service start.
* Do **not** commit real secrets.

---
## 6  Observability (Phoenix)

* Instrument all agent interactions with Phoenix tracing (see the [LangGraph/LangChain integration guide](https://arize.com/docs/phoenix/integrations/frameworks/langchain/langchain-tracing)).
* Include `trace_id` in service logs for cross‑reference.
* Each agent adds a `monitoring.py` helper so importing the package automatically sets up Phoenix.

---
## 7  Coding Standards & Workflow Rules

1. **File size** – never create a source file longer than **500 lines**; refactor into modules/helpers when necessary.
2. **Testing**
   * Always create **Pytest unit tests** for every new feature (functions, classes, routes, etc.).
   * After updating any logic, update or add tests as needed to keep coverage ≥ 80 %.
3. **Documentation & Comments**
   * Comment any **non‑obvious code** so a mid‑level developer can follow.
   * For complex logic include an inline `# Reason:` comment explaining *why* the approach was taken.
   * Update `README.md` whenever features, dependencies, or setup steps change.
4. **Clarity & Safety**
   * Never assume missing context — ask clarifying questions if uncertain.
   * Never hallucinate libraries or functions; only import known, verified Python packages.
   * Always confirm file paths and module names exist before referencing them in code or tests.
5. **Style & Tooling**
   * Strict Google‑style docstrings on all public methods.
   * Prefer **dataclasses** for simple data holders.
   * Use **async** when IO‑bound; default to sync otherwise.
   * Enforce ruff/black formatting via pre‑commit.

---
## 8  Prompts & Agents

* Never leak internal chain‑of‑thought to end users (unless explicitly in dev mode).
* Build the ReAct logger agent **manually** — do **not** use the `create_react_agent` helper.
* Agent tools:
  * `log_<table>` tools write to Postgres via SQLAlchemy.
  * `web_search` uses the [Bing Web Search API](https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search); it must parse nutritional data.
  * `calculate` wraps `python_eval(expr)` with math‑safe guards.
* Use `shared/utils/dates.py` to resolve relative times against **America/Chicago** timezone.

---
## 9  Docker & Compose

* Root‑level `docker/compose.yaml` defines services + Postgres + (Phase 2) Phoenix.
* Use named volumes for Postgres data.
* Each container installs only its dependency group via `uv pip sync --groups <name>` (optionally pointing to the `.uv` wheel cache to speed builds).
* Build args / env vars inject revision labels for tracing.

---
## 10  CI / Pre‑Commit (future‑proof)

* A future feature file will set up GitHub Actions to run lint, tests, and Docker builds.
* For now, include `.pre-commit-config.yaml` referencing ruff, black, and trailing‑whitespace hooks.

---
## 11  Documentation Etiquette

* Keep `dev/PLANNING.md` succinct; do not bloat with low‑level details.
* Before starting a new feature, Claude must read the associated feature file and create a detailed PRP in `dev/PRPs/` for approval **before** coding.
* Do **not** modify this file or PLANNING.md unless explicitly asked.

---
**In short**: read PLANNING.md first, respect service boundaries, write clean and well‑reasoned Python, keep files under 500 lines, containerise everything, instrument Phoenix, maintain tests & docs, and ask questions when in doubt.

