# coding=utf-8
from django import template

register = template.Library()

@register.filter
def multi(value, arg):
    return value * arg