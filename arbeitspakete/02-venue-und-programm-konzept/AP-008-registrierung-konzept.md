# AP-008: Registrierungs-Konzept entwickeln

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-008 |
| **Workstream** | Teilnehmer-Management |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 08.04.2026 – 21.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Ein vollständiges Konzept für das Registrierungssystem entwickeln – von der Tool-Auswahl über Ticket-Kategorien bis hin zum Datenschutz-Konzept – das als Grundlage für die technische Einrichtung (AP-024) dient.

## Voraussetzungen (Abhängigkeiten)
- AP-001: Event-Konzept finalisieren (Format, Größe und Zielgruppen müssen bekannt sein)

## Eingaben (Inputs)
- `workstreams/programm/event-konzept.md` – Event-Format und Zielgruppen
- `config/event.yaml` – Teilnehmerzahl (125 erwartet, max. 150)

## Aufgaben (Checkliste)
- [ ] Registrierungstools evaluieren und auswählen (Pretix, Eventbrite, Tito, selbst gehostet) – DSGVO-Konformität prüfen
- [ ] Ticket-Kategorien definieren: Standardticket, Studierendenticket (ermäßigt), Speaker-Ticket (kostenlos), Sponsor-Ticket
- [ ] Ticket-Preise vorschlagen (basierend auf Budget-Rahmen aus AP-002)
- [ ] Registrierungsfelder festlegen: Name, E-Mail, Affiliation, Verpflegungspräferenzen (vegan/vegetarisch/allergien), Barrierefreiheitsbedarf, Einverständnis Foto/Video
- [ ] Anmeldefristen definieren: Early Bird (bis wann?), Regular (bis wann?), Last Minute (bis 01.10.2026?)
- [ ] Wartelisten-Prozess beschreiben (ab wann, wie kommunizieren)
- [ ] Stornierungsbedingungen festlegen
- [ ] Datenschutz-Konzept skizzieren (welche Daten, wie lange gespeichert, an wen weitergegeben)
- [ ] Bestätigungs-E-Mail-Inhalt skizzieren
- [ ] Konzept in `workstreams/teilnehmer/registrierungs-konzept.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/teilnehmer/registrierungs-konzept.md` – vollständiges Registrierungskonzept mit Tool-Wahl, Tickets, Feldern, Datenschutz

## Hinweise für den Agenten
- DSGVO-Konformität ist nicht optional – wähle nur Tools mit EU-Datenspeicherung oder dokumentiere, warum eine Ausnahme vertretbar ist.
- Plane die Registrierungsöffnung auf 01.05.2026 (laut `config/event.yaml`) – der technische Aufbau muss vorher abgeschlossen sein.
- Berücksichtige, dass Workshop- und Hackathon-Plätze begrenzt sind und separat registriert/zugewiesen werden müssen.
