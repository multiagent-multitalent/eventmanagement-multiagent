"""LLM factory with automatic fallback to a mock implementation."""

import json
import logging
from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage

from src.config import get_llm_config

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Mock LLM – returns realistic German placeholder content without a live model
# ---------------------------------------------------------------------------

class MockLLM(BaseChatModel):
    """Deterministic mock that returns realistic German event-planning text."""

    model_name: str = "mock-llm"

    @property
    def _llm_type(self) -> str:
        return "mock"

    def _generate(self, messages: list[BaseMessage], **kwargs: Any):  # type: ignore[override]
        from langchain_core.outputs import ChatGeneration, ChatResult

        last_content = str(messages[-1].content) if messages else ""
        response_text = self._route_response(last_content)
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=response_text))])

    async def _agenerate(self, messages: list[BaseMessage], **kwargs: Any):  # type: ignore[override]
        return self._generate(messages, **kwargs)

    def _route_response(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        # Check planning first – these prompts also contain "venue" as selected option
        if "zeitplan" in prompt_lower or "logistikkonzept" in prompt_lower or "budgetentwurf" in prompt_lower:
            return self._mock_planning_response()
        if "einladungs-e-mail" in prompt_lower or "pressemitteilung" in prompt_lower or "social-media" in prompt_lower:
            return self._mock_content_response()
        # Research is the default – its prompt explicitly mentions venue scouting
        return self._mock_research_response()

    def _mock_research_response(self) -> str:
        data = {
            "venue_options": [
                {
                    "name": "Nürnberg Convention Center (NCC)",
                    "description": "Modernes Kongresszentrum im Herzen von Nürnberg mit flexiblen Raumaufteilungen und erstklassiger AV-Technik.",
                    "pros": [
                        "Zentrale Lage direkt am Hauptbahnhof",
                        "Kapazität für 50–500 Personen",
                        "Vollständige technische Ausstattung inklusive",
                        "Erfahrenes Veranstaltungsteam vor Ort",
                    ],
                    "cons": [
                        "Höhere Mietkosten im Vergleich zu Alternativen",
                        "Eingeschränkte Parkmöglichkeiten in der Nähe",
                    ],
                    "estimated_cost": "8.500 – 12.000 EUR",
                    "recommendation_score": 5,
                },
                {
                    "name": "Technische Hochschule Nürnberg – Campus Innovationszentrum",
                    "description": "Moderner Universitätscampus mit Hörsälen, Seminarräumen und offenen Kollaborationsflächen.",
                    "pros": [
                        "Akademisches Ambiente passend zur Zielgruppe",
                        "Günstige Konditionen für Non-Profit-Veranstalter",
                        "Gute ÖPNV-Anbindung",
                        "Flexible Raumkombinationen für parallele Tracks",
                    ],
                    "cons": [
                        "Catering muss extern organisiert werden",
                        "Begrenzte Verfügbarkeit an Wochenenden",
                    ],
                    "estimated_cost": "3.500 – 5.500 EUR",
                    "recommendation_score": 4,
                },
                {
                    "name": "Norisring Eventlocation",
                    "description": "Historisches Industriegebäude mit urbanem Charakter, ideal für kreative und technologiefokussierte Events.",
                    "pros": [
                        "Einzigartiges Ambiente mit Wiedererkennungswert",
                        "Großzügige Grundfläche für Hackathon-Bereich",
                        "Ausreichend Parkplätze vorhanden",
                    ],
                    "cons": [
                        "Aufwendigere Bestuhlung und Dekoration notwendig",
                        "Akustik erfordert zusätzliche Beschallungsanlage",
                        "Entfernung vom Stadtzentrum (ca. 15 min mit ÖPNV)",
                    ],
                    "estimated_cost": "5.000 – 7.500 EUR",
                    "recommendation_score": 3,
                },
            ],
            "catering_options": [
                {
                    "name": "Kochkollektiv Nürnberg",
                    "description": "Regionales Bio-Catering mit saisonalen Menüs, Fokus auf pflanzliche Ernährung und Nachhaltigkeit.",
                    "pros": [
                        "Regionale und saisonale Zutaten",
                        "Breites vegetarisches/veganes Angebot",
                        "Nachhaltiges Konzept (Zero Waste)",
                        "Erfahrung mit Konferenz-Catering",
                    ],
                    "cons": [
                        "Preislich im oberen Segment",
                        "Begrenzte Kapazität bei kurzfristiger Buchung",
                    ],
                    "estimated_cost": "45 – 60 EUR pro Person",
                    "recommendation_score": 5,
                },
                {
                    "name": "Gaststätte Zum Goldenen Anker – Eventcatering",
                    "description": "Traditionelles fränkisches Catering mit Buffet-Service und modernen Optionen für Konferenzen.",
                    "pros": [
                        "Klassische fränkische Küche",
                        "Gutes Preis-Leistungs-Verhältnis",
                        "Zuverlässige Lieferlogistik",
                    ],
                    "cons": [
                        "Weniger vegane/vegetarische Alternativen",
                        "Standardisiertes Angebot ohne viel Flexibilität",
                    ],
                    "estimated_cost": "30 – 40 EUR pro Person",
                    "recommendation_score": 3,
                },
                {
                    "name": "FoodTruck Festival Nürnberg GmbH",
                    "description": "Modernes Food-Truck-Konzept mit verschiedenen Küchen und einem informellen, netzwerkfördernden Ambiente.",
                    "pros": [
                        "Vielfalt an Küchen und Diätoptionen",
                        "Informelles Networking-Ambiente",
                        "Skalierbar je nach Teilnehmerzahl",
                        "Außergewöhnliches Erlebnis für Teilnehmer",
                    ],
                    "cons": [
                        "Abhängig von Außenbereich oder großer Halle",
                        "Koordinationsaufwand mit mehreren Anbietern",
                        "Wetterbedingungen bei Outdoor-Option",
                    ],
                    "estimated_cost": "35 – 50 EUR pro Person",
                    "recommendation_score": 4,
                },
            ],
        }
        return json.dumps(data, ensure_ascii=False)

    def _mock_planning_response(self) -> str:
        data = {
            "schedule": {
                "day_1": {
                    "date": "2026-10-14",
                    "theme": "Eröffnung & Keynotes",
                    "slots": [
                        {"time": "09:00 – 10:00", "activity": "Registrierung & Begrüßungskaffee"},
                        {"time": "10:00 – 10:30", "activity": "Eröffnung & Willkommensrede (Prof. Dr. Sigurd Schacht)"},
                        {"time": "10:30 – 11:30", "activity": "Keynote 1: Stand der KI-Transparenz in Europa"},
                        {"time": "11:30 – 12:30", "activity": "Keynote 2: AI Act – Praktische Umsetzung"},
                        {"time": "12:30 – 13:30", "activity": "Mittagessen & Networking"},
                        {"time": "13:30 – 15:30", "activity": "Parallele Workshops (Track A: Governance, Track B: Technik)"},
                        {"time": "15:30 – 16:00", "activity": "Kaffeepause"},
                        {"time": "16:00 – 17:30", "activity": "Panel: Verantwortungsvolle KI in der Praxis"},
                        {"time": "17:30 – 19:00", "activity": "Networking-Empfang & Get-Together"},
                    ],
                },
                "day_2": {
                    "date": "2026-10-15",
                    "theme": "Workshops & Hackathon",
                    "slots": [
                        {"time": "09:00 – 09:15", "activity": "Tageseröffnung"},
                        {"time": "09:15 – 12:00", "activity": "Hackathon: KI-Transparenz-Tools entwickeln"},
                        {"time": "09:15 – 12:00", "activity": "Workshop-Reihe: Human Compatible AI (parallel)"},
                        {"time": "12:00 – 13:00", "activity": "Mittagessen"},
                        {"time": "13:00 – 15:00", "activity": "Präsentationen der Hackathon-Gruppen"},
                        {"time": "15:00 – 16:30", "activity": "Keynote 3: AI Safety – Globale Perspektiven"},
                        {"time": "16:30 – 17:30", "activity": "Roundtable: Zukünftige Regulierung von KI"},
                        {"time": "17:30 – 18:00", "activity": "Tagesabschluss"},
                        {"time": "19:00 – 22:00", "activity": "Conference Dinner (optional, Extraticket)"},
                    ],
                },
                "day_3": {
                    "date": "2026-10-16",
                    "theme": "Abschluss & Ausblick",
                    "slots": [
                        {"time": "09:00 – 09:15", "activity": "Tageseröffnung"},
                        {"time": "09:15 – 11:00", "activity": "Keynote 4: Policy-Empfehlungen zum EU AI Act"},
                        {"time": "11:00 – 12:30", "activity": "Workshops: Anwendungsfälle KI-Governance"},
                        {"time": "12:30 – 13:30", "activity": "Mittagessen"},
                        {"time": "13:30 – 15:00", "activity": "World Café: Lessons Learned & Best Practices"},
                        {"time": "15:00 – 16:00", "activity": "Abschlusspanel & Ausblick AITD 2027"},
                        {"time": "16:00 – 16:30", "activity": "Verabschiedung & Ausklang"},
                    ],
                },
            },
            "logistics": {
                "venue_setup": "Aufbau am 13. Oktober 2026 (Vortag), Abbau am 16. Oktober nach 17:00 Uhr.",
                "registration": "Online-Registrierung via Pretix. Vor-Ort-Check-in mit QR-Code-Scan.",
                "av_technology": "Beamer, Mikrofone, Live-Streaming-Setup für alle Hauptsessions.",
                "accessibility": "Barrierefreier Zugang, Induktionsschleife für Hörbehinderte, Live-Untertitel.",
                "accommodation": "Zimmerkontingent in 3 Partnerhotels in der Nähe des Veranstaltungsorts.",
                "transport": "ÖPNV-Empfehlungen, Shuttle-Service vom Hauptbahnhof am An-/Abreisetag.",
                "wifi": "Dediziertes Konferenz-WLAN, Kapazität für 200+ Geräte.",
                "sustainability": "Recyclingpapier, digitale Unterlagen bevorzugt, CO₂-Kompensation.",
            },
            "budget": {
                "currency": "EUR",
                "total_estimated": 42500,
                "breakdown": {
                    "venue": {"amount": 8500, "note": "NCC Tagespauschale 3 Tage"},
                    "catering": {"amount": 7500, "note": "125 Personen × 2,5 Tage × 24 EUR (Puffer)"},
                    "av_technology": {"amount": 4500, "note": "Ton, Licht, Streaming, Kameras"},
                    "speakers": {"amount": 6000, "note": "Reise + Unterkunft 6 Keynote-Speaker"},
                    "marketing": {"amount": 3500, "note": "Print, Online-Werbung, Social Media"},
                    "staff": {"amount": 4000, "note": "Eventpersonal, Moderatoren, Helfer"},
                    "accommodation_partner": {"amount": 2000, "note": "Zimmerkontingent-Verwaltung"},
                    "contingency": {"amount": 4000, "note": "Puffer 10%"},
                    "misc": {"amount": 2500, "note": "Drucksachen, Namensschilder, Goodie-Bags"},
                },
            },
        }
        return json.dumps(data, ensure_ascii=False)

    def _mock_content_response(self) -> str:
        data = {
            "invitation_email": {
                "subject": "Einladung: AI Transparency Days 2026 – 14.–16. Oktober in Nürnberg",
                "body": (
                    "Sehr geehrte Damen und Herren,\n\n"
                    "wir freuen uns, Sie herzlich zu den AI Transparency Days 2026 einzuladen!\n\n"
                    "Vom 14. bis 16. Oktober 2026 bringen wir in Nürnberg führende Expertinnen und Experten "
                    "aus Forschung, Industrie und Politik zusammen, um die Zukunft transparenter und "
                    "verantwortungsvoller Künstlicher Intelligenz zu gestalten.\n\n"
                    "**Was Sie erwartet:**\n"
                    "• 4 hochkarätige Keynotes von internationalen KI-Expertinnen und -Experten\n"
                    "• Praxisworkshops zu AI Governance & AI Safety\n"
                    "• Hackathon: Entwickeln Sie KI-Transparenz-Tools\n"
                    "• Exklusives Networking mit 125 Gleichgesinnten\n\n"
                    "**Datum:** 14.–16. Oktober 2026\n"
                    "**Ort:** Nürnberg Convention Center, Nürnberg\n\n"
                    "Sichern Sie sich jetzt Ihren Platz: [Registrierungslink]\n\n"
                    "Mit freundlichen Grüßen,\n"
                    "Das AITD 2026-Team\n"
                    "COAI gGmbH"
                ),
            },
            "social_media_posts": {
                "twitter_x": (
                    "🚀 Save the Date! Die #AITransparencyDays 2026 kommen nach Nürnberg!\n\n"
                    "📅 14.–16. Oktober 2026\n"
                    "📍 Nürnberg\n"
                    "🎯 KI-Transparenz • AI Safety • AI Governance\n\n"
                    "Keynotes, Workshops & Hackathon – seid dabei! 🤖✨\n\n"
                    "👉 Jetzt registrieren: [Link]\n"
                    "#AITD2026 #KI #ArtificialIntelligence #AIAct #Nürnberg"
                ),
                "linkedin": (
                    "🎉 **AI Transparency Days 2026 – Call for Participation!**\n\n"
                    "Wir laden Sie herzlich zu Deutschlands führender Konferenz für KI-Transparenz ein:\n\n"
                    "📅 **Datum:** 14.–16. Oktober 2026\n"
                    "📍 **Ort:** Nürnberg Convention Center\n"
                    "👥 **Teilnehmende:** 125 Expertinnen und Experten\n\n"
                    "**Programm-Highlights:**\n"
                    "✅ International renommierte Keynote-Speaker\n"
                    "✅ Praxisnahe Workshops zu AI Governance & AI Safety\n"
                    "✅ Hackathon für KI-Transparenz-Lösungen\n"
                    "✅ Intensives Networking mit der KI-Community\n\n"
                    "Veranstaltet von der COAI gGmbH in Kooperation mit der Hochschule Ansbach.\n\n"
                    "🔗 Jetzt anmelden: [Link]\n\n"
                    "#AITD2026 #AITransparenz #KünstlicheIntelligenz #AIAct #Innovation #Nürnberg"
                ),
                "instagram": (
                    "✨ Große Ankündigung! ✨\n\n"
                    "Die AI Transparency Days 2026 kommen nach Nürnberg! 🤖🌟\n\n"
                    "3 Tage | 125 Köpfe | 1 Mission: KI transparenter und sicherer machen 💡\n\n"
                    "📅 14.–16. Oktober 2026\n"
                    "📍 Nürnberg, Deutschland\n\n"
                    "Was dich erwartet:\n"
                    "🎤 Top-Keynotes\n"
                    "🛠 Hands-on Workshops\n"
                    "💻 Hackathon\n"
                    "🤝 Epic Networking\n\n"
                    "Link in Bio für Tickets & Infos! 🔗\n\n"
                    "#AITD2026 #KI #AI #AITransparency #Nürnberg #Tech #Innovation #Conference"
                ),
            },
            "press_release": {
                "headline": "AI Transparency Days 2026: Nürnberg wird zum Zentrum der KI-Transparenz-Debatte",
                "subheadline": "COAI gGmbH lädt vom 14. bis 16. Oktober 2026 zu Konferenz, Workshops und Hackathon ein",
                "body": (
                    "Nürnberg, April 2026 – Die gemeinnützige Forschungsorganisation COAI gGmbH veranstaltet "
                    "vom 14. bis 16. Oktober 2026 die AI Transparency Days 2026 (AITD 2026) im Nürnberg "
                    "Convention Center. Die Konferenz bringt rund 125 Expertinnen und Experten aus Forschung, "
                    "Industrie und Politik zusammen, um aktuelle Fragen zu KI-Transparenz, AI Safety und "
                    "AI Governance zu diskutieren.\n\n"
                    "Unter dem Motto 'Transparenz schafft Vertrauen' bietet die dreitägige Veranstaltung ein "
                    "abwechslungsreiches Programm: Neben vier internationalen Keynotes stehen praxisnahe "
                    "Workshops, ein Hackathon zur Entwicklung von KI-Transparenz-Tools sowie ausgedehnte "
                    "Networking-Möglichkeiten auf dem Programm.\n\n"
                    "'Mit den AI Transparency Days 2026 wollen wir einen wichtigen Beitrag zur gesellschaftlichen "
                    "Diskussion über verantwortungsvolle KI leisten', erklärt Steffen Höpfner, Geschäftsführer "
                    "der COAI gGmbH. 'Nürnberg ist als Technologiestandort der ideale Austragungsort für dieses "
                    "Event.'\n\n"
                    "Die Registrierung für die AI Transparency Days 2026 ist ab Mai 2026 möglich. Weitere "
                    "Informationen sind unter www.coairesearch.org verfügbar.\n\n"
                    "**Über COAI gGmbH**\n"
                    "Die COAI gGmbH ist ein gemeinnütziges Forschungsinstitut für Human Compatible AI mit Sitz "
                    "in Nürnberg. Das Institut forscht und informiert zu den gesellschaftlichen Auswirkungen "
                    "Künstlicher Intelligenz und setzt sich für transparente und sichere KI-Systeme ein."
                ),
                "contact": {
                    "organization": "COAI gGmbH",
                    "website": "https://www.coairesearch.org",
                    "city": "Nürnberg",
                },
            },
        }
        return json.dumps(data, ensure_ascii=False)


# ---------------------------------------------------------------------------
# LLM factory
# ---------------------------------------------------------------------------

def create_llm() -> BaseChatModel:
    """Create the configured LLM, falling back to MockLLM on connection errors."""
    cfg = get_llm_config()
    provider = cfg["provider"]

    try:
        if provider == "ollama":
            from langchain_community.chat_models import ChatOllama

            llm = ChatOllama(
                model=cfg["model"],
                base_url=cfg["base_url"],
                temperature=cfg["temperature"],
            )
            # Connectivity probe – detect early if Ollama is reachable
            llm.invoke("Verbindungstest")
            return llm

        if provider in ("openai", "openai_compatible"):
            from langchain_openai import ChatOpenAI

            return ChatOpenAI(
                model=cfg["model"],
                openai_api_base=cfg["base_url"],
                openai_api_key=cfg["api_key"],
                temperature=cfg["temperature"],
            )

    except Exception as exc:
        logger.warning("LLM '%s' unavailable (%s) – falling back to MockLLM.", provider, exc)

    return MockLLM()
