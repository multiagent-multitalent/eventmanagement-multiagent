# Flowise – Visual LangChain UI

## Überblick

**Flowise** ist eine Open-Source-Plattform mit grafischer Benutzeroberfläche zum Erstellen von LLM-Applikationen und Agenten-Workflows – basierend auf LangChain, aber ohne Code. Der Drag-&-Drop-Editor macht es auch für Nicht-Entwickler zugänglich.

| Eigenschaft | Wert |
|---|---|
| **Website** | https://flowiseai.com |
| **GitHub** | https://github.com/FlowiseAI/Flowise |
| **Lizenz** | Apache 2.0 |
| **Programmiersprache** | TypeScript / Node.js |
| **GitHub-Sterne** | ~35.000+ |
| **Lokale Installation** | ✅ Docker, npm |
| **Visuelle Oberfläche** | ✅ Drag & Drop Editor |
| **Multi-Agenten** | ⚠️ Über Sequential Agent Chain |
| **Lokale LLMs** | ✅ Ollama Node integriert |

---

## Stärken für Eventplanung

- **Kein Code nötig**: Agenten-Flows visuell bauen
- **Integrierter Ollama-Node**: Direktanbindung lokaler Modelle ohne Konfigurationsaufwand
- **Chatbot-Interface**: Schnell testbar über eingebettetes Chat-Widget
- **API-Endpoint**: Jeder Flow ist automatisch als REST-API verfügbar
- **Marketplace**: Vorgefertigte Flows importierbar

---

## Installation (lokal via Docker)

```bash
docker run -d \
  --name flowise \
  -p 3000:3000 \
  -v flowise_data:/root/.flowise \
  flowiseai/flowise:latest
```

### docker-compose.yml

```yaml
version: "3.8"

services:
  flowise:
    image: flowiseai/flowise:latest
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - PORT=3000
      - FLOWISE_USERNAME=admin
      - FLOWISE_PASSWORD=changeme
      - DATABASE_PATH=/root/.flowise
      - APIKEY_PATH=/root/.flowise
      - LOG_PATH=/root/.flowise/logs
    volumes:
      - flowise_data:/root/.flowise

volumes:
  flowise_data:
```

```bash
docker-compose up -d
# Öffne http://localhost:3000
```

---

## Anbindung an Ollama

In der Flowise-Oberfläche:

1. Neuen Flow erstellen
2. Node **"ChatOllama"** hinzufügen
3. Konfiguration:
   - **Base URL**: `http://host.docker.internal:11434`
   - **Model Name**: `llama3.2` (oder anderes Modell)
4. ChatOllama-Node mit weiteren Nodes verbinden

> Unter Linux: `http://172.17.0.1:11434` statt `host.docker.internal`

---

## Typische Flows für Eventplanung

### Flow 1: CfP-Assistent

```
[Ollama Chat Model]
         ↓
[ConversationChain]
         ↓
[Chat Widget / API]
```

Beispiel-Systemprompt:
```
Du bist ein Assistent für den Call for Papers der AI Transparency Days 2026.
Beantworte Fragen zu Einreichungsrichtlinien, helfe bei der Formulierung 
von Abstracts und kategorisiere eingehende Einreichungen nach den Themen:
- AI Transparency
- AI Safety
- AI Governance
- Human Compatible AI
```

### Flow 2: Dokumenten-basierter Assistent (RAG)

```
[PDF / Markdown Files] → [Document Loader]
                                ↓
                      [Text Splitter]
                                ↓
                      [In-Memory Vector Store]
                                ↓
[Ollama Embeddings] → [Retriever]
                                ↓
                      [Conversational Retrieval Chain]
                                ↓
                      [ChatOllama]
```

Anwendung: Alle Workstream-Dokumente (`workstreams/`) als Wissensbasis laden.

### Flow 3: Multi-Step Agent

```
[ChatOllama]
     ↓
[OpenAI Function Agent]
     ├─→ [Tool: Read File]
     ├─→ [Tool: Write File]
     └─→ [Tool: HTTP Request]
```

---

## Flows als JSON exportieren (Versionierung)

Flowise-Flows können als JSON-Dateien exportiert werden:

1. Flow öffnen → **Export** → JSON-Datei speichern
2. Datei unter `agentic-workflows/03-flowise/flows/` ablegen
3. Importieren: **Import** → JSON-Datei auswählen

```bash
# Flows via API exportieren
curl -H "Authorization: Bearer <api-key>" \
  http://localhost:3000/api/v1/chatflows \
  > flows/all-flows.json
```

---

## API-Nutzung (Automatisierung)

Jeder Flowise-Flow ist automatisch als REST-API verfügbar:

```bash
# Flow über API aufrufen
curl -X POST \
  http://localhost:3000/api/v1/prediction/<flow-id> \
  -H "Content-Type: application/json" \
  -d '{"question": "Erstelle ein Speaker-Briefing für Dr. Müller"}'
```

```python
import requests

response = requests.post(
    "http://localhost:3000/api/v1/prediction/<flow-id>",
    json={"question": "Erstelle ein Speaker-Briefing für Dr. Müller"}
)
print(response.json()["text"])
```

---

## Einschränkungen

- Komplexe Agenten-Koordination ist eingeschränkter als in Code-basierten Frameworks
- Flows sind JSON-basiert, aber nicht so gut für Git-Diff geeignet wie Klartextdateien
- Keine native Unterstützung für Cron-Jobs / zeitgesteuerte Ausführung

---

## Fazit

Flowise ist die **einfachste Einstiegsmöglichkeit** für KI-gestützte Eventplanung ohne Programmierkenntnisse. Besonders wertvoll für Teams, die schnell eine Wissensdatenbank oder einen Assistenten aufbauen wollen.

**→ Ideal für:** Schnelle Prototypen, dokumentenbasierte Assistenten (RAG), Teams ohne Python-Kenntnisse, erste Experimente mit lokalen LLMs.
