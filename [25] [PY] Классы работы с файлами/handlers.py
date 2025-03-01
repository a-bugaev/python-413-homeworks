"""
    HW 25. Классы работы с файлами
    based on code from hw 22
"""

import os
from typing import Any

# from pprint import pprint
import csv
import json
import yaml

os.chdir(os.path.dirname(__file__))

# except FileNotFoundError:
#     return "The file was not found."
# except PermissionError:
#     return "Permission denied."
# except OSError:
#     return "An OS-related error occurred."
# except EOFError:
#     return "Reached the end of the file unexpectedly."
# except UnicodeDecodeError:
#     return "Failed to decode the file content."
# except ValueError:
#     return "Invalid file mode."

ENCODINGS = {"TXT": "utf-8", "CSV": "utf-8-sig", "JSON": "utf-8", "YAML": "utf-8"}
SEPARATORS: dict[str, tuple] = {
    "CSV": (";",),
    "JSON": (
        ", ",
        ": ",
    ),
}
INDENTS = {"JSON": 4, "YAML": 4}


class TxtFileHandler:
    """
    TXT: read, write, append
    """

    # TODO
    # FileNotFoundError
    # PermissionError
    @staticmethod
    def read_file(filepath: str) -> str:
        """
        Читает данные из текстового файла.
        filepath: string, path to file
        returns content of file (string)
        """
        if os.path.exists(filepath):
            with open(filepath, "r", encoding=ENCODINGS["TXT"]) as file:
                return file.read()
        else:
            return ""

    @staticmethod
    def write_file(filepath: str, *data: str) -> None:
        """
        Записывает данные в текстовый файл.
        filepath: string, path to file
        data: string or list of strings
        returns nothing
        """
        with open(filepath, "w", encoding=ENCODINGS["TXT"]) as file:
            for item in data:
                file.write(item)

    @staticmethod
    def append_file(filepath: str, *data: str) -> None:
        """
        Добавляет данные в конец текстового файла.
        filepath: string, path to file
        data: string or list of strings
        returns nothing
        """
        with open(filepath, "a", encoding=ENCODINGS["TXT"]) as file:
            for item in data:
                file.write(item)


class CSVFileHandler:
    """
    CSV: read, write, append
    """
    # TODO
    # Обработка исключений, связанных с операциями ввода-вывода
    @staticmethod
    def read_file(filepath: str) -> list[dict]:
        """
        Читает данные из CSV файла.
        filepath: string, path to file
        returns content of file (list of dicts)
        """
        if os.path.exists(filepath):
            with open(
                filepath, mode="r", newline="", encoding=ENCODINGS["CSV"]
            ) as file:
                reader = csv.DictReader(file, delimiter=SEPARATORS["CSV"][0])
                data_list = []
                for row in reader:
                    data_list.append(row)
                return data_list
        else:
            return []

    @staticmethod
    def write_file(filepath: str, *data: list[dict]) -> None:
        """
        Записывает данные в CSV файл.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(filepath, "w", encoding=ENCODINGS["CSV"]) as file:
            fieldnames = data[0][0].keys()
            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                delimiter=SEPARATORS["CSV"][0],
            )

            writer.writeheader()
            for item in data:
                for row in item:
                    writer.writerow(row)

    @staticmethod
    def append_file(filepath: str, *data: list[dict]) -> None:
        """
        Добавляет данные в конец CSV файла.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(filepath, "a", newline="", encoding=ENCODINGS["CSV"]) as file:
            fieldnames = data[0][0].keys()
            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                delimiter=SEPARATORS["CSV"][0],
            )
            for item in data:
                for row in item:
                    writer.writerow(row)


class JSONFileHandler:
    """
    JSON: read, write, append
    """

    # TODO
    # JSONDecodeError
    # FileNotFoundError
    @staticmethod
    def read_file(filepath: str) -> list:
        """
        Читает данные из JSON файла.
        filepath: string, path to file
        returns content of file (list of any)
        """
        if os.path.exists(filepath):
            with open(filepath, "r", encoding=ENCODINGS["JSON"]) as file:
                return json.load(file)
        else:
            return []

    @staticmethod
    def write_file(filepath: str, *data: list[dict]) -> None:
        """
        Записывает данные в JSON файл.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(filepath, "a", encoding=ENCODINGS["JSON"]) as file:
            batch = data[0]
            for item in data[1:]:
                batch.append(item[0])
            json.dump(
                batch,
                file,
                ensure_ascii=False,
                indent=INDENTS["JSON"],
                separators=SEPARATORS["JSON"],
            )

    @staticmethod
    def append_file(filepath: str, *data: list[dict]) -> None:
        """
        Добавляет данные в конец JSON файла.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(filepath, "r", encoding=ENCODINGS["JSON"]) as json_file:
            existing_data = json.load(json_file)
        for item in data:
            existing_data.extend(item)
        with open(filepath, "w", encoding=ENCODINGS["JSON"]) as json_file:
            json.dump(
                existing_data,
                json_file,
                indent=INDENTS["JSON"],
                separators=SEPARATORS["JSON"],
            )


class YAMLFileHandler:
    """
    YAML: read, write, append
    """
    # TODO
    @staticmethod
    def read_file(filepath: str) -> Any:
        """
        Читает данные из YAML файла.
        filepath: string, path to file
        returns content of file (list of any)
        """
        if os.path.exists(filepath):
            with open(filepath, "r", encoding=ENCODINGS["YAML"]) as file:
                return yaml.safe_load(file)
        else:
            return []

    @staticmethod
    def write_file(filepath: str, *data: list[dict]) -> None:
        """
        Записывает данные в YAML файл.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(filepath, "w", encoding=ENCODINGS["YAML"]) as file:
            for item in data:
                yaml.dump(
                    item,
                    file,
                    allow_unicode=True,
                    default_flow_style=False,
                    indent=INDENTS["YAML"],
                )

    @staticmethod
    def append_file(filepath: str, *data: list[dict]) -> None:
        """
        Добавляет данные в конец YAML файла.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(filepath, "a", encoding=ENCODINGS["YAML"]) as file:
            for item in data:
                yaml.dump(
                    item,
                    file,
                    allow_unicode=True,
                    default_flow_style=False,
                    indent=INDENTS["YAML"],
                )
