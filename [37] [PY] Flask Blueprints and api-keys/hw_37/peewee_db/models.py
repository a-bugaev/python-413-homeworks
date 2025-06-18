"""
hw_37/peewee_db/models.py
Модели для базы данных
"""

import os
from datetime import datetime
from peewee import (
    Model,
    CharField,
    TextField,
    DecimalField,
    DateTimeField,
    ForeignKeyField,
    CompositeKey,
    Check,
    SqliteDatabase,
)
from dotenv import load_dotenv

load_dotenv()

DB_FILE_PATH = os.getenv("DB_FILE_PATH")
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
