"""
    test all methods
"""

import os
from file_classes import (
    JsonFile,
    TxtFile,
    CsvFile,
)

os.chdir(os.path.dirname(__file__))
if os.path.exists("example.txt"):
    os.remove("example.txt")
if os.path.exists("example.json"):
    os.remove("example.json")
if os.path.exists("example.csv"):
    os.remove("example.csv")

# Работа с TXT файлами
txt_handler = TxtFile(filepath="example.txt")
txt_handler.write("Начало файла.\n")
txt_handler.append("Добавляем строку.\n")
content_txt = txt_handler.read()
print("Содержимое TXT:\n", content_txt)

# Работа с CSV файлами
csv_handler = CsvFile(filepath="example.csv")
data_csv = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
csv_handler.write(data_csv)
csv_handler.append([{"name": "Charlie", "age": "35"}])
content_csv = csv_handler.read()
print("Содержимое CSV:\n", content_csv)

# Работа с JSON файлами
json_handler = JsonFile(filepath="example.json")
data_json = [{"product": "Laptop", "price": 1500}, {"product": "Phone", "price": 800}]
json_handler.write(data_json)
json_handler.append([{"product": "Tablet", "price": 600}])
content_json = json_handler.read()
print("Содержимое JSON:\n", content_json)
