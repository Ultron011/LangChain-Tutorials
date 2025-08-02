from langchain_groq import ChatGroq
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# LLM setup
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Define a tool
@tool
def multiply(a: int, b: int) -> int:
    '''Multiplies two integers.'''
    return a * b


llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage('can u multiply 3 with 10')

messages = [query]

result = llm_with_tools.invoke(messages)

messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

print(llm_with_tools.invoke(messages).content)