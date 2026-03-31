# Block 04: Buchungen & Veröffentlichung

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 01.05.2026 – 15.05.2026 |
| **Phase** | Phase 2/3: Planung → Umsetzung |
| **Verantwortung** | Studierendenteam (operations, kommunikation, programm) |
| **Vorgänger-Block** | Block 03: Recherche & Ausschreibung (muss vollständig abgeschlossen sein) |
| **Nachfolger-Block** | Block 05: Umsetzung nach Venue-Buchung |

## Beschreibung

Der kritischste Block: Die Venue wird gebucht, der CfP geht live (Zieldatum: 30.04./01.05.2026), die Website wird gelauncht und die öffentliche Kommunikation beginnt. Nach diesem Block ist das Event öffentlich und verbindliche Buchungen sind gemacht.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-015 | Venue buchen | 🔴 Kritisch | operations | AP-009 |
| AP-016 | CfP veröffentlichen | 🔴 Kritisch | programm | AP-010 |
| AP-017 | Website launchen | 🔴 Kritisch | kommunikation | AP-004, AP-008, AP-010 |
| AP-018 | Kommunikationsplan erstellen | 🟡 Hoch | kommunikation | AP-004 |
| AP-019 | Content-Kalender aufsetzen | 🟡 Hoch | kommunikation | AP-018 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:** Block 03 muss vollständig abgeschlossen sein:
- `workstreams/venue-logistik/venue-recherche.md` mit Angeboten
- `workstreams/programm/cfp-text.md` fertig
- `workstreams/kommunikation/kommunikationsstrategie.md` fertig

## Parallele Ausführung innerhalb dieses Blocks

```
AP-015 (Venue buchen)       → sofort starten, kritischer Pfad
AP-016 (CfP veröffentlichen) → parallel zu AP-015 (unabhängig)
AP-017 (Website)            → parallel, aber benötigt CfP-Text aus AP-016
AP-018 (Komm-Plan)          → parallel zu AP-015/016
AP-019 (Content-Kalender)   → nach AP-018
```

## Definition of Done für diesen Block

- [ ] AP-015: Venue vertraglich gebucht, Buchungsbestätigung liegt vor
- [ ] AP-016: CfP ist öffentlich und über alle Kanäle kommuniziert
- [ ] AP-017: Event-Website ist live und zugänglich
- [ ] AP-018: `workstreams/kommunikation/kommunikationsplan.md` ist fertig
- [ ] AP-019: `workstreams/kommunikation/content-kalender.md` ist fertig
- [ ] `dashboard/status.md` ist aktualisiert
