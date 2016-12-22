# blog/checks.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.core.checks import Warning, register, Tags


@register(Tags.compatibility)
def setings_check(app_configs, **kwargs):
    from django.conf import settings
    errors = []
    if not settings.ADMINS:
        errors.append(
            Warning(
            """The system admins are not set in the project
        settings""",
            hint="""In order to receive notifications when new apply forms
        are created, define system admins like ADMIN(("Admin", "example@example.com"),)
        in your settings""",
            id="blog.F001",
        )
    )
    return errors
