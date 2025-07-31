import streamlit as st
import tempfile
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import SimpleNodeParser

# Set up Streamlit page
st.set_page_config(page_title="RAG PDF Chatbot", layout="wide")
st.title("📄💬 RAG PDF Chatbot")
st.write("Upload a PDF, let it index, then ask questions!")

# State to store index and documents
if "index" not in st.session_state:
    st.session_state.index = None
    st.session_state.documents = None

# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

# Helper to process PDF and build vector index
def process_pdf_and_index(pdf_path):
    with st.spinner("🔄 Indexing your PDF..."):
        # Load document
        reader = SimpleDirectoryReader(input_files=[pdf_path])
        documents = reader.load_data()

        # Split and embed
        parser = SimpleNodeParser()
        nodes = parser.get_nodes_from_documents(documents)

        Settings.llm = Ollama(model="llama3.2", temperature=0, context_window=4096, request_timeout=60.0)
        Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

        index = VectorStoreIndex(nodes)
        return index, documents

# Handle PDF upload
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    # Build the vector store
    st.write("⏳ Starting indexing...")
    st.session_state.index, st.session_state.documents = process_pdf_and_index(tmp_file_path)
    st.success("✅ Indexing complete! You can now enter your query below.")

# Query input and response
if st.session_state.index:
    query = st.text_input("💬 Enter your query:")
    if query:
        with st.spinner("🔍 Searching..."):
            query_engine = st.session_state.index.as_query_engine()
            response = query_engine.query(query)
            st.markdown(f"**Answer:** {response}")