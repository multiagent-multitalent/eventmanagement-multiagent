# AP-050: Feedback auswerten

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-050 |
| **Workstream** | Nachbereitung |
| **Agent** | Koordination (`.claude/agents/koordination.md`) |
| **Phase** | Phase 6: Nachbereitung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 25.10.2026 – 07.11.2026 |
| **Status** | ⬜ Offen |

## Ziel
Die gesammelten Feedback-Daten systematisch auswerten und einen Feedback-Bericht erstellen, der konkrete Erkenntnisse und Handlungsempfehlungen für AITD 2027 liefert.

## Voraussetzungen (Abhängigkeiten)
- AP-048: Feedback-Survey (Umfrage-Rücklauf-Deadline abgelaufen)

## Eingaben (Inputs)
- Rohdaten aus der Feedback-Umfrage (CSV-Export)
- `workstreams/nachbereitung/event-protokoll.md` – Event-Protokoll mit Vorfällen und Beobachtungen

## Aufgaben (Checkliste)
- [ ] Feedback-Rohdaten exportieren und in Analysetabelle überführen
- [ ] Quantitative Auswertung: Mittelwerte und Verteilung für alle bewerteten Aspekte berechnen
- [ ] NPS-Score berechnen und interpretieren
- [ ] Qualitative Auswertung: offene Antworten lesen, Themen/Muster identifizieren
- [ ] Top-3 Stärken des Events identifizieren (was wurde besonders positiv bewertet)
- [ ] Top-3 Verbesserungspotenziale identifizieren (was wurde kritisiert)
- [ ] Besondere Vorkommnisse aus Event-Protokoll einbeziehen
- [ ] Vergleich: Erwartungen vs. Realität (Feedbacks der Teilnehmenden im Kontext der ursprünglichen Ziele)
- [ ] Feedback-Bericht in `workstreams/nachbereitung/feedback-auswertung.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/nachbereitung/feedback-auswertung.md` – Feedback-Bericht mit quantitativen Ergebnissen, qualitativen Themen und Handlungsempfehlungen

## Hinweise für den Agenten
- Bleibe beim Interpretieren des Feedbacks sachlich und konstruktiv – auch kritisches Feedback ist wertvoll.
- Unterscheide zwischen strukturellen Problemen (müssen für AITD 2027 geändert werden) und Einzelmeinungen.
- Der Feedback-Bericht fließt direkt in die Lessons Learned (AP-051) ein – gestalte ihn entsprechend handlungsorientiert.
