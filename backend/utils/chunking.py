from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Split cleaned text into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_text(text)

    return chunks