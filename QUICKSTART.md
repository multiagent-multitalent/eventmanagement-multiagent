# 🚀 Quickstart

In 3 Schritten zur lauffähigen Event-Planung mit KI-Agenten.

---

## 1️⃣ Konfiguration vorbereiten

Pflege die Event-Basisdaten ein:

```bash
# Ediere diese Dateien:
config/event.yaml      # Event-Details, Datum, Ort, Budget
config/team.yaml       # Team-Zusammensetzung
```

Beispiel (`config/event.yaml`):

```yaml
event:
  name: "AI Transparency Days 2026"
  date_start: "2026-10-14"
  date_end: "2026-10-16"
  city: "Nürnberg"
  country: "Deutschland"
  attendees_expected: 125
  budget_total: 10000.0
```

---

## 2️⃣ Dependencies installieren

```bash
pip install -r requirements.txt
```

Dies installiert:
- `langchain>=0.3.0` – LLM-Integration
- `langgraph>=0.2.0` – Agent-Framework
- `pyyaml>=6.0` – YAML-Konfiguration
- `python-dotenv>=1.0` – Environment-Variablen
- `rich>=13.0` – Terminal-Formatting

---

## 3️⃣ Planung starten (Terminal-CLI)

### Standard-Modus (interaktiv)

```bash
python -m src.cli
```

Die CLI fragt nach Venue und Catering, dann startet die automatische Planung.

### Automatischer Modus

```bash
# Keine Benutzer-Eingaben, wählt automatisch erste Option
python -m src.cli --auto
```

### Mit Optionen

```bash
# Venue und Catering vorwählen
python -m src.cli --venue "Convention Center" --catering "Kochkollektiv"

# Mit spezifischem LLM-Modell
python -m src.cli --provider ollama --model llama3.2

# Mit externem Service
python -m src.cli --provider openai --model gpt-4 --api-key sk-...
```

---

## 📋 Ergebnisse prüfen

Nach der Planung findest du **nur Markdown-Dateien**:

```
workstreams/
├── PLANUNGSLOG.md                 ← Master-Log (immer lesen zuerst!)
├── programm/
│   ├── TASKS.md
│   ├── agenda-entwurf.md
│   └── ...
├── kommunikation/
│   ├── kommunikationsplan.md
│   └── ...
└── [weitere Workstreams...]
```

### Nächste Schritte nach Lauf

1. **Lese [workstreams/PLANUNGSLOG.md](workstreams/PLANUNGSLOG.md)**  
   → Überblick über alle Entscheidungen und Meilensteine

2. **Überprüfe die Workstream-Outputs**  
   → `workstreams/[workstream]/TASKS.md` – Aufgabenlisten  
   → `workstreams/[workstream]/status-*.md` – Status-Reports

3. **Treffe Entscheidungen**  
   → Benutzer-Eingaben geben Optionen vor, die du bestätigen kannst

4. **Git-Commit**  
   ```bash
   git add workstreams/
   git commit -m "Event-Planung: Initial planning completed"
   ```

---

## 📚 Weitere Ressourcen

| Ressource | Zweck |
|-----------|-------|
| [CLAUDE.md](CLAUDE.md) | 🤖 Für KI-Agenten: Systemüberblick |
| [docs/TERMINAL-CLI.md](docs/TERMINAL-CLI.md) | 🎯 Terminal-CLI Kommandoreferenz |
| [docs/MARKDOWN-WORKFLOW.md](docs/MARKDOWN-WORKFLOW.md) | 📝 Markdown-Workflow Anleitung |
| [workstreams/PLANUNGSLOG.md](workstreams/PLANUNGSLOG.md) | 📊 Aktueller Planungsstatus |
| [config/event.yaml](config/event.yaml) | ⚙️ Event-Konfiguration |
| [examples/aitd-2026](examples/aitd-2026) | 📖 Demo-Beispiel (AITD 2026) |

---

## ⚠️ Wichtige Hinweise

### Streamlit ist deprecated ❌

Die Streamlit-Integrierung wurde **vollständig entfernt**. Der Terminal-Mode ist jetzt der Standard.

- `streamlit run streamlit_app.py` funktioniert **nicht mehr**
- Verwende statt dessen: `python -m src.cli`

### JSON ist deprecated ❌

Alle Outputs erfolgen jetzt als **Markdown** (`.md`):

- ✅ Konsistente Formatierung
- ✅ Git-versionierbar
- ✅ Von Menschen lesbar
- ❌ Keine JSON-Dateien mehr

Alte `event-planning-output.json`-Dateien können gelöscht werden.

### Markdown ist das Standard-Format ✅

Siehe: [docs/MARKDOWN-WORKFLOW.md](docs/MARKDOWN-WORKFLOW.md)

---

## 🆘 Probleme?

| Problem | Lösung |
|---------|--------|
| CLI startet nicht | `pip install -r requirements.txt` |
| LLM nicht erkannt | `pip install langchain langchain-ollama pyyaml` |
| Interaktive Eingabe nicht möglich | `python -m src.cli --auto` |
| CUDA-Fehler beim lokalen Modell | Überprüfe deine GPU-Treiber oder nutze CPU-Mode |

---

*Quickstart gültig ab: April 2026*

**Viel Erfolg mit deiner Event-Planung! 🎉**

