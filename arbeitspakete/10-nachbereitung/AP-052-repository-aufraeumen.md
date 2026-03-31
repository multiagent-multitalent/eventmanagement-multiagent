# AP-052: Repository aufräumen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-052 |
| **Workstream** | Nachbereitung |
| **Agent** | Dokumentation (`.claude/agents/dokumentation.md`) |
| **Phase** | Phase 6: Nachbereitung |
| **Priorität** | 🟢 Normal |
| **Zeitraum** | 22.11.2026 – 30.11.2026 |
| **Status** | ⬜ Offen |

## Ziel
Das Repository in einen sauberen, gut dokumentierten Zustand bringen, der als Vorlage für zukünftige Events (AITD 2027) dienen kann.

## Voraussetzungen (Abhängigkeiten)
- AP-051: Lessons Learned dokumentieren

## Eingaben (Inputs)
- Gesamtes Repository
- `workstreams/nachbereitung/lessons-learned.md`

## Aufgaben (Checkliste)
- [ ] Repository-Struktur prüfen: Sind alle Workstream-Ordner vollständig befüllt?
- [ ] Entwurfs-Dateien und Duplikate entfernen oder in Archiv verschieben
- [ ] Sensible Daten prüfen: Keine Passwörter, Kontaktdaten (Privatpersonen) oder Vertragsdetails im öffentlichen Repository
- [ ] `dashboard/status.md` auf finalen Stand aktualisieren (alle APs als ✅ oder ⏭️ markieren)
- [ ] `README.md` des Repositories aktualisieren (Event 2026 als abgeschlossen markieren, Hinweis auf AITD 2027)
- [ ] `config/event.yaml` mit tatsächlichen Werten aktualisieren (finale Teilnehmerzahl, tatsächliche Venue etc.)
- [ ] Archiv mit allen wichtigen Entscheidungen und Dokumenten befüllen
- [ ] Repository-Tag für AITD-2026-Abschluss setzen (git tag)
- [ ] Anleitung zum Klonen des Repositories für AITD 2027 in README.md einfügen

## Ausgaben (Outputs)
- Bereinigtes, vollständig dokumentiertes Repository als Vorlage für AITD 2027

## Hinweise für den Agenten
- Denke beim Aufräumen immer aus der Perspektive einer neuen Person, die das Repository für AITD 2027 klont – was fehlt? Was ist unklar?
- Erstelle einen kurzen „How to reuse this repository"-Abschnitt in der README.md.
- Stelle sicher, dass alle personenbezogenen Daten (Teilnehmerlisten, Kontaktdaten) aus dem öffentlichen Repository entfernt sind – diese gehören in sichere, separate Speicher.
