"""
returns hr value from choices field
"""

from django import template

register = template.Library()


@register.filter
def get_display(obj, field_name):
    """
    returns get_<stuff>_display() value from field
    """
    method_name = f"get_{field_name}_display"
    return getattr(obj, method_name)()
