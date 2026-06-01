# CHANGELOG — Event Management Multi-Agent System

Dieses Dokument protokolliert alle wesentlichen Änderungen am Projekt in umgekehrt chronologischer Reihenfolge.

---

## [2026-04-28] UX-Verbesserungen & Erweitertes Logging

**Art:** UX & Dokumentation
**Auslöser:** Feedback zur Benutzerfreundlichkeit der Streamlit-Anwendung (vor der vollständigen Migration) und Bedarf an detaillierterer Traceability.

### Neu

- **Dokumentations-Modul:** Einführung eines dedizierten Moduls zur Verwaltung von Agenten-Logs.
- **Real-time Logging:** Unterstützung für Echtzeit-Logging in Dashboard und Graph-Ansichten.
- **Eingabe-Validierung:** Robuste Validierung für Benutzerinteraktionen in der App.

### Geändert

- **Sidebar-Struktur:** Klarere Gliederung der Sidebar für bessere Navigation.
- **Output-Formate:** Umstellung auf benutzerfreundlichere Formate für Agenten-Ergebnisse.

---

## [2026-04-14] Refactoring: Streamlit → Terminal-CLI + Markdown

**Art:** Architektur-Shift
**Auslöser:** Wunsch nach einer robusteren, CI/CD-fähigen Architektur und Abkehr von der Browser-Abhängigkeit für Kernfunktionen.

### Was geändert wurde

- **Terminal-CLI (`src/cli.py`):** Neue primäre Schnittstelle basierend auf der `rich`-Library. Unterstützt Tabellen, Fortschrittsbalken und interaktive Auswahl.
- **Markdown-Logging System:** Komplette Umstellung von JSON-basierten Logs (`PLANUNGSLOG.json`) auf strukturierte Markdown-Dateien (`PLANUNGSLOG.md`).
- **Delegation:** `src/main.py` delegiert nun direkt an die neue CLI-Logik.
- **Bereinigung:** Streamlit-Abhängigkeiten aus `requirements.txt` entfernt.

### Verifikation

| Komponente | Status | Details |
|---|---|---|
| CLI-Einstieg | ✅ Funktioniert | `python -m src.cli` |
| Markdown-Logger | ✅ Aktiv | Erzeugt strukturierte Logs in `workstreams/` |
| Rich-UI | ✅ Implementiert | Farbige Terminal-Ausgabe & Progress-Bars |

---

## [2026-04-13] Execution Logging für Planungs-Agenten

**Art:** Feature
**Details:** Implementierung einer detaillierten Protokollierung der Agenten-Ausführung, um die Entscheidungsprozesse transparenter zu machen.

---

## [2026-03-31] Universal-Repository & AITD 2026 Demo

**Art:** Content & Struktur
**Auslöser:** Das Repository wurde von einem spezifischen Event-Planer zu einem universellen Framework für beliebige Events umgebaut.

### Neu

- **Demo-Event:** "AI Transparency Days 2026" (AITD 2026) als Referenz-Beispiel in `examples/aitd-2026/`.
- **Arbeitspakete (APs):** Erstellung von 52 detaillierten Arbeitspaketen in 10 Blöcken (AP-001 bis AP-052) unter `arbeitspakete/`.
- **Agentic Workflows:** Neuer Ordner `agentic-workflows/` mit Vergleichen von 7 Frameworks (n8n, LangGraph, CrewAI, etc.) und Guides für lokale KI-Modelle.

---

## [2026-03-30] Initialer Setup & Repository-Struktur

**Art:** Initialisierung

### Neu

- **Basis-Struktur:** Einrichtung der Verzeichnisse `src/`, `docs/`, `templates/`, `config/`, `workstreams/`, `dashboard/` und `archiv/`.
- **Dokumentation:** Erstellung von `CLAUDE.md`, `README.md` und ersten Prozessbeschreibungen im `docs/`-Ordner.
- **Phasenmodell:** Definition des 10-Phasen-Modells für das Event-Management.

---

## [2026-03-23] Projektstart

- Initialer Commit und Projekt-Setup.
