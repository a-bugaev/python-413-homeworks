"""
    22. Функции работы с файлами
"""

from typing import Any
import json
import csv
import yaml


def read_json(file_path: str, encoding: str = "utf-8") -> Any:
    """
    Читает данные из JSON-файла.
    """
    with open(file_path, "r", encoding=encoding) as file:
        data = json.load(file)
        return data


def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Записывает данные в JSON-файл.
    """
    with open(file_path, "w", encoding=encoding) as file:
        batch = data[0]
        for item in data[1:]:
            batch.update(item)
        json.dump(batch, file, ensure_ascii=False, indent=4, separators=(", ", ": "))


def append_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Добавляет данные в существующий JSON-файл.
    """
    with open(file_path, "r", encoding=encoding) as json_file:
        existing_data = json.load(json_file)
    for item in data:
        existing_data.extend(item)
    with open(file_path, "w", encoding=encoding) as json_file:
        json.dump(existing_data, json_file, indent=4, separators=(",", ": "))


def read_csv(file_path: str, delimiter=";", encoding: str = "utf-8-sig") -> list:
    """
    Читает данные из CSV-файла.
    """
    with open(file_path, "r", encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        output = []
        for row in reader:
            output.append(row)
        return output


def write_csv(*data: dict, file_path, delimiter=";", encoding: str = "utf-8-sig") -> None:
    """
    Записывает данные в CSV-файл.
    """
    with open(file_path, "w", encoding=encoding) as file:
        fieldnames = data[0][0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)

        writer.writeheader()
        for item in data:
            for row in item:
                writer.writerow(row)


def append_csv(*data: dict, file_path, delimiter=";", encoding: str = "utf-8-sig") -> None:
    """
    Добавляет данные в существующий CSV-файл.
    """
    with open(file_path, "a", newline="", encoding=encoding) as file:
        fieldnames = data[0][0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)
        for item in data:
            for row in item:
                writer.writerow(row)


def read_txt(file_path: str, encoding: str = "utf-8") -> str:
    """
    Читает данные из текстового файла.
    """
    with open(file_path, "r", encoding=encoding) as file:
        content = file.read()
        return content


def write_txt(*data: str, file_path, encoding: str = "utf-8") -> None:
    """
    Записывает данные в текстовый файл.
    """
    with open(file_path, "w", encoding=encoding) as file:
        for item in data:
            file.write(item)


def append_txt(*data: str, file_path, encoding: str = "utf-8") -> None:
    """
    Добавляет данные в конец текстового файла.
    """
    with open(file_path, "a", encoding=encoding) as file:
        for item in data:
            file.write(item)


def read_yaml(file_path: str, encoding: str = "utf-8") -> Any:
    """
    Читает данные из YAML-файла.
    """
    with open(file_path, "r", encoding=encoding) as file:
        data = yaml.safe_load(file)
        return data


def write_yaml(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Записывает данные в YAML-файл.
    """
    with open(file_path, "w", encoding=encoding) as file:
        for item in data:
            yaml.dump(item, file, default_flow_style=False)


def append_yaml(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Добавляет данные в YAML-файл.
    """
    with open(file_path, "a", encoding=encoding) as file:
        for item in data:
            yaml.dump(item, file, default_flow_style=False)
