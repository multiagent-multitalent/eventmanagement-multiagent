# AP-032: Badge-Design entwickeln

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-032 |
| **Workstream** | Teilnehmer-Management |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟢 Normal |
| **Zeitraum** | 15.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Ein Badge-Design (Namensschild) für alle Teilnehmenden entwickeln, das CI-konform ist, alle notwendigen Informationen enthält und vor dem Event gedruckt werden kann.

## Voraussetzungen (Abhängigkeiten)
- AP-024: Registrierung einrichten (Teilnehmer-Daten-Struktur bekannt)

## Eingaben (Inputs)
- `workstreams/teilnehmer/registrierungs-konzept.md` – Registrierungsfelder (welche Daten auf dem Badge)
- `workstreams/kommunikation/kommunikationsstrategie.md` – CI/CD-Richtlinien

## Aufgaben (Checkliste)
- [ ] Badge-Inhalt definieren: Name, Affiliation, Ticket-Kategorie (farblich oder mit Icon), QR-Code (für Check-In), ggf. Pronomen-Feld
- [ ] Badge-Größe festlegen (Standard: A6 quer / Kreditkartenformat)
- [ ] Design-Vorlage erstellen (Canva, Figma oder ähnliches CI-konform)
- [ ] Verschiedene Badge-Typen gestalten: Teilnehmende, Speaker, Helfer, Presse, Orga
- [ ] Badge-Halter und Lanyard-Farben für verschiedene Rollen wählen
- [ ] Print-Spezifikationen festlegen (Auflösung, Format, Druckerei-Anforderungen)
- [ ] Test-Druck mit Beispieldaten durchführen
- [ ] Druck-Workflow dokumentieren (wann drucken, wie Daten exportieren, wer druckt)
- [ ] Badge-Design und Spezifikationen in `workstreams/teilnehmer/badge-design.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/teilnehmer/badge-design.md` – Badge-Design-Dokumentation mit Vorlage, Druck-Spezifikationen und Workflow

## Hinweise für den Agenten
- Plane, dass Badges erst kurz vor dem Event (ca. 1 Woche vorher) gedruckt werden, wenn die Registrierungszahlen stabil sind.
- Der QR-Code auf dem Badge kann für das Check-In-System (AP-045) genutzt werden – koordiniere dies mit dem Registrierungstool.
- Berücksichtige Pronomen-Angaben freiwillig als Feld – das ist ein kleines aber wichtiges Inklusionssignal.
