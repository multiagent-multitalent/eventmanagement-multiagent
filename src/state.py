"""TypedDict definition for the shared LangGraph state."""

from typing import Any, Optional
from typing_extensions import TypedDict


class TaskPackage(TypedDict):
    id: str
    agent: str
    task: str
    status: str  # "pending" | "running" | "completed" | "error"
    output: str


class VenueOption(TypedDict):
    name: str
    description: str
    pros: list[str]
    cons: list[str]
    estimated_cost: str
    recommendation_score: int


class CateringOption(TypedDict):
    name: str
    description: str
    pros: list[str]
    cons: list[str]
    estimated_cost: str
    recommendation_score: int


class WebSource(TypedDict):
    title: str
    url: str
    snippet: str


class ResearchResults(TypedDict):
    venue_options: list[VenueOption]
    catering_options: list[CateringOption]
    web_sources: list[WebSource]


class UserDecision(TypedDict):
    selected_venue: str
    selected_catering: str
    notes: str


class AgentJournalEntry(TypedDict):
    agent: str
    phase: str
    action: str
    rationale: str
    outcome: str


class EventPlanningState(TypedDict):
    # Workflow control
    stage: int                        # 1 = research, 2 = planning & content
    status: str                       # "running" | "waiting_for_user" | "approved" | "completed" | "cancelled" | "error"

    # Input data
    event_data: dict[str, Any]        # Contents of config/event.yaml

    # Workpackage tracking (all agents append here)
    task_packages: list[TaskPackage]

    # Stage 1 outputs
    research_results: Optional[ResearchResults]

    # Human gate
    user_decision: Optional[UserDecision]

    # Stage 2 outputs
    planning_output: Optional[dict[str, Any]]
    content_output: Optional[dict[str, Any]]

    # Runtime diagnostics and self-documentation
    diagnostics: Optional[dict[str, Any]]
    agent_journal: list[AgentJournalEntry]

    # UI helpers
    next_step: str
    error: Optional[str]
