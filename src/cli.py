"""Terminal-basierte CLI für den Event-Management Orchestrator.

Verwendet Rich für benutzerfreundliche Terminal-UI und Markdown für Logging.

Usage:
    python -m src.cli
"""

import argparse
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.markdown import Markdown

from src.config import load_event_config, get_repo_root, get_llm_config, normalize_llm_provider
from src.workflows.event_planning_graph import create_event_planning_graph, create_thread

# Rich Console für formatierte Ausgabe
console = Console()
logger = logging.getLogger(__name__)


class MarkdownLogger:
    """Schreibt Logs und State in Markdown-Dateien statt JSON."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.workstreams_dir = repo_root / "workstreams"
        self.workstreams_dir.mkdir(exist_ok=True)
        self.timestamp = datetime.now().isoformat()

    def log_planning_progress(self, state: dict[str, Any]) -> None:
        """Speichert aktuellen Planungsstatus in PLANUNGSLOG.md."""
        log_file = self.workstreams_dir / "PLANUNGSLOG.md"

        task_packages = state.get("task_packages", [])
        completed = sum(1 for pkg in task_packages if pkg.get("status") == "completed")
        total = len(task_packages)
        progress_pct = int((completed / total) * 100) if total else 0

        # Markdown-Format
        md_content = f"""# Planungslog

**Aktualisiert:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Status-Zusammenfassung

- **Arbeitspakete:** {completed}/{total} abgeschlossen ({progress_pct}%)
- **Status:** {state.get('status', 'unknown')}
- **Phase:** {state.get('stage', 'unknown')}

## Arbeitspakete

| ID | Agent | Aufgabe | Status | Ausgabe |
|----|-------|---------|--------|---------|
"""
        for pkg in task_packages:
            status_icon = "✅" if pkg.get("status") == "completed" else (
                "⏳" if pkg.get("status") == "running" else (
                    "❌" if pkg.get("status") == "error" else "🔲"
                )
            )
            md_content += f"| {pkg.get('id', '')} | {pkg.get('agent', '')} | {pkg.get('task', '')} | {status_icon} {pkg.get('status', '')} | {pkg.get('output', '')[:50]}... |\n"

        # Web-Search Status
        diagnostics = state.get("diagnostics", {}) or {}
        web = diagnostics.get("web_search", {}) or {}
        if web:
            md_content += f"\n## 🔎 Online-Recherche\n\n- **Anfragen:** {web.get('query_count', 0)}\n- **Quellen:** {web.get('source_count', 0)}\n"

        # Agent Journal
        journal = state.get("agent_journal", [])
        if journal:
            md_content += "\n## 📔 Agent-Dokumentation\n\n"
            for entry in journal[-5:]:
                md_content += f"- **{entry.get('agent', 'Unknown')}:** {entry.get('note', '')}\n"

        log_file.write_text(md_content, encoding="utf-8")
        console.print(f"✓ Planungslog gespeichert: [cyan]{log_file.relative_to(self.repo_root)}[/cyan]")

    def log_workstream_output(self, workstream_name: str, output: dict[str, Any]) -> None:
        """Speichert Workstream-Ausgaben als Markdown."""
        workstream_dir = self.workstreams_dir / workstream_name.lower()
        workstream_dir.mkdir(exist_ok=True)

        output_file = workstream_dir / f"output-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

        md_content = f"""# Workstream: {workstream_name}

**Erstellt:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Zusammenfassung

{output.get('summary', 'Keine Zusammenfassung verfügbar')}

## Details

{output.get('details', 'Keine Details verfügbar')}

## Nächste Schritte

{output.get('next_steps', 'Siehe Planungslog für nächste Schritte')}
"""

        output_file.write_text(md_content, encoding="utf-8")
        console.print(f"✓ Workstream-Ausgabe gespeichert: [cyan]{output_file.relative_to(self.repo_root)}[/cyan]")


def _parse_args() -> argparse.Namespace:
    """Parst Command-Line-Argumente."""
    parser = argparse.ArgumentParser(
        description="🎪 Event-Management Orchestrator – Terminal-CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Automatischer Modus: wählt erste Option und startet ohne Rückfragen",
    )
    parser.add_argument(
        "--venue",
        type=str,
        default="",
        help="Venue-Name für automatische Auswahl",
    )
    parser.add_argument(
        "--catering",
        type=str,
        default="",
        help="Catering-Name für automatische Auswahl",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="",
        help="LLM-Provider (ollama, lmstudio, localai, openai)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="",
        help="LLM-Modellname",
    )
    parser.add_argument(
        "--base-url",
        type=str,
        default="",
        help="LLM-Base-URL",
    )
    return parser.parse_args()


def _print_header() -> None:
    """Zeigt Willkommensnachricht an."""
    header = """
╔════════════════════════════════════════════════════════════╗
║                   🎪  EVENT-MANAGEMENT                     ║
║              Orchestrator – Universal CLI                  ║
║                 Vollautomatische Planung                   ║
╚════════════════════════════════════════════════════════════╝
"""
    console.print(header, style="bold cyan")


def _print_event_info(event_config: dict[str, Any]) -> None:
    """Zeigt Event-Informationen in einer Tabelle an."""
    event = event_config.get("event", {})

    info_panel = Panel(
        f"""[bold]Event:[/bold] {event.get('name', 'Unbekannt')}
[bold]Datum:[/bold] {event.get('date_start', 'TBD')} – {event.get('date_end', 'TBD')}
[bold]Ort:[/bold] {event.get('city', 'TBD')}, {event.get('country', 'TBD')}
[bold]Teilnehmer:[/bold] {event.get('attendees_expected', 'TBD')}""",
        title="[cyan]📋 Event-Konfiguration[/cyan]",
        border_style="cyan",
    )
    console.print(info_panel)


def _print_llm_config(llm_config: dict[str, Any]) -> None:
    """Zeigt LLM-Konfiguration an."""
    provider = normalize_llm_provider(str(llm_config.get("provider", "ollama")))
    model = llm_config.get("model", "llama3.2")
    base_url = llm_config.get("base_url", "http://localhost:11434")

    llm_panel = Panel(
        f"""[bold]Provider:[/bold] {provider}
[bold]Modell:[/bold] {model}
[bold]Base-URL:[/bold] {base_url}""",
        title="[yellow]🤖 LLM-Konfiguration[/yellow]",
        border_style="yellow",
    )
    console.print(llm_panel)


def _print_venue_options(venue_options: list[dict]) -> None:
    """Zeigt Venue-Optionen in einer Tabelle."""
    if not venue_options:
        console.print("[yellow]Keine Venue-Optionen verfügbar[/yellow]")
        return

    table = Table(title="[cyan]🏢 Venue-Optionen[/cyan]", show_header=True, header_style="bold cyan")
    table.add_column("#", style="dim")
    table.add_column("Name", style="magenta")
    table.add_column("Kosten", style="yellow")
    table.add_column("Bewertung", style="green")
    table.add_column("Beschreibung", style="white")

    for i, opt in enumerate(venue_options, 1):
        stars = "⭐" * int(opt.get("recommendation_score", 0))
        table.add_row(
            str(i),
            opt.get("name", ""),
            opt.get("estimated_cost", "TBD"),
            stars or "N/A",
            opt.get("description", "")[:40],
        )

    console.print(table)


def _print_progress(task_packages: list[dict]) -> None:
    """Zeigt Fortschritt der Arbeitspakete."""
    if not task_packages:
        return

    completed = sum(1 for pkg in task_packages if pkg.get("status") == "completed")
    total = len(task_packages)
    progress_pct = int((completed / total) * 100) if total else 0

    table = Table(title="[cyan]📊 Fortschritt[/cyan]", show_header=True, header_style="bold cyan")
    table.add_column("Metrik", style="dim")
    table.add_column("Wert", style="yellow")

    table.add_row("Arbeitspakete", f"{completed}/{total}")
    table.add_row("Fortschritt", f"{progress_pct}%")
    table.add_row("Status", "🟢 Aktiv" if progress_pct < 100 else "✅ Abgeschlossen")

    console.print(table)


def _select_option(options: list[dict], label: str) -> str:
    """Interaktive Auswahl einer Option."""
    if not options:
        return ""

    _print_venue_options(options) if "recommendation_score" in options[0] else None

    while True:
        try:
            raw = input(f"\n{label} (1-{len(options)}, oder Enter für 1): ").strip()
            if raw == "":
                return options[0].get("name", "Option 1")
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return options[idx].get("name", f"Option {idx+1}")
            console.print(f"[red]Fehler: Bitte eine Zahl zwischen 1 und {len(options)} eingeben[/red]")
        except ValueError:
            console.print(f"[red]Fehler: Ungültige Eingabe[/red]")
        except EOFError:
            console.print("[yellow]Automatischer Modus: Option 1 gewählt[/yellow]")
            return options[0].get("name", "Option 1")
        except KeyboardInterrupt:
            console.print("\n[red]Abgebrochen[/red]")
            sys.exit(0)


def main() -> None:
    """Haupteinstieg der Terminal-CLI."""
    args = _parse_args()

    # LLM-Konfiguration aus Args
    if args.provider:
        os.environ["LLM_PROVIDER"] = args.provider
    if args.model:
        os.environ["LLM_MODEL"] = args.model
    if args.base_url:
        os.environ["LLM_BASE_URL"] = args.base_url

    _print_header()

    # Repository und Config laden
    repo_root = get_repo_root()
    event_config = load_event_config()
    llm_config = get_llm_config()
    markdown_logger = MarkdownLogger(repo_root)

    _print_event_info(event_config)
    _print_llm_config(llm_config)

    # Workflow erstellen
    console.print("\n[cyan]📦 Initialisiere Workflow...[/cyan]")
    workflow = create_event_planning_graph()
    thread_config = create_thread()

    initial_state = {
        "stage": 1,
        "status": "running",
        "event_data": event_config,
        "task_packages": [],
        "research_results": None,
        "user_decision": None,
        "planning_output": None,
        "diagnostics": {},
        "agent_journal": [],
        "error": None,
    }

    # Workflow ausführen mit Progress-Anzeige
    console.print("\n[cyan]🚀 Starte Planung...[/cyan]\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TextColumn("[progress.percentage]{task.percentage:.0%}"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Verarbeite Arbeitspakete...", total=None)

        try:
            for event_chunk in workflow.stream(initial_state, thread_config, stream_mode="updates"):
                if isinstance(event_chunk, dict):
                    for node_name, node_state in event_chunk.items():
                        if isinstance(node_state, dict):
                            initial_state.update(node_state)
                            task_packages = initial_state.get("task_packages", [])
                            if task_packages:
                                progress.update(task, description=f"[cyan]{node_name}: {len(task_packages)} Pakete")

        except Exception as e:
            console.print(f"[red]❌ Fehler während der Planung: {e}[/red]")
            initial_state["error"] = str(e)

    # Ergebnisse anzeigen
    console.print("\n[cyan]✅ Planung abgeschlossen[/cyan]\n")
    _print_progress(initial_state.get("task_packages", []))

    # Markdown-Output speichern
    markdown_logger.log_planning_progress(initial_state)

    # Zusammenfassung
    console.print(
        Panel(
            """[bold green]✅ Planung erfolgreich abgeschlossen![/bold green]

Alle Logs wurden in [cyan]workstreams/[/cyan] als Markdown gespeichert.

[bold]Nächste Schritte:[/bold]
1. Überprüfe [cyan]workstreams/PLANUNGSLOG.md[/cyan]
2. Arbeite in deinem bevorzugten Workstream-Ordner
3. Alle Änderungen sollten in Markdown dokumentiert werden

[bold yellow]Hinweis:[/bold yellow] Diese CLI speichert alle Outputs als Markdown.
JSON-Dateien werden nicht mehr erzeugt.""",
            title="[green]🎉 Fertig[/green]",
            border_style="green",
        )
    )


if __name__ == "__main__":
    main()
