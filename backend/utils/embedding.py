from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """
    Generates vector embeddings using Sentence Transformers.
    """

    def __init__(self):
        print("Loading embedding model...")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("Embedding model loaded successfully!")

    def generate_embeddings(self, chunks):
        """
        Generate embeddings for a list of text chunks.

        Args:
            chunks (list): List of text chunks

        Returns:
            list: Embedding vectors
        """

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True
        )

        return embeddings