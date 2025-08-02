from langchain_community.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.tools import InjectedToolArg
from typing import Annotated
import requests
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path
import json


env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
API_KEY = '9d4afa0c37a7738f98d36b63'


model = ChatGroq(model="llama-3.3-70b-versatile")


# Tool Creation
@tool
def get_conversion_factor(base_currency: str, target_currency: str) ->float:
    """This function fetches the currency conversion factor between a given base currency and a target currency"""
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}'
    
    response = requests.get(url)
    return response.json()

@tool 
def convert(base_currency: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float: # LLM doesn't set the value of conversion rate before the previous tool return the conversion rate
    """Given a currency conversion rate, this function calculates the target currency value from the given base currency value"""
    return base_currency * conversion_rate

# result = get_conversion_factor.invoke({'base_currency' : 'USD', 'target_currency' : "INR"})
# print(result['conversion_rate'])

# Tool Binding
llm_with_tools = model.bind_tools([get_conversion_factor, convert])

# Tool Calling
messages = [HumanMessage('what is the conversion factor between USD and INR , and based on that can u convert 10 USD into INR')]

ai_message = llm_with_tools.invoke(messages)
# print(ai_message.tool_calls)
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call)
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        messages.append(tool_message1)
    
    if tool_call['name'] == 'convert':
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)
        

result = llm_with_tools.invoke(messages)
print(result.content)