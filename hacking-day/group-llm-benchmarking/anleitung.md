# Anleitung zur Benchmarking von LLMs in Azure AI Foundry für KBA RAG Anwendungen

## Einführung

Diese Anleitung richtet sich an IT-Supporter, die Large Language Models (LLMs) in Azure AI Foundry benchmarken möchten, um das beste Modell für eine Knowledge-Based Augmented Retrieval (KBA RAG) Anwendung zu finden.

Wir orientieren uns zunächst an den Grundlagen der [Azure AI Search RAG Lösungen](https://learn.microsoft.com/en-us/azure/search/tutorial-rag-build-solution-models) und vertiefen dann das Verständnis für [Model Benchmarks in Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/model-benchmarks).

## Zielsetzung

- Einarbeitung in die Benchmarking-Prozesse für LLMs in Azure AI Foundry.
- Vergleich von fünf ausgewählten Modellen für eine KBA RAG Anwendung.
- Bereitstellung eines Beispielcodes zur Durchführung eines Benchmarks.
- Empfehlung des besten Modells basierend auf den Testergebnissen.

## Voraussetzungen

- Zugriff auf Azure AI Studio und Azure AI Foundry.
- Basiswissen zu LLMs und RAG-Architekturen.
- Eine eingerichtete Azure-Umgebung mit AI Foundry und OpenAI oder Azure OpenAI Modelle.
- Installierte Python-Umgebung mit den Bibliotheken: `azure-ai-ml`, `openai`, `pandas`, `matplotlib`.

## Auswahl der Test-Modelle

Wir testen die folgenden fünf LLMs, die in Azure AI Foundry verfügbar sind:

1. **GPT-4 Turbo (OpenAI)**
2. **Gemini 1.5 Pro (Google DeepMind)**
3. **Claude 3 Opus (Anthropic)**
4. **Mistral Large (Mistral AI)**
5. **Llama 3 70B (Meta)**

Diese Modelle wurden aufgrund ihrer Vielseitigkeit, Retrieval-Fähigkeiten und Performance im RAG-Umfeld ausgewählt.

## Benchmarking-Ansatz

Das Benchmarking erfolgt anhand folgender Kriterien:

- **Antwortqualität**: Präzision und Korrektheit der generierten Antworten.
- **Latenz**: Antwortzeit des Modells.
- **Kosten**: Token-Kosten pro Abfrage.
- **Kontextverständnis**: Fähigkeit, über längere Kontextfenster relevante Antworten zu generieren.
- **Skalierbarkeit**: Effizienz für hohe Nutzerlasten.

## Beispiel: Python-Code für Benchmarking

Hier ein Beispielskript zur Durchführung der Benchmarks:

```python
import openai
import time
import pandas as pd
import matplotlib.pyplot as plt

# Modell-Setup
test_models = [
    {"name": "gpt-4-turbo", "provider": "openai"},
    {"name": "gemini-1.5-pro", "provider": "google"},
    {"name": "claude-3-opus", "provider": "anthropic"},
    {"name": "mistral-large", "provider": "mistral"},
    {"name": "llama-3-70b", "provider": "meta"},
]

# TODO - Bitte die Fragen hier anpassen mit euren typischen Suchanfragen deren Lösungen in der Datenbank zu finden sind
prompt = "Wie kann ich mein Passwort zurücksetzen?"

benchmark_results = []

for model in test_models:
    start_time = time.time()
    response = openai.ChatCompletion.create(
        model=model["name"],
        # TODO - Bitte hier auch System Promp anpassen. Ihr müsstet im Experimentieren selbst rausfinden welches System Prompt am bestem performt.
        messages=[{"role": "system", "content": "Du bist ein hilfreicher KI-Assistent."},
                  {"role": "user", "content": prompt}]
    )
    end_time = time.time()
    
    answer = response["choices"][0]["message"]["content"]
    token_usage = response["usage"]["total_tokens"]
    latency = end_time - start_time
    
    benchmark_results.append({
        "Model": model["name"],
        "Antwort": answer[:1000] + "...",  # Nur die ersten 1000 Zeichen zur Übersicht
        "Latenz (s)": latency,
        "Tokens": token_usage
    })

# Ergebnisse in DataFrame speichern
df_results = pd.DataFrame(benchmark_results)
print(df_results)

# Visualisierung
plt.figure(figsize=(10, 5))
plt.bar(df_results["Model"], df_results["Latenz (s)"], color='blue')
plt.xlabel("Model")
plt.ylabel("Latenz (s)")
plt.title("Benchmark Latenzvergleich")
plt.show()
```

## Fazit & Empfehlung

Nach Durchführung der Benchmarks sollten die Ergebnisse analysiert werden, um das beste Modell für die spezifische RAG-Anwendung auszuwählen. Basierend auf den erfassten Daten kann eine fundierte Entscheidung getroffen werden.

Empfohlen wird eine Kombination aus:

- **Qualitativ bester Antwort**: GPT-4 Turbo oder Claude 3 Opus.
- **Schnellste Antwortzeiten**: Mistral Large oder Gemini 1.5 Pro.
- **Kosteneffizienz**: Llama 3 70B.

Je nach Anforderungen an Kosten, Geschwindigkeit oder Antwortqualität sollte das Modell angepasst werden.

