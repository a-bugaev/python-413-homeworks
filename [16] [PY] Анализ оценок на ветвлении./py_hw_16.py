
"""
Запросить имя студента и его оценку, после чего классифицировать уровень знаний по шкале
"""

"""
Начальный уровень: 1, 2, 3
Средний уровень: 4, 5, 6
Достаточный уровень: 7, 8, 9
Высокий уровень: 10, 11, 12
"""

def classify(grade):
    if 1 <= grade <= 3:
        print(f"Уровень знаний студента {name} - начальный")
    elif 4 <= grade <= 6:
        print(f"Уровень знаний студента {name} - средний")
    elif 7 <= grade <= 9:
        print(f"Уровень знаний студента {name} - достаточный")
    elif 10 <= grade <= 12:
        print(f"Уровень знаний студента {name} - высокий")
    else:
        print("Некорректная оценка")


#тест

# for grade in range(0, 14):
#     print(grade)
#     classify(grade)

name = ''
while not name.isalpha():
    name = input("Введите имя студента: ")

grade = ''
while not grade.isdigit():
    grade = input("Введите оценку студента: ")
grade = int(grade)

classify(grade)