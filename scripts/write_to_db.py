from pathlib import Path

import pandas as pd
from sqlalchemy import text
from db_utils import get_engine

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data.parquet"

# Загружаем 100 строк из Parquet
if not DATA_PATH.exists():
    raise FileNotFoundError(
        "Файл data.parquet не найден. Сначала запустите data_loader.py"
    )

df = pd.read_parquet(DATA_PATH)
data_to_upload = df.head(100).copy()

if len(data_to_upload) != 100:
    raise ValueError("В датасете меньше 100 строк")

# Подключаемся к PostgreSQL
engine = get_engine()

# Записываем данные
table_name = "sharypovaas"

with engine.begin() as connection:
    data_to_upload.to_sql(
        name=table_name,
        con=connection,
        if_exists="fail",
        index=False
    )

    result = connection.execute(
        text("SELECT COUNT(*) FROM sharypovaas")
    )

    count = result.scalar()

print("Количество записанных строк:", count)
print("Запись в homeworks завершена!")