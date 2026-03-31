"""Configuration loader for event data and LLM settings."""

import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

load_dotenv()

_REPO_ROOT = Path(__file__).parent.parent


def load_event_config(path: str | None = None) -> dict[str, Any]:
    """Load event configuration from YAML file."""
    config_path = Path(path) if path else _REPO_ROOT / "config" / "event.yaml"
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_llm_config() -> dict[str, Any]:
    """Return LLM configuration from environment variables."""
    return {
        "provider": os.getenv("LLM_PROVIDER", "ollama"),
        "model": os.getenv("LLM_MODEL", "llama3.2"),
        "base_url": os.getenv("LLM_BASE_URL", "http://localhost:11434"),
        "api_key": os.getenv("LLM_API_KEY", "local"),
        "temperature": float(os.getenv("LLM_TEMPERATURE", "0.1")),
    }


def get_dashboard_config() -> dict[str, Any]:
    """Return dashboard configuration from environment variables."""
    return {
        "port": int(os.getenv("DASHBOARD_PORT", "8501")),
        "checkpoint_db": os.getenv(
            "CHECKPOINT_DB", "checkpoints/event_planning.sqlite"
        ),
    }


def get_repo_root() -> Path:
    """Return the repository root path."""
    return _REPO_ROOT
