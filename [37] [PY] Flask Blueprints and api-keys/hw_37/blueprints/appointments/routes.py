"""
hw_37/blueprints/appointments/routes.py
"""

import json
from flask import Blueprint, request
from peewee import DoesNotExist
from hw_37.auth import auth_check
from .pw_actions import (
    get_all_appointments,
    get_appointment_by_id,
    get_all_appointments_by_master,
    add_appointment,
    update_appointment,
    delete_appointment,
)

appointments_bp = Blueprint("appointments", __name__, url_prefix="/appointments")


@appointments_bp.route("/", methods=["GET"])
def ep_get_appointments() -> tuple[str, int, dict]:
    """
    Получить все записи на услуги с опциональной сортировкой
    :return: json string: str, status code: int, headers: dict
    """

    auth_result = auth_check(request.headers.get("API-KEY"), request.endpoint)
    if auth_result is not True:
        return auth_result

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


@appointments_bp.route("/<int:appointment_id>", methods=["GET"])
def ep_get_appointment_by_id(appointment_id: int) -> tuple[str, int, dict]:
    """
    Получить информацию о записи по ID
    :param appointment_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """

    auth_result = auth_check(request.headers.get("API-KEY"), request.endpoint)
    if auth_result is not True:
        return auth_result

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


@appointments_bp.route("/master/<int:master_id>", methods=["GET"])
def ep_get_appointments_by_master(master_id: int) -> tuple[str, int, dict]:
    """
    Получить все записи для заданного мастера
    :param master_id: int
    :return: json string: str, status code: int, headers: dict
    """

    auth_result = auth_check(request.headers.get("API-KEY"), request.endpoint)
    if auth_result is not True:
        return auth_result

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


@appointments_bp.route("/", methods=["POST"])
def ep_add_appointment() -> tuple[str, int, dict]:
    """
    Создать новую запись
    :return: json string: str, status code: int, headers: dict
    """

    auth_result = auth_check(request.headers.get("API-KEY"), request.endpoint)
    if auth_result is not True:
        return auth_result

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


@appointments_bp.route("/<int:appointment_id>", methods=["PUT"])
def ep_update_appointment(appointment_id: int) -> tuple[str, int, dict]:
    """
    Обновить запись
    :param appointment_id: int
    :return: json string: str, status code: int, headers: dict | error text: str, status code: int
    """

    auth_result = auth_check(request.headers.get("API-KEY"), request.endpoint)
    if auth_result is not True:
        return auth_result

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


@appointments_bp.route("/<int:appointment_id>", methods=["DELETE"])
def ep_delete_appointment(appointment_id: int) -> tuple[str, int, dict] | tuple[str, int]:
    """
    Удалить запись
    :param appointment_id: int
    :return: status/error string: str, status code: int
    """

    auth_result = auth_check(request.headers.get("API-KEY"), request.endpoint)
    if auth_result is not True:
        return auth_result

    try:
        delete_appointment(appointment_id)
    except DoesNotExist as e:
        return (
            json.dumps({"error": str(e)}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return "", 204


@appointments_bp.errorhandler(404)
def not_found_handler(e) -> tuple[str, int, dict]:
    """
    универсальный хендлер для несуществующих адресов
    """

    return (
        json.dumps({"'not found' fallback exception": str(e)}, ensure_ascii=False),
        404,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@appointments_bp.errorhandler(Exception)
def fallback_handler(e) -> tuple[str, int, dict]:
    """
    вернёт краткие данные в json формате о необработанных исключениях
    """

    return (
        json.dumps({"fallback exception": str(e)}, ensure_ascii=False),
        500,
        {"Content-Type": "application/json; charset=utf-8"},
    )
