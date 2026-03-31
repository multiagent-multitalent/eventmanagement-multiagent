# AP-039: Übergabedokumentation erstellen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-039 |
| **Workstream** | Nachbereitung |
| **Agent** | Dokumentation (`.claude/agents/dokumentation.md`) |
| **Phase** | Phase 4: Übergabe |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 23.06.2026 – 28.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Eine vollständige Übergabedokumentation erstellen, die COAI gGmbH in die Lage versetzt, alle laufenden Planungsstränge nahtlos zu übernehmen und das Event erfolgreich durchzuführen.

## Voraussetzungen (Abhängigkeiten)
- Alle APs aus Blöcken 01–07 müssen abgeschlossen sein

## Eingaben (Inputs)
- `dashboard/status.md` – aktueller Status aller Workstreams
- Alle `workstreams/*/` – sämtliche erstellten Artefakte
- `archiv/entscheidungslog.md` – getroffene Entscheidungen

## Aufgaben (Checkliste)
- [ ] Übergabedokument strukturieren: Executive Summary, Status aller Workstreams, wichtige Kontakte, laufende Verträge, offene Aufgaben
- [ ] Status-Übersicht aller 10 Workstreams erstellen (was ist abgeschlossen, was läuft noch, was fehlt)
- [ ] Alle aktiven Verträge auflisten: Venue, Caterer, Hotel-Kontingente, Sponsoring-Verträge, Technik-Mietverträge
- [ ] Wichtige Kontakte dokumentieren: Venue-Ansprechperson, Caterer-Kontakt, alle bestätigten Speaker, Helfer-Kontaktliste
- [ ] Kritische Fristen dokumentieren: wann muss was getan werden (z.B. finale Catering-Mengenangabe, Badge-Druck, Helfer-Briefing)
- [ ] Zugangsdaten-Verzeichnis erstellen (Passwort-Manager oder sicheres Dokument – getrennt von diesem Dokument)
- [ ] Schritt-für-Schritt-Anleitung für die nächsten 3 Monate (Juli–Oktober) erstellen
- [ ] Übergabedokumentation in `workstreams/nachbereitung/uebergabe-dokumentation.md` ablegen

## Ausgaben (Outputs)
- `workstreams/nachbereitung/uebergabe-dokumentation.md` – vollständiges Übergabedokument für COAI

## Hinweise für den Agenten
- Das Übergabedokument muss von jemandem verstanden werden, der das Projekt nicht kennt – verzichte auf interne Abkürzungen und erkläre den Kontext.
- Priorisiere klar: Was muss COAI in den ersten 2 Wochen nach Übergabe erledigen?
- Referenziere alle relevanten Dateipfade im Repository – COAI soll sich im Repository ohne Suchaufwand zurechtfinden.
