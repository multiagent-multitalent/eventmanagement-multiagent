# AP-014: Catering-Konzept entwickeln

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-014 |
| **Workstream** | Catering |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🟢 Normal |
| **Zeitraum** | 22.04.2026 – 30.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Ein vollständiges Catering-Konzept erstellen, das alle Verpflegungsbedarfe über 3 Tage abdeckt, Anbieter identifiziert und als Grundlage für die Catering-Beauftragung (AP-022) dient.

## Voraussetzungen (Abhängigkeiten)
- AP-005: Venue-Anforderungen definieren (Catering-Infrastruktur der Venue muss bekannt sein)

## Eingaben (Inputs)
- `workstreams/venue-logistik/venue-anforderungen.md` – Catering-Infrastruktur der Venue
- `config/event.yaml` – Teilnehmerzahl (125), Format (3 Tage), Datum

## Aufgaben (Checkliste)
- [ ] Catering-Bedarfsplan erstellen: pro Tag und Mahlzeit (Morgen-Kaffee, Mittagessen, Kaffeepausen, Abendessen Tag 1/2)
- [ ] Menü-Optionen vorschlagen: Standard, Vegetarisch, Vegan, Glutenfrei (Anteilsschätzungen)
- [ ] Get-Together/Networking-Dinner-Format für Tag 1 abends entwickeln
- [ ] Nachhaltigkeits-Anforderungen formulieren (regionale Produkte, Mehrweg, Foodwaste-Reduktion)
- [ ] Externe Catering-Anbieter in Nürnberg recherchieren (mind. 3 Anbieter)
- [ ] Prüfen, ob Venue eigenes Catering anbietet vs. externer Caterer bevorzugt
- [ ] Preisschätzung pro Person/Tag für Budgetplanung erstellen
- [ ] Anforderungen an Catering-Setup beschreiben (Buffet vs. Menü, Stellfläche, Personal)
- [ ] Konzept in `workstreams/catering/catering-konzept.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/catering/catering-konzept.md` – vollständiges Catering-Konzept mit Menüplan, Anbieter-Recherche und Budgetschätzung

## Hinweise für den Agenten
- Plane konservativ: Bei 125 Teilnehmenden solltest du ca. 30% vegetarisch, 15% vegan und 10% glutenfrei einplanen (Richtwerte können beim Registrierungsformular angepasst werden).
- Ein Networking-Dinner am ersten Abend ist ein wichtiges Community-Building-Element – plane es als separates Event mit entsprechendem Atmosphäre-Konzept.
- Die finale Catering-Beauftragung (AP-022) kann erst nach Venue-Buchung (AP-015) erfolgen, da Venue und Caterer oft gekoppelt sind.
