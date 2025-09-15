""" Tests """

import os
from files_utils import *


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)


# example json dataset
json_data = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Jane", "age": 25},
    {"id": 3, "name": "Bob", "age": 40},
]

write_json(json_data, file_path="test.json")

#
#    test.json content:
#    ```
#    [
#        {
#            "id": 1,
#            "name": "John",
#            "age": 30
#        },
#        {
#            "id": 2,
#            "name": "Jane",
#            "age": 25
#        },
#        {
#            "id": 3,
#            "name": "Bob",
#            "age": 40
#        }
#    ]
#
#

print(read_json("test.json"))

#
#    printed content:
#    [{'id': 1, 'name': 'John', 'age': 30}, {'id': 2, 'name': 'Jane', 'age': 25}, {'id': 3, 'name': 'Bob', 'age': 40}]
#

# additional json dataset

more_json_data = [
    {"id": 4, "name": "Alice", "age": 28},
    {"id": 5, "name": "Mike", "age": 35},
    {"id": 6, "name": "Sara", "age": 22},
]

append_json(more_json_data, file_path="test.json")

#
#    test.json content:
#
#    [
#        {
#            "id": 1,
#            "name": "John",
#            "age": 30
#        },
#        {
#            "id": 2,
#            "name": "Jane",
#            "age": 25
#        },
#        {
#            "id": 3,
#            "name": "Bob",
#            "age": 40
#        },
#        {
#            "id": 4,
#            "name": "Alice",
#            "age": 28
#        },
#        {
#            "id": 5,
#            "name": "Mike",
#            "age": 35
#        },
#        {
#            "id": 6,
#            "name": "Sara",
#            "age": 22
#        }
#    ]


# example csv dataset
csv_data = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Jane", "age": 25},
    {"id": 3, "name": "Bob", "age": 40},
]

write_csv(csv_data, file_path="test.csv")

#
#    test.csv content:
#
#       id,name,age
#       1,John,30
#       2,Jane,25
#       3,Bob,40


print(read_csv(file_path="test.csv"))

#
#   printed content:
#   [['id,name,age'], ['1,John,30'], ['2,Jane,25'], ['3,Bob,40']]
#

# additional csv dataset

more_csv_data = [
    {"id": 4, "name": "Alice", "age": 28},
    {"id": 5, "name": "Mike", "age": 35},
    {"id": 6, "name": "Sara", "age": 22},
]

append_csv(more_csv_data, file_path="test.csv")

#
#    test.csv content:
#
#       id;name;age
#       1;John;30
#       2;Jane;25
#       3;Bob;40
#       4;Alice;28
#       5;Mike;35
#       6;Sara;22


write_txt("Hello, World!", file_path="test.txt")

#
#    test.txt content:
#    Hello, World!


print(read_txt(file_path="test.txt"))

#
#   printed content:
#   Hello, World!

append_txt("\nHellow world again!", file_path="test.txt")

#
#    test.txt content:
#    Hello, World!
#    Hellow world again!
#

# YAML examlple dataset
yaml_data = [
    {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": 12345,
        },
        "hobbies": ["Reading", "Hiking", "Swimming"],
    },
    {
        "name": "Jane Smith",
        "age": 25,
        "address": {
            "street": "456 Elm St",
            "city": "Anytown",
            "state": "CA",
            "zip": 12345,
        },
        "hobbies": ["Painting", "Yoga", "Traveling"],
    },
    {
        "name": "Bob Johnson",
        "age": 40,
        "address": {
            "street": "789 Oak St",
            "city": "Anytown",
            "state": "CA",
            "zip": 12345,
        },
        "hobbies": ["Cooking", "Gardening", "Fishing"],
    },
]

write_yaml(yaml_data, file_path="test.yaml")

#
#   test.yaml content:
#
#
# - address:
#    city: Anytown
#    state: CA
#    street: 123 Main St
#    zip: 12345
#  age: 30
#  hobbies:
#  - Reading
#  - Hiking
#  - Swimming
#  name: John Doe
# - address:
#    city: Anytown
#    state: CA
#    street: 456 Elm St
#    zip: 12345
#  age: 25
#  hobbies:
#  - Painting
#  - Yoga
#  - Traveling
#  name: Jane Smith
# - address:
#    city: Anytown
#    state: CA
#    street: 789 Oak St
#    zip: 12345
#  age: 40
#  hobbies:
#  - Cooking
#  - Gardening
#  - Fishing
#  name: Bob Johnson
#

print(read_yaml(file_path="test.yaml"))

#
#   printed content:
#
# [{'address': {'city': 'Anytown', 'state': 'CA', 'street': '123 Main St', 'zip': 12345}, 'age': 30, 'hobbies': ['Reading', 'Hiking', 'Swimming'], 'name': 'John Doe'}, {'address': {'city': 'Anytown', 'state': 'CA', 'street': '456 Elm St', 'zip': 12345}, 'age': 25, 'hobbies': ['Painting', 'Yoga', 'Traveling'], 'name': 'Jane Smith'}, {'address': {'city': 'Anytown', 'state': 'CA', 'street': '789 Oak St', 'zip': 12345}, 'age': 40, 'hobbies': ['Cooking', 'Gardening', 'Fishing'], 'name': 'Bob Johnson'}]
#

more_yaml_data = [
    {
        "name": "Alice",
        "age": 28,
        "address": {
            "street": "456 Elm St",
            "city": "Anytown",
            "state": "CA",
            "zip": 12345,
        },
        "hobbies": ["Painting", "Yoga", "Traveling"],
    },
    {
        "name": "Mike",
        "age": 35,
        "address": {
            "street": "789 Oak St",
            "city": "Anytown",
            "state": "CA",
            "zip": 12345,
        },
        "hobbies": ["Cooking", "Gardening", "Fishing"],
    },
    {
        "name": "Greg",
        "age": 45,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": 12345,
        },
        "hobbies": ["Reading", "Hiking", "Swimming"],
    },
]

append_yaml(more_yaml_data, file_path="test.yaml")

# test.yaml content:
#
#   - address:
#       city: Anytown
#       state: CA
#       street: 123 Main St
#       zip: 12345
#     age: 30
#     hobbies:
#     - Reading
#     - Hiking
#     - Swimming
#     name: John Doe
#   - address:
#       city: Anytown
#       state: CA
#       street: 456 Elm St
#       zip: 12345
#     age: 25
#     hobbies:
#     - Painting
#     - Yoga
#     - Traveling
#     name: Jane Smith
#   - address:
#       city: Anytown
#       state: CA
#       street: 789 Oak St
#       zip: 12345
#     age: 40
#     hobbies:
#     - Cooking
#     - Gardening
#     - Fishing
#     name: Bob Johnson
#   - address:
#       city: Anytown
#       state: CA
#       street: 456 Elm St
#       zip: 12345
#     age: 28
#     hobbies:
#     - Painting
#     - Yoga
#     - Traveling
#     name: Alice
#   - address:
#       city: Anytown
#       state: CA
#       street: 789 Oak St
#       zip: 12345
#     age: 35
#     hobbies:
#     - Cooking
#     - Gardening
#     - Fishing
#     name: Mike
#   - address:
#       city: Anytown
#       state: CA
#       street: 123 Main St
#       zip: 12345
#     age: 45
#     hobbies:
#     - Reading
#     - Hiking
#     - Swimming
#     name: Greg
