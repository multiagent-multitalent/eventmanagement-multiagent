# AP-026: Anreise-Informationen erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-026 |
| **Workstream** | Unterkunft & Anreise |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟢 Normal |
| **Zeitraum** | 15.05.2026 – 31.05.2026 |
| **Status** | ⬜ Offen |

## Ziel
Umfassende Anreise-Informationen für Teilnehmende erstellen, die auf der Website publiziert werden und im Teilnehmer-Infopaket (AP-036) verwendet werden.

## Voraussetzungen (Abhängigkeiten)
- AP-015: Venue buchen (genaue Adresse und Lage bekannt)
- AP-023: Hotel-Kontingente vereinbaren (Hotel-Buchungslinks bekannt)

## Eingaben (Inputs)
- `workstreams/venue-logistik/venue-buchung.md` – Venue-Adresse, ÖPNV-Anbindung
- `workstreams/unterkunft-anreise/hotel-kontingente.md` – Hotel-Buchungslinks und -Preise

## Aufgaben (Checkliste)
- [ ] Venue-Adresse und Anfahrtsbeschreibung verfassen
- [ ] ÖPNV-Verbindungen dokumentieren: vom Nürnberger Hauptbahnhof, vom Flughafen, von den Hotel-Kontingenten
- [ ] PKW-Anfahrt: Parkplatzsituation, nächste Parkhäuser, Kosten
- [ ] Zugverbindungen: ICE-Verbindungen nach Nürnberg aus den wichtigsten deutschen Städten
- [ ] Flugverbindungen: Nürnberger Flughafen (NUE), Verbindung zur Venue
- [ ] Hotel-Empfehlungen mit Buchungslinks aus AP-023 einfügen
- [ ] Barrierefreiheit: rollstuhlgerechter Zugang zur Venue und zu den Hotels
- [ ] Anreise-Info-Seite für die Website aufbereiten
- [ ] Anreise-Infos in `workstreams/unterkunft-anreise/anreise-infos.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/unterkunft-anreise/anreise-infos.md` – vollständige Anreise-Informationen für Website und Teilnehmer-Infopaket

## Hinweise für den Agenten
- Berücksichtige, dass AITD 2026 internationale Gäste hat – beschreibe auch internationale Anreise (Flughafen, internationale Zugverbindungen).
- Integriere konkrete ÖPNV-Verbindungen (Liniennummern, Haltestellen) – keine vagen Beschreibungen.
- Empfehle das Deutschlandticket oder Nürnberger Tagestickets als günstige ÖPNV-Option für die Eventtage.
