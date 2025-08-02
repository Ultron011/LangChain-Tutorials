from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. Define the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# 2. Define templates
report_prompt = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template="Write a 7 line summary on the following text:\n{text}",
    input_variables=["text"]
)

# 3. Create parser
parser = StrOutputParser()

chain = report_prompt | model | parser | summary_prompt | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)