from utils.vector_store import VectorStore


class SemanticSearch:
    """
    Performs semantic search on the ChromaDB vector database.
    """

    def __init__(self, embedding_generator):
        """
        Initialize Semantic Search.
        """

        self.embedding_generator = embedding_generator
        self.vector_store = VectorStore()

    def search(self, query, top_k=3):
        """
        Search the vector database using semantic similarity.
        """

        # Generate embedding for the query
        query_embedding = self.embedding_generator.generate_embeddings([query])

        # Search ChromaDB
        results = self.vector_store.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=top_k
        )

        formatted_results = []

        if len(results["documents"][0]) == 0:
            return formatted_results

        for i in range(len(results["documents"][0])):

            formatted_results.append({

                "document": results["documents"][0][i],

                "source": results["metadatas"][0][i]["source"],

                "chunk": results["metadatas"][0][i]["chunk"],

                "distance": results["distances"][0][i]

            })

        return formatted_results