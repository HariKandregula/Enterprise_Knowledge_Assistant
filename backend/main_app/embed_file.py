import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from sentence_transformers import SentenceTransformer

def process_file(filename):
    loader = PyPDFLoader(filename)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    text_chunks = []
    for chunk in chunks:
        text_chunks.append(chunk.page_content)

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(path="./chroma_db")

    collection_name = "enterprise_docs"

    # Delete the collection if it already exists (optional)
    try:
        client.delete_collection(collection_name)
        print("Existing collection deleted.")
    except:
        pass

    collection = client.create_collection(name=collection_name)

    embeddings = model.encode(
    text_chunks,
    convert_to_numpy=True,
    normalize_embeddings=True
    )

    collection.add(
        ids=ids,
        documents=text_chunks,
        embeddings=embeddings.tolist(),
    )

    query = "Can I work from home?"

    query_embedding = model.encode(
    query,
    convert_to_numpy=True,
    normalize_embeddings=True
    )

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    return results["documents"]

