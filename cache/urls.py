# coding=utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('cache_utils.views',
    url(r'^refresh', 'refresh', name='refresh'),
)
