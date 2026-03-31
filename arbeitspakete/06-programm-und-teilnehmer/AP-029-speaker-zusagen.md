# AP-029: Speaker-Zusagen einholen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-029 |
| **Workstream** | Programm & Inhalt |
| **Agent** | Programm (`.claude/agents/programm.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 15.06.2026 – 25.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Alle akzeptierten Speaker über ihre Annahme informieren, abgelehnte Einreichende benachrichtigen und verbindliche Zusagen von allen Keynote-Speakern und Session-Referierenden einholen.

## Voraussetzungen (Abhängigkeiten)
- AP-027: CfP-Einreichungen sichten und bewerten

## Eingaben (Inputs)
- `workstreams/programm/cfp-entscheidungen.md` – Liste akzeptierter/abgelehnter Einreichungen
- `config/event.yaml` – Event-Daten für Kommunikation

## Aufgaben (Checkliste)
- [ ] Benachrichtigungs-E-Mails verfassen: Annahme-E-Mail (mit nächsten Schritten), Ablehnung-E-Mail (mit Dank), Warteliste-E-Mail
- [ ] Alle akzeptierten Speaker per E-Mail über Annahme informieren
- [ ] Alle abgelehnten Einreichenden per E-Mail benachrichtigen
- [ ] Verbindliche Zusage (Bestätigung) von jedem akzeptierten Speaker anfordern
- [ ] Zusagen im Tracking-Dokument vermerken
- [ ] Bei Nicht-Antwort: Nachfassen nach 5 Werktagen
- [ ] Absagen von akzeptierten Speakern: Warteliste aktivieren und nächste Kandidaten anfragen
- [ ] Speaker-Daten für Website und Briefings sammeln: Foto, Bio (100 Wörter), Social-Media-Links, technische Anforderungen
- [ ] Speaker-Zusagen in `workstreams/programm/speaker-zusagen.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/programm/speaker-zusagen.md` – vollständige Speaker-Liste mit Zusage-Status, Kontaktdaten und gesammelten Daten

## Hinweise für den Agenten
- Setze eine klare Rückmelde-Deadline für die Bestätigung (z.B. 7 Werktage nach Benachrichtigung).
- Frage aktiv nach besonderen Bedürfnissen oder technischen Anforderungen (spezielle Software, HDMI-Adapter etc.).
- Speaker-Infos (Foto, Bio) werden direkt für die Website und das Session-Steckbrief-Dokument (AP-031) benötigt.
