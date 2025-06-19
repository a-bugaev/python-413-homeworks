"""
hw_37/auth.py
api key authentication
"""

import json
from typing import Literal

USERS = [
    {
        "name": "admin_name",
        "API_KEY": "uUXf(pvDD)*Qkj(Js@puV9vVAHwst9Ry",
        "role": "admin",
    },
    {"name": "user_name", "API_KEY": "x4Y_%$b7z(Mvec_anrK82^vyTy^)8TvS", "role": "user"},
]

ACCESS_TABLE = [
    {
        "endpoint": "masters.ep_get_masters",
        "admin": True,
        "user": True,
    },
    {
        "endpoint": "masters.ep_get_master_by_id",
        "admin": True,
        "user": True,
    },
    {
        "endpoint": "masters.ep_add_master",
        "admin": True,
        "user": False,
    },
    {
        "endpoint": "masters.ep_update_master",
        "admin": True,
        "user": False,
    },
    {
        "endpoint": "masters.ep_delete_master",
        "admin": True,
        "user": False,
    },
    {
        "endpoint": "appointment.ep_get_appointments",
        "admin": True,
        "user": True,
    },
    {
        "endpoint": "appointment.ep_get_appointment_by_id",
        "admin": True,
        "user": True,
    },
    {
        "endpoint": "appointment.ep_get_appointments_by_master",
        "admin": True,
        "user": True,
    },
    {
        "endpoint": "appointment.ep_add_appointment",
        "admin": True,
        "user": False,
    },
    {
        "endpoint": "appointment.ep_update_appointment",
        "admin": True,
        "user": False,
    },
    {
        "endpoint": "appointment.ep_delete_appointment",
        "admin": True,
        "user": False,
    },
]


def is_valid_api_key(api_key):
    """
    Проверяет, является ли ключ API действительным
    """
    return any(user["API_KEY"] == api_key for user in USERS)


def is_admin(api_key):
    """
    Проверяет, имеет ли пользователь с данным ключом API права администратора
    """
    return any(user["API_KEY"] == api_key and user["role"] == "admin" for user in USERS)


def get_access_rules(endpoint: str) -> dict | None:
    """
    Возвращает правила доступа для указанного пути и метода из ACCESS_TABLE
    """
    for rule in ACCESS_TABLE:
        if rule["endpoint"] == endpoint:
            return {
                "admin": rule["admin"],
                "user": rule["user"],
            }
    return None


def auth_check(api_key: str | None, endpoint: str | None) -> Literal[True] | tuple:
    """
    Проверяет, имеет ли пользователь с данным ключом API права на выполнение запроса
    """

    if api_key is None:
        return (
            json.dumps({"Unauthorized": "API key is required"}, ensure_ascii=False),
            401,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    if endpoint is None:
        return (
            json.dumps({"error": "Endpoint not found"}, ensure_ascii=False),
            404,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    api_key_belongs_to_admin = is_admin(api_key)
    if api_key_belongs_to_admin:
        return True

    api_key_is_valid = is_valid_api_key(api_key)
    if not api_key_is_valid:
        return (
            json.dumps({"Unauthorized": "invalid api key"}, ensure_ascii=False),
            401,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    access_rules = get_access_rules(endpoint)
    if not access_rules:
        return (
            json.dumps({"Unauthorized": "no access rules found"}, ensure_ascii=False),
            401,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    if not api_key_belongs_to_admin == access_rules["admin"]:
        return (
            json.dumps({"Forbidden": "only admin access is allowed"}, ensure_ascii=False),
            403,
            {"Content-Type": "application/json; charset=utf-8"},
        )

    return True
