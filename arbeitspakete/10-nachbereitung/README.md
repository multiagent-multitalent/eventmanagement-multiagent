# Block 10: Nachbereitung (COAI)

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 17.10.2026 – 30.11.2026 |
| **Phase** | Phase 6: Nachbereitung |
| **Verantwortung** | **COAI gGmbH** |
| **Vorgänger-Block** | Block 09: Event-Durchführung (muss abgeschlossen sein) |
| **Nachfolger-Block** | – (Abschluss des Projekts) |

## Beschreibung

⚠️ **Dieser Block liegt vollständig in der Verantwortung von COAI gGmbH.** Nach dem Event wird Feedback gesammelt, Materialien archiviert, Learnings dokumentiert und das Repository aufgeräumt. Projektabschluss: 30. November 2026.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Verantwortung | Zeitraum |
|---|---|---|---|---|
| AP-048 | Feedback-Survey versenden | 🔴 Kritisch | COAI | 17.–24.10.2026 |
| AP-049 | Materialien sammeln | 🟡 Hoch | COAI | 17.–31.10.2026 |
| AP-050 | Feedback auswerten | 🟡 Hoch | COAI | 25.10.–07.11.2026 |
| AP-051 | Lessons Learned dokumentieren | 🟡 Hoch | COAI | 08.–22.11.2026 |
| AP-052 | Repository aufräumen | 🟢 Normal | COAI | 22.–30.11.2026 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:**
- Block 09 vollständig abgeschlossen (Event stattgefunden)
- `workstreams/nachbereitung/event-protokoll.md` aus AP-046 vorhanden

## Parallele Ausführung innerhalb dieses Blocks

```
AP-048 (sofort nach Event)
AP-049 (sofort nach Event, parallel zu AP-048)
    │
    └──→ AP-050 (nach AP-048, Feedback-Rücklauf abwarten)
              │
              └──→ AP-051 (nach AP-050)
                        │
                        └──→ AP-052 (abschließend)
```

## Definition of Done für diesen Block

- [ ] AP-048: Feedback-Survey versendet und Rücklauf dokumentiert
- [ ] AP-049: Alle Materialien (Fotos, Videos, Dokumente) gesammelt und archiviert
- [ ] AP-050: Feedback ausgewertet und Bericht erstellt
- [ ] AP-051: Lessons Learned dokumentiert und im Repository abgelegt
- [ ] AP-052: Repository bereinigt und für zukünftige Nutzung vorbereitet
- [ ] Projekt offiziell abgeschlossen (30.11.2026)
