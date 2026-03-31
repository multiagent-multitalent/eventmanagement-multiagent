"""LangGraph StateGraph for the event-planning workflow."""

import logging
import uuid
from pathlib import Path
from typing import Any

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from src.agents.content_agent import run_content_agent
from src.agents.planning_agent import run_planning_agent
from src.agents.research_agent import run_research_agent
from src.config import get_repo_root
from src.state import EventPlanningState

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Node implementations
# ---------------------------------------------------------------------------

def research_node(state: EventPlanningState) -> dict[str, Any]:
    """Run research agent."""
    return run_research_agent(state)


def human_review_node(state: EventPlanningState) -> dict[str, Any]:
    """
    Process human decision after Stage 1.

    This node is only entered after the graph is resumed by the dashboard with
    an updated user_decision and status='approved' (or 'cancelled').
    """
    user_decision = state.get("user_decision")
    status = state.get("status", "waiting_for_user")

    if status == "cancelled":
        return {
            "status": "cancelled",
            "next_step": "Planung abgebrochen",
        }

    if user_decision and status == "approved":
        return {
            "stage": 2,
            "status": "running",
            "next_step": "Stage 2: Planungs- und Content-Agent werden gestartet",
        }

    # Safety fallback – should not normally happen
    return {
        "status": "waiting_for_user",
        "next_step": "Bitte Venue und Catering auswählen und Stage 2 freigeben",
    }


def planning_node(state: EventPlanningState) -> dict[str, Any]:
    """Run planning agent."""
    return run_planning_agent(state)


def content_node(state: EventPlanningState) -> dict[str, Any]:
    """Run content agent."""
    return run_content_agent(state)


def finalize_node(state: EventPlanningState) -> dict[str, Any]:
    """Write markdown output files and mark workflow as completed."""
    try:
        _write_output_files(state)
    except Exception as exc:
        logger.error("Could not write output files: %s", exc)

    return {
        "stage": 2,
        "status": "completed",
        "next_step": "Planung abgeschlossen – alle Dokumente wurden erstellt",
    }


# ---------------------------------------------------------------------------
# Conditional routing
# ---------------------------------------------------------------------------

def _after_human_review(state: EventPlanningState) -> str:
    status = state.get("status", "waiting_for_user")
    if status == "cancelled":
        return "end"
    return "planning"


# ---------------------------------------------------------------------------
# Output file generation
# ---------------------------------------------------------------------------

def _write_output_files(state: EventPlanningState) -> None:
    repo_root = get_repo_root()
    event_data = state.get("event_data", {})
    event = event_data.get("event", event_data)
    event_name = event.get("name", "Event")
    research = state.get("research_results") or {}
    user_decision = state.get("user_decision") or {}
    planning = state.get("planning_output") or {}
    content = state.get("content_output") or {}

    # --- Venue research ---
    venue_path = repo_root / "workstreams" / "venue-logistik" / "venue-recherche.md"
    venue_path.parent.mkdir(parents=True, exist_ok=True)
    venue_path.write_text(
        _render_venue_md(event_name, research, user_decision), encoding="utf-8"
    )
    logger.info("Written: %s", venue_path)

    # --- Catering concept ---
    catering_path = repo_root / "workstreams" / "catering" / "catering-konzept.md"
    catering_path.parent.mkdir(parents=True, exist_ok=True)
    catering_path.write_text(_render_catering_md(event_name, research, user_decision), encoding="utf-8")
    logger.info("Written: %s", catering_path)

    # --- Program / agenda ---
    program_path = repo_root / "workstreams" / "programm" / "agenda-entwurf.md"
    program_path.parent.mkdir(parents=True, exist_ok=True)
    program_path.write_text(_render_agenda_md(event_name, planning), encoding="utf-8")
    logger.info("Written: %s", program_path)

    # --- Communication plan ---
    comm_path = repo_root / "workstreams" / "kommunikation" / "kommunikationsplan.md"
    comm_path.parent.mkdir(parents=True, exist_ok=True)
    comm_path.write_text(_render_communication_md(event_name, content), encoding="utf-8")
    logger.info("Written: %s", comm_path)


def _render_venue_md(event_name: str, research: dict, user_decision: dict) -> str:
    selected = user_decision.get("selected_venue", "")
    lines = [f"# Venue-Recherche: {event_name}\n"]
    if selected:
        lines.append(f"**Ausgewählte Venue:** {selected}\n")
    lines.append("\n## Venue-Optionen\n")
    for opt in research.get("venue_options", []):
        score = "⭐" * int(opt.get("recommendation_score", 0))
        lines.append(f"### {opt.get('name', '')} {score}\n")
        lines.append(f"{opt.get('description', '')}\n\n")
        lines.append(f"**Geschätzte Kosten:** {opt.get('estimated_cost', 'TBD')}\n\n")
        lines.append("**Vorteile:**\n")
        for pro in opt.get("pros", []):
            lines.append(f"- {pro}\n")
        lines.append("\n**Nachteile:**\n")
        for con in opt.get("cons", []):
            lines.append(f"- {con}\n")
        lines.append("\n---\n\n")
    return "".join(lines)


def _render_catering_md(event_name: str, research: dict, user_decision: dict) -> str:
    selected = user_decision.get("selected_catering", "")
    lines = [f"# Catering-Konzept: {event_name}\n"]
    if selected:
        lines.append(f"**Ausgewählter Caterer:** {selected}\n\n")
    lines.append("## Catering-Optionen\n")
    for opt in research.get("catering_options", []):
        score = "⭐" * int(opt.get("recommendation_score", 0))
        lines.append(f"### {opt.get('name', '')} {score}\n")
        lines.append(f"{opt.get('description', '')}\n\n")
        lines.append(f"**Geschätzte Kosten:** {opt.get('estimated_cost', 'TBD')}\n\n")
        lines.append("**Vorteile:**\n")
        for pro in opt.get("pros", []):
            lines.append(f"- {pro}\n")
        lines.append("\n**Nachteile:**\n")
        for con in opt.get("cons", []):
            lines.append(f"- {con}\n")
        lines.append("\n---\n\n")
    return "".join(lines)


def _render_agenda_md(event_name: str, planning: dict) -> str:
    lines = [f"# Agenda-Entwurf: {event_name}\n\n"]
    schedule = planning.get("schedule", {})
    for day_key in sorted(schedule.keys()):
        day = schedule[day_key]
        lines.append(f"## {day.get('date', day_key)} – {day.get('theme', '')}\n\n")
        lines.append("| Uhrzeit | Aktivität |\n|---|---|\n")
        for slot in day.get("slots", []):
            lines.append(f"| {slot.get('time', '')} | {slot.get('activity', '')} |\n")
        lines.append("\n")

    budget = planning.get("budget", {})
    if budget:
        lines.append("## Budget-Übersicht\n\n")
        lines.append(f"**Gesamtbudget:** {budget.get('total_estimated', 'TBD')} {budget.get('currency', 'EUR')}\n\n")
        lines.append("| Kategorie | Betrag (EUR) | Anmerkung |\n|---|---|---|\n")
        for cat, details in budget.get("breakdown", {}).items():
            lines.append(f"| {cat} | {details.get('amount', '')} | {details.get('note', '')} |\n")
        lines.append("\n")

    logistics = planning.get("logistics", {})
    if logistics:
        lines.append("## Logistik-Konzept\n\n")
        for key, value in logistics.items():
            lines.append(f"**{key.replace('_', ' ').title()}:** {value}\n\n")

    return "".join(lines)


def _render_communication_md(event_name: str, content: dict) -> str:
    lines = [f"# Kommunikationsplan: {event_name}\n\n"]

    email = content.get("invitation_email", {})
    if email:
        lines.append("## Einladungs-E-Mail\n\n")
        lines.append(f"**Betreff:** {email.get('subject', '')}\n\n")
        lines.append("```\n")
        lines.append(email.get("body", ""))
        lines.append("\n```\n\n")

    posts = content.get("social_media_posts", {})
    if posts:
        lines.append("## Social-Media-Posts\n\n")
        for platform, text in posts.items():
            lines.append(f"### {platform.replace('_', ' ').title()}\n\n")
            lines.append(f"{text}\n\n")

    pr = content.get("press_release", {})
    if pr:
        lines.append("## Pressemitteilung\n\n")
        lines.append(f"# {pr.get('headline', '')}\n")
        lines.append(f"*{pr.get('subheadline', '')}*\n\n")
        lines.append(pr.get("body", ""))
        lines.append("\n\n")
        contact = pr.get("contact", {})
        if contact:
            lines.append("**Kontakt:**\n")
            for k, v in contact.items():
                lines.append(f"- {k}: {v}\n")

    return "".join(lines)


# ---------------------------------------------------------------------------
# Graph factory
# ---------------------------------------------------------------------------

def create_event_planning_graph():
    """Build and compile the LangGraph StateGraph."""
    checkpointer = MemorySaver()

    graph = StateGraph(EventPlanningState)

    graph.add_node("research_node", research_node)
    graph.add_node("human_review_node", human_review_node)
    graph.add_node("planning_node", planning_node)
    graph.add_node("content_node", content_node)
    graph.add_node("finalize_node", finalize_node)

    graph.add_edge(START, "research_node")
    graph.add_edge("research_node", "human_review_node")
    graph.add_conditional_edges(
        "human_review_node",
        _after_human_review,
        {"planning": "planning_node", "end": END},
    )
    graph.add_edge("planning_node", "content_node")
    graph.add_edge("content_node", "finalize_node")
    graph.add_edge("finalize_node", END)

    compiled = graph.compile(
        checkpointer=checkpointer,
        interrupt_before=["human_review_node"],
    )
    return compiled


def create_thread() -> dict[str, Any]:
    """Return a fresh LangGraph thread configuration."""
    return {"configurable": {"thread_id": str(uuid.uuid4())}}
