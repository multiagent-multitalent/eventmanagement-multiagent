# AutoGen – Multi-Agent Conversation Framework

## Überblick

**AutoGen** (von Microsoft Research) ist ein Python-Framework für konversationsbasierte Multi-Agenten-Systeme. Agenten können miteinander kommunizieren, Tools ausführen und komplexe Aufgaben durch Zusammenarbeit lösen.

| Eigenschaft | Wert |
|---|---|
| **Website** | https://microsoft.github.io/autogen/ |
| **GitHub** | https://github.com/microsoft/autogen |
| **Lizenz** | MIT |
| **Programmiersprache** | Python |
| **GitHub-Sterne** | ~35.000+ |
| **Lokale Installation** | ✅ pip |
| **Visuelle Oberfläche** | ⚠️ AutoGen Studio (separates Tool) |
| **Multi-Agenten** | ✅ Kernfeature |
| **Lokale LLMs** | ✅ OpenAI-kompatibler Endpunkt |

---

## Stärken für Eventplanung

- **Natürliche Agenten-Konversation**: Agenten diskutieren Probleme wie ein echtes Team
- **Rollenbasierte Agenten**: Jeder Agent hat eine spezifische Persona und Expertise
- **Code-Ausführung**: Agenten können Python-Code schreiben und ausführen lassen
- **Human Proxy Agent**: Mensch kann jederzeit in Konversation eingreifen
- **Gruppenkonversation**: Mehrere Agenten lösen eine Aufgabe gemeinsam

---

## Installation

```bash
pip install pyautogen
# oder neue Version:
pip install autogen-agentchat autogen-ext[openai]
```

---

## Anbindung an lokale KI-Modelle

### Ollama (empfohlen)

```python
import autogen

config_list = [
    {
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",  # Platzhalter
        "api_type": "openai",
    }
]

llm_config = {
    "config_list": config_list,
    "temperature": 0.1,
    "seed": 42,  # Reproduzierbarkeit
}
```

### LocalAI / vLLM / LM Studio

```python
config_list = [
    {
        "model": "mistral-7b",
        "base_url": "http://localhost:8080/v1",  # LocalAI
        "api_key": "local",
        "api_type": "openai",
    }
]
```

### OAI_CONFIG_LIST (JSON-Datei für Reproduzierbarkeit)

```json
[
  {
    "model": "llama3.2",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama",
    "api_type": "openai"
  }
]
```

```python
config_list = autogen.config_list_from_json("OAI_CONFIG_LIST")
```

---

## Beispiel: Eventplanungs-Team mit AutoGen

```python
import autogen
import yaml

# Event-Konfiguration laden
with open("config/event.yaml") as f:
    event_config = yaml.safe_load(f)

event_name = event_config["event"]["name"]
event_date = f"{event_config['event']['date_start']} bis {event_config['event']['date_end']}"

# LLM Konfiguration
llm_config = {
    "config_list": [{
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
    }],
    "temperature": 0.1,
    "seed": 42,
}

# Agenten definieren
orchestrator = autogen.AssistantAgent(
    name="Orchestrator",
    system_message=f"""Du bist der Orchestrator für {event_name}.
    Du koordinierst alle Planungsaktivitäten und verteilst Aufgaben.
    Event: {event_name}, Datum: {event_date}, Ort: Nürnberg.
    Antworte immer auf Deutsch.""",
    llm_config=llm_config,
)

programm_agent = autogen.AssistantAgent(
    name="ProgrammAgent",
    system_message=f"""Du bist der Programm-Agent für {event_name}.
    Deine Aufgaben: CfP erstellen, Agenda planen, Speaker koordinieren.
    Themen: AI Transparency, AI Safety, AI Governance, Human Compatible AI.
    Antworte immer auf Deutsch.""",
    llm_config=llm_config,
)

kommunikation_agent = autogen.AssistantAgent(
    name="KommunikationAgent",
    system_message=f"""Du bist der Kommunikations-Agent für {event_name}.
    Deine Aufgaben: Social Media, Newsletter, Pressemitteilungen, E-Mails.
    Antworte immer auf Deutsch.""",
    llm_config=llm_config,
)

# Human Proxy (für Human-in-the-Loop)
human_proxy = autogen.UserProxyAgent(
    name="EventPlanner",
    human_input_mode="TERMINATE",  # Fragt nach, bevor er beendet
    max_consecutive_auto_reply=5,
    code_execution_config={
        "work_dir": "outputs",
        "use_docker": False,
    },
)

# Gruppenkonversation
groupchat = autogen.GroupChat(
    agents=[human_proxy, orchestrator, programm_agent, kommunikation_agent],
    messages=[],
    max_round=20,
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Workflow starten
human_proxy.initiate_chat(
    manager,
    message=f"""
    Wir planen {event_name} vom {event_date} in Nürnberg.
    Erwartete Teilnehmer: {event_config['event']['attendees_expected']}
    Format: {event_config['event']['format']}
    
    Aufgaben für diese Sitzung:
    1. CfP-Vorlage erstellen (Programm-Agent)
    2. Social-Media-Ankündigung verfassen (Kommunikations-Agent)
    3. Nächste Meilensteine definieren (Orchestrator)
    """
)
```

---

## Reproduzierbarkeit

```python
# Deterministischer Seed für reproduzierbare Ergebnisse
llm_config = {
    "seed": 42,
    "temperature": 0.0,
    ...
}

# Konversations-Cache aktivieren
llm_config = {
    "cache_seed": 42,  # Cached Responses für gleiche Prompts
    ...
}

# Konversationsprotokoll speichern
import json
with open("outputs/conversation_log.json", "w") as f:
    json.dump(groupchat.messages, f, ensure_ascii=False, indent=2)
```

---

## AutoGen Studio (visuelle Oberfläche)

```bash
pip install autogenstudio

# Starten
autogenstudio ui --port 8081 --host localhost
# Öffne http://localhost:8081
```

AutoGen Studio ermöglicht:
- Agenten visuell konfigurieren
- Workflows ohne Code erstellen
- Konversationen testen und debuggen

---

## Projektstruktur

```
autogen-event-planning/
├── config/
│   └── event.yaml              # Event-Konfiguration
├── agents/
│   ├── config.py               # LLM-Konfiguration
│   ├── orchestrator.py
│   ├── programm_agent.py
│   ├── kommunikation_agent.py
│   └── operations_agent.py
├── workflows/
│   ├── full_planning.py        # Vollständiger Planungs-Workflow
│   ├── cfp_workflow.py         # Nur CfP-Erstellung
│   └── communication_workflow.py
├── outputs/                    # Generierte Artefakte + Logs
├── OAI_CONFIG_LIST             # LLM-Konfiguration (JSON)
├── requirements.txt
└── main.py
```

---

## Einschränkungen

- Konversationsbasierter Ansatz kann bei langen Workflows unvorhersehbar werden
- Mehr RAM bei großen Konversationsketten benötigt
- Reproduzierbarkeit bei `temperature > 0` eingeschränkt (auch mit `seed`)
- Komplex bei mehr als 5-6 Agenten

---

## Fazit

AutoGen eignet sich hervorragend für **explorative Planungssessions**, bei denen Agenten als virtuelles Team diskutieren und gemeinsam Lösungen erarbeiten. Das natürliche Konversationsmodell spiegelt gut reale Teamdynamiken wider.

**→ Ideal für:** Kollaborative Problemlösung, Brainstorming-Sessions, Planungsworkshops mit KI-Agenten als virtuellem Team.
