# AP-027: CfP-Einreichungen sichten und bewerten

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-027 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 15.06.2026 – 25.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Alle CfP-Einreichungen systematisch sichten, nach der Bewertungsrubrik bewerten und eine priorisierte Liste akzeptierter, abgelehnter und auf Warteliste gesetzter Sessions erstellen.

## Voraussetzungen (Abhängigkeiten)
- AP-016: CfP veröffentlichen (Einreichungsplattform muss gelaufen sein)
- CfP-Deadline 15.06.2026 muss verstrichen sein
- AP-007: CfP-Bewertungsrubrik erstellen

## Eingaben (Inputs)
- Alle Einreichungen aus der CfP-Plattform (Export als CSV oder direkter Zugriff)
- `workstreams/programm/cfp-bewertungsrubrik.md` – Bewertungskriterien
- `workstreams/programm/programm-tracks.md` – Track-Definitionen

## Aufgaben (Checkliste)
- [ ] Alle Einreichungen aus der Plattform exportieren und Übersicht erstellen (Anzahl, Verteilung nach Track/Format)
- [ ] Vollständigkeit prüfen: Einreichungen mit fehlenden Pflichtfeldern markieren und ggf. nachfordern
- [ ] Erste Sichtung: Einreichungen nach Tracks sortieren und offensichtliche Off-Topics aussortieren
- [ ] Alle verbliebenen Einreichungen nach Bewertungsrubrik (AP-007) bewerten
- [ ] Interessenkonflikte identifizieren und ausschließen (Reviewer darf eigene Einreichung nicht bewerten)
- [ ] Ranking pro Track erstellen (höchste Bewertung → niedrigste)
- [ ] Entscheidungsliste erstellen: Akzeptiert / Warteliste / Abgelehnt
- [ ] Diversitäts-Check: Gibt die Auswahl die Vielfalt der Community wieder?
- [ ] Entscheidungen in `workstreams/programm/cfp-entscheidungen.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/programm/cfp-entscheidungen.md` – vollständige Bewertungsliste mit Entscheidung und Begründung pro Einreichung

## Hinweise für den Agenten
- Plane für ca. 50–80 Einreichungen und eine Annahmequote von 40–50% (20–35 Sessions gesamt für 3 Tracks × 3 Tage).
- Dokumentiere für jede Ablehnung eine kurze Begründung – diese hilft bei der Kommunikation mit Einreichenden.
- Stelle sicher, dass die finale Auswahl die 3 Tracks ausgewogen befüllt und verschiedene Sessionformate enthält.
