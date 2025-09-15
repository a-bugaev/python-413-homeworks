"""
allows iterate through simple numbers
"""

from django import template

register = template.Library()


@register.filter
def range_0(num_value):
    """
    returns list [0, 1, 2, . . . , num_value] (including)
    """
    return [range(0, num_value + 1)]


@register.filter
def range_1(num_value):
    """
    returns list [1, 2, . . . , num_value] (including)
    """
    return [num for num in range(1, num_value + 1)]
