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

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- API keys for respective providers (OpenAI, Anthropic, Google, HuggingFace)

### Installation
```bash
pip install langchain langchain-openai langchain-anthropic langchain-google-genai langchain-huggingface python-dotenv scikit-learn numpy
```

## 🔧 What You'll Learn

**Models & Integration**
- Connect with multiple AI providers (OpenAI, Anthropic, Google, HuggingFace)
- Implement both API-based and locally hosted models
- Generate and compare text embeddings for semantic search

**Prompt Engineering**
- Design effective prompt templates for different use cases
- Manage conversation history and context
- Build interactive chatbot interfaces

**Data Structure & Parsing**
- Generate structured outputs with schema validation
- Parse model outputs into specific data formats
- Handle JSON, Pydantic models, and custom data structures

**Workflow Orchestration**
- Build complex multi-step processing chains
- Implement parallel and conditional execution patterns
- Create custom components with Runnable interfaces

**Best Practices**
- Structure LangChain applications for scalability
- Handle different message types and conversation flows
- Optimize performance with parallel processing

## 📚 Tutorial Progression

The tutorials are organized in a logical learning sequence:

1. **Models** - Start with basic model integration and usage patterns
2. **Prompts** - Learn effective prompt engineering and conversation management
3. **Structured Output** - Generate and validate structured data from models
4. **Output Parsers** - Parse and format model outputs into specific structures
5. **Chains** - Build complex workflows by connecting multiple components
6. **Runnables** - Master low-level building blocks for custom implementations

Each section contains practical examples that build upon previous concepts. Follow the numbered folders for the optimal learning experience.

## 🔄 Continuous Updates

This repository is actively maintained and updated with new tutorials and examples. Each commit adds new functionality while maintaining existing examples for reference.

---

*Last Updated: August 2025*
