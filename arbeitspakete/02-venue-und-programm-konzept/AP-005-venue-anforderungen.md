# AP-005: Venue-Anforderungen definieren

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-005 |
| **Workstream** | Venue & Logistik |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 08.04.2026 – 14.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Eine vollständige, priorisierte Anforderungsliste für das Veranstaltungslokal erstellen, die als Grundlage für die Venue-Recherche (AP-009) und Venue-Buchung (AP-015) dient.

## Voraussetzungen (Abhängigkeiten)
- AP-001: Event-Konzept finalisieren
- AP-002: Budget-Rahmen festlegen

## Eingaben (Inputs)
- `workstreams/programm/event-konzept.md` – Format (Konferenz + Workshops + Hackathon, 3 Tracks)
- `workstreams/venue-logistik/budget-rahmen.md` – Venue-Budget
- `config/event.yaml` – Teilnehmerzahl (125), Datum, Ort (Nürnberg)

## Aufgaben (Checkliste)
- [ ] Flächenbedarf kalkulieren: Hauptbühne (125 Pax Kino/Theater-Bestuhlung), 3 Track-Räume (je ~40 Pax), 2 Workshop-Räume (je ~25 Pax), Hackathon-Fläche (~40 Pax)
- [ ] Foyer-/Networking-Fläche einplanen (Catering, Poster-Ausstellung, Sponsor-Stände)
- [ ] Technische Mindestanforderungen festlegen: Projektion, Soundanlage, Mikrofone, WLAN (mind. 100 Mbit/s symmetrisch)
- [ ] Barrierefreiheit als Pflichtanforderung dokumentieren
- [ ] Catering-Infrastruktur prüfen: eigene Küche vs. externer Caterer
- [ ] Lage-Anforderungen: Erreichbarkeit mit ÖPNV (Hauptbahnhof Nürnberg max. 30 min), Parkplätze
- [ ] Verfügbarkeitszeitraum definieren: 13. Oktober (Aufbau), 14.–16. Oktober (Event), 16. Oktober abends (Abbau)
- [ ] Budget-Rahmen für Venue aus AP-002 als Maximalpreis eintragen
- [ ] Anforderungen nach Must-have / Nice-to-have / No-go kategorisieren
- [ ] Anforderungsdokument in `workstreams/venue-logistik/venue-anforderungen.md` erstellen

## Ausgaben (Outputs)
- `workstreams/venue-logistik/venue-anforderungen.md` – priorisierte Anforderungsliste mit Raumliste, Technik, Lage und Budget

## Hinweise für den Agenten
- Das Dokument muss so strukturiert sein, dass es direkt als Briefing an Venues geschickt werden kann (Anfrage-Schreiben in AP-009).
- Plane einen separaten Raum für Speaker-Vorbereitung/Grüne-Zimmer-Funktion ein.
- Berücksichtige, dass ein Hackathon andere Infrastruktur benötigt als Vorträge: Steckdosen an jedem Tisch, stabiles WLAN, flexible Möblierung.
