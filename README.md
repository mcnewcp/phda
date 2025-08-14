# PHDA - Personal Health Data Assistant

A Python-based health tracking application that uses AI to help users log, analyze, and understand their health data through natural language interactions.

## Quick Start

### 1. Environment Setup

```bash
# Clone and navigate to the project
cd phda

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Copy the example environment file and configure your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your actual credentials:
```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
SUPABASE_URL=your_supabase_project_url_here
SUPABASE_KEY=your_supabase_anon_key_here
```

### 3. Database Setup

Run the database setup script to create the required tables:

```bash
python setup_database.py
```

### 4. Run the Application

```bash
streamlit run src/main.py
```

The app will open in your browser at `http://localhost:8501`.

## Project Structure

```
phda/
├── src/                    # Source code
│   ├── __init__.py
│   ├── main.py            # Streamlit app entry point
│   └── config.py          # Configuration management
├── tests/                 # Test files
├── .dev/                  # Development documentation
│   ├── REQUIREMENTS.md
│   └── PLANNING.md
├── requirements.txt       # Python dependencies
├── setup_database.py      # Database setup script
├── .env.example          # Environment variables template
├── .gitignore
├── CLAUDE.md             # Development guidelines
└── README.md
```

## Development Status

### ✅ Phase 1.1 - Foundation Setup (Complete)
- Project structure initialized
- Core dependencies installed (LangGraph, LangChain, Streamlit, Supabase)
- Environment configuration set up
- Database schema defined
- Basic Streamlit app created

### 🔄 Phase 1.2 - Agent Development (Next)
- Body composition logging tool with Supabase MCP
- LangGraph agent using `create_react_agent`
- Natural language parsing for datetime references
- Data validation and error handling

### ⏳ Phase 1.3 - Streamlit Integration (Planned)
- Chat interface in Streamlit
- Session state management
- Agent-frontend connection

### ⏳ Phase 1.4 - Deployment (Planned)
- Streamlit Cloud deployment
- End-to-end testing

## Technology Stack

- **Python 3.11+**: Primary development language
- **LangGraph**: Agent orchestration
- **LangChain + Anthropic**: LLM integration
- **Streamlit**: Web interface
- **Supabase**: PostgreSQL database
- **pytest**: Testing framework

## Data Schema

The `body_composition` table stores health measurements:
- `datetime`: Timestamp of measurement
- `weight`: Weight in pounds (decimal)
- `smm`: Skeletal muscle mass in pounds (decimal)  
- `pbf`: Percent body fat (whole percentage)
- `ecw_tbw`: ECW/TBW ratio (decimal form)

## Contributing

See `CLAUDE.md` for development guidelines and coding standards.

## License

This project is for educational and personal use.