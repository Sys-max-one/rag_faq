Retrieval-Augmented Generation (RAG) pipeline using FAQ PDF documents and AWS Bedrock for the LLM inference

---

# HR Policy Document Q\&A using Embeddings and AWS Bedrock

This project demonstrates a simple yet powerful pipeline to perform question-answering on HR policy documents using embeddings and Amazon Bedrock's Claude foundation model. It loads a PDF, splits it into manageable chunks, creates vector embeddings, and then enables natural language querying over the data.

## Project Workflow

1. **📄 Load PDF Data**

   * Uses `PDFLoader` to extract and load raw text from HR policy documents.

2. **✂️ Text Splitting**

   * The raw text is split into manageable chunks using recursive character-based text splitting for optimal embedding and retrieval performance.

3. **🧠 Generate Embeddings**

   * Text chunks are embedded using a client-connected embedding service (e.g., OpenAI, Cohere, HuggingFace).

4. **🏪 Store Embeddings in Vector Database**

   * Embeddings are stored using `VectorstoreIndexCreator` to enable semantic search over the document content.

5. **📚 Index HR Policy Document**

   * The processed HR document is indexed into a searchable vector store to enable fast retrieval of relevant text chunks.

6. **🤖 LLM Connection via Bedrock**

   * Amazon Bedrock's Claude foundation model is used to generate answers using retrieved documents and user prompts.

7. **🔍 Search + Prompt Completion**

   * The user prompt is semantically matched against the indexed document. Relevant chunks are retrieved and passed with the prompt to the Claude model for intelligent response generation.

## Tech Stack

* Python
* LangChain
* Amazon Bedrock (Claude Model)
* VectorstoreIndexCreator (e.g., FAISS, Chroma)
* Embedding provider (e.g., OpenAI, Cohere)
* PDFLoader

## Example Use Case

> User prompt: “How many vacation days are allowed per year?”

✅ The system retrieves the relevant section from the HR policy document and passes it with the prompt to the Claude LLM, which responds with a concise, accurate answer.
