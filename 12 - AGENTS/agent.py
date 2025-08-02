from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Loads the llm
model = ChatGroq(model="llama-3.3-70b-versatile")

# Load the search tool
search_tool = DuckDuckGoSearchRun()

# Load the prompt for react agent
prompt = hub.pull('hwchase17/react')

# create an react agent
agent = create_react_agent(
    llm = model,
    tools = [search_tool],
    prompt = prompt
)

# Create an agent executor
agent_executor = AgentExecutor(
    agent = agent,
    tools=[search_tool],
    verbose=True
)

response = agent_executor.invoke({"input" : 'What is the capital of india and population of india'})
print(response)