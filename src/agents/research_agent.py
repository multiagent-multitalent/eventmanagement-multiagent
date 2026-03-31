"""Research agent: venue scouting and catering comparison."""

import json
import logging
from typing import Any

from langchain_core.messages import HumanMessage

from src.llm import create_llm
from src.state import EventPlanningState, ResearchResults, TaskPackage

logger = logging.getLogger(__name__)


def _make_research_prompt(event_data: dict[str, Any]) -> str:
    event = event_data.get("event", event_data)
    name = event.get("name", "Unbekanntes Event")
    city = event.get("city", "unbekannte Stadt")
    attendees = event.get("attendees_expected", "unbekannte Anzahl")
    date_start = event.get("date_start", "TBD")
    date_end = event.get("date_end", "TBD")
    budget = event_data.get("budget", {})
    budget_total = budget.get("total_estimated", "TBD")

    return f"""Du bist ein erfahrener Event-Research-Agent. Erstelle eine detaillierte Marktanalyse für das folgende Event:

Event: {name}
Ort: {city}
Datum: {date_start} bis {date_end}
Teilnehmerzahl: {attendees}
Gesamtbudget: {budget_total} EUR

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

    try:
        llm = create_llm()
        prompt = _make_research_prompt(event_data)
        response = llm.invoke([HumanMessage(content=prompt)])
        raw_output = response.content if hasattr(response, "content") else str(response)

        research_results = _parse_research_output(str(raw_output))

        if research_results is None:
            logger.warning("Could not parse LLM output; using mock data.")
            from src.llm import MockLLM
            mock = MockLLM()
            research_results = _parse_research_output(mock._mock_research_response())

        # Mark both task packages as completed
        for pkg in task_packages:
            if pkg["id"] == "AP1.1":
                pkg["status"] = "completed"
                pkg["output"] = f"{len(research_results['venue_options'])} Venue-Optionen analysiert"
            elif pkg["id"] == "AP1.2":
                pkg["status"] = "completed"
                pkg["output"] = f"{len(research_results['catering_options'])} Catering-Optionen analysiert"

        return {
            "stage": 1,
            "status": "waiting_for_user",
            "task_packages": task_packages,
            "research_results": research_results,
            "next_step": "Bitte Venue und Catering auswählen und Stage 2 freigeben",
            "error": None,
        }

    except Exception as exc:
        logger.error("Research agent error: %s", exc)
        for pkg in task_packages:
            if pkg["id"] in ("AP1.1", "AP1.2"):
                pkg["status"] = "error"
                pkg["output"] = str(exc)
        return {
            "stage": 1,
            "status": "error",
            "task_packages": task_packages,
            "error": str(exc),
            "next_step": "Fehler in Stage 1 – bitte prüfen",
        }
