# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter
def weight_display(value, unit):
    """
    Display a weight value in the user's preferred unit.
    :param value: the weight as a float (stored in the user's unit)
    :param unit: 'kg' or 'lb'
    :returns: formatted string with unit label
    """
    if value is None:
        return ""
    try:
        value = float(value)
    except (TypeError, ValueError):
        return str(value)
    if unit == "lb":
        total_oz = round(value * 16)
        lbs = total_oz // 16
        oz = total_oz % 16
        if oz == 0:
            return f"{lbs} lbs"
        return f"{lbs} lbs {oz} oz"
    return f"{value:g} kg"


@register.filter
def next(some_list, current_index):
    """
    Returns the element at the next index of the zero-indexed list
    :param some_list: a list
    :param current_index: the current index to increment
    :returns: the element at the next index or an empty string
    """
    if not some_list or current_index >= len(some_list) - 1:
        return ""
    return some_list[current_index + 1]


@register.filter
def prev(some_list, current_index):
    """
    Returns the element at the previous index of the zero-indexed list
    :param some_list: a list
    :param current_index: the current index to decrement
    :returns: the element at the previous index or an empty string
    """
    if not some_list or current_index <= 0:
        return ""
    return some_list[current_index - 1]
