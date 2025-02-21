---
project: "[[Академия TOP]]"
journal: "[[PYTHON413]]"
tags:
  - PYTHON413
date: 2025-01-25
type:
  - home work
hw_num: 22
topic: "Вам предстоит создать набор функций для работы с файлами различных форматов: JSON, CSV, TXT и YAML. Эти функции позволят вам читать, записывать и обновлять данные в указанных форматах. Кроме того, вы создадите тесты для этих функций, чтобы убедиться в корректной работе вашего кода."
hw_theme:
  - python
  - JSON
  - yaml
  - CSV
  - txt
  - чтение и запись JSON
  - функции
st_group: python 413
links:
---
# Домашнее задание 📃

## Краткое содержание

Вам предстоит создать набор функций для работы с файлами различных форматов: JSON, CSV, TXT и YAML. Эти функции позволят вам читать, записывать и обновлять данные в указанных форматах. Кроме того, вы создадите тесты для этих функций, чтобы убедиться в корректной работе вашего кода.

### Технологии: 🦾
- Python
- JSON
- CSV
- TXT
- YAML

## Задание 👷‍♂️

Создайте модуль `files_utils.py`, содержащий следующие функции:

### Функции для работы с JSON:

1. **Функция `read_json(file_path: str, encoding: str = "utf-8")`**
   - Описание: Читает данные из JSON-файла.
   - Входные параметры:
     - `file_path`: Путь к файлу.
     - `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
   - Возвращаемое значение: Данные, считанные из файла.

2. **Функция `write_json(*data: dict, file_path: str, encoding: str = "utf-8")`**
   - Описание: Записывает данные в JSON-файл.
   - Входные параметры:
     - `data`: Данные для записи.
     - `file_path`: Путь к файлу.
     - `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
   - Возвращаемое значение: Нет.

3. **Функция `append_json(*data: dict, file_path: str, encoding: str = "utf-8")`**
   - Описание: Добавляет данные в существующий JSON-файл.
   - Входные параметры:
     - `data`: Список словарей с данными для добавления.
     - `file_path`: Путь к файлу.
     - `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
   - Возвращаемое значение: Нет.

### Функции для работы с CSV:

4. **Функция `read_csv(file_path: str, delimiter=';', encoding: str ='utf-8-sig')`**
   - Описание: Читает данные из CSV-файла.
   - Входные параметры:
     - `file_path`: Путь к файлу.
     - `delimiter`: Разделитель полей в файле (по умолчанию `';'`).
     - `encoding`: Кодировка файла (по умолчанию `"windows-1251"`).
   - Возвращаемое значение: Данные, считанные из файла.

5. **Функция `write_csv(*data: dict, file_path: str, delimiter=';', encoding: str ='utf-8-sig')`**
   - Описание: Записывает данные в CSV-файл.
   - Входные параметры:
     - `data`: Данные для записи.
     - `file_path`: Путь к файлу.
     - `delimiter`: Разделитель полей в файле (по умолчанию `';'`).
     - `encoding`: Кодировка файла (по умолчанию `'utf-8-sig'`).
   - Возвращаемое значение: Нет.

6. **Функция `append_csv(*data: dict, file_path: str, delimiter=';', encoding: str ='utf-8-sig')`**
   - Описание: Добавляет данные в существующий CSV-файл.
   - Входные параметры:
     - `data`: Данные для добавления.
     - `file_path`: Путь к файлу.
     - `delimiter`: Разделитель полей в файле (по умолчанию `';'`).
     - `encoding`: Кодировка файла (по умолчанию `'utf-8-sig'`).
   - Возвращаемое значение: Нет.

### Функции для работы с TXT:

7. **Функция `read_txt(file_path: str, encoding: str = "utf-8")`**
   - Описание: Читает данные из текстового файла.
   - Входные параметры:
     - `file_path`: Путь к файлу.
     - `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
   - Возвращаемое значение: Содержимое файла.

8. **Функция `write_txt(*data: str, file_path: str, encoding: str = "utf-8")`**
   - Описание: Записывает данные в текстовый файл.
   - Входные параметры:
     - `data`: Данные для записи.
     - `file_path`: Путь к файлу.
     - `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
   - Возвращаемое значение: Нет.

9. **Функция `append_txt(*data: str, file_path: str, encoding: str = "utf-8")`**
   - Описание: Добавляет данные в конец текстового файла.
   - Входные параметры:
     - `data`: Данные для добавления.
     - `file_path`: Путь к файлу.
     - `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
   - Возвращаемое значение: Нет.

### Функция для работы с YAML:

10. **Функция `read_yaml(file_path)`**
    - Описание: Читает данные из YAML-файла.
    - Входные параметры:
      - `file_path`: Путь к файлу.
    - Возвращаемое значение: Данные, считанные из файла.

### Вызов функций

После создания всех функций, выполните их вызов в модуле `files_utils_tests.py`. Создайте минимальный датасет для тестирования каждой функции и сохраните результаты в соответствующие файлы:

- `test.txt`
- `test.json`
- `test.csv`
- `test.yaml`

### Таблица функций и аргументов

Аннотации типов тут не полные. Вам нужно будет это поправить.

| №   | Название функции | Аргументы                                         |
| --- | ---------------- | ------------------------------------------------- |
| 1   | `read_json`      | `file_path: str, encoding: str = "utf-8"`         |
| 2   | `write_json`     | `data, file_path: str, encoding: str`             |
| 3   | `append_json`    | `data: list[dict], file_path: str, encoding: str` |
| 4   | `read_csv`       | `file_path, delimiter=';', encoding: str`         |
| 5   | `write_csv`      | `data, file_path, delimiter=';', encoding: str`   |
| 6   | `append_csv`     | `data, file_path, delimiter=';', encoding: str`   |
| 7   | `read_txt`       | `file_path, encoding: str = "utf-8"`              |
| 8   | `write_txt`      | `data, file_path, encoding: str = "utf-8"`        |
| 9   | `append_txt`     | `data, file_path, encoding: str = "utf-8"`        |
| 10  | `read_yaml`      | `file_path`                                       |

Опишите параметры погодного приложения в YAML и сделайте тестовое чтение из документа.


>[!warning]
>### Критерии проверки 👌
>- Соблюдение нейминга и стиля PEP-8.
>- Правильная работа с JSON-файлами: корректная запись данных с отступами и использованием кодировки UTF-8.
>- Использование всех необходимых параметров для работы с CSV-файлами.
>- Рабочий код, который проходит тестирование.
>- Наличие вызова функций в коде.
>- Архив с домашним заданием должен содержать файл где есть ссылка на репозиторий GitHub.
>- Использование контекстного менеджера with для открытия файлов
>- Разделение кода на два файла: `files_utils.py` и `files_utils_tests.py`.
>- Не менее **5 коммитов** в репозитории для данной домашней работы.
>- Аннотирование типов и документация для всех функций. Включая возвращаемое значение