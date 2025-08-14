"""Configuration management for PHDA application."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration settings."""
    
    # Anthropic API settings
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    
    # Supabase settings
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    # LangSmith settings (optional)
    LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "phda")
    
    @classmethod
    def validate(cls) -> bool:
        """Validate required configuration values are present."""
        required_vars = [
            ("ANTHROPIC_API_KEY", cls.ANTHROPIC_API_KEY),
            ("SUPABASE_URL", cls.SUPABASE_URL),
            ("SUPABASE_KEY", cls.SUPABASE_KEY),
        ]
        
        missing_vars = [name for name, value in required_vars if not value]
        
        if missing_vars:
            print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
            print("Please check your .env file and ensure all required variables are set.")
            return False
        
        return True