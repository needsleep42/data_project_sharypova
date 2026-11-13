
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


TABLE_NAME = "sharypovaas_etl"


def get_engine():
    root = Path(__file__).resolve().parents[2]
    load_dotenv(root / ".env")

    db_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.environ["HOMEWORK_DB_USER"],
        password=os.environ["HOMEWORK_DB_PASSWORD"],
        host=os.environ["HOMEWORK_DB_HOST"],
        port=int(os.environ["HOMEWORK_DB_PORT"]),
        database=os.environ["HOMEWORK_DB_NAME"]
    )

    return create_engine(
        db_url,
        connect_args={"connect_timeout": 10}
    )


def load_data(data):
    if not 1 <= len(data) <= 100:
        raise ValueError("Для записи требуется от 1 до 100 строк")

    engine = get_engine()

    try:
        with engine.begin() as connection:
            data.to_sql(
                name=TABLE_NAME,
                con=connection,
                if_exists="fail",
                index=False
            )

        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(*) FROM sharypovaas_etl")
            )
            count = result.scalar()

        if count != len(data):
            raise ValueError("Количество строк в БД не совпадает")

        print(f"В PostgreSQL записано {count} строк")

    finally:
        engine.dispose()
