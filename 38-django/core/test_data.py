"""
core/test_data.py
"""

MASTERS = [
    {
        "id": 1,
        "name": "Эльдар 'Бритва' Рязанов",
        "description": "Мастер с опытом работы — владелец непревзойденной техники, чьи 'бритвы' (игр.) делают прически идеальными и гладкими.",
        "work_experience": 10,
    },
    {
        "id": 2,
        "name": "Зоя 'Ножницы' Космодемьянская",
        "description": "Мастер с 8-летним опытом — настоящий виртуоз 'ножниц', каждый клиент получает уникальный и точный до мелочей образ.",
        "work_experience": 8,
    },
    {
        "id": 3,
        "name": "Борис 'Фен' Пастернак",
        "description": "Мастер с 12-летним опытом — творец форм, его 'фен' превращает волосы в легкие, вьющиеся и элегантные произведения искусства.",
        "work_experience": 12,
    },
    {
        "id": 4,
        "name": "Иннокентий 'Лак' Смоктуновский",
        "description": "Мастер с 15-летним опытом — маг 'лака', создавая на прядях глянцевую или матовую чарму, словно на волшебной палитре.",
        "work_experience": 15,
    },
    {
        "id": 5,
        "name": "Раиса 'Бигуди' Горбачёва",
        "description": "Мастер с 9-летним опытом — молчаливая гувернантка стилей, ее 'бигуди' (игр.) всегда приводят в идеальную, неподдельную форму.",
        "work_experience": 9,
    },
]


SERVICES = [
    {
        "id": 1,
        "name": "Стрижка под 'Горшок'",
        "description": "Классическая стрижка",
        "price": 500,
    },
    {
        "id": 2,
        "name": "Укладка 'Взрыв на макаронной фабрике'",
        "description": "Стильная укладка",
        "price": 700,
    },
    {
        "id": 3,
        "name": "Королевское бритье опасной бритвой",
        "description": "Роскошное бритье",
        "price": 1000,
    },
    {
        "id": 4,
        "name": "Окрашивание 'Жизнь в розовом цвете'",
        "description": "Модное окрашивание",
        "price": 1200,
    },
    {
        "id": 5,
        "name": "Мытье головы 'Душ впечатлений'",
        "description": "Релаксирующее мытье",
        "price": 300,
    },
    {
        "id": 6,
        "name": "Стрижка бороды 'Боярин'",
        "description": "Стильная стрижка бороды",
        "price": 600,
    },
    {
        "id": 7,
        "name": "Массаж головы 'Озарение'",
        "description": "Релаксирующий массаж",
        "price": 800,
    },
    {
        "id": 8,
        "name": "Укладка 'Ветер в голове'",
        "description": "Легкая укладка",
        "price": 400,
    },
    {
        "id": 9,
        "name": "Плетение косичек 'Викинг'",
        "description": "Стильное плетение",
        "price": 900,
    },
    {
        "id": 10,
        "name": "Полировка лысины до блеска",
        "description": "Блестящая полировка",
        "price": 200,
    },
]


STATUS_NEW = "новая"
STATUS_CONFIRMED = "подтвержденная"
STATUS_CANCELLED = "отмененная"
STATUS_COMPLETED = "выполненная"


ORDERS = [
    {
        "id": 1,
        "client_name": "Пётр 'Безголовый' Головин",
        "services": [1, 10],
        "master_id": 1,
        "date": "2025-03-20",
        "status": STATUS_NEW,
    },
    {
        "id": 2,
        "client_name": "Василий 'Кудрявый' Прямиков",
        "services": [2],
        "master_id": 2,
        "date": "2025-03-21",
        "status": STATUS_CONFIRMED,
    },
    {
        "id": 3,
        "client_name": "Афанасий 'Бородач' Бритвенников",
        "services": [3, 6, 7],
        "master_id": 3,
        "date": "2025-03-19",
    },
]


def get_order_ids():
    """
    возвращает список id заказов
    """
    return [order["id"] for order in ORDERS]


def get_master_ids():
    """
    возвращает список id мастера
    """
    return [master["id"] for master in MASTERS]


def get_service_ids():
    """
    возвращает список id услуг
    """
    return [service["id"] for service in SERVICES]


def get_order_by_id(order_id):
    """
    упрощает сборку контекста для страницы
    """
    for order in ORDERS:
        if order["id"] == order_id:
            return order
    return None


def get_master_by_id(master_id):
    """
    упрощает сборку контекста для страницы
    """
    for master in MASTERS:
        if master["id"] == master_id:
            return master
    return None


def get_service_by_id(service_id):
    """
    упрощает сборку контекста для страницы
    """
    for service in SERVICES:
        if service["id"] == service_id:
            return service
    return None
