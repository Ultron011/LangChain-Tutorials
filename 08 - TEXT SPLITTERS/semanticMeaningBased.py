from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize embeddings model
embeddings_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# Load text file
loader = TextLoader('./sampleText.txt')
docs = loader.load()

# Initialize semantic splitter
splitter = SemanticChunker(
    embeddings_model,
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1
)

# Use the splitter
result = splitter.create_documents([docs[0].page_content])

# Print result
print(len(result))
for chunk in result:
    print(chunk.page_content)
