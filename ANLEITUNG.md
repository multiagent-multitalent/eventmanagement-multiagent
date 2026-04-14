# Anleitung: Event-Management Orchestrator

Diese Anleitung zeigt dir Schritt fuer Schritt, wie du das Programm lokal einrichtest, startest und fuer eigene Events nutzt.

## 1. Ziel des Programms

Der Event-Management Orchestrator automatisiert die Planung von Events in zwei Stufen:

1. Stage 1: Recherche von Venue- und Catering-Optionen
2. Stage 2: Erstellung von Planungs- und Kommunikationsartefakten

Ergebnisse werden automatisch in den Workstreams gespeichert.

## 2. Voraussetzungen

- Windows, macOS oder Linux
- Python 3.10+
- Optional: lokales oder externes LLM (z. B. Ollama, LM Studio, LocalAI, OpenAI-kompatibel)

## 3. Installation

Im Projektordner ausfuehren:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Konfiguration

Pflege zuerst die Event- und Teamdaten:

- [config/event.yaml](config/event.yaml)
- [config/team.yaml](config/team.yaml)

Wichtige Felder in [config/event.yaml](config/event.yaml):

- `event.name`
- `event.date_start`, `event.date_end`
- `event.city`
- `event.attendees_expected`
- `topics`, `target_audience`, `milestones`

## 5. LLM konfigurieren (optional, aber empfohlen)

Die Runtime liest Umgebungsvariablen wie:

- `LLM_PROVIDER` (z. B. `ollama`, `lmstudio`, `localai`, `openai_compatible`, `openai`)
- `LLM_MODEL`
- `LLM_BASE_URL`
- `LLM_API_KEY`

Beispiel (PowerShell, Ollama):

```powershell
$env:LLM_PROVIDER="ollama"
$env:LLM_MODEL="llama3.2"
$env:LLM_BASE_URL="http://localhost:11434"
```

Wenn keine Werte gesetzt sind, nutzt das System sinnvolle Defaults.

## 6. Programm starten

### Terminal-CLI (Standard)

```bash
python -m src.cli
```

Ablauf:

1. Event-Daten aus [config/event.yaml](config/event.yaml) werden geladen
2. Wähle Venue (mit Empfehlungen)
3. Wähle Catering-Partner
4. Planung startet automatisch
5. Artefakte und Logs in `workstreams/` prüfen

### Automatischer Modus (keine Interaktion)

```bash
python -m src.cli --auto
```

### Mit spezifischem Modell oder Optionen

```bash
# Mit Venue und Catering vorwählen
python -m src.cli --venue "Nuernberg Convention Center (NCC)" --catering "Kochkollektiv Nuernberg"

# Mit lokalem Ollama-Modell
python -m src.cli --provider ollama --model llama3.2 --base-url http://localhost:11434

# Mit OpenAI oder externem Service
python -m src.cli --provider openai --model gpt-4 --api-key sk-...
```

Die CLI fragt interaktiv nach Venue und Catering, oder nutzt die angegebenen Werte. Siehe [docs/TERMINAL-CLI.md](docs/TERMINAL-CLI.md) für alle verfügbaren Optionen.

## 7. Wo landen die Ergebnisse?

Nach erfolgreichem Lauf erzeugt das System unter [workstreams/](workstreams/):

- [workstreams/PLANUNGSLOG.md](workstreams/PLANUNGSLOG.md) – Master-Log aller Planungsschritte
- [workstreams/programm/](workstreams/programm/) – Agenda, Zeitplan, Speaker
- [workstreams/kommunikation/](workstreams/kommunikation/) – Kommunikationsplan, E-Mail-Anschreiben
- [workstreams/venue-logistik/](workstreams/venue-logistik/) – Venue-Recherche, Logistik-Checklisten
- [workstreams/catering/](workstreams/catering/) – Catering-Konzept und Menü-Entwürfe
- [workstreams/[weitere Bereiche]/](workstreams/) – Teilnehmer, Technik, Personal, Sponsoring, etc.

Alle Outputs sind **Markdown-Dateien** (`.md`) und können in Git verfolgt werden.

Ueberblick und Fortschritt:

- [dashboard/status.md](dashboard/status.md)
- [workstreams/README.md](workstreams/README.md)

## 8. Funktion pruefen (Smoke-Test)

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 9. Typische Probleme und Loesungen

1. `ModuleNotFoundError`
   Ursache: Abhaengigkeiten fehlen.
   Loesung: `pip install -r requirements.txt` erneut ausfuehren.

2. Keine LLM-Antwort / Verbindungsfehler
   Ursache: LLM-Endpunkt nicht erreichbar oder falsche Base-URL.
   Loesung: `LLM_PROVIDER`, `LLM_BASE_URL`, `LLM_MODEL` pruefen und lokalen Dienst starten.

3. Leere oder unvollstaendige Ergebnisse
   Ursache: Konfiguration unvollstaendig.
   Loesung: [config/event.yaml](config/event.yaml) und [config/team.yaml](config/team.yaml) komplett ausfuellen.

## 10. Empfohlener Standardablauf

1. [config/event.yaml](config/event.yaml) und [config/team.yaml](config/team.yaml) pflegen
2. Terminal-CLI starten: `python -m src.cli`
3. Venue und Catering auswählen
4. Automatische Planung läuft
5. Ergebnisse in [workstreams/PLANUNGSLOG.md](workstreams/PLANUNGSLOG.md) prüfen
6. Entscheidungen in [CONFIRM.md](CONFIRM.md) bestätigen
