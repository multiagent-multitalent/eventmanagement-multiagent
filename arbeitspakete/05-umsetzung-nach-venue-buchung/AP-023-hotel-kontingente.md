# AP-023: Hotel-Kontingente vereinbaren

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-023 |
| **Workstream** | Unterkunft & Anreise |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 08.05.2026 – 25.05.2026 |
| **Status** | ⬜ Offen |

## Ziel
Mit mindestens 2–3 Hotels in Nürnberg Zimmerkontingente zu Sonderpreisen für AITD-2026-Teilnehmende vereinbaren.

## Voraussetzungen (Abhängigkeiten)
- AP-012: Hotel-Recherche (Shortlist und erste Kontakte)

## Eingaben (Inputs)
- `workstreams/unterkunft-anreise/hotel-recherche.md` – Hotel-Shortlist mit Kontakten
- `config/event.yaml` – Datum (14.–16. Oktober 2026), Teilnehmerzahl (125)

## Aufgaben (Checkliste)
- [ ] Hotels aus Shortlist (AP-012) kontaktieren und Kontingent-Angebot anfragen
- [ ] Konditionen aushandeln: Sonderpreis für AITD-Teilnehmende, Buchungscode, Stornofristen
- [ ] Kontingent-Größen festlegen: Budget-Hotel (30 Zimmer), Standard (20 Zimmer), Superior (10 Zimmer)
- [ ] Abruftermin vereinbaren (bis wann müssen nicht abgerufene Zimmer zurückgegeben werden)
- [ ] Barrierefreie Zimmer-Kontingent sichern (mind. 2–3 Zimmer)
- [ ] Kontingent-Buchungslinks oder Codes erhalten
- [ ] Kontingente in `workstreams/unterkunft-anreise/hotel-kontingente.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/unterkunft-anreise/hotel-kontingente.md` – Kontingent-Übersicht mit Buchungslinks, Preisen und Abrufterminen

## Hinweise für den Agenten
- Hotels im Oktober in Nürnberg sind aufgrund von Messen schnell ausgebucht – handele Kontingente früh (Mai 2026) ab.
- Wähle Hotels, die mit ÖPNV gut zur Venue erreichbar sind – das ist ein wichtiges Argument für internationale Gäste.
- Die Hotel-Infos fließen in AP-026 (Anreise-Informationen) und AP-036 (Teilnehmer-Infopakete).
