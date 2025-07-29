# Personal Health Data Assistant – PLANNING.md

> **Purpose**  This file gives Claude (and human developers) a concise, phase‑level roadmap for the project.  It is **always** safe for Claude to read in full as part of its context when writing code.  Detailed feature requirements live in separate `dev/features/*` files.

---

## 1  Project Scope

A Python‑first, containerised micro‑services stack that lets a single user:

1. Log health events in natural language via an **AI Data Logger** agent.
2. Ingest daily Apple Health exports and other sources via **Data Logging Workflows**.
3. View interactive dashboards of near‑real‑time stats & trends.
4. Ask free‑form questions to an **AI Analytics Assistant**.
5. (Later) Receive model‑based predictions & personalised insights.

---

## 2  Repository Layout (monorepo)

```
/ (repo root)
  ├─ .gitignore               # master ignore list for all services
  ├─ .env.example             # consolidated env‑var template for the whole stack
  ├─ ai_data_logger/          # service 1 – LangGraph agent & tools
  ├─ data_workflows/          # service 2 – scheduled ETL jobs
  ├─ analytics_workflows/     # service 3 – stats + ML jobs (later)
  ├─ ai_analytics_assistant/  # service 4 – LangGraph analyst agent (later)
  ├─ ui/                      # service 5 – Streamlit app (later React)
  ├─ shared/                  # common utils, DB models, config helpers
  ├─ docker/                  # Dockerfiles & compose.yaml
  ├─ tests/                   # integration tests; each service holds its own unit tests
  └─ dev/
       ├─ PLANNING.md         # <‑‑ this file
       ├─ PRPs/               # Product Requirement Prompts reside here
       ├─ features/           # each numbered feature spec lives here
       └─ ...
```

*One ****uv**** environment at repo root; dependency groups in ****\`\`**** keep per‑service installs slim.*

---

## 3  Phase Road‑map

| Phase                                   | Goal                                        | Key Deliverables                                                                                                                           |
| --------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **1 – Logging MVP**                     | End‑to‑end manual logging                   | *Manual* LangGraph ReAct agent (GPT‑4o), Postgres container (with `user_id='mcnewcp'`), minimal Streamlit chat page, Phoenix cloud tracing |
| **2 – Local ETL & Self‑Hosted Phoenix** | Automated data import & local observability | Health Auto Export endpoint & parser, scheduled ETL container, Phoenix docker service added, dashboard skeleton                            |
| **3 – Descriptive Analytics**           | Daily/weekly summaries                      | Analytics Workflows container computes aggregates; dashboard plots with Plotly                                                             |
| **4 – AI Analytics Assistant (v1)**     | On‑demand Q&A                               | Analyst LangGraph agent w/ read‑only DB + Python REPL tool; second Streamlit chat page                                                     |
| **5 – Personalised ML Models**          | Predictive insights                         | Feature engineering, regression training, model artefact tables, insights surfaced in dashboard & Q&A                                      |
| **6 – Web UI Refactor**                 | Production‑ready interface                  | REST API gateways, React SPA, auth stub, optional triage‑agent optimisation                                                                |

> **Iteration Policy**  Each phase should ship *fully runnable* compose stack + docs; later phases may refactor earlier code but must maintain previous functionality unless explicitly deprecated.

---

## 4  Testing Strategy

- **Unit tests** live **inside each service** directory – e.g. `ai_data_logger/tests/`.
- **Integration tests** live in root `tests/` and spin up selected containers via docker‑compose (or mocks) to verify inter‑service flows.
- Use **pytest** + **pytest‑asyncio**. Aim ≥80 % coverage on service code before promoting a feature to “complete”.

---

## 5  Environment & Deployment Targets

- **Local dev:** `docker compose up` brings Postgres, services, self‑hosted Phoenix, and UI (Streamlit) online.
- **Cloud lift‑and‑shift:** stack runs unchanged on any Compose‑aware host (e.g. Railway, Fly.io), or can be promoted to ECS/Fargate.  Postgres should migrate to a managed instance (Supabase Free Tier initially).
- **Secrets:** all API keys & DB creds come from `.env`; provide `.env.example` and load via `python‑dotenv`.

---

## 6  Decision Log Snapshot

- DB = **PostgreSQL** (container, `user_id` column from day 1).
- Agent orchestration = **LangGraph** built by hand (*not* `create_react_agent`).
- Observability = **Arize Phoenix** (cloud ➜ self‑host container in Phase 2).
- Visualisation = **Plotly** via Streamlit `st.plotly_chart`.
- Virtual env = **uv** w/ per‑service dependency groups.
- Monorepo chosen for developer velocity; may split later if team grows.

---

