import pandas as pd
from pathlib import Path

DATASET_URL = "https://drive.google.com/uc?export=download&id=1AzuOQPWF5PUckfjcGoHsmzs5hGJxtO7j"
OUTPUT_PATH = Path(__file__).parent / "data.parquet"


def load_data():
    data = pd.read_csv(DATASET_URL)
    return data


def convert_types(data):
    data = data.copy()

    data["experiment_datetime"] = pd.to_datetime(
        data["experiment_datetime"], format="%d.%m.%Y %H:%M"
    )
    data["instrument"] = data["instrument"].astype("category")
    data["crucible_type"] = data["crucible_type"].astype("category")

    return data


if __name__ == "__main__":
    data = load_data()
    data = convert_types(data)
    data.to_parquet(OUTPUT_PATH, index=False)
