"""CLI entry point for the Event-Management Orchestrator.

Diese Datei delegiert an src.cli – die neue Terminal-basierte CLI.

Usage:
    python -m src.main
    python -m src.cli

Alle Outputs erfolgen als Markdown in workstreams/
"""

import sys
from src.cli import main as cli_main


if __name__ == "__main__":
    cli_main()

