"""Configuration loader for event data and LLM settings."""

import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

load_dotenv()

_EXTERNAL_LLM_PROJECT_PATH = Path(
    os.getenv(
        "EXTERNAL_LLM_PROJECT_PATH",
        r"C:\Users\garry\Documents\01Hochschule Ansbach\KDT\kdt2\Projekt\Code",
    )
)
_EXTERNAL_DOTENV_PATH = _EXTERNAL_LLM_PROJECT_PATH / ".env"
if _EXTERNAL_DOTENV_PATH.exists():
    # Keep explicitly set environment variables and only fill missing values.
    load_dotenv(dotenv_path=_EXTERNAL_DOTENV_PATH, override=False)

_REPO_ROOT = Path(__file__).parent.parent


def normalize_llm_provider(provider: str | None) -> str:
    """Normalize provider aliases to internal provider names."""
    raw = (provider or "").strip().lower().replace("-", "_")
    aliases = {
        "": "ollama",
        "openaicompatible": "openai_compatible",
        "openai_compatible": "openai_compatible",
        "lmstudio": "lmstudio",
        "localai": "localai",
        "ollama": "ollama",
        "openai": "openai",
    }
    return aliases.get(raw, raw)


def default_llm_base_url(provider: str) -> str:
    """Return provider-specific default base URL."""
    defaults = {
        "ollama": "http://localhost:11434",
        "lmstudio": "http://127.0.0.1:1234/v1",
        "localai": "http://localhost:8080/v1",
        "openai_compatible": "http://localhost:8080/v1",
        "openai": "https://api.openai.com/v1",
    }
    return defaults.get(provider, "http://localhost:11434")


def _resolve_llm_env(key: str, fallback_key: str, default: str) -> str:
    """Resolve LLM values with fallback to LOCAL_LLM_* compatibility keys."""
    return os.getenv(key) or os.getenv(fallback_key) or default


def _normalize_base_url_for_provider(provider: str, base_url: str) -> str:
    """Ensure OpenAI-compatible providers use a /v1 base URL."""
    cleaned = (base_url or "").rstrip("/")
    if provider in {"openai", "openai_compatible", "lmstudio", "localai"} and not cleaned.endswith("/v1"):
        return f"{cleaned}/v1"
    return cleaned


def load_event_config(path: str | None = None) -> dict[str, Any]:
    """Load event configuration from YAML file."""
    config_path = Path(path) if path else _REPO_ROOT / "config" / "event.yaml"
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_llm_config() -> dict[str, Any]:
    """Return LLM configuration from environment variables."""
    provider = normalize_llm_provider(_resolve_llm_env("LLM_PROVIDER", "LOCAL_LLM_PROVIDER", "ollama"))
    default_base_url = default_llm_base_url(provider)
    resolved_base_url = _resolve_llm_env("LLM_BASE_URL", "LOCAL_LLM_BASE_URL", default_base_url)
    normalized_base_url = _normalize_base_url_for_provider(provider, resolved_base_url)
    return {
        "provider": provider,
        "model": _resolve_llm_env("LLM_MODEL", "LOCAL_LLM_MODEL", "llama3.2"),
        "base_url": normalized_base_url,
        "api_key": _resolve_llm_env("LLM_API_KEY", "OPENAI_API_KEY", "local"),
        "temperature": float(_resolve_llm_env("LLM_TEMPERATURE", "LOCAL_LLM_TEMPERATURE", "0.1")),
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
