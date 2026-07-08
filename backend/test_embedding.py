from utils.embedding import EmbeddingGenerator

generator = EmbeddingGenerator()

chunks = [
    "Workers must wear helmets.",
    "Emergency exits must remain clear."
]

embeddings = generator.generate_embeddings(chunks)

print(type(embeddings))
print(embeddings.shape)
print(embeddings[0][:10])