# Block 08: Übergabe

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 23.06.2026 – 30.06.2026 |
| **Phase** | Phase 4: Übergabe |
| **Verantwortung** | Studierendenteam → COAI gGmbH |
| **Vorgänger-Block** | Block 07: Personal & Abschluss (muss vollständig abgeschlossen sein) |
| **Nachfolger-Block** | Block 09: Event-Durchführung (COAI) |

## Beschreibung

Der Abschlussblock des Studierendenteams: Alle Planungsergebnisse werden dokumentiert, Zugänge übergeben, offene TODOs aufgelistet und ein Abschlussbericht erstellt. Nach diesem Block übernimmt COAI gGmbH die vollständige Verantwortung für das Event.

**Deadline: 30. Juni 2026** (unveränderlich, laut `config/event.yaml: final_report`)

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-039 | Übergabedokumentation erstellen | 🔴 Kritisch | dokumentation | Block 07 vollständig |
| AP-040 | Zugänge übergeben | 🔴 Kritisch | operations | AP-039 |
| AP-041 | Offene TODOs dokumentieren | 🔴 Kritisch | koordination | AP-039 |
| AP-042 | Abschlussbericht erstellen | 🟡 Hoch | dokumentation | AP-039, AP-040, AP-041 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:** Alle vorherigen Blöcke (01–07) müssen abgeschlossen sein.

## Parallele Ausführung innerhalb dieses Blocks

```
AP-039 (zuerst, Basis für alle anderen)
    │
    ├──→ AP-040 (parallel zu AP-041)
    ├──→ AP-041 (parallel zu AP-040)
    └──→ AP-042 (nach AP-039 + AP-040 + AP-041)
```

## Definition of Done für diesen Block

- [ ] AP-039: `workstreams/nachbereitung/uebergabe-dokumentation.md` vollständig
- [ ] AP-040: Alle Zugänge (Website, Registrierung, Kommunikationskanäle, Venue-Kontakt) an COAI übergeben
- [ ] AP-041: `workstreams/nachbereitung/offene-todos.md` mit priorisierten offenen Punkten
- [ ] AP-042: `workstreams/nachbereitung/abschlussbericht.md` fertig und an Betreuer gesendet
- [ ] Übergabe-Meeting mit COAI und Betreuern durchgeführt
- [ ] `dashboard/status.md` ist final aktualisiert
