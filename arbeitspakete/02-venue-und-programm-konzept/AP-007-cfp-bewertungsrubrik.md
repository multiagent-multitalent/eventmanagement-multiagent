# AP-007: CfP-Bewertungsrubrik erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-007 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 14.04.2026 – 21.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Eine klare, anwendbare Bewertungsrubrik für CfP-Einreichungen erstellen, die ein faires und nachvollziehbares Review-Verfahren ermöglicht und in AP-027 (Einreichungen sichten) direkt eingesetzt wird.

## Voraussetzungen (Abhängigkeiten)
- AP-006: Programm-Tracks konzipieren (Themen und Formate müssen bekannt sein)

## Eingaben (Inputs)
- `workstreams/programm/programm-tracks.md` – Track-Definitionen und Sessionformate

## Aufgaben (Checkliste)
- [ ] Bewertungsdimensionen definieren (z.B. Relevanz, Originalität, Praxisbezug, Präsentationsqualität, Diversität)
- [ ] Gewichtung der Dimensionen festlegen (Prozentsätze oder Punkte-Skala)
- [ ] Bewertungsskala definieren (z.B. 1–5 Punkte pro Kriterium mit Beschreibung was 1/3/5 Punkte bedeuten)
- [ ] Ausschlusskriterien definieren (was führt zur sofortigen Ablehnung)
- [ ] Bewertungsformular als Markdown-Tabelle oder Checkliste erstellen
- [ ] Reviewer-Leitfaden verfassen (Wie lange dauert eine Bewertung? Wie mit Interessenkonflikten umgehen?)
- [ ] Prozess für Zweitbewertungen bei strittigen Einreichungen festlegen
- [ ] Mindest-Akzeptanzquote und -Ablehnungsquote schätzen (basierend auf erwarteten Einreichungen)
- [ ] Rubrik in `workstreams/programm/cfp-bewertungsrubrik.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/programm/cfp-bewertungsrubrik.md` – Bewertungsrubrik mit Kriterien, Skala, Reviewer-Leitfaden

## Hinweise für den Agenten
- Die Rubrik muss von Personen ohne tiefes KI-Fachwissen nutzbar sein (z.B. für Hilfskräfte, die erste Durchsicht machen).
- Baue explizit ein Kriterium für Diversität ein (Geschlecht, Herkunft, Karrierestufe der Speaker).
- Plane für ca. 50–80 erwartete Einreichungen und eine Annahmequote von ca. 40–50%.
