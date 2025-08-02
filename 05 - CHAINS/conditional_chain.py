from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # Use gemini-2.0-flash only if supported

# Output parsers
parser = StrOutputParser()

# Define Pydantic output model
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompt for sentiment classification
prompt1 = PromptTemplate(
    template=(
        "Classify the sentiment of the following feedback text into positive or negative:\n"
        "{feedback}\n"
        "{format_instructions}"
    ),
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

# Classifier chain: feedback → model → structured sentiment
classifier_chain = prompt1 | model | parser2

# Prompts for response generation
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=["feedback"]
)

# Branching based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not determine sentiment.")
)

# Full chain
chain = classifier_chain | branch_chain

# Example invocation
result = chain.invoke({"feedback": "This is a Wonderful phone."})
print(result)
