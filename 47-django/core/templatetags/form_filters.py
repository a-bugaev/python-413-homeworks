"""
get queryset from field
"""

from django import template

register = template.Library()


@register.filter
def get_all(field_with_relations):
    """
    Model.related_things_field|get_all
    """
    return field_with_relations.all()


@register.filter
def get_field_queryset(form, form_field_name):
    """
    form.fields['key'].queryset -> form.get_field_queryset|form_field_name
    """
    return list(form.fields[form_field_name].queryset)


@register.filter
def get_errors_for_field(form, form_field_name):
    """
    form.fields['key'].queryset -> form.get_field_queryset|form_field_name
    """
    return [str(err_obj) for err_obj in form.errors[form_field_name]]


@register.filter
def get_non_field_errors(form):
    """
    form.non_field_errors() -> form|get_non_field_errors
    """
    return [str(err_obj) for err_obj in form.non_field_errors]
