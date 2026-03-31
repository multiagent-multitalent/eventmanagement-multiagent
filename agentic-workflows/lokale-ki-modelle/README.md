# Lokale KI-Modelle – Infrastruktur & Serving

## Überblick

Alle vorgestellten Workflow-Frameworks unterstützen **lokale KI-Modelle** über OpenAI-kompatible APIs. Dieser Abschnitt beschreibt die verschiedenen Model-Serving-Optionen, ihre Eigenschaften und Konfiguration.

---

## Vergleich der Optionen

| Tool | Typ | Einstieg | GPU nötig | OpenAI-API | Modellauswahl | Ressourcen |
|---|---|---|---|---|---|---|
| **Ollama** | CLI + API | ⭐ Sehr einfach | Nein (CPU möglich) | ✅ `/v1` | Groß | Gering |
| **LM Studio** | Desktop App | ⭐ Sehr einfach | Nein (CPU möglich) | ✅ `/v1` | Groß | Mittel |
| **LocalAI** | Docker / Binary | Mittel | Nein (CPU möglich) | ✅ vollständig | Groß | Mittel |
| **vLLM** | Python Server | Hoch | Empfohlen | ✅ vollständig | Groß | Hoch |
| **HF TGI** | Docker | Mittel | Empfohlen | ✅ | Mittel | Hoch |
| **GPT4All** | Desktop App | ⭐ Sehr einfach | Nein | ✅ `/v1` | Mittel | Gering |

---

## 1. Ollama (Empfohlen)

**Ollama** ist die einfachste Möglichkeit, LLMs lokal zu betreiben. Ein einzelner Befehl genügt zum Download und Starten.

### Installation

```bash
# Linux / macOS
curl -fsSL https://ollama.com/install.sh | sh

# Windows: Installer von https://ollama.com/download
```

### Modelle laden und starten

```bash
# Modell herunterladen und starten (in einem Befehl)
ollama run llama3.2          # Meta Llama 3.2 (3B / 7B)
ollama run mistral            # Mistral 7B
ollama run gemma3             # Google Gemma 3 (2B / 9B / 27B)
ollama run qwen2.5            # Alibaba Qwen 2.5
ollama run phi4               # Microsoft Phi-4
ollama run deepseek-r1        # DeepSeek R1 (Reasoning)

# Alle verfügbaren Modelle: https://ollama.com/library
```

### API-Endpunkt

```bash
# Ollama läuft automatisch auf Port 11434
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Hallo!"}]
  }'
```

### Empfohlene Modelle für Eventplanung

| Modell | Größe | Stärke | RAM-Bedarf |
|---|---|---|---|
| `llama3.2:3b` | 2 GB | Schnell, gut für einfache Texte | 4 GB |
| `llama3.2` | 5 GB | Ausgewogen, gut für Deutsch | 8 GB |
| `llama3.1:8b` | 5 GB | Sehr gut für Deutsch | 8 GB |
| `mistral` | 4 GB | Sehr gut für strukturierte Ausgaben | 6 GB |
| `gemma3:9b` | 6 GB | Google-Modell, gut für Analysen | 10 GB |
| `qwen2.5:7b` | 5 GB | Sehr gutes Verständnis/Ausgabe | 8 GB |
| `deepseek-r1:7b` | 5 GB | Reasoning-Modell, gut für Planung | 8 GB |

### Docker (für Server-Betrieb)

```bash
# CPU
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama_models:/root/.ollama \
  ollama/ollama

# GPU (NVIDIA)
docker run -d \
  --gpus=all \
  --name ollama \
  -p 11434:11434 \
  -v ollama_models:/root/.ollama \
  ollama/ollama
```

---

## 2. LM Studio

**LM Studio** ist eine Desktop-Applikation mit grafischer Oberfläche zum Herunterladen und Betreiben lokaler LLMs.

### Eigenschaften

- Grafische Oberfläche zum Modell-Download und -Verwaltung
- Eingebauter Chat-Client
- **OpenAI-kompatibler Server** auf Port 1234 aktivierbar
- Unterstützt GGUF-Modelle (quantisiert)
- Läuft ohne Installation (portable)

### Installation

Download von https://lmstudio.ai (Windows, macOS, Linux)

### OpenAI-kompatibler Server aktivieren

1. LM Studio öffnen
2. „Local Server" Tab auswählen
3. Modell auswählen und Server starten
4. Server läuft auf `http://localhost:1234/v1`

### API-Nutzung

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="local-model",  # Modellname wie in LM Studio angezeigt
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",  # Platzhalter
)
```

---

## 3. LocalAI

**LocalAI** ist ein vollständiger OpenAI-API-Drop-in-Ersatz, der lokal betrieben wird. Er unterstützt nicht nur Text-Modelle, sondern auch Bild-Generierung, Sprache-zu-Text und Text-zu-Sprache.

### Installation via Docker

```bash
docker run -ti -p 8080:8080 \
  -v $PWD/models:/build/models \
  --name localai \
  localai/localai:latest-aio-cpu

# GPU (NVIDIA)
docker run -ti --gpus all -p 8080:8080 \
  -v $PWD/models:/build/models \
  --name localai \
  localai/localai:latest-aio-gpu-nvidia-cuda-12
```

### Modell herunterladen

```bash
# Modell-Konfiguration erstellen
mkdir -p models
cat > models/llama3.yaml << EOF
name: llama3
backend: llama
parameters:
  model: llama-3.2-3b-instruct.Q4_K_M.gguf
  temperature: 0.1
context_size: 8192
EOF

# Modell-Datei (GGUF) herunterladen und in models/ ablegen
```

### API-Nutzung (identisch zu OpenAI)

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="llama3",
    base_url="http://localhost:8080/v1",
    api_key="local",
)
```

---

## 4. vLLM

**vLLM** ist ein hochperformanter Inference-Server für LLMs, optimiert für GPU-Betrieb mit PagedAttention-Technologie. Empfohlen für Produktionsumgebungen mit hohem Durchsatz.

### Installation

```bash
pip install vllm
```

### Server starten

```bash
# Einfach
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3.2-3B-Instruct \
  --port 8000

# Mit Quantisierung (weniger RAM)
python -m vllm.entrypoints.openai.api_server \
  --model mistralai/Mistral-7B-Instruct-v0.3 \
  --quantization awq \
  --port 8000
```

### API-Nutzung

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="meta-llama/Llama-3.2-3B-Instruct",
    base_url="http://localhost:8000/v1",
    api_key="vllm",
)
```

---

## 5. HuggingFace Text Generation Inference (TGI)

**TGI** ist der offizielle HuggingFace-Inference-Server, kompatibel mit allen HuggingFace-Modellen.

```bash
docker run --gpus all \
  --shm-size 1g \
  -p 8080:80 \
  -v $PWD/models:/data \
  ghcr.io/huggingface/text-generation-inference:latest \
  --model-id meta-llama/Llama-3.2-3B-Instruct
```

---

## Empfehlungen nach Hardware

### Laptop / Workstation (ohne GPU, 16 GB RAM)

```
Empfehlung: Ollama + llama3.2:3b oder mistral
Begründung: Niedrigster Ressourcenbedarf, einfachste Installation
Performance: ~5-15 Token/Sekunde (CPU)
```

### Workstation mit NVIDIA GPU (8 GB VRAM)

```
Empfehlung: Ollama + llama3.1:8b oder qwen2.5:7b
Begründung: GPU-Beschleunigung, gute Modellgröße
Performance: ~30-60 Token/Sekunde
```

### Server mit NVIDIA GPU (24+ GB VRAM)

```
Empfehlung: vLLM + llama3.1:70b (quantisiert) oder Mixtral
Begründung: Maximale Modellqualität, hoher Durchsatz
Performance: >100 Token/Sekunde
```

---

## Universelle Konfiguration für alle Frameworks

### .env Datei

```bash
# Lokales Modell (Ollama)
LLM_PROVIDER=ollama
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.2
LLM_API_KEY=ollama

# Oder: LocalAI
# LLM_PROVIDER=openai-compatible
# LLM_BASE_URL=http://localhost:8080/v1
# LLM_MODEL=mistral
# LLM_API_KEY=local

# Embedding-Modell (für RAG)
EMBEDDING_MODEL=nomic-embed-text
EMBEDDING_BASE_URL=http://localhost:11434
```

### Python: Universelle LLM-Factory

```python
import os
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

def get_llm(temperature: float = 0.1):
    """Erstellt LLM basierend auf Umgebungsvariablen."""
    provider = os.getenv("LLM_PROVIDER", "ollama")
    
    if provider == "ollama":
        return ChatOllama(
            model=os.getenv("LLM_MODEL", "llama3.2"),
            base_url=os.getenv("LLM_BASE_URL", "http://localhost:11434"),
            temperature=temperature,
        )
    else:
        return ChatOpenAI(
            model=os.getenv("LLM_MODEL", "mistral"),
            base_url=os.getenv("LLM_BASE_URL", "http://localhost:8080/v1"),
            api_key=os.getenv("LLM_API_KEY", "local"),
            temperature=temperature,
        )
```

---

## Embedding-Modelle für RAG

Für Retrieval-Augmented Generation (RAG) werden zusätzlich Embedding-Modelle benötigt:

```bash
# Empfohlene Embedding-Modelle für Ollama
ollama pull nomic-embed-text   # Sehr gut für Deutsch (English optimiert)
ollama pull mxbai-embed-large  # Sehr gut für multilinguale Texte
ollama pull multilingual-e5-large  # Speziell für nicht-englische Texte
```

```python
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="mxbai-embed-large",
    base_url="http://localhost:11434",
)
```

---

## Modell-Qualitätsbewertung für Deutsch

| Modell | Deutsch-Qualität | Empfehlung |
|---|---|---|
| llama3.2:3b | ⭐⭐⭐ | Schnell, ausreichend für Entwürfe |
| llama3.1:8b | ⭐⭐⭐⭐ | Gut für die meisten Aufgaben |
| mistral:7b | ⭐⭐⭐⭐ | Sehr strukturierte Ausgaben |
| qwen2.5:7b | ⭐⭐⭐⭐⭐ | Exzellent für Deutsch |
| gemma3:9b | ⭐⭐⭐⭐ | Google-Qualität |
| deepseek-r1:8b | ⭐⭐⭐⭐ | Gut für komplexe Planungsaufgaben |

> **Tipp:** Für deutschsprachige Eventplanung ist `qwen2.5:7b` oder `llama3.1:8b` empfehlenswert.
