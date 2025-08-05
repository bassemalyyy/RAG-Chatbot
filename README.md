Simple RAG System for PDF Documents
===================================

Welcome to the **Simple RAG System** repository! This project provides two tools to build and interact with a Retrieval-Augmented Generation (RAG) system for PDF documents using [LlamaIndex](https://www.llamaindex.ai/). Explore and query your PDFs with ease using either a Jupyter Notebook for development or a user-friendly Streamlit app for real-time interaction.

* * * * *

📂 Features
-----------

-   ✅ **Upload and Parse PDFs**: Process any PDF document for indexing and querying.
-   ✅ **Ollama Embeddings**: Leverage powerful embeddings for accurate content retrieval.
-   ✅ **Natural Language Queries**: Ask questions in plain language and get AI-generated answers.
-   ✅ **Live Indexing Status**: Streamlit app displays real-time indexing progress.
-   ✅ **LlamaIndex-Powered**: Utilizes LlamaIndex for efficient vector storage and retrieval.

* * * * *

🔧 Requirements
---------------

To get started, install the required dependencies using pip:

```bash
pip install streamlit llama-index llama-index-llms-ollama llama-index-embeddings-ollama
```

* * * * *

🚀 Usage
--------

This repository includes two tools for interacting with the RAG system:

### 🔬 Notebook Version (`simple-rag.ipynb`)

Ideal for development, experimentation, and step-by-step exploration.

1.  Launch the notebook:

    ```bash
    jupyter notebook simple-rag.ipynb
    ```

2.  Update the PDF file path in the notebook to point to your desired document.
3.  Run the cells to index the PDF and interact with the RAG system via queries.

### 🌐 Streamlit App (`simple-rag-streamlit.py`)

A user-friendly interface for real-time PDF processing and querying.

1.  Run the Streamlit app:

    ```bash
    streamlit run simple-rag-streamlit.py
    ```

2.  Upload a PDF file through the web interface.
3.  Monitor the indexing progress in real-time.
4.  Enter a query in natural language and receive an AI-generated response.

* * * * *

🧠 Credits
----------

This project is built using the following technologies:

-   [LlamaIndex](https://www.llamaindex.ai/): For vector storage and retrieval.
-   [Streamlit](https://streamlit.io/): For the interactive web interface.
-   [Ollama](https://ollama.com/): For LLM and Embedding models.
