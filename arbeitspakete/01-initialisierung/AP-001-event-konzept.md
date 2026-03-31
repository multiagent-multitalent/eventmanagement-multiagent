# AP-001: Event-Konzept finalisieren

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-001 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Orchestrator (`.claude/agents/orchestrator.md`) |
| **Phase** | Phase 1: Initialisierung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 01.04.2026 – 07.04.2026 |
| **Status** | ✅ Abgeschlossen |

## Ziel
Das Event-Konzept für die AI Transparency Days 2026 wird auf Basis der Konfiguration in `config/event.yaml` zu einem vollständigen, abgestimmten Konzeptpapier ausgearbeitet. Dieses Dokument dient als Referenz für alle weiteren Arbeitspakete.

## Voraussetzungen (Abhängigkeiten)
- Keine – kann sofort gestartet werden

## Eingaben (Inputs)
- `config/event.yaml` – Event-Basisdaten (Datum, Ort, Größe, Format, Themen)
- `config/team.yaml` – Team-Struktur und Verantwortlichkeiten
- `docs/phasenmodell.md` – Projektphasen und Meilensteine
- `templates/programm/` – Vorlagen für Programm-Artefakte

## Aufgaben (Checkliste)
- [x] Event-Basisdaten aus `config/event.yaml` prüfen und bei Bedarf ergänzen
- [x] Ziele des Events in 3–5 Sätzen formulieren (Was soll AITD 2026 erreichen?)
- [x] Zielgruppen konkretisieren (Forschende, Praktiker, Studierende, Policymaker – Anteile schätzen)
- [x] Formatbeschreibung ausarbeiten: Konferenz + Workshops + Hackathon, 3 Tracks, Hauptbühne
- [x] Thematischen Rahmen der 3 Tracks vorschlagen (basierend auf AI Transparency, Safety, Governance, Human Compatible AI)
- [x] Erwartetes Programm-Skelett skizzieren: Tag 1 (Eröffnung, Keynotes), Tag 2 (Tracks + Workshops), Tag 3 (Hackathon + Abschluss)
- [x] Alleinstellungsmerkmale des Events herausarbeiten (Was macht AITD 2026 besonders?)
- [x] Sprachpolitik festlegen: Deutsch/Englisch-Mix, Übersetzungsbedarf?
- [x] Konzeptpapier in `workstreams/programm/event-konzept.md` schreiben

## Ausgaben (Outputs)
- `workstreams/programm/event-konzept.md` – vollständiges Event-Konzept mit Zielen, Zielgruppen, Format und Themen

## Hinweise für den Agenten
- Das Event-Konzept muss so konkret sein, dass Venue-Anforderungen (AP-005) direkt daraus abgeleitet werden können.
- Stelle sicher, dass das 3-Tage-Format (14.–16. Oktober 2026) explizit beschrieben wird, inkl. welche Formate an welchem Tag stattfinden.
- Stimme das Konzept mit COAI gGmbH ab (Betreuer: Steffen Höpfner) – dokumentiere etwaige Abstimmungsnotizen als Kommentar im Dokument.
