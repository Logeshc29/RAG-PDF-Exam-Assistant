from langchain.vectorstores import FAISS

def create_vector_store(docs, embeddings):

    vector_store = FAISS.from_documents(
        docs,
        embeddings
    )

    return vector_store
