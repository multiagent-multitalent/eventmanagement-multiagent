# CrewAI – Multi-Agent Orchestration Framework

## Überblick

**CrewAI** ist ein Python-Framework für die Orchestrierung von KI-Agenten, die wie ein Team zusammenarbeiten. Jeder Agent hat eine klar definierte Rolle, Ziele und Werkzeuge. Das rollenbasierte Modell passt perfekt zum bestehenden Agenten-System dieses Projekts.

| Eigenschaft | Wert |
|---|---|
| **Website** | https://crewai.com |
| **GitHub** | https://github.com/crewAIInc/crewAI |
| **Lizenz** | MIT |
| **Programmiersprache** | Python |
| **GitHub-Sterne** | ~25.000+ |
| **Lokale Installation** | ✅ pip |
| **Visuelle Oberfläche** | ❌ (nur Code / YAML) |
| **Multi-Agenten** | ✅ Kernfeature |
| **Lokale LLMs** | ✅ Ollama, LiteLLM |

---

## Stärken für Eventplanung

- **Rollenbasierte Agenten**: Direkte Entsprechung zu unserem Agenten-Modell
- **YAML-Konfiguration**: Agenten und Tasks in YAML-Dateien definierbar → Git-freundlich
- **Sequentielle & hierarchische Crews**: Flexible Workflow-Struktur
- **Tool-Integration**: Agenten erhalten spezifische Werkzeuge
- **Einfache API**: Sehr wenig Boilerplate-Code
- **Flows**: Neueres Feature für komplexere Zustandsmaschinen

---

## Installation

```bash
pip install crewai crewai-tools

# Neues CrewAI-Projekt erstellen (empfohlen)
crewai create crew aitd-event-planning
cd aitd-event-planning
```

---

## Anbindung an lokale KI-Modelle

### Ollama (empfohlen)

```python
from crewai import LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
)
```

### Über LiteLLM (universell)

```python
from crewai import LLM

# Ollama
llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

# LocalAI
llm = LLM(model="openai/mistral", base_url="http://localhost:8080/v1", api_key="local")

# vLLM
llm = LLM(model="openai/llama3", base_url="http://localhost:8000/v1", api_key="vllm")

# LM Studio
llm = LLM(model="openai/local-model", base_url="http://localhost:1234/v1", api_key="lm-studio")
```

---

## YAML-basierte Konfiguration (empfohlen)

### `config/agents.yaml`

```yaml
orchestrator:
  role: "Event-Orchestrator"
  goal: >
    Koordiniere alle Planungsaktivitäten für die AI Transparency Days 2026
    und stelle sicher, dass alle Arbeitspakete rechtzeitig abgeschlossen werden.
  backstory: >
    Du bist ein erfahrener Eventmanager mit Expertise in Konferenzorganisation
    und KI-Themen. Du behältst den Überblick über alle Workstreams.

programm_agent:
  role: "Programm-Manager"
  goal: >
    Erstelle ein ausgewogenes, hochwertiges Konferenzprogramm mit relevanten
    Themen, renommierten Speakern und ansprechender Agenda.
  backstory: >
    Du bist spezialisiert auf wissenschaftliche Konferenzen und kennst die
    AI-Forschungslandschaft. Du hast bereits mehrere CfP-Prozesse geleitet.

kommunikation_agent:
  role: "Kommunikations-Manager"
  goal: >
    Entwickle und koordiniere die gesamte Außenkommunikation für AITD 2026,
    inklusive Social Media, Newsletter und Pressemitteilungen.
  backstory: >
    Du bist Marketing-Experte mit Fokus auf Wissenschaftskommunikation
    und hast Erfahrung mit der Vermarktung von Fachkonferenzen.

operations_agent:
  role: "Operations-Manager"
  goal: >
    Stelle die reibungslose logistische Durchführung des Events sicher,
    inklusive Venue, Catering, Technik und Personal.
  backstory: >
    Du bist ein detailorientierter Organisationsprofi, der komplexe
    Logistikprozesse koordiniert und keine Deadline vergisst.
```

### `config/tasks.yaml`

```yaml
cfp_erstellen:
  description: >
    Erstelle einen vollständigen Call for Papers (CfP) für {event_name}.
    
    Event-Details:
    - Datum: {date_start} bis {date_end}
    - Ort: {city}
    - Themen: {topics}
    - Zielgruppe: {target_audience}
    - Sprachen: {languages}
    
    Der CfP soll enthalten:
    1. Event-Beschreibung
    2. Themengebiete mit Beispielen
    3. Einreichungsformat und -anforderungen
    4. Wichtige Fristen (basierend auf Meilensteinen)
    5. Kontaktinformationen
  expected_output: >
    Ein vollständiger CfP als Markdown-Dokument, bereit für die Veröffentlichung.
  agent: programm_agent

kommunikationsplan_erstellen:
  description: >
    Erstelle einen detaillierten Kommunikationsplan für {event_name}.
    Berücksichtige alle Kanäle: Social Media, Newsletter, Presse.
    Orientiere dich an den Projektmeilensteinen.
  expected_output: >
    Ein Kommunikationsplan mit Zeitplan, Kanälen und Beispiel-Inhalten.
  agent: kommunikation_agent
  context:
    - cfp_erstellen
```

### `src/aitd_event_planning/crew.py`

```python
import yaml
from pathlib import Path
from crewai import Agent, Crew, Task, Process, LLM
from crewai_tools import FileReadTool, FileWriterTool

# Lokales LLM laden
llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

# Event-Konfiguration laden
with open("config/event.yaml") as f:
    import yaml
    event_config = yaml.safe_load(f)

event = event_config["event"]

# YAML-Konfigurationen laden
with open("config/agents.yaml") as f:
    agents_config = yaml.safe_load(f)

with open("config/tasks.yaml") as f:
    tasks_config = yaml.safe_load(f)

# Tools
file_read = FileReadTool()
file_write = FileWriterTool()

# Agenten erstellen
orchestrator = Agent(
    role=agents_config["orchestrator"]["role"],
    goal=agents_config["orchestrator"]["goal"],
    backstory=agents_config["orchestrator"]["backstory"],
    llm=llm,
    verbose=True,
)

programm_agent = Agent(
    role=agents_config["programm_agent"]["role"],
    goal=agents_config["programm_agent"]["goal"],
    backstory=agents_config["programm_agent"]["backstory"],
    tools=[file_read, file_write],
    llm=llm,
    verbose=True,
)

kommunikation_agent = Agent(
    role=agents_config["kommunikation_agent"]["role"],
    goal=agents_config["kommunikation_agent"]["goal"],
    backstory=agents_config["kommunikation_agent"]["backstory"],
    tools=[file_read, file_write],
    llm=llm,
    verbose=True,
)

# Tasks erstellen
cfp_task = Task(
    description=tasks_config["cfp_erstellen"]["description"].format(
        event_name=event["name"],
        date_start=event["date_start"],
        date_end=event["date_end"],
        city=event["city"],
        topics=", ".join(event["topics"]),
        target_audience=", ".join(event["target_audience"]),
        languages=", ".join(event["languages"]),
    ),
    expected_output=tasks_config["cfp_erstellen"]["expected_output"],
    agent=programm_agent,
    output_file="workstreams/programm/cfp.md",
)

kommunikation_task = Task(
    description=tasks_config["kommunikationsplan_erstellen"]["description"].format(
        event_name=event["name"],
    ),
    expected_output=tasks_config["kommunikationsplan_erstellen"]["expected_output"],
    agent=kommunikation_agent,
    context=[cfp_task],
    output_file="workstreams/kommunikation/kommunikationsplan.md",
)

# Crew zusammenstellen
crew = Crew(
    agents=[orchestrator, programm_agent, kommunikation_agent],
    tasks=[cfp_task, kommunikation_task],
    process=Process.sequential,  # oder Process.hierarchical
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
```

---

## Projektstruktur (CrewAI Standard)

```
aitd-event-planning/
├── config/
│   ├── event.yaml              # Event-Konfiguration (aus Hauptprojekt)
│   ├── agents.yaml             # Agenten-Definitionen
│   └── tasks.yaml              # Task-Definitionen
├── src/
│   └── aitd_event_planning/
│       ├── __init__.py
│       ├── crew.py             # Crew-Definition
│       ├── main.py             # Einstiegspunkt
│       └── tools/
│           ├── __init__.py
│           └── custom_tools.py
├── workstreams/                # Output-Ordner (aus Hauptprojekt)
├── tests/
│   └── test_crew.py
├── pyproject.toml
└── .env                        # Umgebungsvariablen (API-Keys)
```

---

## Reproduzierbarkeit

```python
# Deterministisches LLM
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0.0,
    seed=42,
)

# Ausgaben immer in definierte Dateien schreiben
task = Task(
    ...,
    output_file="workstreams/programm/cfp.md",  # Immer gleicher Pfad
)
```

```bash
# Ausführung versionieren
crewai run > outputs/run_$(date +%Y%m%d_%H%M%S).log
```

---

## Prozessmodelle

```python
# Sequentiell: Task 1 → Task 2 → Task 3
crew = Crew(process=Process.sequential, ...)

# Hierarchisch: Orchestrator koordiniert Agenten
crew = Crew(
    process=Process.hierarchical,
    manager_llm=llm,  # LLM für Manager-Agent
    ...
)
```

---

## Fazit

CrewAI ist die **beste Wahl für dieses Projekt**, weil die rollenbasierte Architektur direkt dem bestehenden Agenten-Modell (Orchestrator + 5 Fachagenten) entspricht. Die YAML-Konfiguration ermöglicht Versionierung und einfache Anpassung.

**→ Ideal für:** Multi-Agenten-Szenarien mit klaren Rollen, YAML-konfigurierbare Workflows, einfacher Einstieg mit gutem Produktions-Potenzial.
