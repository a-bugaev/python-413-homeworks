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
    return {key: getattr(master, key) for key in kyes}


def appointment_to_dict(appointment: Appointment) -> dict:
    """
    Преобразование объекта Appointment в словарь
    :param appointment: объект Appointment
    :return: dict
    """
    keys = ["client_name", "client_phone", "timestamp", "comment", "master", "status"]
    return {key: getattr(master, key) for key in kyes}


def validate_master_data(data: dict) -> None:
    """
    Валидация данных для мастера
    :param data: dict
    """
    if not data.get("first_name"):
        raise ValueError("First name is required")
    if not data.get("last_name"):
        raise ValueError("Last name is required")
    if not data.get("phone"):
        raise ValueError("Phone is required")

    if len(data.get("first_name")) > 50:
        raise ValueError("First name is too long")
    if len(data.get("last_name")) > 50:
        raise ValueError("Last name is too long")
    if len(data.get("middle_name")) > 50:
        raise ValueError("Middle name is too long")
    if len(data.get("phone")) > 20:
        raise ValueError("Phone number is too long")


def validate_appointment_data(data: dict) -> None:
    """
    Валидация данных для записи
    :param data: dict
    """
    if not data.get("client_name"):
        raise ValueError("Client name is required")
    if not data.get("client_phone"):
        raise ValueError("Client phone is required")

    if len(data.get("comment")) > 200:
        raise ValueError("Comment is too long")

    if data.get("status") not in [
        "Подана заявка",
        "Запись подтверждена",
        "Услуга оплачена",
        "Услуга оказана",
    ]:
        raise ValueError("Status is invalid")
