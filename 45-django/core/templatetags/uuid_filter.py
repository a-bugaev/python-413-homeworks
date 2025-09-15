"""
уникальный идентификатор
"""

import uuid
from django import template

register = template.Library()

@register.filter
def get_uuid(_):
    """
    ""|get_uuid
    """
    return str(uuid.uuid4().hex)
