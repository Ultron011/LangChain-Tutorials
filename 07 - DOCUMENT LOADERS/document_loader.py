from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableLambda
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

def document_loader(input_dict):
    file_path = input_dict['file_path']
    loader = TextLoader(file_path, encoding='utf8')
    docs = loader.load()
    return {'rules': docs[0].page_content}

DocumentLoader = RunnableLambda(document_loader)  

prompt = PromptTemplate(
    template="Simulate a game based on the following rulebook \n Rulebook - {rules}",
    input_variables=['rules']
)

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

chain = DocumentLoader | prompt | model | parser

result = chain.invoke({'file_path' : './game_rulebook.txt'})
print(result)