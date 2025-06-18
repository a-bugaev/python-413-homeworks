"""
hw_37/blueprints/masters/routes.py
"""

import json
from flask import Blueprint, request
from peewee import DoesNotExist
from .pw_actions import (
    get_all_masters,
    get_master_by_id,
    add_master,
    update_master,
    delete_master,
)

masters_bp = Blueprint("masters", __name__, url_prefix="/masters")


@masters_bp.route("/masters", methods=["GET"])
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


@masters_bp.route("/masters/<int:master_id>", methods=["GET"])
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


@masters_bp.route("/masters", methods=["POST"])
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


@masters_bp.route("/masters/<int:master_id>", methods=["PUT"])
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


@masters_bp.route("/masters/<int:master_id>", methods=["DELETE"])
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

@masters_bp.errorhandler(404)
def not_found_handler(e) -> tuple[str, int, dict]:
    """
    универсальный хендлер для несуществующих адресов
    """

    return (
        json.dumps({"'not found' fallback exception": str(e)}, ensure_ascii=False),
        404,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@masters_bp.errorhandler(Exception)
def fallback_handler(e) -> tuple[str, int, dict]:
    """
    вернёт краткие данные в json формате о необработанных исключениях
    """

    return (
        json.dumps({"fallback exception": str(e)}, ensure_ascii=False),
        500,
        {"Content-Type": "application/json; charset=utf-8"},
    )
