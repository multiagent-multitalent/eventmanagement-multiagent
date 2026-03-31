# AP-012: Hotel-Recherche

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-012 |
| **Workstream** | Unterkunft & Anreise |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 22.04.2026 – 30.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Geeignete Hotels in der Nähe der Venue (noch TBD) recherchieren, Kontingent-Möglichkeiten prüfen und eine Empfehlung für die Hotel-Kontingent-Vereinbarungen (AP-023) vorbereiten.

## Voraussetzungen (Abhängigkeiten)
- AP-001: Event-Konzept finalisieren (Datum und Ort bekannt)

## Eingaben (Inputs)
- `config/event.yaml` – Datum (14.–16. Oktober 2026), Ort Nürnberg, Teilnehmerzahl 125

## Aufgaben (Checkliste)
- [ ] Recherche: Hotels in Nürnberg in der Nähe des Hauptbahnhofs und möglicher Venue-Standorte
- [ ] Preisklassen abdecken: Budget (bis 80€/Nacht), Standard (80–150€/Nacht), Superior (150€+/Nacht)
- [ ] Pro Hotel ermitteln: Name, Adresse, Preisklasse, Zimmeranzahl, Entfernung zur Venue, ÖPNV-Anbindung, Website
- [ ] Kontingent-Optionen prüfen: Können Hotels Gruppen-Kontingente mit speziellem Preis und Buchungscode anbieten?
- [ ] Mind. 3 Hotels pro Preisklasse auf Shortlist setzen
- [ ] Kontakt zu Top-3 Empfehlungen aufnehmen und Verfügbarkeit für Oktober 2026 anfragen
- [ ] Frühbuchervorteile und Stornierungsbedingungen vergleichen
- [ ] Barrierefreie Zimmer-Verfügbarkeit prüfen
- [ ] Ergebnisse in `workstreams/unterkunft-anreise/hotel-recherche.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/unterkunft-anreise/hotel-recherche.md` – Hotel-Vergleich mit Empfehlungen für Kontingent-Vereinbarungen

## Hinweise für den Agenten
- Der Oktober ist Messezeit in Nürnberg (Nürnberger Messen) – prüfe Messetermine im Oktober 2026 auf mögliche Kapazitätsengpässe.
- Empfehle mindestens eine günstige Option für Studierende und eine komfortable Option für internationale Gäste/Keynote-Speaker.
- Die endgültige Hotel-Buchung (Kontingente) erfolgt in AP-023, sobald die Venue gebucht ist.
