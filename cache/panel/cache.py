# coding=utf-8
from debug_toolbar.panels.cache import CacheDebugPanel


class RefreshCacheDebugPanel(CacheDebugPanel):
    """
    Panel that displays the cache statistics.
    """
    name = 'RCache'
    template = 'debug_toolbar/panels/cache_utils.html'
    has_content = True
