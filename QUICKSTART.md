# Quickstart: Event-Planung mit KI-Agenten

Dieses Repository ermöglicht vollständige Event-Planung durch KI-Agenten – du gibst die Event-Details ein, die Agenten erledigen den Rest. Es funktioniert für **jedes Event**: Konferenzen, Workshops, Hackathons, Seminare und mehr.

> **Demo:** Sieh dir [`examples/aitd-2026/`](examples/aitd-2026/) an – dort findest du alle Artefakte, die der Orchestrator für die AI Transparency Days 2026 automatisch generiert hat.

---

## In 3 Schritten zur fertigen Event-Planung

### Schritt 1: Event-Details eintragen (5 Minuten)

Öffne `config/event.yaml` und fülle die Felder aus:

```yaml
event:
  name: "Dein Event-Name"
  date_start: "YYYY-MM-DD"
  date_end: "YYYY-MM-DD"
  city: "Deine Stadt"
  attendees_expected: 100
  # ... weitere Details
```

Das war es. Der Rest läuft automatisch.

---

### Schritt 2: Orchestrator starten

Starte den **Orchestrator-Agenten** (`.claude/agents/orchestrator.md`) mit folgendem Prompt:

```
Lies config/event.yaml und führe die vollständige Event-Planung durch.
Generiere alle Artefakte für alle Workstreams gemäß CLAUDE.md.
```

Der Orchestrator übernimmt automatisch:

| Phase | Was passiert | Wer macht es |
|---|---|---|
| 🚀 Initialisierung | Event-Konzept, Team-Setup, Meilensteine | Orchestrator |
| 📋 Planung | Venue-Konzept, CfP, Budget-Rahmen, Kommunikationsplan | Alle 5 Agenten |
| ⚙️ Umsetzung | Alle Planungsartefakte generieren | Alle 5 Agenten |
| 🎯 Finalisierung | Dashboard aktualisieren, Bestätigung vorbereiten | Koordination |

---

### Schritt 3: Bestätigen (10 Minuten)

Öffne `CONFIRM.md` – dort findet sich eine Zusammenfassung aller generierten Artefakte und die finalen Entscheidungen, die menschliche Bestätigung brauchen:

- [ ] Event-Konzept freigeben
- [ ] Venue-Auswahl bestätigen
- [ ] Budget-Rahmen genehmigen
- [ ] Programm-Konzept bestätigen
- [ ] Kommunikationsplan freigeben

---

## Was der Orchestrator automatisch generiert

Nach dem Start erstellt der Orchestrator automatisch alle Planungsartefakte:

### Programm
- `workstreams/programm/track-konzept.md` – Detailliertes Track-Konzept mit 3 parallelen Tracks
- `workstreams/programm/cfp-ausschreibung.md` – Call for Papers (DE + EN)
- `workstreams/programm/agenda-entwurf.md` – Vorläufige Tagesagenda

### Kommunikation
- `workstreams/kommunikation/kommunikationsplan.md` – Kommunikationsplan mit Zeitlinie
- `workstreams/kommunikation/social-media-kit.md` – Social-Media-Posts für alle Phasen
- `workstreams/kommunikation/pressemitteilung-entwurf.md` – Pressemitteilung-Entwurf

### Venue & Logistik
- `workstreams/venue-logistik/venue-recherche.md` – Venue-Anforderungen und Recherche-Grundlage
- `workstreams/venue-logistik/raumplan-entwurf.md` – Raumplanung auf Basis der Teilnehmerzahl

### Teilnehmer
- `workstreams/teilnehmer/registrierung-konzept.md` – Registrierungskonzept und Ticket-Kategorien
- `workstreams/teilnehmer/teilnehmer-infopaket.md` – Willkommens-E-Mail und Infopaket

### Catering
- `workstreams/catering/catering-konzept.md` – Verpflegungskonzept für alle Event-Tage
- `workstreams/catering/anbieter-liste.md` – Recherche-Grundlage für Catering-Anbieter

### Technik
- `workstreams/technik/technik-anforderungen.md` – Technische Anforderungen pro Raum
- `workstreams/technik/technik-checkliste.md` – Checkliste für On-Site-Technik

### Personal
- `workstreams/personal/helfer-planung.md` – Helferbedarf und Schichtplan-Entwurf
- `workstreams/personal/helfer-briefing.md` – Briefing-Vorlage für freiwillige Helfer

### Sponsoring & Budget
- `workstreams/sponsoring/sponsoring-konzept.md` – Sponsoring-Pakete und Ansprache-Strategie
- `workstreams/sponsoring/budget-rahmen.md` – Grober Budget-Rahmen

### Unterkunft & Anreise
- `workstreams/unterkunft-anreise/hotel-recherche.md` – Hotel-Recherche-Grundlage
- `workstreams/unterkunft-anreise/anreise-info.md` – Anreiseinformationen für Teilnehmer

### Nachbereitung
- `workstreams/nachbereitung/feedback-plan.md` – Feedback-Strategie und Survey-Link-Plan

### Koordination
- `dashboard/status.md` – Aktualisierter Dashboard-Status
- `archiv/entscheidungslog.md` – Dokumentierte Entscheidungen

---

## Für ein neues Event: Repository klonen

```bash
git clone https://github.com/multiagent-multitalent/eventmanagement-multiagent.git mein-event
cd mein-event
# config/event.yaml mit deinen Event-Details ausfüllen
# Orchestrator starten → alle Planungsartefakte werden in workstreams/ generiert
```

Die `config/event.yaml` enthält Demo-Werte der AI Transparency Days 2026 als Orientierung. Ersetze diese mit deinen eigenen Event-Details.

---

## Hilfe & Orientierung

| Frage | Antwort findest du hier |
|---|---|
| Wie funktioniert das System? | `CLAUDE.md` |
| Aktueller Planungsstand? | `dashboard/status.md` |
| Welche Entscheidungen wurden getroffen? | `archiv/entscheidungslog.md` |
| Welche Artefakte gibt es? | `workstreams/*/README.md` |
| Wie sind die Agenten konfiguriert? | `.claude/agents/` |

---

*Ziel: Du gibst die Event-Details ein – die Agenten erledigen den Rest. Nur die finale Bestätigung liegt bei dir.*
