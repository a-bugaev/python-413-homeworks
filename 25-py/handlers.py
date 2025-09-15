"""
    HW 25. Классы работы с файлами
    based on code from hw 22
"""

import os
from typing import Any

import csv
import json
import yaml

os.chdir(os.path.dirname(__file__))

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
    @staticmethod
    def read_file(filepath: str) -> str:
        """
        Читает данные из текстового файла.
        filepath: string, path to file
        returns content of file (string)
        """
        try:
            with open(filepath, "r", encoding=ENCODINGS["TXT"]) as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
            return ""
        except PermissionError:
            print("Permission denied.")
            return ""

    @staticmethod
    def write_file(filepath: str, *data: str) -> None:
        """
        Записывает данные в текстовый файл.
        filepath: string, path to file
        data: string or list of strings
        returns nothing
        """
        try:
            with open(filepath, "w", encoding=ENCODINGS["TXT"]) as file:
                for item in data:
                    file.write(item)
        except PermissionError:
            print("Permission denied.")

    @staticmethod
    def append_file(filepath: str, *data: str) -> None:
        """
        Добавляет данные в конец текстового файла.
        filepath: string, path to file
        data: string or list of strings
        returns nothing
        """
        try:
            with open(filepath, "a", encoding=ENCODINGS["TXT"]) as file:
                for item in data:
                    file.write(item)
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")


class CSVFileHandler:
    """
    CSV: read, write, append
    """
    @staticmethod
    def read_file(filepath: str) -> list[dict]:
        """
        Читает данные из CSV файла.
        filepath: string, path to file
        returns content of file (list of dicts)
        """
        try:
            with open(
                filepath, mode="r", newline="", encoding=ENCODINGS["CSV"]
            ) as file:
                reader = csv.DictReader(file, delimiter=SEPARATORS["CSV"][0])
                data_list = []
                for row in reader:
                    data_list.append(row)
                return data_list
        except FileNotFoundError:
            print("File not found.")
            return []
        except PermissionError:
            print("Permission denied.")
            return []

    @staticmethod
    def write_file(filepath: str, *data: list[dict]) -> None:
        """
        Записывает данные в CSV файл.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        try:
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
        except FileNotFoundError:
            print("File not found.")

    @staticmethod
    def append_file(filepath: str, *data: list[dict]) -> None:
        """
        Добавляет данные в конец CSV файла.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        try:
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
        except FileNotFoundError:
            print("File not found.")


class JSONFileHandler:
    """
    JSON: read, write, append
    """
    @staticmethod
    def read_file(filepath: str) -> list:
        """
        Читает данные из JSON файла.
        filepath: string, path to file
        returns content of file (list of any)
        """
        try:
            with open(filepath, "r", encoding=ENCODINGS["JSON"]) as file:
                return json.load(file)
        except FileNotFoundError:
            print("File not found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return []

    @staticmethod
    def write_file(filepath: str, *data: list[dict]) -> None:
        """
        Записывает данные в JSON файл.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(filepath, "w", encoding=ENCODINGS["JSON"]) as file:
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
        try:
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
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")


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
