"""Research agent: venue scouting and catering comparison."""

import json
import logging
from typing import Any

from langchain_core.messages import HumanMessage

from src.llm import create_llm
from src.state import EventPlanningState, ResearchResults, TaskPackage
from src.websearch import build_web_research_context

logger = logging.getLogger(__name__)


def _is_web_search_enabled(event_data: dict[str, Any]) -> bool:
    runtime_cfg = event_data.get("runtime", {})
    value = runtime_cfg.get("enable_web_search", True)
    if isinstance(value, str):
        return value.strip().lower() in ("1", "true", "yes", "on")
    return bool(value)


def _make_research_prompt(event_data: dict[str, Any], web_context_text: str = "") -> str:
    event = event_data.get("event", event_data)
    name = event.get("name", "Unbekanntes Event")
    city = event.get("city", "unbekannte Stadt")
    attendees = event.get("attendees_expected", "unbekannte Anzahl")
    date_start = event.get("date_start", "TBD")
    date_end = event.get("date_end", "TBD")
    budget = event_data.get("budget", {})
    budget_total = budget.get("total_estimated", "TBD")

    web_block = ""
    if web_context_text.strip():
        web_block = f"""

Aktuelle Online-Recherche (Web-Snippets und Quellen, als Kontext nutzen):
{web_context_text}
"""

    return f"""Du bist ein erfahrener Event-Research-Agent. Erstelle eine detaillierte Marktanalyse für das folgende Event:

Event: {name}
Ort: {city}
Datum: {date_start} bis {date_end}
Teilnehmerzahl: {attendees}
Gesamtbudget: {budget_total} EUR
{web_block}

Aufgabe: Analysiere und empfehle 3 Venue-Optionen und 3 Catering-Optionen für dieses Event.

Antworte AUSSCHLIESSLICH mit einem validen JSON-Objekt in diesem exakten Format:
{{
  "venue_options": [
    {{
      "name": "Name der Location",
      "description": "Kurzbeschreibung",
      "pros": ["Vorteil 1", "Vorteil 2"],
      "cons": ["Nachteil 1", "Nachteil 2"],
      "estimated_cost": "X.XXX – X.XXX EUR",
      "recommendation_score": 4
    }}
  ],
  "catering_options": [
    {{
      "name": "Name des Caterers",
      "description": "Kurzbeschreibung",
      "pros": ["Vorteil 1", "Vorteil 2"],
      "cons": ["Nachteil 1", "Nachteil 2"],
      "estimated_cost": "XX – XX EUR pro Person",
      "recommendation_score": 4
    }}
  ]
}}

Wichtig: Antworte NUR mit dem JSON, ohne Erklärungen oder Markdown-Formatierung.
"""


def _parse_research_output(raw: str) -> ResearchResults | None:
    """Extract and validate the JSON research results from LLM output."""
    raw = raw.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        lines = raw.split("\n")
        raw = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    try:
        data = json.loads(raw)
        if "venue_options" in data and "catering_options" in data:
            return data  # type: ignore[return-value]
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def run_research_agent(state: EventPlanningState) -> dict[str, Any]:
    """LangGraph node: research agent."""
    logger.info("Research agent starting…")
    event_data = state.get("event_data", {})
    task_packages: list[TaskPackage] = list(state.get("task_packages", []))
    agent_journal = list(state.get("agent_journal", []))
    diagnostics = dict(state.get("diagnostics", {}))

    # AP1.1 – Venue research
    ap1_1: TaskPackage = {
        "id": "AP1.1",
        "agent": "Research-Agent",
        "task": "Venue-Recherche: 3 Location-Optionen mit Vor-/Nachteilen",
        "status": "running",
        "output": "",
    }
    # AP1.2 – Catering research
    ap1_2: TaskPackage = {
        "id": "AP1.2",
        "agent": "Research-Agent",
        "task": "Catering-Recherche: 3 Catering-Optionen mit Vor-/Nachteilen",
        "status": "running",
        "output": "",
    }
    task_packages = [p for p in task_packages if p["id"] not in ("AP1.1", "AP1.2")]
    task_packages.extend([ap1_1, ap1_2])
    agent_journal.append(
        {
            "agent": "Research-Agent",
            "phase": "stage1",
            "action": "Venue- und Catering-Recherche gestartet",
            "rationale": "Optionen und Risiken muessen vor der Freigabe transparent sein.",
            "outcome": "Analyse laeuft.",
        }
    )

    try:
        web_context: dict[str, Any] = {"sources": [], "context_text": "", "queries": []}
        web_search_enabled = _is_web_search_enabled(event_data)
        diagnostics["web_search"] = {
            "enabled": web_search_enabled,
            "status": "disabled",
            "queries": [],
            "source_count": 0,
            "message": "Online-Websuche ist deaktiviert.",
        }
        if web_search_enabled:
            web_context = build_web_research_context(event_data)
            source_count = len(web_context.get("sources", []))
            diagnostics["web_search"] = {
                "enabled": True,
                "status": "ok" if source_count > 0 else "no_results",
                "queries": web_context.get("queries", []),
                "source_count": source_count,
                "message": "Websuche erfolgreich." if source_count > 0 else "Websuche aktiv, aber ohne Treffer.",
            }

        llm = create_llm()
        prompt = _make_research_prompt(event_data, web_context_text=str(web_context.get("context_text", "")))
        response = llm.invoke([HumanMessage(content=prompt)])
        raw_output = response.content if hasattr(response, "content") else str(response)

        research_results = _parse_research_output(str(raw_output))

        if research_results is None:
            logger.warning("Could not parse LLM output; using mock data.")
            from src.llm import MockLLM
            mock = MockLLM()
            research_results = _parse_research_output(mock._mock_research_response())

        if research_results is None:
            raise RuntimeError("Research-Ausgabe konnte nicht als JSON geparst werden.")

        research_results["web_sources"] = web_context.get("sources", [])

        # Mark both task packages as completed
        for pkg in task_packages:
            if pkg["id"] == "AP1.1":
                pkg["status"] = "completed"
                pkg["output"] = f"{len(research_results['venue_options'])} Venue-Optionen analysiert"
            elif pkg["id"] == "AP1.2":
                pkg["status"] = "completed"
                source_count = len(research_results.get("web_sources", []))
                if source_count > 0:
                    pkg["output"] = f"{len(research_results['catering_options'])} Catering-Optionen analysiert ({source_count} Web-Quellen)"
                else:
                    pkg["output"] = f"{len(research_results['catering_options'])} Catering-Optionen analysiert"

        agent_journal.append(
            {
                "agent": "Research-Agent",
                "phase": "stage1",
                "action": "Marktanalyse abgeschlossen",
                "rationale": "Die besten Optionen wurden anhand Kosten, Eignung und Verfuegbarkeit priorisiert.",
                "outcome": f"{len(research_results['venue_options'])} Venues und {len(research_results['catering_options'])} Catering-Optionen bereitgestellt.",
            }
        )

        return {
            "stage": 1,
            "status": "waiting_for_user",
            "task_packages": task_packages,
            "research_results": research_results,
            "diagnostics": diagnostics,
            "agent_journal": agent_journal,
            "next_step": "Bitte Venue und Catering auswählen und Stage 2 freigeben",
            "error": None,
        }

    except Exception as exc:
        logger.error("Research agent error: %s", exc)
        for pkg in task_packages:
            if pkg["id"] in ("AP1.1", "AP1.2"):
                pkg["status"] = "error"
                pkg["output"] = str(exc)
        diagnostics["web_search"] = {
            "enabled": diagnostics.get("web_search", {}).get("enabled", False),
            "status": "error",
            "queries": diagnostics.get("web_search", {}).get("queries", []),
            "source_count": diagnostics.get("web_search", {}).get("source_count", 0),
            "message": f"Fehler bei der Recherche: {exc}",
        }
        agent_journal.append(
            {
                "agent": "Research-Agent",
                "phase": "stage1",
                "action": "Recherche fehlgeschlagen",
                "rationale": "Die Verarbeitung konnte nicht sauber abgeschlossen werden.",
                "outcome": str(exc),
            }
        )
        return {
            "stage": 1,
            "status": "error",
            "task_packages": task_packages,
            "diagnostics": diagnostics,
            "agent_journal": agent_journal,
            "error": str(exc),
            "next_step": "Fehler in Stage 1 – bitte prüfen",
        }
