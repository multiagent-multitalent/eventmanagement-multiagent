# Block 02: Venue & Programm-Konzept

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 08.04.2026 – 21.04.2026 |
| **Phase** | Phase 2: Planung |
| **Verantwortung** | Studierendenteam (operations, programm) |
| **Vorgänger-Block** | Block 01: Initialisierung (muss vollständig abgeschlossen sein) |
| **Nachfolger-Block** | Block 03: Recherche & Ausschreibung |

## Beschreibung

In diesem Block werden die konzeptionellen Grundlagen für Venue und Programm erarbeitet – noch vor der eigentlichen Recherche. Hier entstehen die Anforderungslisten und Konzepte, die als Grundlage für Recherchen und die Speaker-Kuration dienen.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-005 | Venue-Anforderungen definieren | 🔴 Kritisch | operations | AP-001, AP-002 |
| AP-006 | Programm-Tracks konzipieren | 🔴 Kritisch | programm | AP-001 |
| AP-008 | Registrierungs-Konzept entwickeln | 🟡 Hoch | operations | AP-001 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:** Block 01 muss vollständig abgeschlossen sein:
- `workstreams/programm/event-konzept.md` muss existieren
- `workstreams/venue-logistik/budget-rahmen.md` muss existieren

## Parallele Ausführung innerhalb dieses Blocks

```
AP-005 ──→ (Ergebnis fließt in Block 03)
AP-006 ──→ (Ergebnis fließt in Block 03)
AP-008 ──→ (Ergebnis fließt in Block 04)
```

Alle drei APs können **vollständig parallel** gestartet werden, sobald Block 01 abgeschlossen ist.

## Definition of Done für diesen Block

- [ ] AP-005: `workstreams/venue-logistik/venue-anforderungen.md` existiert mit detaillierter Anforderungsliste
- [ ] AP-006: `workstreams/programm/programm-tracks.md` existiert mit 3 definierten Tracks
- [ ] AP-008: `workstreams/teilnehmer/registrierungs-konzept.md` existiert
- [ ] `dashboard/status.md` ist aktualisiert
