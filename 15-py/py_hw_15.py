from datetime import datetime

"""
Задание 1
"""


def convert_and_print_seconds(seconds):
    """
    convert amount of seconds to years, months, days, hours, minutes and seconds
    and print result
    """
    second_duration = 1
    minute_duration = second_duration * 60
    hour_duration = minute_duration * 60
    day_duration = hour_duration * 24
    month_duration = day_duration * 30.4375
    year_duration = month_duration * 12

    years_qty = seconds // year_duration
    remaining_seconds = seconds % year_duration
    months_qty = remaining_seconds // month_duration
    remaining_seconds %= month_duration
    days_qty = remaining_seconds // day_duration
    remaining_seconds %= day_duration
    hours_qty = remaining_seconds // hour_duration
    remaining_seconds %= hour_duration
    minutes_qty = remaining_seconds // minute_duration
    seconds_qty = remaining_seconds % minute_duration

    print(
        f"""
    В указанном количестве секунд ({seconds}):
    лет: {    int(years_qty  ) }
    месяцев: {int(months_qty ) }
    дней: {   int(days_qty   ) }
    часов: {  int(hours_qty  ) }
    минут: {  int(minutes_qty) }
    секунд: { int(seconds_qty) }
    """
    )


now = round(datetime.timestamp(datetime.now()))
convert_and_print_seconds(now)
user_input = input("seconds: ")
convert_and_print_seconds(int(user_input))


"""
Задание 2
"""


def temperature_converter(celsius):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    reomur = celsius * 4 / 5
    print(
        f"""
    Температура в грдусах Кельвина: {round(kelvin,2)} [K]
    Температура в грдусах Фаренгейта: {round(fahrenheit,2)} [°F]
    Температура в грдусах Реомюра: {round(reomur,2)} [°Ré]
    """
    )


user_input = float(input("Введите температуру в градусах Цельсия: "))
temperature_converter(user_input)
