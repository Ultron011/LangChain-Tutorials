from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional


load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro')

class Review(BaseModel):
    
    key_themes: list[str] = Field(description="write all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment : str = Field(description="Return sentiment of the review either positive , negative or neutral")
    pros : Optional[list[str]] = Field(description="write down all the pros inside a list", default=None)
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" The hardware is great , but the software feels bloated. There are too many pre-intsalled apps that i can't remove.
             Also the UI looks Outdated as compared to other brands. Hoping for a software update to fix this.""")
print(result)