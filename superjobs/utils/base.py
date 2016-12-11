# utils/base.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import urlparse
from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings


class UrlMixin(models.Model):
    """TODO: A replacement for get_absoulte_url()
    Models extending this mixin ashould have either
    get_url or get_url_path implemented.
    return: TODO
    """
    class Meta:
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = selg.get_url_path()
        except NotImplementedError:
            raise
        website_url = getattr(
            settings, "DEFAULT_WEBSITE_URL",
            "http://127.0.0.0.1:8000"
        )
        return website_url + path
    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        except NotImplementedError:
            raise
        bits = urlparse.urlparse(url)
        return urlparse.urlunparse(("", "") + bits[2:])
    get_url_path.dont_recurse = True

    def get_absolut_url(self):
        return self.get_url_path()
