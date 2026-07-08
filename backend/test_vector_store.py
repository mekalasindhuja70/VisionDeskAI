from utils.embedding import EmbeddingGenerator
from utils.vector_store import VectorStore

chunks = [
    "Workers must wear helmets.",
    "Emergency exits must remain clear."
]

generator = EmbeddingGenerator()

embeddings = generator.generate_embeddings(chunks)

db = VectorStore()

db.add_document(
    "Safety_Manual.txt",
    chunks,
    embeddings
)

print("Total Chunks in DB:", db.count_documents())