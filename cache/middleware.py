# coding=utf-8
from django.core.cache import cache


class CacheRefreshMiddleware:
    def process_request(self, request):
        if 'refresh' in request.GET:
            cache.clear()
