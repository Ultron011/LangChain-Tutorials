from langchain_groq import ChatGroq
from langchain_community.tools import tool
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

result = llm_with_tools.invoke("Multiply 3 with 5")
print(result.tool_calls)