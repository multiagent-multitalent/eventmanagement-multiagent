# Agentic Workflows – Umsetzungsmöglichkeiten

Dieses Verzeichnis dokumentiert verschiedene Frameworks und Plattformen für **reproduzierbare, agentenbasierte Workflows** in der Eventplanung. Alle vorgestellten Lösungen erfüllen folgende Grundanforderungen:

- ✅ **Lokal betreibbar** (Self-hosted / On-Premise)
- ✅ **Open Source** (oder zumindest kostenlos nutzbar)
- ✅ **API-kompatibel** mit lokalen KI-Modellen (Ollama, LocalAI, vLLM etc.)
- ✅ **Reproduzierbar** (Workflows versionierbar, nachvollziehbar, wiederholbar)

---

## Übersicht der Optionen

| # | Tool / Framework | Typ | Zielgruppe | Einstieg |
|---|---|---|---|---|
| 1 | [**n8n**](./01-n8n/README.md) | Visual Workflow Automation | Nicht-Techniker & Entwickler | Mittel |
| 2 | [**LangChain / LangGraph**](./02-langchain-langgraph/README.md) | Code-basiertes AI-Framework | Entwickler (Python) | Hoch |
| 3 | [**Flowise**](./03-flowise/README.md) | Visual LangChain UI | Nicht-Techniker & Entwickler | Einfach |
| 4 | [**Dify**](./04-dify/README.md) | LLM Application Platform | Nicht-Techniker & Entwickler | Einfach |
| 5 | [**AutoGen**](./05-autogen/README.md) | Multi-Agent-Framework | Entwickler (Python) | Mittel |
| 6 | [**CrewAI**](./06-crewai/README.md) | Multi-Agent-Orchestrierung | Entwickler (Python) | Mittel |
| 7 | [**Prefect**](./07-prefect/README.md) | Workflow-Orchestrierung | Entwickler (Python) | Mittel |
| – | [**Lokale KI-Modelle**](./lokale-ki-modelle/README.md) | Model-Serving-Infrastruktur | Alle | Variiert |

---

## Schnell-Entscheidungshilfe

```
Bist du technisch versiert und programmierst in Python?
├── Ja → Willst du Multi-Agenten (mehrere KI-Rollen)?
│         ├── Ja → CrewAI oder AutoGen (→ 05, 06)
│         └── Nein → LangGraph für komplexe Flows / Prefect für Pipelines (→ 02, 07)
└── Nein → Bevorzugst du eine visuelle Oberfläche (Drag & Drop)?
           ├── Ja → Dify oder Flowise (→ 03, 04)
           └── Auch Integrationen & Automatisierungen wichtig → n8n (→ 01)
```

---

## Empfohlene Kombination für dieses Projekt

Für den **AI Transparency Days 2026** und ähnliche Events empfehlen wir:

| Schicht | Tool | Begründung |
|---|---|---|
| **Workflow-Engine** | n8n | Visuelle Workflows, einfache Integrationen, kein Code nötig |
| **Agenten-Logik** | CrewAI | Saubere Rollenverteilung, entspricht unserem Agenten-Modell |
| **Lokale KI-Modelle** | Ollama | Einfachste lokale LLM-Infrastruktur |
| **Optionale UI** | Dify oder Flowise | Für nicht-technische Teammitglieder |

→ Details und Begründung: **[`empfehlung.md`](./empfehlung.md)**

---

## Verzeichnisstruktur

```
agentic-workflows/
├── README.md                      # Diese Datei – Überblick
├── empfehlung.md                  # Finale Empfehlung für dieses Projekt
├── vergleich.md                   # Detaillierte Vergleichsmatrix
├── 01-n8n/
│   └── README.md                  # n8n – Visual Workflow Automation
├── 02-langchain-langgraph/
│   └── README.md                  # LangChain / LangGraph
├── 03-flowise/
│   └── README.md                  # Flowise – Visual LangChain UI
├── 04-dify/
│   └── README.md                  # Dify – LLM Application Platform
├── 05-autogen/
│   └── README.md                  # AutoGen – Multi-Agent Framework
├── 06-crewai/
│   └── README.md                  # CrewAI – Multi-Agent Orchestration
├── 07-prefect/
│   └── README.md                  # Prefect – Workflow Orchestration
└── lokale-ki-modelle/
    └── README.md                  # Ollama, LocalAI, vLLM, LM Studio
```

---

## Gemeinsame Anforderungen

### Reproduzierbarkeit
Alle Workflows sollen:
- **Versionierbar** sein (Git-freundliche Konfigurationsdateien)
- **Parametrisierbar** sein (Event-Konfiguration aus `config/event.yaml` einlesbar)
- **Wiederholbar** sein (gleicher Input → gleicher Output)
- **Nachvollziehbar** sein (Logs, Audit-Trail)

### Lokale AI-Modelle via API
Alle Tools unterstützen OpenAI-kompatible APIs. Damit können lokale Modelle (z.B. via Ollama, LocalAI, vLLM) genutzt werden, indem der API-Endpunkt auf `http://localhost:11434` (Ollama) oder ähnliche lokale Adressen gesetzt wird.

```yaml
# Beispiel: OpenAI-kompatibler Endpunkt für lokale Modelle
api_base: "http://localhost:11434/v1"
api_key: "ollama"  # Ollama benötigt keinen echten Key
model: "llama3.2"
```

→ Details zu lokalen Modellen: **[`lokale-ki-modelle/README.md`](./lokale-ki-modelle/README.md)**
