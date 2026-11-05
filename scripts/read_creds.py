import sqlite3
from pathlib import Path
from dotenv import set_key

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "creds.db"
ENV_PATH = ROOT / ".env"

with sqlite3.connect(DB_PATH) as connection:
    connection.row_factory = sqlite3.Row

    student = connection.execute(
        'SELECT * FROM access WHERE "user" = ?',
        ("student",)
    ).fetchone()

    homework = connection.execute(
        'SELECT * FROM access WHERE "user" != ?',
        ("student",)
    ).fetchone()

if student is None or homework is None:
    raise ValueError("Не найдены необходимые учётные записи")

# Настройки учебной базы
set_key(ENV_PATH, "STUDENT_DB_HOST", str(student["url"]))
set_key(ENV_PATH, "STUDENT_DB_PORT", str(student["port"]))
set_key(ENV_PATH, "STUDENT_DB_USER", str(student["user"]))
set_key(ENV_PATH, "STUDENT_DB_PASSWORD", str(student["pass"]))
set_key(ENV_PATH, "STUDENT_DB_NAME", "freezone")

# Настройки базы для домашних заданий
set_key(ENV_PATH, "HOMEWORK_DB_HOST", str(homework["url"]))
set_key(ENV_PATH, "HOMEWORK_DB_PORT", str(homework["port"]))
set_key(ENV_PATH, "HOMEWORK_DB_USER", str(homework["user"]))
set_key(ENV_PATH, "HOMEWORK_DB_PASSWORD", str(homework["pass"]))
set_key(ENV_PATH, "HOMEWORK_DB_NAME", "homeworks")

print("Настройки подключения сохранены в .env")
