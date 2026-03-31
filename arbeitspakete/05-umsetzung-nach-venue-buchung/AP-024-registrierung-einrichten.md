# AP-024: Registrierung einrichten

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-024 |
| **Workstream** | Teilnehmer-Management |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 25.04.2026 – 01.05.2026 |
| **Status** | ⬜ Offen |

## Ziel
Das Registrierungssystem technisch einrichten, testen und am 01.05.2026 öffnen, sodass Teilnehmende sich ab diesem Datum verbindlich anmelden können.

## Voraussetzungen (Abhängigkeiten)
- AP-017: Website launchen (für Verlinkung)
- AP-008: Registrierungs-Konzept entwickeln

## Eingaben (Inputs)
- `workstreams/teilnehmer/registrierungs-konzept.md` – Tool-Wahl, Ticket-Kategorien, Formularfelder, Datenschutz
- `workstreams/kommunikation/website-launch.md` – Website-URL für Verlinkung

## Aufgaben (Checkliste)
- [ ] Registrierungs-Tool gemäß Konzept (AP-008) einrichten und konfigurieren
- [ ] Ticket-Kategorien anlegen: Standardticket, Studierendenticket, Speaker-Ticket, Sponsor-Ticket
- [ ] Preise konfigurieren (basierend auf Budget-Rahmen aus AP-002)
- [ ] Pflicht- und Optionalfelder im Formular konfigurieren
- [ ] Bestätigungs-E-Mail einrichten (automatisch nach Registrierung)
- [ ] Datenschutzerklärung und Einwilligungen im Formular einbinden
- [ ] Early-Bird-Deadline und Regular-Deadline einstellen
- [ ] Workshop-/Hackathon-Plätze als limitierte Optionen konfigurieren
- [ ] System mit Testregistrierung vollständig testen (Zahlungsabwicklung, Bestätigungs-Mail, Admin-Ansicht)
- [ ] Registrierungs-Link auf Website einbinden
- [ ] Registrierungs-Status in `workstreams/teilnehmer/registrierung-einrichtung.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/teilnehmer/registrierung-einrichtung.md` – Dokumentation der Systemkonfiguration, Test-Protokoll, Admin-Zugang-Speicherort

## Hinweise für den Agenten
- Das Registrierungssystem muss am 01.05.2026 live sein (Zieldatum laut `config/event.yaml`).
- Teste die gesamte Registrierungsstrecke mit mind. 2 verschiedenen Ticket-Typen und einer Zahlungsabwicklung.
- Stelle sicher, dass Administratoren (COAI) Zugriff auf alle Registrierungsdaten haben und dass ein CSV-Export möglich ist.
