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
            "title": instance.title,
            "link": instance.get_ur(),
        }
        plain_text_message = """
        A new Form for for "%(title)s" has been created.
        You can preview it at %(link)s.""" % context
        html_message = """
        <p>A new viral video called "%(title)s" has beed created.</p>
        <p>You can priview it <a href="%(link)s">here</a></p>""" % context

        mail_admin(
            subject="New Job Form was Added at superjobs.com",
            message=plain_text_message,
            html_message=html_message,
            fail_silently=True,
        )
