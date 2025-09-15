"""
butch rename inside diven path
"""

import os
from tabulate import tabulate

INPUT_DIR = input("Input path (abs): ")

INPUT_LISTDIR = os.listdir(INPUT_DIR)

INPUT_LISTDIR_STR = "\n".join(INPUT_LISTDIR)

with open("./output.txt", "w", encoding="utf-8") as f:
    f.write(INPUT_LISTDIR_STR)

CONTINUE = "___"
while CONTINUE != "":
    CONTINUE = input("Edit output file as you want and hit Enter, it's safe for now")

CHECKOUT_INPUT_LIST = [
    {"INPUT": input_item} for input_item in INPUT_LISTDIR
]

with open("./output.txt", "r", encoding="utf-8") as f:
    CHECKOUT_OUTPUT_STR = f.read()

CHECKOUT_OUTPUT_LIST = [
    {"OUTPUT": input_item} for input_item in CHECKOUT_OUTPUT_STR.split("\n")
]

CHECKOUT_LIST:list = []

for i, val in enumerate(CHECKOUT_INPUT_LIST):
    CHECKOUT_LIST.append({
        **val, **CHECKOUT_OUTPUT_LIST[i]
    })

print(tabulate(CHECKOUT_LIST, headers="keys"))

CONTINUE = "___"
while CONTINUE != "":
    CONTINUE = input("Is it ok? (Hit Enter with caution now)")

for item in CHECKOUT_LIST:
    os.rename(INPUT_DIR + "/" + item["INPUT"], INPUT_DIR + "/" + item["OUTPUT"])

print("done")