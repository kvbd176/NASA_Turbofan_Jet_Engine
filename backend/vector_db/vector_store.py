import faiss
import pickle
import os

from embeddings import EmbeddingGenerator



BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


INDEX_PATH = os.path.join(
    BASE_DIR,
    "vector_db",
    "faiss.index"
)


DOC_PATH = os.path.join(
    BASE_DIR,
    "vector_db",
    "documents.pkl"
)



def create_vector_store():


    generator = EmbeddingGenerator()


    documents, embeddings = generator.generate_embeddings()


    print(
        "Creating FAISS index..."
    )


    dimension = embeddings.shape[1]


    index = faiss.IndexFlatL2(
        dimension
    )


    index.add(
        embeddings
    )


    print(
        "Total vectors:",
        index.ntotal
    )


    faiss.write_index(
        index,
        INDEX_PATH
    )


    with open(
        DOC_PATH,
        "wb"
    ) as f:

        pickle.dump(
            documents,
            f
        )


    print("FAISS saved successfully")



if __name__ == "__main__":

    create_vector_store()