# AP-002: Budget-Rahmen festlegen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-002 |
| **Workstream** | Venue & Logistik |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 1: Initialisierung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 07.04.2026 – 14.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Einen realistischen Budget-Rahmen für AITD 2026 erstellen, der alle Kostenkategorien mit Schätzwerten abdeckt und als Steuerungsinstrument für alle nachfolgenden Beschaffungs- und Buchungs-APs dient.

## Voraussetzungen (Abhängigkeiten)
- AP-001: Event-Konzept finalisieren (Format und Größe müssen bekannt sein)

## Eingaben (Inputs)
- `config/event.yaml` – Teilnehmerzahl (125), Format, Kategorien
- `workstreams/programm/event-konzept.md` – Event-Format und -Umfang
- `templates/budget/` – Budget-Vorlagen (falls vorhanden)

## Aufgaben (Checkliste)
- [ ] Kostenkategorien aus `config/event.yaml` (venue, catering, technik, kommunikation, personal, drucksachen, sonstiges) mit Platzhaltern befüllen
- [ ] Marktrecherche für Venue-Kosten in Nürnberg (Tagungsräume für ~125 Personen, 3 Tage): Richtwerte ermitteln
- [ ] Catering-Richtwert pro Person/Tag schätzen (Mittagessen, Kaffeepausen, Abendessen)
- [ ] Technik-Budgetanteil schätzen (AV-Ausstattung, Streaming, WLAN)
- [ ] Kommunikations-Budget schätzen (Website, Social Media, Druck)
- [ ] Personal-/Helfer-Kosten abschätzen (Honorare, Aufwandsentschädigungen)
- [ ] Drucksachen-Budget schätzen (Namensschilder, Programm-Hefte, Beschilderung)
- [ ] Einnahmen-Seite skizzieren: Ticketeinnahmen (Schätzung), Sponsoring-Ziel, ggf. Fördermittel
- [ ] Puffer (10–15 %) einplanen
- [ ] Budget-Dokument in `workstreams/venue-logistik/budget-rahmen.md` erstellen

## Ausgaben (Outputs)
- `workstreams/venue-logistik/budget-rahmen.md` – Budget-Rahmen mit Schätzwerten pro Kategorie, Einnahmen-Seite und Puffer

## Hinweise für den Agenten
- Da `total_estimated: TBD` in der Konfiguration steht, muss dieser AP einen realistischen Schätzwert liefern – recherchiere Vergleichswerte für Konferenzen dieser Größenordnung (100–150 Personen) in Bayern.
- Das Budget muss mit der Sponsoring-Strategie (AP-003) kompatibel sein – halte den Anteil, der durch Sponsoring finanziert werden soll, explizit offen.
- Verwende eine Tabelle mit Spalten: Kategorie | Minimum (€) | Realistisch (€) | Maximum (€) | Anmerkungen.
