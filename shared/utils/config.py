"""
Configuration utilities for Personal Health Data Assistant.

Handles environment variable loading and configuration management.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_database_url() -> str:
    """Get the PostgreSQL database URL from environment variables."""
    return os.getenv(
        "POSTGRES_URL", "postgresql://phda_user:your_secure_password_here@localhost:5432/phda_db"
    )


def get_user_id() -> str:
    """Get the primary user ID for single-user setup."""
    return os.getenv("USER_ID", "mcnewcp")


def get_timezone() -> str:
    """Get the configured timezone."""
    return os.getenv("TIMEZONE", "America/Chicago")
