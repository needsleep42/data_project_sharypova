import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

ROOT = Path(__file__).resolve().parent.parent

load_dotenv(ROOT / ".env")

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("HOMEWORK_DB_USER"),
    password=os.getenv("HOMEWORK_DB_PASSWORD"),
    host=os.getenv("HOMEWORK_DB_HOST"),
    port=int(os.getenv("HOMEWORK_DB_PORT")),
    database=os.getenv("HOMEWORK_DB_NAME"),
)

engine = create_engine(db_url, connect_args={"connect_timeout": 10})

with engine.connect() as connection:
    result = connection.execute(text("SELECT current_database()"))
    database_name = result.scalar()

print("Подключение успешно!")
print("База данных:", database_name)
