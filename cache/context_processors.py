# coding=utf-8
from django.conf import settings


def timeout(request):
    return {
        'CACHE_TIMEOUT': getattr(settings, 'CACHE_TIMEOUT_TEMPLATE', 60 * 60)
    }
