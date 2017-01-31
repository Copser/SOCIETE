"""
WSGI config for superjobs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from dj_static import Cling, MediaCling
from django.core.wsgi import get_wsgi_application
from django.core.cache.backends.memcached import BaseMemcachedCache


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superjobs.settings")
# Fix django closing connection to MemCachier after every request
BaseMemcachedCache.close = lambda self, **kwargs: None
application = Cling(MediaCling(get_wsgi_application()))
