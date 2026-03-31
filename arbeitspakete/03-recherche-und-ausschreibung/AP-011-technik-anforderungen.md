# AP-011: Technik-Anforderungen konkretisieren

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-011 |
| **Workstream** | Technik |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 2: Planung |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 22.04.2026 – 30.04.2026 |
| **Status** | ⬜ Offen |

## Ziel
Einen vollständigen Technik-Anforderungskatalog erstellen, der alle AV-, IT- und Streaming-Bedarfe für alle Räume und das gesamte 3-tägige Event abdeckt.

## Voraussetzungen (Abhängigkeiten)
- AP-005: Venue-Anforderungen definieren
- AP-006: Programm-Tracks konzipieren

## Eingaben (Inputs)
- `workstreams/venue-logistik/venue-anforderungen.md` – Raumliste und Technik-Basisanforderungen
- `workstreams/programm/programm-tracks.md` – Sessionformate (bestimmt Technik-Bedarf pro Raum)

## Aufgaben (Checkliste)
- [ ] Räumliche Technikbedarfe inventarisieren: Hauptbühne, Track-Räume, Workshop-Räume, Hackathon-Bereich
- [ ] AV-Equipment pro Raum festlegen: Beamer/Display-Größe, Auflösung, Lautsprecher, Mikrofone (Headset, Handmikro, Ansteckmikro)
- [ ] Streaming-Anforderungen klären: Live-Stream ja/nein, welche Räume, welche Plattform (YouTube, Vimeo?)
- [ ] Aufzeichnungs-Konzept festlegen: welche Sessions aufzeichnen, Kamerapositionierung, Einwilligung der Speaker
- [ ] WLAN-Anforderungen spezifizieren: mind. 100 Mbit/s symmetrisch, Kapazität für 150 gleichzeitige Geräte, separate SSIDs für Teilnehmende/Speaker/Staff
- [ ] Hackathon-spezifische Technik: Steckdosenleisten, Mehrfachstecker, Netzwerk-Switches
- [ ] Zeitplanungsdisplays/Monitore für Flur-Beschilderung einplanen
- [ ] Backup-Lösungen definieren (lokaler HDMI-Fallback, Offline-Präsentations-Speicher)
- [ ] Technik-Anforderungen in `workstreams/technik/technik-anforderungen.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/technik/technik-anforderungen.md` – vollständiger Technik-Anforderungskatalog mit Raum-by-Raum-Auflistung

## Hinweise für den Agenten
- Unterscheide klar zwischen Technik, die die Venue stellen soll (in AP-009 anfragen) und Technik, die extern beschafft werden muss (AP-021).
- Plane Techniker-Bedarf ein: Wer betreut die Technik während des Events? Wie viele Technik-Helfer werden benötigt?
- Berücksichtige Barrierefreiheit: Induktionsschleife für Hörgeräte-Träger, Untertitelung für Live-Stream?
