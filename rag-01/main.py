# https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfloader
# https://docs.langchain.com/oss/python/integrations/splitters
# https://docs.langchain.com/oss/python/integrations/text_embedding/google_generative_ai
# https://aistudio.google.com/app/
# https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant

from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


file_path = Path(__file__).parent / "OSI_TP-IP-Model.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()
#print(docs)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = text_splitter.split_documents(docs)

print(f"Docs - {len(docs)}")
print(f"Splits - {len(split_docs)}")

embedder = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key = "AIzaSyA5LmAgRh24Wg4c1M0u8hYFaSU1hD_8kik"
)


vector = embedder.embed_query("hello, world!")
# print(vector)


vector_store = QdrantVectorStore.from_documents(
    documents=[],
    embedding=embedder,
    collection_name="my_documents",
    url="http://localhost:6333",
)

vector_store.add_documents(documents=split_docs)
print("Injection done - vector embeddings stored into DB")
