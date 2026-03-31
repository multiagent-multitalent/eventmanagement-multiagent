# AP-041: Offene TODOs dokumentieren

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-041 |
| **Workstream** | Nachbereitung |
| **Agent** | Koordination (`.claude/agents/koordination.md`) |
| **Phase** | Phase 4: Übergabe |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 26.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Alle offenen Aufgaben, die nach der Übergabe von COAI erledigt werden müssen, vollständig und priorisiert dokumentieren – damit nichts vergessen wird.

## Voraussetzungen (Abhängigkeiten)
- AP-039: Übergabedokumentation erstellen

## Eingaben (Inputs)
- `dashboard/status.md` – alle APs mit Status
- `workstreams/nachbereitung/uebergabe-dokumentation.md` – offene Punkte aus Übergabedokument
- Alle Workstream-Dokumente auf offene Checkbox-Punkte prüfen

## Aufgaben (Checkliste)
- [ ] Alle Workstreams systematisch auf offene Aufgaben durchsuchen (ungecheckte Checkboxen in AP-Dateien)
- [ ] Offene Punkte aus allen laufenden Verträgen (Catering, Technik, Hotel) dokumentieren (finale Mengenangaben, Restfristen)
- [ ] Kommunikations-TODOs für Juli–Oktober identifizieren (aus Content-Kalender)
- [ ] Sponsoring-TODOs: noch laufende Akquise-Gespräche dokumentieren
- [ ] Technik-TODOs: offene Beschaffungen oder Buchungen
- [ ] Personal-TODOs: Helfer-Schichtplan noch zu verfeinern?
- [ ] Alle TODOs priorisieren: 🔴 Dringend (sofort nach Übergabe), 🟡 Wichtig (bis September), 🟢 Nice-to-have
- [ ] Offene TODOs in `workstreams/nachbereitung/offene-todos.md` mit Verantwortlichen und Deadlines dokumentieren

## Ausgaben (Outputs)
- `workstreams/nachbereitung/offene-todos.md` – priorisierte Liste aller offenen Aufgaben mit Deadlines und empfohlenen Verantwortlichen

## Hinweise für den Agenten
- Sei ehrlich und vollständig – eine unvollständige TODO-Liste ist schlimmer als eine lange.
- Ordne jeden TODO dem zuständigen Workstream zu, damit COAI sofort weiß, wer kümmert sich.
- Dokumentiere auch, warum ein TODO noch offen ist (Abhängigkeit von Daten, Entscheidung, Termin).
