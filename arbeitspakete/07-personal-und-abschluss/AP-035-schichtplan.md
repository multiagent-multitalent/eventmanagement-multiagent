# AP-035: Schichtplan erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-035 |
| **Workstream** | Personal & Helfer |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 25.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Einen vollständigen Schichtplan erstellen, der alle Helfer-Rollen für alle 4 Tage (Aufbau 13.10. + Event 14.–16.10.2026) abdeckt und als Übergabe-Dokument an COAI übergeben werden kann.

## Voraussetzungen (Abhängigkeiten)
- AP-034: Helfer rekrutieren (alle Helfer mit Qualifikationen bekannt)
- AP-028: Agenda erstellen (Zeitplan bekannt)

## Eingaben (Inputs)
- `workstreams/personal/helfer-liste.md` – alle Helfer mit Verfügbarkeiten
- `workstreams/programm/agenda.md` – detaillierter Zeitplan
- `workstreams/personal/helferbedarf.md` – Bedarf pro Rolle und Zeit

## Aufgaben (Checkliste)
- [ ] Schichtplan-Vorlage erstellen: Tabelle mit Zeitslots (Zeilen) × Rollen/Orte (Spalten)
- [ ] Helfer den Rollen zuweisen (basierend auf Qualifikation und Verfügbarkeit)
- [ ] Aufbautag (13.10.) vollständig planen: wer kommt wann, welche Aufgaben
- [ ] Tag 1–3 planen: Check-In, Raum-Betreuung, Technik, Catering-Koordination
- [ ] Abbau planen
- [ ] Pausenzeiten für Helfer einplanen (Helfer müssen auch essen und Pausen haben)
- [ ] Schichtplan-Lücken identifizieren und mit Reserve-Helfern schließen
- [ ] Schichtplan an alle Helfer kommunizieren (vorab zur Bestätigung schicken)
- [ ] Schichtplan in `workstreams/personal/schichtplan.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/personal/schichtplan.md` – vollständiger Schichtplan für alle 4 Tage, nach Datum/Uhrzeit/Raum/Person gegliedert

## Hinweise für den Agenten
- Der Schichtplan muss so gestaltet sein, dass COAI ihn am Event-Tag direkt nutzen kann – exportierbar als PDF oder printbar.
- Markiere kritische Rollen (Check-In, Technik) und stelle sicher, dass diese immer doppelt besetzt sind.
- Plane eine Helfer-Kontaktliste für den Event-Tag (Handy-Nummern aller Helfer) als Teil des Dokuments.
