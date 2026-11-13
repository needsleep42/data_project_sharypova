
def validate_data(data):
    required_columns = [
        "temperature_C",
        "mass_percent",
        "dtg_pct_per_min",
        "ph"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Отсутствуют столбцы: {missing_columns}"
        )

    if data.empty:
        raise ValueError("Нет данных для загрузки")

    if data[required_columns].isna().any().any():
        raise ValueError(
            "В основных измеряемых величинах есть пропуски"
        )

    return data
