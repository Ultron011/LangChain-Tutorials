from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

model = ChatGroq(model="llama-3.3-70b-versatile")

url = 'https://www.flipkart.com/motorola-g45-5g-brilliant-blue-128-gb/p/itmc45105311348e?pid=MOBH3YKQT2HEAPAM&lid=LSTMOBH3YKQT2HEAPAMTX4TTX&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=default_BestsellerId_tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=c35bca31-9f37-46ee-894b-9c654a2cd271.MOBH3YKQT2HEAPAM.SEARCH&ppt=browse&ppn=browse&ssid=rpzs5u7zls0000001754027492687'
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text -\n {text}",
    input_variables=['question', 'text']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    'question': 'how is camera quality?',
    'text' : docs[0].page_content
}) 

print(result)