import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

INPUT_FILE = "test_FD003.txt"
OUTPUT_FILE = "test_FD003_50.txt"

# Read NASA dataset
df = pd.read_csv(INPUT_FILE, sep=r"\s+", header=None, engine="python")

print("Original Shape:", df.shape)

# Column names
cols = [
    "engine_id","cycle",
    "setting1","setting2","setting3",
    "sensor1","sensor2","sensor3","sensor4","sensor5",
    "sensor6","sensor7","sensor8","sensor9","sensor10",
    "sensor11","sensor12","sensor13","sensor14","sensor15",
    "sensor16","sensor17","sensor18","sensor19","sensor20","sensor21"
]

df.columns = cols

# Pick 50 random engines
engines = sorted(df.engine_id.unique())
selected = random.sample(engines, 50)

new_frames = []

new_engine = 1

for eng in selected:

    temp = df[df.engine_id == eng].copy()

    # Renumber engine ids
    temp["engine_id"] = new_engine

    # Slightly modify sensors (not engine_id, cycle or settings)
    sensor_cols = [c for c in cols if c.startswith("sensor")]

    for col in sensor_cols:

        noise = np.random.normal(
            0,
            temp[col].std() * 0.02 + 0.001,
            len(temp)
        )

        temp[col] += noise

    new_frames.append(temp)

    new_engine += 1

new_df = pd.concat(new_frames)

new_df = new_df.sort_values(
    ["engine_id","cycle"]
)

print("New Shape:", new_df.shape)

new_df.to_csv(
    OUTPUT_FILE,
    sep=" ",
    header=False,
    index=False,
    float_format="%.5f"
)

print("Saved:", OUTPUT_FILE)