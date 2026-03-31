"""Streamlit dashboard for the Event-Management Orchestrator."""

import json
import logging
import uuid
from typing import Any

import streamlit as st

from src.config import load_event_config
from src.workflows.event_planning_graph import create_event_planning_graph, create_thread

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="Event-Management Orchestrator",
    page_icon="🎪",
    layout="wide",
)


# ---------------------------------------------------------------------------
# Cached resources
# ---------------------------------------------------------------------------

@st.cache_resource
def get_workflow():
    return create_event_planning_graph()


# ---------------------------------------------------------------------------
# Session-state initialisation
# ---------------------------------------------------------------------------

def _init_session_state() -> None:
    defaults: dict[str, Any] = {
        "thread_id": str(uuid.uuid4()),
        "current_stage": 0,
        "graph_state": None,
        "workflow_config": None,
        "stage1_done": False,
        "stage2_done": False,
        "running": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _build_initial_state(form_data: dict[str, Any]) -> dict[str, Any]:
    return {
        "stage": 1,
        "status": "running",
        "event_data": {"event": form_data},
        "task_packages": [],
        "research_results": None,
        "user_decision": None,
        "planning_output": None,
        "content_output": None,
        "next_step": "Stage 1 starten",
        "error": None,
    }


def _status_badge(status: str) -> str:
    mapping = {
        "completed": "✅",
        "running": "⏳",
        "pending": "🔲",
        "error": "❌",
    }
    return mapping.get(status, "❓")


def _render_task_table(task_packages: list[dict]) -> None:
    if not task_packages:
        return
    rows = []
    for pkg in task_packages:
        rows.append(
            {
                "ID": pkg.get("id", ""),
                "Agent": pkg.get("agent", ""),
                "Aufgabe": pkg.get("task", ""),
                "Status": f"{_status_badge(pkg.get('status', ''))} {pkg.get('status', '')}",
                "Ergebnis": pkg.get("output", ""),
            }
        )
    st.dataframe(rows, use_container_width=True)


def _render_venue_cards(venue_options: list[dict]) -> str | None:
    selected = None
    options = [v.get("name", f"Venue {i+1}") for i, v in enumerate(venue_options)]
    selected = st.radio("Venue auswählen:", options, key="selected_venue_radio")

    for opt in venue_options:
        is_selected = opt.get("name") == selected
        border = "2px solid #4CAF50" if is_selected else "1px solid #ddd"
        score_stars = "⭐" * int(opt.get("recommendation_score", 0))
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {opt.get('name', '')} {score_stars}")
                st.write(opt.get("description", ""))
                st.markdown(f"**Kosten:** {opt.get('estimated_cost', 'TBD')}")
            with col2:
                st.markdown("**Vorteile:**")
                for pro in opt.get("pros", []):
                    st.markdown(f"✓ {pro}")
                st.markdown("**Nachteile:**")
                for con in opt.get("cons", []):
                    st.markdown(f"✗ {con}")
    return selected


def _render_catering_cards(catering_options: list[dict]) -> str | None:
    options = [c.get("name", f"Caterer {i+1}") for i, c in enumerate(catering_options)]
    selected = st.radio("Catering auswählen:", options, key="selected_catering_radio")

    for opt in catering_options:
        score_stars = "⭐" * int(opt.get("recommendation_score", 0))
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {opt.get('name', '')} {score_stars}")
                st.write(opt.get("description", ""))
                st.markdown(f"**Kosten:** {opt.get('estimated_cost', 'TBD')}")
            with col2:
                st.markdown("**Vorteile:**")
                for pro in opt.get("pros", []):
                    st.markdown(f"✓ {pro}")
                st.markdown("**Nachteile:**")
                for con in opt.get("cons", []):
                    st.markdown(f"✗ {con}")
    return selected


# ---------------------------------------------------------------------------
# Sidebar – event configuration form
# ---------------------------------------------------------------------------

def render_sidebar() -> dict[str, Any] | None:
    st.sidebar.title("🎪 Event-Konfiguration")

    config = load_event_config()
    event = config.get("event", {})
    budget_cfg = config.get("budget", {})

    with st.sidebar.form("event_config_form"):
        event_name = st.text_input("Event-Name", value=event.get("name", ""))
        date_start = st.text_input("Startdatum (JJJJ-MM-TT)", value=event.get("date_start", ""))
        date_end = st.text_input("Enddatum (JJJJ-MM-TT)", value=event.get("date_end", ""))
        city = st.text_input("Stadt", value=event.get("city", ""))
        attendees = st.number_input(
            "Erwartete Teilnehmerzahl",
            min_value=1,
            max_value=10000,
            value=int(event.get("attendees_expected", 125)),
        )
        budget_total = st.text_input(
            "Gesamtbudget (EUR)",
            value=str(budget_cfg.get("total_estimated", "TBD")),
        )
        format_options = ["Konferenz", "Workshop", "Hackathon", "Meetup", "Webinar", "Hybrid"]
        current_formats = event.get("format", ["Konferenz"])
        selected_formats = st.multiselect("Format", format_options, default=current_formats)
        topics_raw = st.text_area(
            "Themen (eine pro Zeile)",
            value="\n".join(event.get("topics", [])),
        )

        submitted = st.form_submit_button("▶ Stage 1 starten (Research)", type="primary")

    if submitted:
        return {
            "name": event_name,
            "date_start": date_start,
            "date_end": date_end,
            "city": city,
            "attendees_expected": int(attendees),
            "budget_total": budget_total,
            "format": selected_formats,
            "topics": [t.strip() for t in topics_raw.splitlines() if t.strip()],
            "organizer": event.get("organizer", {}),
        }
    return None


# ---------------------------------------------------------------------------
# Stage 1 – Research tab
# ---------------------------------------------------------------------------

def render_stage1_tab() -> None:
    st.header("📍 Stage 1: Research & Optionen")

    graph_state = st.session_state.get("graph_state")

    if not st.session_state.get("stage1_done") and graph_state is None:
        st.info("Fülle die Event-Konfiguration in der Sidebar aus und klicke 'Stage 1 starten'.")
        return

    if st.session_state.get("running"):
        with st.spinner("Research-Agent läuft…"):
            st.write("Analysiere Venues und Catering-Optionen…")
        return

    if graph_state is None:
        st.info("Noch keine Daten vorhanden.")
        return

    # Task package table
    st.subheader("Arbeitspakete")
    _render_task_table(graph_state.get("task_packages", []))

    research = graph_state.get("research_results")
    if not research:
        if graph_state.get("error"):
            st.error(f"Fehler: {graph_state['error']}")
        return

    # Venue cards
    st.subheader("🏢 Venue-Optionen")
    selected_venue = _render_venue_cards(research.get("venue_options", []))

    # Catering cards
    st.subheader("🍽️ Catering-Optionen")
    selected_catering = _render_catering_cards(research.get("catering_options", []))

    # Approval notes
    notes = st.text_area("Anmerkungen zur Auswahl (optional)", key="approval_notes")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Freigeben & Stage 2 starten", type="primary"):
            _approve_and_start_stage2(selected_venue, selected_catering, notes)
    with col2:
        if st.button("❌ Abbrechen"):
            _cancel_workflow()

    # Raw JSON state expander
    with st.expander("🔍 Aktueller JSON-State"):
        display_state = {
            "stage": graph_state.get("stage"),
            "status": graph_state.get("status"),
            "task_packages": graph_state.get("task_packages", []),
            "next_step": graph_state.get("next_step"),
        }
        st.json(display_state)


def _approve_and_start_stage2(selected_venue: str, selected_catering: str, notes: str) -> None:
    workflow = get_workflow()
    config = st.session_state.get("workflow_config")
    if config is None:
        st.error("Kein aktiver Workflow-Thread gefunden.")
        return

    user_decision = {
        "selected_venue": selected_venue or "",
        "selected_catering": selected_catering or "",
        "notes": notes,
    }

    # Update graph state with user decision
    workflow.update_state(
        config,
        {"user_decision": user_decision, "status": "approved"},
    )

    st.session_state["running"] = True
    with st.spinner("Planungs- und Content-Agent arbeiten…"):
        final_state = workflow.invoke(None, config=config)

    st.session_state["graph_state"] = final_state
    st.session_state["stage2_done"] = True
    st.session_state["running"] = False
    st.success("Stage 2 abgeschlossen!")
    st.rerun()


def _cancel_workflow() -> None:
    workflow = get_workflow()
    config = st.session_state.get("workflow_config")
    if config:
        workflow.update_state(config, {"status": "cancelled"})
        workflow.invoke(None, config=config)
    st.session_state["graph_state"] = None
    st.session_state["stage1_done"] = False
    st.session_state["stage2_done"] = False
    st.warning("Planung abgebrochen.")
    st.rerun()


# ---------------------------------------------------------------------------
# Stage 2 – Planning & Content tab
# ---------------------------------------------------------------------------

def render_stage2_tab() -> None:
    st.header("📋 Stage 2: Planung & Content")

    if not st.session_state.get("stage2_done"):
        st.info("Stage 2 startet automatisch nach Ihrer Freigabe in Stage 1.")
        return

    graph_state = st.session_state.get("graph_state") or {}

    st.subheader("Arbeitspakete")
    _render_task_table(graph_state.get("task_packages", []))

    # Planning output
    planning = graph_state.get("planning_output") or {}
    if planning:
        st.subheader("📅 Zeitplan (Agenda)")
        schedule = planning.get("schedule", {})
        for day_key in sorted(schedule.keys()):
            day = schedule[day_key]
            with st.expander(f"{day.get('date', day_key)} – {day.get('theme', '')}"):
                for slot in day.get("slots", []):
                    st.write(f"**{slot.get('time', '')}** – {slot.get('activity', '')}")

        st.subheader("💰 Budget-Entwurf")
        budget = planning.get("budget", {})
        if budget:
            total = budget.get("total_estimated", "TBD")
            currency = budget.get("currency", "EUR")
            st.metric("Gesamtbudget", f"{total:,} {currency}" if isinstance(total, (int, float)) else f"{total} {currency}")
            breakdown = budget.get("breakdown", {})
            if breakdown:
                rows = [
                    {"Kategorie": k, "Betrag (EUR)": v.get("amount", ""), "Anmerkung": v.get("note", "")}
                    for k, v in breakdown.items()
                ]
                st.dataframe(rows, use_container_width=True)

    # Content output
    content = graph_state.get("content_output") or {}
    if content:
        st.subheader("📣 Kommunikationsmaterialien")

        email = content.get("invitation_email", {})
        if email:
            with st.expander("✉️ Einladungs-E-Mail"):
                st.markdown(f"**Betreff:** {email.get('subject', '')}")
                st.text_area("E-Mail-Text", value=email.get("body", ""), height=250, disabled=True, key="email_preview")

        posts = content.get("social_media_posts", {})
        if posts:
            _PLATFORM_LABELS = {
                "x_twitter": "X (ehemals Twitter)",
                "linkedin": "LinkedIn",
                "instagram": "Instagram",
                "facebook": "Facebook",
                "mastodon": "Mastodon",
            }
            with st.expander("📱 Social-Media-Posts"):
                for platform, text in posts.items():
                    label = _PLATFORM_LABELS.get(platform, platform.replace("_", " ").title())
                    st.markdown(f"**{label}**")
                    st.text_area(platform, value=text, height=150, disabled=True, key=f"post_{platform}")

        pr = content.get("press_release", {})
        if pr:
            with st.expander("📰 Pressemitteilung"):
                st.markdown(f"## {pr.get('headline', '')}")
                st.markdown(f"*{pr.get('subheadline', '')}*")
                st.write(pr.get("body", ""))

    # Download button
    if planning or content:
        all_outputs = {
            "stage": graph_state.get("stage"),
            "status": graph_state.get("status"),
            "task_packages": graph_state.get("task_packages", []),
            "planning_output": planning,
            "content_output": content,
            "next_step": graph_state.get("next_step"),
        }
        st.download_button(
            label="⬇️ Alle Outputs als JSON herunterladen",
            data=json.dumps(all_outputs, ensure_ascii=False, indent=2),
            file_name="aitd2026-event-planning-outputs.json",
            mime="application/json",
        )
        st.success(
            "✅ Markdown-Dateien wurden in die Workstreams-Ordner geschrieben:\n"
            "- `workstreams/venue-logistik/venue-recherche.md`\n"
            "- `workstreams/catering/catering-konzept.md`\n"
            "- `workstreams/programm/agenda-entwurf.md`\n"
            "- `workstreams/kommunikation/kommunikationsplan.md`"
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    _init_session_state()

    st.title("🎪 Event-Management Orchestrator")
    st.caption("KI-gestütztes Multi-Agenten-System für vollautomatische Event-Planung")

    # Sidebar form handling
    form_data = render_sidebar()

    if form_data is not None:
        # User clicked "Start Stage 1"
        workflow = get_workflow()
        thread_config = create_thread()
        st.session_state["thread_id"] = thread_config["configurable"]["thread_id"]
        st.session_state["workflow_config"] = thread_config
        st.session_state["stage1_done"] = False
        st.session_state["stage2_done"] = False
        st.session_state["running"] = True
        st.session_state["graph_state"] = None

        initial_state = _build_initial_state(form_data)

        with st.spinner("Research-Agent läuft…"):
            result = workflow.invoke(initial_state, config=thread_config)

        st.session_state["graph_state"] = result
        st.session_state["stage1_done"] = True
        st.session_state["current_stage"] = 1
        st.session_state["running"] = False
        st.rerun()

    # Main tabs
    tab1, tab2 = st.tabs(["📍 Stage 1: Research", "📋 Stage 2: Planung & Content"])
    with tab1:
        render_stage1_tab()
    with tab2:
        render_stage2_tab()


if __name__ == "__main__":
    main()
