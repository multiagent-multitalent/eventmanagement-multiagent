# AP-010: CfP-Text verfassen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-010 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 22.04.2026 – 28.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Einen ansprechenden, vollständigen Call-for-Papers-Text erstellen, der zur Veröffentlichung am 30.04.2026 bereit ist und qualitativ hochwertige Einreichungen aus der KI-Community anzieht.

## Voraussetzungen (Abhängigkeiten)
- AP-006: Programm-Tracks konzipieren
- AP-007: CfP-Bewertungsrubrik erstellen

## Eingaben (Inputs)
- `workstreams/programm/programm-tracks.md` – Track-Definitionen und Sessionformate
- `workstreams/programm/cfp-bewertungsrubrik.md` – Bewertungskriterien
- `config/event.yaml` – Event-Daten, Datum, Ort

## Aufgaben (Checkliste)
- [ ] Einleitungstext verfassen: Was ist AITD 2026? Warum sollte man einreichen?
- [ ] Thematischen Fokus beschreiben: AI Transparency, Safety, Governance, Human Compatible AI
- [ ] Alle 3 Tracks mit Titeln und typischen Themenbeispielen beschreiben
- [ ] Alle Sessionformate mit Dauer und Anforderungen beschreiben (Vortrag 20min, Panel 45min, Lightning Talk 5min, Workshop 90min)
- [ ] Einreichungsprozess erklären: Was muss eingereicht werden? (Titel, Abstract, Bio, Erfahrungslevel, technische Anforderungen)
- [ ] Deadlines klar hervorheben: Einreichungsdeadline 15.06.2026, Benachrichtigung bis ca. 15.07.2026
- [ ] Speaker-Konditionen kommunizieren: Ticket inklusive? Reisekostenerstattung?
- [ ] Diversitäts-Statement hinzufügen
- [ ] CfP-Text auf Deutsch und Englisch verfassen
- [ ] Text in `workstreams/programm/cfp-text.md` speichern

## Ausgaben (Outputs)
- `workstreams/programm/cfp-text.md` – vollständiger CfP-Text in Deutsch und Englisch, zur sofortigen Veröffentlichung bereit

## Hinweise für den Agenten
- Der CfP-Text muss bis 30.04.2026 fertig und freigegeben sein (Veröffentlichungsdatum laut `config/event.yaml`).
- Schreibe den Text einladend und ermutigend – besonders für Early-Career-Researcher und Praktikerinnen, die vielleicht zum ersten Mal einreichen.
- Füge einen konkreten Link-Platzhalter für die Einreichungsplattform ein (z.B. `[EINREICHUNGSLINK]`).
