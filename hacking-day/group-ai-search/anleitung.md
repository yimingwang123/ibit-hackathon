# Anleitung zur Auswahl und Feinabstimmung der AI Search Konfiguration auf Azure für KBA RAG Anwendungen

## Einführung

Diese Anleitung richtet sich an IT-Supporter, die AI Search in Azure optimal konfigurieren möchten, um die beste Retrieval-Augmented Generation (RAG) Lösung für eine Knowledge-Based Application (KBA) zu realisieren.

Wir orientieren uns an den folgenden Microsoft Learn Tutorials und deren wichtigsten Inhalten:

- [RAG tutorial: Design an index](https://learn.microsoft.com/en-us/azure/search/tutorial-rag-build-solution-index-schema?source=recommendations)
  - Definition eines Schema-Designs für RAG in Azure AI Search.
  - Strukturierung von Indizes, Felder und Datentypen für optimalen Abruf.
  
- [RAG tutorial: Build an indexing pipeline](https://learn.microsoft.com/en-us/azure/search/tutorial-rag-build-solution-pipeline?source=recommendations)
  - Erstellung einer Indexierungspipeline für das Laden, Chunking und Einbetten von Inhalten.
  - Automatisierung der Datenaufnahme aus verschiedenen Quellen.
  
- [RAG tutorial: Search using an LLM](https://learn.microsoft.com/en-us/azure/search/tutorial-rag-build-solution-query?source=recommendations)
  - Konstruktion von Suchanfragen für LLM-gestützte Retrievalprozesse.
  - Nutzung von LLMs zur Verbesserung von Suchergebnissen in AI Search.
  
- [RAG tutorial: Tune relevance](https://learn.microsoft.com/en-us/azure/search/tutorial-rag-build-solution-maximize-relevance?source=recommendations)
  - Anpassung der Relevanzeinstellungen zur Verbesserung von KI-gestützten Suchergebnissen.
  - Experimentieren mit BM25, Vektorsuche und hybriden Strategien.
  
- [RAG tutorial: Minimize storage and costs](https://learn.microsoft.com/en-us/azure/search/tutorial-rag-build-solution-minimize-storage?source=recommendations)
  - Vektorkomprimierung zur Reduzierung von Speicherplatzverbrauch.
  - Nutzung von schmaleren Datentypen zur Effizienzsteigerung.
  
- [Productivity tools - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/resource-tools?source=recommendations)
  - Vorstellung von Tools zur Automatisierung von Azure AI Search Workflows.
  
- [Quickstart RAG - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-rag?source=recommendations)
  - Erste Schritte zur Implementierung einer RAG-Suche mit Azure OpenAI.

## Zielsetzung

- Einführung in die Index-, Indexierungs- und Suchkonfiguration für AI Search.
- Vergleich von drei verschiedenen AI Search Konfigurationen für eine KBA RAG Anwendung.
- Bereitstellung eines Beispielcodes zur Evaluierung der Suchleistung.
- Empfehlung der besten Konfiguration basierend auf Benchmarkergebnissen.

## Voraussetzungen

- Zugriff auf Azure AI Search.
- Grundlegende Kenntnisse zu RAG-Architekturen.
- Eine eingerichtete Azure AI Search Instanz mit Indexen und Pipelines.
- Installierte Python-Umgebung mit den Bibliotheken: `azure-search-documents`, `pandas`, `matplotlib`.

## Auswahl der Test-Konfigurationen

Wir testen die folgenden drei AI Search Konfigurationen:

1. **Standard Vektor-Suche** (Vector Search mit Cosine Similarity)
2. **Hybrid-Suche** (Kombination von BM25 Textsuche + Vektor-Suche)
3. **Re-Ranking mit LLM-Unterstützung** (Erweiterung durch Azure OpenAI Re-Ranker)

### 1. Standard Vektor-Suche
Diese Konfiguration nutzt eine reine Vektor-Suche basierend auf Cosine Similarity. Sie ist effizient für embeddings-basierte Suchabfragen.

### 2. Hybrid-Suche
Hier wird BM25 für textbasierte Suche mit einer Vektor-Suche kombiniert. Dies verbessert die Ergebnisse, wenn sowohl strukturierte als auch unstrukturierte Daten genutzt werden.

### 3. Re-Ranking mit LLM
Diese Konfiguration erweitert die Hybrid-Suche durch ein LLM-gestütztes Re-Ranking der Ergebnisse. Dies verbessert die Präzision der besten Treffer.

## Beispiel: Python-Code für Benchmarking der Suchkonfigurationen

Hier ein Beispiel, um die Suchperformance der verschiedenen Konfigurationen zu testen:

```python
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd
import time

# Azure Search Konfig
service_endpoint = "https://<your-search-service>.search.windows.net"
index_name = "kba-index"
api_key = "<your-api-key>"

search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(api_key))

# TODO - Bitte die Fragen hier anpassen mit euren typischen Suchanfragen deren Lösungen in der Datenbank zu finden sind
query = "Wie kann ich mein Passwort zurücksetzen?"

configs = ["vector", "hybrid", "rerank"]
results = []

for config in configs:
    start_time = time.time()
    response = search_client.search(query, query_type=config, top=5)
    end_time = time.time()
    
    docs = [doc['content'][:200] + "..." for doc in response]
    latency = end_time - start_time
    
    results.append({
        "Konfiguration": config,
        "Latenz (s)": latency,
        "Top-Ergebnis": docs[0] if docs else "Keine Ergebnisse"
    })

# Ergebnisse ausgeben
df_results = pd.DataFrame(results)
print(df_results)
```

## Fazit & Empfehlung

Nach Durchführung der Benchmarks sollten die Ergebnisse analysiert werden, um die beste Suchkonfiguration für die spezifische KBA RAG-Anwendung zu ermitteln.

Empfohlen wird:
- **Für schnelle, kosteneffiziente Suche**: Standard Vektor-Suche.
- **Für bessere Relevanz und Textsuche**: Hybrid-Suche.
- **Für höchste Antwortqualität und LLM-Unterstützung**: Re-Ranking mit LLM.

