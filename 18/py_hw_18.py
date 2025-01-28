"""
    ДЗ №18: Генератор пословиц на основе случайных замен.
"""

import random

# source data

PROVERBS = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]

VARIANTS = [
    "кот",
    "шеф",
    "мозг",
    "лес",
    "фолк",
    "код",
    "рот",
    "мёд",
    "лук",
    "лес",
    "год",
    "час",
    "друг",
    "муж",
    "айфон",
    "стол",
    "нос",
    "сыр",
    "хлеб",
    "мир",
    "свет",
    "рок",
    "дед",
    "дом",
    "сон",
    "глаз",
    "торт",
    "драйв",
    "байк",
    "джаз",
    "грим",
    "рэп",
    "старт",
    "пинг-понг",
    "каприз",
    "драйф",
    "размах",
    "панк",
    "размер",
    "перекус",
    "блеск",
    "накал",
    "размен",
    "кураж",
    "форсаж",
    "прорыв",
]


# 1. Запрос на количество пословиц:


def get_proverbs_qty():
    while True:
        proverbs_qty = input("Количество пословиц: ")
        if proverbs_qty.isdigit():
            proverbs_qty = int(proverbs_qty)
            print('')
            break
        else:
            print("Некорректное значение")
    return proverbs_qty


proverbs_qty = get_proverbs_qty()

# 2. Инициализация списков:

results = []
proverbs = PROVERBS.copy()
variants = VARIANTS.copy()

# 3. Цикл для генерации пословиц:

for i in range(proverbs_qty):
    if len(proverbs) == 0 or len(variants) == 0:
        break
    proverbs_random = random.choice(proverbs)
    proverbs.remove(proverbs_random)
    variants_random = random.choice(variants)
    variants.remove(variants_random)
    if "ум" in proverbs_random:
        results.append(proverbs_random.replace("ум", variants_random))
    elif "Ум" in proverbs_random:
        results.append(proverbs_random.replace("Ум", variants_random.capitalize()))
    else:
        results.append(proverbs_random)

# 4. Вывод результата:

for number, result in enumerate(results):
    print(f"{number+1}) {result}\n")


"""
    Получим все возможные уникальные варианты пословиц и будем выдавать пользователю запрошенное количество, пока список не закончится.
"""

# 1. Переберём оба списка

results_2 = []
proverbs_2 = PROVERBS.copy()
variants_2 = VARIANTS.copy()

for proverbs_random in proverbs_2:
    for variants_random in variants_2:
        if "ум" in proverbs_random:
            results_2.append(proverbs_random.replace("ум", variants_random))
        elif "Ум" in proverbs_random:
            results_2.append(
                proverbs_random.replace("Ум", variants_random.capitalize())
            )
        else:
            results_2.append(proverbs_random)

# 2. Будем выдавать пользователю запрошенное количество пословиц, пока список не закончится.

print("_____________________\n")
print("Всего возможных уникальных пословиц: ", len(results_2), "\n")

while len(results_2) > 0:
    print(f"Осталось {len(results_2)} уникальных пословиц.\n")
    proverbs_qty = get_proverbs_qty()
    for i in range(proverbs_qty):
        if len(results_2) > 0:
            selected_proverb = random.choice(results_2)
            print(f"{i+1}) {selected_proverb}\n")
            results_2.remove(selected_proverb)
        else:
            print("Список пословиц закончился.")
            break
