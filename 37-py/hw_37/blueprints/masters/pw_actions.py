"""
hw_37/blueprints/appointments/routes.py
Appointments routes group
"""

import os
from dotenv import load_dotenv
from peewee import SqliteDatabase, DoesNotExist
from hw_37.peewee_db import Master
from .utils import master_to_dict, validate_master_data

load_dotenv()

DB_FILE_PATH = os.getenv("DB_FILE_PATH")
DB = SqliteDatabase(DB_FILE_PATH)


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
