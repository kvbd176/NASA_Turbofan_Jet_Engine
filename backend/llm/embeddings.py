import pandas as pd
import os
import pickle

import faiss

from sentence_transformers import SentenceTransformer



CSV_PATH = "data/outputs/final_output.csv"

VECTOR_PATH = "vector_store/engine.index"

TEXT_PATH = "vector_store/engine_text.pkl"



class EngineEmbedding:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def create_documents(self):

        df = pd.read_csv(CSV_PATH)


        documents=[]


        for _,row in df.iterrows():

            text=f"""
            Engine ID: {row['engine_id']}

            Cycle: {row['cycle']}

            Sensor2: {row['sensor2']}
            Sensor3: {row['sensor3']}
            Sensor4: {row['sensor4']}

            Health Status:
            {row.get('health_status','Unknown')}

            Remaining Useful Life:
            {row.get('RUL','Unknown')}
            """

            documents.append(text)


        return documents



    def create_embeddings(self):

        documents=self.create_documents()


        embeddings=self.model.encode(
            documents,
            show_progress_bar=True
        )


        embeddings=embeddings.astype("float32")


        dimension=embeddings.shape[1]


        index=faiss.IndexFlatL2(
            dimension
        )


        index.add(
            embeddings
        )


        os.makedirs(
            "vector_store",
            exist_ok=True
        )


        faiss.write_index(
            index,
            VECTOR_PATH
        )


        with open(TEXT_PATH,"wb") as f:

            pickle.dump(
                documents,
                f
            )


        return {

            "status":"success",

            "vectors_created":len(documents)

        }



if __name__=="__main__":


    engine=EngineEmbedding()


    result=engine.create_embeddings()


    print(result)