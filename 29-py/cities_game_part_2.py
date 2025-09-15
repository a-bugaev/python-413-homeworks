"""
HW 29. Cities game. Part 2.
"""

import sys
import random
from cities_game_part_1 import City, CitiesSerializer
from hw_27_file_classes import JsonFile


class CityGame:
    """
    Отвечает за внутреннюю игровую логику, должен обеспечивать реализацию правил игры «Города»
    """

    def __init__(self, cities_serializer: CitiesSerializer):
        self.cities = cities_serializer.get_all_cities()
        self.current_city: None | City = None
        self.possible_cities: list[City] = self.cities

    def __get_last_letter(self, city_name: str) -> str:
        for i in range(len(city_name) - 1, -1, -1):
            if city_name[i] not in {"ь", "ы", "й"}:
                return city_name[i]
        return city_name[0]

    def __find_possible_cities(self):
        not_used_cities = [city for city in self.cities if not city.is_used]
        if self.current_city:
            last_letter = self.__get_last_letter(self.current_city.name)
            self.possible_cities = [
                city
                for city in not_used_cities
                if city.name.lower().startswith(last_letter)
            ]
        else:
            self.possible_cities = not_used_cities

    def __validate_human_input(self, human_input: str) -> City | None:
        # find City
        city_inst: None | City = None
        for city in self.possible_cities:
            if city.name.lower() == human_input.lower():
                city_inst = city
                break
        if not city_inst:
            print("города нет в базе, либо он уже использован")
        return city_inst

    def start_game(self) -> str:
        """
        первый ход передаётся компьютеру
        цикл:
            ход компьютера
            проверка окончания игры
            ход игрока
            проверка окончания игры
        """
        print(
            'Игра "Города".\nПреимущественно города РФ.\nПоследние незначащие буквы отсекаются ("ь", "ы", "й").\nБудте внимательны с правописанием.\nCtrl+C для выхода'
        )
        while True:
            self.__find_possible_cities()

            self.computer_turn()

            if self.check_game_over():
                return "game over, you lose"

            while True:
                try:
                    if self.human_turn(input("Ваш ход: ")):
                        break
                except KeyboardInterrupt:
                    print('\nBye!')
                    sys.exit()
            if self.check_game_over():
                return "game over, you win"

    def human_turn(self, city_input: str) -> bool:
        """
        city_input:str - название города
        returns:bool - true если ход корректен, false в случае ошибки
        """
        validation_result = self.__validate_human_input(city_input)
        if validation_result:
            self.current_city = validation_result
            self.current_city.is_used = True
            print(
                f"Ваш город: {self.current_city.name} (Население: {self.current_city.population})."
            )
            return True
        return False

    def computer_turn(self) -> None:
        """
        случайно выбирает подходящий для хода город
        обновляет состяние игры
        возвращает City
        """
        self.current_city = random.choice(self.possible_cities)
        self.current_city.is_used = True
        print(
            f"Город компьютера: {self.current_city.name} (Население: {self.current_city.population})."
        )

    def check_game_over(self) -> bool:
        """
        проверка на возможность следующего хода
        return:bool
        """
        self.__find_possible_cities()
        return not bool(len(self.possible_cities))


class GameManager:
    """
    фасад, инкапсулирует взаимодействие между всеми компонентами игры
    """

    def __init__(
        self,
        json_file: JsonFile,
        cities_serializer: CitiesSerializer,
        city_game: CityGame,
    ):
        self.json_file = json_file
        self.cities_serializer = cities_serializer
        self.city_game = city_game

    def __call__(self) -> None:
        self.display_game_result(self.run_game())
        sys.exit()

    def run_game(self) -> str:
        """
        starts game, waits for game over, returns result as string
        """
        return self.city_game.start_game()

    def display_game_result(self, result: str) -> None:
        """
        выводит итоговый результат игры
        """
        print(result)

if __name__ == "__main__":
    cities_json_file = JsonFile("cities.json")
    cities_json_data = cities_json_file.read()
    cities_serializer_inst = CitiesSerializer(cities_json_data)
    city_game_inst = CityGame(cities_serializer_inst)
    game_manager = GameManager(cities_json_file, cities_serializer_inst, city_game_inst)
    game_manager()
