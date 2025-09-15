"""
hw_37/blueprints/appointments/utils.py
Функции для работы с записями на прием
"""

from hw_37.peewee_db import Appointment


def appointment_to_dict(appointment: Appointment) -> dict:
    """
    Преобразование объекта Appointment в словарь
    :param appointment: объект Appointment
    :return: dict
    """
    keys = ["client_name", "client_phone", "timestamp", "comment", "master", "status"]
    return {key: str(getattr(appointment, key)) for key in keys}


def validate_appointment_data(data: dict) -> None:
    """
    Валидация данных для записи
    :param data: dict
    """
    if not data.get("client_name"):
        raise ValueError("Пропущено обязательное поле: Имя клиента")
    if not data.get("client_phone"):
        raise ValueError("Пропущено обязательное поле: Телефон клиента")

    if len(str(data.get("comment"))) > 200:
        raise ValueError("Значение превышает допустимую длинну: Комментарий")

    if data.get("status"):
        if data.get("status") not in [
            "Подана заявка",
            "Запись подтверждена",
            "Услуга оплачена",
            "Услуга оказана",
        ]:
            raise ValueError("Некорректное значение статуса")

    for key in data.keys():
        if key not in [
            "client_name",
            "client_phone",
            "timestamp",
            "comment",
            "master",
            "status",
        ]:
            raise ValueError("Ключ не распознан")
