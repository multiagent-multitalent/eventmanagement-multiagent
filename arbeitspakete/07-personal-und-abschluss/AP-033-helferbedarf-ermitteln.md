# AP-033: Helferbedarf ermitteln

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-033 |
| **Workstream** | Personal & Helfer |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 16.06.2026 – 22.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Den konkreten Helferbedarf für Aufbau, Event-Betrieb und Abbau ermitteln und in einem strukturierten Dokument festhalten, das als Grundlage für Rekrutierung und Schichtplanung dient.

## Voraussetzungen (Abhängigkeiten)
- AP-028: Agenda erstellen (Zeitplan bekannt)
- AP-020: Raumplanung erstellen (Räume und Aufgaben bekannt)

## Eingaben (Inputs)
- `workstreams/programm/agenda.md` – Zeitplan für alle 3 Tage
- `workstreams/venue-logistik/raumplanung.md` – Raumstruktur
- `workstreams/technik/technik-beschaffung.md` – Technik-Setup

## Aufgaben (Checkliste)
- [ ] Aufgabenfelder für Helfer identifizieren: Check-In/Registration, Raum-Betreuung, Technik-Support, Catering-Koordination, Beschilderung/Orientierung, Social Media/Foto, Pressekontakt
- [ ] Für jede Aufgabe: benötigte Anzahl Helfer, Zeitraum, Qualifikationsanforderungen (Sprachen, Technik-Know-how)
- [ ] Aufbautag (13.10.2026): Helfer für Möbelaufbau, Technik-Setup, Beschilderung
- [ ] Tag 1 (14.10.): Check-In-Team, Technik-Team, Raum-Teams
- [ ] Tag 2 (15.10.): Raum-Teams für parallele Tracks
- [ ] Tag 3 (16.10.): Workshop- und Hackathon-Betreuung
- [ ] Abbautag: Helfer für Abbau und Rücktransport
- [ ] Gesamt-Helferzahl und Gesamtstunden berechnen
- [ ] Helferbedarf in `workstreams/personal/helferbedarf.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/personal/helferbedarf.md` – strukturierter Helferbedarf mit Aufgaben, Zeiten und Anforderungen pro Rolle

## Hinweise für den Agenten
- Plane mind. 15–20 Helfer für ein Event dieser Größenordnung (125 Teilnehmende, 3 Tage).
- Unterscheide zwischen bezahlten Kräften (z.B. professionelles Technik-Team) und Ehrenamtlichen (Studierende, Community).
- Jede Helfer-Rolle braucht ein Backup – keine Single Points of Failure im Schichtplan.
