
import argparse

from .extract import extract_data
from .transform import transform_data
from .validate import validate_data
from .load import load_data


def main():
    parser = argparse.ArgumentParser(
        description="ETL для экспериментальных данных ТГА"
    )
    parser.add_argument(
        "--limit",
        type=int,
        required=True,
        help="Количество строк для записи в БД (от 1 до 100)"
    )

    args = parser.parse_args()

    if not 1 <= args.limit <= 100:
        parser.error("--limit должен быть от 1 до 100")

    print("Загрузка исходных данных...")
    data = extract_data()

    print("Преобразование данных...")
    data = transform_data(data)

    print("Проверка качества данных...")
    data = validate_data(data)

    data = data.head(args.limit).copy()

    print("Запись в PostgreSQL...")
    load_data(data)

    print("ETL завершён!")


if __name__ == "__main__":
    main()
