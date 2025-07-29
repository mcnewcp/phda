"""
pytest configuration for Personal Health Data Assistant.

Provides shared fixtures and test configuration.
"""

from __future__ import annotations

import logging

import pytest
from dotenv import load_dotenv

# Import fixtures from modules
from tests.fixtures.database import *  # noqa: F401,F403

# Load test environment variables
load_dotenv()

# Configure logging for tests
logging.basicConfig(level=logging.INFO)


@pytest.fixture(autouse=True)
def setup_test_environment() -> None:
    """Set up test environment for all tests."""
    # Placeholder for test environment setup
    pass


@pytest.fixture
def sample_health_data() -> dict:
    """Sample health data for testing."""
    return {
        "user_id": "test_user",
        "event_type": "exercise",
        "description": "30 minute run",
        "timestamp": "2024-01-01T12:00:00Z",
    }
