# AP-042: Abschlussbericht erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-042 |
| **Workstream** | Nachbereitung |
| **Agent** | Dokumentation (`.claude/agents/dokumentation.md`) |
| **Phase** | Phase 4: Übergabe |
| **Priorität** | 🟡 Hoch |
| **Zeitraum** | 28.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Einen professionellen Abschlussbericht über die Planungsarbeit des Studierendenteams erstellen, der an die Betreuer (Prof. Schacht, Steffen Höpfner) übergeben wird.

## Voraussetzungen (Abhängigkeiten)
- AP-039: Übergabedokumentation erstellen
- AP-040: Zugänge übergeben
- AP-041: Offene TODOs dokumentieren

## Eingaben (Inputs)
- `workstreams/nachbereitung/uebergabe-dokumentation.md`
- `workstreams/nachbereitung/offene-todos.md`
- `dashboard/status.md` – Gesamtstatus
- `archiv/entscheidungslog.md` – Entscheidungshistorie

## Aufgaben (Checkliste)
- [ ] Abschlussbericht-Struktur festlegen: Executive Summary, Projektziele und -ergebnis, Übersicht aller Arbeitspakete, erreichte Meilensteine, Budget-Ist-Stand, offene Punkte, Empfehlungen für COAI
- [ ] Executive Summary (1 Seite) verfassen: Was wurde erreicht? Was bleibt offen?
- [ ] Alle 52 APs mit Status (abgeschlossen/offen) auflisten
- [ ] Meilenstein-Erreichung dokumentieren (Speaker-Einladungen versandt? Venue gebucht? etc.)
- [ ] Budget-Ist-Stand dokumentieren (was wurde bereits ausgegeben/gebunden)
- [ ] Lessons Learned aus dem Planungsprozess als Empfehlungen formulieren
- [ ] Risiken für den weiteren Verlauf identifizieren und dokumentieren
- [ ] Bericht formatieren (professionelles Layout, PDF-Export)
- [ ] Bericht an Betreuer senden (Prof. Schacht, Steffen Höpfner)
- [ ] Bericht in `workstreams/nachbereitung/abschlussbericht.md` ablegen

## Ausgaben (Outputs)
- `workstreams/nachbereitung/abschlussbericht.md` – vollständiger Abschlussbericht für Betreuer und COAI

## Hinweise für den Agenten
- Der Abschlussbericht dient auch als Leistungsnachweis des Studierendenteams – stelle sicher, dass alle Leistungen klar dokumentiert sind.
- Sei transparent über offene Punkte und Risiken – das schafft Vertrauen und hilft COAI bei der Übernahme.
- Der Bericht ist bis 30.06.2026 (final_report-Datum aus `config/event.yaml`) fertigzustellen und zu versenden.
