# Event-Management mit KI-Agenten

Dieses Repository ist ein wiederverwendbares System zur Event-Planung mit spezialisierten KI-Agenten.
Die Demo-Implementierung ist AI Transparency Days 2026 unter [examples/aitd-2026](examples/aitd-2026).

## Startpunkte

1. Für Menschen: [QUICKSTART.md](QUICKSTART.md)
2. Vollständige Anleitung: [ANLEITUNG.md](ANLEITUNG.md)
3. Für Agenten: [CLAUDE.md](CLAUDE.md)
4. Projektstatus: [dashboard/status.md](dashboard/status.md)
5. Bestätigungen: [CONFIRM.md](CONFIRM.md)

## Struktur auf einen Blick

| Bereich | Inhalt | Einstieg |
|---|---|---|
| Konfiguration | Event- und Teamdaten | [config/event.yaml](config/event.yaml), [config/team.yaml](config/team.yaml) |
| Steuerungsdoku | Rollen, Phasen, Ablagelogik | [docs/README.md](docs/README.md) |
| Arbeitspakete | Phasenbasierter Masterplan (was zu tun ist) | [arbeitspakete/README.md](arbeitspakete/README.md) |
| Workstreams | Laufende/generierte Artefakte (was schon erarbeitet ist) | [workstreams/README.md](workstreams/README.md) |
| Vorlagen | Wiederverwendbare Templates nach Bereich | [templates/README.md](templates/README.md) |
| Orchestrator-Code | Python-Code für Terminal-CLI | [src/cli.py](src/cli.py), [src/main.py](src/main.py) |
| CLI-Referenz | Terminal-Kommandos und Optionen | [docs/TERMINAL-CLI.md](docs/TERMINAL-CLI.md) |
| Markdown-Workflow | Dokumentations-Standards | [docs/MARKDOWN-WORKFLOW.md](docs/MARKDOWN-WORKFLOW.md) |
| Demo-Outputs | Vollständiges Referenzbeispiel | [examples/README.md](examples/README.md) |

## Typischer Ablauf

1. Eventdaten in [config/event.yaml](config/event.yaml) pflegen.
2. Terminal-CLI starten: `python -m src.cli`
3. Ergebnisse in [workstreams/PLANUNGSLOG.md](workstreams/PLANUNGSLOG.md) prüfen
4. Entscheidungen in [CONFIRM.md](CONFIRM.md) bestätigen.

## Lokaler Betrieb

Terminal-CLI:

```bash
python -m src.cli
```

Automatischer Modus:

```bash
python -m src.cli --auto
```

Smoke-Test:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Ablageregel

- Neues im Planungsprozess: nach [arbeitspakete](arbeitspakete)
- Neue operative Ergebnisse: nach [workstreams](workstreams)
- Wiederverwendbare Muster: nach [templates](templates)
- Methoden und Governance: nach [docs](docs)

Details: [docs/repository-structure.md](docs/repository-structure.md)
