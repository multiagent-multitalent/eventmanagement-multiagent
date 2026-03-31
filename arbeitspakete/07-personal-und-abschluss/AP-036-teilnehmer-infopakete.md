# AP-036: Teilnehmer-Infopakete erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-036 |
| **Workstream** | Teilnehmer-Management |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 20.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Ein vollständiges Teilnehmer-Infopaket zusammenstellen, das alle notwendigen Informationen für Teilnehmende enthält und ca. 2 Wochen vor dem Event per E-Mail versendet wird.

## Voraussetzungen (Abhängigkeiten)
- AP-030: Speaker-Briefings (Venue-Details bekannt und kommuniziert)
- AP-026: Anreise-Infos erstellen

## Eingaben (Inputs)
- `workstreams/programm/agenda.md` – Programm-Übersicht
- `workstreams/unterkunft-anreise/anreise-infos.md` – Anreise und Hotels
- `workstreams/unterkunft-anreise/hotel-kontingente.md` – Hotel-Buchungslinks
- `workstreams/venue-logistik/venue-buchung.md` – Venue-Adresse

## Aufgaben (Checkliste)
- [ ] Inhalte des Infopaketes festlegen: Programm-Übersicht, Venue-Infos, Anreise, Hotels, Check-In-Prozess, Verhaltensregeln/Code of Conduct, Networking-Möglichkeiten, Praktische Tipps (Nürnberg)
- [ ] Infopaket in einem ansprechenden Format erstellen (PDF oder strukturierte E-Mail)
- [ ] Code of Conduct des Events aufnehmen
- [ ] FAQ-Sektion für häufige Fragen entwickeln
- [ ] Kontaktdaten für Rückfragen am Event-Tag angeben
- [ ] Infopaket-Versand-Timing planen: 2 Wochen vor Event (ca. 01.10.2026), 3 Tage Reminder
- [ ] Infopaket in `workstreams/teilnehmer/infopaket.md` ablegen

## Ausgaben (Outputs)
- `workstreams/teilnehmer/infopaket.md` – vollständiges Teilnehmer-Infopaket, versandbereit

## Hinweise für den Agenten
- Das Infopaket wird von COAI versendet (nach Übergabe) – gestalte es so, dass es ohne weitere Anpassung direkt versandt werden kann.
- Füge eine Checkliste für Teilnehmende ein: Was sollte man mitbringen? (Laptop, Ladekabel, Visitenkarten etc.)
- Weise explizit auf die Foto-/Videodokumentation des Events hin und erkläre, wie Teilnehmende dem widersprechen können.
