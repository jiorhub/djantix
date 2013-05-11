# coding=utf-8
from django.core.cache import cache
from django.contrib import messages
from djantix.shortcuts import redirect_to_back
from django.utils.translation import ugettext_lazy as _


def refresh(request):
    if request.user.is_superuser:
        cache.clear()
        messages.success(request, _('The cache is updated'))
    else:
        messages.error(request, _('Access denied'))
    return redirect_to_back(request)
