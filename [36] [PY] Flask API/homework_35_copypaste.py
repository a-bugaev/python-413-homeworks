"""
    HW 35
    PeeWee‑модели и скрипт наполнения БД «Барбершоп»
"""

import os
from datetime import datetime
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    TextField,
    DecimalField,
    DateTimeField,
    ForeignKeyField,
    CompositeKey,
    Check,
)

DB_FILE_PATH = "./barbershop.db"
DB = SqliteDatabase(DB_FILE_PATH)


class Master(Model):
    """
    Описание таблицы мастеров
    """

    first_name = CharField(max_length=50, null=False)
    last_name = CharField(max_length=50, null=False)
    middle_name = CharField(max_length=50, null=True)
    phone = CharField(max_length=20, unique=True)

    class Meta:
        database = DB


class Service(Model):
    """
    Описание таблицы оказываемых услуг
    """

    title = CharField(max_length=100, unique=True)
    description = TextField(null=True)
    price = DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        database = DB


class Appointment(Model):
    """
    Описание таблицы записей на обслуживание
    """

    client_name = CharField(null=False)
    client_phone = CharField(null=False)
    timestamp = DateTimeField(default=lambda: datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))
    comment = CharField(max_length=200)
    master = ForeignKeyField(Master, backref="appointments")
    status = CharField(
        null=False,
        constraints=[
            Check(
                """
                status IN (
                    'Подана заявка',
                    'Запись подтверждена',
                    'Услуга оплачена',
                    'Услуга оказана'
                )
                """.replace(
                    "    ", ""
                )
            )
        ],
        default="Подана заявка",
    )

    class Meta:
        database = DB


class MasterService(Model):
    """
    Описание связующей таблицы - мастера и оказываемые ими услуги. (Все делают всё для простоты)
    """

    master = ForeignKeyField(Master, backref="services_offered")
    service = ForeignKeyField(Service)

    class Meta:
        database = DB
        primary_key = CompositeKey("master", "service")


class AppointmentService(Model):
    """
    Описание связующей таблицы - записи на обслуживание и заказанные услуги.
    """

    appointment = ForeignKeyField(Appointment, backref="services")
    service = ForeignKeyField(Service)

    class Meta:
        database = DB
        primary_key = CompositeKey("appointment", "service")


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


def test_prints():
    """
    Вывод данных из созданной базы
    """

    DB.connect()

    print("Мастера:")
    for master in Master.select():
        print(
            f"""
            ID: {master.id}
            Имя: {master.first_name}
            Фамилия: {master.last_name}
            Отчество: {master.middle_name}
            Телефон: {master.phone}
            """.replace(
                "    ", ""
            )
        )

    print("\nУслуги:")
    for service in Service.select():
        print(
            f"""
            ID: {service.id}
            Название: {service.title}
            Описание: {service.description}
            Цена: {service.price}
            """.replace(
                "    ", ""
            )
        )

    print("\nЗаписи:")
    appointments = Appointment.select().order_by(Appointment.id)
    appointments_with_services = appointments.prefetch(AppointmentService)

    for appointment in appointments_with_services:
        services_str = ", ".join(service.service.title for service in appointment.services)
        print(
            f"""
            ID: {appointment.id}
            Имя Клиента: {appointment.client_name}
            Телефон Клиента: {appointment.client_phone}
            Дата_Время: {appointment.timestamp}
            Мастер: {appointment.master.last_name} {appointment.master.first_name} {appointment.master.middle_name}
            Статус: {appointment.status}
            Услуги: {services_str}
            Комментарий: {appointment.comment}
            """.replace(
                "    ", ""
            )
        )

    DB.close()


def main():

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isfile(DB_FILE_PATH):
        os.remove(DB_FILE_PATH)

    create_tables()
    populate_db()
    test_prints()


if __name__ == "__main__":
    main()
