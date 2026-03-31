# AP-017: Website launchen

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-017 |
| **Workstream** | Kommunikation & Marketing |
| **Agent** | Kommunikation (`.claude/agents/kommunikation.md`) |
| **Phase** | Phase 3: Umsetzung |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 25.04.2026 – 01.05.2026 |
| **Status** | ⬜ Offen |

## Ziel
Die offizielle Event-Website für AITD 2026 aufsetzen und live schalten – als zentrale Informationsquelle für alle Zielgruppen (Teilnehmende, Speaker, Sponsoren, Presse).

## Voraussetzungen (Abhängigkeiten)
- AP-004: Kommunikationsstrategie definieren (CI/CD-Richtlinien)
- AP-008: Registrierungs-Konzept entwickeln (Registrierungs-Tool-Entscheidung)
- AP-010: CfP-Text verfassen (Inhalte für CfP-Seite)

## Eingaben (Inputs)
- `workstreams/kommunikation/kommunikationsstrategie.md` – CI/CD, Tonalität, Sprachen
- `workstreams/programm/cfp-text.md` – CfP-Inhalte
- `workstreams/teilnehmer/registrierungs-konzept.md` – Registrierungs-Tool und -Link
- `config/event.yaml` – Event-Basisdaten

## Aufgaben (Checkliste)
- [ ] Website-Plattform auswählen (WordPress, Hugo, Webflow – DSGVO-konform, Cookie-Banner)
- [ ] Domain sichern (aitd2026.de oder ähnlich, koordiniere mit COAI)
- [ ] Pflichtseiten erstellen: Startseite, Über das Event, Programm (Platzhalter), CfP, Registrierung, Venue/Anreise, Sponsoren, Kontakt, Impressum, Datenschutzerklärung
- [ ] CI/CD anwenden: Farben, Schriften, Logo (AITD 2026 + COAI gGmbH)
- [ ] CfP-Seite mit Link zur Einreichungsplattform aufschalten
- [ ] Cookie-Banner und Datenschutzerklärung (DSGVO) korrekt einrichten
- [ ] Website auf mobilen Geräten testen
- [ ] SEO-Grundlagen: Page-Titel, Meta-Descriptions, Keywords (AI Transparency Days, Nürnberg 2026)
- [ ] Launch-Datum: 30.04.2026 (zusammen mit CfP-Veröffentlichung)
- [ ] Website-URL in `workstreams/kommunikation/website-launch.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/kommunikation/website-launch.md` – Dokumentation des Website-Launches (URL, Struktur, CMS-Zugangsdaten-Speicherort)

## Hinweise für den Agenten
- Die Website muss am gleichen Tag wie der CfP live gehen (30.04.2026) – koordiniere die Launches.
- Achte auf DSGVO-Konformität: Kein Google Analytics ohne Einwilligung, Cookie-Banner, korrekte Datenschutzerklärung.
- Plane schon jetzt Platzhalter für Inhalte, die noch folgen: Programm, Speaker, Sponsoren – kein „Coming Soon" ohne Zeitangabe.
