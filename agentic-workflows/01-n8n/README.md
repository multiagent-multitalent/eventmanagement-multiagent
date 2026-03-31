# n8n – Visual Workflow Automation

## Überblick

**n8n** (ausgesprochen „n-eight-n") ist eine Open-Source-Workflow-Automatisierungsplattform mit einer visuellen, Node-basierten Oberfläche. Sie verbindet verschiedene Dienste und kann KI-Agenten in komplexe Automatisierungspipelines integrieren.

| Eigenschaft | Wert |
|---|---|
| **Website** | https://n8n.io |
| **GitHub** | https://github.com/n8n-io/n8n |
| **Lizenz** | Apache 2.0 (Community) + proprietäre Enterprise-Erweiterungen |
| **Programmiersprache** | TypeScript / Node.js |
| **Sterne (GitHub)** | ~50.000+ |
| **Lokale Installation** | ✅ Docker, npm, Desktop App |
| **Visuelle Oberfläche** | ✅ Drag & Drop Workflow Editor |
| **Multi-Agenten** | ⚠️ Möglich, aber nicht nativ |
| **Lokale LLMs** | ✅ Über LangChain-Node oder HTTP-Request |

---

## Stärken für Eventplanung

- **400+ integrierte Nodes**: E-Mail (SMTP, Gmail), Kalender, Spreadsheets, Notion, Airtable, Slack, Telegram, HTTP-Requests etc.
- **KI-Nodes**: LangChain-Integration, OpenAI-kompatibler Endpunkt konfigurierbar
- **Zeitgesteuerte Ausführung**: Cron-Trigger für regelmäßige Aufgaben
- **Human-in-the-Loop**: Warteschritte mit manueller Genehmigung
- **Wiederverwendbarkeit**: Workflows als JSON exportierbar/importierbar

---

## Installation (lokal via Docker)

```bash
# Einfachste Installation
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n

# Mit docker-compose (empfohlen für persistente Nutzung)
```

### docker-compose.yml

```yaml
version: "3.8"

services:
  n8n:
    image: docker.n8n.io/n8nio/n8n:latest
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=changeme
      - WEBHOOK_URL=http://localhost:5678/
      - GENERIC_TIMEZONE=Europe/Berlin
    volumes:
      - n8n_data:/home/node/.n8n
      - ./workflows:/home/node/workflows   # Workflow-Backups

volumes:
  n8n_data:
```

```bash
docker-compose up -d
# Öffne http://localhost:5678
```

---

## Anbindung an lokale KI-Modelle

### Mit Ollama (empfohlen)

In n8n den **LangChain** → **Chat Model** → **Ollama** Node verwenden:

```
Host: http://host.docker.internal:11434
Modell: llama3.2 / mistral / gemma3
```

> **Hinweis:** `host.docker.internal` ist der Docker-interne Hostname für den Host-Rechner. Unter Linux ggf. `172.17.0.1` oder `--add-host=host.docker.internal:host-gateway` verwenden.

### Mit LocalAI / OpenAI-kompatibler API

Im **OpenAI** Node:
```
Base URL: http://localhost:8080/v1
API Key: (beliebig, z.B. "local")
Modell: (je nach LocalAI-Konfiguration)
```

---

## Anwendungsfälle für Eventplanung

### 1. CfP-Einreichungen automatisch verarbeiten
```
[E-Mail Trigger] → [KI: Einreichung kategorisieren] → [Notion: Datensatz anlegen] → [E-Mail: Bestätigung senden]
```

### 2. Social-Media-Kalender erstellen
```
[Webhook / Manuell] → [Lese event.yaml] → [KI: Posts generieren] → [Google Sheets: Kalender befüllen] → [Slack: Team benachrichtigen]
```

### 3. Speaker-Briefings generieren
```
[Airtable: Speaker-Daten lesen] → [KI: Briefing generieren] → [PDF erstellen] → [E-Mail: Briefing versenden]
```

### 4. Budget-Tracking
```
[Cron: täglich] → [Google Sheets: Ausgaben lesen] → [KI: Analyse & Bericht] → [Slack: Alert wenn Budget überschritten]
```

---

## Workflow als JSON (Versionierung)

Workflows können exportiert und unter `workflows/` versioniert werden:

```bash
# Workflow exportieren (n8n CLI)
n8n export:workflow --id=<id> --output=workflows/cfp-processor.json

# Workflow importieren
n8n import:workflow --input=workflows/cfp-processor.json
```

---

## Reproduzierbarkeit

- Workflows als **JSON-Dateien** exportierbar → Git-kompatibel
- **Umgebungsvariablen** für API-Keys und Konfigurationen nutzbar
- **Workflow-Versionen** im integrierten Editor nachverfolgbar
- **Execution-Logs** für jede Ausführung gespeichert

---

## Einschränkungen

- Komplexe Multi-Agenten-Koordination ist umständlicher als in spezialisierten Frameworks (CrewAI, AutoGen)
- Die „fair code"-Lizenz erlaubt keine Weiterverkaufen ohne Lizenz (für Eigennutz unproblematisch)
- Einige erweiterte Features (z.B. SAML, Audit Log) nur in der kostenpflichtigen Enterprise-Version

---

## Fazit

n8n ist die **beste Wahl für Eventplaner ohne tiefes Python-Know-how**, die komplexe Integrationen brauchen. Die Kombination aus visuellem Editor, hunderten von Integrationen und KI-Unterstützung macht es zum vielseitigsten Tool in dieser Liste.

**→ Ideal für:** Automatisierung von E-Mail-Flows, Kalender-Management, Benachrichtigungen, Datensammlung und -verteilung.
