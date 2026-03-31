# AP-031: Session-Steckbriefe erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-031 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 22.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Für jede Session einen kompakten Steckbrief erstellen, der auf der Website, im Programm-Heft und in der Event-App verwendet werden kann.

## Voraussetzungen (Abhängigkeiten)
- AP-028: Agenda erstellen (alle Sessions mit Zeitslots bekannt)
- AP-030: Speaker-Briefings (Speaker-Bio und Foto gesammelt)

## Eingaben (Inputs)
- `workstreams/programm/agenda.md` – alle Sessions mit Zeitslots
- `workstreams/programm/speaker-zusagen.md` – Speaker-Bios und Fotos
- Speaker-Informationen (Bios, Abstracts) von Speakern erhalten

## Aufgaben (Checkliste)
- [ ] Steckbrief-Template erstellen: Titel, Speaker (Name, Affiliation, Foto-URL), Abstract (max. 200 Wörter), Format, Track, Datum/Uhrzeit/Raum, Tags/Keywords
- [ ] Für jede akzeptierte Session einen Steckbrief ausfüllen
- [ ] Abstracts ggf. kürzen oder präzisieren (mit Genehmigung der Speaker)
- [ ] Tags und Keywords für jede Session vergeben (für Filterfunktion auf Website)
- [ ] Steckbriefe auf inhaltliche Konsistenz prüfen (keine Wiederholungen, Überschneidungen korrekt markiert)
- [ ] Steckbriefe in maschinenlesbarem Format speichern (Markdown oder JSON)
- [ ] Website-Update mit Session-Steckbriefen koordinieren
- [ ] Alle Steckbriefe in `workstreams/programm/session-steckbriefe.md` sammeln

## Ausgaben (Outputs)
- `workstreams/programm/session-steckbriefe.md` – alle Session-Steckbriefe in einheitlichem Format, bereit für Website und Programm-Heft

## Hinweise für den Agenten
- Die Steckbriefe müssen für zwei Zielgruppen funktionieren: technisch versierte Fachleute (detaillierter Abstract) und interessierte Laien (verständliche Kurzbeschreibung).
- Halte Tags und Keywords konsistent – nutze eine vordefinierte Tag-Taxonomie (z.B. aus den Track-Themen).
- Plane die Steckbriefe so, dass sie auch in einem gedruckten Programm-Heft (A5, 2 Seiten) funktionieren.
