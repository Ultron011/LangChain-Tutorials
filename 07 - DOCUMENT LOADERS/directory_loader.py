from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path='./dummy_data',
    glob='*.txt',
    loader_cls=TextLoader
)

# Loads all the documents at once
# docs = loader.load()

# for document in docs:
#     print(document.metadata)

# Loads On Demand
docs = loader.lazy_load()
for document in docs:
    print(document.metadata)