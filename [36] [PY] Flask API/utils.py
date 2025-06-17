"""
HW 36. Flask API
utils.py: вспомогательные функции
"""

from homework_35_copypaste import Master, Appointment


def master_to_dict(master: Master) -> dict:
    """
    Преобразование объекта Master в словарь
    :param master: объект Master
    :return: dict
    """
    kyes = ["first_name", "last_name", "middle_name", "phone"]
    return {key: str(getattr(master, key)) for key in kyes}


def appointment_to_dict(appointment: Appointment) -> dict:
    """
    Преобразование объекта Appointment в словарь
    :param appointment: объект Appointment
    :return: dict
    """
    keys = ["client_name", "client_phone", "timestamp", "comment", "master", "status"]
    return {key: str(getattr(appointment, key)) for key in keys}


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
