# Event-Management mit KI-Agenten

Dieses Repository ist ein universelles Planungssystem für Events jeder Art – von Konferenzen über Workshops bis zu Hackathons. KI-Agenten übernehmen die gesamte Routineplanung; du gibst nur die Event-Details ein.

> **Demo-Beispiel:** Die AI Transparency Days 2026 (AITD 2026) dienen als Referenzimplementierung und zeigen, was das System automatisch generiert. Alle Demo-Artefakte liegen in [`examples/aitd-2026/`](examples/aitd-2026/).

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
├── QUICKSTART.md                    # 🚀 Schnellstart (3 Schritte)
├── CONFIRM.md                       # ✅ Bestätigungsdokument (nach Orchestrator-Lauf)
├── .claude/agents/                  # 6 Agenten-Konfigurationen
│   ├── orchestrator.md              # Master-Orchestrator
│   ├── kommunikation.md
│   ├── operations.md
│   ├── programm.md
│   ├── koordination.md
│   └── dokumentation.md
├── docs/                            # Phasenmodell, Workstreams, Rollen
├── templates/                       # Artefakt-Vorlagen für alle Phasen
├── config/                          # Event- und Team-Konfiguration
│   ├── event.yaml                   # ← Hier deine Event-Details eintragen
│   └── team.yaml
├── workstreams/                     # Laufende Arbeit pro Bereich (vom Orchestrator befüllt)
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
├── examples/                        # 📖 Demo-Outputs für fertige Events
│   └── aitd-2026/                   # AI Transparency Days 2026 – vollständiges Beispiel
├── dashboard/                       # Status und Tracking
│   └── status.md
└── archiv/                          # Entscheidungslog, Lessons Learned
```

---

## Für welche Events geeignet?

Das System funktioniert für jede Art von Event:

- **Konferenzen** (z. B. Fachkonferenzen, Community-Events)
- **Workshops & Seminare**
- **Hackathons**
- **Hybride Events** (Präsenz + Online)
- Jede Kombination davon

Einfach `config/event.yaml` anpassen – der Rest läuft automatisch.

---

## Demo-Beispiel

Die **AI Transparency Days 2026** (Konferenz, 125 Teilnehmer, Nürnberg) dienen als vollständiges Beispiel:

→ [`examples/aitd-2026/`](examples/aitd-2026/) – Alle generierten Artefakte ansehen
