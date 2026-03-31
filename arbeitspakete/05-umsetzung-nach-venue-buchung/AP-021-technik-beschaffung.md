# AP-021: Technik beschaffen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-021 |
| **Workstream** | Technik |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 08.05.2026 – 31.05.2026 |
| **Status** | ⬜ Offen |

## Ziel
Alle Technik-Komponenten, die nicht durch die Venue gestellt werden, beschaffen oder leihen und sicherstellen, dass am Aufbautag (13.10.2026) alle Geräte verfügbar sind.

## Voraussetzungen (Abhängigkeiten)
- AP-015: Venue buchen (was stellt die Venue, was muss extern beschafft werden?)
- AP-011: Technik-Anforderungen konkretisieren

## Eingaben (Inputs)
- `workstreams/technik/technik-anforderungen.md` – vollständiger Anforderungskatalog
- `workstreams/venue-logistik/venue-buchung.md` – Technik-Inklusivleistungen der Venue

## Aufgaben (Checkliste)
- [ ] Delta berechnen: Technik-Anforderungen MINUS was die Venue stellt = was muss extern beschafft werden
- [ ] Externe Beschaffungsoptionen prüfen: mieten (AV-Verleiher Nürnberg) vs. kaufen vs. von COAI/Hochschule leihen
- [ ] Angebote von mind. 2 AV-Verleihern einholen
- [ ] Entscheidung Mieten/Kaufen treffen (kostenoptimiert, unter Budget-Rahmen aus AP-002)
- [ ] Bestellungen/Buchungen aufgeben (mit Liefertermin 12.10. oder spätestens 13.10.2026)
- [ ] Aufzeichnungs-/Streaming-Setup beschaffen (Kameras, Mikrofone, Capture-Cards, Software)
- [ ] Backup-Technik sichern (HDMI-Adapter-Set, Verlängerungskabel, Spare-Mikros)
- [ ] Technik-Briefing-Unterlagen für Helfer vorbereiten
- [ ] Beschaffungsübersicht in `workstreams/technik/technik-beschaffung.md` erstellen

## Ausgaben (Outputs)
- `workstreams/technik/technik-beschaffung.md` – vollständige Beschaffungsliste mit Kosten, Lieferanten und Lieferterminen

## Hinweise für den Agenten
- Bestelle/buche Technik so früh wie möglich – AV-Equipment ist in Oktober (Messezeit in Nürnberg) oft knapp.
- Erstelle eine detaillierte Packliste für den Aufbautag (was kommt von wo, wer bringt es).
- Plane einen Technik-Testlauf am Aufbautag ein (13.10.2026, nachmittags) – dokumentiere das in der Raumplanung.
