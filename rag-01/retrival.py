from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings


embedder = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key = "AIzaSyA5LmAgRh24Wg4c1M0u8hYFaSU1hD_8kik"
)

retrival = QdrantVectorStore.from_existing_collection(
    embedding=embedder,
    collection_name="my_documents",
    url="http://localhost:6333",
)


search_result = retrival.similarity_search(
    query = "what OSI stands for?"
)


print(f"Relevent chuncks - {search_result}")