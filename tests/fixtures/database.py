"""
Database test fixtures for Personal Health Data Assistant.

Placeholder for Phase 1 development.
TODO: Add PostgreSQL test database fixtures and setup utilities.
"""

from __future__ import annotations

import pytest

from shared.utils.config import get_database_url


@pytest.fixture
def db_url() -> str:
    """Get database URL for testing."""
    return get_database_url()


@pytest.fixture
def test_user_id() -> str:
    """Get test user ID."""
    return "test_user"


# TODO: Add database fixture for creating test database
# TODO: Add fixture for database session/connection
# TODO: Add fixtures for sample test data
