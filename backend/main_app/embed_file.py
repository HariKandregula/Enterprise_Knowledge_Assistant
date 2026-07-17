import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


def get_model_and_chroma_collection():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(path="./chroma_db")

    collection_name = "enterprise_docs"

    collection = client.get_or_create_collection(collection_name)
    return model, collection


def get_document(prompt):
    model, collection = get_model_and_chroma_collection()

    query_embedding = model.encode(
    prompt,
    convert_to_numpy=True,
    normalize_embeddings=True
    )

    try:
        results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
        )
        result = results["documents"][0][0]
        return result
    except:
        return ""


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

    model, collection = get_model_and_chroma_collection()

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

