from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional


load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro')

json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes" : {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the themes discussed in the review in a list"
        }
    },
    "required": ["key_themes"]
}
    
structured_model = model.with_structured_output(json_schema )

result = structured_model.invoke(""" The hardware is great , but the software feels bloated. There are too many pre-intsalled apps that i can't remove.
             Also the UI looks Outdated as compared to other brands. Hoping for a software update to fix this.""")
print(result)