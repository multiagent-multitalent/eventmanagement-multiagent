"""Markdown-basiertes Logging und Output-System für Event-Planung.

Ersetzt JSON-Exports durch strukturierte Markdown-Dokumente.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Optional
import re


class MarkdownWorkstreamLogger:
    """Verwaltet Markdown-basierte Logs und Outputs für Workstreams."""

    def __init__(self, workstreams_dir: Path):
        self.workstreams_dir = workstreams_dir
        self.workstreams_dir.mkdir(exist_ok=True)

    def _create_markdown_header(self, title: str, level: int = 1) -> str:
        """Erstellt Markdown-Header."""
        return "#" * level + f" {title}\n"

    def _create_markdown_table(self, headers: list[str], rows: list[list[str]]) -> str:
        """Erstellt Markdown-Tabelle."""
        md = "| " + " | ".join(headers) + " |\n"
        md += "|" + "|".join(["---"] * len(headers)) + "|\n"
        for row in rows:
            md += "| " + " | ".join(str(cell) for cell in row) + " |\n"
        return md + "\n"

    def create_task_log(self, workstream_name: str, tasks: list[dict[str, Any]]) -> Path:
        """Erstellt ein Task-Logdatei für einen Workstream."""
        workstream_dir = self.workstreams_dir / workstream_name.lower()
        workstream_dir.mkdir(exist_ok=True)
        log_file = workstream_dir / "TASKS.md"

        md_content = self._create_markdown_header(f"Arbeitspakete: {workstream_name}", 1)
        md_content += f"**Aktualisiert:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        # Statistik
        completed = sum(1 for t in tasks if t.get("status") == "completed")
        total = len(tasks)
        pct = int((completed / total) * 100) if total else 0

        md_content += self._create_markdown_header("Status-Übersicht", 2)
        md_content += f"- ✅ **Abgeschlossen:** {completed}/{total} ({pct}%)\n"
        md_content += f"- 📊 **Fortschritt:** {'█' * (pct // 10)}{' ' * (10 - pct // 10)} {pct}%\n\n"

        # Task-Tabelle
        md_content += self._create_markdown_header("Aufgaben", 2)
        headers = ["ID", "Titel", "Status", "Beauftragter", "Fälligkeit", "Notizen"]
        rows = []
        for task in tasks:
            status_icon = {
                "completed": "✅",
                "in_progress": "⏳",
                "pending": "🔲",
                "blocked": "🚫",
                "error": "❌"
            }.get(task.get("status", "pending"), "❓")

            rows.append([
                task.get("id", ""),
                task.get("title", ""),
                f"{status_icon} {task.get('status', '')}",
                task.get("assigned_to", "-"),
                task.get("due_date", "-"),
                task.get("notes", "")[:50]
            ])

        md_content += self._create_markdown_table(headers, rows)
        log_file.write_text(md_content, encoding="utf-8")
        return log_file

    def create_research_log(
        self,
        workstream_name: str,
        research_topic: str,
        sources: list[dict[str, Any]],
        summary: str
    ) -> Path:
        """Erstellt ein Recherche-Log mit Quellen."""
        workstream_dir = self.workstreams_dir / workstream_name.lower()
        workstream_dir.mkdir(exist_ok=True)
        log_file = workstream_dir / f"research-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

        md_content = self._create_markdown_header(f"Recherche: {research_topic}", 1)
        md_content += f"**Datum:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        md_content += self._create_markdown_header("Zusammenfassung", 2)
        md_content += f"{summary}\n\n"

        md_content += self._create_markdown_header("Quellen", 2)
        headers = ["#", "Quelle", "Titel", "Relevanz", "Notizen"]
        rows = []
        for i, source in enumerate(sources, 1):
            rows.append([
                str(i),
                source.get("url", "-")[:50],
                source.get("title", ""),
                source.get("relevance_score", 0),
                source.get("notes", "")[:40]
            ])

        md_content += self._create_markdown_table(headers, rows)
        log_file.write_text(md_content, encoding="utf-8")
        return log_file

    def create_decision_log(
        self,
        workstream_name: str,
        decision: str,
        options: list[str],
        chosen_option: str,
        reasoning: str,
        stakeholders: list[str]
    ) -> Path:
        """Dokumentiert eine Entscheidung."""
        workstream_dir = self.workstreams_dir / workstream_name.lower()
        workstream_dir.mkdir(exist_ok=True)
        log_file = workstream_dir / f"decision-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

        md_content = self._create_markdown_header(f"Entscheidung: {decision}", 1)
        md_content += f"**Datum:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        md_content += f"**Beteiligte:** {', '.join(stakeholders)}\n\n"

        md_content += self._create_markdown_header("Optionen", 2)
        for i, option in enumerate(options, 1):
            marker = "✅ **[GEWÄHLT]**" if option == chosen_option else ""
            md_content += f"{i}. {option} {marker}\n"

        md_content += f"\n{self._create_markdown_header('Begründung', 2)}"
        md_content += f"{reasoning}\n"

        log_file.write_text(md_content, encoding="utf-8")
        return log_file

    def create_action_plan(
        self,
        workstream_name: str,
        title: str,
        actions: list[dict[str, Any]],
        timeline: str
    ) -> Path:
        """Erstellt einen Aktionsplan für einen Workstream."""
        workstream_dir = self.workstreams_dir / workstream_name.lower()
        workstream_dir.mkdir(exist_ok=True)
        log_file = workstream_dir / f"action-plan-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

        md_content = self._create_markdown_header(f"Aktionsplan: {title}", 1)
        md_content += f"**Erstellt:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        md_content += f"**Timeline:** {timeline}\n\n"

        md_content += self._create_markdown_header("Maßnahmen", 2)
        for i, action in enumerate(actions, 1):
            md_content += f"\n### {i}. {action.get('title', '')}\n"
            md_content += f"- **Responsible:** {action.get('owner', 'TBD')}\n"
            md_content += f"- **Start:** {action.get('start_date', 'TBD')}\n"
            md_content += f"- **End:** {action.get('end_date', 'TBD')}\n"
            md_content += f"- **Description:** {action.get('description', '')}\n"
            if action.get('dependencies'):
                md_content += f"- **Dependencies:** {', '.join(action['dependencies'])}\n"

        log_file.write_text(md_content, encoding="utf-8")
        return log_file

    def create_status_report(
        self,
        workstream_name: str,
        status: str,
        completed_items: list[str],
        in_progress_items: list[str],
        blocked_items: list[str],
        next_steps: list[str],
        risks: Optional[list[dict[str, Any]]] = None
    ) -> Path:
        """Erstellt einen Statusbericht."""
        workstream_dir = self.workstreams_dir / workstream_name.lower()
        workstream_dir.mkdir(exist_ok=True)
        log_file = workstream_dir / f"status-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

        status_icon = {"on_track": "🟢", "at_risk": "🟡", "off_track": "🔴"}.get(status, "❓")

        md_content = self._create_markdown_header(f"Status-Report: {workstream_name}", 1)
        md_content += f"**Datum:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        md_content += f"**Status:** {status_icon} {status}\n\n"

        if completed_items:
            md_content += self._create_markdown_header("✅ Abgeschlossen", 2)
            for item in completed_items:
                md_content += f"- {item}\n"
            md_content += "\n"

        if in_progress_items:
            md_content += self._create_markdown_header("⏳ In Bearbeitung", 2)
            for item in in_progress_items:
                md_content += f"- {item}\n"
            md_content += "\n"

        if blocked_items:
            md_content += self._create_markdown_header("🚫 Blockiert", 2)
            for item in blocked_items:
                md_content += f"- {item}\n"
            md_content += "\n"

        if risks:
            md_content += self._create_markdown_header("⚠️ Risiken", 2)
            for risk in risks:
                md_content += f"- **{risk.get('title', '')}** (Likelihood: {risk.get('likelihood', 'unknown')}) - {risk.get('mitigation', '')}\n"
            md_content += "\n"

        if next_steps:
            md_content += self._create_markdown_header("➡️ Nächste Schritte", 2)
            for i, step in enumerate(next_steps, 1):
                md_content += f"{i}. {step}\n"

        log_file.write_text(md_content, encoding="utf-8")
        return log_file


class MarkdownPlanningLog:
    """Master-Log für die gesamte Event-Planung (ersetzt PLANUNGSLOG.json)."""

    def __init__(self, workstreams_dir: Path):
        self.workstreams_dir = workstreams_dir
        self.log_file = workstreams_dir / "PLANUNGSLOG.md"

    def initialize(self, event_name: str, event_config: dict[str, Any]) -> None:
        """Initialisiert das Planungslog."""
        md_content = f"""# Event-Planungslog: {event_name}

**Erstellt:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Version:** 1.0

## 📋 Event-Konfiguration

| Feld | Wert |
|------|------|
| **Name** | {event_config.get('event', {}).get('name', 'TBD')} |
| **Datum** | {event_config.get('event', {}).get('date_start', 'TBD')} – {event_config.get('event', {}).get('date_end', 'TBD')} |
| **Ort** | {event_config.get('event', {}).get('city', 'TBD')}, {event_config.get('event', {}).get('country', 'TBD')} |
| **Teilnehmer erwartet** | {event_config.get('event', {}).get('attendees_expected', 'TBD')} |

## 📊 Workstream-Status

| Workstream | Status | Fortschritt | Verantwortlicher |
|-----------|--------|-------------|-----------------|
| Programm | 🔲 Pending | 0% | TBD |
| Kommunikation | 🔲 Pending | 0% | TBD |
| Teilnehmer | 🔲 Pending | 0% | TBD |
| Venue & Logistik | 🔲 Pending | 0% | TBD |
| Catering | 🔲 Pending | 0% | TBD |
| Technik | 🔲 Pending | 0% | TBD |
| Personal | 🔲 Pending | 0% | TBD |
| Sponsoring | 🔲 Pending | 0% | TBD |
| Unterkunft & Anreise | 🔲 Pending | 0% | TBD |
| Nachbereitung | 🔲 Pending | 0% | TBD |

## 📅 Timeline

```
Initialisierung → Planung → Umsetzung → Durchführung → Nachbereitung
```

## 📝 Entscheidungslog

*Noch keine Entscheidungen dokumentiert*

## ⚠️ Risikobericht

*Noch keine Risiken identifiziert*

---

**Zuletzt aktualisiert:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        self.log_file.write_text(md_content, encoding="utf-8")

    def append_entry(self, workstream: str, action: str, details: str) -> None:
        """Fügt einen neuen Eintrag ins Log ein."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"\n- **[{timestamp}] {workstream}:** {action} — {details}"

        if not self.log_file.exists():
            self.initialize("Unknown Event", {})

        content = self.log_file.read_text(encoding="utf-8")
        # Insert before last "Zuletzt aktualisiert"
        content = content.replace(
            f"\n---\n\n**Zuletzt aktualisiert:**",
            f"{entry}\n\n---\n\n**Zuletzt aktualisiert:**"
        )
        content = content.replace(
            "**Zuletzt aktualisiert:** " + content.split("**Zuletzt aktualisiert:** ")[-1].split("\n")[0],
            f"**Zuletzt aktualisiert:** {timestamp}"
        )
        self.log_file.write_text(content, encoding="utf-8")
