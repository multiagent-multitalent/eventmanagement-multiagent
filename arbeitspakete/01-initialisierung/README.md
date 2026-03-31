# Block 01: Initialisierung

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 01.04.2026 – 14.04.2026 (Kickoff + 2 Wochen) |
| **Phase** | Phase 1: Initialisierung |
| **Verantwortung** | Studierendenteam (alle Agenten) |
| **Vorgänger-Block** | – (Startpunkt) |
| **Nachfolger-Block** | Block 02: Venue & Programm-Konzept |

## Beschreibung

Der erste Block legt das strategische Fundament des gesamten Events. Hier werden das Event-Konzept finalisiert, der Budgetrahmen abgesteckt, die Sponsoring-Strategie entwickelt und die Kommunikationsstrategie definiert. Ohne diese Grundlagen können keine weiteren Blöcke sinnvoll bearbeitet werden.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-001 | Event-Konzept finalisieren | 🔴 Kritisch | orchestrator | Keine |
| AP-002 | Budget-Rahmen festlegen | 🔴 Kritisch | operations | AP-001 |
| AP-003 | Sponsoring-Strategie entwickeln | 🟡 Hoch | kommunikation | AP-001, AP-002 |
| AP-004 | Kommunikationsstrategie definieren | 🟡 Hoch | kommunikation | AP-001 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:** Keine – dieser Block kann sofort gestartet werden.

**Was muss vorliegen:**
- Zugang zu `config/event.yaml` (bereits vorhanden)
- Zugang zu `config/team.yaml` (bereits vorhanden)
- Kickoff-Meeting hat stattgefunden (01.04.2026)

## Parallele Ausführung innerhalb dieses Blocks

```
AP-001 (muss zuerst abgeschlossen sein)
    │
    ├──→ AP-002 (kann parallel zu AP-004 laufen)
    │
    └──→ AP-004 (kann parallel zu AP-002 laufen)
              │
              └──→ AP-003 (benötigt AP-001 + AP-002)
```

**Empfohlene Ausführungsreihenfolge:**
1. AP-001 starten und abschließen
2. AP-002 und AP-004 parallel starten
3. AP-003 starten sobald AP-002 abgeschlossen ist

## Definition of Done für diesen Block

- [ ] AP-001: `workstreams/programm/event-konzept.md` existiert und ist inhaltlich vollständig
- [ ] AP-002: `workstreams/venue-logistik/budget-rahmen.md` existiert mit konkreten Zahlen
- [ ] AP-003: `workstreams/sponsoring/sponsoring-strategie.md` existiert
- [ ] AP-004: `workstreams/kommunikation/kommunikationsstrategie.md` existiert
- [ ] `dashboard/status.md` ist aktualisiert
