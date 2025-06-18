"""
hw_37/blueprints/routes/errorhandler.py
"""

import json
from flask import Blueprint

_errorhandler_bp = Blueprint("errorhandler", __name__)


@_errorhandler_bp.errorhandler(404)
def not_found_handler(e) -> tuple[str, int, dict]:
    """
    универсальный хендлер для несуществующих адресов
    """

    return (
        json.dumps({"'not found' fallback exception": str(e)}, ensure_ascii=False),
        404,
        {"Content-Type": "application/json; charset=utf-8"},
    )


@_errorhandler_bp.errorhandler(Exception)
def fallback_handler(e) -> tuple[str, int, dict]:
    """
    вернёт краткие данные в json формате о необработанных исключениях
    """

    return (
        json.dumps({"fallback exception": str(e)}, ensure_ascii=False),
        500,
        {"Content-Type": "application/json; charset=utf-8"},
    )

errorhandler_bp = _errorhandler_bp
