# Empfehlung – Agentic Workflows für AITD 2026

## Zusammenfassung

Nach Analyse aller Optionen empfehlen wir für das Event-Management-System der **AI Transparency Days 2026** eine **modulare Kombination** aus drei komplementären Tools, die jeweils unterschiedliche Anforderungen abdecken.

---

## Empfohlene Stack-Kombination

```
┌─────────────────────────────────────────────────────────────┐
│                    AITD 2026 Workflow Stack                   │
├──────────────────┬──────────────────┬───────────────────────┤
│  Agenten-Logik   │  Integrationen   │  KI-Infrastruktur     │
│                  │                  │                        │
│  CrewAI          │  n8n             │  Ollama               │
│  ─────────────   │  ─────────────   │  ────────────         │
│  Multi-Agenten   │  400+ Services   │  Lokale LLMs          │
│  YAML-Config     │  Zeitplanung     │  OpenAI-API           │
│  Git-freundlich  │  Webhooks        │  Kein Cloud-Zwang     │
└──────────────────┴──────────────────┴───────────────────────┘
```

| Schicht | Tool | Version | Zweck |
|---|---|---|---|
| **Agenten-Logik** | **CrewAI** | ≥ 0.80 | Multi-Agenten-Orchestrierung |
| **Workflow-Integration** | **n8n** | ≥ 1.0 | Externe Integrationen, Zeitplanung |
| **KI-Infrastruktur** | **Ollama** | ≥ 0.3 | Lokale LLM-Bereitstellung |
| *Optional: RAG/UI* | *Dify* | *≥ 0.9* | *Dokumenten-Assistent, Team-UI* |

---

## Begründung

### Warum CrewAI als Agenten-Framework?

Das bestehende Agenten-Modell dieses Projekts (Orchestrator + 5 Fachagenten) lässt sich **direkt** in CrewAI abbilden:

| Bestehender Agent | CrewAI Role |
|---|---|
| Orchestrator | Manager (hierarchischer Prozess) |
| Programm-Agent | `role: "Programm-Manager"` |
| Kommunikation-Agent | `role: "Kommunikations-Manager"` |
| Operations-Agent | `role: "Operations-Manager"` |
| Koordination-Agent | `role: "Koordinations-Manager"` |
| Dokumentation-Agent | `role: "Dokumentations-Manager"` |

**Weitere Gründe:**
- YAML-Konfiguration ist Git-kompatibel und versionierbar
- Ausgaben direkt in `workstreams/` schreibbar
- Einfache Integration mit Ollama
- Aktive Community, gute Dokumentation

### Warum n8n für Integrationen?

CrewAI ist stark bei Agenten-Logik, aber schwach bei:
- Zeitgesteuerten Ausführungen (Cron-Jobs)
- E-Mail-Triggern und -Versand
- Google Sheets, Notion, Airtable
- Slack/Teams-Benachrichtigungen
- Webhook-Handling

n8n füllt diese Lücke als **Glue Code** zwischen dem KI-Agenten-System und externen Services. Die Integration läuft über HTTP-Webhooks.

### Warum Ollama für lokale LLMs?

- Einfachste Installation (ein Befehl)
- Breite Modellauswahl (llama, mistral, gemma, qwen, ...)
- Automatischer OpenAI-API-kompatibler Endpunkt
- Läuft ohne GPU auf CPU (ausreichend für Entwicklung)
- Kein Cloud-Anbieter, keine Datenschutzbedenken

---

## Architekturdiagramm

```
config/event.yaml
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│                    CrewAI Crew                             │
│                                                            │
│  ┌────────────┐    Koordiniert    ┌────────────────────┐  │
│  │ Orchestrator│ ──────────────→ │  Fachagenten        │  │
│  │  (Manager)  │                 │  • Programm         │  │
│  └────────────┘                  │  • Kommunikation    │  │
│                                  │  • Operations       │  │
│                                  │  • Koordination     │  │
│                                  │  • Dokumentation    │  │
│                                  └────────────────────┘  │
│                                           │               │
│                                           ▼               │
│                                   [Ollama / LLM]          │
└──────────────────────────────────────────────────────────┘
       │
       ▼
workstreams/        ← Artefakte (Markdown-Dateien)
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│                       n8n                                  │
│                                                            │
│  [CrewAI Webhook] → [Post-Processing] → [Verteilen]       │
│  [Cron Trigger]   → [Status-Update]   → [Slack Alert]     │
│  [E-Mail Trigger] → [CfP Processing]  → [Notion Entry]    │
└──────────────────────────────────────────────────────────┘
```

---

## Implementierungsplan

### Phase 1: Grundinfrastruktur (1-2 Tage)

```bash
# 1. Ollama installieren und Modell laden
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1:8b  # oder qwen2.5:7b für besseres Deutsch

# 2. Python-Umgebung einrichten
python -m venv venv
source venv/bin/activate
pip install crewai crewai-tools langchain-community pyyaml

# 3. n8n starten
docker run -d --name n8n -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

### Phase 2: CrewAI Crew einrichten (2-3 Tage)

```bash
# CrewAI-Projekt erstellen
crewai create crew aitd-agents
cd aitd-agents

# Event-Konfiguration verknüpfen
ln -s ../config/event.yaml config/event.yaml
ln -s ../workstreams workstreams
```

Dateien anpassen:
- `config/agents.yaml` – 6 Agenten-Definitionen (→ Vorlage in `06-crewai/README.md`)
- `config/tasks.yaml` – Aufgaben pro Workstream
- `src/aitd_agents/crew.py` – Crew zusammenstellen

### Phase 3: n8n Workflows (1-2 Tage)

1. n8n öffnen: http://localhost:5678
2. Workflows für häufige Aufgaben erstellen:
   - CfP-E-Mails empfangen und kategorisieren
   - Wöchentliche Status-Erinnerungen
   - CrewAI-Workflow auslösen (HTTP Webhook)

### Phase 4: Testen & Verfeinern (laufend)

- Prompts in `config/agents.yaml` und `config/tasks.yaml` optimieren
- Modell wechseln (llama3.2 → qwen2.5 → llama3.1) und vergleichen
- Workflows automatisieren

---

## Alternative: Nur-n8n-Ansatz (für Nicht-Entwickler)

Wenn kein Python-Know-how im Team vorhanden ist:

```
n8n + Ollama
├── n8n für alle Workflows (visuell)
├── Ollama als LLM-Backend
└── Kein Code nötig
```

Nachteil: Weniger präzise Agenten-Koordination, keine YAML-Konfiguration.

---

## Datenschutz & Sicherheit

Da alle Komponenten lokal laufen, verlassen **keine Planungsdaten das eigene System**:

| Datenkategorie | Verbleib |
|---|---|
| Event-Konfiguration | Lokal in `config/event.yaml` |
| Agenten-Prompts | Lokal in `config/agents.yaml` |
| LLM-Inferenz | Lokal via Ollama |
| Workflow-Daten | Lokal in n8n-Datenbank |
| Artefakte | Lokal in `workstreams/` |

---

## Kosten

| Komponente | Kosten |
|---|---|
| CrewAI (Community) | **Kostenlos** |
| n8n (Self-hosted) | **Kostenlos** |
| Ollama | **Kostenlos** |
| Dify (Self-hosted) | **Kostenlos** |
| **Gesamt** | **0 € laufende Kosten** |

Nur Hardware/Server-Kosten fallen an (eigener Laptop oder eigener Server).

---

## Weiterführende Ressourcen

| Resource | URL |
|---|---|
| CrewAI Dokumentation | https://docs.crewai.com |
| n8n Dokumentation | https://docs.n8n.io |
| Ollama Modell-Bibliothek | https://ollama.com/library |
| LangGraph Dokumentation | https://langchain-ai.github.io/langgraph/ |
| Dify Dokumentation | https://docs.dify.ai |
| AutoGen Dokumentation | https://microsoft.github.io/autogen/ |
| Prefect Dokumentation | https://docs.prefect.io |
