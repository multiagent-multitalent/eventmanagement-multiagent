# Projekthistorie: Detaillierte Timeline & Analyse

Dieses Dokument dient als Grundlage für den Projektbericht. Es rekonstruiert die Entwicklung des Eventmanagement Multi-Agent Systems von den ersten Versuchen bis zum finalen Architekturstand.

---

## 1. Timeline der Entwicklung

| Datum | Meilenstein / Commit | Bedeutung |
|---|---|---|
| **23.03.2026** | Projektstart | Initiales Repository-Setup. |
| **30.03.2026** | **"Rough Draft" Phase** | Erster Entwurf des Planungsprozesses. Fokus liegt exklusiv auf *AI Transparency Days 2026*. |
| **30.03.2026** | `517b151` - Automated Workflow | Einführung des ersten automatischen Workflows. Dateien wie `PLANUNGSLOG.md` sind noch fest mit AITD-Werten vorbefüllt. |
| **31.03.2026** | **Universal Repository** (`13015ff`) | **Kritischer Wendepunkt:** Verschiebung der AITD-Daten nach `examples/`. Das Repo wird zum universellen Framework. |
| **31.03.2026** | `a4eb03b` - Python Orchestrator | Implementierung des Orchestrators mit LangGraph. Einführung eines echten State-Managements (`src/state.py`). |
| **31.03.2026** | `28ab7b1` - Web-Dashboard | Erstes Streamlit-Interface für den Orchestrator. |
| **14.04.2026** | **Refactoring CLI & Markdown** | Vollständige Entfernung von Streamlit. Umstellung auf Terminal-CLI (Rich) und Markdown-Logging. |
| **Juni 2026** | Dokumentation & Abschluss | Erstellung der System-Erklärungen und finalen Berichte. |

---

## 2. Analyse: Das Persistenz-Problem ("Gedächtnis-Fehler")

### Ursache
In der frühen Phase (vor dem 31. März) arbeiteten die Agenten nach dem Prinzip der "agentischen Dokumentation". Sie nutzten das Dateisystem als Langzeitgedächtnis. 
Da die Ordnerstruktur fest auf ein Event (AITD) zugeschnitten war und die Dateien bereits Inhalte enthielten, "fanden" die Agenten bei jedem Start Informationen vor, die sie fälschlicherweise als Ergebnisse ihrer aktuellen Arbeit interpretierten.

### Symptome
- Agenten schlugen Venues vor, die bereits im Dokument standen, obwohl sie neu suchen sollten.
- Bei Änderungen an der Event-Konfiguration (z.B. Teilnehmerzahl) blieben alte Berechnungen in den Dokumenten erhalten.
- Das System war unfähig, ein zweites, anderes Event im selben Repository zu planen.

### Lösung: Der "Reset & Framework" Ansatz
Die Lösung bestand aus drei Schritten:
1. **Beispieldaten isolieren:** Alles, was mit dem Test-Event zu tun hatte, wurde in `examples/` verschoben.
2. **Template-Logik:** Die aktiven `workstreams/` wurden in leere "Platzhalter" verwandelt, die erst zur Laufzeit befüllt werden.
3. **In-Memory State:** Durch LangGraph wurde ein "State" eingeführt, der während der Laufzeit im RAM existiert. Erst am Ende (oder bei Meilensteinen) wird dieser State in Dateien geschrieben. Dadurch lesen Agenten während der Planung aus einer sauberen Datenstruktur statt aus (evtl. veralteten) Textdateien.

---

## 3. Die Rolle der Benutzeroberfläche

### Von Streamlit zur CLI
Der Wechsel von Streamlit zur Terminal-CLI war keine rein optische Entscheidung:
- **Stabilität:** Streamlit hatte oft Probleme mit dem Session-State (Abstürze bei langen Agenten-Läufen).
- **Agenten-Interaktion:** Im Terminal können Agenten den Output direkter verarbeiten und protokollieren.
- **Protokollierung:** Das neue Markdown-Logging-System ermöglicht es, jeden Schritt der Agenten als permanente Datei zu sichern, was die Transparenz massiv erhöht hat.

---

## 4. Zusammenfassung für den Projektbericht

Der entscheidende Durchbruch des Projekts war die Erkenntnis, dass **KI-Agenten eine saubere Trennung zwischen Konfiguration, State (Laufzeit) und Dokumentation benötigen**. 
Das Persistenz-Problem wurde nicht durch "bessere Prompts" gelöst, sondern durch eine **systemische Architekturänderung**: die Umwandlung eines statischen Dokumenten-Speichers in ein dynamisches Multi-Agenten-Framework.

---
*Erstellt für Jana Mumm zur Vorbereitung des Projektberichts.*
