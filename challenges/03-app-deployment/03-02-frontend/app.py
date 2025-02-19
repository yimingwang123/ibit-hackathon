import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from langchain.callbacks.base import BaseCallbackHandler
from azure.search.documents.models import VectorizedQuery


# Lade Umgebungsvariablen
load_dotenv(dotenv_path="../../../.env")

# Azure AI Search & CosmosDB Config
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")
AZURE_SEARCH_INDEX = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")

# OpenAI Config
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME")
EMBEDDING_NAME = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")


# Set up Hybrid Search with Azure AI Search
def setup_azure_ai():
    """Initialisiert Azure AI Search für Hybrid-Suche."""
    
    # Embedding Model für Vektor-Suche
    embeddings_model = AzureOpenAIEmbeddings(
        azure_deployment=EMBEDDING_NAME,
        chunk_size=1
    )

    # Azure AI Search Client
    search_client = SearchClient(
        endpoint=AZURE_SEARCH_ENDPOINT,
        index_name=AZURE_SEARCH_INDEX,
        credential=AzureKeyCredential(AZURE_SEARCH_KEY)
    )

    # LLM (GPT) Initialisierung
    llm = AzureChatOpenAI(
        azure_deployment = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME")
    )

    return search_client, embeddings_model, llm


# Azure AI Hybrid Search
def hybrid_search(query, search_client, embeddings_model):
    """Führt eine Hybrid-Suche mit Azure AI Search durch (Keyword + Vector + Semantic)."""
    
    # Vektor-Erstellung für semantische Suche 
    query_vector = embeddings_model.embed_query(query)

    vector_query = VectorizedQuery(
    vector=query_vector,
    k_nearest_neighbors=5,  # Anzahl der ähnlichen Treffer
    fields="vector"  # Das Feld im Index, das Embeddings enthält
)

    # Azure AI Search Abfrage 
    search_results = search_client.search(
    search_text=query,  # Textbasierte Suche
    vector_queries=[vector_query],  # Vektorbasierte Suche
    query_type="semantic",  # Semantische Suche aktivieren
    semantic_configuration_name="movies-semantic-config",
    select=['id', 'original_language', 'original_title', 'popularity',
            'release_date', 'vote_average', 'vote_count', 'genre',
            'overview', 'revenue', 'runtime', 'tagline'],
    top=5
)

    #  Ergebnisse formatieren 
    context = []
    for item in search_results:
        context.append(
            f"-  🎬 Titel:  {item.get('original_title', 'N/A')}\n"
            f"  -  🌍 Sprache:  {item.get('original_language', 'N/A')}\n"
            f"  -  📅 Erscheinungsdatum:  {item.get('release_date', 'N/A')}\n"
            f"  -  ⭐ Bewertung:  {item.get('vote_average', 'N/A')} ({item.get('vote_count', 'N/A')} Stimmen)\n"
            f"  -  🔥 Beliebtheit:  {item.get('popularity', 'N/A')}\n"
            f"  -  🎭 Genre:  {item.get('genre', 'N/A')}\n"
            f"  -  🕒 Laufzeit:  {item.get('runtime', 'N/A')} Minuten\n"
            f"  -  💰 Einnahmen:  {item.get('revenue', 'N/A')}\n"
            f"  -  📝 Beschreibung:  {item.get('overview', 'Keine Beschreibung verfügbar')}\n"
            f"  -  📢 Tagline:  {item.get('tagline', 'Keine Tagline')}\n"
            f"  {'-'*50}"
        )

    return "\n".join(context)



#  Streamlit Callback Handlers 
class StreamHandler(BaseCallbackHandler):
    """Verarbeitet LLM-Streaming-Ausgabe für die UI."""
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str,  kwargs):
        self.text += token
        self.container.info(self.text)


#  Streamlit UI Setup 
st.sidebar.image("movieagent.jpg")
st.header("🎬 `Movie AI Agent`")
st.info("Ich bin ein KI-Agent, der Fragen zu Filmen beantworten kann.")

# Initialisierung von Azure AI Search & OpenAI Embeddings
if 'search_client' not in st.session_state:
    st.session_state['search_client'], st.session_state['embeddings_model'], st.session_state['llm'] = setup_azure_ai()

search_client = st.session_state.search_client
embeddings_model = st.session_state.embeddings_model
llm = st.session_state.llm

#  Benutzerabfrage 
question = st.text_input("🎤 `Stelle eine Frage zu Filmen:`")

if question:
    #  Hybrid AI Search starten 
    film_kontext = hybrid_search(question, search_client, embeddings_model)

    #  Prompt Template für LLM 
    prompt_template = PromptTemplate(
        input_variables=["frage", "film_kontext"],
        template="""Du bist ein KI-System, das auf Basis der folgenden Filmdaten antworten soll.
        Frage: {frage}
        
        Hier sind die relevanten Filminformationen, die als Kontext dienen:
        {film_kontext}
        
        Antworte bitte möglichst konkret.
        """
    )

    #  Pipeline definieren 
    chain = LLMChain(llm=llm, prompt=prompt_template)

    #  Antwort generieren 
    answer = st.empty()
    stream_handler = StreamHandler(answer, initial_text="`💡 Antwort:`\n\n")
    
    result = chain.run({"frage": question, "film_kontext": film_kontext}, callbacks=[stream_handler])

    #  Ausgabe formatieren 
    st.subheader("🎬 `Antwort:`")
    st.info(result)
    
    st.subheader("📚 `Genutzte Filminformationen:`")
    st.markdown(film_kontext)
