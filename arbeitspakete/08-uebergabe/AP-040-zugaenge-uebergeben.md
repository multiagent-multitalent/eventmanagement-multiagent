# AP-040: Zugänge übergeben

## Metadaten
| Feld | Wert |
|---|---|
| **ID** | AP-040 |
| **Workstream** | Nachbereitung |
| **Agent** | Operations (`.claude/agents/operations.md`) |
| **Phase** | Phase 4: Übergabe |
| **Priorität** | 🔴 Kritisch |
| **Zeitraum** | 26.06.2026 – 30.06.2026 |
| **Status** | ⬜ Offen |

## Ziel
Alle digitalen Zugänge, Accounts und Systeme an COAI gGmbH übergeben und sicherstellen, dass das Studierendenteam keinen exklusiven Zugang mehr zu Event-relevanten Systemen hat.

## Voraussetzungen (Abhängigkeiten)
- AP-039: Übergabedokumentation erstellen

## Eingaben (Inputs)
- `workstreams/nachbereitung/uebergabe-dokumentation.md` – Übersicht aller Systeme und Zugänge

## Aufgaben (Checkliste)
- [ ] Alle digitalen Systeme inventarisieren: Website-CMS, Registrierungstool, Social-Media-Accounts, E-Mail-Accounts, Newsletter-Tool, Cloud-Speicher (Repository)
- [ ] Für jedes System: COAI-Admin-Zugang einrichten oder Credentials übergeben
- [ ] Website: COAI als Admin hinzufügen, Studierenden-Accounts auf Redakteur/Viewer zurückstufen oder entfernen
- [ ] Registrierungstool: COAI-Admin-Zugang einrichten, Test-Transaktion durchführen
- [ ] Social-Media-Accounts: Account-Ownership oder Zugangsdaten übergeben
- [ ] Repository (GitHub): COAI-Teammitglieder als Owner/Admin hinzufügen
- [ ] Übergabe-Protokoll erstellen: was wurde wann übergeben, von wem an wen
- [ ] Übergabe-Protokoll in `workstreams/nachbereitung/zugaenge-uebergabe.md` dokumentieren

## Ausgaben (Outputs)
- `workstreams/nachbereitung/zugaenge-uebergabe.md` – Übergabe-Protokoll aller Zugänge

## Hinweise für den Agenten
- Zugangsdaten niemals im Klarttext im Repository speichern – nutze einen Passwort-Manager oder einen verschlüsselten Kanal für die Übergabe.
- Stelle sicher, dass COAI nach der Übergabe ALLE Zugänge selbst testen kann – kein „wird schon klappen".
- Führe die Zugänge-Übergabe idealerweise in einem gemeinsamen Übergabe-Meeting durch (persönlich oder Video-Call).
