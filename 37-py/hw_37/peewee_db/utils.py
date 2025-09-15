"""
hw_37/peewee_db/utils.py
Файл для работы с базой данных
"""

import os
from dotenv import load_dotenv
from peewee import SqliteDatabase
from .models import Appointment, Master, Service, MasterService, AppointmentService

load_dotenv()

DB_FILE_PATH = os.getenv("DB_FILE_PATH")
DB = SqliteDatabase(DB_FILE_PATH)


def create_tables():
    """
    Создание всех таблиц
    """
    DB.connect()
    DB.create_tables([Master, Service, Appointment, MasterService, AppointmentService])
    DB.close()


def populate_db():
    """
    Наполнение таблиц данными
    """
    DB.connect()

    master_data = [
        {
            "first_name": "Татьяна",
            "last_name": "Иванова",
            "middle_name": "Михайловна",
            "phone": "+53778541390",
        },
        {
            "first_name": "Василий",
            "last_name": "Сидоров",
            "middle_name": "Петрович",
            "phone": "+06997643570",
        },
    ]
    Master.insert_many(master_data).execute()

    services_data = [
        {"title": "Стрижка мужская модельная", "description": "-", "price": 600},
        {"title": "Помывка головы", "description": "-", "price": 300},
        {"title": "Окрашивание волос", "description": "-", "price": 1000},
        {"title": "Простое бритье", "description": "-", "price": 200},
        {"title": "Стайлинг бороды", "description": "-", "price": 500},
    ]
    Service.insert_many(services_data).execute()

    masters = {master.id: master for master in Master.select()}

    appointment_data = [
        {
            "client_name": "Клиент Первый",
            "client_phone": "+70527416207",
            "master": masters[1],
            "status": "Подана заявка",
            "comment": "текст комментария для Первого",
        },
        {
            "client_name": "Клиентка Вторая",
            "client_phone": "+72655470674",
            "master": masters[2],
            "status": "Запись подтверждена",
            "comment": "текст комментария для Второй",
        },
        {
            "client_name": "Клиент Третий",
            "client_phone": "+39699848096",
            "master": masters[1],
            "status": "Услуга оплачена",
            "comment": "текст комментария для Третьего",
        },
        {
            "client_name": "Клиентка Четвертая",
            "client_phone": "+75926060365",
            "master": masters[2],
            "status": "Услуга оказана",
            "comment": "текст комментария для Четвёртой",
        },
    ]
    appointments = []
    for data in appointment_data:
        app = Appointment.create(
            client_name=data["client_name"],
            client_phone=data["client_phone"],
            master=data["master"],
            status=data["status"],
            comment=data["comment"],
        )
        appointments.append(app.id)

    MasterService.insert_many(
        [
            {"master": 1, "service": 1},
            {"master": 1, "service": 2},
            {"master": 1, "service": 3},
            {"master": 1, "service": 4},
            {"master": 1, "service": 5},
            {"master": 2, "service": 1},
            {"master": 2, "service": 2},
            {"master": 2, "service": 3},
            {"master": 2, "service": 4},
            {"master": 2, "service": 5},
        ]
    ).execute()

    appointment_service_data = [
        {"appointment": appointments[0], "service": 1},
        {"appointment": appointments[0], "service": 4},
        {"appointment": appointments[1], "service": 2},
        {"appointment": appointments[1], "service": 3},
        {"appointment": appointments[2], "service": 1},
        {"appointment": appointments[2], "service": 5},
        {"appointment": appointments[3], "service": 2},
        {"appointment": appointments[3], "service": 3},
    ]

    AppointmentService.insert_many(appointment_service_data).execute()

    DB.close()


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
