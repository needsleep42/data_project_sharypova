
import pandas as pd

DATASET_URL = "https://drive.google.com/uc?export=download&id=1AzuOQPWF5PUckfjcGoHsmzs5hGJxtO7j"


def extract_data():
    data = pd.read_csv(DATASET_URL)

    if data.empty:
        raise ValueError("Исходный датасет пустой")

    return data
