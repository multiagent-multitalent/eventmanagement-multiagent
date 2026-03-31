# CLAUDE.md – Einstiegspunkt für KI-Agenten

Willkommen im universellen Event-Management-System. Dieses Repository ermöglicht die vollautomatische Planung von Events jeder Art mit KI-Agenten.

> **Demo-Beispiel:** Die AI Transparency Days 2026 (AITD 2026) zeigen als Referenzimplementierung, was das System generiert. Alle Demo-Artefakte liegen in [`examples/aitd-2026/`](examples/aitd-2026/).

---

## 🚀 Schnellstart (für Menschen)

**→ [`QUICKSTART.md`](QUICKSTART.md)** – In 3 Schritten zur fertigen Event-Planung:
1. `config/event.yaml` ausfüllen
2. Orchestrator-Agent starten
3. `CONFIRM.md` bestätigen

**Aktueller Status:** [`dashboard/status.md`](dashboard/status.md)
**Offene Bestätigungen:** [`CONFIRM.md`](CONFIRM.md)

---

## Für KI-Agenten: Wie dieses System funktioniert

Dieses Repository ist das zentrale Arbeitssystem für alle Planungsprozesse. Du als Agent kannst hier:
- Den aktuellen Planungsstand einsehen (`dashboard/status.md`)
- Aufgaben in den Workstreams bearbeiten (`workstreams/`)
- Vorlagen für Artefakte nutzen (`templates/`)
- Die Konfiguration des Events lesen (`config/event.yaml`)
- Das Phasenmodell und die Rollen nachschlagen (`docs/`)

---

## Wie dieses System funktioniert

### Agenten-Rollen

Es gibt **6 Agenten** – 1 Orchestrator und 5 Fachagenten:

| Agent | Datei | Fokus |
|---|---|---|
| **Orchestrator** | `.claude/agents/orchestrator.md` | **Vollautomatische Planung aus event.yaml** |
| Kommunikation | `.claude/agents/kommunikation.md` | Social Media, Newsletter, Presse, E-Mail |
| Operations | `.claude/agents/operations.md` | Checklisten, Logistik, Bestellungen, Abhängigkeiten |
| Programm | `.claude/agents/programm.md` | CfP, Zeitplan, Sessions, Speaker-Briefings |
| Koordination | `.claude/agents/koordination.md` | Dashboard, Status-Updates, Meilensteine, Risiken |
| Dokumentation | `.claude/agents/dokumentation.md` | Protokolle, Reports, Wissensbasis, Lessons Learned |

### Wo du anfangen sollst

0. **Prüfe `QUICKSTART.md`** – wenn du neu bist und alles automatisch erledigen willst
1. **Lese `config/event.yaml`** – Event-Eckdaten, Datum, Ort, Größe
2. **Lese `dashboard/status.md`** – aktueller Stand aller Workstreams
3. **Lese deine Agenten-Konfiguration** in `.claude/agents/` – deine Rolle und Verantwortlichkeiten
4. **Arbeite im passenden Workstream** unter `workstreams/`

### Planungsphasen

Das Event folgt einem strukturierten Phasenmodell (Details: `docs/phasenmodell.md`):

1. **Initialisierung** (Kick-off, Konzept)
2. **Planung** (Struktur, Venue, Programm, Budget)
3. **Umsetzung** (Umsetzung aller Arbeitspakete)
4. **Durchführung** (Vor-Ort, Event-Tage)
5. **Nachbereitung** (Feedback, Dokumentation, Lessons Learned)

### Workstreams

Jeder Workstream hat einen eigenen Ordner unter `workstreams/` mit:
- `README.md` – Aufgaben, Status, Verantwortliche
- Artefakten und Arbeitsdokumenten

### Vorlagen

Unter `templates/` liegen Vorlagen für alle Planungsphasen – gegliedert nach Workstream. Nutze diese als Ausgangspunkt für neue Dokumente.

### Prinzip: Agenten unterstützen, Menschen entscheiden

- Agenten übernehmen Routinearbeit (Checklisten, Statusverfolgung, Textentwürfe)
- Menschen treffen strategische Entscheidungen, führen Gespräche, gestalten kreativ

---

## Repository-Struktur

```text
eventmanagement-multiagent/
├── CLAUDE.md                        # Dieser Einstiegspunkt
├── QUICKSTART.md                    # 🚀 Schnellstart für Menschen (3 Schritte)
├── CONFIRM.md                       # ✅ Finale Bestätigung nach Agent-Durchlauf
├── archiv/2026-03-repository-cleanup/Task Requirements.md  # archivierte Aufgabenstellung
├── .claude/agents/                  # 6 Agenten-Konfigurationen
│   ├── orchestrator.md              # 🤖 Master-Orchestrator (vollautomatisch)
│   ├── kommunikation.md
│   ├── operations.md
│   ├── programm.md
│   ├── koordination.md
│   └── dokumentation.md
├── docs/                            # Phasenmodell, Workstreams, Rollen
│   ├── phasenmodell.md
│   ├── workstreams.md
│   └── rollen.md
├── templates/                       # Artefakt-Vorlagen für alle Phasen
│   ├── programm/
│   ├── kommunikation/
│   ├── teilnehmer/
│   ├── venue-logistik/
│   ├── catering/
│   ├── technik/
│   ├── personal/
│   ├── sponsoring/
│   ├── budget/
│   ├── unterkunft-anreise/
│   └── nachbereitung/
├── config/                          # Event- und Team-Konfiguration
│   ├── event.yaml                   # ← Hier deine Event-Details eintragen (Demo: AITD 2026)
│   └── team.yaml
├── workstreams/                     # Laufende Arbeit pro Bereich (vom Orchestrator befüllt)
│   ├── programm/
│   ├── kommunikation/
│   ├── teilnehmer/
│   ├── venue-logistik/
│   ├── catering/
│   ├── technik/
│   ├── personal/
│   ├── sponsoring/
│   ├── unterkunft-anreise/
│   └── nachbereitung/
├── examples/                        # 📖 Demo-Outputs für fertige Events
│   └── aitd-2026/                   # AI Transparency Days 2026 – vollständiges Beispiel
├── dashboard/                       # Status und Tracking
│   └── status.md
├── archiv/                          # Lessons Learned, Entscheidungslog
│   ├── entscheidungslog.md
│   └── lessons-learned.md
└── agentic-workflows/               # 🤖 Reproduzierbare Workflow-Umsetzungen
    ├── README.md                    # Überblick & Schnell-Entscheidungshilfe
    ├── empfehlung.md                # Empfohlener Stack für dieses Projekt
    ├── vergleich.md                 # Detaillierte Vergleichsmatrix
    ├── 01-n8n/                      # Visual Workflow Automation
    ├── 02-langchain-langgraph/      # Python AI Agent Framework
    ├── 03-flowise/                  # Visual LangChain UI
    ├── 04-dify/                     # LLM Application Platform
    ├── 05-autogen/                  # Multi-Agent Conversation Framework
    ├── 06-crewai/                   # Multi-Agent Orchestration (empfohlen)
    ├── 07-prefect/                  # Workflow Orchestration
    └── lokale-ki-modelle/           # Ollama, LocalAI, vLLM, LM Studio
```

---

## Für neue Teammitglieder

Frage einfach einen der Agenten:
- „Wie funktioniert die Eventplanung in diesem System?"
- „Was muss als Nächstes passieren?"
- „Welche Artefakte fehlen noch in Workstream X?"
- „Wer ist für was verantwortlich?"

Der Agent liest diese Datei und die verlinkten Dokumente und gibt dir eine fundierte Antwort.

---

*Dieses Repository ist eine universelle Vorlage für Events jeder Art. Konfiguriere `config/event.yaml` und `config/team.yaml`, starte den Orchestrator – fertig. Die AI Transparency Days 2026 in `examples/aitd-2026/` zeigen als Demo, was das System automatisch generiert.*
