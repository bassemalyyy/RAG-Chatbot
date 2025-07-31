This repository includes two tools for building and interacting with a Retrieval-Augmented Generation (RAG) system over PDF documents using [LlamaIndex](https://www.llamaindex.ai/):

- `simple-rag.ipynb`: A notebook version for development and exploration.

- `simple_rag_streamlit.py`: A user-friendly Streamlit app for real-time PDF upload, indexing, and querying.

---

## 📂 Features

✅ Upload and parse any PDF  

✅ Index content using OpenAI embeddings  

✅ Query indexed content via natural language  

✅ Streamlit version shows live indexing status  

✅ Uses LlamaIndex for vector storage and retrieval

---

## 🔧 Requirements

Install dependencies via pip:

```bash

pip install streamlit llama-index openai
```

🚀 Usage

🔬 Notebook Version

```bash

jupyter notebook simple-rag.ipynb
```

Modify the path to your desired PDF.

Run cells to index and interact.

🌐 Streamlit App

```bash

streamlit run simple-rag-streamlit.py
```

Upload a PDF file.

Wait for the indexing progress.

Enter your query and receive an AI-generated answer.


🧠 Credits

Built using:

LlamaIndex

Streamlit

Ollama
