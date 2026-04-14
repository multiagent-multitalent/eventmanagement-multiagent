# 📋 Markdown-Workflow Anleitung

**Ab Version: 2026-04**

Das Event-Management System verwendet **ausschließlich Markdown** für die Dokumentation und Logging. JSON-Dateien sind vollständig entfernt.

## 🎯 Prinzipien

1. **Nur Markdown** – Alle Outputs, Logs und Dokumentationen erfolgen als `.md`-Dateien
2. **Terminal-basiert** – Die App läuft vollständig im Terminal (keine UI-Frameworks)
3. **Human-readable** – Alle Logs sind für Menschen lesbar formatiert
4. **Versionierbar** – Markdown-Dateien können in Git verfolgt werden
5. **Struktur über Inhalt** – Einheitliche Markdown-Formate für alle Workstreams

---

## 📁 Verzeichnisstruktur

```
workstreams/
├── PLANUNGSLOG.md          ← Master-Log aller Planungsschritte
├── programm/
│   ├── TASKS.md            ← Aufgaben für Programmbereich
│   ├── action-plan-*.md    ← Aktionspläne
│   ├── status-*.md         ← Statusberichte
│   ├── research-*.md       ← Recherche-Ergebnisse
│   └── decision-*.md       ← Entscheidungen
├── kommunikation/
├── teilnehmer/
├── venue-logistik/
├── catering/
├── technik/
├── personal/
├── sponsoring/
├── unterkunft-anreise/
└── nachbereitung/
```

---

## 📝 Markdown-Dateitypen

### 1. **PLANUNGSLOG.md** (Master-Log)

Zentrale Dokumentation aller Planungsschritte.

```markdown
# Event-Planungslog: [Event-Name]

**Erstellt:** YYYY-MM-DD HH:MM:SS
**Version:** 1.0

## 📋 Event-Konfiguration

| Feld | Wert |
|------|------|
| **Name** | ... |
| **Datum** | ... |

## 📊 Workstream-Status

| Workstream | Status | Fortschritt | Verantwortlicher |
|-----------|--------|-------------|-----------------|
| Programm | 🔲 Pending | 0% | TBD |
| ... | ... | ... | ... |

## 📅 Timeline

... (siehe weiter unten)

## 📝 Entscheidungslog

- **[2026-04-14 10:30] Venue-Auswahl**  
  Gewählt: XY-Halle, kostet 50.000 EUR

## ⚠️ Risikobericht

- **Venue-Verfügbarkeit** (Likelihood: medium)  
  Mitigation: Ausweichort vorbereiten

---
**Zuletzt aktualisiert:** YYYY-MM-DD HH:MM:SS
```

### 2. **TASKS.md** (Workstream-Aufgaben)

Pro Workstream eine Aufgabenliste.

```markdown
# Arbeitspakete: [Workstream-Name]

**Aktualisiert:** YYYY-MM-DD HH:MM:SS

## Status-Übersicht

- ✅ **Abgeschlossen:** 5/10 (50%)
- 📊 **Fortschritt:** █████░░░░░ 50%

## Aufgaben

| ID | Titel | Status | Beauftragter | Fälligkeit | Notizen |
|----|-------|--------|-------------|-----------|---------|
| T001 | Venue-Recherche | ✅ completed | Max | 2026-04-30 | Fertig |
| T002 | Angebote einholen | ⏳ in_progress | Sandra | 2026-05-10 | 3/5 Angebote |
| T003 | Vertrag verhandeln | 🔲 pending | Max | 2026-05-20 | Wartet auf T002 |
```

### 3. **research-YYYYMMDD-HHMMSS.md** (Recherche-Ergebnisse)

Dokumentiert gesammelte Recherche-Resultate mit Quellen.

```markdown
# Recherche: [Thema]

**Datum:** 2026-04-14 10:30:00

## Zusammenfassung

Kurze Zusammenfassung der Recherche (2-3 Sätze).

## Quellen

| # | Quelle | Titel | Relevanz | Notizen |
|---|--------|-------|----------|---------|
| 1 | https://... | ... | ⭐⭐⭐⭐ | Sehr relevant |
| 2 | ... | ... | ⭐⭐⭐ | Teilweise relevant |

## Erkenntnisse

- **Punkt 1:** Beschreibung
- **Punkt 2:** Beschreibung
```

### 4. **decision-YYYYMMDD-HHMMSS.md** (Entscheidungen)

Dokumentiert wichtige Entscheidungen mit Optionen und Begründung.

```markdown
# Entscheidung: [Entscheidungstitel]

**Datum:** 2026-04-14 10:30:00
**Beteiligte:** Max, Sandra, Michael

## Optionen

1. Option A – Beschreibung
2. Option B – Beschreibung
3. ✅ **[GEWÄHLT]** Option C – Beschreibung

## Begründung

Warum wurde diese Option gewählt?
- Pro: ...
- Pro: ...
```

### 5. **action-plan-YYYYMMDD-HHMMSS.md** (Aktionspläne)

Detaillierter Aktionsplan mit Maßnahmen, Owner und Fristen.

```markdown
# Aktionsplan: [Titel]

**Erstellt:** 2026-04-14 10:30:00
**Timeline:** 2026-05-01 bis 2026-06-30

## Maßnahmen

### 1. Venue-Recherche
- **Verantwortlich:** Max
- **Start:** 2026-04-15
- **Ende:** 2026-05-01
- **Beschreibung:** Recherchiere die Top-5-Venues in München
- **Dependencies:** Keine

### 2. Angebote einholen
- **Verantwortlich:** Sandra
- **Start:** 2026-05-02
- **Ende:** 2026-05-15
- **Beschreibung:** Stelle Anfragen bei allen 5 Venues
- **Dependencies:** Maßnahme 1
```

### 6. **status-YYYYMMDD-HHMMSS.md** (Statusbericht)

Aktueller Status eines Workstreams mit Fortschritt, Blockaden und nächsten Schritten.

```markdown
# Status-Report: [Workstream-Name]

**Datum:** 2026-04-14 10:30:00
**Status:** 🟢 on_track

## ✅ Abgeschlossen

- Venue-Recherche durchgeführt
- Top-5-Venues identifiziert

## ⏳ In Bearbeitung

- Angebote von Venues einholen
- Budget-Abgleich

## 🚫 Blockiert

- Catering-Partner fehlt (Abhängigkeit: Venue-Entscheidung)

## ⚠️ Risiken

- **Halle XY belegt** (Likelihood: medium)  
  Mitigation: Ausweichort bereithaben

## ➡️ Nächste Schritte

1. Bis 2026-04-20: Alle Angebote sammeln
2. Bis 2026-04-25: Entscheidung treffen
3. Bis 2026-04-30: Vertrag unterzeichnen
```

---

## 🚀 Wie die Terminal-CLI arbeitet

### Installation

```bash
pip install -r requirements.txt
```

### Starten

```bash
# Standard-Modus
python -m src.cli

# Mit Optionen
python -m src.cli --auto --provider ollama --model llama3.2
```

### Ausgaben

Die CLI erstellt automatisch:
1. `workstreams/PLANUNGSLOG.md` – Wird aktualisiert
2. `workstreams/[workstream]/TASKS.md` – Pro Workstream
3. `workstreams/[workstream]/research-*.md` – Recherche-Ergebnisse
4. `workstreams/[workstream]/decision-*.md` – Entscheidungen
5. `workstreams/[workstream]/status-*.md` – Status-Updates

---

## ✏️ Manuelle Ergänzungen

Du kannst Markdown-Dateien jederzeit manuell ergänzen:

1. Öffne die entsprechende `.md`-Datei
2. Bearbeite unter dem entsprechenden Abschnitt (z.B. `## Erkenntnisse`)
3. Speichere die Datei – Git verfolgt die Änderung
4. Commit mit aussagekräftiger Nachricht:
   ```bash
   git add workstreams/programm/research-*.md
   git commit -m "Recherche: Top-5-Speaker identifiziert"
   ```

---

## 📊 Richtlinien für Markdown

### Formatierung

- **Fett:** `**Text**`
- *Kursiv:* `*Text*`
- `Code:` `` `code` ``
- Listen: `-` oder `*`
- Tabellen: `| Column |`

### Emoji-Konventionen

| Icon | Bedeutung |
|------|-----------|
| ✅ | Abgeschlossen |
| ⏳ | In Bearbeitung |
| 🔲 | Ausstehend |
| 🚫 | Blockiert |
| ❌ | Fehler |
| ⚠️ | Warnung/Risiko |
| 🟢 | On Track |
| 🟡 | At Risk |
| 🔴 | Off Track |

### Datum-Format

ISO-Format: `YYYY-MM-DD HH:MM:SS`

---

## 🔄 Workflow-Beispiel

1. **Agent erstellt Research-Log:**
   ```
   workstreams/venue-logistik/research-20260414-103000.md
   ```

2. **Du ergänzt manuell:**
   ```markdown
   ## Erkenntnisse (USER-ADDED)
   
   - Halle XY ist ideal für 500 Personen
   - Budget: 50.000 EUR (inkl. Setup)
   ```

3. **Agent erstellt Decision-Log:**
   ```
   workstreams/venue-logistik/decision-20260415-140000.md
   ```

4. **Agent aktualisiert PLANUNGSLOG.md:**
   ```
   ## 📝 Entscheidungslog
   
   - **[2026-04-15 14:00] Venue-Auswahl**  
     Gewählt: Halle XY, 50.000 EUR
   ```

5. **Agent erstellt Action-Plan:**
   ```
   workstreams/venue-logistik/action-plan-20260415-150000.md
   ```

---

## 🛑 Importantе Regeln

1. **Keine JSON-Dateien** – Alles ist Markdown
2. **Zeitstempel bei Änderungen** – Datum/Uhrzeit bei neuen Dateien
3. **Strukturierte Tabellen** – Für übersichtliche Darstellung
4. **Eindeutige Dateinamen** – Format: `[type]-YYYYMMDD-HHMMSS.md`
5. **Git-tracking** – Alle `.md`-Dateien werden versioniert

---

## ❓ FAQ

**F: Kann ich JSON verwenden?**  
A: **Nein.** Das System ist auf Markdown normalisiert. JSON widerspricht dem Prinzip der Lesbarkeit.

**F: Wie migriere ich alte JSON-Dateien?**  
A: Sie sind automatisch in Markdown konvertiert worden. JSON-Files im gitignore können gelöscht werden.

**F: Kann ich die Struktur ändern?**  
A: Ja – passe die Markdown-Formate an, aber halte die Konvention bei und dokumentiere Changes in README.

**F: Wie behalte ich den Überblick?**  
A: Nutze `workstreams/PLANUNGSLOG.md` als Navigationshub. Alle wichtigen Entscheidungen landen dort.

---

*Dokumentation gültig ab: April 2026*
