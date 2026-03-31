# AP-028: Agenda erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-028 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 20.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Eine vollständige, finale Agenda für alle 3 Event-Tage erstellen, die Räume, Zeitslots und Session-Zuordnungen enthält und zur Veröffentlichung auf der Website bereit ist.

## Voraussetzungen (Abhängigkeiten)
- AP-027: CfP-Einreichungen sichten und bewerten (Akzeptierte Sessions bekannt)
- AP-020: Raumplanung erstellen (Räume und Kapazitäten bekannt)

## Eingaben (Inputs)
- `workstreams/programm/cfp-entscheidungen.md` – akzeptierte Sessions mit Formaten
- `workstreams/venue-logistik/raumplanung.md` – verfügbare Räume und Kapazitäten
- `workstreams/programm/programm-tracks.md` – Track-Struktur und Zeitgerüst

## Aufgaben (Checkliste)
- [ ] Zeitgerüst der 3 Tage festlegen: Startzeiten, Endzeiten, Pause-Fenster, gemeinsame Plenarsessions
- [ ] Keynote-Slots planen: mind. 2 Keynotes (Eröffnung Tag 1, Abschluss Tag 3)
- [ ] Sessions auf Zeitslots und Räume aufteilen (kein Konflikt zwischen gleichzeitigen Sessions, die sich überschneiden)
- [ ] Parallele Tracks für Tag 2 planen (Track 1, 2, 3 gleichzeitig in verschiedenen Räumen)
- [ ] Workshop-Slots für Tag 3 planen (2 parallele Workshops)
- [ ] Hackathon-Block planen (Tag 3, mit Präsentation)
- [ ] Networking-Dinner für Abend Tag 1 eintragen
- [ ] Puffer/Flex-Slots einplanen (für Verzögerungen)
- [ ] Agenda in `workstreams/programm/agenda.md` in Tabellenform erstellen
- [ ] Agenda für Website aufbereiten

## Ausgaben (Outputs)
- `workstreams/programm/agenda.md` – vollständige 3-Tages-Agenda in Tabellenform (Datum | Uhrzeit | Raum | Session | Speaker)

## Hinweise für den Agenten
- Die Agenda muss bis 31.07.2026 finalisiert und veröffentlicht sein (laut `config/event.yaml: program_final`).
- Plane Raumwechsel-Puffer von mind. 10–15 Minuten zwischen Sessions ein.
- Achte auf ausgewogene Track-Inhalte: kein Track sollte deutlich weniger Sessions haben als die anderen.
