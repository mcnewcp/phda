# PHDA Project Requirements

## Project Overview
Personal Health Data Assistant (PHDA) is a Python-based health tracking application that uses AI to help users log, analyze, and understand their health data through natural language interactions.

## Technical Stack

### Core Technologies
- **Python 3.11+**: Primary development language
- **LangGraph**: Agent orchestration using `create_react_agent`
- **Streamlit**: Web interface
- **Anthropic API**: LLM provider (Claude models)
- **Supabase**: PostgreSQL database with MCP integration
- **Arize Phoenix**: Agent monitoring

### Deployment
- **Phase 1**: Streamlit Cloud
- **Future**: Docker, cloud platforms (AWS/GCP/Azure)

## Data Schema

### Body Composition Table
Required fields:
- `datetime` (timestamp): Date and time of measurement
- `weight` (float): Weight in pounds
- `smm` (float): Skeletal muscle mass in pounds
- `pbf` (float): Percent body fat (whole percentage)
- `ecw_tbw` (float): ECW/TBW ratio (decimal form)

## Functional Requirements

### Phase 1: Body Composition Logging
- Natural language input parsing
- Temporal reference handling ("yesterday", "this morning")
- Data validation for reasonable ranges
- Single-user access (no authentication)
- Streamlit chat interface

### Future Phases (Planned)
- Multi-user authentication via Supabase OAuth2
- Apple Health data import
- Nutrition and activity logging
- Analytics and predictive modeling
- On-demand health insights via AI analyst

## Performance Requirements
- Agent response initiation: < 2 seconds
- Data write operations: < 1 second
- Streamlit Cloud resource limit: 1GB RAM

## Security & Privacy
- **Phase 1**: Development only, no production health data
- **Future**: HIPAA compliance considerations, encryption, audit logging