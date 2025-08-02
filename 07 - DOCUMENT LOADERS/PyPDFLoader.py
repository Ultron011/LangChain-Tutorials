from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader # Only good for textual data inside pdf
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

model = ChatGroq(model="llama-3.3-70b-versatile")

loader = PyPDFLoader('./dl-curriculum.pdf')

docs = loader.load()

print(docs[0].page_content)