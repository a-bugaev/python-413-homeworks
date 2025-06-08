"""
HW 36. Flask API
app.py: эндпоинты
"""

import json
from flask import Flask, jsonify, request
from peewee_actions import *
from utils import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/masters")
def get_masters() -> (str, int, dict):
    """
    Получить список всех мастеров
    :return: json string: str, status code: int, headers: dict
    """
    masters = get_all_masters()
    return (
        json.dumps(masters, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/masters/<int:master_id>")
def get_master_by_id(master_id: int) -> (str, int, dict) | (str, int):
    """
    Получить информацию о мастере по ID
    :param master_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """
    master = get_master_by_id(master_id)
    if master:
        return (
            json.dumps(master, ensure_ascii=False),
            200,
            {"Content-Type": "application/json; charset=utf-8"},
        )
    return "Not found", 404


@app.route("/masters", methods=["POST"])
def add_master() -> (str, int, dict):
    """
    Добавить нового мастера
    :return: json string: str, status code: int, headers: dict
    """
    data = request.json
    master = add_master(**data)
    return (
        json.dumps(master, ensure_ascii=False),
        201,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/masters/<int:master_id>", methods=["PUT"])
def update_master(master_id) -> (str, int, dict) | (str, int):
    """
    Обновить информацию о мастере
    :param master_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """
    data = request.json
    master = update_master(master_id, **data)
    if master:
        return (
            json.dumps(master, ensure_ascii=False),
            200,
            {"Content-Type": "application/json; charset=utf-8"},
        )
    return "Not found", 404


@app.route("/masters/<int:master_id>", methods=["DELETE"])
def delete_master(master_id) -> (str, int):
    """
    Удалить мастера
    :param master_id: int
    :return: status/error string: str, status code: int
    """
    master = delete_master(master_id)
    if master:
        return "Deleted", 204
    return "Not found", 404


@app.route("/appointments?sort_by=<str:sort_by>&direction=<str:direction>")
def get_appointments() -> (str, int, dict):
    """
    Получить все записи на услуги с опциональной сортировкой
    :return: json string: str, status code: int, headers: dict
    """

    appointments = get_all_appointments(sort_by, direction)

    return (
        json.dumps(appointments, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments/<int:appointment_id>")
def get_appointment_by_id(appointment_id) -> (str, int, dict) | (str, int):
    """
    Получить информацию о записи по ID
    :param appointment_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """
    appointment = get_appointment_by_id(appointment_id)
    if appointment:
        return (
            json.dumps(appointment, ensure_ascii=False),
            200,
            {"Content-Type": "application/json; charset=utf-8"},
        )
    return "Not found", 404


@app.route("/appointointments/master/<int:master_id>")
def get_appointments_by_master(master_id) -> (str, int, dict):
    """
    Получить все записи для заданного мастера
    :param master_id: int
    :return: json string: str, status code: int, headers: dict
    """
    appointments = get_appointments_by_master(master_id)
    return (
        json.dumps(appointments, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments", methods=["POST"])
def add_appointment() -> (str, int, dict):
    """
    Создать новую запись
    :return: json string: str, status code: int, headers: dict
    """
    data = request.json
    appointment = add_appointment(**data)
    return (
        json.dumps(appointment, ensure_ascii=False),
        201,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments/<int:appointment_id>", methods=["PUT"])
def update_appointment(appointment_id):
    """
    Обновить запись
    :param appointment_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """
    data = request.json
    appointment = update_appointment(appointment_id, **data)
    if appointment:
        return (
            json.dumps(appointment, ensure_ascii=False),
            200,
            {"Content-Type": "application/json; charset=utf-8"},
        )
    return "Not found", 404


@app.route("/appointments/<int:appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):
    """
    Удалить запись
    :param appointment_id: int
    :return: status/error string: str, status code: int
    """
    appointment = delete_appointment(appointment_id)
    if appointment:
        return "Deleted", 204
    return "Not found", 404


if __name__ == "__main__":
    # Создание таблиц, если они не существуют
    if not (check_db_file_existance or check_tables_existance):
        create_tables_and_populate()

    # Запуск веб-сервера
    app.run(debug=True)

# TODO: turn on mypy and pylint