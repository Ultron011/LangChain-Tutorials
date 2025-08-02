from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from dotenv import load_dotenv
from pathlib import Path

documents = [
    Document(
        page_content="""
        Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, 
        one of the two pillars of modern physics (alongside quantum mechanics). His mass–energy equivalence formula E = mc² 
        has been dubbed "the world's most famous equation".
        """,
        metadata={"source": "wiki_einstein", "topic": "Physics"}
    ),
    Document(
        page_content="""
        The Apollo 11 mission was the first to land humans on the Moon. Commander Neil Armstrong and lunar module pilot Buzz Aldrin 
        formed the American crew that landed the Apollo Lunar Module Eagle on July 20, 1969, while Michael Collins remained in lunar orbit.
        In LangChain, a Contextual Compression Retriever works by using an LLM-based compressor 
        to extract only the most relevant parts of a document given a query, reducing noise and improving retrieval quality.
        """,
        metadata={"source": "nasa_history", "mission": "Apollo11"}
    ),
    Document(
        page_content="""
        In LangChain, a Contextual Compression Retriever works by using an LLM-based compressor 
        to extract only the most relevant parts of a document given a query, reducing noise and improving retrieval quality.
        """,
        metadata={"source": "langchain_docs", "section": "Retrievers"}
    ),
    Document(
        page_content="""
        Claude Monet was a founder of French Impressionist painting. His consistent and prolific practice of painting outdoors led 
        to innovations in capturing natural light and fleeting moments, as seen in works like Water Lilies and Impression, Sunrise.
        """,
        metadata={"source": "art_catalog", "artist": "Monet"}
    ),
    Document(
        page_content="""
        Kubernetes is an open-source container orchestration platform that automates many of the manual processes involved 
        in deploying, managing, and scaling containerized applications. It groups containers into logical units for easy management and discovery.
        """,
        metadata={"source": "devops_notes", "topic": "Kubernetes"}
    ),
]

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

model = ChatGroq(model="llama-3.3-70b-versatile")

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Creating and intializing the vector store
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model
)

# Creating the base retriever
base_retriever = vector_store.as_retriever(search_kwargs={'k' : 3})

# Creating the base compressor
base_compressor = LLMChainExtractor.from_llm(model)

# Create the contextual compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=base_compressor
)

# Query the retriever
query = "Who was the first person to walk on the Moon"
compressed_result = compression_retriever.invoke(query)

for i , doc in enumerate(compressed_result):
    print(f'\n---Result {i+1}---')
    print(doc.page_content)