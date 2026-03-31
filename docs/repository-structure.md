# Repository-Struktur und Ablageregeln

Dieses Dokument definiert die Ablagelogik im Repository, damit neue Artefakte konsistent einsortiert werden.

## Zielbild

Die Struktur trennt zwischen:
- Konfiguration und Steuerung
- fachlicher Planung
- operativer Umsetzung
- Code des Orchestrators

## Top-Level-Bereiche

| Bereich | Zweck | Beispiele |
|---|---|---|
| `config/` | Eingabedaten und Team-Setup | `event.yaml`, `team.yaml` |
| `docs/` | Methodik, Rollen, Leitfaden | `phasenmodell.md`, `rollen.md` |
| `arbeitspakete/` | Phasenbasierter Aufgaben-Masterplan | `01-initialisierung/*`, `04-buchungen-und-veroeffentlichung/*` |
| `workstreams/` | Laufende und generierte Ergebnisartefakte je Bereich | `workstreams/programm/agenda-entwurf.md` |
| `templates/` | Startvorlagen pro Fachbereich | `templates/kommunikation/*` |
| `src/` | Orchestrator-Code (CLI, Dashboard, Agenten, Workflow) | `src/main.py`, `src/workflows/event_planning_graph.py` |
| `dashboard/` | Management-Sicht für Status und Zeitplan | `status.md`, `zeitplan.md` |
| `archiv/` | Entscheidungen und Erkenntnisse | `entscheidungslog.md`, `lessons-learned.md` |
| `examples/` | Referenz-Outputs für Demo-Events | `examples/aitd-2026/` |

## Ablageregeln

1. Neue normative Planungsschritte kommen in `arbeitspakete/`.
2. Neue operative Ausarbeitungen kommen in den passenden `workstreams/<bereich>/`-Ordner.
3. Wiederverwendbare Textbausteine oder Muster kommen in `templates/`.
4. Steuer- und Governance-Dokumente kommen nach `docs/` oder `dashboard/`.
5. Nur produktiver Python-Code gehört nach `src/`; Tests liegen in `tests/`.

## Schnell-Check vor Commits

- Liegt jede neue Datei im richtigen Zielordner nach obigen Regeln?
- Sind neue Workstream-Artefakte im passenden Bereich abgelegt?
- Wurde bei Strukturänderungen auch `README.md` aktualisiert?
- Läuft der Smoke-Test aus `tests/` weiterhin durch?
