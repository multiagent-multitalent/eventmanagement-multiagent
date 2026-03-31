# Event-Management mit KI-Agenten

Dieses Repository ist ein wiederverwendbares System zur Event-Planung mit spezialisierten KI-Agenten.
Die Demo-Implementierung ist AI Transparency Days 2026 unter [examples/aitd-2026](examples/aitd-2026).

## Startpunkte

1. Für Menschen: [QUICKSTART.md](QUICKSTART.md)
2. Für Agenten: [CLAUDE.md](CLAUDE.md)
3. Projektstatus: [dashboard/status.md](dashboard/status.md)
4. Bestätigungen: [CONFIRM.md](CONFIRM.md)

## Struktur auf einen Blick

| Bereich | Inhalt | Einstieg |
|---|---|---|
| Konfiguration | Event- und Teamdaten | [config/event.yaml](config/event.yaml), [config/team.yaml](config/team.yaml) |
| Steuerungsdoku | Rollen, Phasen, Ablagelogik | [docs/README.md](docs/README.md) |
| Arbeitspakete | Phasenbasierter Masterplan (was zu tun ist) | [arbeitspakete/README.md](arbeitspakete/README.md) |
| Workstreams | Laufende/generierte Artefakte (was schon erarbeitet ist) | [workstreams/README.md](workstreams/README.md) |
| Vorlagen | Wiederverwendbare Templates nach Bereich | [templates/README.md](templates/README.md) |
| Dashboard | Status- und Zeitsteuerung | [dashboard/status.md](dashboard/status.md), [dashboard/zeitplan.md](dashboard/zeitplan.md) |
| Orchestrator-Code | Python-Code für CLI/UI/Workflow | [src/main.py](src/main.py), [streamlit_app.py](streamlit_app.py) |
| Demo-Outputs | Vollständiges Referenzbeispiel | [examples/README.md](examples/README.md) |

## Typischer Ablauf

1. Eventdaten in [config/event.yaml](config/event.yaml) pflegen.
2. Orchestrator starten (Agent oder Streamlit).
3. Ergebnisse in [workstreams](workstreams) und Status in [dashboard/status.md](dashboard/status.md) prüfen.
4. Entscheidungen in [CONFIRM.md](CONFIRM.md) bestätigen.

## Lokaler Betrieb

CLI:

```bash
python -m src.main
```

Streamlit:

```bash
streamlit run streamlit_app.py
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
