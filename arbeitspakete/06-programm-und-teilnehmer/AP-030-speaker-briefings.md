# AP-030: Speaker-Briefings erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-030 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 20.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Individuelle Speaker-Briefing-Dokumente erstellen und an alle bestätigten Speaker versenden, sodass diese alle relevanten Informationen für ihre Präsentation haben.

## Voraussetzungen (Abhängigkeiten)
- AP-028: Agenda erstellen (Zeitslot und Raum des Speakers muss bekannt sein)
- AP-029: Speaker-Zusagen einholen (alle bestätigten Speaker müssen bekannt sein)

## Eingaben (Inputs)
- `workstreams/programm/agenda.md` – Zeitslots und Raumzuordnungen
- `workstreams/programm/speaker-zusagen.md` – bestätigte Speaker mit Kontaktdaten
- `workstreams/venue-logistik/venue-buchung.md` – Venue-Details
- `workstreams/unterkunft-anreise/anreise-infos.md` – Anreise-Informationen

## Aufgaben (Checkliste)
- [ ] Speaker-Briefing-Template erstellen: Event-Überblick, Datum/Zeit/Raum des Slots, technische Ausstattung, Vortragsdauer und Q&A-Zeit, Code of Conduct, Kontaktperson bei Fragen
- [ ] Für jeden bestätigten Speaker ein individualisiertes Briefing erstellen
- [ ] Praktische Informationen einfügen: Anfahrt, Check-In-Prozess, Speaker-Lounge, Verpflegung
- [ ] Technische Informationen: Präsentation vorab einreichen (bis wann?), verfügbare Anschlüsse (HDMI, USB-C)
- [ ] Code of Conduct des Events an alle Speaker kommunizieren
- [ ] Briefings per E-Mail an alle Speaker versenden
- [ ] Bestätigung des Erhalts anfordern
- [ ] Briefings in `workstreams/programm/speaker-briefings.md` ablegen

## Ausgaben (Outputs)
- `workstreams/programm/speaker-briefings.md` – Speaker-Briefing-Template und Versand-Protokoll

## Hinweise für den Agenten
- Das Briefing muss so klar sein, dass Speaker keine Rückfragen haben – teste es an einem Test-Leser.
- Bitte alle Speaker, ihre Präsentationsfolien mindestens 48h vor ihrem Slot einzureichen (spart Zeit beim Aufbau).
- Weise explizit auf die Aufzeichnungs-Situation hin: Wird die Session gefilmt? Gibt es Live-Stream? Speaker müssen einwilligen.
