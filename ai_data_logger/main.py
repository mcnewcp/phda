"""
AI Data Logger - Part of Personal Health Data Assistant

This service handles natural language health data logging via LangGraph ReAct agent.
Currently a placeholder for Phase 1 development.
"""

from __future__ import annotations

import logging

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for AI Data Logger service."""
    logger.info("AI Data Logger starting...")
    # Placeholder implementation
    logger.info("AI Data Logger ready")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
