import pandas as pd
import os


def load_processed_data(user_id):

    file_path = os.path.join(
        "processed",
        f"user_{user_id}",
        "final_output.csv"
    )

    if not os.path.exists(file_path):
        return None

    return pd.read_csv(file_path)