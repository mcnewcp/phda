"""Main Streamlit application for PHDA."""

import streamlit as st
from config import Config

def main():
    """Main application entry point."""
    
    # Configure Streamlit page
    st.set_page_config(
        page_title="PHDA - Personal Health Data Assistant",
        page_icon="🏥",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Validate configuration
    if not Config.validate():
        st.error("❌ Configuration Error")
        st.write("Please ensure all required environment variables are set in your .env file:")
        st.code("""
ANTHROPIC_API_KEY=your_anthropic_api_key_here
SUPABASE_URL=your_supabase_project_url_here
SUPABASE_KEY=your_supabase_anon_key_here
        """)
        st.stop()
    
    # Main UI
    st.title("🏥 Personal Health Data Assistant")
    st.write("Welcome to PHDA! This app helps you log and track your health data using natural language.")
    
    # Placeholder for chat interface (Phase 1.3)
    st.info("💡 **Phase 1.1 Complete!** The foundation is set up. Chat interface coming in Phase 1.2.")
    
    # Show current configuration status
    with st.expander("🔧 Configuration Status"):
        st.success("✅ Anthropic API configured")
        st.success("✅ Supabase connection configured")
        
        if Config.LANGCHAIN_TRACING_V2:
            st.success("✅ LangSmith tracing enabled")
        else:
            st.info("ℹ️ LangSmith tracing disabled (optional)")
    
    # Development info
    with st.expander("🚧 Development Status"):
        st.write("**Completed:**")
        st.write("- ✅ Project structure setup")
        st.write("- ✅ Dependencies installed")
        st.write("- ✅ Environment configuration")
        st.write("- ✅ Database schema ready")
        st.write("- ✅ Basic Streamlit app")
        
        st.write("**Next Steps (Phase 1.2):**")
        st.write("- 🔄 Implement body composition logging agent")
        st.write("- 🔄 Add natural language parsing")
        st.write("- 🔄 Connect to Supabase database")

if __name__ == "__main__":
    main()