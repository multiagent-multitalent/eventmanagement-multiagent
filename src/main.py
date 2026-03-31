"""CLI entry point for the Event-Management Orchestrator.

Usage:
    python -m src.main
"""

import json
import logging
import sys
from pathlib import Path

from src.config import load_event_config, get_repo_root
from src.workflows.event_planning_graph import create_event_planning_graph, create_thread

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def _print_section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print("=" * 60)


def _print_venue_options(venue_options: list[dict]) -> None:
    for i, opt in enumerate(venue_options, 1):
        stars = "⭐" * int(opt.get("recommendation_score", 0))
        print(f"\n  [{i}] {opt.get('name')} {stars}")
        print(f"      Kosten: {opt.get('estimated_cost', 'TBD')}")
        print(f"      {opt.get('description', '')}")
        pros = opt.get("pros", [])
        if pros:
            print(f"      ✓ {' | '.join(pros[:2])}")
        cons = opt.get("cons", [])
        if cons:
            print(f"      ✗ {' | '.join(cons[:2])}")


def _print_catering_options(catering_options: list[dict]) -> None:
    for i, opt in enumerate(catering_options, 1):
        stars = "⭐" * int(opt.get("recommendation_score", 0))
        print(f"\n  [{i}] {opt.get('name')} {stars}")
        print(f"      Kosten: {opt.get('estimated_cost', 'TBD')}")
        print(f"      {opt.get('description', '')}")


def _select_option(options: list[dict], label: str) -> str:
    """Prompt user to select one option by number."""
    while True:
        try:
            raw = input(f"\n{label} (1-{len(options)}): ").strip()
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return options[idx].get("name", f"Option {idx+1}")
            print(f"  Bitte eine Zahl zwischen 1 und {len(options)} eingeben.")
        except ValueError:
            print(f"  Bitte eine Zahl zwischen 1 und {len(options)} eingeben.")
        except EOFError:
            # Non-interactive environment: default to first option
            print(f"  Nicht-interaktiver Modus – wähle automatisch Option 1.")
            return options[0].get("name", "Option 1")
        except KeyboardInterrupt:
            print("\nAbgebrochen.")
            sys.exit(0)


def _save_json_output(state: dict, repo_root: Path) -> None:
    output_dir = repo_root / "workstreams"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "event-planning-output.json"
    output_file.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    print(f"\n  JSON-Ausgabe gespeichert: {output_file}")


def main() -> None:
    print("\n🎪  Event-Management Orchestrator – CLI")
    print("    Vollautomatische Event-Planung mit KI-Agenten\n")

    # Load config
    repo_root = get_repo_root()
    event_config = load_event_config()
    event = event_config.get("event", {})
    event_name = event.get("name", "Unbekanntes Event")
    print(f"  Event: {event_name}")
    print(f"  Datum: {event.get('date_start')} – {event.get('date_end')}")
    print(f"  Ort:   {event.get('city')}")
    print(f"  Teilnehmer: {event.get('attendees_expected')}")

    # Build graph
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
        "content_output": None,
        "next_step": "Stage 1 starten",
        "error": None,
    }

    # -----------------------------------------------------------------------
    # Stage 1: Research
    # -----------------------------------------------------------------------
    _print_section("Stage 1: Research (Venues & Catering)")
    print("  Research-Agent analysiert Optionen…")

    stage1_result = workflow.invoke(initial_state, config=thread_config)

    if stage1_result.get("error"):
        print(f"\n❌ Fehler in Stage 1: {stage1_result['error']}")
        sys.exit(1)

    research = stage1_result.get("research_results") or {}
    venue_options = research.get("venue_options", [])
    catering_options = research.get("catering_options", [])

    print("\n📊 Stage 1 Ergebnis (JSON):")
    summary = {
        "stage": stage1_result.get("stage"),
        "status": stage1_result.get("status"),
        "task_packages": [
            {"id": p["id"], "status": p["status"], "output": p["output"]}
            for p in stage1_result.get("task_packages", [])
        ],
        "next_step": stage1_result.get("next_step"),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    # Display options
    _print_section("Venue-Optionen")
    _print_venue_options(venue_options)

    _print_section("Catering-Optionen")
    _print_catering_options(catering_options)

    # -----------------------------------------------------------------------
    # Human decision
    # -----------------------------------------------------------------------
    _print_section("Ihre Entscheidung")

    selected_venue = _select_option(venue_options, "Venue auswählen")
    print(f"  ✓ Venue ausgewählt: {selected_venue}")

    selected_catering = _select_option(catering_options, "Catering auswählen")
    print(f"  ✓ Catering ausgewählt: {selected_catering}")

    try:
        notes = input("\n  Anmerkungen (optional, Enter zum Überspringen): ").strip()
    except (EOFError, KeyboardInterrupt):
        notes = ""

    user_decision = {
        "selected_venue": selected_venue,
        "selected_catering": selected_catering,
        "notes": notes,
    }

    # -----------------------------------------------------------------------
    # Stage 2: Planning & Content
    # -----------------------------------------------------------------------
    _print_section("Stage 2: Planung & Content-Erstellung")
    print("  Planungs-Agent und Content-Agent arbeiten…")

    workflow.update_state(
        thread_config,
        {"user_decision": user_decision, "status": "approved"},
    )

    final_state = workflow.invoke(None, config=thread_config)

    if final_state.get("error"):
        print(f"\n❌ Fehler in Stage 2: {final_state['error']}")

    print("\n✅ Stage 2 abgeschlossen!")

    # Show task package summary
    print("\n📋 Alle Arbeitspakete:")
    for pkg in final_state.get("task_packages", []):
        icon = "✅" if pkg["status"] == "completed" else "❌"
        print(f"  {icon} {pkg['id']} ({pkg['agent']}): {pkg['output']}")

    # Show key planning outputs
    planning = final_state.get("planning_output") or {}
    if planning:
        budget = planning.get("budget", {})
        total = budget.get("total_estimated", "TBD")
        print(f"\n💰 Budgetentwurf: {total} EUR")

    content = final_state.get("content_output") or {}
    if content:
        email_subject = content.get("invitation_email", {}).get("subject", "")
        print(f"\n✉️  Einladungs-E-Mail Betreff: {email_subject}")

    # Output JSON summary
    print("\n📊 Stage 2 Ergebnis (JSON):")
    result_summary = {
        "stage": final_state.get("stage"),
        "status": final_state.get("status"),
        "task_packages": [
            {"id": p["id"], "status": p["status"], "output": p["output"]}
            for p in final_state.get("task_packages", [])
        ],
        "next_step": final_state.get("next_step"),
    }
    print(json.dumps(result_summary, ensure_ascii=False, indent=2))

    # Save full output JSON
    _save_json_output(final_state, repo_root)

    print("\n📁 Markdown-Dateien wurden erstellt:")
    print("   workstreams/venue-logistik/venue-recherche.md")
    print("   workstreams/catering/catering-konzept.md")
    print("   workstreams/programm/agenda-entwurf.md")
    print("   workstreams/kommunikation/kommunikationsplan.md")
    print("\n🎉 Planung abgeschlossen!\n")


if __name__ == "__main__":
    main()
