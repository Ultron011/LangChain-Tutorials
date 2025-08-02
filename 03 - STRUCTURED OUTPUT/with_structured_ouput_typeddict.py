from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro')

class Review(TypedDict):
    summary: Annotated[str, "a brief summary of the review"]
    sentiment: Annotated[str, "return sentiment of the review either negative , positive or netural"]
    pros: Annotated[Optional[str], "Write the name of the reviewer"]
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" The hardware is great , but the software feels bloated. There are too many pre-intsalled apps that i can't remove.
             Also the UI looks Outdated as compared to other brands. Hoping for a software update to fix this.""")
print(result)