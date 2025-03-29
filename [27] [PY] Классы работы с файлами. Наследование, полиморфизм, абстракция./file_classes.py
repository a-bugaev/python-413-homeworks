"""
HW 27. File classes. Polymorphism, inheritance, abstraction.
commonly copypasted from hw 25
"""

from abc import ABC, abstractmethod
import csv
import json


class AbstractFile(ABC):
    """
    Abstract base class for file operations
    """

    ENCODINGS = {"TXT": "utf-8", "CSV": "utf-8-sig", "JSON": "utf-8", "YAML": "utf-8"}
    SEPARATORS: dict[str, tuple] = {
        "CSV": (";",),
        "JSON": (
            ", ",
            ": ",
        ),
    }
    INDENTS = {"JSON": 4, "YAML": 4}

    @abstractmethod
    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def read(self):
        """
        placeholder
        """
        raise NotImplementedError("Subclasses must implement read() method")

    @abstractmethod
    def write(self, *data):
        """
        placeholder
        """
        raise NotImplementedError("Subclasses must implement write() method")

    @abstractmethod
    def append(self, *data):
        """
        placeholder
        """
        raise NotImplementedError("Subclasses must implement append() method")


class JsonFile(AbstractFile):
    """
    JSON: read, write, append
    """

    def __init__(self, filepath: str):
        """
        each @abstractmethod must be implemented in children
        """
        super().__init__(filepath)

    def read(self) -> list:
        """
        Читает данные из JSON файла.
        filepath: string, path to file
        returns content of file (list of any)
        """
        try:
            with open(self.filepath, "r", encoding=self.ENCODINGS["JSON"]) as file:
                return json.load(file)
        except FileNotFoundError:
            print("File not found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return []

    def write(self, *data: list[dict]) -> None:
        """
        Записывает данные в JSON файл.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        with open(self.filepath, "w", encoding=self.ENCODINGS["JSON"]) as file:
            batch = data[0]
            for item in data[1:]:
                batch.append(item[0])
            json.dump(
                batch,
                file,
                ensure_ascii=False,
                indent=self.INDENTS["JSON"],
                separators=self.SEPARATORS["JSON"],
            )

    def append(self, *data: list[dict]) -> None:
        """
        Добавляет данные в конец JSON файла.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        try:
            with open(self.filepath, "r", encoding=self.ENCODINGS["JSON"]) as json_file:
                existing_data = json.load(json_file)
            for item in data:
                existing_data.extend(item)
            with open(self.filepath, "w", encoding=self.ENCODINGS["JSON"]) as json_file:
                json.dump(
                    existing_data,
                    json_file,
                    indent=self.INDENTS["JSON"],
                    separators=self.SEPARATORS["JSON"],
                )
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")


class TxtFile(AbstractFile):
    """
    TXT: read, write, append
    """

    def __init__(self, filepath: str):
        """
        each @abstractmethod must be implemented in children
        """
        super().__init__(filepath)

    def read(self) -> str:
        """
        Читает данные из текстового файла.
        filepath: string, path to file
        returns content of file (string)
        """
        try:
            with open(self.filepath, "r", encoding=self.ENCODINGS["TXT"]) as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
            return ""
        except PermissionError:
            print("Permission denied.")
            return ""

    def write(self, *data: str) -> None:
        """
        Записывает данные в текстовый файл.
        filepath: string, path to file
        data: string or list of strings
        returns nothing
        """
        try:
            with open(self.filepath, "w", encoding=self.ENCODINGS["TXT"]) as file:
                for item in data:
                    file.write(item)
        except PermissionError:
            print("Permission denied.")

    def append(self, *data: str) -> None:
        """
        Добавляет данные в конец текстового файла.
        filepath: string, path to file
        data: string or list of strings
        returns nothing
        """
        try:
            with open(self.filepath, "a", encoding=self.ENCODINGS["TXT"]) as file:
                for item in data:
                    file.write(item)
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")


class CsvFile(AbstractFile):
    """
    CSV: read, write, append
    """

    def __init__(self, filepath: str):
        """
        each @abstractmethod must be implemented in children
        """
        super().__init__(filepath)

    def read(self) -> list[dict]:
        """
        Читает данные из CSV файла.
        filepath: string, path to file
        returns content of file (list of dicts)
        """
        try:
            with open(
                self.filepath, mode="r", newline="", encoding=self.ENCODINGS["CSV"]
            ) as file:
                reader = csv.DictReader(file, delimiter=self.SEPARATORS["CSV"][0])
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

    def write(self, *data: list[dict]) -> None:
        """
        Записывает данные в CSV файл.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        try:
            with open(self.filepath, "w", encoding=self.ENCODINGS["CSV"]) as file:
                fieldnames = data[0][0].keys()
                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames,
                    delimiter=self.SEPARATORS["CSV"][0],
                )

                writer.writeheader()
                for item in data:
                    for row in item:
                        writer.writerow(row)
        except FileNotFoundError:
            print("File not found.")

    def append(self, *data: list[dict]) -> None:
        """
        Добавляет данные в конец CSV файла.
        filepath: string, path to file
        data: list of dicts
        returns nothing
        """
        try:
            with open(
                self.filepath, "a", newline="", encoding=self.ENCODINGS["CSV"]
            ) as file:
                fieldnames = data[0][0].keys()
                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames,
                    delimiter=self.SEPARATORS["CSV"][0],
                )
                for item in data:
                    for row in item:
                        writer.writerow(row)
        except FileNotFoundError:
            print("File not found.")
