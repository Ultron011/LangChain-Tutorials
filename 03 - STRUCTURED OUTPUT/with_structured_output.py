from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

#Schema
# class Review(TypedDict):
#     key_themes: Annotated[list[str], "write down all the key themes discussed in the reivew in a list"]
#     summary: Annotated[str, 'A brief summary of the review']
#     sentiment: Annotated[Literal['pos', 'neg'], 'Return the sentiment of the review either positive , negative or neutral']
#     pros: Annotated[Optional[list[str]], 'Write down all the pros inside a list']
#     cons: Annotated[Optional[list[str]], 'Write down all the cons inside a list']
    
# Schema
# class Review(BaseModel):
#     key_themes: list[str] = Field(description='write down all the key themes discussed in the reivew in a list')
#     summary: str = Field(description='A brief summary of the review')
#     sentiment: Literal['pos', 'neg'] = Field(description='Return the sentiment of the review')
#     pros: Optional[list[str]] = Field(description='Write down all the pros inside a list')
#     cons: Optional[list[str]] = Field(description='Write down all the cons inside a list')

json_schema = {
    "title" : "Review",
    "type" : 'object',
    'properties' : {
        'key_themes' : {      
            'type': 'array',
            'items': {
                'type' : 'string'
            },
            'description' : 'write down all the key themes discussed in the reivew in a list'
        }, 
        'summary' : {
            'type': 'string',
            'description': 'A brief summary of the reivew'
        },
        'sentiment' : {
            'type' : 'string',
            'enum' : ['pos', 'neg'],
            'description' : 'Return sentiment of the reivew either positive or negative'
        }
    },
    'required' : ['key_themes', 'summary', 'sentiment']
}
    
# structured_model = model.with_structured_output(Review)
structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""The Samsung Galaxy S24 Ultra is a powerhouse flagship that delivers on almost every front. Its camera system is incredibly versatile, capturing crisp and detailed photos in both bright and low-light conditions. The 200MP main sensor is especially impressive, making it one of the best smartphone cameras available. The 6.8-inch AMOLED display is vibrant, sharp, and super smooth with its 120Hz refresh rate. Performance-wise, the Snapdragon 8 Gen 3 chip ensures that everything from gaming to multitasking is lightning fast. Battery life easily lasts a full day, and the charging speed is decent, though not industry-leading. One of the standout features is the AI integration for real-time translation and photo editing, which genuinely adds value. The build quality is premium with a sleek, sturdy design. However, the phone is quite bulky and definitely not budget-friendly. Overall, it’s a top-tier device meant for those who want the absolute best Android experience """)

print(result)
