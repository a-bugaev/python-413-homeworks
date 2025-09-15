"""
    HW_24. One-line funcs
"""

from pprint import pprint
from typing import Dict, Set, List, Any

# 1
from marvel import full_dict

# 2
user_input: str = input("Numbers separated by space:\n")
user_input_list: List[str] = user_input.split(" ")
user_input_list_nums: List[Any] = list(
    map(lambda i: int(i) if i.isdigit() else None, user_input_list)
)

# 3
repacked_marvel_data: List[Dict[str, Any]] = [
    {"id": film_id, **film} for film_id, film in full_dict.items()
]
print("\n 3 repacked_marvel_data:\n")
pprint(repacked_marvel_data)

# 4
filtered_by_user_input: List[Dict[str, Any]] = list(
    filter(lambda film: int(film["id"]) in user_input_list_nums, repacked_marvel_data)
)
print("\n 4 filtered_by_user_input:\n")
pprint(filtered_by_user_input)

# 5
directors_set: Set[str] = {film["director"] for film in repacked_marvel_data}
print("\n 5 directors_set:\n")
pprint(directors_set)

# 6
src_dict_with_stringified_years: Dict[int, Dict[str, Any]] = {
    film_id: {**film, "year": str(film["year"])}
    for (film_id, film) in full_dict.items()
}
print("\n 6 src_dict_with_stringified_years:\n")
pprint(src_dict_with_stringified_years)
print("year types")
print(
    [type(film["year"]) for (film_id, film) in src_dict_with_stringified_years.items()]
)

# 7
starts_with_ch: List[Dict[str, Any]] = list(
    filter(
        lambda film: (
            film["title"][0].lower() == "ч" if isinstance(film["title"], str) else False
        ),
        repacked_marvel_data,
    )
)
print("\n 7 starts_with_ch:\n")
pprint(starts_with_ch)

# 8
sorted_by_title: Dict[int, Dict[str, Any]] = dict(
    zip(
        range(0, len(full_dict) - 1),
        sorted(
            full_dict.values(),
            key=lambda film: film["title"] if isinstance(film["title"], str) else "",
        ),
    )
)
print("\n 8 sorted_by_title:\n")
pprint(sorted_by_title)

# 9
sorted_by_title_and_year: Dict[int, Dict[str, Any]] = dict(
    zip(
        range(0, len(full_dict) - 1),
        sorted(
            full_dict.values(),
            key=lambda film: (
                film["title"] if isinstance(film["title"], str) else "",
                film["year"] if isinstance(film["year"], int) else float("inf"),
            ),
        ),
    )
)
print("\n 9 sorted_by_title_and_year:\n")
pprint(sorted_by_title_and_year)

# 10
filtered_and_sorted: List[Dict[str, Any]] = list(
    sorted(
        filter(lambda film: film["id"] in user_input_list_nums, repacked_marvel_data),
        key=lambda film: film["title"] if isinstance(film["title"], str) else "",
    )
)
print("\n 10 filtered_and_sorted:\n")
pprint(filtered_and_sorted)

# 11

# screenshot attached
