from langchain_community.retrievers import WikipediaRetriever

# Initialize the retriever
retriever = WikipediaRetriever(
    top_k_results=2,
    lang='en'
)

query = 'Russia vs Ukraine'
docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f'Result {i+1} - ')
    print(f'{doc.page_content}...')