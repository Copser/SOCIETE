# blog/signals.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import ApplyFormModel


@receiver(post_save, sender=ApplyFormModel)
def inform_administrations(sender, **kwargs):
    """TODO: Buidling email signal system which needs to
    warn administration every time when are user apply for
    a posted job
    return: TODO
    """
    from django.core.mail import mail_admins
    instance = kwargs["instance"]
    created = kwargs["created"]
    if created:
        context = {
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
        }
        plain_text_message = """
        A new applicant "%(first_name)s","%(last_name)s", "%(email)s", has applied for
        one of posted jobs.
        You can preview it at administration.""" % context
        html_message = """
        <p>A new apply form superjobs was created by "%(first_name)s", "%(last_name)s", "%(email)s"</p>
        <p>Check the administration.</p>""" % context

        mail_admins(
            subject="New Job Form was Added at superjobs.com",
            message=plain_text_message,
            html_message=html_message,
            fail_silently=True,
        )
