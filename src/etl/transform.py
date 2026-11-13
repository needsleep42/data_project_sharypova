
import pandas as pd


def transform_data(data):
    data = data.copy()

    data["experiment_datetime"] = pd.to_datetime(
        data["experiment_datetime"],
        format="%d.%m.%Y %H:%M"
    )

    data["instrument"] = data["instrument"].astype("category")
    data["crucible_type"] = data["crucible_type"].astype("category")

    return data
