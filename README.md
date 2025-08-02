# LangChain Tutorials

A comprehensive collection of LangChain tutorials covering various aspects of building AI applications. This repository demonstrates practical implementations and design patterns using the LangChain framework.

## 📁 Repository Structure

### 01 - MODELS
Foundation models and their implementations in LangChain.

- **LLMs** - Basic large language model implementations using OpenAI GPT models
- **ChatModels** - Conversational AI implementations across multiple providers (OpenAI, Anthropic, Google, HuggingFace)
- **EmbeddedModels** - Text embedding examples for semantic search and document similarity

### 02 - PROMPTS
Prompt engineering and template management for better AI interactions.

- **Chat Templates** - Structured prompt templates for conversational models
- **Message Handling** - System, human, and AI message management
- **Interactive Chatbots** - Building conversational interfaces with memory

### 03 - STRUCTURED OUTPUT
Generate structured data from language models with schema validation.

- **Pydantic Models** - Define and validate structured output schemas
- **TypedDict** - Use Python type hints for output structure
- **JSON Schema** - Schema-based structured output generation

### 04 - OUTPUT PARSERS
Parse and format model outputs into specific data structures.

- **String Parsers** - Basic text output parsing
- **Pydantic Parsers** - Structured output parsing with validation
- **JSON Parsers** - JSON format output handling

### 05 - CHAINS
Build complex workflows by connecting multiple components.

- **Simple Chains** - Basic prompt-model-parser chains
- **Sequential Chains** - Multi-step processing workflows
- **Parallel Chains** - Concurrent execution patterns
- **Conditional Chains** - Logic-based chain branching

### 06 - RUNNABLES
Low-level building blocks for creating custom LangChain components.

- **Runnable Sequences** - Chain multiple operations together
- **Runnable Parallel** - Execute operations concurrently
- **Runnable Lambda** - Custom function integration
- **Runnable Passthrough** - Data flow control patterns

### 07 - DOCUMENT LOADERS
Load and process documents from various sources for AI applications.

- **Text Loaders** - Load plain text files and documents
- **PDF Loaders** - Extract content from PDF documents
- **Web Loaders** - Load content from web pages
- **Directory Loaders** - Batch process multiple documents

### 08 - TEXT SPLITTERS
Split large documents into manageable chunks for processing.

- **Length-Based Splitting** - Split text by character or token count
- **Semantic Splitting** - Split based on meaning and context
- **Structure-Based Splitting** - Split by document structure (headers, paragraphs)
- **Document-Aware Splitting** - Format-specific splitting strategies

### 09 - VECTOR STORES
Store and manage document embeddings for efficient retrieval.

- **Chroma Integration** - Local vector database implementation
- **Document Storage** - Store and index document embeddings
- **Similarity Search** - Find relevant documents using vector similarity

### 10 - RETRIEVERS
Advanced retrieval strategies for finding relevant information.

- **Vector Store Retrievers** - Basic similarity-based retrieval
- **Multi-Query Retrievers** - Generate multiple search queries
- **Contextual Compression** - Compress retrieved content for relevance
- **MMR Search** - Maximum marginal relevance search strategies
- **Wikipedia Retrievers** - Search external knowledge sources

### 11 - TOOLS
Extend AI capabilities with external tools and functions.

- **Built-in Tools** - Web search, shell commands, and system tools
- **Custom Tools** - Create domain-specific tools and functions
- **Tool Binding** - Connect tools to language models
- **Tool Execution** - Execute tools safely within AI workflows

### 12 - AGENTS
Autonomous AI systems that can reason and take actions.

- **ReAct Agents** - Reasoning and acting pattern implementation
- **Agent Executors** - Manage agent execution and tool usage
- **Multi-Step Reasoning** - Complex problem-solving with tools

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- API keys for respective providers (OpenAI, Anthropic, Google, HuggingFace)

### Installation
```bash
pip install langchain langchain-openai langchain-anthropic langchain-google-genai langchain-huggingface python-dotenv scikit-learn numpy
```

## 🔧 What You'll Learn

**Foundation & Integration**
- Connect with multiple AI providers (OpenAI, Anthropic, Google, HuggingFace)
- Implement both API-based and locally hosted models
- Generate and compare text embeddings for semantic search

**Prompt Engineering & Output Control**
- Design effective prompt templates for different use cases
- Generate structured outputs with schema validation
- Parse and format model outputs into specific data structures

**Document Processing & Retrieval**
- Load and process documents from various sources (text, PDF, web)
- Split large documents into manageable chunks
- Store embeddings in vector databases for efficient retrieval
- Implement advanced retrieval strategies (MMR, multi-query, compression)

**Workflow Orchestration**
- Build complex multi-step processing chains
- Implement parallel and conditional execution patterns
- Create custom components with Runnable interfaces

**Advanced AI Systems**
- Extend AI capabilities with external tools and functions
- Build autonomous agents that can reason and take actions
- Implement safe tool execution within AI workflows

**Best Practices**
- Structure LangChain applications for scalability
- Optimize performance with parallel processing
- Handle different data sources and formats efficiently

## 📚 Tutorial Progression

The tutorials are organized in a logical learning sequence:

**Foundation (01-06)**
1. **Models** - Start with basic model integration and usage patterns
2. **Prompts** - Learn effective prompt engineering and conversation management
3. **Structured Output** - Generate and validate structured data from models
4. **Output Parsers** - Parse and format model outputs into specific structures
5. **Chains** - Build complex workflows by connecting multiple components
6. **Runnables** - Master low-level building blocks for custom implementations

**Document Processing & Retrieval (07-10)**
7. **Document Loaders** - Load and process documents from various sources
8. **Text Splitters** - Split large documents into manageable chunks
9. **Vector Stores** - Store and manage document embeddings efficiently
10. **Retrievers** - Implement advanced retrieval strategies for finding relevant information

**Advanced AI Systems (11-12)**
11. **Tools** - Extend AI capabilities with external tools and functions
12. **Agents** - Build autonomous AI systems that can reason and take actions

Each section contains practical examples that build upon previous concepts. Follow the numbered folders for the optimal learning experience.

## 🔄 Continuous Updates

This repository is actively maintained and updated with new tutorials and examples. Each commit adds new functionality while maintaining existing examples for reference.

---

*Last Updated: August 2025*
