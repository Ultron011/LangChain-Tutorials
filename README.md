# 🦜⛓️ LangChain Tutorials

> **A comprehensive, hands-on collection of LangChain tutorials for building production-ready AI applications**

This repository provides a structured learning path through LangChain's ecosystem, from basic model integration to advanced AI agents. Each tutorial includes practical examples, real-world use cases, and best practices.

## 🎯 Quick Start

```bash
# Clone the repository
git clone https://github.com/Ultron011/LangChain-Tutorials.git
cd LangChain-Tutorials

# Install dependencies
pip install -r requirements.txt

# Set up your API keys in .env file
cp .env.example .env  # Add your API keys here
```

## 🗺️ Learning Path

| Phase | Topics | Duration | Prerequisites |
|-------|--------|----------|---------------|
| **🏗️ Foundation** | Models, Prompts, Output Control | 2-3 days | Python basics |
| **📄 Document AI** | Loading, Splitting, Vector Storage, Retrieval | 3-4 days | Foundation complete |
| **🤖 Advanced AI** | Tools, Agents, Complex Workflows | 2-3 days | Document AI complete |

## � Tutorial Modules

### 🏗️ **Foundation Phase**
*Master the core building blocks of LangChain applications*

<details>
<summary><strong>01 - 🧠 MODELS</strong> - Foundation models and integrations</summary>

- 🔤 **LLMs** - OpenAI GPT models for text generation
- 💬 **ChatModels** - Multi-provider conversational AI (OpenAI, Anthropic, Google, HuggingFace)
- 🔢 **EmbeddedModels** - Text embeddings for semantic search and similarity

**What you'll build:** Basic AI-powered text generation and embedding systems
</details>

<details>
<summary><strong>02 - 📝 PROMPTS</strong> - Prompt engineering mastery</summary>

- 🎯 **Chat Templates** - Dynamic, reusable prompt structures
- 💭 **Message Handling** - System, human, and AI message management
- 🤖 **Interactive Chatbots** - Conversational interfaces with memory

**What you'll build:** Sophisticated chatbots with context awareness
</details>

<details>
<summary><strong>03 - 📊 STRUCTURED OUTPUT</strong> - Schema-driven AI responses</summary>

- 🏗️ **Pydantic Models** - Type-safe data structures
- 📋 **TypedDict** - Python type hints for output validation
- 🔗 **JSON Schema** - Standardized data formats

**What you'll build:** AI systems that return consistent, validated data structures
</details>

<details>
<summary><strong>04 - 🔧 OUTPUT PARSERS</strong> - Format AI responses perfectly</summary>

- 📝 **String Parsers** - Clean text output processing
- ✅ **Pydantic Parsers** - Validated structured parsing
- 📄 **JSON Parsers** - Reliable JSON format handling

**What you'll build:** Robust parsing systems for any output format
</details>

<details>
<summary><strong>05 - ⛓️ CHAINS</strong> - Connect components into workflows</summary>

- 🔗 **Simple Chains** - Basic prompt-model-parser pipelines
- 📈 **Sequential Chains** - Multi-step processing workflows
- ⚡ **Parallel Chains** - Concurrent execution patterns
- 🔀 **Conditional Chains** - Logic-based workflow branching

**What you'll build:** Complex AI workflows with multiple processing steps
</details>

<details>
<summary><strong>06 - 🔩 RUNNABLES</strong> - Low-level component building</summary>

- 🔄 **Runnable Sequences** - Custom operation chaining
- ⚡ **Runnable Parallel** - Concurrent task execution
- ⚙️ **Runnable Lambda** - Custom function integration
- 📤 **Runnable Passthrough** - Advanced data flow control

**What you'll build:** Custom LangChain components and advanced pipelines
</details>

### 📄 **Document AI Phase**
*Transform documents into intelligent, searchable knowledge bases*

<details>
<summary><strong>07 - 📁 DOCUMENT LOADERS</strong> - Ingest any document format</summary>

- 📄 **Text Loaders** - Plain text and markdown files
- 📕 **PDF Loaders** - Extract content from PDFs
- 🌐 **Web Loaders** - Scrape and process web content
- 📂 **Directory Loaders** - Batch process document collections

**What you'll build:** Universal document ingestion systems
</details>

<details>
<summary><strong>08 - ✂️ TEXT SPLITTERS</strong> - Intelligent document chunking</summary>

- 📏 **Length-Based** - Character and token count splitting
- 🧠 **Semantic** - Meaning-aware text segmentation
- 📑 **Structure-Based** - Header and paragraph-aware splitting
- 📋 **Document-Aware** - Format-specific chunking strategies

**What you'll build:** Smart text processing that preserves context and meaning
</details>

<details>
<summary><strong>09 - 🗄️ VECTOR STORES</strong> - High-performance embedding storage</summary>

- 💾 **Chroma Integration** - Local vector database setup
- 📊 **Document Indexing** - Efficient embedding storage
- 🔍 **Similarity Search** - Lightning-fast relevant document retrieval

**What you'll build:** Scalable knowledge bases with semantic search
</details>

<details>
<summary><strong>10 - 🎯 RETRIEVERS</strong> - Advanced information retrieval</summary>

- 🔍 **Vector Store Retrievers** - Similarity-based document search
- 🔄 **Multi-Query** - Enhanced search with query expansion
- 🗜️ **Contextual Compression** - Relevant content extraction
- 🎯 **MMR Search** - Diverse, relevant result ranking
- 📚 **Wikipedia Integration** - External knowledge source access

**What you'll build:** Sophisticated search systems with multiple retrieval strategies
</details>

### 🤖 **Advanced AI Phase**
*Build autonomous AI systems that can think and act*

<details>
<summary><strong>11 - 🛠️ TOOLS</strong> - Extend AI with external capabilities</summary>

- 🔧 **Built-in Tools** - Web search, shell commands, system integration
- ⚙️ **Custom Tools** - Domain-specific function creation
- 🔗 **Tool Binding** - Seamless model-tool integration
- 🛡️ **Safe Execution** - Secure tool usage in AI workflows

**What you'll build:** AI assistants with real-world interaction capabilities
</details>

<details>
<summary><strong>12 - 🕵️ AGENTS</strong> - Autonomous reasoning and action</summary>

- 🧠 **ReAct Agents** - Reasoning and acting pattern implementation
- 🎮 **Agent Executors** - Controlled autonomous execution
- 🔄 **Multi-Step Reasoning** - Complex problem-solving workflows

**What you'll build:** Intelligent agents that can solve complex problems independently
</details>

## 🚀 Getting Started

### 📋 Prerequisites
- **Python 3.8+** with pip
- **API Keys** from your chosen providers:
  - 🔑 `OPENAI_API_KEY` - For OpenAI models (GPT-4, embeddings)
  - 🔑 `ANTHROPIC_API_KEY` - For Claude models  
  - 🔑 `GOOGLE_API_KEY` - For Gemini models
  - 🔑 `HUGGINGFACEHUB_API_TOKEN` - For HuggingFace models
  - 🔑 `GROQ_API_KEY` - For Groq models (optional)

### ⚡ Installation
```bash
# Essential LangChain packages
pip install langchain langchain-community langchain-core

# Provider-specific packages
pip install langchain-openai langchain-anthropic langchain-google-genai langchain-huggingface

# Additional utilities
pip install python-dotenv scikit-learn numpy chromadb
```

### 🎯 Choose Your Starting Point

| **🆕 New to LangChain?** | **📄 Building Document AI?** | **🤖 Creating AI Agents?** |
|-------------------------|------------------------------|----------------------------|
| Start with **01 - MODELS** | Jump to **07 - DOCUMENT LOADERS** | Begin at **11 - TOOLS** |
| Learn the fundamentals | Build knowledge systems | Create autonomous AI |

## 🎖️ What You'll Master

### 🏗️ **Core Skills**
- ✅ **Multi-Provider Integration** - Work with OpenAI, Anthropic, Google, HuggingFace seamlessly
- ✅ **Prompt Engineering** - Design effective prompts for any use case
- ✅ **Output Control** - Get structured, validated responses every time
- ✅ **Workflow Design** - Build complex, maintainable AI pipelines

### 📊 **Document Intelligence**
- ✅ **Universal Document Processing** - Handle PDFs, text, web content, and more
- ✅ **Smart Text Splitting** - Preserve context while chunking documents
- ✅ **Vector Search** - Build fast, semantic search systems
- ✅ **Advanced Retrieval** - Implement RAG with multiple search strategies

### 🤖 **AI Agent Development**
- ✅ **Tool Integration** - Connect AI to external APIs, databases, and systems
- ✅ **Agent Architecture** - Build reasoning agents that can plan and execute
- ✅ **Safe Execution** - Implement secure, controlled AI automation

## 🏆 Real-World Applications

Each tutorial prepares you to build production systems like:

- 🔍 **Intelligent Search Engines** - Vector-powered document search
- 💬 **Advanced Chatbots** - Context-aware conversational AI
- 📊 **Data Analysis Assistants** - AI that can query and analyze data
- 🤖 **Automation Agents** - AI that can perform complex tasks autonomously
- 📚 **Knowledge Management** - AI-powered document processing and Q&A

## �️ Suggested Learning Schedule

### Week 1: Foundation Building
- **Days 1-2:** Models & Prompts (01-02)
- **Days 3-4:** Structured Output & Parsers (03-04)  
- **Days 5-6:** Chains & Runnables (05-06)
- **Day 7:** Practice & Review

### Week 2: Document Intelligence
- **Days 1-2:** Document Loaders & Text Splitters (07-08)
- **Days 3-4:** Vector Stores & Retrievers (09-10)
- **Days 5-7:** Build Your First RAG System

### Week 3: Advanced AI Systems
- **Days 1-3:** Tools & Agent Development (11-12)
- **Days 4-7:** Capstone Project - Build a Complete AI Assistant

## 💡 Pro Tips

> **🎯 Learn by Building:** Each folder contains working examples. Run them, modify them, break them, and fix them!

> **🔍 Start Simple:** Master each concept before moving to the next. Complexity builds naturally.

> **🤝 Join the Community:** Share your projects and get help in LangChain community forums.

> **📚 Keep the Docs Handy:** Bookmark the [official LangChain documentation](https://python.langchain.com/) for reference.

## 🔄 Stay Updated

This repository evolves with the LangChain ecosystem. Watch this repo to get notifications about:
- 🆕 New tutorial modules
- 🔧 Framework updates and migrations  
- 💡 Best practice updates
- 🐛 Bug fixes and improvements

---

<div align="center">

**🌟 Ready to build the future of AI applications?**

[**🚀 Start with 01 - MODELS →**](./01%20-%20MODELS/)

*Made with ❤️ for the LangChain community*

</div>
