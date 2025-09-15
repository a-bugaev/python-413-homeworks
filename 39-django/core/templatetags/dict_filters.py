"""
adds access to dict values
"""

from django import template

register = template.Library()


@register.filter
def get_item(dictionary_or_list: dict | list, key_or_index):
    """
    <dict_name or list_name>|get_item:<dict_key or list_index>
    """
    if isinstance(dictionary_or_list, list):
        return dictionary_or_list[key_or_index]
    if isinstance(dictionary_or_list, dict):
        return dictionary_or_list.get(key_or_index)

@register.filter
def get_by_id(list_of_dicts, id_):
    """
    <list_of_dicts>|get_by_id:<id>
    """
    for dict_ in list_of_dicts:
        if str(dict_["id"]) == str(id_):
            return dict_
