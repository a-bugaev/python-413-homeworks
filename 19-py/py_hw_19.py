"""
    ДЗ №19. Работа с фильмами в Python.
"""

import copy
import os

# source data

SMALL_DICT = {
    "Человек-муравей и Оса: Квантомания": 2023,
    "Стражи Галактики. Часть 3": 2023,
    "Капитан Марвел 2": 2023,
    "Дэдпул 3": 2024,
    "Капитан Америка: Дивный новый мир": 2024,
    "Громовержцы": 2024,
    "Блэйд": 2025,
    "Фантастическая четвёрка": 2025,
    "Мстители: Династия Канга": 2026,
    "Мстители: Секретные войны": 2027,
    "Безымянный фильм о Человеке-пауке": None,
    "Безымянный фильм о Шан-Чи": None,
    "Безымянный фильм о Вечных": None,
    "Безымянный фильм о мутантах": None,
}


def find_by_title():
    """Задача 1: Поиск фильмов по названию"""

    result = []

    q = input("Введите название фильма: ")

    for title, year in SMALL_DICT.items():
        if q.lower() in title.lower():
            result.append([year, title])

    if len(result) == 0:
        print("Ничего не найдено :(")
    else:
        for result_item in result:
            print(result_item[0], result_item[1])


def filter_by_year():
    """Задача 2: Фильтрация фильмов по году выхода"""

    result = []

    while True:
        year_input = input("Год: ")
        if year_input.isdigit():
            year_input = int(year_input)
            break
    while True:
        direction = input(f"[ДО {year_input}](1) или [ПОСЛЕ {year_input}](2): ")
        if int(direction) == 1 or int(direction) == 2:
            break
    else:
        print("Введите 1 или 2")

    for title, year in SMALL_DICT.items():
        if direction == "1" and none_avoiding_comparsion(year, "<=", year_input):
            (result.append([year, title]))
        elif direction == "2" and none_avoiding_comparsion(year, ">=", year_input):
            (result.append([year, title]))

    if len(result) == 0:
        print("Ничего не найдено :(")
    else:
        for result_item in result:
            print(result_item[0], result_item[1])


def print_all_titles():
    """2.2.I Попробуйте просто распечатать названия фильмов."""

    for title in SMALL_DICT:
        print(title)


def make_list_of_titles():
    """2.2.II Попробуйте собрать список названий фильмов."""
    result = []

    for title in SMALL_DICT:
        result.append(title)

    print(result)


def make_sorted_dict():
    """2.2.III Попробуйте собрать словарь
    (как исходный, но [фильтрованный(?)] сортированный по году)."""
    result = []

    while True:
        direction = input("[ПО ВОЗРАСТАНИЮ](1) или [ПО УБЫВАНИЮ](2): ")
        if int(direction) == 1 or int(direction) == 2:
            break
    else:
        print("Введите 1 или 2")

    def sorting_key(item):
        return float("inf") if not isinstance(item[1], int) else int(item[1])

    small_dict_copy = copy.copy(SMALL_DICT)

    result = dict(
        sorted(small_dict_copy.items(), key=sorting_key, reverse=int(direction) == 2)
    )

    print(result)


def make_list_of_dicts():
    """2.2.IV Попробуйте собрать список словарей в формате [{‘Человек-хрюк’: 2024}, ...]."""
    result = []

    for title, year in SMALL_DICT.items():
        result.append({title: year})

    print(result)


def _exit():
    os.system("cls" if os.name == "nt" else "clear")
    exit()


def none_avoiding_comparsion(value_1: any, direction: str, value_2: any):
    """Always positive result to None side"""
    if (direction == "<" or direction == "<=" or direction == "==") and value_1 is None:
        return True
    elif (
        direction == ">" or direction == ">=" or direction == "=="
    ) and value_2 is None:
        return True
    elif direction == "==" and value_1 is None and value_2 is None:
        return True
    elif value_1 is None or value_2 is None:
        return False
    else:
        if direction == "<=":
            return int(value_1) <= int(value_2)
        elif direction == ">=":
            return int(value_1) >= int(value_2)
        elif direction == "<":
            return int(value_1) < int(value_2)
        elif direction == ">":
            return int(value_1) > int(value_2)
        elif direction == "==":
            return int(value_1) == int(value_2)


MENU = [
    {"num": 1, "print_name": "найти по названию", "exec": "find_by_title"},
    {"num": 2, "print_name": "отфильтровать по году выхода", "exec": "filter_by_year"},
    {"num": 3, "print_name": "показать все названия", "exec": "print_all_titles"},
    {"num": 4, "print_name": "собрать список названий", "exec": "make_list_of_titles"},
    {
        "num": 5,
        "print_name": "собрать словарь, отсортированный по году",
        "exec": "make_sorted_dict",
    },
    {"num": 6, "print_name": "собрать список словарей", "exec": "make_list_of_dicts"},
    {"num": 7, "print_name": "выход", "exec": "_exit"},
]


def main():
    """simple menu"""
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print("ДЗ №19. Работа с фильмами в Python.")
        print("Выберите действие:")
        for menu_item in MENU:
            print(f"{menu_item['num']}. {menu_item['print_name']}")

        choice = input("Введите номер: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in range(1, len(MENU) + 1):
                globals()[MENU[choice - 1]["exec"]]()
                input("Нажмите Enter для продолжения...")

                main()
            else:
                print("Некорректный выбор. Пожалуйста, выберите номер из списка.")
                input("Нажмите Enter для продолжения...")
                main()
        else:
            print("Некорректный выбор. Пожалуйста, выберите номер из списка.")
            input("Нажмите Enter для продолжения...")
            main()
    except KeyboardInterrupt:
        _exit()


main()
