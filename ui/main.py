"""
UI - Part of Personal Health Data Assistant

This service handles the Streamlit web interface for the application.
Currently a placeholder for Phase 1 development.
"""

from __future__ import annotations

import logging

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for UI service."""
    logger.info("UI service starting...")
    # Placeholder implementation
    logger.info("UI service ready")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
