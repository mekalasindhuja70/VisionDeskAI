import chromadb
from chromadb.errors import IDAlreadyExistsError


class VectorStore:
    """
    Handles storing and retrieving document embeddings using ChromaDB.
    """

    def __init__(self):

        # Create/Open local database
        self.client = chromadb.PersistentClient(path="vector_db")

        # Create collection if it doesn't exist
        self.collection = self.client.get_or_create_collection(
            name="visiondesk_documents"
        )

        print("Connected to ChromaDB successfully!")

    # =====================================================
    # Check Duplicate Document
    # =====================================================

    def document_exists(self, filename):
        """
        Check whether a document already exists.
        """

        results = self.collection.get(
            where={"source": filename}
        )

        return len(results["ids"]) > 0

    # =====================================================
    # Store Document
    # =====================================================

    def add_document(self, filename, chunks, embeddings):
        """
        Store document chunks and embeddings.
        """

        ids = []
        metadatas = []

        for i in range(len(chunks)):

            ids.append(f"{filename}_{i}")

            metadatas.append({
                "source": filename,
                "chunk": i + 1,
                "chunk_length": len(chunks[i])
            })

        try:

            self.collection.add(
                ids=ids,
                documents=chunks,
                embeddings=embeddings.tolist(),
                metadatas=metadatas
            )

            print(f"✅ {filename} stored successfully!")

        except IDAlreadyExistsError:

            print(f"⚠️ {filename} already exists.")

    # =====================================================
    # Total Chunks
    # =====================================================

    def count_documents(self):
        """
        Returns total stored chunks.
        """

        return self.collection.count()

    # =====================================================
    # List Documents
    # =====================================================

    def list_documents(self):
        """
        Returns all uploaded documents.
        """

        results = self.collection.get()

        documents = {}

        if results["metadatas"] is None:
            return []

        for metadata in results["metadatas"]:

            filename = metadata["source"]

            if filename not in documents:

                documents[filename] = 0

            documents[filename] += 1

        output = []

        for filename, chunk_count in sorted(documents.items()):

            output.append({

                "filename": filename,

                "chunks": chunk_count

            })

        return output

    # =====================================================
    # Delete Document
    # =====================================================

    def delete_document(self, filename):
        """
        Delete a document from ChromaDB.
        """

        self.collection.delete(
            where={
                "source": filename
            }
        )

        print(f"🗑 Deleted {filename}")

    # =====================================================
    # Clear Knowledge Base
    # =====================================================

    def clear_database(self):
        """
        Deletes every stored vector.
        """

        results = self.collection.get()

        if results["ids"]:

            self.collection.delete(
                ids=results["ids"]
            )

            print("Knowledge Base Cleared.")

    # =====================================================
    # Statistics
    # =====================================================

    def get_statistics(self):
        """
        Returns Knowledge Base statistics.
        """

        documents = self.list_documents()

        stats = {

            "documents": len(documents),

            "chunks": self.count_documents(),

            "document_names": documents

        }

        return stats