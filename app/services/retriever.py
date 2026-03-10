from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection(name="knowledge_base")


def retrieve_context(query):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    context = ""

    # Safety check if DB is empty
    if "documents" not in results or len(results["documents"]) == 0:
        return "No additional context available."

    docs = results["documents"][0]

    for doc in docs:
        context += doc + "\n"

    return context