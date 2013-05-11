# coding=utf-8
from django import template
"""
Template tags for working with lists.

You'll use these in templates thusly::

    {% load listutil %}
    {% for sublist in mylist|parition:"3" %}
        {% for item in mylist %}
            do something with {{ item }}
        {% endfor %}
    {% endfor %}
"""

register = template.Library()


@register.filter
def partition(thelist, n):
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = len(thelist) / n
    return [thelist[p * i:p * (i + 1)] for i in range(n - 1)] + [thelist[p * (i + 1):]]


@register.filter
def partition_horizontal(thelist, n):
    try:
        n = float(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = int(round(len(thelist) / n))
    return [thelist[i::p] for i in range(p)]
