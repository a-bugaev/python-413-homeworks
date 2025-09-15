"""
hw_37/blueprints/appointments/routes.py
Appointments routes group
"""

import os
from dotenv import load_dotenv
from peewee import SqliteDatabase, DoesNotExist
from hw_37.peewee_db import Appointment
from .utils import appointment_to_dict, validate_appointment_data


load_dotenv()

DB_FILE_PATH = os.getenv("DB_FILE_PATH")
DB = SqliteDatabase(DB_FILE_PATH)


def get_all_appointments(sort_by: str = "id", direction: str = "asc") -> list[dict]:
    """
    Получить все записи на услуги с опциональной сортировкой
    :return:
    """
    DB.connect()

    sort_by_attr = getattr(Appointment, sort_by)

    try:
        if direction == "desc":
            appointments = Appointment.select().order_by(sort_by_attr.desc())
        else:
            appointments = Appointment.select().order_by(sort_by_attr)
    except DoesNotExist as e:
        raise DoesNotExist("Данные не найдены") from e

    appointments_dicts = []
    for appointment_inst in appointments:
        appointment_dict = appointment_to_dict(appointment_inst)
        appointments_dicts.append(appointment_dict)

    DB.close()

    return appointments_dicts


def get_appointment_by_id(appointment_id: int) -> dict:
    """
    Получить запись по ID
    :param appointment_id:
    :return:
    """

    DB.connect()

    try:
        appointment_inst = Appointment.get_by_id(appointment_id)
    except DoesNotExist as e:
        raise DoesNotExist(f"Нет записи под ID {appointment_id}") from e

    appointment_dict = appointment_to_dict(appointment_inst)

    DB.close()

    return appointment_dict


def get_all_appointments_by_master(master_id: int) -> list[dict]:
    """
    Получить все записи для заданного мастера
    :param master_id:
    :return:
    """

    DB.connect()

    try:
        appointments_insts = Appointment.select().where(Appointment.master == master_id)
    except DoesNotExist as e:
        raise DoesNotExist(f"Нет записей c мастером под ID {master_id}") from e

    appointments_dicts = []
    for appointments_inst in appointments_insts:
        appointments_dicts.append(appointment_to_dict(appointments_inst))

    DB.close()

    return appointments_dicts


def add_appointment(appointment_data: dict) -> int:
    """
    Добавить новую запись на услугу
    :param appointment_data: dict
    :return: int - id созданной записи
    """

    DB.connect()

    validate_appointment_data(appointment_data)
    appointment_obj = Appointment.create(**appointment_data)

    DB.close()

    return appointment_obj.id


def update_appointment(appointment_id: int, appointment_data: dict):
    """
    Обновить запись на услугу
    :param appointment_id:
    :param appointment_data:
    :return:
    """

    DB.connect()

    try:
        appointment_inst = Appointment.get(
            Appointment.id == appointment_id  # type: ignore[attr-defined]
        )
    except DoesNotExist as e:
        raise DoesNotExist(f"Нет записи под ID {appointment_id}") from e

    src_appointment_dict = appointment_to_dict(appointment_inst)
    upd_appointment_dict = {**src_appointment_dict, **appointment_data}
    validate_appointment_data(upd_appointment_dict)

    for key, value in upd_appointment_dict.items():
        setattr(appointment_inst, key, value)

    appointment_inst.save()

    DB.close()

    return appointment_id


def delete_appointment(appointment_id: int) -> int:
    """
    Удалить запись на услугу
    :param appointment_id:
    :return:
    """

    DB.connect()

    try:
        appointment = Appointment.get(
            Appointment.id == appointment_id  # type: ignore[attr-defined]
        )
        appointment.delete_instance()
    except DoesNotExist as e:
        raise DoesNotExist(f"Нет записи под ID {appointment_id}") from e

    DB.close()

    return appointment_id
