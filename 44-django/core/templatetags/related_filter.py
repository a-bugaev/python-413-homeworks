"""
adds access to related objects
"""

from django import template

register = template.Library()


@register.filter
def get_all(field_with_relations):
    """
    Model.related_things_field|get_all
    """
    return field_with_relations.all()
