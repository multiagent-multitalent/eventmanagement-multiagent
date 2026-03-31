# Block 07: Personal & Abschluss

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 16.06.2026 – 30.06.2026 |
| **Phase** | Phase 3: Umsetzung → Übergabe |
| **Verantwortung** | Studierendenteam (operations, kommunikation) |
| **Vorgänger-Block** | Block 06: Programm & Teilnehmer (parallel möglich für AP-033–035) |
| **Nachfolger-Block** | Block 08: Übergabe |

## Beschreibung

Der letzte Block vor der Übergabe: Helferbedarf ermitteln, Helfer rekrutieren, Schichtplan erstellen, Teilnehmer-Infopakete zusammenstellen, das fertige Programm kommunizieren und die Beschilderung planen.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-033 | Helferbedarf ermitteln | 🟡 Hoch | operations | AP-028, AP-020 |
| AP-034 | Helfer rekrutieren | 🟡 Hoch | operations | AP-033 |
| AP-035 | Schichtplan erstellen | 🟡 Hoch | operations | AP-034, AP-028 |
| AP-036 | Teilnehmer-Infopakete erstellen | 🟡 Hoch | operations | AP-030, AP-026 |
| AP-037 | Programm kommunizieren | 🟡 Hoch | kommunikation | AP-031, AP-019 |
| AP-038 | Beschilderung planen | 🟢 Normal | operations | AP-020 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:**
- AP-028 (Agenda) muss abgeschlossen sein → für AP-033, AP-035, AP-037
- AP-020 (Raumplanung) muss abgeschlossen sein → für AP-033, AP-038
- AP-031 (Session-Steckbriefe) muss abgeschlossen sein → für AP-037

## Parallele Ausführung innerhalb dieses Blocks

```
AP-033 → AP-034 → AP-035
AP-036 (parallel, sobald AP-030 und AP-026 fertig)
AP-037 (parallel, sobald AP-031 fertig)
AP-038 (parallel, sobald AP-020 fertig)
```

## Definition of Done für diesen Block

- [ ] AP-033: `workstreams/personal/helferbedarf.md` mit konkreter Bedarfsliste
- [ ] AP-034: Helfer rekrutiert, Zusagen dokumentiert
- [ ] AP-035: `workstreams/personal/schichtplan.md` fertig
- [ ] AP-036: `workstreams/teilnehmer/infopaket.md` fertig
- [ ] AP-037: Programm auf Website und Social Media veröffentlicht
- [ ] AP-038: `workstreams/venue-logistik/beschilderung.md` fertig
- [ ] `dashboard/status.md` ist aktualisiert
