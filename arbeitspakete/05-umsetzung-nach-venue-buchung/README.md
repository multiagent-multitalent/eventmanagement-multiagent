# Block 05: Umsetzung nach Venue-Buchung

## Überblick

| Feld | Wert |
|---|---|
| **Zeitraum** | 08.05.2026 – 31.05.2026 |
| **Phase** | Phase 3: Umsetzung |
| **Verantwortung** | Studierendenteam (operations, kommunikation) |
| **Vorgänger-Block** | Block 04: Buchungen & Veröffentlichung (Venue-Buchung AP-015 muss abgeschlossen sein) |
| **Nachfolger-Block** | Block 06: Programm & Teilnehmer |

## Beschreibung

Nach der Venue-Buchung können alle ortsabhängigen Planungen konkretisiert werden: Raumplanung, Technik-Beschaffung, Catering-Beauftragung, Hotel-Kontingente und Anreise-Infos. Parallel laufen die Registrierung und die Sponsoren-Akquise an.

## Arbeitspakete in diesem Block

| AP | Titel | Priorität | Agent | Abhängigkeiten |
|---|---|---|---|---|
| AP-020 | Raumplanung erstellen | 🔴 Kritisch | operations | AP-015, AP-006 |
| AP-021 | Technik beschaffen | 🟡 Hoch | operations | AP-015, AP-011 |
| AP-022 | Catering beauftragen | 🟡 Hoch | operations | AP-015, AP-014 |
| AP-023 | Hotel-Kontingente vereinbaren | 🟡 Hoch | operations | AP-012 |
| AP-024 | Registrierung einrichten | 🔴 Kritisch | operations | AP-017, AP-008 |
| AP-025 | Sponsoren-Akquise starten | 🟡 Hoch | kommunikation | AP-013, AP-015 |
| AP-026 | Anreise-Informationen erstellen | 🟢 Normal | operations | AP-015, AP-023 |

## Abhängigkeiten von anderen Blöcken

**Voraussetzungen:**
- AP-015 (Venue-Buchung) muss abgeschlossen sein → für AP-020, AP-021, AP-022, AP-026
- AP-017 (Website live) muss abgeschlossen sein → für AP-024
- Block 03 komplett abgeschlossen → für alle APs

## Parallele Ausführung innerhalb dieses Blocks

Alle 7 APs können **vollständig parallel** gestartet werden (sobald AP-015 abgeschlossen ist):

```
AP-020 Raumplanung          ← AP-015 fertig
AP-021 Technik              ← AP-015 fertig
AP-022 Catering             ← AP-015 fertig
AP-023 Hotel-Kontingente    ← parallel (keine Venue-Abhängigkeit)
AP-024 Registrierung        ← AP-017 fertig (unabhängig von AP-015)
AP-025 Sponsoren-Akquise    ← unabhängig (kann sofort starten)
AP-026 Anreise-Infos        ← AP-015 + AP-023 fertig
```

## Definition of Done für diesen Block

- [ ] AP-020: `workstreams/venue-logistik/raumplanung.md` mit Raumbelegungsplan
- [ ] AP-021: `workstreams/technik/technik-beschaffung.md` mit Bestellliste und Lieferbestätigungen
- [ ] AP-022: `workstreams/catering/catering-beauftragung.md` mit Vertragsabschluss
- [ ] AP-023: `workstreams/unterkunft-anreise/hotel-kontingente.md` mit Buchungslinks
- [ ] AP-024: Registrierungssystem online und getestet
- [ ] AP-025: `workstreams/sponsoring/sponsoren-akquise.md` mit Kontakt-Protokoll
- [ ] AP-026: `workstreams/unterkunft-anreise/anreise-infos.md` erstellt
- [ ] `dashboard/status.md` ist aktualisiert
