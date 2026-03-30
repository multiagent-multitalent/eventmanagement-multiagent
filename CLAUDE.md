# CLAUDE.md – Einstiegspunkt für KI-Agenten

Willkommen im Event-Management-System für die **AI Transparency Days 2026** (AITD 2026).

Dieses Repository ist das zentrale Arbeitssystem für alle Planungsprozesse. Du als Agent kannst hier:
- Den aktuellen Planungsstand einsehen (`dashboard/status.md`)
- Aufgaben in den Workstreams bearbeiten (`workstreams/`)
- Vorlagen für Artefakte nutzen (`templates/`)
- Die Konfiguration des Events lesen (`config/event.yaml`)
- Das Phasenmodell und die Rollen nachschlagen (`docs/`)

---

## Wie dieses System funktioniert

### Agenten-Rollen

Es gibt **5 spezialisierte Agenten**, jeder mit eigenem Fokusbereich:

| Agent | Datei | Fokus |
|---|---|---|
| Kommunikation | `.claude/agents/kommunikation.md` | Social Media, Newsletter, Presse, E-Mail |
| Operations | `.claude/agents/operations.md` | Checklisten, Logistik, Bestellungen, Abhängigkeiten |
| Programm | `.claude/agents/programm.md` | CfP, Zeitplan, Sessions, Speaker-Briefings |
| Koordination | `.claude/agents/koordination.md` | Dashboard, Status-Updates, Meilensteine, Risiken |
| Dokumentation | `.claude/agents/dokumentation.md` | Protokolle, Reports, Wissensbasis, Lessons Learned |

### Wo du anfangen sollst

1. **Lese `config/event.yaml`** – Event-Eckdaten, Datum, Ort, Größe
2. **Lese `dashboard/status.md`** – aktueller Stand aller Workstreams
3. **Lese deine Agenten-Konfiguration** in `.claude/agents/` – deine Rolle und Verantwortlichkeiten
4. **Arbeite im passenden Workstream** unter `workstreams/`

### Planungsphasen

Das Event folgt einem strukturierten Phasenmodell (Details: `docs/phasenmodell.md`):

1. **Initialisierung** (Kick-off, Konzept)
2. **Planung** (Struktur, Venue, Programm, Budget)
3. **Umsetzung** (Umsetzung aller Arbeitspakete)
4. **Durchführung** (Vor-Ort, Event-Tage)
5. **Nachbereitung** (Feedback, Dokumentation, Lessons Learned)

### Workstreams

Jeder Workstream hat einen eigenen Ordner unter `workstreams/` mit:
- `README.md` – Aufgaben, Status, Verantwortliche
- Artefakten und Arbeitsdokumenten

### Vorlagen

Unter `templates/` liegen Vorlagen für alle Planungsphasen – gegliedert nach Workstream. Nutze diese als Ausgangspunkt für neue Dokumente.

### Prinzip: Agenten unterstützen, Menschen entscheiden

- Agenten übernehmen Routinearbeit (Checklisten, Statusverfolgung, Textentwürfe)
- Menschen treffen strategische Entscheidungen, führen Gespräche, gestalten kreativ

---

## Repository-Struktur

```text
eventmanagement-multiagent/
├── CLAUDE.md                        # Dieser Einstiegspunkt
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

## Für neue Teammitglieder

Frage einfach einen der Agenten:
- „Wie funktioniert die Eventplanung in diesem Projekt?"
- „Was muss als Nächstes passieren?"
- „Welche Artefakte fehlen noch in Workstream X?"
- „Wer ist für was verantwortlich?"

Der Agent liest diese Datei und die verlinkten Dokumente und gibt dir eine fundierte Antwort.

---

*Dieses Repository ist eine Vorlage und kann für zukünftige Events geklont werden. Konfiguriere einfach `config/event.yaml` und `config/team.yaml` und starte direkt.*
