# Arbeitspakete – AI Transparency Days 2026

Dieses Verzeichnis enthält alle Arbeitspakete (APs) für die Planung und Durchführung der **AI Transparency Days 2026** (AITD 2026), gegliedert nach Ausführungsreihenfolge und Abhängigkeiten.

**Event:** 14.–16. Oktober 2026 | Nürnberg | 125 Teilnehmende | Veranstalter: COAI gGmbH  
**Projektabschluss (Übergabe):** 30. Juni 2026  
**Gesamtanzahl Arbeitspakete:** 52 (AP-001 bis AP-052)

---

## Abhängigkeitsgraph

```
Block 01 – Initialisierung
├── AP-001 Event-Konzept
├── AP-002 Budget-Rahmen          ← abhängig von AP-001
├── AP-003 Sponsoring-Strategie   ← abhängig von AP-001, AP-002
└── AP-004 Kommunikationsstrategie ← abhängig von AP-001
         │
         ▼
Block 02 – Venue & Programm-Konzept
├── AP-005 Venue-Anforderungen    ← abhängig von AP-001, AP-002
├── AP-006 Programm-Tracks        ← abhängig von AP-001
├── AP-007 CfP-Bewertungsrubrik   ← abhängig von AP-006
└── AP-008 Registrierung-Konzept  ← abhängig von AP-001
         │
         ▼
Block 03 – Recherche & Ausschreibung
├── AP-009 Venue-Recherche        ← abhängig von AP-005
├── AP-010 CfP-Text               ← abhängig von AP-006, AP-007
├── AP-011 Technik-Anforderungen  ← abhängig von AP-005, AP-006
├── AP-012 Hotel-Recherche        ← abhängig von AP-001
├── AP-013 Sponsoren-Recherche    ← abhängig von AP-003
└── AP-014 Catering-Konzept       ← abhängig von AP-005
         │
         ▼
Block 04 – Buchungen & Veröffentlichung
├── AP-015 Venue-Buchung          ← abhängig von AP-009
├── AP-016 CfP-Veröffentlichung   ← abhängig von AP-010
├── AP-017 Website-Launch         ← abhängig von AP-004, AP-008, AP-010
├── AP-018 Kommunikationsplan     ← abhängig von AP-004
└── AP-019 Content-Kalender       ← abhängig von AP-018
         │
         ▼
Block 05 – Umsetzung nach Venue-Buchung
├── AP-020 Raumplanung            ← abhängig von AP-015, AP-006
├── AP-021 Technik-Beschaffung    ← abhängig von AP-015, AP-011
├── AP-022 Catering beauftragen   ← abhängig von AP-015, AP-014
├── AP-023 Hotel-Kontingente      ← abhängig von AP-012
├── AP-024 Registrierung einrichten ← abhängig von AP-017, AP-008
├── AP-025 Sponsoren-Akquise      ← abhängig von AP-013, AP-015
└── AP-026 Anreise-Infos          ← abhängig von AP-015, AP-023
         │
         ▼
Block 06 – Programm & Teilnehmer
├── AP-027 CfP-Einreichungen sichten ← abhängig von AP-016 + CfP-Deadline
├── AP-028 Agenda erstellen        ← abhängig von AP-027, AP-020
├── AP-029 Speaker-Zusagen         ← abhängig von AP-027
├── AP-030 Speaker-Briefings       ← abhängig von AP-028, AP-029
├── AP-031 Session-Steckbriefe     ← abhängig von AP-028, AP-030
└── AP-032 Badge-Design            ← abhängig von AP-024
         │
         ▼
Block 07 – Personal & Abschluss
├── AP-033 Helferbedarf ermitteln  ← abhängig von AP-028, AP-020
├── AP-034 Helfer-Rekrutierung     ← abhängig von AP-033
├── AP-035 Schichtplan             ← abhängig von AP-034, AP-028
├── AP-036 Teilnehmer-Infopakete   ← abhängig von AP-030, AP-026
├── AP-037 Programm-Kommunikation  ← abhängig von AP-031, AP-019
└── AP-038 Beschilderung           ← abhängig von AP-020
         │
         ▼
Block 08 – Übergabe (Projektabschluss 30.06.2026)
├── AP-039 Übergabedokumentation   ← abhängig von Block 07
├── AP-040 Zugänge übergeben       ← abhängig von AP-039
├── AP-041 Offene TODOs            ← abhängig von AP-039
└── AP-042 Abschlussbericht        ← abhängig von AP-039, AP-040, AP-041
         │
         ▼ (COAI übernimmt ab hier)
Block 09 – Event-Durchführung (COAI)
├── AP-043 Helfer-Briefing         ← abhängig von AP-035
├── AP-044 Aufbau & Technik        ← abhängig von AP-043
├── AP-045 Check-In-Management     ← abhängig von AP-043, AP-032
├── AP-046 Event-Betrieb           ← abhängig von AP-044, AP-045
└── AP-047 Abbau                   ← abhängig von AP-046
         │
         ▼
Block 10 – Nachbereitung (COAI)
├── AP-048 Feedback-Survey         ← abhängig von AP-046
├── AP-049 Materialien sammeln     ← abhängig von AP-047
├── AP-050 Feedback-Auswertung     ← abhängig von AP-048
├── AP-051 Lessons Learned         ← abhängig von AP-050, AP-049
└── AP-052 Repository aufräumen    ← abhängig von AP-051
```

---

## Übersicht aller Blöcke

| Block | Name | Zeitraum | APs | Verantwortung |
|---|---|---|---|---|
| **01** | Initialisierung | Apr 2026 (Woche 1–2) | AP-001–004 | Studierendenteam |
| **02** | Venue & Programm-Konzept | Apr 2026 (Woche 2–3) | AP-005–008 | Studierendenteam |
| **03** | Recherche & Ausschreibung | Apr–Mai 2026 | AP-009–014 | Studierendenteam |
| **04** | Buchungen & Veröffentlichung | Mai 2026 (ab 01.05.) | AP-015–019 | Studierendenteam |
| **05** | Umsetzung nach Venue-Buchung | Mai–Jun 2026 | AP-020–026 | Studierendenteam |
| **06** | Programm & Teilnehmer | Jun 2026 (nach CfP-Deadline) | AP-027–032 | Studierendenteam |
| **07** | Personal & Abschluss | Jun 2026 (letzte 2 Wochen) | AP-033–038 | Studierendenteam |
| **08** | Übergabe | bis 30.06.2026 | AP-039–042 | Studierendenteam |
| **09** | Event-Durchführung | 13.–16. Okt 2026 | AP-043–047 | **COAI** |
| **10** | Nachbereitung | Okt–Nov 2026 | AP-048–052 | **COAI** |

---

## Wie dieses System benutzt wird

### Für Agenten

1. **Lese zuerst `config/event.yaml`** – dort stehen alle Eckdaten des Events.
2. **Wähle den aktuellen Block** basierend auf dem heutigen Datum und dem Projektstatus in `dashboard/status.md`.
3. **Bearbeite APs innerhalb eines Blocks parallel** – innerhalb eines Blocks gibt es keine Blockierungen.
4. **Prüfe die Voraussetzungen** jedes AP-Files, bevor du anfängst.
5. **Schreibe Outputs in die angegebenen Pfade** unter `workstreams/`.
6. **Aktualisiere den Status** in `dashboard/status.md` nach Abschluss jedes APs.

### Ausführungsregel

```
Blöcke = strikt sequenziell (Block N+1 erst starten wenn Block N abgeschlossen)
APs innerhalb eines Blocks = parallel ausführbar
```

### Statuswerte

| Symbol | Bedeutung |
|---|---|
| ⬜ | Offen – noch nicht begonnen |
| 🔄 | In Bearbeitung |
| ✅ | Abgeschlossen |
| ❌ | Blockiert (Voraussetzung fehlt) |
| ⏭️ | Übersprungen (nicht relevant) |

---

## Legende

| Symbol | Bedeutung |
|---|---|
| 🔴 Kritisch | Blockiert andere APs oder den Projektfortschritt |
| 🟡 Hoch | Wichtig für Meilensteine |
| 🟢 Normal | Kann ohne sofortigen Zeitdruck erledigt werden |

---

## Workstream-Zuordnung

| Workstream | Ordner | Zuständiger Agent |
|---|---|---|
| Programm & Inhalt | `workstreams/programm/` | `programm.md` |
| Kommunikation & Marketing | `workstreams/kommunikation/` | `kommunikation.md` |
| Teilnehmer-Management | `workstreams/teilnehmer/` | `operations.md` |
| Venue & Logistik | `workstreams/venue-logistik/` | `operations.md` |
| Catering | `workstreams/catering/` | `operations.md` |
| Technik | `workstreams/technik/` | `operations.md` |
| Personal & Helfer | `workstreams/personal/` | `operations.md` |
| Sponsoring | `workstreams/sponsoring/` | `kommunikation.md` |
| Unterkunft & Anreise | `workstreams/unterkunft-anreise/` | `operations.md` |
| Nachbereitung | `workstreams/nachbereitung/` | `dokumentation.md` |
