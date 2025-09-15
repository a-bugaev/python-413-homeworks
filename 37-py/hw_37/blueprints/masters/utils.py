"""
hw_37/blueprints/masters/utils.py
Функции для работы с записями на прием
"""

from hw_37.peewee_db import Master

def master_to_dict(master: Master) -> dict:
    """
    Преобразование объекта Master в словарь
    :param master: объект Master
    :return: dict
    """
    kyes = ["first_name", "last_name", "middle_name", "phone"]
    return {key: str(getattr(master, key)) for key in kyes}


def validate_master_data(data: dict) -> None:
    """
    Валидация данных для мастера
    :param data: dict
    """
    if not data.get("first_name"):
        raise ValueError("Пропущено обязательное поле: Имя")
    if not data.get("last_name"):
        raise ValueError("Пропущено обязательное поле: Фамилия")
    if not data.get("phone"):
        raise ValueError("Пропущено обязательное поле: Телефон")

    if len(str(data.get("first_name"))) > 50:
        raise ValueError("Значение превышает допустимую длинну: Имя")
    if len(str(data.get("last_name"))) > 50:
        raise ValueError("Значение превышает допустимую длинну: Фамилия")
    if len(str(data.get("middle_name"))) > 50:
        raise ValueError("Значение превышает допустимую длинну: Отчество")
    if len(str(data.get("phone"))) > 20:
        raise ValueError("Значение превышает допустимую длинну: Телефон")

    for key in data.keys():
        if key not in [
            "first_name",
            "last_name",
            "middle_name",
            "phone",
        ]:
            raise ValueError("Ключ не распознан")
