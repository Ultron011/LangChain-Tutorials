from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

loader = TextLoader('./markdown.txt', encoding='utf8')
docs = loader.load()

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=120,
    chunk_overlap=0
)

result = splitter.split_text(docs[0].page_content)
print(result)