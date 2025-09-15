"""
создаёт праильные строки для различных лет
"""

from datetime import datetime
from django import template

register = template.Library()


@register.filter
def get_year_form(year):
    """
    создаёт праильные строки для различных лет
    """
    if year == 1:
        return f"{year} год"
    elif 2 <= year % 10 <= 4 and not 12 <= year % 100 <= 14:
        return f"{year} года"
    else:
        return f"{year} лет"


@register.filter
def local_format(datetime_field: datetime):
    """
    Привычный локальный формат даты и времени
    """
    return datetime_field.strftime("%Y-%m-%d %H:%M:%S")
