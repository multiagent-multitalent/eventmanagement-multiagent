# 🎪 Terminal-CLI Referenz

**Die Event-Management-Anwendung läuft jetzt vollständig im Terminal – kein Streamlit mehr.**

---

## 🚀 Schnellstart

### Installation

```bash
# Abhängigkeiten installieren
pip install -r requirements.txt
```

### Starten

```bash
# Standard-Modus
python -m src.cli

# Mit Automatisierung (keine Benutzer-Eingaben)
python -m src.cli --auto

# Mit spezifischem LLM-Modell
python -m src.cli --provider ollama --model llama3.2 --base-url http://localhost:11434

# Mit OpenAI/Anthropic
python -m src.cli --provider openai --model gpt-4 --api-key sk-...
```

---

## 📋 Kommandozeilen-Optionen

| Option | Beispiel | Beschreibung |
|--------|----------|-------------|
| `--auto` | `--auto` | Automatischer Modus: wählt erste Option, keine Benutzer-Eingaben |
| `--venue` | `--venue "Halle A"` | Venue automatisch auswählen |
| `--catering` | `--catering "Catering XY"` | Catering automatisch auswählen |
| `--provider` | `--provider ollama` | LLM-Provider: `ollama`, `openai`, `openai-compatible`, `anthropic`, `lmstudio`, `lokalai` |
| `--model` | `--model llama3.2` | LLM-Modellname |
| `--base-url` | `--base-url http://localhost:11434` | LLM-Server-URL (für lokal gehostete Modelle) |
| `--api-key` | `--api-key sk-...` | API-Key für externe Services (OpenAI, etc.) |

---

## 📦 Ausgabe-Struktur

Die CLI erstellt **nur Markdown-Dateien**:

```
workstreams/
├── PLANUNGSLOG.md                  ← Master-Log aller Planungsschritte
├── event-planning-output.md        ← Vollständiger Output (Alternative zu JSON)
├── programm/
│   ├── TASKS.md                   ← Aufgaben für Programmbereich
│   ├── action-plan-*.md           ← Aktionspläne
│   ├── status-*.md                ← Statusberichte
│   └── research-*.md              ← Recherche-Ergebnisse
├── kommunikation/
│   ├── TASKS.md
│   └── status-*.md
├── catering/
│   ├── TASKS.md
│   ├── catering-konzept.md
│   └── research-*.md
├── venue-logistik/
│   ├── TASKS.md
│   ├── venue-recherche.md
│   └── action-plan-*.md
└── [weitere Workstreams...]
```

---

## 🎯 Beispiele

### Beispiel 1: Standard-Ausführung (interaktiv)

```bash
$ python -m src.cli

╔════════════════════════════════════════════════════════════╗
║                   🎪  EVENT-MANAGEMENT                     ║
║              Orchestrator – Universal CLI                  ║
║                 Vollautomatische Planung                   ║
╚════════════════════════════════════════════════════════════╝

📋 Event-Konfiguration
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Event:             ┃ AI Transparency Days 2026        ┃
┃ Datum:             ┃ 2026-10-14 – 2026-10-16          ┃
┃ Ort:               ┃ Nürnberg, Deutschland            ┃
┃ Teilnehmer:        ┃ 125                              ┃
┗━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

🤖 LLM-Konfiguration
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Provider:          ┃ ollama                           ┃
┃ Modell:            ┃ llama3.2                         ┃
┃ Base-URL:          ┃ http://localhost:11434           ┃
┗━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

📦 Initialisiere Workflow...

🚀 Starte Planung...

🏢 Venue-Optionen
┏───┬─────────────────────┬───────────┬──────────┬────────────────┓
┃ # ┃ Name                ┃ Kosten    ┃ Bewertung┃ Beschreibung    ┃
┡━━━┼─────────────────────┼───────────┼──────────┼────────────────┩
│ 1 │ Halle A             │ 50.000 €  │ ⭐⭐⭐⭐  │ Modern, zentral │
│ 2 │ Convention Center   │ 75.000 €  │ ⭐⭐⭐⭐⭐│ Premium, groß   │
│ 3 │ Gemeindehaus        │ 15.000 €  │ ⭐⭐     │ Kompakt         │
└───┴─────────────────────┴───────────┴──────────┴────────────────┘

Venue auswählen (1-3, oder Enter für 1): 1

✅ Planung abgeschlossen

✅ Fortschritt
┏────────────────┳──────┓
┃ Metrik         ┃ Wert ┃
┡━━━━━━━━━━━━━━━━┇━━━━━━┩
│ Arbeitspakete  │ 8/8  │
│ Fortschritt    │ 100% │
│ Status         │ ✅   │
└────────────────┴──────┘

✓ Planungslog gespeichert: workstreams/PLANUNGSLOG.md

🎉 Fertig

✅ Planung erfolgreich abgeschlossen!

Alle Logs wurden in workstreams/ als Markdown gespeichert.

Nächste Schritte:
1. Überprüfe workstreams/PLANUNGSLOG.md
2. Arbeite in deinem bevorzugten Workstream-Ordner
3. Alle Änderungen sollten in Markdown dokumentiert werden

Hinweis: Diese CLI speichert alle Outputs als Markdown.
JSON-Dateien werden nicht mehr erzeugt.
```

### Beispiel 2: Automatischer Modus

```bash
python -m src.cli --auto --venue "Convention Center" --catering "Kochkollektiv"
```

### Beispiel 3: Mit spezifischem Modell

```bash
python -m src.cli --provider ollama --model llama2 --base-url http://localhost:11434
```

---

## 🔧 Konfiguration

### LLM-Provider

**Lokal gehostete Modelle:**

- `--provider ollama` – Ollama (bevorzugt für lokal-first)
- `--provider lmstudio` – LM Studio
- `--provider localai` – LocalAI
- `--provider openai-compatible` – Beliebiger OpenAI-kompatibler Server

**Remote-Services:**

- `--provider openai` – OpenAI GPT-4, GPT-3.5
- `--provider anthropic` – Claude
- `--provider huggingface` – Hugging Face Inference

### Umgebungsvariablen

```bash
export LLM_PROVIDER=ollama
export LLM_MODEL=llama3.2
export LLM_BASE_URL=http://localhost:11434
export LLM_API_KEY=local

python -m src.cli
```

---

## 📁 Datei-Management

### Ausgaben nach Lauf

Nach jeder CLI-Ausführung wird automatisch erstellt:

1. **PLANUNGSLOG.md** – Aktualisiert
2. **[workstream]/TASKS.md** – Aufgaben pro Bereich
3. **[workstream]/research-*.md** – Neue Recherche-Dateien
4. **[workstream]/action-plan-*.md** – Neue Action-Pläne
5. **[workstream]/status-*.md** – Neue Status-Reports

### Alte JSON-Dateien

⚠️ **Wichtig:** JSON-Dateien sind **vollständig entfernt**. Falls du alte Dateien hast:

```bash
# Optionale Bereinigung
rm workstreams/event-planning-output.json
rm workstreams/PLANUNGSLOG.json
```

Beide sind in Markdown migriert.

---

## 🐛 Troubleshooting

### Problem: CLI startet nicht

```bash
# Abhängigkeiten installiert?
pip install -r requirements.txt

# Python-Umgebung korrekt?
python --version   # sollte 3.10+ sein

# Arbeite von Projekt-Root aus
cd c:\Git\eventmanagement-multiagent
python -m src.cli
```

### Problem: LLM wird nicht erkannt

```bash
# Prüfe ob Server läuft (für Ollama)
curl http://localhost:11434/api/tags

# Explizit angeben
python -m src.cli --provider ollama --model llama3.2
```

### Problem: Interaktive Eingabe nicht möglich

Der Non-interactive-Modus wird automatisch erkannt. Nutze `--auto` oder spezifische Optionen:

```bash
python -m src.cli --auto --venue "XY" --catering "ZY"
```

---

## 📚 Weitere Ressourcen

- [Markdown-Workflow Anleitung](../docs/MARKDOWN-WORKFLOW.md)
- [Event-Konfiguration](../config/event.yaml)
- [QUICKSTART](../QUICKSTART.md)
- [Planungslog](../workstreams/PLANUNGSLOG.md)

---

*Dokumentation gültig ab: April 2026*
