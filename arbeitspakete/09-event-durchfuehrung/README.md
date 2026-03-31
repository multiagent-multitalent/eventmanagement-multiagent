# Block 09: Event-Durchführung (COAI)

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 13.–16. Oktober 2026 |
| **Phase** | Phase 5: Durchführung |
| **Verantwortung** | **COAI gGmbH** (Studierendenteam hat übergeben) |
| **Vorgänger-Block** | Block 08: Übergabe (vollständig abgeschlossen) |
| **Nachfolger-Block** | Block 10: Nachbereitung |

## Beschreibung

⚠️ **Dieser Block liegt in der Verantwortung von COAI gGmbH.** Das Studierendenteam hat das Event übergeben. Die hier beschriebenen Arbeitspakete sind für die Durchführung des physischen Events an der Venue in Nürnberg.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Verantwortung | Zeitraum |
|---|---|---|---|---|
| AP-043 | Helfer-Briefing durchführen | 🔴 Kritisch | COAI | 13.10.2026 |
| AP-044 | Aufbau & Technik-Setup | 🔴 Kritisch | COAI | 13.10.2026 |
| AP-045 | Check-In-Management | 🔴 Kritisch | COAI | 14.–16.10.2026 |
| AP-046 | Event-Betrieb | 🔴 Kritisch | COAI | 14.–16.10.2026 |
| AP-047 | Abbau | 🟡 Hoch | COAI | 16.10.2026 (abends) |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:**
- Block 08 vollständig abgeschlossen (Übergabe erfolgt)
- Alle vorbereiteten Dokumente müssen vorhanden sein: Schichtplan, Helfer-Liste, Raumplanung, Technik-Beschaffung, Agenda, Teilnehmer-Infopakete

## Parallele Ausführung innerhalb dieses Blocks

```
AP-043 (Aufbautag, 13.10.)
AP-044 (Aufbautag, 13.10. – parallel zu AP-043)
    │
    └──→ AP-045 (ab 14.10. morgens)
    └──→ AP-046 (ab 14.10. – parallel zu AP-045)
              │
              └──→ AP-047 (16.10. nach Ende)
```

## Definition of Done für diesen Block

- [ ] AP-043: Alle Helfer gebrieft und Schichtplan bestätigt
- [ ] AP-044: Alle Räume technisch bereit (Technik-Test abgeschlossen)
- [ ] AP-045: Check-In-System läuft, alle Teilnehmenden erfolgreich eingecheckt
- [ ] AP-046: Event vollständig durchgeführt, keine kritischen Zwischenfälle
- [ ] AP-047: Venue vollständig abgebaut, Schlüssel zurückgegeben
