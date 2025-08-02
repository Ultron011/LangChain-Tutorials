from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import  load_dotenv

load_dotenv()

model = ChatGroq(model="gemma2-9b-it")

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the following joke \n {joke}",
    input_variables=['joke']
)

parser = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt1 , model, parser)

parallel_chain = RunnableParallel({
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(prompt2, model, parser)
        })

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)
result = final_chain.invoke({"topic": "school"})
print(result['joke'])
print(result['explanation'])