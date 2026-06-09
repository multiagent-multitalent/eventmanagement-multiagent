# System-Erklärung — Eventmanagement Multi-Agent System

> Begleitdokument zur Projektdokumentation
> Stand: Juni 2026

Dieses Dokument erklärt das System ausführlich und verständlich, ohne technisches Fachvokabular vorauszusetzen. Es dient als Leitfaden, um die Architektur, die Arbeitsweise und die wissenschaftlichen Hintergründe des "Eventmanagement Multi-Agent" Projekts zu verstehen.

---

## Inhaltsverzeichnis

1. [Worum geht es?](#1-worum-geht-es)
2. [Die Kernidee](#2-die-kernidee)
3. [Die Analogie: Das virtuelle Planungsteam](#3-die-analogie-das-virtuelle-planungsteam)
4. [Das große Bild: Die drei Ebenen](#4-das-große-bild-die-drei-ebenen)
5. [Der Workflow: Vom Briefing zum Masterplan](#5-der-workflow-vom-briefing-zum-masterplan)
6. [Die technischen Bausteine](#6-die-technischen-bausteine)
7. [Wissenschaftliche Grundlagen](#7-wissenschaftliche-grundlagen)
8. [Struktur und Verzeichnisse](#8-struktur-und-verzeichnisse)
9. [Glossar](#9-glossar)

---

## 1. Worum geht es?

Das System automatisiert die komplexe Planung von Veranstaltungen (Events). Aus einem einfachen Beschreibungstext (Briefing) – wie z. B. *"Planung eines Firmenjubiläums für 200 Personen in Berlin"* – erstellt das System eine vollständige Projektstruktur. Dazu gehören Zeitpläne, Budgetrahmen, Catering-Konzepte und Risikoanalysen.

Besonderheit: Die Arbeit wird nicht von einer einzelnen KI erledigt, sondern von einem **Team spezialisierter KI-Agenten**, die unterschiedliche Rollen einnehmen.

---

## 2. Die Kernidee

> **"Ein lokales Multi-Agenten-System, das Eventplanung durch spezialisierte Workflows automatisiert und Ergebnisse in strukturierten Dokumenten sichert."**

- **Lokal:** Das System läuft auf der eigenen Hardware. Sensible Eventdaten verlassen das System nicht (außer für gezielte Web-Recherchen).
- **Multi-Agenten:** Statt eines "Alleskönners" arbeiten spezialisierte Agenten (z. B. für Content oder Planung) zusammen.
- **Markdown-basiert:** Alle Ergebnisse werden in einem universellen, mensch- und maschinenlesbaren Format (Markdown) gespeichert.

---

## 3. Die Analogie: Das virtuelle Planungsteam

Stellen wir uns ein menschliches Event-Büro vor:

- **Der Koordinator (Orchestrator):** Nimmt das Briefing entgegen, behält den Überblick und delegiert Aufgaben.
- **Der Planungs-Experte:** Erstellt die Struktur, definiert die Phasen und setzt Meilensteine.
- **Der Content-Spezialist:** Formuliert Texte, Einladungen und detaillierte Beschreibungen für die Arbeitspakete.
- **Der Rechercheur:** Sucht im Internet nach Locations, Preisen und Trends.

Im System sind diese Rollen durch Python-Skripte und LLM-Aufrufe (Large Language Models) ersetzt, die exakt diese Aufgaben übernehmen.

---

## 4. Das große Bild: Die drei Ebenen

Das System ist in drei Schichten unterteilt:

```
┌──────────────────────────────────────────────────────────────┐
│  1. Benutzer-Schnittstelle (Terminal-CLI)                    │
│     - Interaktive Steuerung über die Kommandozeile           │
│     - Farbige Status-Anzeigen und Fortschrittsbalken         │
│     - Auswahl von Event-Modellen und Providern               │
└──────────────────────────────────────────────────────────────┘
                              ↕
┌──────────────────────────────────────────────────────────────┐
│  2. Logik & Koordination (Python-Kern)                       │
│     - Der Orchestrator steuert den Ablauf                    │
│     - Verwaltung des Event-Status (State Management)         │
│     - Markdown-Logger schreibt alle Zwischenergebnisse       │
└──────────────────────────────────────────────────────────────┘
                              ↕
┌──────────────────────────────────────────────────────────────┐
│  3. Intelligenz-Schicht (KI-Agenten & LLMs)                  │
│     - Planning Agent: Erstellt die Struktur                  │
│     - Content Agent: Generiert detaillierte Inhalte          │
│     - Web-Search: Holt aktuelle Informationen                │
└──────────────────────────────────────────────────────────────┘
```

---

## 5. Der Workflow: Vom Briefing zum Masterplan

Der Planungsprozess folgt einem definierten Pfad:

1. **Briefing-Analyse:** Das System liest die Anforderungen ein.
2. **Strukturierung:** Der Planning Agent entwirft ein Phasenmodell (z. B. die 10 Phasen von Initialisierung bis Nachbereitung).
3. **Detail-Planung:** Für jede Phase werden spezifische Arbeitspakete (APs) generiert.
4. **Content-Generierung:** Der Content Agent füllt die APs mit Leben (Ziele, Aufgaben, Verantwortlichkeiten).
5. **Dokumentation:** Der Markdown-Logger schreibt alles in das `workstreams/`-Verzeichnis und aktualisiert das zentrale `PLANUNGSLOG.md`.

---

## 6. Die technischen Bausteine

### 6.1 Terminal-CLI (Rich)
Anstelle einer komplexen Web-Oberfläche nutzt das System eine hochmoderne Terminal-Schnittstelle. Mit der `rich`-Bibliothek werden Tabellen, Emojis und Fortschrittsanzeigen direkt in der Konsole gerendert. Dies sorgt für eine schnelle, stabile und entwicklerfreundliche Bedienung.

### 6.2 Markdown-Logging-System
Ein Kernstück ist der `MarkdownLogger`. Er sorgt dafür, dass die KI nicht "in eine Blackbox" arbeitet. Jeder Gedankengang und jedes Ergebnis wird sofort in strukturierte Markdown-Dateien geschrieben. Dies ermöglicht:
- **Transparenz:** Man kann der KI beim "Denken" zusehen.
- **Editierbarkeit:** Nutzer können die Pläne einfach in jedem Texteditor anpassen.
- **Langzeitarchivierung:** Keine proprietären Datenbankformate nötig.

### 6.3 Agentische Workflows
Im Ordner `agentic-workflows/` befinden sich Analysen verschiedener Frameworks (n8n, LangGraph, CrewAI). Das System nutzt diese Erkenntnisse, um die Zusammenarbeit der Agenten so effizient wie möglich zu gestalten (z. B. durch sequenzielle oder parallele Aufgabenverteilung).

---

## 7. Wissenschaftliche Grundlagen

Das System basiert auf aktuellen Forschungsergebnissen im Bereich der Künstlichen Intelligenz:

- **Chain-of-Thought (CoT):** Die Agenten werden angewiesen, ihre Schritte nacheinander zu planen, was die Logik der Ergebnisse verbessert (Wei et al. 2022).
- **Multi-Agent Systems (MAS):** Die Aufteilung in Rollen reduziert die Fehlerquote, da jedes Modell eine kleinere, fokussierte Aufgabe hat (MetaGPT, Hong et al. 2023).
- **RAG (Retrieval-Augmented Generation):** Durch die Einbindung von Vorlagen und Web-Recherche wird das Wissen des Modells gezielt erweitert, ohne dass es halluziniert.

---

## 8. Historie & Evolution: Vom Prototyp zum Framework

Die Entwicklung des Systems verlief in drei markanten Phasen. Diese Historie ist entscheidend, um die heutige Architektur zu verstehen.

### Phase 1: Der "AITD-Spezialist" (März 2026)
Ursprünglich war das Repository kein allgemeines Werkzeug, sondern ein spezieller Planer für die *AI Transparency Days 2026*. 
- **Das Problem:** Daten und Logik waren vermischt. Ergebnisse der Agenten wurden direkt in den Hauptordnern gespeichert.
- **Der "Gedächtnis-Fehler":** Da KI-Agenten vorhandene Dokumente lesen, um Kontext zu erhalten, "erinnerten" sie sich bei jedem neuen Start an die Ergebnisse des vorherigen Laufs. Wenn man versuchte, ein anderes Event zu planen, sahen die Agenten die alten AITD-Dateien und dachten, die Arbeit sei bereits erledigt. Informationen aus dem letzten Durchlauf flossen so ungewollt in neue Planungen ein.

### Phase 2: Das Universal-Repository (31. März 2026)
Um diesen "Gedächtnis-Leak" zu stoppen, wurde das Projekt radikal umgebaut:
- **Trennung von Demo und Kern:** Alle AITD-spezifischen Daten wurden in den Ordner `examples/aitd-2026/` verschoben.
- **Neutralisierung:** Die Haupt-Workstreams wurden geleert und durch neutrale Vorlagen ersetzt. Das System wurde zu einem Framework, das erst durch die `config/event.yaml` erfährt, welches Event es gerade planen soll.
- **Einführung des Orchestrators:** Mit LangGraph wurde ein echtes Zustandsmanagement (`src/state.py`) eingeführt, das den Fortschritt im Arbeitsspeicher verwaltet, statt sich nur auf vorhandene Dateien zu verlassen.

### Phase 3: Der Architektur-Shift (April 2026)
In der finalen Phase erfolgte der Wechsel der Benutzeroberfläche:
- **Abkehr von Streamlit:** Die Browser-basierte Oberfläche wurde durch eine robustere Terminal-CLI ersetzt.
- **Markdown-First:** Das System wechselte von flüchtigen JSON-Logs zu dauerhaften, strukturierten Markdown-Protokollen. Dies stellte sicher, dass die Dokumentation für Menschen sofort lesbar ist, während die Agenten eine klare, unmissverständliche Struktur für ihre Arbeit vorfinden.

---

## 9. Struktur und Verzeichnisse

| Ordner | Inhalt |
|---|---|
| `src/` | Der Quellcode (CLI, Agenten, Logger) |
| `docs/` | Dokumentation zu Workflows und Standards |
| `templates/` | Vorlagen für verschiedene Event-Bereiche (Catering, Technik, etc.) |
| `workstreams/` | Die generierten Pläne und das Master-Log (`PLANUNGSLOG.md`) |
| `arbeitspakete/` | Die 52 vordefinierten Pakete für das Demo-Event |
| `agentic-workflows/` | Vergleiche und Guides für KI-Architekturen |

---

## 9. Glossar

| Begriff | Erklärung |
|---|---|
| **Agent** | Ein spezialisierter Teil der KI, der eine bestimmte Rolle (z. B. Planer) übernimmt. |
| **Briefing** | Das Start-Dokument mit den Kundenwünschen. |
| **CLI** | "Command Line Interface" – Die Steuerung per Texteingabe im Terminal. |
| **LLM** | "Large Language Model" – Das Gehirn der KI (z. B. GPT-4, Llama). |
| **Markdown** | Ein einfaches Textformat für Dokumente (Dateiendung `.md`). |
| **Orchestrator** | Das Steuerungsprogramm, das die Agenten koordiniert. |
| **Workstream** | Ein spezifischer Arbeitsbereich (z. B. Logistik oder Kommunikation). |

---

*Dokument erstellt von Gemini CLI am 1. Juni 2026.*
