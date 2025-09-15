"""
allows to show rating stars stars
"""

from django import template

register = template.Library()


@register.filter
def get_bool_list_from(actual_value, max_value):
    """
    returns get_<stuff>_display() value from field
    """
    return [num <= actual_value for num in range(1, max_value+1)]
