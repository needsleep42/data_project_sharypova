import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

ROOT = Path(__file__).resolve().parent.parent

# 1. Загружаем 100 строк из Parquet
DATA_PATH = ROOT / "data.parquet"

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "Файл data.parquet не найден. Сначала запустите data_loader.py"
    )

df = pd.read_parquet(DATA_PATH)
data_to_upload = df.head(100).copy()

if len(data_to_upload) != 100:
    raise ValueError("В датасете меньше 100 строк")

# 2. Получаем настройки подключения из .env
load_dotenv(ROOT / ".env")

required_vars = [
    "HOMEWORK_DB_USER",
    "HOMEWORK_DB_PASSWORD",
    "HOMEWORK_DB_HOST",
    "HOMEWORK_DB_PORT",
    "HOMEWORK_DB_NAME"
]

for var in required_vars:
    if not os.getenv(var):
        raise ValueError(
            "Не найдены настройки подключения. Сначала запустите read_creds.py"
        )

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("HOMEWORK_DB_USER"),
    password=os.getenv("HOMEWORK_DB_PASSWORD"),
    host=os.getenv("HOMEWORK_DB_HOST"),
    port=int(os.getenv("HOMEWORK_DB_PORT")),
    database=os.getenv("HOMEWORK_DB_NAME"),
)

engine = create_engine(
    db_url,
    connect_args={"connect_timeout": 10}
)

# 3. Записываем данные в PostgreSQL
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
