# Detaillierte Vergleichsmatrix – Agentic Workflow Tools

## Kriterien-Legende

| Symbol | Bedeutung |
|---|---|
| ✅ | Vollständig unterstützt |
| ⚠️ | Eingeschränkt / mit Aufwand möglich |
| ❌ | Nicht unterstützt |
| 🔧 | Erfordert manuelle Konfiguration |

---

## Hauptvergleich

| Kriterium | n8n | LangGraph | Flowise | Dify | AutoGen | CrewAI | Prefect |
|---|---|---|---|---|---|---|---|
| **Lizenz** | Apache 2.0 (Community) / proprietär (Enterprise) | MIT | Apache 2.0 | MIT | MIT | MIT | Apache 2.0 |
| **Programmiersprache** | TypeScript/JavaScript | Python | TypeScript/JavaScript | Python/TypeScript | Python | Python | Python |
| **Lokale Installation** | ✅ Docker | ✅ pip | ✅ Docker/npm | ✅ Docker | ✅ pip | ✅ pip | ✅ pip/Docker |
| **Visuelle Oberfläche** | ✅ | ❌ | ✅ | ✅ | ⚠️ (Studio) | ❌ | ⚠️ (Dashboard) |
| **Multi-Agenten** | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| **Lokale LLMs (Ollama)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **OpenAI-API-kompatibel** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Git-Versionierung** | ⚠️ (JSON-Export) | ✅ | ⚠️ (JSON-Export) | ⚠️ (YAML-Export) | ✅ | ✅ | ✅ |
| **Workflow-Reproduzierbarkeit** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **Externe Integrationen** | ✅✅✅ (400+ Nodes) | 🔧 | ✅ | ✅ | 🔧 | 🔧 | ✅ |
| **Einstiegshürde** | Mittel | Hoch | Niedrig | Niedrig | Mittel | Mittel | Mittel |
| **Dokumentationsqualität** | Sehr gut | Sehr gut | Gut | Sehr gut | Gut | Gut | Sehr gut |
| **Community / Aktivität** | Sehr aktiv | Sehr aktiv | Aktiv | Sehr aktiv | Aktiv | Sehr aktiv | Sehr aktiv |
| **Produktionsreife** | Hoch | Hoch | Mittel | Hoch | Mittel | Mittel-Hoch | Hoch |
| **Skalierbarkeit** | Gut | Sehr gut | Mittel | Gut | Gut | Gut | Sehr gut |
| **YAML/Code-Konfiguration** | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| **Human-in-the-Loop** | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| **Trigger / Zeitplanung** | ✅ | 🔧 | ⚠️ | ⚠️ | 🔧 | 🔧 | ✅ |
| **Observability / Tracing** | ✅ | ✅ (LangSmith) | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |

---

## Ressourcenbedarf (Lokalbetrieb)

| Tool | RAM (min.) | RAM (empfohlen) | Festplatte | CPU |
|---|---|---|---|---|
| n8n | 512 MB | 1–2 GB | 1 GB | 1 Core |
| LangGraph | 256 MB | 512 MB | 200 MB | 1 Core |
| Flowise | 512 MB | 1 GB | 500 MB | 1 Core |
| Dify | 2 GB | 4 GB | 5 GB | 2 Cores |
| AutoGen | 256 MB | 512 MB | 200 MB | 1 Core |
| CrewAI | 256 MB | 512 MB | 200 MB | 1 Core |
| Prefect | 512 MB | 1 GB | 500 MB | 1 Core |
| **Ollama + Modell** | **8 GB** | **16 GB** | **5–30 GB** | **4+ Cores** |

> **Hinweis:** Für lokale KI-Modelle ist der Ressourcenbedarf dominant. Eine GPU (NVIDIA/AMD) reduziert die Inferenzzeit erheblich.

---

## Unterstützte lokale AI-Backends

| Tool | Ollama | LocalAI | vLLM | LM Studio | HuggingFace TGI |
|---|---|---|---|---|---|
| n8n | ✅ | ✅ | ✅ | ✅ | ✅ |
| LangGraph | ✅ | ✅ | ✅ | ✅ | ✅ |
| Flowise | ✅ | ✅ | ✅ | ✅ | ✅ |
| Dify | ✅ | ✅ | ✅ | ✅ | ✅ |
| AutoGen | ✅ | ✅ | ✅ | ✅ | ✅ |
| CrewAI | ✅ | ✅ | ✅ | ✅ | ✅ |
| Prefect | ✅ | ✅ | ✅ | ✅ | ✅ |

> Alle Tools unterstützen OpenAI-kompatible APIs. Lokale Modelle werden durch Setzen der `api_base`-URL eingebunden.

---

## Anwendungsfälle im Eventmanagement

| Anwendungsfall | n8n | LangGraph | Flowise | Dify | AutoGen | CrewAI | Prefect |
|---|---|---|---|---|---|---|---|
| CfP-E-Mails automatisch kategorisieren | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Speaker-Briefings generieren | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Social-Media-Kalender erstellen | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Venue-Recherche koordinieren | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| Budget-Tracking automatisieren | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ |
| Mehrstufige Agenten-Planung | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| Integration mit externen APIs | ✅✅✅ | 🔧 | ✅ | ✅ | 🔧 | 🔧 | ✅ |
| Geplante/zeitgesteuerte Ausführung | ✅ | 🔧 | ⚠️ | ⚠️ | 🔧 | 🔧 | ✅ |
| Menschliche Genehmigungsschritte | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| Protokoll / Auditierbarkeit | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |

---

## Bewertungspunkte (0–10)

| Kriterium | Gewichtung | n8n | LangGraph | Flowise | Dify | AutoGen | CrewAI | Prefect |
|---|---|---|---|---|---|---|---|---|
| Lokalbetrieb (einfach) | 20% | 9 | 8 | 9 | 7 | 8 | 8 | 8 |
| Open Source / Lizenz | 15% | 8 | 10 | 10 | 10 | 10 | 10 | 10 |
| Lokale LLM-Unterstützung | 20% | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| Reproduzierbarkeit | 15% | 8 | 10 | 7 | 8 | 8 | 9 | 10 |
| Multi-Agenten-Fähigkeit | 15% | 6 | 10 | 6 | 9 | 10 | 10 | 6 |
| Einstiegshürde (niedrig = gut) | 10% | 7 | 4 | 9 | 9 | 6 | 6 | 6 |
| Integrationen | 5% | 10 | 6 | 8 | 8 | 6 | 6 | 8 |
| **Gesamt** | **100%** | **8,2** | **8,4** | **8,2** | **8,6** | **8,5** | **8,8** | **8,3** |

> **Hinweis:** Die Gewichtungen sind auf die Anforderungen dieses Projekts (reproduzierbare Multi-Agenten-Workflows, lokaler Betrieb) ausgerichtet. Für andere Projekte können andere Gewichtungen sinnvoller sein.

---

## Entscheidungsmatrix nach Teamprofil

| Teamprofil | Empfehlung | Begründung |
|---|---|---|
| Kein Entwickler im Team | Dify + Ollama | Vollständige UI, kein Code nötig |
| Python-Entwickler | CrewAI + LangGraph + Ollama | Maximale Kontrolle, gut dokumentiert |
| Mix aus Technikern & Nicht-Technikern | n8n + CrewAI + Ollama | n8n für Integrationen, CrewAI für Agenten |
| Fokus auf Reproduzierbarkeit | Prefect + LangGraph + Ollama | Beste Versionierbarkeit und Logging |
| Schneller Prototyp | Flowise oder Dify + Ollama | Schnellster Einstieg |
