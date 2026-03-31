# Registrierungs-Vorlage: [Event-Name]

*Vorlage – Platzhalter [in eckigen Klammern] durch konkrete Angaben ersetzen*

---

## Registrierungsformular-Felder

### Pflichtfelder

**Persönliche Daten**
- Vorname *
- Nachname *
- E-Mail-Adresse *
- Organisation / Unternehmen / Hochschule *
- Position / Rolle *
- Land *

**Ticket-Auswahl**
- Ticket-Kategorie * (Dropdown: Early Bird / Regular / Studierende / Sonstiges)
- Gutscheincode (Freitext, optional)

**Event-relevante Angaben**
- Ernährungsbedürfnisse * (Checkbox: Keine / Vegetarisch / Vegan / Glutenfrei / Laktosefrei / Halal / Koscher / Sonstiges → Freitext)
- Teilnahme Social Dinner? * (Ja / Nein / Vielleicht)
- Wie haben Sie von uns erfahren? (Dropdown: Newsletter / Social Media / Kolleg:in / Hochschule / Presse / Sonstiges)

**Optionale Felder**
- LinkedIn-Profil (URL)
- Interesse an Hackathon-Teilnahme? (Ja / Nein)
- Im Teilnehmer-Verzeichnis erscheinen? (Ja / Nein)
- Kommentar / Besondere Anforderungen (Freitext)

**Datenschutz**
- Datenschutzerklärung akzeptieren * (Checkbox + Link zur Datenschutzerklärung)
- Newsletter-Opt-in (separates Checkbox, nicht verpflichtend)

---

## Ticket-Kategorien

| Kategorie | Preis | Gültig bis | Nachweis |
|---|---|---|---|
| Early Bird | [€] | [Datum] | – |
| Regular | [€] | [Event-Ende] | – |
| Studierende | [€] | [Event-Ende] | Immatrikulationsnachweis |
| Speaker | 0 € | – | Einladungscode |
| Sponsor-Kontingent | 0 € | – | Sponsor-Code |

---

## Bestätigungs-E-Mail

**Betreff:** Anmeldung bestätigt: [Event-Name] ✅

```
Hallo [Vorname],

vielen Dank für deine Anmeldung zu [Event-Name]!

📅 Datum: [Datum]
📍 Ort: [Venue, Ort]
🎫 Ticket-Kategorie: [Kategorie]
📋 Buchungsnummer: [Nummer]

Dein QR-Code für den Check-In ist im Anhang / unter diesem Link: [Link/QR-Code]

Was passiert als Nächstes:
→ Das Programm wird veröffentlicht am [Datum]
→ Ein Infopaket mit allen Details erhältst du ca. 2 Wochen vor dem Event

Fragen? [kontakt@event.de] oder [Website]

Wir freuen uns auf dich!
Das [Event-Name]-Team
```

---

## Reminder-E-Mail (2 Wochen vor Event)

**Betreff:** [Event-Name] in 2 Wochen! Alle Infos

```
Hallo [Vorname],

es ist fast so weit! In 2 Wochen startet [Event-Name].

📅 Datum: [Datum]
📍 Adresse: [Vollständige Adresse + Maps-Link]
⏰ Check-In: ab [Uhrzeit]

Programm-Highlights:
→ [Highlight 1]
→ [Highlight 2]
→ [Highlight 3]

Praktische Infos:
→ Anreise: [Kurze Beschreibung / Link zu Details]
→ Hotel-Empfehlungen: [Link]
→ WLAN vor Ort: [SSID] / Passwort am Check-In

Dein QR-Code für den Check-In: [QR-Code / Link]

Fragen? [kontakt@event.de]

Bis bald!
Das [Event-Name]-Team
```

---

## Check-In-Prozess

### Setup
- 2–3 Check-In-Stationen
- Teilnehmer-Suche: Name ODER QR-Code-Scan
- Badges: vorbereitete Boxen (alphabetisch) oder On-Demand-Druck

### Ablauf
1. Teilnehmer kommt → QR-Code zeigen oder Name nennen
2. Im System suchen und einchecken
3. Badge ausgeben
4. Programm / Welcome-Pack ausgeben
5. Kurze Orientierung geben

---

## Empfohlene Tools

| Tool | Typ | Kosten | DSGVO |
|---|---|---|---|
| pretix | Open-Source, selbst hostbar | kostenlos + Hosting | ✅ |
| Tito | SaaS | kostenlos bis 1.000 € | ✅ |
| Eventbrite | SaaS | ~3% + 0,75 €/Ticket | ✅ |

---

*Vorlage aus dem AITD-2026-Event-Management-Repository.*
