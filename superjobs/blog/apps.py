# blog/apps.py
# -*- UTF-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ApplyFormModelAppConfig(AppConfig):
    name = "blog"
    verbose_name = _("Apply Form")

    def ready(self):
        from .signals import inform_administrations
        from .checks import setings_check
