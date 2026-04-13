"""Documentation and logging module for agent execution tracking.

This module provides functions to document every agent execution step
and maintain an execution log in Markdown format.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


class ExecutionLogger:
    """Logger for agent execution steps and workflow progress."""

    def __init__(self, repo_root: Path):
        """Initialize the execution logger.
        
        Args:
            repo_root: The repository root directory path
        """
        self.repo_root = repo_root
        self.log_file = repo_root / "workstreams" / "PLANUNGSLOG.md"
        self.json_log_file = repo_root / "workstreams" / "PLANUNGSLOG.json"
        self.execution_entries = []
        self._ensure_log_files()

    def _ensure_log_files(self) -> None:
        """Ensure log files and directories exist."""
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        
        if not self.log_file.exists():
            self._write_markdown_header()
        
        if not self.json_log_file.exists():
            self.json_log_file.write_text(json.dumps([], indent=2), encoding="utf-8")

    def _write_markdown_header(self) -> None:
        """Write header to markdown log file."""
        header = """# 📋 Planungslog – Agenten-Ausführungen

Dieses Dokument dokumentiert jeden Schritt und jede Ausführung der Agenten
im Event-Management-Orchestrator.

---

"""
        self.log_file.write_text(header, encoding="utf-8")

    def log_agent_step(
        self,
        agent_name: str,
        step_name: str,
        status: str = "completed",
        input_data: Optional[dict[str, Any]] = None,
        output_data: Optional[dict[str, Any]] = None,
        error_message: Optional[str] = None,
        duration_seconds: Optional[float] = None,
    ) -> None:
        """Log a single agent execution step.
        
        Args:
            agent_name: Name of the agent (e.g., "research_agent", "planning_agent")
            step_name: Human-readable name of the step (e.g., "Venue Research")
            status: Step status - "pending", "running", "completed", "error"
            input_data: Input data to the agent step
            output_data: Output data from the agent step
            error_message: Error message if status is "error"
            duration_seconds: Duration of the step in seconds
        """
        timestamp = datetime.now().isoformat()
        
        entry = {
            "timestamp": timestamp,
            "agent": agent_name,
            "step": step_name,
            "status": status,
            "input_summary": self._summarize_data(input_data),
            "output_summary": self._summarize_data(output_data),
            "error": error_message,
            "duration_seconds": duration_seconds,
        }
        
        self.execution_entries.append(entry)
        
        # Append to both markdown and JSON logs
        self._append_to_markdown(entry)
        self._append_to_json(entry)
        
        logger.info(
            f"✓ Logged agent step: {agent_name} → {step_name} ({status})"
        )

    def log_workflow_stage(
        self,
        stage: int,
        stage_name: str,
        status: str = "started",
        description: Optional[str] = None,
    ) -> None:
        """Log workflow stage transitions.
        
        Args:
            stage: Stage number (1, 2, 3, etc.)
            stage_name: Human-readable stage name
            status: Stage status - "started", "completed", "paused", "aborted"
            description: Optional description of the stage
        """
        timestamp = datetime.now().isoformat()
        
        entry = {
            "timestamp": timestamp,
            "type": "workflow_stage",
            "stage": stage,
            "stage_name": stage_name,
            "status": status,
            "description": description,
        }
        
        self.execution_entries.append(entry)
        self._append_to_markdown_stage(entry)
        self._append_to_json(entry)
        
        logger.info(f"→ Logged workflow stage: {stage_name} ({status})")

    def log_user_decision(
        self,
        decision_data: dict[str, Any],
        notes: Optional[str] = None,
    ) -> None:
        """Log user decisions and approvals.
        
        Args:
            decision_data: The decision data (selected venue, catering, etc.)
            notes: Optional notes from the user
        """
        timestamp = datetime.now().isoformat()
        
        entry = {
            "timestamp": timestamp,
            "type": "user_decision",
            "decision": decision_data,
            "notes": notes,
        }
        
        self.execution_entries.append(entry)
        self._append_to_markdown_decision(entry)
        self._append_to_json(entry)
        
        logger.info("👤 Logged user decision")

    def _summarize_data(self, data: Optional[dict[str, Any]]) -> str:
        """Create a concise summary of data for logging.
        
        Args:
            data: The data to summarize
            
        Returns:
            A summary string (max 500 chars)
        """
        if not data:
            return "None"
        
        summary = json.dumps(data, default=str, ensure_ascii=False)
        if len(summary) > 500:
            summary = summary[:497] + "..."
        return summary

    def _append_to_markdown(self, entry: dict[str, Any]) -> None:
        """Append an agent step entry to markdown log.
        
        Args:
            entry: The log entry to append
        """
        timestamp = entry.get("timestamp", "")
        agent = entry.get("agent", "unknown")
        step = entry.get("step", "")
        status = entry.get("status", "unknown")
        duration = entry.get("duration_seconds")
        error = entry.get("error")
        input_summary = entry.get("input_summary", "None")
        output_summary = entry.get("output_summary", "None")
        
        # Status emoji
        status_emoji = {
            "pending": "⏳",
            "running": "🔄",
            "completed": "✅",
            "error": "❌",
        }.get(status, "•")
        
        lines = [
            f"\n## {status_emoji} {agent.replace('_', ' ').title()} – {step}",
            f"\n**Timestamp:** {timestamp}",
            f"\n**Status:** {status}",
        ]
        
        if duration:
            lines.append(f"\n**Dauer:** {duration:.2f}s")
        
        if input_summary != "None":
            lines.append(f"\n**Input:**\n```json\n{input_summary}\n```")
        
        if output_summary != "None":
            lines.append(f"\n**Output:**\n```json\n{output_summary}\n```")
        
        if error:
            lines.append(f"\n**Fehler:** {error}")
        
        lines.append("\n")
        
        # Append to file
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write("".join(lines))

    def _append_to_markdown_stage(self, entry: dict[str, Any]) -> None:
        """Append a workflow stage entry to markdown log.
        
        Args:
            entry: The stage entry to append
        """
        timestamp = entry.get("timestamp", "")
        stage = entry.get("stage", "")
        stage_name = entry.get("stage_name", "")
        status = entry.get("status", "")
        description = entry.get("description", "")
        
        status_emoji = {
            "started": "▶️",
            "completed": "🎯",
            "paused": "⏸️",
            "aborted": "❌",
        }.get(status, "•")
        
        lines = [
            f"\n# {status_emoji} Stage {stage}: {stage_name}",
            f"\n**Timestamp:** {timestamp}",
            f"\n**Status:** {status}",
        ]
        
        if description:
            lines.append(f"\n**Beschreibung:** {description}")
        
        lines.append("\n")
        lines.append("---")
        lines.append("\n")
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write("".join(lines))

    def _append_to_markdown_decision(self, entry: dict[str, Any]) -> None:
        """Append a user decision entry to markdown log.
        
        Args:
            entry: The decision entry to append
        """
        timestamp = entry.get("timestamp", "")
        decision = entry.get("decision", {})
        notes = entry.get("notes", "")
        
        lines = [
            f"\n### 👤 Benutzerentscheidung",
            f"\n**Timestamp:** {timestamp}",
            f"\n**Entscheidung:**",
        ]
        
        for key, value in decision.items():
            key_display = key.replace("_", " ").title()
            lines.append(f"\n- **{key_display}:** {value}")
        
        if notes:
            lines.append(f"\n**Anmerkungen:** {notes}")
        
        lines.append("\n")
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write("".join(lines))

    def _append_to_json(self, entry: dict[str, Any]) -> None:
        """Append an entry to JSON log.
        
        Args:
            entry: The log entry to append
        """
        try:
            existing = json.loads(self.json_log_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, FileNotFoundError):
            existing = []
        
        existing.append(entry)
        self.json_log_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")

    def get_execution_summary(self) -> dict[str, Any]:
        """Get a summary of all executions.
        
        Returns:
            A dictionary with execution statistics
        """
        agent_steps = [e for e in self.execution_entries if "agent" in e]
        stages = [e for e in self.execution_entries if e.get("type") == "workflow_stage"]
        decisions = [e for e in self.execution_entries if e.get("type") == "user_decision"]
        
        return {
            "total_entries": len(self.execution_entries),
            "agent_steps": len(agent_steps),
            "workflow_stages": len(stages),
            "user_decisions": len(decisions),
            "agents_used": list(set(e.get("agent") for e in agent_steps if e.get("agent"))),
            "last_update": datetime.now().isoformat(),
        }
