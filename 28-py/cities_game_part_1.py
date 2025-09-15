"""
game "cities". part 1.
"""

import os
from pprint import pprint
from dataclasses import dataclass, field
from hw_27_file_classes import JsonFile  # file copypasted form hw27

os.chdir(os.path.dirname(os.path.abspath(__file__)))

@dataclass(order=True)
class City:
    """
    dataclass with validation and comparison by population
    """

    name: str = field(compare=False)
    population: int
    subject: str = field(compare=False)
    district: str = field(compare=False)
    latitude: float = field(compare=False)
    longitude: float = field(compare=False)
    is_used: bool = field(compare=False, default=False)

    def __validate_population(self) -> bool:
        if self.population < 0 or type(self.population) != int:
            print(ValueError("Population value error"))
            return False
        return True

    def __validate_name(self) -> bool:
        if not isinstance(self.name, str) or len(self.name) == 0:
            print(ValueError("Name value error"))
            return False
        return True

    def __post_init__(self) -> None:
        if not self.__validate_population():
            return
        if not self.__validate_name():
            return

    def __eq__(self, other) -> bool:
        return self.population == other.population

    def __ne__(self, other) -> bool:
        return self.population != other.population


class CitiesSerializer:
    """
    creates inner list of dicts from JSON data
    """

    def __init__(self, city_data:list[dict]) -> None:
        # main functional here
        self.__cities = []
        for city in city_data:
            self.__cities.append(City(
                name=city["name"],
                population=city["population"],
                subject=city["subject"],
                district=city["district"],
                latitude=city["coords"]["lat"],
                longitude=city["coords"]["lon"],
            ))

    def get_all_cities(self) -> list[City]:
        """
        return internal list
        """
        return self.__cities

if __name__ == "__main__":
    cities_file = JsonFile("cities.json")
    serializer = CitiesSerializer(cities_file.read())
    full_list = serializer.get_all_cities()

    print(len(full_list))

    print("\ntop 5 lowest population\n".upper())
    full_list.sort(key=lambda x: float(x.population), reverse=False)
    pprint(full_list[:5])

    print("\ntop 5 northest\n".upper())
    full_list.sort(key=lambda x: float(x.latitude), reverse=True)
    pprint(full_list[:5])

    print("\ntop 5 westest\n".upper())
    full_list.sort(key=lambda x: float(x.longitude), reverse=False)
    pprint(full_list[:5])
