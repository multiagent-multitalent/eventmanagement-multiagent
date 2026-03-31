# LangChain / LangGraph – Python AI Agent Framework

## Überblick

**LangChain** ist das meistgenutzte Python-Framework zum Erstellen von LLM-Applikationen. **LangGraph** baut darauf auf und ermöglicht zustandsbehaftete, zyklische Multi-Agenten-Workflows – ideal für komplexe Planungsprozesse.

| Eigenschaft | LangChain | LangGraph |
|---|---|---|
| **Website** | https://python.langchain.com | https://langchain-ai.github.io/langgraph/ |
| **GitHub** | https://github.com/langchain-ai/langchain | https://github.com/langchain-ai/langgraph |
| **Lizenz** | MIT | MIT |
| **Programmiersprache** | Python | Python |
| **GitHub-Sterne** | ~100.000+ | ~10.000+ |
| **Lokale Installation** | ✅ pip | ✅ pip |
| **Visuelle Oberfläche** | ❌ (nur Code) | ⚠️ LangGraph Studio (Beta) |
| **Multi-Agenten** | ⚠️ (mit Chains) | ✅ nativ |
| **Lokale LLMs** | ✅ | ✅ |

---

## Stärken für Eventplanung

- **Maximale Flexibilität**: Agenten-Logik exakt wie gewünscht implementierbar
- **Zustandsbehaftete Workflows**: LangGraph speichert den aktuellen Planungsstand
- **Human-in-the-Loop**: Unterbrechungspunkte für menschliche Genehmigungen
- **Tool-Calling**: Agenten können eigene Funktionen aufrufen (Dateioperationen, APIs)
- **Streaming**: Echtzeit-Ausgabe während der Verarbeitung
- **LangSmith**: Optionales Tracing & Debugging (auch Self-hosted)

---

## Installation

```bash
pip install langchain langgraph langchain-community langchain-openai
```

---

## Anbindung an lokale KI-Modelle

### Ollama (empfohlen)

```python
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",
    temperature=0.1,
)
```

### OpenAI-kompatibler Endpunkt (LocalAI, vLLM, LM Studio)

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="mistral",
    base_url="http://localhost:8080/v1",  # LocalAI
    api_key="local",  # Platzhalter-Key
    temperature=0.1,
)
```

---

## Beispiel: LangGraph Multi-Agenten Workflow für Eventplanung

### Architektur

```
event.yaml
    │
    ▼
[Orchestrator Agent]
    ├─→ [Programm Agent]      # CfP, Agenda, Speaker
    ├─→ [Kommunikation Agent] # Social Media, Newsletter
    ├─→ [Operations Agent]    # Checklisten, Logistik
    └─→ [Koordination Agent]  # Dashboard, Status
         │
         ▼
    [Human Review Node]
         │
         ▼
    [Ausgabe / workstreams/]
```

### Minimalbeispiel (LangGraph)

```python
import yaml
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOllama

# Zustand des Workflows
class EventPlanningState(TypedDict):
    event_config: dict
    programm_draft: str
    kommunikation_draft: str
    review_required: bool
    final_output: dict

# LLM laden
llm = ChatOllama(model="llama3.2", base_url="http://localhost:11434")

# Agenten-Knoten
def programm_agent(state: EventPlanningState) -> EventPlanningState:
    config = state["event_config"]
    prompt = f"""
    Erstelle ein Programmentwurf für das Event:
    Name: {config['event']['name']}
    Datum: {config['event']['date_start']} bis {config['event']['date_end']}
    Format: {config['event']['format']}
    Themen: {config['event']['topics']}
    """
    response = llm.invoke(prompt)
    return {**state, "programm_draft": response.content}

def kommunikation_agent(state: EventPlanningState) -> EventPlanningState:
    config = state["event_config"]
    response = llm.invoke(
        f"Erstelle einen Kommunikationsplan für {config['event']['name']}."
    )
    return {**state, "kommunikation_draft": response.content}

def human_review(state: EventPlanningState) -> EventPlanningState:
    # Unterbrechungspunkt für menschliche Überprüfung
    return {**state, "review_required": True}

# Graph aufbauen
workflow = StateGraph(EventPlanningState)
workflow.add_node("programm", programm_agent)
workflow.add_node("kommunikation", kommunikation_agent)
workflow.add_node("review", human_review)

workflow.set_entry_point("programm")
workflow.add_edge("programm", "kommunikation")
workflow.add_edge("kommunikation", "review")
workflow.add_edge("review", END)

app = workflow.compile(interrupt_before=["review"])  # Human-in-the-Loop

# Ausführen
with open("config/event.yaml") as f:
    event_config = yaml.safe_load(f)

result = app.invoke({"event_config": event_config, "review_required": False})
print(result["programm_draft"])
```

---

## Projektstruktur für Eventplanung

```
event-planning-agents/
├── config/
│   └── event.yaml              # Aus dem Hauptprojekt
├── agents/
│   ├── orchestrator.py         # Koordiniert alle Agenten
│   ├── programm_agent.py       # CfP, Agenda, Speaker
│   ├── kommunikation_agent.py  # Social Media, Newsletter
│   ├── operations_agent.py     # Checklisten, Logistik
│   └── koordination_agent.py  # Dashboard, Status
├── tools/
│   ├── file_tools.py           # Dateien lesen/schreiben
│   ├── calendar_tools.py       # Kalender-Operationen
│   └── email_tools.py          # E-Mail-Versand
├── workflows/
│   └── event_planning_graph.py # LangGraph-Workflow-Definition
├── outputs/                    # Generierte Artefakte
├── requirements.txt
└── main.py                     # Einstiegspunkt
```

---

## Reproduzierbarkeit

```python
# Deterministischer Seed für reproduzierbare Ausgaben
llm = ChatOllama(model="llama3.2", temperature=0.0, seed=42)

# Workflow-State als Checkpoint speichern (LangGraph)
from langgraph.checkpoint.sqlite import SqliteSaver
memory = SqliteSaver.from_conn_string("checkpoints/event_planning.sqlite")
app = workflow.compile(checkpointer=memory)
```

---

## Observability mit LangSmith (Self-hosted)

```bash
# LangSmith selbst hosten
docker run -p 1984:1984 langchain/langsmith-backend:latest
```

```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "http://localhost:1984"
os.environ["LANGCHAIN_API_KEY"] = "local"
```

---

## requirements.txt

```
langchain>=0.3.0
langgraph>=0.2.0
langchain-community>=0.3.0
langchain-openai>=0.2.0
pyyaml>=6.0
python-dotenv>=1.0
```

---

## Fazit

LangGraph ist die **beste Wahl für technische Teams**, die maximale Kontrolle über ihre Agenten-Logik benötigen. Die Graph-basierte Architektur spiegelt das bestehende Agenten-Modell (Orchestrator + 5 Fachagenten) direkt wider.

**→ Ideal für:** Komplexe, zustandsbehaftete Multi-Agenten-Workflows, Reproduzierbarkeit durch Code, Integration mit bestehenden Python-Systemen.
