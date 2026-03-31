# AP-048: Feedback-Survey versenden

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-048 |
| **Workstream** | Nachbereitung |
| **Agent** | Dokumentation (`.claude/agents/dokumentation.md`) |
| **Phase** | Phase 6: Nachbereitung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 17.10.2026 – 24.10.2026 |
| **Status** | ⬜ Offen |

## Ziel
Eine professionelle Feedback-Umfrage an alle Teilnehmenden, Speaker und Helfer versenden und einen guten Rücklauf sicherstellen.

## Voraussetzungen (Abhängigkeiten)
- AP-046: Event-Betrieb (Event muss stattgefunden haben)

## Eingaben (Inputs)
- `workstreams/teilnehmer/checkin-protokoll.md` – E-Mail-Adressen aller Teilnehmenden
- `workstreams/programm/speaker-zusagen.md` – Speaker-Kontaktdaten
- `workstreams/personal/helfer-liste.md` – Helfer-Kontaktdaten

## Aufgaben (Checkliste)
- [ ] Feedback-Fragebogen erstellen: allgemeine Zufriedenheit, Programm-Bewertung, Venue/Catering/Technik, Verbesserungsvorschläge, NPS-Score, Interesse an AITD 2027
- [ ] Separate Fragebogen-Varianten: Teilnehmende, Speaker (mit spezifischen Fragen zur Betreuung), Helfer
- [ ] Umfrage-Tool konfigurieren (DSGVO-konform: z.B. LimeSurvey, SurveyMonkey EU)
- [ ] Umfrage-E-Mail verfassen: Danksagung + Link zur Umfrage + Rücklauf-Deadline (7–10 Tage)
- [ ] Umfrage innerhalb von 48h nach Event-Ende versenden (während die Eindrücke frisch sind)
- [ ] Reminder nach 5 Tagen an alle, die noch nicht geantwortet haben
- [ ] Rücklauf-Rate dokumentieren

## Ausgaben (Outputs)
- `workstreams/nachbereitung/feedback-survey.md` – Fragebogen-Dokumentation und Rücklauf-Protokoll

## Hinweise für den Agenten
- Versende die Umfrage maximal 48h nach Event-Ende – die Teilnehmenden sind dann noch im „Event-Modus" und motivierter zu antworten.
- Halte die Umfrage kurz (max. 10 Minuten Ausfüllzeit) – längere Umfragen haben deutlich niedrigeren Rücklauf.
- Kommuniziere, dass Feedback direkt in die Planung von AITD 2027 einfließt – das steigert die Motivation zur Teilnahme.
