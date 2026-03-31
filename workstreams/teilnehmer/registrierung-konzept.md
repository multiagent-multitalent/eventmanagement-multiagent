# Registrierungs-Konzept: AI Transparency Days 2026

*Generiert durch: Operations-Agent | Basierend auf: config/event.yaml (125 Teilnehmer)*

---

## Überblick

Das Registrierungssystem muss ca. 125 Teilnehmer in verschiedenen Kategorien verwalten, Ticket-Buchungen abwickeln und Informationen für Catering, Badges und On-Site-Check-In bereitstellen.

---

## Ticket-Kategorien

| Kategorie | Preis | Beschreibung |
|---|---|---|
| Early Bird | 80 € | Bis 30. Juni 2026 |
| Regular | 120 € | Ab 1. Juli 2026 |
| Studierende | 30 € | Mit Immatrikulationsnachweis |
| Speaker | 0 € | Für akzeptierte Speaker |
| Sponsor-Kontingent | 0 € | Je nach Sponsoring-Paket |
| Orga-Team | 0 € | COAI-Mitarbeiter und Helfer |

---

## Registrierungsformular – Pflichtfelder

### Persönliche Daten
- Vorname, Nachname
- E-Mail-Adresse (für Bestätigungsmail und Kommunikation)
- Organisation / Unternehmen / Hochschule
- Position / Rolle
- Land

### Ticket-Auswahl
- Ticket-Kategorie
- Gutscheincode (für Sponsoren-Kontingente, Speaker)

### Event-relevante Angaben
- Ernährungsbedürfnisse: Keine Einschränkung / Vegetarisch / Vegan / Glutenfrei / Laktosefrei / Halal / Koscher / Sonstiges (Freitext)
- Teilnahme Social Dinner (Tag 1)?: Ja / Nein / Vielleicht
- Wie haben Sie von AITD 2026 erfahren?: Newsletter / Social Media / Kolleg:in / Hochschule / Sonstiges

### Optional
- LinkedIn-Profil (für Networking)
- Interesse an Hackathon-Teilnahme?: Ja / Nein
- Soll ich im Teilnehmer-Verzeichnis erscheinen?: Ja / Nein (Datenschutz)

---

## Empfohlene Tools

| Tool | Typ | Kosten | Eignung |
|---|---|---|---|
| **pretix** | Open-Source, selbst hostbar | kostenlos / Hosting-Kosten | ✅ Sehr gut für Konferenzen |
| **Eventbrite** | SaaS | ~3% + 0,75 € pro Ticket | ✅ Einfach, bekannt |
| **Tito** | SaaS | kostenlos bis 1.000 € Einnahmen | ✅ Gut für Tech-Events |
| **Typeform + Stripe** | Formular + Zahlung | Typeform-Abo + Stripe-Gebühren | ⚠️ Mehr Eigenaufwand |
| **Google Forms** | Kostenlos | 0 € | ⚠️ Kein Zahlungs-Handling |

**Empfehlung:** **pretix** (open-source, DSGVO-konform, sehr flexibel) oder **Tito** (einfachste Einrichtung für kleine Events).

---

## Bestätigungs-E-Mail (Vorlage)

```
Betreff: Deine Anmeldung zur AITD 2026 ist bestätigt! ✅

Hallo [Vorname],

herzlich willkommen! Wir freuen uns, dich bei den AI Transparency Days 2026 begrüßen zu dürfen.

📅 Datum: 14.–16. Oktober 2026
📍 Ort: [Venue-Name], Nürnberg
🎫 Dein Ticket: [Ticket-Kategorie]

Deine Buchungsnummer: [NUMMER]
Dein persönlicher QR-Code für den Check-In: [QR-CODE]

Was kommt als Nächstes?
→ Programm: veröffentlicht am 31. Juli 2026 unter [Website]
→ Teilnehmer-Infopaket: erhältst du Anfang Oktober

Bei Fragen: [kontakt@aitd2026.de]

Bis Oktober!
Das AITD-2026-Team
COAI gGmbH
```

---

## Check-In-Prozess (Vor-Ort)

### Setup
- 2–3 Check-In-Stationen (Tablets/Laptops)
- Suche nach Name oder QR-Code-Scan
- Automatischer Badge-Druck (falls Tool unterstützt) oder vorbereitete Badge-Boxes (alphabetisch sortiert)

### Ablauf
1. Teilnehmer kommt an Check-In-Counter
2. QR-Code aus Bestätigungs-E-Mail zeigen ODER Namen nennen
3. Helfer sucht in System, checkt Teilnehmer ein
4. Badge ausgeben
5. Programm-Heft / Welcome-Bag ausgeben (falls vorhanden)
6. Kurze Orientierung: „Track-Räume sind rechts, Hackathon geradeaus, Kaffee links"

---

## Badge-Design

| Element | Inhalt |
|---|---|
| Vorderseite | Name (groß), Organisation, Rolle/Kategorie (Farbkodierung) |
| Rückseite | Programm-Übersicht (QR-Code zur vollständigen Agenda) |
| Farbkodierung | Blau: Regulär; Grün: Speaker; Orange: Orga/Helfer; Lila: Sponsor |
| Material | Recyclingpapier, Lanyard wiederverwendbar |

---

## Zeitplan Registrierung

| Aufgabe | Wann |
|---|---|
| Registrierungstool auswählen | April 2026 |
| Formular einrichten | April 2026 |
| Registrierung öffnen | 1. Mai 2026 |
| Early-Bird-Frist | 30. Juni 2026 |
| Registrierung schließen | 1. Oktober 2026 |
| Teilnehmerliste für Badge-Druck exportieren | 7. Oktober 2026 |
| Badges drucken und sortieren | 10.–12. Oktober 2026 |
| Check-In-System testen | 13. Oktober 2026 |

---

## Datenschutz (DSGVO)

- Datenschutzerklärung auf Anmeldeformular verlinken
- Löschfristen definieren: Daten 12 Monate nach Event löschen
- Drittanbieter prüfen: Tools müssen DSGVO-konform sein
- Opt-In für Newsletter separat abfragen (nicht in Ticket-Kauf integrieren)

---

## Offene Entscheidungen [OFFEN]

- [ ] Registrierungstool auswählen
- [ ] Ticketpreise final bestätigen lassen
- [ ] Badge-Design erstellen
- [ ] Zahlungsabwicklung klären (SEPA, Kreditkarte, Paypal?)

---

*Nächster Schritt: Registrierungstool auswählen und Formular bis April 2026 einrichten.*
