import faiss
import pickle
import os

from sentence_transformers import SentenceTransformer


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


VECTOR_PATH = os.path.join(
    BASE_DIR,
    "vector_db",
    "faiss.index"
)


DOC_PATH = os.path.join(
    BASE_DIR,
    "vector_db",
    "documents.pkl"
)



model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



print("Loading FAISS index from:", VECTOR_PATH)


index = faiss.read_index(
    VECTOR_PATH
)



with open(
    DOC_PATH,
    "rb"
) as f:

    documents = pickle.load(f)



print("Vector database loaded successfully")
print("Documents:", len(documents))



def retrieve(query, k=3):


    query_embedding = model.encode(
        [query]
    )


    distances, indices = index.search(
        query_embedding,
        k
    )


    results=[]


    for i in indices[0]:

        if i < len(documents):

            results.append(
                documents[i]
            )


    return "\n\n".join(results)