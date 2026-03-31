# Block 03: Recherche & Ausschreibung

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 22.04.2026 – 30.04.2026 |
| **Phase** | Phase 2: Planung |
| **Verantwortung** | Studierendenteam (operations, programm, kommunikation) |
| **Vorgänger-Block** | Block 02: Venue & Programm-Konzept (muss vollständig abgeschlossen sein) |
| **Nachfolger-Block** | Block 04: Buchungen & Veröffentlichung |

## Beschreibung

In diesem Block werden aktive Recherchen durchgeführt und Ausschreibungstexte erstellt. Venues werden identifiziert und angefragt, der CfP-Text wird formuliert, Technik-Anforderungen konkretisiert, Hotels recherchiert, Sponsoren identifiziert und das Catering konzipiert. Am Ende dieses Blocks sind alle Entscheidungsgrundlagen für Buchungen und Veröffentlichungen vorhanden.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-009 | Venue-Recherche | 🔴 Kritisch | operations | AP-005 |
| AP-010 | CfP-Text verfassen | 🔴 Kritisch | programm | AP-006, AP-007 |
| AP-011 | Technik-Anforderungen konkretisieren | 🟡 Hoch | operations | AP-005, AP-006 |
| AP-012 | Hotel-Recherche | 🟡 Hoch | operations | AP-001 |
| AP-013 | Sponsoren-Recherche | 🟡 Hoch | kommunikation | AP-003 |
| AP-014 | Catering-Konzept entwickeln | 🟢 Normal | operations | AP-005 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:** Block 02 muss vollständig abgeschlossen sein:
- `workstreams/venue-logistik/venue-anforderungen.md` muss existieren
- `workstreams/programm/programm-tracks.md` muss existieren
- `workstreams/programm/cfp-bewertungsrubrik.md` muss existieren
- `workstreams/teilnehmer/registrierungs-konzept.md` muss existieren

## Parallele Ausführung innerhalb dieses Blocks

Alle 6 APs können **vollständig parallel** gestartet werden, sobald Block 02 abgeschlossen ist:

```
AP-009 (Venue-Recherche)         → Ergebnis → AP-015
AP-010 (CfP-Text)                → Ergebnis → AP-016
AP-011 (Technik-Anforderungen)   → Ergebnis → AP-021
AP-012 (Hotel-Recherche)         → Ergebnis → AP-023
AP-013 (Sponsoren-Recherche)     → Ergebnis → AP-025
AP-014 (Catering-Konzept)        → Ergebnis → AP-022
```

## Definition of Done für diesen Block

- [ ] AP-009: `workstreams/venue-logistik/venue-recherche.md` mit mind. 3 Venue-Optionen inkl. Angeboten
- [ ] AP-010: `workstreams/programm/cfp-text.md` fertig und zur Veröffentlichung bereit
- [ ] AP-011: `workstreams/technik/technik-anforderungen.md` mit konkreter Ausstattungsliste
- [ ] AP-012: `workstreams/unterkunft-anreise/hotel-recherche.md` mit mind. 3 Hotel-Optionen
- [ ] AP-013: `workstreams/sponsoring/sponsoren-recherche.md` mit priorisierter Kontaktliste
- [ ] AP-014: `workstreams/catering/catering-konzept.md` mit Anbieter-Recherche
- [ ] `dashboard/status.md` ist aktualisiert
