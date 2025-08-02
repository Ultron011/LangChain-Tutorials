from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

model2 = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provied notes and quiz into a single document \n {notes} and {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
    Support Vector Machines (SVM) is a supervised machine learning algorithm commonly used for classification tasks. SVM constructs a hyperplane or set of hyperplanes in a high-dimensional space that separates the different classes. A good separation is achieved by the hyperplane that has the largest margin, meaning the maximum distance between data points of different classes.

    Support Vector Machine(SVM) is a powerful classifier that works both on linearly and nonlinearly separable data. SVM tries to find the “best” margin (distance between the line and the support vectors) that separates the classes.
"""

result = chain.invoke({"text" : text})

print(result)

chain.get_graph().print_ascii()