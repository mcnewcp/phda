"""
Date and time utilities for Personal Health Data Assistant.

Handles timezone-aware date operations for America/Chicago timezone.
"""

from __future__ import annotations

from datetime import datetime

import pytz

from .config import get_timezone


def get_current_datetime() -> datetime:
    """Get current datetime in the configured timezone."""
    tz = pytz.timezone(get_timezone())
    return datetime.now(tz)


def parse_relative_time(time_str: str) -> datetime:
    """
    Parse relative time strings against America/Chicago timezone.

    Placeholder for Phase 1 development.
    TODO: Implement relative time parsing for natural language inputs.
    """
    # Placeholder implementation
    return get_current_datetime()
