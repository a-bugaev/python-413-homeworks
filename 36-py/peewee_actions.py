"""
HW 36. Flask API
peewee_actions.py: взаимодействие с бд
"""

import os
from peewee import DoesNotExist
from homework_35_copypaste import (
    Master,
    Appointment,
    create_tables,
    populate_db,
    DB_FILE_PATH,
    DB,
)
from utils import (
    master_to_dict,
    appointment_to_dict,
    validate_master_data,
    validate_appointment_data,
)


def get_all_masters() -> list[dict]:
    """
    Получить список всех мастеров
    :return:
    """

    try:
        DB.connect()
        masters = Master.select()
        master_dicts = []
        for master_inst in masters:
            master_dicts.append(master_to_dict(master_inst))
        DB.close()
    except DoesNotExist as e:
        raise DoesNotExist("Данные не найдены") from e

    return master_dicts


def get_master_by_id(master_id: int) -> dict | None:
    """
    Получить информацию о мастере по ID
    :param master_id:
    :return: dict
    """

    try:
        DB.connect()
        master_inst = Master.get(Master.id == master_id)  # type: ignore[attr-defined]
        DB.close()
    except DoesNotExist as e:
        raise DoesNotExist(f"Нет мастера под ID {master_id}") from e

    return master_to_dict(master_inst)


def add_master(master_data: dict) -> int:
    """
    Добавить нового мастера
    :param master_data:
    :return:
    """

    DB.connect()
    validate_master_data(master_data)
    new_master_obj = Master.create(**master_data)
    DB.close()

    return new_master_obj.id


def update_master(master_id: int, master_data: dict) -> int:
    """
    Обновить информацию о мастере
    :param master_id:
    :param master_data:
    :return:
    """

    DB.connect()

    try:
        master_inst = Master.get(Master.id == master_id)  # type: ignore[attr-defined]
    except DoesNotExist as e:
        raise DoesNotExist(f"Нет мастера под ID {master_id}") from e

    src_master_dict = master_to_dict(master_inst)
    upd_master_dict = {**src_master_dict, **master_data}
    validate_master_data(upd_master_dict)

    for key, value in upd_master_dict.items():
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
    try:
        Master.get(Master.id == master_id).delete_instance()  # type: ignore[attr-defined]
    except DoesNotExist as e:
        raise DoesNotExist(f"Нет мастера под ID {master_id}") from e

    DB.close()

    return master_id


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
    return os.path.isfile(DB_FILE_PATH)


def check_tables_existance():
    """
    Проверяет, существуют ли таблица
    :return:
    """
    return Master.table_exists() and Appointment.table_exists()


def remove_db_file():
    """
    Удаляет файл базы данных
    :return:
    """
    if os.path.isfile(DB_FILE_PATH):
        os.remove(DB_FILE_PATH)
