from sqlalchemy import text
from db_utils import get_engine

engine = get_engine()

with engine.connect() as connection:
    result = connection.execute(text("SELECT current_database()"))
    database_name = result.scalar()

print("Подключение успешно!")
print("База данных:", database_name)