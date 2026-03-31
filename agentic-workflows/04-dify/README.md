# Dify – Open Source LLM Application Platform

## Überblick

**Dify** ist eine vollständige Open-Source-Plattform zum Erstellen, Deployen und Betreiben von LLM-Applikationen. Sie bietet einen visuellen Workflow-Editor, RAG-Pipeline, Multi-Agenten-Unterstützung und ein eingebautes Chat-Interface – alles in einer Lösung.

| Eigenschaft | Wert |
|---|---|
| **Website** | https://dify.ai |
| **GitHub** | https://github.com/langgenius/dify |
| **Lizenz** | MIT (Community) / proprietär (Enterprise) |
| **Programmiersprache** | Python (Backend) + TypeScript (Frontend) |
| **GitHub-Sterne** | ~60.000+ |
| **Lokale Installation** | ✅ Docker Compose |
| **Visuelle Oberfläche** | ✅ Vollständige Web-App |
| **Multi-Agenten** | ✅ Agent-Node im Workflow |
| **Lokale LLMs** | ✅ Ollama, LocalAI, vLLM |

---

## Stärken für Eventplanung

- **Vollständige Plattform**: Kein separates Frontend nötig, alles in einer App
- **Visueller Workflow-Builder**: Komplexe Flows grafisch erstellen
- **RAG-Pipeline**: Dokumente hochladen und als Wissensbasis nutzen
- **Chatbot & Assistent**: Fertige Chat-Interfaces ohne Entwicklungsaufwand
- **Variablen & Parameter**: Event-Konfiguration als Input-Variablen
- **API & Webhooks**: Workflows automatisiert auslösen

---

## Installation (lokal via Docker Compose)

```bash
# Repository klonen
git clone https://github.com/langgenius/dify.git
cd dify/docker

# Umgebungsvariablen konfigurieren
cp .env.example .env
# .env anpassen (z.B. SECRET_KEY setzen)

# Starten
docker compose up -d
```

> Öffne http://localhost nach dem Start. Initialer Setup-Wizard erscheint.

### Minimalanforderungen
- Docker + Docker Compose
- 4 GB RAM (8 GB empfohlen)
- 5 GB freier Festplattenspeicher

---

## Anbindung an lokale KI-Modelle

### Ollama einrichten

1. In Dify: **Einstellungen** → **Modell-Anbieter** → **Ollama**
2. Konfiguration:
   ```
   API Endpoint: http://host.docker.internal:11434
   ```
3. Verfügbare Modelle werden automatisch erkannt

### LocalAI einrichten

```
API Endpoint: http://host.docker.internal:8080/v1
API Key: local (Platzhalter)
```

### vLLM einrichten

```
API Endpoint: http://host.docker.internal:8000/v1
API Key: vllm-key (Platzhalter)
```

---

## Dify Workflow für Eventplanung

### Workflow-Typen in Dify

| Typ | Beschreibung | Anwendungsfall |
|---|---|---|
| **Chatbot** | Konversationeller Assistent | CfP-Beratung, FAQ |
| **Text Generator** | Einmalige Textgenerierung | Briefings, Pressemitteilungen |
| **Workflow** | Mehrstufige Pipeline | Komplexe Planungsaufgaben |
| **Agent** | Autonomer Problemlöser | Recherche, Datenbeschaffung |

### Beispiel-Workflow: Speaker-Briefing-Generator

**Schritte im visuellen Editor:**

```
[Start]
  ↓
[Input: speaker_name, speaker_topic, event_date]
  ↓
[LLM Node: Recherche-Prompt]
  "Recherchiere {speaker_name} und ihre Arbeit zu {speaker_topic}"
  ↓
[LLM Node: Briefing erstellen]
  "Erstelle ein strukturiertes Speaker-Briefing für {speaker_name}..."
  ↓
[Template Node: Markdown formatieren]
  ↓
[End: Briefing ausgeben]
```

### YAML-Workflow-Export (Versionierung)

Dify-Workflows können als YAML exportiert werden:

```yaml
# Beispiel: Dify Workflow Definition
app:
  name: "AITD 2026 Speaker Briefing Generator"
  mode: workflow
  
nodes:
  - id: start
    type: start
    outputs:
      - variable: speaker_name
        type: string
      - variable: event_config
        type: string
        
  - id: llm_briefing
    type: llm
    model:
      provider: ollama
      name: llama3.2
    prompt:
      system: "Du bist ein Assistent für die AI Transparency Days 2026."
      user: "Erstelle ein Briefing für Speaker {speaker_name}..."
```

---

## Wissensdatenbank (RAG) aufbauen

1. **Wissensdatenbank erstellen**: Einstellungen → Wissensdatenbank → Neu
2. **Dokumente hochladen**: Alle `workstreams/**/*.md` Dateien
3. **Einbettungsmodell**: Ollama Embeddings oder lokales Modell
4. **In Workflow einbinden**: Knowledge Retrieval Node

```
[Input: Frage]
    ↓
[Knowledge Retrieval Node]   ← Durchsucht alle Workstream-Dokumente
    ↓
[LLM Node: Antwort generieren]
    ↓
[Output]
```

---

## API-Integration

```bash
# Workflow über API auslösen
curl -X POST 'http://localhost/v1/workflows/run' \
  -H 'Authorization: Bearer <app-api-key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "inputs": {
      "speaker_name": "Dr. Anna Schmidt",
      "event_date": "2026-10-14"
    },
    "response_mode": "blocking",
    "user": "event-planner"
  }'
```

```python
import requests

def generate_speaker_briefing(speaker_name: str, event_date: str) -> str:
    response = requests.post(
        "http://localhost/v1/workflows/run",
        headers={
            "Authorization": "Bearer <api-key>",
            "Content-Type": "application/json"
        },
        json={
            "inputs": {
                "speaker_name": speaker_name,
                "event_date": event_date
            },
            "response_mode": "blocking",
            "user": "event-planner"
        }
    )
    return response.json()["data"]["outputs"]["briefing"]
```

---

## Dify für das bestehende Agenten-Modell

Das bestehende Modell (Orchestrator + 5 Fachagenten) kann in Dify abgebildet werden:

| Bestehender Agent | Dify App-Typ | Dify App Name |
|---|---|---|
| Orchestrator | Workflow | AITD Orchestrator |
| Programm | Agent / Workflow | AITD Programm-Agent |
| Kommunikation | Text Generator | AITD Kommunikations-Agent |
| Operations | Workflow | AITD Operations-Agent |
| Koordination | Chatbot | AITD Dashboard-Assistent |
| Dokumentation | Text Generator | AITD Dokumentations-Agent |

---

## Einschränkungen

- Benötigt mehr Ressourcen als leichtgewichtige Alternativen (Docker Compose mit mehreren Services)
- Enterprise-Features (SSO, Audit-Log, erweiterte Berechtigungen) kostenpflichtig
- Workflow-Exporte als JSON/YAML nicht immer perfekt Git-diffbar

---

## Fazit

Dify ist die **umfassendste All-in-One-Lösung** für Teams, die eine professionelle KI-Plattform ohne Cloud-Abhängigkeit wollen. Die Kombination aus visuellem Editor, RAG-Pipeline und fertigen Chat-Interfaces macht es zur stärksten lokalen Alternative zu kommerziellen Diensten.

**→ Ideal für:** Teams, die eine vollständige Plattform suchen, RAG über interne Dokumente, mehrere parallele KI-Applikationen, professionelle Präsentation der Ergebnisse.
