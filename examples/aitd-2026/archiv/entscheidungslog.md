# Entscheidungslog: AI Transparency Days 2026

Dieses Dokument hält alle wichtigen Entscheidungen fest: was entschieden wurde, wer es entschieden hat und warum.

---

## Format

```
### [DATUM] [THEMA]
**Entscheidung:** [Was wurde entschieden?]
**Entscheider:** [Wer hat entschieden?]
**Begründung:** [Warum diese Entscheidung?]
**Alternativen:** [Was wurde verworfen und warum?]
**Auswirkungen:** [Welche Workstreams sind betroffen?]
```

---

## Entscheidungen

### 2026-03-30 Automatisierte Planung: Orchestrator-Workflow eingeführt
**Entscheidung:** Neues Orchestrator-System eingeführt (`QUICKSTART.md`, `.claude/agents/orchestrator.md`, `CONFIRM.md`). Ziel: Automatische Generierung aller Planungsartefakte aus `config/event.yaml` – minimaler menschlicher Input.
**Entscheider:** Copilot Agent (basierend auf Problem Statement)
**Begründung:** Problem Statement fordert, dass der Mensch nur Event-Details eingibt und die Agenten den Rest erledigen. Ohne Orchestrator war jeder Workstream isoliert und erforderte manuelle Koordination.
**Alternativen:** Manuelle Koordination der einzelnen Agenten (verworfen: zu hoher Aufwand für Menschen).
**Auswirkungen:** Alle Workstreams. Neuer Einstiegspunkt: `QUICKSTART.md`.

---

### 2026-03-30 Track-Konzept: 3 parallele Tracks
**Entscheidung:** 3 parallele Tracks: (1) AI Transparency & Explainability, (2) AI Safety & Governance, (3) AI in Practice.
**Entscheider:** Programm-Agent (basierend auf `config/event.yaml` topics)
**Begründung:** Topics in event.yaml sind AI Transparency, AI Safety, AI Governance, Human Compatible AI. Drei Tracks decken diese Bereiche sinnvoll ab und passen zur Zielgruppe (Forschende, Praktiker, Policymaker).
**Alternativen:** 2 Tracks (zu wenig Differenzierung), 4 Tracks (zu viele für 125 Personen).
**Auswirkungen:** Programm, Venue (Raumbedarf), Kommunikation (Track-Beschreibungen).

---

### 2026-03-30 Venue-Empfehlung: TH Nürnberg als erste Priorität
**Entscheidung:** TH Nürnberg als bevorzugte Venue empfohlen (Score 4,4/5 in Bewertungsmatrix). CPH Nürnberg als zweite Option.
**Entscheider:** Operations-Agent (basierend auf Anforderungsmatrix)
**Begründung:** Beste Kombination aus Preis-Leistung, akademischer Atmosphäre (passend für Forschungskonferenz) und ÖPNV-Anbindung. Kooperationspotenzial mit Hochschule (COAI-Verbindungen).
**Alternativen:** NCC Ost Messe (teurer, weniger persönlich), Tagungshotel (All-in-One aber teurer, unpersönlicher).
**Auswirkungen:** Venue, Catering, Technik (Venue-eigene Ausstattung), Unterkunft (Nähe Hotels).

---

### 2026-03-30 Budget-Rahmen: Realistisches Szenario ~46.000 €
**Entscheidung:** Realistisches Ausgaben-Budget von ca. 46.675 € kalkuliert. Förderantrag (BMBF/Bayern) wird empfohlen um Finanzierungslücke zu schließen.
**Entscheider:** Koordinations-Agent (basierend auf Branchenstandards für 125 Personen, 3 Tage)
**Begründung:** Venue + Catering sind die größten Kostenpositionen. Ohne Förderung ist das Event nur kostendeckend bei Kombination aus gutem Sponsoring und günstiger Venue.
**Alternativen:** Kleineres Budget durch Venue-Hochschule und reduziertes Catering (möglich aber Einschränkungen); höheres Budget durch professionellere Venue (nicht empfohlen für diese Größe).
**Auswirkungen:** Alle Workstreams (Budget-Allokation), Sponsoring (Ziele), Ticketpreise.

---

### 2026-03-30 Repository-Struktur
**Entscheidung:** Repository nach Workstream-Struktur organisiert (10 Workstreams, 5 Agenten-Rollen).
**Entscheider:** Team / Copilot Agent (initiales Setup)
**Begründung:** Entspricht der Struktur aus den Task Requirements; ermöglicht klare Verantwortlichkeiten und einfaches Navigieren.
**Alternativen:** Flat-Struktur ohne Workstreams (verworfen: zu unübersichtlich bei 10 Bereichen).
**Auswirkungen:** Alle Workstreams.

---

*Neue Einträge oben einfügen (neueste zuerst).*
