# AP-018: Kommunikationsplan erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-018 |
| **Workstream** | Kommunikation & Marketing |
| **Agent** | Kommunikation (`.claude/agents/kommunikation.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 01.05.2026 – 10.05.2026 |
| **Status** | ⬜ Offen |

## Ziel
Einen detaillierten Kommunikationsplan für die gesamte Laufzeit des Events erstellen, der alle geplanten Kommunikationsmaßnahmen, Verantwortlichkeiten und Zeitpunkte dokumentiert.

## Voraussetzungen (Abhängigkeiten)
- AP-004: Kommunikationsstrategie definieren

## Eingaben (Inputs)
- `workstreams/kommunikation/kommunikationsstrategie.md` – Kanäle, Phasen, Key Messages
- `config/event.yaml` – Meilensteine und Daten

## Aufgaben (Checkliste)
- [ ] Kommunikationsphasen in konkrete Wochen aufteilen (April–November 2026)
- [ ] Für jede Phase: geplante Maßnahmen, Kanal, Inhalt-Typ (Post, Newsletter, Pressemitteilung), Verantwortliche/r
- [ ] Pressemitteilungen planen: Ankündigung des Events, Programm-Veröffentlichung, Post-Event-Zusammenfassung
- [ ] Newsletter-Frequenz festlegen (monatlich? bi-wöchentlich?)
- [ ] Social-Media-Rhythmus definieren: wie oft pro Woche auf welchem Kanal
- [ ] Krisenkommunkations-Protokoll skizzieren (was tun bei negativem Feedback, Absagen von Keynote-Speakern etc.)
- [ ] Kommunikationsplan als Tabelle in `workstreams/kommunikation/kommunikationsplan.md` erstellen

## Ausgaben (Outputs)
- `workstreams/kommunikation/kommunikationsplan.md` – detaillierter Kommunikationsplan von April bis November 2026

## Hinweise für den Agenten
- Der Plan muss für COAI nutzbar sein nach der Übergabe (30.06.2026) – dokumentiere auch die Kommunikationsmaßnahmen für Juli–November.
- Plane explizit eine Kommunikation nach Eingang der Speaker-Zusagen (Juni 2026) zur Bekanntgabe des Programms (ca. Ende Juli 2026).
- Integriere die Meilensteine aus `config/event.yaml` als feste Ankerpunkte im Kommunikationsplan.
