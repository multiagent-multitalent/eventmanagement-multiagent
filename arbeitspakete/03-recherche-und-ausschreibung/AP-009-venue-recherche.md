# AP-009: Venue-Recherche

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-009 |
| **Workstream** | Venue & Logistik |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 22.04.2026 – 30.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Mindestens 3 geeignete Veranstaltungsorte in Nürnberg identifizieren, Angebote einholen und eine Entscheidungsvorlage für die Venue-Buchung (AP-015) erstellen.

## Voraussetzungen (Abhängigkeiten)
- AP-005: Venue-Anforderungen definieren

## Eingaben (Inputs)
- `workstreams/venue-logistik/venue-anforderungen.md` – vollständige Anforderungsliste mit Must-haves und Budget
- `config/event.yaml` – Datum (13.–16. Oktober 2026), Nürnberg

## Aufgaben (Checkliste)
- [ ] Recherche starten: Tagungszentren, Kongresshäuser, Hochschul-Räumlichkeiten und Co-Working-/Eventlocations in Nürnberg (Radius 5km vom Hauptbahnhof)
- [ ] Kandidaten-Longlist (mind. 6 Orte) erstellen mit Name, Adresse, Kapazität und Website
- [ ] Must-have-Kriterien (aus AP-005) gegen jeden Kandidaten prüfen und Nichterfüller aussortieren
- [ ] Shortlist auf 3–4 Kandidaten reduzieren
- [ ] Anfrage-Schreiben an alle Shortlist-Venues senden (basierend auf Anforderungsdokument)
- [ ] Angebote einholen und dokumentieren: Raummiete (Tages- oder Pauschalpreis), inklusive Technik?, Catering-Optionen, Exklusivnutzung?
- [ ] Vergleichstabelle erstellen: Venue | Preis | Kapazität | Technik | Lage | Verfügbarkeit | Bewertung
- [ ] Empfehlung für Top-2-Venues formulieren
- [ ] Ergebnisse in `workstreams/venue-logistik/venue-recherche.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/venue-logistik/venue-recherche.md` – Vergleichstabelle mit mind. 3 Angeboten und konkreter Empfehlung

## Hinweise für den Agenten
- Prüfe explizit die Verfügbarkeit am 13.–16. Oktober 2026 (einschließlich Aufbautag am 13.10.).
- Wichtige Nürnberger Locations zum Recherchieren: NCC Mitte (Kongress), Meistersingerhalle, Z-Bau, Kulturzentrum Tafelhalle, Hochschul-Locations (FAU, TH Nürnberg).
- Hole immer schriftliche Angebote mit konkreten Preisen ein – keine rein telefonischen Auskünfte.
