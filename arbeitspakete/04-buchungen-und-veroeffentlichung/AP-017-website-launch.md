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

## Eingaben (Inputs)
- `workstreams/kommunikation/kommunikationsstrategie.md` – CI/CD, Tonalität, Sprachen
- `workstreams/teilnehmer/registrierungs-konzept.md` – Registrierungs-Tool und -Link
- `config/event.yaml` – Event-Basisdaten

## Aufgaben (Checkliste)
- [ ] Website-Plattform auswählen (WordPress, Hugo, Webflow – DSGVO-konform, Cookie-Banner)
- [ ] Domain sichern (aitd2026.de oder ähnlich, koordiniere mit COAI)
- [ ] Pflichtseiten erstellen: Startseite, Über das Event, Programm (Platzhalter), Registrierung, Venue/Anreise, Sponsoren, Kontakt, Impressum, Datenschutzerklärung
- [ ] CI/CD anwenden: Farben, Schriften, Logo (AITD 2026 + COAI gGmbH)
- [ ] Cookie-Banner und Datenschutzerklärung (DSGVO) korrekt einrichten
- [ ] Website auf mobilen Geräten testen
- [ ] SEO-Grundlagen: Page-Titel, Meta-Descriptions, Keywords (AI Transparency Days, Nürnberg 2026)
- [ ] Launch-Datum: 30.04.2026 (zusammen mit den ersten öffentlichen Ankündigungen)
- [ ] Website-URL in `workstreams/kommunikation/website-launch.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/kommunikation/website-launch.md` – Dokumentation des Website-Launches (URL, Struktur, CMS-Zugangsdaten-Speicherort)

## Hinweise für den Agenten
- Die Website sollte zum gleichen Zeitpunkt wie die ersten Speaker-Ankündigungen live gehen (30.04.2026).
- Achte auf DSGVO-Konformität: Kein Google Analytics ohne Einwilligung, Cookie-Banner, korrekte Datenschutzerklärung.
- Plane schon jetzt Platzhalter für Inhalte, die noch folgen: Programm, Speaker, Sponsoren – kein „Coming Soon" ohne Zeitangabe.
