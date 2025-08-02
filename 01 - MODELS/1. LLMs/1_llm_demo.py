from langchain_openai import OpenAI # Tells lanchain how to communicate with openai api
from dotenv import load_dotenv # Load secret keys from .env file

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India?")

print(result)
