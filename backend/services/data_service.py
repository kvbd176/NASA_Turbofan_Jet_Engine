import os
import pandas as pd
from services.pipeline_service import PipelineService


UPLOAD_DIR = "uploads"
PROCESSED_DIR = "processed"

def get_user_dataset_path(user_id):

    user_folder = os.path.join(
        UPLOAD_DIR,
        f"user_{user_id}"
    )

    if not os.path.exists(user_folder):
        return None

    files = os.listdir(user_folder)

    if len(files) == 0:
        return None

    return os.path.join(
        user_folder,
        files[0]
    )


def process_user_dataset(user_id):

    df = load_user_dataset(
        user_id
    )

    if df is None:
        return None

    pipeline = PipelineService()

    df = pipeline.run_pipeline(df)

    output_file = pipeline.save_output(
        df,
        user_id
    )

    return {
        "processed_file": output_file,
        "rows_processed": len(df)
    }


def load_user_dataset(user_id):

    dataset_path = get_user_dataset_path(
        user_id
    )

    if dataset_path is None:
        return None

    df = pd.read_csv(
    dataset_path,
        sep=r"\s+",
        header=None
    )

    df.columns = [
        "engine_id",
        "cycle",
        "setting1",
        "setting2",
        "setting3",
        "sensor1",
        "sensor2",
        "sensor3",
        "sensor4",
        "sensor5",
        "sensor6",
        "sensor7",
        "sensor8",
        "sensor9",
        "sensor10",
        "sensor11",
        "sensor12",
        "sensor13",
        "sensor14",
        "sensor15",
        "sensor16",
        "sensor17",
        "sensor18",
        "sensor19",
        "sensor20",
        "sensor21"
    ]
    print(df.columns.tolist())

    return df