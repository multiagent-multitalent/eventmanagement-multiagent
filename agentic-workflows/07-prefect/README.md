# Prefect – Workflow Orchestration

## Überblick

**Prefect** ist ein Open-Source-Workflow-Orchestrierungsframework für Python. Es eignet sich besonders für datenintensive Pipelines, zeitgesteuerte Aufgaben und Workflows, bei denen Zuverlässigkeit, Retry-Logik und Observability entscheidend sind.

| Eigenschaft | Wert |
|---|---|
| **Website** | https://www.prefect.io |
| **GitHub** | https://github.com/PrefectHQ/prefect |
| **Lizenz** | Apache 2.0 |
| **Programmiersprache** | Python |
| **GitHub-Sterne** | ~16.000+ |
| **Lokale Installation** | ✅ pip + Prefect Server |
| **Visuelle Oberfläche** | ✅ Prefect UI (Web-Dashboard) |
| **Multi-Agenten** | ⚠️ Möglich über Tasks + LLM-Integrationen |
| **Lokale LLMs** | ✅ Über LangChain, direkte API-Calls |

---

## Stärken für Eventplanung

- **Robustheit**: Retry-Logik, Fehlerbehandlung, Timeouts automatisch
- **Zeitplanung**: Schedules (Cron, Intervall) für regelmäßige Aufgaben
- **Observability**: Dashboard mit Run-Historie, Logs, Alerts
- **Parallelisierung**: Tasks parallel ausführen
- **Parametrierung**: Workflows mit unterschiedlichen Inputs ausführen
- **Caching**: Ergebnisse cachen, um unnötige Wiederholungen zu vermeiden

---

## Installation

```bash
pip install prefect

# Lokalen Prefect-Server starten
prefect server start
# Öffne http://localhost:4200
```

---

## Anbindung an lokale KI-Modelle

```python
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

# Ollama
def get_llm():
    return ChatOllama(
        model="llama3.2",
        base_url="http://localhost:11434",
        temperature=0.1,
    )

# LocalAI / OpenAI-kompatibel
def get_llm_localai():
    return ChatOpenAI(
        model="mistral",
        base_url="http://localhost:8080/v1",
        api_key="local",
    )
```

---

## Beispiel: Prefect Workflow für Eventplanung

```python
import yaml
from pathlib import Path
from datetime import datetime
from prefect import flow, task
from prefect.tasks import task_input_hash
from langchain_community.chat_models import ChatOllama

# LLM (einmal instanziieren)
llm = ChatOllama(model="llama3.2", base_url="http://localhost:11434")

# Event-Konfiguration laden
@task(name="Event-Konfiguration laden", retries=2)
def load_event_config(config_path: str = "config/event.yaml") -> dict:
    with open(config_path) as f:
        return yaml.safe_load(f)

# CfP generieren (mit Caching)
@task(
    name="CfP generieren",
    cache_key_fn=task_input_hash,
    cache_expiration=None,  # Unbegrenzt cachen
    retries=3,
    retry_delay_seconds=30,
)
def generate_cfp(event_config: dict) -> str:
    event = event_config["event"]
    prompt = f"""
    Erstelle einen Call for Papers (CfP) für:
    Name: {event['name']}
    Datum: {event['date_start']} bis {event['date_end']}
    Ort: {event['city']}
    Themen: {', '.join(event['topics'])}
    Zielgruppe: {', '.join(event['target_audience'])}
    
    Erstelle einen vollständigen, professionellen CfP auf Deutsch.
    """
    response = llm.invoke(prompt)
    return response.content

# Speaker-Briefing generieren
@task(name="Speaker-Briefing generieren", retries=2)
def generate_speaker_briefing(speaker: dict, event_config: dict) -> str:
    prompt = f"""
    Erstelle ein Speaker-Briefing für {speaker['name']}.
    Thema: {speaker.get('topic', 'KI und Transparenz')}
    Event: {event_config['event']['name']}
    Datum: {event_config['event']['date_start']}
    """
    response = llm.invoke(prompt)
    return response.content

# Ergebnisse in Workstream-Ordner speichern
@task(name="Artefakt speichern")
def save_artifact(content: str, output_path: str) -> str:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(content, encoding="utf-8")
    return output_path

# Kommunikationsplan erstellen
@task(name="Kommunikationsplan erstellen", retries=2)
def generate_kommunikationsplan(event_config: dict, cfp_content: str) -> str:
    prompt = f"""
    Erstelle einen Kommunikationsplan für {event_config['event']['name']}.
    Berücksichtige den folgenden CfP:
    {cfp_content[:500]}...
    
    Der Plan soll folgende Kanäle umfassen:
    - LinkedIn
    - Twitter/X
    - Newsletter
    - Pressemitteilung
    
    Erstelle konkrete Zeitplanung und Beispiel-Posts.
    """
    response = llm.invoke(prompt)
    return response.content

# Haupt-Flow
@flow(
    name="AITD 2026 Planungs-Workflow",
    log_prints=True,
)
def event_planning_flow(
    config_path: str = "config/event.yaml",
    output_dir: str = "workstreams",
    run_cfp: bool = True,
    run_kommunikation: bool = True,
):
    """
    Hauptworkflow für die Eventplanung.
    Generiert alle Planungsartefakte aus der Event-Konfiguration.
    """
    print(f"Starte Planungs-Workflow: {datetime.now().isoformat()}")
    
    # Schritt 1: Konfiguration laden
    event_config = load_event_config(config_path)
    print(f"Event: {event_config['event']['name']}")
    
    results = {}
    
    # Schritt 2: CfP generieren
    if run_cfp:
        cfp = generate_cfp(event_config)
        save_artifact(cfp, f"{output_dir}/programm/cfp.md")
        results["cfp"] = cfp
        print("✅ CfP generiert")
    
    # Schritt 3: Kommunikationsplan (abhängig von CfP)
    if run_kommunikation and run_cfp:
        komm_plan = generate_kommunikationsplan(event_config, results.get("cfp", ""))
        save_artifact(komm_plan, f"{output_dir}/kommunikation/kommunikationsplan.md")
        print("✅ Kommunikationsplan generiert")
    
    print("Planungs-Workflow abgeschlossen.")
    return results

if __name__ == "__main__":
    event_planning_flow()
```

---

## Zeitgesteuerte Ausführung (Schedule)

```python
from prefect.schedules import CronSchedule

# Jeden Montag um 8 Uhr Status-Update generieren
@flow(schedule=CronSchedule(cron="0 8 * * 1"))
def weekly_status_update():
    event_config = load_event_config()
    # Status-Bericht generieren...

# Deployment erstellen
if __name__ == "__main__":
    weekly_status_update.serve(name="Weekly Status Update")
```

---

## Parallele Task-Ausführung

```python
from prefect import flow, task
from prefect.futures import wait

@flow(name="Parallele Artefakt-Generierung")
def parallel_artifacts_flow():
    event_config = load_event_config()
    
    # Parallel starten (nicht auf Ergebnis warten)
    cfp_future = generate_cfp.submit(event_config)
    
    # Auf beide warten
    cfp = cfp_future.result()
    
    # Jetzt abhängige Tasks
    komm_plan = generate_kommunikationsplan(event_config, cfp)
    
    return {"cfp": cfp, "kommunikationsplan": komm_plan}
```

---

## Prefect Server lokal betreiben

```bash
# Server starten (persistente Datenbank)
prefect server start --host 0.0.0.0

# In .env setzen
echo "PREFECT_API_URL=http://localhost:4200/api" >> .env
```

### docker-compose.yml

```yaml
version: "3.8"

services:
  prefect:
    image: prefecthq/prefect:3-latest
    restart: unless-stopped
    ports:
      - "4200:4200"
    command: prefect server start --host 0.0.0.0
    volumes:
      - prefect_data:/root/.prefect

volumes:
  prefect_data:
```

---

## Reproduzierbarkeit

```python
# Task-Caching für identische Inputs
@task(cache_key_fn=task_input_hash)
def generate_cfp(event_config: dict) -> str: ...

# Flow-Parameter dokumentieren
@flow
def event_planning_flow(
    config_path: str = "config/event.yaml",
    model_name: str = "llama3.2",
    temperature: float = 0.1,
    seed: int = 42,
): ...

# Ausführungsprotokoll
# Prefect speichert automatisch alle Runs mit Parametern, Logs und Ergebnissen
# → Abrufbar über UI oder API
```

---

## Projektstruktur

```
prefect-event-planning/
├── config/
│   └── event.yaml
├── flows/
│   ├── event_planning.py       # Haupt-Flow
│   ├── weekly_status.py        # Regelmäßiger Status-Flow
│   └── cfp_workflow.py
├── tasks/
│   ├── llm_tasks.py            # KI-bezogene Tasks
│   ├── file_tasks.py           # Datei-Operationen
│   └── notification_tasks.py   # Benachrichtigungen
├── workstreams/                # Outputs
├── requirements.txt
└── .env
```

---

## Fazit

Prefect ist die **beste Wahl für zuverlässige, zeitgesteuerte Pipelines** mit starker Observability. Besonders wertvoll für regelmäßige Aufgaben wie wöchentliche Status-Updates, Erinnerungen und Daten-Synchronisation.

**→ Ideal für:** Zeitgesteuerte Workflows, datenintensive Pipelines, Teams mit hohen Anforderungen an Zuverlässigkeit und Monitoring, Integration mit bestehenden Python-Systemen.
