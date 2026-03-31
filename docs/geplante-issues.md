# Geplante Issues und Subtasks – AI Transparency Days 2026

Dieses Dokument listet alle geplanten GitHub-Issues und Subtasks für die AITD 2026-Planung.
Es dient als Grundlage für die Erstellung von Issues im GitHub-Projekt.

---

## Übersicht

| # | Titel | Workstream | Phase | Priorität |
|---|---|---|---|---|
| 1 | Repository- und Agenten-Setup | Übergreifend | Phase 1 | 🔴 Hoch |
| 2 | Event-Konzept und Konfiguration | Übergreifend | Phase 1 | 🔴 Hoch |
| 3 | Venue-Recherche und -Buchung | Venue & Logistik | Phase 2 | 🔴 Hoch |
| 4 | Track-Konzept und Speaker-Kuration | Programm | Phase 2 | 🔴 Hoch |
| 5 | Kommunikationsplan und Content-Kalender | Kommunikation | Phase 2 | 🔴 Hoch |
| 6 | Budget-Rahmen und Sponsoring-Konzept | Sponsoring | Phase 2 | 🔴 Hoch |
| 7 | Registrierungssystem einrichten | Teilnehmer | Phase 2/3 | 🟡 Mittel |
| 8 | Technik-Anforderungen und -Beschaffung | Technik | Phase 2/3 | 🟡 Mittel |
| 9 | Catering-Konzept und -Beauftragung | Catering | Phase 2/3 | 🟡 Mittel |
| 10 | Speaker-Zusagen einholen und Programm finalisieren | Programm | Phase 3 | 🔴 Hoch |
| 11 | Speaker-Management | Programm | Phase 3 | 🔴 Hoch |
| 12 | Social-Media- und Newsletter-Kampagnen | Kommunikation | Phase 3 | 🟡 Mittel |
| 13 | Helfer-Rekrutierung und Schichtplanung | Personal | Phase 3 | 🟡 Mittel |
| 14 | Hotelkontingente und Anreiseinformationen | Unterkunft & Anreise | Phase 3 | 🟢 Niedrig |
| 15 | On-Site-Koordination und Durchführung | Übergreifend | Phase 4 | 🔴 Hoch |
| 16 | Feedback-Auswertung und Abschlussbericht | Nachbereitung | Phase 5 | 🟡 Mittel |
| 17 | Lessons Learned und Repository-Cleanup | Nachbereitung | Phase 5 | 🟡 Mittel |
| 18 | Reflexionsbericht (Forschung) | Übergreifend | Phase 5 | 🟡 Mittel |

---

## Detaillierte Issue-Beschreibungen

---

### Issue 1: Repository- und Agenten-Setup

**Titel:** Repository- und Agenten-Setup finalisieren

**Phase:** Phase 1 – Initialisierung  
**Priorität:** 🔴 Hoch  
**Agent:** Koordination

**Beschreibung:**
Das Repository ist die zentrale Arbeitsgrundlage. Alle Konfigurationen müssen für den Projektstart bereit sein.

**Aufgaben:**
- [ ] `config/team.yaml` mit echten Team-Mitgliedern ausfüllen
- [ ] Agenten-Konfigurationen auf Team-Workflow anpassen
- [ ] GitHub-Projekt/Kanban-Board einrichten
- [ ] Meilensteine in GitHub erstellen
- [ ] Alle Team-Mitglieder als Repository-Contributor hinzufügen
- [ ] Arbeitsweise mit Agenten im Team besprechen und festlegen

**Ressourcen:** `config/`, `docs/rollen.md`, `CLAUDE.md`

---

### Issue 2: Event-Konzept und Konfiguration

**Titel:** Event-Konzept finalisieren und Konfiguration ausfüllen

**Phase:** Phase 1 – Initialisierung  
**Priorität:** 🔴 Hoch  
**Agent:** Koordination

**Beschreibung:**
Bevor die operative Planung beginnt, müssen die Grundentscheidungen zum Event getroffen werden.

**Aufgaben:**
- [ ] Genaues Datum festlegen (Vorschlag: 14.–16. Oktober 2026 – bestätigen oder anpassen)
- [ ] Event-Format entscheiden: Präsenz / Hybrid / Streaming?
- [ ] Anzahl der Tracks entscheiden (2 oder 3 parallele Tracks?)
- [ ] Thematische Schwerpunkte der Tracks grob festlegen
- [ ] `config/event.yaml` mit finalen Werten aktualisieren
- [ ] Budget-Rahmen grob abstecken

**Ressourcen:** `config/event.yaml`, `docs/phasenmodell.md`

---

### Issue 3: Venue-Recherche und -Buchung

**Titel:** Venue für AITD 2026 recherchieren und buchen

**Phase:** Phase 2 – Planung  
**Priorität:** 🔴 Hoch  
**Agent:** Operations

**Beschreibung:**
Die Venue ist eine der kritischsten Entscheidungen – sie beeinflusst fast alle anderen Workstreams. Frühzeitig starten.

**Aufgaben:**
- [ ] Venue-Anforderungen definieren (aus `templates/venue-logistik/venue-anforderungen.md`)
- [ ] Potenzielle Locations im Raum Nürnberg/Franken recherchieren
- [ ] Mindestens 3 Optionen identifizieren
- [ ] Besichtigungstermine vereinbaren
- [ ] Angebote einholen und vergleichen (Bewertungsmatrix nutzen)
- [ ] Venue-Entscheidung treffen und buchen
- [ ] Raumplan erstellen

**Kriterien:**
- Hauptsaal für 150 Personen
- 2–3 Parallel-Tracks (je 60–80 Personen)
- Workshop-Räume (je 25–30 Personen)
- Gute ÖPNV-Anbindung in Nürnberg
- WLAN für 150+ Geräte

**Deadline:** Mai 2026 (Venues sind oft 6+ Monate im Voraus ausgebucht)

**Ressourcen:** `workstreams/venue-logistik/`, `templates/venue-logistik/venue-anforderungen.md`

---

### Issue 4: Track-Konzept und Speaker-Kuration

**Titel:** Programm-Konzept entwickeln und Speaker einladen

**Phase:** Phase 2 – Planung  
**Priorität:** 🔴 Hoch  
**Agent:** Programm

**Beschreibung:**
Das Programm ist das Herzstück des Events. Da die AI Transparency Days keinen Call for Papers haben, werden Speaker gezielt eingeladen und kuratiert.

**Aufgaben:**
- [ ] Track-Konzept entwickeln (Themen, Formate, Zielgruppen)
- [ ] Keynote-Themen und mögliche Keynote-Speaker identifizieren
- [ ] Speaker-Shortlist pro Track erstellen
- [ ] Einladungs-E-Mails vorbereiten (DE + EN)
- [ ] Speaker-Einladungen versenden
- [ ] Speaker-Zusagen verfolgen und dokumentieren

**Deadline:** Speaker-Einladungen Ende April 2026

**Ressourcen:** `workstreams/programm/`, `templates/programm/`

---

### Issue 5: Kommunikationsplan und Content-Kalender

**Titel:** Kommunikationsplan und Content-Kalender erstellen

**Phase:** Phase 2 – Planung  
**Priorität:** 🔴 Hoch  
**Agent:** Kommunikation

**Beschreibung:**
Ohne strukturierte Kommunikation werden Event-Ankündigungen zu wenig Menschen erreichen. Früh planen, früh starten.

**Aufgaben:**
- [ ] Kommunikationsstrategie und Kernbotschaften definieren
- [ ] Zielgruppen-Kanäle festlegen
- [ ] Kommunikationsplan erstellen
- [ ] Content-Kalender aufbauen (Vorlage: `templates/kommunikation/content-kalender.md`)
- [ ] Social-Media-Kanäle prüfen und ggf. einrichten
- [ ] Erste Inhalte erstellen: Save-the-Date-Posts, Event-Ankündigung

**Ressourcen:** `workstreams/kommunikation/`, `templates/kommunikation/`

---

### Issue 6: Budget-Rahmen und Sponsoring-Konzept

**Titel:** Budget definieren und Sponsoring-Konzept entwickeln

**Phase:** Phase 2 – Planung  
**Priorität:** 🔴 Hoch  
**Agent:** Koordination

**Beschreibung:**
Ohne Budget-Rahmen können keine Entscheidungen über Venue, Catering und Technik getroffen werden.

**Aufgaben:**
- [ ] Kostenschätzungen für alle Workstreams sammeln
- [ ] Budget-Plan erstellen (Einnahmen und Ausgaben)
- [ ] Sponsoring-Konzept entwickeln (Pakete, Gegenleistungen)
- [ ] Potenzielle Sponsoren recherchieren
- [ ] Ticket-Preise festlegen

**Ressourcen:** `workstreams/sponsoring/`

---

### Issue 7: Registrierungssystem einrichten

**Titel:** Registrierungssystem auswählen und einrichten

**Phase:** Phase 2/3  
**Priorität:** 🟡 Mittel  
**Agent:** Operations

**Beschreibung:**
Für 100–150 Teilnehmer braucht es ein professionelles Registrierungssystem.

**Aufgaben:**
- [ ] Anforderungen definieren (Ticket-Kategorien, Bezahlmethoden, Datenfelder)
- [ ] Systemoptionen vergleichen (z. B. Pretix, Eventbrite, Ti.to)
- [ ] System auswählen und einrichten
- [ ] Registrierungsseite testen
- [ ] Registrierung öffnen (Ziel: Mai 2026)
- [ ] Bestätigungsmails und Reminders einrichten

**Ressourcen:** `workstreams/teilnehmer/`

---

### Issue 8: Technik-Anforderungen und -Beschaffung

**Titel:** Technik-Anforderungen spezifizieren und Equipment beschaffen

**Phase:** Phase 2/3  
**Priorität:** 🟡 Mittel  
**Agent:** Operations

**Beschreibung:**
AV-Equipment, WLAN und Streaming müssen frühzeitig geplant werden.

**Aufgaben:**
- [ ] AV-Anforderungen pro Raum spezifizieren
- [ ] WiFi-Kapazität prüfen (mit Venue)
- [ ] Streaming-Entscheidung: ja/nein/hybrid
- [ ] Hackathon-Infrastruktur definieren
- [ ] Vorhandene Venue-Infrastruktur dokumentieren
- [ ] Fehlende Technik beschaffen oder mieten

**Ressourcen:** `workstreams/technik/`

---

### Issue 9: Catering-Konzept und -Beauftragung

**Titel:** Catering planen und Anbieter beauftragen

**Phase:** Phase 2/3  
**Priorität:** 🟡 Mittel  
**Agent:** Operations

**Beschreibung:**
Gutes Catering ist entscheidend für die Teilnehmer-Erfahrung und Networking-Möglichkeiten.

**Aufgaben:**
- [ ] Catering-Konzept entwickeln (Mahlzeiten, Snacks, Abendprogramm)
- [ ] Dietary-Requirements-Abfrage in Registrierung einbauen
- [ ] Catering-Anbieter recherchieren
- [ ] Angebote einholen und Anbieter auswählen
- [ ] Abendprogramm (Social Dinner / Networking) planen
- [ ] Catering beauftragen

**Ressourcen:** `workstreams/catering/`

---

### Issue 10: Speaker-Zusagen einholen und Programm finalisieren

**Titel:** Speaker-Zusagen einholen und Programm aufstellen

**Phase:** Phase 3 – Umsetzung  
**Priorität:** 🔴 Hoch  
**Agent:** Programm

**Beschreibung:**
Nach dem Versand der Einladungen müssen Speaker-Zusagen eingeholt und die finale Agenda aufgestellt werden.

**Aufgaben:**
- [ ] Speaker-Zusagen nachverfolgen und dokumentieren
- [ ] Programm-Meeting: Agenda-Entscheidungen treffen
- [ ] Absagen kommunizieren und ggf. Ersatz einladen
- [ ] Agenda aufbauen (Räume, Slots, Pausen)
- [ ] Agenda auf Website veröffentlichen

**Abhängigkeit:** Nach Speaker-Einladungen (April 2026)

**Ressourcen:** `workstreams/programm/`

---

### Issue 11: Speaker-Management

**Titel:** Speaker managen: Briefings, Reise und On-Site-Betreuung

**Phase:** Phase 3 – Umsetzung  
**Priorität:** 🔴 Hoch  
**Agent:** Programm

**Beschreibung:**
Speaker brauchen klare Informationen und persönliche Betreuung.

**Aufgaben:**
- [ ] Speaker-Briefing-Template ausfüllen (Vorlage: `templates/programm/speaker-briefing.md`)
- [ ] Briefings an alle Speaker senden
- [ ] Reise- und Unterkunfts-Anfragen beantworten
- [ ] Präsentationen einsammeln (Deadline 1 Woche vorher)
- [ ] Technik-Check mit Speakern klären
- [ ] On-Site-Betreuung organisieren

**Ressourcen:** `workstreams/programm/`, `templates/programm/speaker-briefing.md`

---

### Issue 12: Social-Media- und Newsletter-Kampagnen

**Titel:** Kommunikations-Kampagnen umsetzen (Social Media, Newsletter, Presse)

**Phase:** Phase 3 – Umsetzung  
**Priorität:** 🟡 Mittel  
**Agent:** Kommunikation

**Beschreibung:**
Laufende Kommunikation gemäß Content-Kalender umsetzen.

**Aufgaben:**
- [ ] Social-Media-Beiträge nach Content-Kalender erstellen und posten
- [ ] Newsletter-Kampagnen erstellen und versenden
- [ ] Pressemitteilung zum Event-Launch versenden
- [ ] Speaker-Ankündigungen veröffentlichen
- [ ] Reminder-Kampagne für Registrierung
- [ ] Programm-Veröffentlichung kommunizieren

**Ressourcen:** `workstreams/kommunikation/`, `templates/kommunikation/`

---

### Issue 13: Helfer-Rekrutierung und Schichtplanung

**Titel:** Helfer rekrutieren und Schichtplan erstellen

**Phase:** Phase 3 – Umsetzung  
**Priorität:** 🟡 Mittel  
**Agent:** Koordination

**Beschreibung:**
Für ein 2–3-tägiges Event mit 100–150 Teilnehmern braucht man ca. 12–16 Helfer.

**Aufgaben:**
- [ ] Helferbedarf pro Bereich ermitteln
- [ ] Helfer-Ausschreibung erstellen
- [ ] Helfer rekrutieren
- [ ] Aufgabenbeschreibungen erstellen
- [ ] Schichtplan aufstellen
- [ ] Helfer-Briefing vorbereiten

**Ressourcen:** `workstreams/personal/`

---

### Issue 14: Hotelkontingente und Anreiseinformationen

**Titel:** Unterkunfts-Kontingente aushandeln und Anreiseinformationen aufbereiten

**Phase:** Phase 3 – Umsetzung  
**Priorität:** 🟢 Niedrig  
**Agent:** Kommunikation

**Beschreibung:**
Besonders für Teilnehmer von außerhalb Nürnbergs sind Unterkunfts- und Anreiseinfos wichtig.

**Aufgaben:**
- [ ] Hotels in Venue-Nähe recherchieren (verschiedene Preiskategorien)
- [ ] Kontingente bei 2–3 Hotels anfragen
- [ ] Anreiseinformationen zusammenstellen (Bahn, Flug, Auto, ÖPNV)
- [ ] Info-Seite auf Website erstellen
- [ ] Infos in Teilnehmer-Kommunikation einbauen

**Ressourcen:** `workstreams/unterkunft-anreise/`

---

### Issue 15: On-Site-Koordination und Durchführung

**Titel:** Event-Durchführung vorbereiten und koordinieren

**Phase:** Phase 4 – Durchführung  
**Priorität:** 🔴 Hoch  
**Agent:** Koordination + Operations

**Beschreibung:**
Die operative Vorbereitung für die Event-Tage: Aufbau, Check-In, Koordination.

**Aufgaben:**
- [ ] Aufbau-Zeitplan erstellen
- [ ] Check-In-Prozess finalisieren
- [ ] Notfall-Kontaktliste erstellen
- [ ] Alle Helfer briefen
- [ ] Aufbau durchführen
- [ ] Check-In managen
- [ ] Event-Koordination on-site
- [ ] Abbau koordinieren

**Ressourcen:** `workstreams/venue-logistik/`, `workstreams/personal/`

---

### Issue 16: Feedback-Auswertung und Abschlussbericht

**Titel:** Feedback auswerten und Abschlussbericht erstellen

**Phase:** Phase 5 – Nachbereitung  
**Priorität:** 🟡 Mittel  
**Agent:** Dokumentation

**Beschreibung:**
Nach dem Event die Ergebnisse dokumentieren und für zukünftige Events aufbereiten.

**Aufgaben:**
- [ ] Feedback-Survey erstellen und versenden (Vorlage: `templates/nachbereitung/feedback-survey.md`)
- [ ] Survey-Ergebnisse auswerten
- [ ] Session-Materialien (Slides, Videos) sammeln und veröffentlichen
- [ ] Abschlussbericht erstellen
- [ ] Dankes-Kommunikation an Teilnehmer, Speaker, Sponsoren, Helfer

**Ressourcen:** `workstreams/nachbereitung/`, `templates/nachbereitung/`

---

### Issue 17: Lessons Learned und Repository-Cleanup

**Titel:** Lessons Learned dokumentieren und Repository als Template aufräumen

**Phase:** Phase 5 – Nachbereitung  
**Priorität:** 🟡 Mittel  
**Agent:** Dokumentation

**Beschreibung:**
Das Repository soll für zukünftige Events wiederverwendbar sein.

**Aufgaben:**
- [ ] Lessons Learned aus allen Phasen zusammentragen (`archiv/lessons-learned.md`)
- [ ] Entscheidungslog finalisieren (`archiv/entscheidungslog.md`)
- [ ] Repository aufräumen (event-spezifische Daten vs. Templates trennen)
- [ ] Konfigurationsdateien auf Platzhalter zurücksetzen
- [ ] README und CLAUDE.md für nächstes Event aktualisieren

**Ressourcen:** `archiv/`, `CLAUDE.md`

---

### Issue 18: Reflexionsbericht (Forschung)

**Titel:** Reflexionsbericht zur Mensch-KI-Zusammenarbeit erstellen

**Phase:** Phase 5 – Nachbereitung  
**Priorität:** 🟡 Mittel  
**Agent:** Dokumentation

**Beschreibung:**
Steffen Höpfner forscht zur Mensch-KI-Zusammenarbeit. Das Team erstellt einen anonymisierten Reflexionsbericht.

**Aufgaben:**
- [ ] Reflexionsfragen aus `archiv/lessons-learned.md` beantworten
- [ ] Erkenntnisse zur Agenten-Nutzung zusammenfassen
- [ ] Reflexionsbericht verfassen (anonymisiert)
- [ ] Bericht an Steffen Höpfner übergeben

**Reflexionsfragen (laut Task Requirements):**
- Was lief gut? Was war schwierig?
- Wie habt ihr euch organisiert?
- Was würdet ihr anders machen?
- Wo war menschliches Urteil unverzichtbar?

**Ressourcen:** `archiv/lessons-learned.md`, `docs/rollen.md`

---

## Abhängigkeiten zwischen Issues

```
Issue 2 (Event-Konzept) → Issue 3 (Venue), Issue 4 (Speaker-Kuration), Issue 6 (Budget)
Issue 3 (Venue) → Issue 8 (Technik), Issue 9 (Catering), Issue 14 (Unterkunft)
Issue 4 (Speaker-Kuration) → Issue 5 (Kommunikation), Issue 10 (Speaker-Zusagen)
Issue 6 (Budget) → alle kostenrelevanten Issues
Issue 7 (Registrierung) → Issue 13 (Helfer: Check-In)
Issue 10 (Speaker-Zusagen) → Issue 11 (Speaker-Management), Issue 12 (Kommunikation: Programm)
Issues 3–14 → Issue 15 (Durchführung)
Issue 15 (Durchführung) → Issues 16–18 (Nachbereitung)
```

---

*Alle Issues sollten im GitHub-Projekt als Tickets angelegt und den Meilensteinen zugeordnet werden.*
