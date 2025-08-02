from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableSequence
from dotenv import  load_dotenv

load_dotenv()

model1 = ChatGroq(model="gemma2-9b-it")

model2 = ChatGroq(model='llama-3.1-8b-instant')

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet" : RunnableSequence(prompt1, model1, parser),
    "linkedin" : RunnableSequence(prompt2, model2, parser)
})

result = parallel_chain.invoke({"topic" : "AI"})
print(result['tweet'])
print(result['linkedin'])