import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer



DOCUMENT_PATH = "rag/documents/engine_reports.txt"

VECTOR_PATH = "vector_db/faiss_index"

METADATA_PATH = "vector_db/metadata.pkl"



model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



def create_embeddings():


    with open(
        DOCUMENT_PATH,
        "r"
    ) as f:

        text = f.read()



    documents = text.split("\n\n")


    print(
        "Documents loaded:",
        len(documents)
    )


    embeddings = model.encode(
        documents,
        show_progress_bar=True
    )


    dimension = embeddings.shape[1]


    index = faiss.IndexFlatL2(
        dimension
    )


    index.add(
        embeddings
    )


    os.makedirs(
        "vector_db",
        exist_ok=True
    )


    faiss.write_index(
        index,
        VECTOR_PATH
    )


    with open(
        METADATA_PATH,
        "wb"
    ) as f:

        pickle.dump(
            documents,
            f
        )


    print("FAISS database created")



if __name__=="__main__":

    create_embeddings()