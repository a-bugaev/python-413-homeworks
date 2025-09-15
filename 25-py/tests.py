"""
    test all methods
"""

import os
from handlers import (
    TxtFileHandler,
    CSVFileHandler,
    JSONFileHandler,
    YAMLFileHandler,
)

os.chdir(os.path.dirname(__file__))
if os.path.exists("example.txt"):
    os.remove("example.txt")
if os.path.exists("example.json"):
    os.remove("example.json")
if os.path.exists("example.csv"):
    os.remove("example.csv")
if os.path.exists("example.yaml"):
    os.remove("example.yaml")

# Работа с TXT файлами
txt_handler = TxtFileHandler()
txt_handler.write_file("example.txt", "Начало файла.\n")
txt_handler.append_file("example.txt", "Добавляем строку.\n")
content_txt = txt_handler.read_file("example.txt")
print("Содержимое TXT:\n", content_txt)

# Работа с CSV файлами
csv_handler = CSVFileHandler()
data_csv = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
csv_handler.write_file("example.csv", data_csv)
csv_handler.append_file("example.csv", [{"name": "Charlie", "age": "35"}])
content_csv = csv_handler.read_file("example.csv")
print("Содержимое CSV:\n", content_csv)

# Работа с JSON файлами
json_handler = JSONFileHandler()
data_json = [{"product": "Laptop", "price": 1500}, {"product": "Phone", "price": 800}]
json_handler.write_file("example.json", data_json)
json_handler.append_file("example.json", [{"product": "Tablet", "price": 600}])
content_json = json_handler.read_file("example.json")
print("Содержимое JSON:\n", content_json)

# Работа с YAML файлами
yaml_handler = YAMLFileHandler()
data_yaml = [{"product": "Laptop", "price": 1500}, {"product": "Phone", "price": 800}]
yaml_handler.write_file("example.yaml", data_yaml)
yaml_handler.append_file("example.yaml", [{"product": "Tablet", "price": 600}])
content_yaml = yaml_handler.read_file("example.yaml")
print("Содержимое YAML:\n", content_yaml)
