"""
WSGI config for societe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from django.core.cache.backends.memcached import BaseMemcachedCache
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "societe.settings")
BaseMemcachedCache.close = lambda self, **kwargs: None
application = Cling(get_wsgi_application())
