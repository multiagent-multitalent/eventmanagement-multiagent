"""Streamlit dashboard for the Event-Management Orchestrator."""

import json
import logging
import os
import uuid
from datetime import date, datetime
from typing import Any

import streamlit as st

from src.config import (
    default_llm_base_url,
    get_llm_config,
    load_event_config,
    normalize_llm_provider,
)
from src.llm import list_available_models
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
    llm_settings = get_llm_config()
    defaults: dict[str, Any] = {
        "thread_id": str(uuid.uuid4()),
        "current_stage": 0,
        "graph_state": None,
        "workflow_config": None,
        "stage1_done": False,
        "stage2_done": False,
        "running": False,
        "llm_settings": llm_settings,
        "available_models": [str(llm_settings.get("model", "llama3.2"))],
        "available_models_context": {
            "provider": normalize_llm_provider(str(llm_settings.get("provider", "ollama"))),
            "base_url": str(llm_settings.get("base_url", "")).strip(),
            "api_key": str(llm_settings.get("api_key", "")).strip(),
        },
        "model_discovery_error": None,
        "active_view": "stage1",
        "view_selector": "📍 Stage 1: Research",
        "requested_view": None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _build_initial_state(form_data: dict[str, Any]) -> dict[str, Any]:
    event_payload = form_data.get("event", form_data)
    runtime_payload = form_data.get("runtime", {})
    return {
        "stage": 1,
        "status": "running",
        "event_data": {"event": event_payload, "runtime": runtime_payload},
        "task_packages": [],
        "research_results": None,
        "user_decision": None,
        "planning_output": None,
        "content_output": None,
        "diagnostics": {},
        "agent_journal": [],
        "next_step": "Stage 1 starten",
        "error": None,
    }


def _apply_llm_runtime_config(runtime: dict[str, Any]) -> None:
    provider = normalize_llm_provider(str(runtime.get("provider", "ollama")))
    model = str(runtime.get("model", "llama3.2")).strip() or "llama3.2"
    base_url = str(runtime.get("base_url", default_llm_base_url(provider))).strip() or default_llm_base_url(provider)
    api_key = str(runtime.get("api_key", "local")).strip() or "local"
    enable_web_search = bool(runtime.get("enable_web_search", True))

    os.environ["LLM_PROVIDER"] = provider
    os.environ["LLM_MODEL"] = model
    os.environ["LLM_BASE_URL"] = base_url
    os.environ["LLM_API_KEY"] = api_key
    os.environ["ENABLE_WEB_SEARCH"] = "1" if enable_web_search else "0"


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


def _merge_state(base_state: dict[str, Any], update: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base_state)
    for key, value in update.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = {**merged[key], **value}
        else:
            merged[key] = value
    return merged


def _extract_stream_update(chunk: Any) -> dict[str, Any]:
    if not isinstance(chunk, dict):
        return {}

    merged_update: dict[str, Any] = {}
    for _, value in chunk.items():
        if isinstance(value, dict):
            merged_update = _merge_state(merged_update, value)
    return merged_update


def _calculate_progress(task_packages: list[dict]) -> tuple[int, int, int]:
    total = len(task_packages)
    if total == 0:
        return (0, 0, 0)

    completed = sum(1 for pkg in task_packages if pkg.get("status") == "completed")
    progress = int((completed / total) * 100)
    return (completed, total, progress)


def _render_progress(task_packages: list[dict], progress_placeholder: Any | None = None) -> None:
    completed, total, progress = _calculate_progress(task_packages)
    text = f"Fortschritt: {completed}/{total} Arbeitspakete abgeschlossen" if total else "Fortschritt: keine Arbeitspakete vorhanden"
    if progress_placeholder is None:
        st.progress(progress / 100 if total else 0.0, text=text)
    else:
        progress_placeholder.progress(progress / 100 if total else 0.0, text=text)


def _render_stage1_snapshot(graph_state: dict[str, Any], section_title: str = "Arbeitspakete") -> None:
    task_packages = graph_state.get("task_packages", [])
    st.subheader(section_title)
    _render_task_table(task_packages)
    _render_progress(task_packages)

    col1, col2, col3 = st.columns(3)
    completed, total, progress = _calculate_progress(task_packages)
    diagnostics = graph_state.get("diagnostics") or {}
    web = diagnostics.get("web_search") or {}
    with col1:
        st.metric("Abgeschlossen", f"{completed}/{total}" if total else "0/0")
    with col2:
        st.metric("Fortschritt", f"{progress}%")
    with col3:
        st.metric("Web-Quellen", str(int(web.get("source_count", 0) or 0)))

    st.subheader("🔎 Online-Suche Status")
    _render_web_search_status(graph_state)

    with st.expander("Warum handelt der Agent so? (Selbst-Dokumentation)", expanded=False):
        _render_agent_journal(graph_state.get("agent_journal", []), max_entries=6)


def _render_web_search_status(graph_state: dict[str, Any]) -> None:
    diagnostics = graph_state.get("diagnostics") or {}
    web = diagnostics.get("web_search") or {}
    if not web:
        st.caption("Websuche-Status liegt noch nicht vor.")
        return

    enabled = bool(web.get("enabled", False))
    status = str(web.get("status", "unknown"))
    source_count = int(web.get("source_count", 0) or 0)
    queries = web.get("queries", [])
    message = str(web.get("message", ""))

    if not enabled:
        st.info("Online-Websuche ist deaktiviert.")
    elif status == "ok":
        st.success(f"Online-Websuche aktiv und erfolgreich ({source_count} Quellen).")
    elif status == "no_results":
        st.warning("Online-Websuche aktiv, aber ohne Treffer.")
    elif status == "error":
        st.error(f"Online-Websuche mit Fehler: {message}")
    else:
        st.info("Online-Websuche-Status wird ermittelt.")

    with st.expander("Details zur Online-Suche"):
        if message:
            st.write(message)
        if queries:
            st.markdown("**Ausgefuehrte Suchanfragen:**")
            for query in queries:
                st.markdown(f"- {query}")


def _render_agent_journal(journal: list[dict[str, Any]], max_entries: int = 12) -> None:
    st.subheader("Agenten-Selbst-Dokumentation")
    if not journal:
        st.caption("Noch keine Selbst-Dokumentation vorhanden.")
        return

    entries = journal[-max_entries:]
    for entry in entries:
        agent = entry.get("agent", "Agent")
        action = entry.get("action", "Aktion")
        rationale = entry.get("rationale", "")
        outcome = entry.get("outcome", "")
        with st.container(border=True):
            st.markdown(f"**{agent}: {action}**")
            if rationale:
                st.markdown(f"**Warum:** {rationale}")
            if outcome:
                st.markdown(f"**Ergebnis:** {outcome}")


def _render_venue_cards(venue_options: list[dict]) -> str | None:
    if not venue_options:
        st.info("Noch keine Venue-Optionen vorhanden. Nächster Schritt: Stage 1 erneut mit aktiver Websuche starten.")
        return None

    summary_rows = []
    for i, opt in enumerate(venue_options, start=1):
        summary_rows.append(
            {
                "Nr.": i,
                "Venue": opt.get("name", f"Venue {i}"),
                "Score": int(opt.get("recommendation_score", 0) or 0),
                "Kosten": str(opt.get("estimated_cost", "TBD")),
                "Pros": len(opt.get("pros", [])),
                "Cons": len(opt.get("cons", [])),
            }
        )

    st.dataframe(summary_rows, use_container_width=True)

    options = [v.get("name", f"Venue {i+1}") for i, v in enumerate(venue_options)]
    selected = st.radio("Venue auswählen:", options, key="selected_venue_radio")
    selected_opt = next((opt for opt in venue_options if opt.get("name") == selected), None)

    if selected_opt:
        with st.expander("Ausgewählte Venue im Detail", expanded=True):
            st.markdown(f"### {selected_opt.get('name', '')}")
            st.write(selected_opt.get("description", ""))
            st.markdown(f"**Kosten:** {selected_opt.get('estimated_cost', 'TBD')}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Vorteile**")
                for pro in selected_opt.get("pros", []):
                    st.markdown(f"- {pro}")
            with col2:
                st.markdown("**Nachteile**")
                for con in selected_opt.get("cons", []):
                    st.markdown(f"- {con}")
    return selected


def _render_catering_cards(catering_options: list[dict]) -> str | None:
    if not catering_options:
        st.info("Noch keine Catering-Optionen vorhanden. Nächster Schritt: Stage 1 erneut ausführen oder Suchkriterien anpassen.")
        return None

    summary_rows = []
    for i, opt in enumerate(catering_options, start=1):
        summary_rows.append(
            {
                "Nr.": i,
                "Catering": opt.get("name", f"Caterer {i}"),
                "Score": int(opt.get("recommendation_score", 0) or 0),
                "Kosten": str(opt.get("estimated_cost", "TBD")),
                "Pros": len(opt.get("pros", [])),
                "Cons": len(opt.get("cons", [])),
            }
        )

    st.dataframe(summary_rows, use_container_width=True)

    options = [c.get("name", f"Caterer {i+1}") for i, c in enumerate(catering_options)]
    selected = st.radio("Catering auswählen:", options, key="selected_catering_radio")

    selected_opt = next((opt for opt in catering_options if opt.get("name") == selected), None)
    if selected_opt:
        with st.expander("Ausgewähltes Catering im Detail", expanded=True):
            st.markdown(f"### {selected_opt.get('name', '')}")
            st.write(selected_opt.get("description", ""))
            st.markdown(f"**Kosten:** {selected_opt.get('estimated_cost', 'TBD')}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Vorteile**")
                for pro in selected_opt.get("pros", []):
                    st.markdown(f"- {pro}")
            with col2:
                st.markdown("**Nachteile**")
                for con in selected_opt.get("cons", []):
                    st.markdown(f"- {con}")
    return selected


def _parse_iso_date(value: Any, fallback: date) -> date:
    if isinstance(value, date):
        return value
    if isinstance(value, str) and value.strip():
        try:
            return datetime.strptime(value.strip(), "%Y-%m-%d").date()
        except ValueError:
            return fallback
    return fallback


def _parse_budget(value: Any, fallback: float = 0.0) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        cleaned = value.replace("EUR", "").replace("€", "").replace(".", "").replace(",", ".").strip()
        try:
            return float(cleaned)
        except ValueError:
            return fallback
    return fallback


def _validate_form_input(event_data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not event_data.get("name", "").strip():
        errors.append("Event-Name fehlt.")
    if not event_data.get("city", "").strip():
        errors.append("Stadt fehlt.")
    if not event_data.get("format"):
        errors.append("Mindestens ein Event-Format auswählen.")
    if event_data.get("date_end") < event_data.get("date_start"):
        errors.append("Enddatum muss nach oder gleich dem Startdatum sein.")
    budget = float(event_data.get("budget_total", 0.0) or 0.0)
    if budget <= 0:
        errors.append("Gesamtbudget muss größer als 0 sein.")
    return errors


def _source_trust_label(url: str) -> str:
    lower = url.lower()
    if any(domain in lower for domain in (".gov", ".edu", "stadt", "messe", "kongress")):
        return "Hoch"
    if any(domain in lower for domain in ("wikipedia", "news", "zeit", "heise", "faz", "spiegel")):
        return "Mittel"
    return "Unbekannt"


def _copy_hint(text: str) -> None:
    st.code(text, language="markdown")
    st.caption("Copy-Hinweis: Nutze das Copy-Icon im Codeblock, um den Inhalt direkt zu übernehmen.")


def _render_next_step_hint(message: str) -> None:
    st.info(f"Nächster Schritt: {message}")


def _inject_ui_polish_styles() -> None:
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 1.6rem;
        }
        .ux-step-card {
            border: 1px solid rgba(120, 120, 120, 0.25);
            border-radius: 10px;
            padding: 0.75rem 0.9rem;
            background: rgba(245, 247, 250, 0.55);
        }
        .ux-step-title {
            margin: 0;
            font-size: 0.9rem;
            font-weight: 600;
            opacity: 0.9;
        }
        .ux-step-status {
            margin: 0.2rem 0 0;
            font-size: 1rem;
            font-weight: 700;
        }
        .ux-subtle-note {
            font-size: 0.9rem;
            opacity: 0.8;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_stage_stepper() -> None:
    stage1_status = "✅ Fertig" if st.session_state.get("stage1_done") else ("⏳ Läuft" if st.session_state.get("running") else "1️⃣ Offen")
    stage2_status = "✅ Fertig" if st.session_state.get("stage2_done") else ("⏳ Läuft" if st.session_state.get("running") and st.session_state.get("active_view") == "stage2" else "2️⃣ Ausstehend")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div class="ux-step-card">
              <p class="ux-step-title">Stage 1: Research</p>
              <p class="ux-step-status">Status: {stage1_status}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        if not st.session_state.get("stage1_done"):
            st.markdown(
                """
                <div class="ux-step-card">
                  <p class="ux-step-title">Stage 2: Planung & Content</p>
                  <p class="ux-step-status">Status: 🔒 Gesperrt bis Freigabe</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="ux-step-card">
                  <p class="ux-step-title">Stage 2: Planung & Content</p>
                  <p class="ux-step-status">Status: {stage2_status}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ---------------------------------------------------------------------------
# Sidebar – event configuration form
# ---------------------------------------------------------------------------

def render_sidebar() -> dict[str, Any] | None:
    st.sidebar.title("🎪 Event-Konfiguration")

    config = load_event_config()
    event = config.get("event", {})
    budget_cfg = config.get("budget", {})
    llm_cfg = get_llm_config()

    st.sidebar.caption("1. Event-Basisdaten · 2. KI-Konfiguration · 3. Review & Start")
    st.sidebar.markdown("### 1) Event-Basisdaten")
    event_name = st.sidebar.text_input("Event-Name", value=event.get("name", ""), key="event_name")
    default_start = _parse_iso_date(event.get("date_start", ""), date.today())
    default_end = _parse_iso_date(event.get("date_end", ""), default_start)
    date_start_value = st.sidebar.date_input("Startdatum", value=default_start, format="YYYY-MM-DD", key="event_date_start")
    date_end_value = st.sidebar.date_input("Enddatum", value=default_end, format="YYYY-MM-DD", key="event_date_end")
    if date_end_value < date_start_value:
        st.sidebar.error("Enddatum muss nach oder gleich Startdatum liegen.")

    city = st.sidebar.text_input("Stadt", value=event.get("city", ""), key="event_city")
    attendees = st.sidebar.number_input(
        "Erwartete Teilnehmerzahl",
        min_value=1,
        max_value=10000,
        value=int(event.get("attendees_expected", 125)),
        key="event_attendees",
    )
    budget_total = st.sidebar.number_input(
        "Gesamtbudget (EUR)",
        min_value=0.0,
        step=500.0,
        value=_parse_budget(budget_cfg.get("total_estimated", 0), fallback=10000.0),
        help="Numerischer Wert in EUR.",
        key="event_budget_total",
    )

    format_options = ["Konferenz", "Workshop", "Hackathon", "Meetup", "Webinar", "Hybrid"]
    raw_formats = event.get("format", ["Konferenz"])
    if isinstance(raw_formats, str):
        raw_formats = [raw_formats]

    format_aliases = {
        "Workshops": "Workshop",
        "Konferenzen": "Konferenz",
        "Webinare": "Webinar",
        "Meetups": "Meetup",
    }
    current_formats = [format_aliases.get(fmt, fmt) for fmt in raw_formats]
    valid_defaults = [fmt for fmt in current_formats if fmt in format_options]
    if not valid_defaults:
        valid_defaults = ["Konferenz"]

    selected_formats = st.sidebar.multiselect("Format", format_options, default=valid_defaults, key="event_formats")
    topics_raw = st.sidebar.text_area(
        "Themen (eine pro Zeile)",
        value="\n".join(event.get("topics", [])),
        key="event_topics",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 2) KI-Konfiguration")
    provider_options = ["ollama", "openai", "openai_compatible", "lmstudio", "localai"]
    configured_provider = normalize_llm_provider(str(st.session_state.get("llm_settings", {}).get("provider", llm_cfg.get("provider", "ollama"))))
    if configured_provider not in provider_options:
        configured_provider = "ollama"
    selected_provider = st.sidebar.selectbox(
        "LLM Provider",
        options=provider_options,
        index=provider_options.index(configured_provider),
        key="runtime_provider",
    )
    current_model = str(st.session_state.get("llm_settings", {}).get("model", llm_cfg.get("model", "llama3.2"))).strip() or "llama3.2"
    suggested_base_url = default_llm_base_url(selected_provider)
    selected_base_url = st.sidebar.text_input(
        "Base URL",
        value=str(st.session_state.get("llm_settings", {}).get("base_url", llm_cfg.get("base_url", suggested_base_url))),
        help="Für OpenAI Cloud auf https://api.openai.com/v1 setzen.",
        key="runtime_base_url",
    )
    selected_api_key = st.sidebar.text_input(
        "API Key",
        value=str(st.session_state.get("llm_settings", {}).get("api_key", llm_cfg.get("api_key", "local"))),
        type="password",
        key="runtime_api_key",
    )

    current_context = {
        "provider": selected_provider,
        "base_url": selected_base_url.strip(),
        "api_key": selected_api_key.strip(),
    }
    stored_context = st.session_state.get("available_models_context", {})
    if (
        stored_context.get("provider") != current_context["provider"]
        or stored_context.get("base_url") != current_context["base_url"]
        or stored_context.get("api_key") != current_context["api_key"]
    ):
        st.session_state["available_models"] = [current_model]
        st.session_state["available_models_context"] = current_context

    if st.sidebar.button("🔎 Modellliste prüfen", use_container_width=True, key="check_models_button"):
        models, discovery_error = list_available_models(
            provider=selected_provider,
            base_url=selected_base_url,
            api_key=selected_api_key,
        )
        if models:
            st.session_state["available_models"] = models
            st.session_state["model_discovery_error"] = None
            st.success(f"{len(models)} Modelle gefunden.")
        else:
            st.session_state["available_models"] = [current_model]
            st.session_state["model_discovery_error"] = discovery_error or "Keine Modelle gefunden."
            st.warning("Keine Modelle gefunden. Prüfe Provider, Base URL und API-Key.")
        st.session_state["available_models_context"] = {
            "provider": selected_provider,
            "base_url": selected_base_url.strip(),
            "api_key": selected_api_key.strip(),
        }

    discovery_error = st.session_state.get("model_discovery_error")
    if discovery_error:
        st.sidebar.caption(f"Modellabfrage: {discovery_error}")

    model_options = [m for m in st.session_state.get("available_models", []) if m]
    if not model_options:
        model_options = [current_model]

    if current_model not in model_options:
        model_options.append(current_model)

    selected_model = st.sidebar.selectbox(
        "LLM Modell",
        options=model_options,
        index=model_options.index(current_model) if current_model in model_options else 0,
        help="Nutze 'Modellliste prüfen', um verfügbare Modelle zu laden.",
        key="runtime_model",
    )
    enable_web_search = st.sidebar.checkbox(
        "Online-Websuche für Research aktivieren",
        value=bool(st.session_state.get("llm_settings", {}).get("enable_web_search", True)),
        help="Ergänzt Stage 1 um aktuelle Web-Quellen.",
        key="runtime_enable_web_search",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 3) Review & Start")
    st.sidebar.caption(
        f"{event_name or 'Unbenanntes Event'} · {city or 'Ort fehlt'} · "
        f"{int(attendees)} Teilnehmende · {budget_total:,.0f} EUR"
    )
    submitted = st.sidebar.button("▶ Stage 1 starten (Research)", type="primary", use_container_width=True, key="start_stage1_button")

    if submitted:
        event_payload = {
            "name": event_name,
            "date_start": date_start_value,
            "date_end": date_end_value,
            "city": city,
            "attendees_expected": int(attendees),
            "budget_total": float(budget_total),
            "format": selected_formats,
            "topics": [t.strip() for t in topics_raw.splitlines() if t.strip()],
            "organizer": event.get("organizer", {}),
        }
        validation_errors = _validate_form_input(event_payload)
        if validation_errors:
            st.sidebar.error("Bitte prüfe die Eingaben:")
            for err in validation_errors:
                st.sidebar.markdown(f"- {err}")
            return None

        event_payload["date_start"] = date_start_value.isoformat()
        event_payload["date_end"] = date_end_value.isoformat()

        runtime = {
            "provider": selected_provider,
            "model": selected_model,
            "base_url": selected_base_url,
            "api_key": selected_api_key,
            "enable_web_search": enable_web_search,
        }
        st.session_state["llm_settings"] = runtime

        return {
            "event": event_payload,
            "runtime": runtime,
        }
    return None


# ---------------------------------------------------------------------------
# Stage 1 – Research tab
# ---------------------------------------------------------------------------

def render_stage1_tab() -> None:
    st.header("📍 Stage 1: Research & Optionen")
    st.caption("Ziel: Optionen recherchieren, vergleichen und für Stage 2 freigeben.")

    graph_state = st.session_state.get("graph_state")

    if st.session_state.get("running") and not st.session_state.get("stage1_done"):
        _run_stage1_live_execution()
        return

    if not st.session_state.get("stage1_done") and graph_state is None:
        _render_next_step_hint("Sidebar vollständig ausfüllen und Stage 1 starten.")
        return

    if graph_state is None:
        _render_next_step_hint("Stage 1 erneut starten.")
        return

    if st.session_state.get("stage1_done") and not st.session_state.get("stage2_done"):
        st.success("Stage 1 abgeschlossen. Prüfe Venue/Catering und starte danach Stage 2.")
        if st.button("➡️ Zur Stage 2 Ansicht wechseln", key="switch_to_stage2_btn"):
            st.session_state["requested_view"] = "stage2"
            st.rerun()

    _render_stage1_snapshot(graph_state)
    st.divider()

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

    web_sources = research.get("web_sources", [])
    if web_sources:
        with st.expander("🌐 Verwendete Web-Quellen"):
            for idx, source in enumerate(web_sources, 1):
                title = source.get("title", "Quelle")
                url = source.get("url", "")
                snippet = source.get("snippet", "")
                timestamp = source.get("retrieved_at") or source.get("timestamp") or "unbekannt"
                trust = _source_trust_label(url)
                st.markdown(f"**{idx}. {title}** · Vertrauen: {trust}")
                st.caption(f"Zeitstempel: {timestamp}")
                if url:
                    st.link_button(f"Quelle öffnen ({idx})", url=url)
                    st.caption(url)
                if snippet:
                    st.caption(snippet)

    if graph_state.get("next_step"):
        _render_next_step_hint(str(graph_state.get("next_step")))

    # Approval notes
    notes = st.text_area("Anmerkungen zur Auswahl (optional)", key="approval_notes")

    col1, col2 = st.columns(2)
    with col1:
        can_approve = bool(selected_venue and selected_catering)
        if st.button("✅ Freigeben & Stage 2 starten", type="primary", disabled=not can_approve):
            _approve_and_start_stage2(selected_venue, selected_catering, notes)
    with col2:
        if not st.session_state.get("confirm_cancel"):
            if st.button("❌ Abbrechen", key="cancel_trigger_btn"):
                st.session_state["confirm_cancel"] = True
                st.rerun()
        else:
            st.warning("Abbrechen beendet den Workflow und verwirft den aktuellen Fortschritt.")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("Ja, endgültig abbrechen", key="cancel_confirm_btn"):
                    st.session_state["confirm_cancel"] = False
                    _cancel_workflow()
            with c2:
                if st.button("Nein, weiter", key="cancel_keep_btn"):
                    st.session_state["confirm_cancel"] = False
                    st.rerun()

    if not (selected_venue and selected_catering):
        st.caption("Bitte Venue und Catering auswählen, um Stage 2 zu starten.")

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

    st.session_state["active_view"] = "stage2"
    st.session_state["requested_view"] = "stage2"
    st.session_state["running"] = True
    st.session_state["stage2_done"] = False
    _apply_llm_runtime_config(st.session_state.get("llm_settings", {}))
    st.rerun()


def _run_stage1_live_execution() -> None:
    workflow = get_workflow()
    config = st.session_state.get("workflow_config")
    initial_state = st.session_state.get("pending_initial_state")

    if config is None or initial_state is None:
        st.error("Stage 1 konnte nicht gestartet werden: fehlende Workflow-Konfiguration.")
        st.session_state["running"] = False
        return

    live_state: dict[str, Any] = {}
    status_placeholder = st.empty()
    state_placeholder = st.empty()

    status_placeholder.info("Stage 1 läuft: Der Research-Agent analysiert Venue- und Catering-Optionen.")

    for chunk in workflow.stream(initial_state, config=config, stream_mode="updates"):
        update = _extract_stream_update(chunk)
        if update:
            live_state = _merge_state(live_state, update)
            st.session_state["graph_state"] = live_state

        current_step = live_state.get("next_step", "Recherche wird ausgeführt")
        status_placeholder.info(f"Aktueller Schritt: {current_step}")
        with state_placeholder.container():
            _render_stage1_snapshot(live_state, section_title="Arbeitspakete (Live)")

    st.session_state["graph_state"] = live_state
    st.session_state["stage1_done"] = live_state.get("status") in ("waiting_for_user", "completed")
    st.session_state["current_stage"] = 1
    st.session_state["running"] = False
    st.session_state["pending_initial_state"] = None

    if live_state.get("error"):
        st.error(f"Stage 1 mit Fehler beendet: {live_state.get('error')}")
    else:
        status_placeholder.success("Stage 1 abgeschlossen. Bitte Auswahl treffen und Stage 2 freigeben.")


def _run_stage2_live_execution() -> None:
    workflow = get_workflow()
    config = st.session_state.get("workflow_config")
    if config is None:
        st.error("Kein aktiver Workflow-Thread gefunden.")
        st.session_state["running"] = False
        return

    live_state = dict(st.session_state.get("graph_state") or {})
    progress_placeholder = st.empty()
    status_placeholder = st.empty()
    tasks_placeholder = st.empty()
    journal_placeholder = st.empty()

    status_placeholder.info("Stage 2 läuft: Planungs- und Content-Agent arbeiten.")
    _render_progress(live_state.get("task_packages", []), progress_placeholder)

    for chunk in workflow.stream(None, config=config, stream_mode="updates"):
        update = _extract_stream_update(chunk)
        if update:
            live_state = _merge_state(live_state, update)
            st.session_state["graph_state"] = live_state

        with tasks_placeholder.container():
            st.subheader("Arbeitspakete (Live)")
            _render_task_table(live_state.get("task_packages", []))

        with journal_placeholder.container():
            _render_agent_journal(live_state.get("agent_journal", []), max_entries=6)

        _render_progress(live_state.get("task_packages", []), progress_placeholder)
        next_step = live_state.get("next_step", "")
        if next_step:
            status_placeholder.info(f"Aktueller Schritt: {next_step}")

    st.session_state["graph_state"] = live_state
    st.session_state["stage2_done"] = live_state.get("status") == "completed"
    st.session_state["running"] = False

    if live_state.get("error"):
        st.error(f"Stage 2 mit Fehler beendet: {live_state.get('error')}")
    else:
        st.success("Stage 2 abgeschlossen!")


def _cancel_workflow() -> None:
    workflow = get_workflow()
    config = st.session_state.get("workflow_config")
    if config:
        workflow.update_state(config, {"status": "cancelled"})
        workflow.invoke(None, config=config)
    st.session_state["graph_state"] = None
    st.session_state["stage1_done"] = False
    st.session_state["stage2_done"] = False
    st.session_state["running"] = False
    st.session_state["pending_initial_state"] = None
    st.session_state["active_view"] = "stage1"
    st.session_state["requested_view"] = "stage1"
    st.warning("Planung abgebrochen.")
    st.rerun()


# ---------------------------------------------------------------------------
# Stage 2 – Planning & Content tab
# ---------------------------------------------------------------------------

def render_stage2_tab() -> None:
    st.header("📋 Stage 2: Planung & Content")
    st.caption("Ziel: Agenda, Budget und Kommunikationsartefakte final ausarbeiten.")

    if st.session_state.get("running") and not st.session_state.get("stage2_done"):
        _run_stage2_live_execution()
        return

    if not st.session_state.get("stage2_done"):
        _render_next_step_hint("In Stage 1 Venue und Catering freigeben.")
        return

    graph_state = st.session_state.get("graph_state") or {}

    st.subheader("Arbeitspakete")
    _render_task_table(graph_state.get("task_packages", []))
    _render_progress(graph_state.get("task_packages", []))
    st.divider()

    with st.expander("Warum handelt der Agent so? (Selbst-Dokumentation)", expanded=True):
        _render_agent_journal(graph_state.get("agent_journal", []))

    # Planning + content outputs
    planning = graph_state.get("planning_output") or {}
    content = graph_state.get("content_output") or {}
    if planning or content:
        tab_agenda, tab_budget, tab_email, tab_social, tab_pr = st.tabs([
            "Agenda",
            "Budget",
            "E-Mail",
            "Social",
            "Presse",
        ])

        with tab_agenda:
            schedule = planning.get("schedule", {})
            if schedule:
                for day_key in sorted(schedule.keys()):
                    day = schedule[day_key]
                    with st.expander(f"{day.get('date', day_key)} – {day.get('theme', '')}"):
                        agenda_lines = []
                        for slot in day.get("slots", []):
                            line = f"{slot.get('time', '')} – {slot.get('activity', '')}"
                            agenda_lines.append(line)
                            st.write(f"**{slot.get('time', '')}** – {slot.get('activity', '')}")
                        if agenda_lines:
                            _copy_hint("\n".join(agenda_lines))
            else:
                st.info("Noch keine Agenda vorhanden.")

        with tab_budget:
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
                st.download_button(
                    label="⬇️ Budget als JSON herunterladen",
                    data=json.dumps(budget, ensure_ascii=False, indent=2),
                    file_name="budget-entwurf.json",
                    mime="application/json",
                    key="download_budget_json",
                )
            else:
                st.info("Noch kein Budget-Entwurf vorhanden.")

        with tab_email:
            email = content.get("invitation_email", {})
            if email:
                st.markdown(f"**Betreff:** {email.get('subject', '')}")
                body = email.get("body", "")
                _copy_hint(body)
                st.download_button(
                    label="⬇️ Einladungs-E-Mail als Text herunterladen",
                    data=body,
                    file_name="einladung.txt",
                    mime="text/plain",
                    key="download_email_txt",
                )
            else:
                st.info("Noch keine Einladungs-E-Mail vorhanden.")

        with tab_social:
            posts = content.get("social_media_posts", {})
            _platform_labels = {
                "x_twitter": "X (ehemals Twitter)",
                "linkedin": "LinkedIn",
                "instagram": "Instagram",
                "facebook": "Facebook",
                "mastodon": "Mastodon",
            }
            if posts:
                for platform, text in posts.items():
                    label = _platform_labels.get(platform, platform.replace("_", " ").title())
                    st.markdown(f"**{label}**")
                    _copy_hint(text)
                st.download_button(
                    label="⬇️ Social-Posts als JSON herunterladen",
                    data=json.dumps(posts, ensure_ascii=False, indent=2),
                    file_name="social-posts.json",
                    mime="application/json",
                    key="download_social_json",
                )
            else:
                st.info("Noch keine Social-Media-Posts vorhanden.")

        with tab_pr:
            pr = content.get("press_release", {})
            if pr:
                headline = pr.get("headline", "")
                subheadline = pr.get("subheadline", "")
                body = pr.get("body", "")
                st.markdown(f"## {headline}")
                st.markdown(f"*{subheadline}*")
                _copy_hint(body)
                st.download_button(
                    label="⬇️ Pressemitteilung als Text herunterladen",
                    data=f"{headline}\n\n{subheadline}\n\n{body}",
                    file_name="pressemitteilung.txt",
                    mime="text/plain",
                    key="download_pr_txt",
                )
            else:
                st.info("Noch keine Pressemitteilung vorhanden.")

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
    _inject_ui_polish_styles()

    st.title("🎪 Event-Management Orchestrator")
    st.caption("KI-gestütztes Multi-Agenten-System für vollautomatische Event-Planung")
    _render_stage_stepper()

    # Sidebar form handling
    form_data = render_sidebar()

    if form_data is not None:
        # User clicked "Start Stage 1"
        thread_config = create_thread()
        st.session_state["thread_id"] = thread_config["configurable"]["thread_id"]
        st.session_state["workflow_config"] = thread_config
        st.session_state["stage1_done"] = False
        st.session_state["stage2_done"] = False
        st.session_state["running"] = True
        st.session_state["active_view"] = "stage1"
        st.session_state["requested_view"] = "stage1"
        st.session_state["graph_state"] = None

        runtime_settings = form_data.get("runtime", {})
        if runtime_settings:
            _apply_llm_runtime_config(runtime_settings)

        initial_state = _build_initial_state(form_data)
        st.session_state["pending_initial_state"] = initial_state
        st.session_state["graph_state"] = None
        st.rerun()

    requested_view = st.session_state.get("requested_view")
    if requested_view == "stage1":
        st.session_state["view_selector"] = "📍 Stage 1: Research"
    elif requested_view == "stage2":
        st.session_state["view_selector"] = "📋 Stage 2: Planung & Content"
    st.session_state["requested_view"] = None

    selected_view = st.radio(
        "Ansicht",
        options=["📍 Stage 1: Research", "📋 Stage 2: Planung & Content"],
        key="view_selector",
        horizontal=True,
    )

    if selected_view == "📋 Stage 2: Planung & Content" and not st.session_state.get("stage1_done"):
        st.warning("Stage 2 ist noch gesperrt. Bitte zuerst Stage 1 abschließen und freigeben.")
        st.session_state["view_selector"] = "📍 Stage 1: Research"
        selected_view = "📍 Stage 1: Research"

    if selected_view == "📍 Stage 1: Research":
        st.session_state["active_view"] = "stage1"
        render_stage1_tab()
    else:
        st.session_state["active_view"] = "stage2"
        render_stage2_tab()


if __name__ == "__main__":
    main()
