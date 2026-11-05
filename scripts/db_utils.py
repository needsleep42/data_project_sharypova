import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def get_engine():
    root = Path(__file__).resolve().parent.parent
    load_dotenv(root / ".env")

    required_vars = [
        "HOMEWORK_DB_USER",
        "HOMEWORK_DB_PASSWORD",
        "HOMEWORK_DB_HOST",
        "HOMEWORK_DB_PORT",
        "HOMEWORK_DB_NAME"
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        raise ValueError(
            f"Отсутствуют настройки: {', '.join(missing)}. "
            "Сначала запустите read_creds.py"
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

    return engine
