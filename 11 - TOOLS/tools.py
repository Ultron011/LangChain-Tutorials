from langchain_community.tools import DuckDuckGoSearchRun, ShellTool, StructuredTool, BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_core.tools import tool

# Built-in tools

# Used to search the web
# search_tool = DuckDuckGoSearchRun()

# results = search_tool.invoke('ipl news')
# print(results)

# Used to run command line script
# shell_tool = ShellTool()
# results = shell_tool.invoke('pip show langchain')
# print(results)

# Custom tools

# Using @tool decorator
# @tool
# def multiply(a:int, b:int) -> int:
#     """Multiply two numbers"""
#     return a*b

# result = multiply.invoke({'a': 3, 'b' : 5})
# print(result)
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)
# print(multiply.args_schema.model_json_schema())

# Using StructuredTool and Pydantic - Enforces more strict rules for input types to the tool 
# class MultiplyInput(BaseModel):
#     a : int = Field(required=True, description='The first number to add')
#     b : int = Field(required=True, description='The second number to add')

# def multiply_func(a : int , b : int) -> int:
#     return a * b

# multiply_tool = StructuredTool.from_function(
#     func = multiply_func,
#     name='multiply',
#     description='Multiply two numbers',
#     args_schema=MultiplyInput
# )

# result = multiply_tool.invoke({'a' : 5, 'b': 3})
# print(result)

# Using BaseTool class
class MultiplyInput(BaseModel):
    a : int = Field(required=True, description='The first number to add')
    b : int = Field(required=True, description='The second number to add')

class MultiplyTool(BaseTool):
    name : str = 'multiply'
    description: str= 'Multiply two numbers'
    
    args_schema: Type[BaseModel] = MultiplyInput
    
    def _run(self, a:int, b:int) -> int:
        return a*b
    
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({ 'a' : 10, 'b' : 10})
print(result)