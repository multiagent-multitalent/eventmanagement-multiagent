"""Content agent: invitation email, social media posts, press release."""

import json
import logging
from typing import Any

from langchain_core.messages import HumanMessage

from src.llm import create_llm
from src.state import EventPlanningState, TaskPackage

logger = logging.getLogger(__name__)


def _make_content_prompt(
    event_data: dict[str, Any],
    user_decision: dict[str, Any],
    planning_output: dict[str, Any],
) -> str:
    event = event_data.get("event", event_data)
    name = event.get("name", "Event")
    date_start = event.get("date_start", "TBD")
    date_end = event.get("date_end", "TBD")
    city = event.get("city", "TBD")
    attendees = event.get("attendees_expected", 125)
    organizer = event.get("organizer", {})
    org_name = organizer.get("name", "Veranstalter")
    venue = user_decision.get("selected_venue", "TBD")
    topics = event.get("topics", [])
    topics_str = ", ".join(topics) if topics else "KI-Transparenz, AI Safety"

    return f"""Du bist ein erfahrener Content-Agent für Event-Marketing. Erstelle professionelle Kommunikationsmaterialien.

Event: {name}
Datum: {date_start} bis {date_end}
Ort: {city}, Venue: {venue}
Teilnehmerzahl: {attendees}
Themen: {topics_str}
Veranstalter: {org_name}

Erstelle:
1. Eine Einladungs-E-Mail (Betreff + Text)
2. Drei Social-Media-Posts (Twitter/X, LinkedIn, Instagram)
3. Eine Pressemitteilung

Antworte AUSSCHLIESSLICH mit einem validen JSON-Objekt in diesem Format:
{{
  "invitation_email": {{
    "subject": "Betreff der E-Mail",
    "body": "Vollständiger E-Mail-Text mit Absätzen"
  }},
  "social_media_posts": {{
    "twitter_x": "Tweet-Text (max. 280 Zeichen)",
    "linkedin": "LinkedIn-Post-Text",
    "instagram": "Instagram-Caption-Text"
  }},
  "press_release": {{
    "headline": "Pressemitteilung-Überschrift",
    "subheadline": "Unterzeile",
    "body": "Vollständiger Pressemitteilung-Text",
    "contact": {{
      "organization": "{org_name}",
      "website": "Website-URL",
      "city": "{city}"
    }}
  }}
}}

Wichtig: Antworte NUR mit dem JSON, ohne Erklärungen oder Markdown-Formatierung. Alle Texte auf Deutsch.
"""


def _parse_content_output(raw: str) -> dict[str, Any] | None:
    raw = raw.strip()
    if raw.startswith("```"):
        lines = raw.split("\n")
        raw = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    try:
        data = json.loads(raw)
        required = {"invitation_email", "social_media_posts", "press_release"}
        if required.issubset(data.keys()):
            return data
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def run_content_agent(state: EventPlanningState) -> dict[str, Any]:
    """LangGraph node: content agent."""
    logger.info("Content agent starting…")
    event_data = state.get("event_data", {})
    user_decision = state.get("user_decision") or {}
    planning_output = state.get("planning_output") or {}
    task_packages: list[TaskPackage] = list(state.get("task_packages", []))
    agent_journal = list(state.get("agent_journal", []))

    new_packages: list[TaskPackage] = [
        {
            "id": "AP2.4",
            "agent": "Content-Agent",
            "task": "Einladungs-E-Mail erstellen",
            "status": "running",
            "output": "",
        },
        {
            "id": "AP2.5",
            "agent": "Content-Agent",
            "task": "Social-Media-Posts erstellen (Twitter/X, LinkedIn, Instagram)",
            "status": "running",
            "output": "",
        },
        {
            "id": "AP2.6",
            "agent": "Content-Agent",
            "task": "Pressemitteilung erstellen",
            "status": "running",
            "output": "",
        },
    ]
    existing_ids = {"AP2.4", "AP2.5", "AP2.6"}
    task_packages = [p for p in task_packages if p["id"] not in existing_ids]
    task_packages.extend(new_packages)
    agent_journal.append(
        {
            "agent": "Content-Agent",
            "phase": "stage2",
            "action": "Kommunikationsinhalte gestartet",
            "rationale": "Fuer die Event-Vermarktung werden konsistente Botschaften pro Kanal benoetigt.",
            "outcome": "Inhaltserstellung laeuft.",
        }
    )

    try:
        llm = create_llm()
        prompt = _make_content_prompt(event_data, user_decision, planning_output)
        response = llm.invoke([HumanMessage(content=prompt)])
        raw_output = response.content if hasattr(response, "content") else str(response)

        content_output = _parse_content_output(str(raw_output))

        if content_output is None:
            logger.warning("Could not parse content output; using mock data.")
            from src.llm import MockLLM
            mock = MockLLM()
            content_output = _parse_content_output(mock._mock_content_response())

        for pkg in task_packages:
            if pkg["id"] == "AP2.4":
                pkg["status"] = "completed"
                subject = content_output.get("invitation_email", {}).get("subject", "")
                pkg["output"] = f"E-Mail erstellt: {subject[:60]}…" if len(subject) > 60 else f"E-Mail erstellt: {subject}"
            elif pkg["id"] == "AP2.5":
                pkg["status"] = "completed"
                platforms = list(content_output.get("social_media_posts", {}).keys())
                pkg["output"] = f"Posts für {', '.join(platforms)} erstellt"
            elif pkg["id"] == "AP2.6":
                pkg["status"] = "completed"
                headline = content_output.get("press_release", {}).get("headline", "")
                pkg["output"] = f"Pressemitteilung: {headline[:60]}…" if len(headline) > 60 else f"PM: {headline}"

        channels = list(content_output.get("social_media_posts", {}).keys())
        agent_journal.append(
            {
                "agent": "Content-Agent",
                "phase": "stage2",
                "action": "Kommunikationspaket abgeschlossen",
                "rationale": "Die Zielgruppen werden ueber E-Mail, Social und Presse parallel angesprochen.",
                "outcome": f"Inhalte fuer Kanaele erstellt: {', '.join(channels)}.",
            }
        )

        return {
            "task_packages": task_packages,
            "content_output": content_output,
            "agent_journal": agent_journal,
            "error": None,
        }

    except Exception as exc:
        logger.error("Content agent error: %s", exc)
        for pkg in task_packages:
            if pkg["id"] in ("AP2.4", "AP2.5", "AP2.6"):
                pkg["status"] = "error"
                pkg["output"] = str(exc)
        agent_journal.append(
            {
                "agent": "Content-Agent",
                "phase": "stage2",
                "action": "Kommunikationsinhalte fehlgeschlagen",
                "rationale": "Die Verarbeitung konnte nicht sauber abgeschlossen werden.",
                "outcome": str(exc),
            }
        )
        return {
            "task_packages": task_packages,
            "agent_journal": agent_journal,
            "error": str(exc),
        }
