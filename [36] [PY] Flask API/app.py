"""
HW 36. Flask API
app.py: эндпоинты
"""

import json
from flask import Flask, request
from peewee import DoesNotExist
from peewee_actions import (
    get_all_masters,
    get_master_by_id,
    add_master,
    update_master,
    delete_master,
    get_all_appointments,
    get_appointment_by_id,
    get_all_appointments_by_master,
    add_appointment,
    update_appointment,
    delete_appointment,
    create_tables_and_populate,
    check_db_file_existance,
    check_tables_existance,
    remove_db_file,
)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/masters", methods=["GET"])
def ep_get_masters() -> tuple[str, int, dict]:
    """
    Получить список всех мастеров
    :return: json string: str, status code: int, headers: dict
    """
    try:
        masters = get_all_masters()
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(masters, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/masters/<int:master_id>", methods=["GET"])
def ep_get_master_by_id(master_id: int) -> tuple[str, int, dict]:
    """
    Получить информацию о мастере по ID
    :param master_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """

    try:
        master = get_master_by_id(master_id)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(master, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/masters", methods=["POST"])
def ep_add_master() -> tuple[str, int, dict]:
    """
    Добавить нового мастера
    :return: json string: str, status code: int, headers: dict
    """

    try:
        data = json.loads(str(request.json))
        added_master_id = add_master(data)
    except ValueError as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            400,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(
            {"success_msg": f"Мастер добавлен под ID: {added_master_id}"}, ensure_ascii=False
        ),
        201,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/masters/<int:master_id>", methods=["PUT"])
def ep_update_master(master_id: int) -> tuple[str, int, dict]:
    """
    Обновить информацию о мастере
    :param master_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """

    try:
        data = json.loads(str(request.json))
    except json.JSONDecodeError:
        return (
            json.dumps({"error": "Некорректные данные JSON"}, ensure_ascii=False),
            400,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    try:
        id_of_updated_master = update_master(master_id, data)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(
            {"success_msg": f"Данные мастера под ID {id_of_updated_master} обновлены"},
            ensure_ascii=False,
        ),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/masters/<int:master_id>", methods=["DELETE"])
def ep_delete_master(master_id: int) -> tuple[str, int, dict] | tuple[str, int]:
    """
    Удалить мастера
    :param master_id: int
    :return: status/error string: str, status code: int
    """

    try:
        delete_master(master_id)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return "", 204


@app.route("/appointments", methods=["GET"])
def ep_get_appointments() -> tuple[str, int, dict]:
    """
    Получить все записи на услуги с опциональной сортировкой
    :return: json string: str, status code: int, headers: dict
    """

    sort_by = request.args.get("sort_by")
    if not sort_by:
        sort_by = "id"
    direction = request.args.get("direction")
    if not direction:
        direction = "asc"

    try:
        appointments = get_all_appointments(sort_by, direction)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(appointments, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments/<int:appointment_id>", methods=["GET"])
def ep_get_appointment_by_id(appointment_id: int) -> tuple[str, int, dict]:
    """
    Получить информацию о записи по ID
    :param appointment_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """

    try:
        appointment = get_appointment_by_id(appointment_id)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(appointment, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments/master/<int:master_id>", methods=["GET"])
def ep_get_appointments_by_master(master_id: int) -> tuple[str, int, dict]:
    """
    Получить все записи для заданного мастера
    :param master_id: int
    :return: json string: str, status code: int, headers: dict
    """

    try:
        appointments = get_all_appointments_by_master(master_id)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(appointments, ensure_ascii=False),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments", methods=["POST"])
def ep_add_appointment() -> tuple[str, int, dict]:
    """
    Создать новую запись
    :return: json string: str, status code: int, headers: dict
    """

    try:
        data = json.loads(str(request.json))
    except json.JSONDecodeError:
        return (
            json.dumps({"error": "Некорректные данные JSON"}, ensure_ascii=False),
            400,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    try:
        appointment = add_appointment(data)
    except ValueError as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            400,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps({"success_msg": f"Запись добавлена под ID: {appointment}"}, ensure_ascii=False),
        201,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments/<int:appointment_id>", methods=["PUT"])
def ep_update_appointment(appointment_id: int) -> tuple[str, int, dict]:
    """
    Обновить запись
    :param appointment_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """

    try:
        data = json.loads(str(request.json))
    except json.JSONDecodeError:
        return (
            json.dumps({"error": "Некорректные данные JSON"}, ensure_ascii=False),
            400,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    try:
        id_of_updated_appointment = update_appointment(appointment_id, data)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )
    except ValueError as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            400,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return (
        json.dumps(
            {"success_msg": f"Данные записи под ID {id_of_updated_appointment} обновлены"},
            ensure_ascii=False,
        ),
        200,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.route("/appointments/<int:appointment_id>", methods=["DELETE"])
def ep_delete_appointment(appointment_id: int) -> tuple[str, int, dict] | tuple[str, int]:
    """
    Удалить запись
    :param appointment_id: int
    :return: status/error string: str, status code: int
    """

    try:
        delete_appointment(appointment_id)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return "", 204


@app.errorhandler(404)
def not_found_handler(e) -> tuple[str, int, dict]:
    """
    универсальный хендлер для несуществующих адресов
    """

    return (
        json.dumps({"'not found' fallback exception": str(e)}, ensure_ascii=False),
        404,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@app.errorhandler(Exception)
def fallback_handler(e) -> tuple[str, int, dict]:
    """
    вернёт краткие данные в json формате о необработанных исключениях
    """

    return (
        json.dumps({"fallback exception": str(e)}, ensure_ascii=False),
        500,
        {"Content-Type": "application/json; charset=utf-8"},
    )


def main():
    # Создание базы данных и таблиц если те не существуют
    if (not check_db_file_existance()) or (not check_tables_existance()):
        create_tables_and_populate()

    # перезапись бд в изначальное состояние для тестирования
    # remove_db_file()
    # create_tables_and_populate()

    # Запуск веб-сервера
    app.run(debug=True, host="127.0.0.1")


if __name__ == "__main__":
    main()
