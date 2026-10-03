import pandas as pd

DATASET_URL = "https://drive.google.com/uc?export=download&id=1AzuOQPWF5PUckfjcGoHsmzs5hGJxtO7j"


def load_data():
    data = pd.read_csv(DATASET_URL)
    print(data.head(10))
    return data


if __name__ == "__main__":
    load_data()

\n