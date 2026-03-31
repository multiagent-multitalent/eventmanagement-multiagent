# AP-020: Raumplanung erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-020 |
| **Workstream** | Venue & Logistik |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 08.05.2026 – 20.05.2026 |
| **Status** | ⬜ Offen |

## Ziel
Einen detaillierten Raumbelegungsplan für alle 3 Event-Tage erstellen, der die Zuordnung aller Programm-Formate zu konkreten Räumen dokumentiert und als Grundlage für Beschilderung und Helfer-Briefing dient.

## Voraussetzungen (Abhängigkeiten)
- AP-015: Venue buchen (konkrete Räumlichkeiten müssen bekannt sein)
- AP-006: Programm-Tracks konzipieren (Format-Bedarf muss bekannt sein)

## Eingaben (Inputs)
- `workstreams/venue-logistik/venue-buchung.md` – konkrete Räume, Kapazitäten, Technik-Ausstattung
- `workstreams/programm/programm-tracks.md` – Tracks und Sessionformate
- `workstreams/technik/technik-anforderungen.md` – Technik-Bedarf pro Raumtyp

## Aufgaben (Checkliste)
- [ ] Alle verfügbaren Räume der Venue inventarisieren: Name, Fläche, Kapazität, Technik-Grundausstattung
- [ ] Raumzuordnung für Tag 1 (14.10.2026): Eröffnung/Hauptbühne, Keynotes, Plenarsession
- [ ] Raumzuordnung für Tag 2 (15.10.2026): Track 1, Track 2, Track 3 + Panel-Räume
- [ ] Raumzuordnung für Tag 3 (16.10.2026): Workshops (2 Räume), Hackathon (Großfläche)
- [ ] Nebenräume zuweisen: Registration/Check-In, Pressebüro, Speaker-Lounge/Grünes Zimmer, Garderoben
- [ ] Cateringflächen einzeichnen: Foyer, Mittagessen-Bereich, Kaffeestationen
- [ ] Bestuhlungspläne pro Raum erstellen (Kino, Theater, Bistro, U-Form, Tische für Hackathon)
- [ ] Raum-Nummern/-Namen für Beschilderung festlegen
- [ ] Auf-/Abbauplan für 13.10. (Aufbautag) erstellen
- [ ] Raumplanung in `workstreams/venue-logistik/raumplanung.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/venue-logistik/raumplanung.md` – vollständiger Raumbelegungsplan mit Bestuhlung, Technik, Catering-Flächen für alle 4 Tage (13.–16.10.)

## Hinweise für den Agenten
- Koordiniere die Raumplanung mit der Venue-Ansprechperson – manche Räume haben fixe Bestuhlung oder Mindestkapazitäten.
- Plane ausreichend Laufwege und Pufferzeiten zwischen parallelen Sessions ein (Raumwechsel-Zeit: mind. 10 Minuten).
- Die Raumplanung ist Grundlage für Beschilderung (AP-038) und Helfer-Schichtplan (AP-035) – gestalte sie deshalb klar und übersichtlich.
