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

Es gibt zwei Betriebsmodi.

### A) Streamlit-Oberflaeche (empfohlen)

```bash
streamlit run streamlit_app.py
```

Danach im Browser die angezeigte URL oeffnen (typisch `http://localhost:8501`).

Ablauf in der UI:

1. Eventdaten pruefen/anpassen
2. Stage 1 starten (Research)
3. Venue und Catering auswaehlen
4. Stage 2 freigeben
5. Artefakte und Fortschritt im Dashboard pruefen

### B) CLI

```bash
python -m src.main
```

Die CLI fuehrt Stage 1 aus, zeigt Optionen an und fragt interaktiv nach deiner Auswahl.

Nutzliche Parameter:

```bash
python -m src.main --auto
python -m src.main --auto --venue "Nuernberg Convention Center (NCC)" --catering "Kochkollektiv Nuernberg"
python -m src.main --provider ollama --model llama3.2 --base-url http://localhost:11434
```

## 7. Wo landen die Ergebnisse?

Nach erfolgreichem Lauf erzeugt das System unter anderem:

- [workstreams/venue-logistik/venue-recherche.md](workstreams/venue-logistik/venue-recherche.md)
- [workstreams/catering/catering-konzept.md](workstreams/catering/catering-konzept.md)
- [workstreams/programm/agenda-entwurf.md](workstreams/programm/agenda-entwurf.md)
- [workstreams/kommunikation/kommunikationsplan.md](workstreams/kommunikation/kommunikationsplan.md)
- [workstreams/event-planning-output.json](workstreams/event-planning-output.json)

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
2. Streamlit starten: `streamlit run streamlit_app.py`
3. Stage 1 ausfuehren, Auswahl treffen, Stage 2 freigeben
4. Ergebnisse in den Workstreams pruefen
5. Entscheidungen in [CONFIRM.md](CONFIRM.md) bestaetigen
