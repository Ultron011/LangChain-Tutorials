from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Source Documents
docs = [
    Document(
        page_content="The LangChain framework simplifies the development of LLM applications.",
        metadata={"source": "langchain_docs", "page": 1}
    ),
    Document(
        page_content="Gemini models by Google are compatible with LangChain embeddings and tools.",
        metadata={"source": "blog_post", "author": "Saurabh Kumar"}
    ),
    Document(
        page_content="RAG (Retrieval-Augmented Generation) improves answer accuracy by grounding LLMs in external data.",
        metadata={"source": "tech_article", "date": "2024-10-15"}
    ),
    Document(
        page_content="Chroma is a vectorstore library that allows semantic search over document chunks.",
        metadata={"source": "chroma_docs", "version": "0.4.14"}
    ),
    Document(
        page_content="Text splitters in LangChain break long texts into manageable semantic chunks.",
        metadata={"source": "notebook", "experiment_id": "exp42"}
    ),
]

# Creating and intializing a vector store
vector_store = Chroma(
    embedding_function=embedding_model,
    collection_name='my_collection'
)

vector_store.add_documents(docs)

retriever = vector_store.as_retriever(
    search_type='mmr', # this uses mmr search strategy to search for similarity
    search_kwargs={'k' : 3, 'lambda_mult':0.5} # lambda_mult - relevance-diverity balance
)

query = 'What is Langchain ?'
result = retriever.invoke(query)

for i , doc in enumerate(result):
    print(f'\n---Result {i+1} ---')
    print(doc.page_content)
