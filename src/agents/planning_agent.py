"""Planning agent: schedule, logistics, and budget drafts."""

import json
import logging
from typing import Any

from langchain_core.messages import HumanMessage

from src.llm import create_llm
from src.state import EventPlanningState, TaskPackage

logger = logging.getLogger(__name__)


def _make_planning_prompt(event_data: dict[str, Any], user_decision: dict[str, Any]) -> str:
    event = event_data.get("event", event_data)
    name = event.get("name", "Event")
    date_start = event.get("date_start", "TBD")
    date_end = event.get("date_end", "TBD")
    attendees = event.get("attendees_expected", 125)
    venue = user_decision.get("selected_venue", "ausgewählte Location")
    catering = user_decision.get("selected_catering", "ausgewähltes Catering")
    notes = user_decision.get("notes", "")

    return f"""Du bist ein erfahrener Event-Planungs-Agent. Erstelle einen detaillierten Planungsrahmen.

Event: {name}
Datum: {date_start} bis {date_end}
Teilnehmerzahl: {attendees}
Ausgewählte Venue: {venue}
Ausgewähltes Catering: {catering}
Anmerkungen: {notes}

Erstelle:
1. Einen detaillierten Zeitplan (Agenda) für alle Tage
2. Ein Logistikkonzept
3. Einen Budgetentwurf

Antworte AUSSCHLIESSLICH mit einem validen JSON-Objekt in diesem Format:
{{
  "schedule": {{
    "day_1": {{"date": "JJJJ-MM-TT", "theme": "Thema", "slots": [{{"time": "HH:MM – HH:MM", "activity": "Aktivität"}}]}},
    "day_2": {{"date": "JJJJ-MM-TT", "theme": "Thema", "slots": []}},
    "day_3": {{"date": "JJJJ-MM-TT", "theme": "Thema", "slots": []}}
  }},
  "logistics": {{
    "venue_setup": "Beschreibung",
    "registration": "Beschreibung",
    "av_technology": "Beschreibung",
    "accessibility": "Beschreibung",
    "accommodation": "Beschreibung",
    "transport": "Beschreibung",
    "wifi": "Beschreibung",
    "sustainability": "Beschreibung"
  }},
  "budget": {{
    "currency": "EUR",
    "total_estimated": 42500,
    "breakdown": {{
      "venue": {{"amount": 8500, "note": "Beschreibung"}},
      "catering": {{"amount": 7500, "note": "Beschreibung"}},
      "av_technology": {{"amount": 4500, "note": "Beschreibung"}},
      "speakers": {{"amount": 6000, "note": "Beschreibung"}},
      "marketing": {{"amount": 3500, "note": "Beschreibung"}},
      "staff": {{"amount": 4000, "note": "Beschreibung"}},
      "contingency": {{"amount": 4000, "note": "10% Puffer"}},
      "misc": {{"amount": 2500, "note": "Sonstiges"}}
    }}
  }}
}}

Wichtig: Antworte NUR mit dem JSON, ohne Erklärungen oder Markdown-Formatierung.
"""


def _parse_planning_output(raw: str) -> dict[str, Any] | None:
    raw = raw.strip()
    if raw.startswith("```"):
        lines = raw.split("\n")
        raw = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    try:
        data = json.loads(raw)
        if "schedule" in data and "logistics" in data and "budget" in data:
            return data
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def run_planning_agent(state: EventPlanningState) -> dict[str, Any]:
    """LangGraph node: planning agent."""
    logger.info("Planning agent starting…")
    event_data = state.get("event_data", {})
    user_decision = state.get("user_decision") or {}
    task_packages: list[TaskPackage] = list(state.get("task_packages", []))

    new_packages: list[TaskPackage] = [
        {
            "id": "AP2.1",
            "agent": "Planungs-Agent",
            "task": "Detaillierter Zeitplan (3-Tages-Agenda)",
            "status": "running",
            "output": "",
        },
        {
            "id": "AP2.2",
            "agent": "Planungs-Agent",
            "task": "Logistikkonzept (Aufbau, AV-Technik, Transport, Barrierefreiheit)",
            "status": "running",
            "output": "",
        },
        {
            "id": "AP2.3",
            "agent": "Planungs-Agent",
            "task": "Budgetentwurf mit Kostenaufstellung",
            "status": "running",
            "output": "",
        },
    ]
    existing_ids = {"AP2.1", "AP2.2", "AP2.3"}
    task_packages = [p for p in task_packages if p["id"] not in existing_ids]
    task_packages.extend(new_packages)

    try:
        llm = create_llm()
        prompt = _make_planning_prompt(event_data, user_decision)
        response = llm.invoke([HumanMessage(content=prompt)])
        raw_output = response.content if hasattr(response, "content") else str(response)

        planning_output = _parse_planning_output(str(raw_output))

        if planning_output is None:
            logger.warning("Could not parse planning output; using mock data.")
            from src.llm import MockLLM
            mock = MockLLM()
            planning_output = _parse_planning_output(mock._mock_planning_response())

        for pkg in task_packages:
            if pkg["id"] == "AP2.1":
                pkg["status"] = "completed"
                days = list(planning_output.get("schedule", {}).keys())
                pkg["output"] = f"Zeitplan für {len(days)} Tage erstellt"
            elif pkg["id"] == "AP2.2":
                pkg["status"] = "completed"
                sections = list(planning_output.get("logistics", {}).keys())
                pkg["output"] = f"Logistikkonzept mit {len(sections)} Bereichen erstellt"
            elif pkg["id"] == "AP2.3":
                pkg["status"] = "completed"
                total = planning_output.get("budget", {}).get("total_estimated", "TBD")
                pkg["output"] = f"Budgetentwurf: {total} EUR Gesamtkosten"

        return {
            "task_packages": task_packages,
            "planning_output": planning_output,
            "error": None,
        }

    except Exception as exc:
        logger.error("Planning agent error: %s", exc)
        for pkg in task_packages:
            if pkg["id"] in ("AP2.1", "AP2.2", "AP2.3"):
                pkg["status"] = "error"
                pkg["output"] = str(exc)
        return {
            "task_packages": task_packages,
            "error": str(exc),
        }
