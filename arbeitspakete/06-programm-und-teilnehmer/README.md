# Block 06: Programm & Teilnehmer

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 15.06.2026 – 30.06.2026 |
| **Phase** | Phase 3: Umsetzung |
| **Verantwortung** | Studierendenteam (programm, operations) |
| **Vorgänger-Block** | Block 05 (vollständig) + CfP-Deadline 15.06.2026 muss verstrichen sein |
| **Nachfolger-Block** | Block 07: Personal & Abschluss |

## Beschreibung

Nach der CfP-Deadline (15.06.2026) werden alle Einreichungen gesichtet und bewertet, die Agenda finalisiert, Speaker informiert und alle programmbezogenen Dokumente erstellt. Parallel werden Badge-Designs entwickelt.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-027 | CfP-Einreichungen sichten | 🔴 Kritisch | programm | AP-016 + CfP-Deadline |
| AP-028 | Agenda erstellen | 🔴 Kritisch | programm | AP-027, AP-020 |
| AP-029 | Speaker-Zusagen einholen | 🔴 Kritisch | programm | AP-027 |
| AP-030 | Speaker-Briefings erstellen | 🟡 Hoch | programm | AP-028, AP-029 |
| AP-031 | Session-Steckbriefe erstellen | 🟡 Hoch | programm | AP-028, AP-030 |
| AP-032 | Badge-Design entwickeln | 🟢 Normal | operations | AP-024 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:**
- CfP-Deadline muss verstrichen sein (15.06.2026)
- AP-020 (Raumplanung) muss abgeschlossen sein
- AP-024 (Registrierung) muss laufen (Teilnehmerdaten vorhanden)

## Parallele Ausführung innerhalb dieses Blocks

```
AP-027 (muss zuerst)
    │
    ├──→ AP-028 + AP-029 (parallel nach AP-027)
                │
                └──→ AP-030 (nach AP-028 + AP-029)
                         │
                         └──→ AP-031

AP-032 (vollständig parallel, unabhängig)
```

## Definition of Done für diesen Block

- [ ] AP-027: Alle Einreichungen bewertet, Entscheidungen getroffen
- [ ] AP-028: `workstreams/programm/agenda.md` – finale Agenda veröffentlicht
- [ ] AP-029: Alle akzeptierten Speaker haben schriftlich zugesagt
- [ ] AP-030: `workstreams/programm/speaker-briefings.md` – alle Speaker informiert
- [ ] AP-031: `workstreams/programm/session-steckbriefe.md` – alle Sessions beschrieben
- [ ] AP-032: Badge-Design fertig, Druckdatei erstellt
- [ ] `dashboard/status.md` ist aktualisiert
