# coding=utf-8
from django.utils.translation import ugettext_lazy as _

def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_active.short_description = _("Mark selected categories as active")


def make_not_active(modeladmin, request, queryset):
    queryset.update(is_active=False)
make_not_active.short_description = _("Mark selected categories as not active")
