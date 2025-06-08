"""
HW 36. Flask API
peewee_actions.py: взаимодействие с бд
"""

import os
from peewee import SqliteDatabase
from homework_35_copypaste import (
    Master,
    Appointment,
    create_tables,
    populate_db,
    DB_FILE_PATH,
    DB,
)
from utils import *


def get_all_masters() -> list[dict]:
    """
    Получить список всех мастеров
    :return:
    """

    DB.connect()

    masters = Master.select()
    master_dicts = []
    for master_inst in masters:
        master_dicts.append(master_to_dict(master_inst))

    DB.close()

    return master_dicts


def get_master_by_id(master_id: int) -> dict:
    """
    Получить информацию о мастере по ID
    :param master_id:
    :return:
    """

    DB.connect()

    master_inst = Master.get(Master.id == master_id)
    master_dict = master_to_dict(master_inst)

    DB.close()

    return master_dict


def add_master(master_data: dict) -> int:
    """
    Добавить нового мастера
    :param master_data:
    :return:
    """
    DB.connect()

    validate_master_data(master_data)
    new_master_id = Master.create(**master_data)

    DB.close()

    return new_master_id


def update_master(master_id: int, master_data: dict) -> int:
    """
    Обновить информацию о мастере
    :param master_id:
    :param master_data:
    :return:
    """

    DB.connect()

    validate_master_data(master_data)
    master_inst = Master.get(Master.id == master_id)
    for key, value in master_data.items():
        setattr(master_inst, key, value)
    master_inst.save()

    DB.close()

    return master_id


def delete_master(master_id: int) -> int:
    """
    Удалить мастера
    :param master_id:
    :return:
    """

    DB.connect()

    Master.get(Master.id == master_id).delete_instance()

    DB.close()

    return master_id


def get_all_appointments(sort_by: str = "id", direction: str = "asc") -> list[dict]:
    """
    Получить все записи на услуги с опциональной сортировкой
    :return:
    """
    DB.connect()

    sort_by = getattr(Appointment, sort_by)
    if direction == "desc":
        appointments = Appointment.select().order_by(sort_by).desc()
    else:
        appointments = Appointment.select().order_by(sort_by)

    appointments_dicts = []
    for appointment_inst in appointments:
        appointment_dict = appointment_to_dict(appointment_inst)
        appointments_dicts.append(appointment_dict)

    DB.close()

    return


def get_appointment_by_id(appointment_id: int) -> dict:
    """
    Получить запись по ID
    :param appointment_id:
    :return:
    """

    DB.connect()

    appointment_inst = Appointment.get_by_id(appointment_id)
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

    appointments_insts = Appointment.select().where(Appointment.master_id == master_id)

    appointments_dicts = []
    for appointments_inst in appointments_insts:
        appointments_dicts.append(appointment_to_dict(appointments_inst))

    DB.close()

    return appointments


def update_appointment(appointment_id: int, appointment_data: dict):
    """
    Обновить запись на услугу
    :param appointment_id:
    :param appointment_data:
    :return:
    """

    DB.connect()

    validate_appointment_data(appointment_data)
    appointment = get_appointment_by_id(appointment_id)
    for key, value in appointment_data.items():
        setattr(appointment, key, value)
    appointment.save()

    DB.close()

    return appointment_id


def delete_appointment(appointment_id: int) -> int:
    """
    Удалить запись на услугу
    :param appointment_id:
    :return:
    """

    DB.connect()

    appointment = get_appointment_by_id(appointment_id)
    appointment.delete_instance()

    DB.close()

    return appointment_id


def create_tables_and_populate():
    """
    создать таблицы и внести данные
    :return:
    """
    create_tables()
    populate_db()


def check_db_file_existance():
    """
    Проверяет, существует ли файл базы данных
    :return:
    """
    return os.path.isfile(DB_FILE)

def check_tables_existance():
    """
    Проверяет, существуют ли таблица
    :return:
    """
    return Master.table_exists() and Appointment.table_exists()