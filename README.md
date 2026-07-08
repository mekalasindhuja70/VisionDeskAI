# 📚 VisionDesk AI

> AI-Powered Enterprise Knowledge Base using Semantic Search and ChromaDB

VisionDesk AI is an intelligent document management system that enables users to upload documents, automatically generate embeddings, store them in a vector database, and perform semantic search using natural language queries.

Instead of traditional keyword search, VisionDesk AI understands the meaning of the user's query and retrieves the most relevant information from uploaded documents.

---

# Features

- Upload PDF, DOCX and TXT documents
- Automatic text extraction
- Text cleaning and preprocessing
- Intelligent document chunking
- SentenceTransformer embeddings
- ChromaDB vector database
- Semantic Search
- Duplicate document detection
- Knowledge Base Management
- Delete individual documents
- Clear entire Knowledge Base
- Professional Responsive UI
- Fast Retrieval

---

# Tech Stack

## Backend

- Python 3.10+
- Flask

## AI

- Sentence Transformers
- all-MiniLM-L6-v2

## Vector Database

- ChromaDB

## Frontend

- HTML5
- CSS3
- JavaScript
- Font Awesome

## Document Processing

- PyPDF2
- python-docx

---

# Project Structure

```
VisionDeskAI/
│
├── app.py
│
├── uploads/
│
├── extracted_text/
│
├── vector_db/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── search_result.html
│   └── documents.html
│
├── static/
│   └── css/
│       └── style.css
│
├── utils/
│   ├── chunking.py
│   ├── embedding.py
│   ├── file_validator.py
│   ├── search.py
│   ├── text_cleaner.py
│   ├── text_extractor.py
│   └── vector_store.py
│
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/VisionDeskAI.git

cd VisionDeskAI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Packages

```text
Flask
chromadb
sentence-transformers
PyPDF2
python-docx
numpy
torch
transformers
```

---

# Run Application

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

# Workflow

## Step 1

Upload a document.

Supported files

- PDF
- DOCX
- TXT

---

## Step 2

The application automatically

- validates file
- extracts text
- cleans text
- splits text into chunks

---

## Step 3

Embeddings are generated using

```
all-MiniLM-L6-v2
```

---

## Step 4

Embeddings are stored inside

```
ChromaDB
```

Each chunk stores

- source filename
- chunk number
- embedding vector

---

## Step 5

User asks a question

Example

```
Where must employees wear helmets?
```

---

## Step 6

Semantic Search converts the question into an embedding.

---

## Step 7

ChromaDB retrieves the most relevant chunks.

---

## Step 8

The results are displayed with

- Source Document
- Chunk Number
- Similarity Distance
- Retrieved Text

---

# Knowledge Base

The Knowledge Base page allows users to

- View uploaded documents
- View chunk count
- Delete documents
- Clear the complete Knowledge Base

---

# Semantic Search Example

Uploaded Documents

```
Safety_Manual.pdf

PPE_Guidelines.pdf

Fire_Safety.pdf
```

User Query

```
What happens if PPE is damaged?
```

Returned Result

```
Damaged PPE should be replaced immediately.
```

---

# Supported Document Types

| Format | Supported |
|---------|-----------|
| PDF | Yes |
| DOCX | Yes |
| TXT | Yes |

---

# AI Pipeline

```
User Upload
      │
      ▼
Text Extraction
      │
      ▼
Text Cleaning
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB Storage
      │
      ▼
Semantic Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Display Results
```

---

# Folder Description

## uploads/

Stores uploaded documents.

---

## extracted_text/

Stores cleaned extracted text.

---

## vector_db/

Stores ChromaDB vector database.

---

## templates/

HTML pages.

---

## static/

CSS and UI assets.

---

## utils/

Contains all backend modules.

---

# Future Enhancements

- RAG (Retrieval-Augmented Generation)
- Gemini API Integration
- Llama 3 Integration
- AI Chatbot
- OCR Support
- Image Search
- Voice Search
- Multi-user Authentication
- Admin Dashboard
- Upload Progress Indicator
- Search History
- Role-Based Access Control
- Document Versioning

---

# Advantages

- Faster than keyword search
- Understands user intent
- Handles multiple document types
- Scalable architecture
- Easy to maintain
- Enterprise-ready design

---

# Screenshots

Add screenshots here

- Dashboard
- Upload Page
- Search Results
- Knowledge Base

---

# Author

**Sindhuja Mekala**

BE – Electronics & Communication Engineering

Stanley College of Engineering & Technology for Women

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

- Flask
- ChromaDB
- Hugging Face
- Sentence Transformers
- Font Awesome