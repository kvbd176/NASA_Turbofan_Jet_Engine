from sentence_transformers import SentenceTransformer
import pandas as pd
import os


class EmbeddingGenerator:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def load_engine_data(self):

        path = "data/outputs/final_output.csv"

        df = pd.read_csv(path)

        return df



    def create_documents(self):

        df = self.load_engine_data()

        documents = []

        for _, row in df.iterrows():

            text = f"""
            Engine ID: {row['engine_id']}
            Cycle: {row['cycle']}

            Sensor values:
            sensor2: {row['sensor2']}
            sensor3: {row['sensor3']}
            sensor4: {row['sensor4']}

            RUL:
            {row['RUL']}

            Engine health status:
            {row.get('health_status','unknown')}
            """

            documents.append(text)


        return documents



    def generate_embeddings(self):

        documents = self.create_documents()

        embeddings = self.model.encode(
            documents,
            show_progress_bar=True
        )

        return documents, embeddings



if __name__ == "__main__":

    generator = EmbeddingGenerator()

    docs, vectors = generator.generate_embeddings()

    print("Documents:",len(docs))
    print("Embedding shape:",vectors.shape)