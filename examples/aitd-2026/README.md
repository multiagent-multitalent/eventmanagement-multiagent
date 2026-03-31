# Demo-Beispiel: AI Transparency Days 2026 (AITD 2026)

Dieses Verzeichnis enthält alle Planungsartefakte, die der Orchestrator-Agent automatisch für die **AI Transparency Days 2026** generiert hat – als Beispiel dafür, was das System für dein Event erzeugen kann.

## Was dieses Demo zeigt

Der Orchestrator hat ausgehend von `config/event.yaml` vollständig automatisch generiert:

| Datei | Inhalt |
|---|---|
| `config/event.yaml` | Event-Konfiguration (125 Teilnehmer, Nürnberg, 14.–16. Oktober 2026) |
| `config/team.yaml` | Team-Vorlage mit Rollen und Verantwortlichkeiten |
| `dashboard/status.md` | Vollständiges Planungs-Dashboard mit Workstream-Status |
| `CONFIRM.md` | Finale Bestätigung mit allen Entscheidungspunkten |
| `PLANUNGSLOG.md` | Chronologischer Planungslog |
| `archiv/entscheidungslog.md` | Alle getroffenen Entscheidungen |

### Generierte Workstream-Artefakte

| Workstream | Dateien |
|---|---|
| Programm | track-konzept.md, cfp-ausschreibung.md, agenda-entwurf.md |
| Kommunikation | kommunikationsplan.md, social-media-kit.md |
| Venue & Logistik | venue-recherche.md |
| Teilnehmer | registrierung-konzept.md |
| Catering | catering-konzept.md |
| Technik | technik-anforderungen.md |
| Personal | helfer-planung.md |
| Sponsoring | sponsoring-konzept.md, budget-rahmen.md |
| Unterkunft & Anreise | hotel-recherche.md |

## Wie du das System für dein eigenes Event nutzt

→ Geh zurück zum Hauptverzeichnis und lies **[QUICKSTART.md](../../QUICKSTART.md)**.

1. `config/event.yaml` mit deinen Event-Details befüllen
2. Orchestrator-Agenten starten
3. Alle Artefakte werden automatisch in `workstreams/` generiert

---

*Dies ist ein Demo-Output. Für ein neues Event: Hauptverzeichnis nutzen, nicht diesen Ordner.*
