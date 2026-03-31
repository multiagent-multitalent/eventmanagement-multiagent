# AP-006: Programm-Tracks konzipieren

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-006 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 08.04.2026 – 14.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Die 3 inhaltlichen Programm-Tracks der AITD 2026 konzipieren und mit Themen, Zielgruppen und Sessionformaten beschreiben – als Grundlage für die Speaker-Kuration und die spätere Agenda (AP-028).

## Voraussetzungen (Abhängigkeiten)
- AP-001: Event-Konzept finalisieren

## Eingaben (Inputs)
- `workstreams/programm/event-konzept.md` – Themen (AI Transparency, Safety, Governance, Human Compatible AI)
- `config/event.yaml` – Format (3 Tracks, Konferenz + Workshops + Hackathon)

## Aufgaben (Checkliste)
- [ ] Namen und inhaltliche Schwerpunkte für Track 1 definieren (Vorschlag: „AI Transparency & Explainability")
- [ ] Namen und inhaltliche Schwerpunkte für Track 2 definieren (Vorschlag: „AI Safety & Governance")
- [ ] Namen und inhaltliche Schwerpunkte für Track 3 definieren (Vorschlag: „Human Compatible AI & Society")
- [ ] Für jeden Track: Zielgruppe(n) benennen, Sessionformate festlegen (Vorträge 20min, Panels 45min, Lightning Talks 5–10min)
- [ ] Workshop-Formate definieren (Hands-on, Dauer 90–120 min, max. 25 Teilnehmende)
- [ ] Hackathon-Konzept skizzieren (Thema, Teamgröße, Dauer, Ergebnispräsentation)
- [ ] Programm-Zeitplan-Gerüst für 3 Tage entwerfen (Zeitblöcke, Pausen, gemeinsame vs. parallele Sessions)
- [ ] Keynote-Format und -Erwartungen definieren (Anzahl, Dauer, internationale vs. nationale Speaker)
- [ ] Track-Konzepte in `workstreams/programm/programm-tracks.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/programm/programm-tracks.md` – Track-Definitionen mit Themen, Formaten, Zielgruppen und Zeitgerüst

## Hinweise für den Agenten
- Die Track-Namen sollten auf Englisch sein (internationale Zielgruppe), die Beschreibungen können zweisprachig sein.
- Das Zeitgerüst muss die 3-tägige Struktur des Events widerspiegeln: Tag 1 eher Eröffnung/Keynotes, Tag 2 parallele Tracks, Tag 3 Workshops/Hackathon.
- Plane explizit Networking-Zeit ein (Kaffeepausen, Mittagessen, abendliches Get-together).
