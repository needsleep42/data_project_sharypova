# OpenAlex Dataset

Датасет научных публикаций по теме гидрогелей, полученный через публичный API [OpenAlex](https://openalex.org/).

Скрипт `read_api.py` обращается к API OpenAlex и получает 100 публикаций по запросу `hydrogel`.

Датасет содержит 6 столбцов: название публикации, год, DOI, количество цитирований, наличие открытого доступа и тип публикации.

Полученные данные сохраняются в формате CSV (`openalex_hydrogels.csv`). Файл исключён из репозитория с помощью `.gitignore`.

## Пример данных

[Скриншот первых 10 строк датасета](https://drive.google.com/file/d/10KfUDMkfYm_7Wh2qJg4Zkw8hmInhZoM8/view?usp=sharing)