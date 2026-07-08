from flask import Flask, render_template, request, redirect
import os

from utils.text_extractor import extract_text
from utils.text_cleaner import clean_text
from utils.chunking import split_text
from utils.embedding import EmbeddingGenerator
from utils.vector_store import VectorStore
from utils.search import SemanticSearch
from utils.file_validator import validate_file

app = Flask(__name__)

# =====================================================
# Flask Configuration
# =====================================================

UPLOAD_FOLDER = "uploads"
EXTRACTED_FOLDER = "extracted_text"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["EXTRACTED_FOLDER"] = EXTRACTED_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXTRACTED_FOLDER, exist_ok=True)

# =====================================================
# Load AI Components
# =====================================================

print("=" * 60)
print("Loading VisionDesk AI Components...")
print("=" * 60)

embedding_generator = EmbeddingGenerator()

vector_store = VectorStore()

search_engine = SemanticSearch(embedding_generator)

print("=" * 60)
print("VisionDesk AI is Ready!")
print("=" * 60)

# =====================================================
# Home
# =====================================================

@app.route("/")
def home():

    return render_template("index.html")


# =====================================================
# Upload
# =====================================================

@app.route("/upload", methods=["POST"])
def upload():

    if "document" not in request.files:

        return render_template(
            "result.html",
            filename="",
            chunk_count=0,
            vector_count=vector_store.count_documents(),
            chunks=[],
            message="❌ No file selected."
        )

    file = request.files["document"]

    is_valid, validation_message = validate_file(file)

    if not is_valid:

        return render_template(
            "result.html",
            filename="",
            chunk_count=0,
            vector_count=vector_store.count_documents(),
            chunks=[],
            message=f"❌ {validation_message}"
        )

    if vector_store.document_exists(file.filename):

        return render_template(
            "result.html",
            filename=file.filename,
            chunk_count=0,
            vector_count=vector_store.count_documents(),
            chunks=[],
            message=f"⚠️ '{file.filename}' already exists."
        )

    print(f"\nUploading : {file.filename}")

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    try:

        extracted_text = extract_text(filepath)

    except Exception as e:

        return render_template(
            "result.html",
            filename=file.filename,
            chunk_count=0,
            vector_count=vector_store.count_documents(),
            chunks=[],
            message=f"❌ {e}"
        )

    cleaned_text = clean_text(extracted_text)

    cleaned_filename = (
        os.path.splitext(file.filename)[0]
        + "_cleaned.txt"
    )

    cleaned_path = os.path.join(
        app.config["EXTRACTED_FOLDER"],
        cleaned_filename
    )

    with open(cleaned_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    chunks = split_text(cleaned_text)

    if len(chunks) == 0:

        return render_template(
            "result.html",
            filename=file.filename,
            chunk_count=0,
            vector_count=vector_store.count_documents(),
            chunks=[],
            message="❌ No text extracted."
        )

    print(f"Chunks : {len(chunks)}")

    embeddings = embedding_generator.generate_embeddings(chunks)

    print("Embeddings Generated")

    vector_store.add_document(
        file.filename,
        chunks,
        embeddings
    )

    print("Stored Successfully")

    return render_template(
        "result.html",
        filename=file.filename,
        chunk_count=len(chunks),
        vector_count=vector_store.count_documents(),
        chunks=chunks,
        message="✅ Document uploaded successfully!"
    )


# =====================================================
# Semantic Search
# =====================================================

@app.route("/search", methods=["POST"])
def search():

    query = request.form.get("query", "").strip()

    if query == "":

        return render_template(
            "search_result.html",
            query="",
            results=[],
            message="Please enter a query."
        )

    print(f"\nSearching : {query}")

    results = search_engine.search(query)

    if results is None:
        results = []

    print(f"Results : {len(results)}")

    return render_template(
        "search_result.html",
        query=query,
        results=results,
        message=""
    )


# =====================================================
# Knowledge Base
# =====================================================

@app.route("/documents")
def documents():

    stats = vector_store.get_statistics()

    return render_template(
        "documents.html",
        documents=stats["document_names"],
        total_documents=stats["documents"],
        total_chunks=stats["chunks"]
    )


# =====================================================
# Delete Document
# =====================================================

@app.route("/delete/<filename>")
def delete_document(filename):

    print(f"Deleting : {filename}")

    vector_store.delete_document(filename)

    upload_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    if os.path.exists(upload_path):
        os.remove(upload_path)

    cleaned_path = os.path.join(
        app.config["EXTRACTED_FOLDER"],
        os.path.splitext(filename)[0] + "_cleaned.txt"
    )

    if os.path.exists(cleaned_path):
        os.remove(cleaned_path)

    return redirect("/documents")


# =====================================================
# Clear Knowledge Base
# =====================================================

@app.route("/clear")
def clear_database():

    vector_store.clear_database()

    for file in os.listdir(app.config["UPLOAD_FOLDER"]):

        os.remove(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                file
            )
        )

    for file in os.listdir(app.config["EXTRACTED_FOLDER"]):

        os.remove(
            os.path.join(
                app.config["EXTRACTED_FOLDER"],
                file
            )
        )

    print("Knowledge Base Cleared")

    return redirect("/documents")


# =====================================================
# Run Flask
# =====================================================

if __name__ == "__main__":

    app.run(debug=True)