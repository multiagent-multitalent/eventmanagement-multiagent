# Quickstart

In 3 Schritten zur lauffähigen Event-Planung mit Agenten.

## 1. Konfiguration eintragen

Pflege die Basisdaten in:

- [config/event.yaml](config/event.yaml)
- [config/team.yaml](config/team.yaml)

## 2. Planung starten

Es gibt zwei Wege.

Agentisch über den Orchestrator:

- Einstieg: [CLAUDE.md](CLAUDE.md)
- Orchestrator-Profil: [.claude/agents/orchestrator.md](.claude/agents/orchestrator.md)

Oder lokal als App:

```bash
streamlit run streamlit_app.py
```

Optional CLI:

```bash
python -m src.main
```

## 3. Ergebnisse prüfen und bestätigen

1. Status prüfen: [dashboard/status.md](dashboard/status.md)
2. Workstream-Artefakte prüfen: [workstreams/README.md](workstreams/README.md)
3. Entscheidungen bestätigen: [CONFIRM.md](CONFIRM.md)

## Orientierung

- Dokumentationsindex: [docs/README.md](docs/README.md)
- Arbeitspaket-Masterplan: [arbeitspakete/README.md](arbeitspakete/README.md)
- Template-Übersicht: [templates/README.md](templates/README.md)
- Demo-Ausgabe: [examples/aitd-2026](examples/aitd-2026)
