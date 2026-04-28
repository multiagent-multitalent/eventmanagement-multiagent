User: erstelle eine anleitung für das Programm

GitHub Copilot: Optimizing tool selection...Ich erstelle dir eine konkrete Bedienungsanleitung für das Programm und prüfe dafür zuerst kurz, wie es aktuell gestartet wird und welche Komponenten es hat, damit die Anleitung exakt zum Repository passt.

Read [](file:///c%3A/Git/eventmanagement-multiagent/src/main.py#1-1), lines 1 to 260

Read [](file:///c%3A/Git/eventmanagement-multiagent/requirements.txt)

Read [](file:///c%3A/Git/eventmanagement-multiagent/streamlit_app.py)

Read [](file:///c%3A/Git/eventmanagement-multiagent/README.md)

Read [](file:///c%3A/Git/eventmanagement-multiagent/QUICKSTART.md)

Ich habe die Startpunkte geprüft; als Nächstes schaue ich auf die Konfiguration und LLM-Umgebungsvariablen, damit die Anleitung auch die Einrichtung korrekt abdeckt.

Read [](file:///c%3A/Git/eventmanagement-multiagent/src/config.py)

Read [](file:///c%3A/Git/eventmanagement-multiagent/src/llm.py#1-1), lines 1 to 320

Read [](file:///c%3A/Git/eventmanagement-multiagent/config/event.yaml)

Read [](file:///c%3A/Git/eventmanagement-multiagent/config/team.yaml)

Ich habe jetzt die technischen Parameter; als letzten Kontext lese ich die Streamlit-Oberfläche an, damit die Anleitung auch die tatsächlichen Bedien-Schritte in der App beschreibt.

Read [](file:///c%3A/Git/eventmanagement-multiagent/src/dashboard/app.py#1-1), lines 1 to 360

Read [](file:///c%3A/Git/eventmanagement-multiagent/src/workflows/event_planning_graph.py)

Als nächsten Schritt lege ich eine neue, vollständige Anleitung als eigene Datei an und verlinke sie im Haupt-README, damit sie direkt auffindbar ist.

Generating patch (164 lines) in [](file:///c%3A/Git/eventmanagement-multiagent/README.md), [](file:///c%3A/Git/eventmanagement-multiagent/ANLEITUNG.md)


```

```

```

```
Die Anleitung ist angelegt und im README verlinkt; ich prüfe jetzt noch kurz auf mögliche Format- oder Syntaxprobleme in den geänderten Dateien.

Checked [](file:///c%3A/Git/eventmanagement-multiagent/ANLEITUNG.md), [](file:///c%3A/Git/eventmanagement-multiagent/README.md), no problems found

Eine vollständige Programmanleitung wurde erstellt und direkt im Einstieg verlinkt.

Geändert:
1. Neue Anleitung: ANLEITUNG.md
2. Startpunkt ergänzt in: README.md

Inhalt der Anleitung:
1. Ziel und Ablauf von Stage 1/Stage 2
2. Voraussetzungen und Installation (venv/Conda)
3. Konfiguration über event.yaml und team.yaml
4. LLM-Setup über Umgebungsvariablen
5. Start über Streamlit und CLI (inkl. Parameterbeispiele)
6. Ausgabeorte in den Workstreams
7. Smoke-Test
8. Troubleshooting und empfohlener Standardablauf

Wenn du möchtest, kann ich als Nächstes noch eine kurze “Schnellreferenz” (1-Seite) für dein Team ergänzen, z. B. als README.md-Abschnitt.

Made changes.