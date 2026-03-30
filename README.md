# Event-Management mit KI-Agenten – AI Transparency Days 2026

Dieses Repository ist das zentrale Arbeits- und Dokumentationssystem für die Planung der **AI Transparency Days 2026 (AITD 2026)** mit KI-Agenten.

Es entsteht im Rahmen des Praxisprojekts *Sommersemester 2026* an der Hochschule Ansbach, in Zusammenarbeit mit der **COAI gGmbH** (Nürnberg).

---

## Schnellstart für KI-Agenten

→ Lies zuerst **[CLAUDE.md](CLAUDE.md)** – dort wird erklärt, wie das System funktioniert.

## Schnellstart für Menschen

1. **Event-Konfiguration:** [`config/event.yaml`](config/event.yaml) – Eckdaten des Events
2. **Team-Konfiguration:** [`config/team.yaml`](config/team.yaml) – Rollen und Verantwortliche eintragen
3. **Dashboard:** [`dashboard/status.md`](dashboard/status.md) – aktueller Stand aller Arbeitsbereiche
4. **Phasenmodell:** [`docs/phasenmodell.md`](docs/phasenmodell.md) – was wann passieren muss

---

## Repository-Struktur

```text
eventmanagement-multiagent/
├── CLAUDE.md                        # Einstiegspunkt für KI-Agenten
├── Task Requirements.md             # Aufgabenstellung des Projekts
├── .claude/agents/                  # 5 Agenten-Konfigurationen
│   ├── kommunikation.md
│   ├── operations.md
│   ├── programm.md
│   ├── koordination.md
│   └── dokumentation.md
├── docs/                            # Phasenmodell, Workstreams, Rollen
│   ├── phasenmodell.md
│   ├── workstreams.md
│   └── rollen.md
├── templates/                       # Artefakt-Vorlagen für alle Phasen
│   ├── programm/                    # CfP, Agenda, Speaker-Briefing
│   ├── kommunikation/               # Content-Kalender, Pressemitteilung
│   ├── venue-logistik/              # Venue-Anforderungen
│   ├── nachbereitung/               # Protokoll, Feedback-Survey
│   └── ...
├── config/                          # Event- und Team-Konfiguration
│   ├── event.yaml
│   └── team.yaml
├── workstreams/                     # Laufende Arbeit pro Bereich
│   ├── programm/
│   ├── kommunikation/
│   ├── teilnehmer/
│   ├── venue-logistik/
│   ├── catering/
│   ├── technik/
│   ├── personal/
│   ├── sponsoring/
│   ├── unterkunft-anreise/
│   └── nachbereitung/
├── dashboard/                       # Status und Tracking
│   └── status.md
└── archiv/                          # Lessons Learned, Entscheidungslog
    ├── entscheidungslog.md
    └── lessons-learned.md
```

---

## Das Event

**AI Transparency Days 2026** – Oktober 2026, Nürnberg  
100–150 Teilnehmer | 2–3 Tage | Vorträge + Workshops + Hackathon  
Veranstalter: [COAI gGmbH](https://www.coairesearch.org)

---

## Betreuung

- Prof. Dr. Sigurd Schacht (Hochschule Ansbach)
- Steffen Höpfner (COAI gGmbH)
