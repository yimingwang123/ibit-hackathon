# Movie AI Agent - README

## Beschreibung
Dies ist eine Streamlit-Webanwendung, die mit Azure AI Search und Azure OpenAI arbeitet, um Fragen zu Filmen basierend auf einer durchsuchbaren Datenbank zu beantworten. Die Anwendung nutzt hybride Suche (semantisch + vektorisiert) für präzisere Ergebnisse.

## Voraussetzungen

### 1. Notwendige Pakete installieren
Installiere die benötigten Bibliotheken mit:

```bash
pip install -r requirements.txt
```

## Anwendung starten

### 1. Streamlit-App ausführen
Nachdem alle Abhängigkeiten installiert und die `.env` Datei eingerichtet wurde, starte die App mit:

```bash
streamlit run app.py
```

## Troubleshooting

Falls die Anwendung nicht startet oder Fehler auftreten, überprüfe:

- Sind die Umgebungsvariablen korrekt gesetzt?
- Sind alle benötigten Python-Pakete installiert? (`pip install -r requirements.txt`)
- Läuft die richtige Python-Version? (`python --version`)
- Existiert dein AI Search Index in Azure?

Falls weiterhin Probleme auftreten, führe die App im Debug-Modus aus:

```bash
streamlit run app.py --server.runOnSave true
```

## Support

Falls du Fragen hast oder Hilfe brauchst, erstelle ein GitHub Issue oder kontaktiere die Entwicklerin (yimiwang@microsoft.com).
